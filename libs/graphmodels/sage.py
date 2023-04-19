      
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field, In
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch.utils.data import Dataset
import numpy as np
from dagster import AssetMaterialization   
from tqdm import tqdm
import typing
from typing import Any
import optuna
from copy import deepcopy
from sklearn import metrics
from tabulate import tabulate
from torch_geometric.utils import negative_sampling
from torch_geometric.nn import GCNConv
import torch
import torch.nn.functional as F
from libs.utils import summary_model


def _fetch_default_params(trial):
    return {'optim': trial.suggest_categorical('optim', ['Adam', 'SGD']),
            'lr': trial.suggest_float('lr', 1e-20, 1e-1),
            'weight_decay': trial.suggest_float('weight_decay', 1e-20, 1e-3)
            }
        
        
class EmbeddingGCN(torch.nn.Module):
        def __init__(self, num_node_features, num_classes):
            super().__init__()
            self.conv1 = GCNConv(num_node_features, 16)
            self.conv2 = GCNConv(16, num_classes)

        def forward(self, data):
            x, edge_index = data.x, data.edge_index
            x = self.conv1(x, edge_index)
            x = F.relu(x)
            x = F.dropout(x, training=self.training)
            x = self.conv2(x, edge_index)
            return x
        
        
@op(config_schema={"metapath": Field(list, default_value=[], description="正样本路径"),
                    "neg_metapath": Field(list, default_value=[], description="负样本路径"),
                    "epoch":Field(int, default_value=500, is_required=False, description="训练轮数"),
                   "lr":Field(float, default_value=0.001, is_required=False, description="学习率"),
                   "optim":Field(str, default_value='Adam', is_required=False, description="优化器"),
                   "weight_decay":Field(float, default_value=1e-20, is_required=False, description="正则"),
                   "layers":Field(list, default_value=[3,3,3], is_required=False, description="卷积层数"),
                   "automl":Field(bool, default_value=False, is_required=False, description="automl"),
                   "automl_trials":Field(int, default_value=4, is_required=False, description="automl实验次数"),
                   "features":Field(typing.Any, default_value=[], is_required=False, description="特征列表"),
                   "label":Field(str, default_value='', is_required=False, description="标签列"),
                   "label_mask":Field(list, default_value=[], is_required=False, description="是否对label遮挡"),
                   "output":Field(str, default_value='', is_required=False, description="模型输出路径")
                   })
def grepo_recommend_model(context, dataset: Dataset)->Any:   
    '''图算法组件      
    :param in0_grepo: 输入图数据集      
    :return out0_gmodel: 输出图模型         
    '''    
    epoch = context.op_config.get('epoch', None)
    def train_model(trial):
        params = _fetch_default_params(trial)
        lr = params.get('lr', None)
        weight_decay = params.get('weight_decay', None)
        
        data = dataset[0]
        pos_edges = data.edge_index
        neg_edges = negative_sampling(edge_index=data.edge_index, 
                        num_nodes=data.x.shape[0], 
                        num_neg_samples=data.edge_index.shape[1])
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = EmbeddingGCN(dataset.num_node_features, dataset.num_classes).to(device)
        data.to(device)
        
        from tqdm import tqdm
        from torch import optim
        tbar = tqdm(range(epoch))
        optimizer = getattr(torch.optim, params.get('optim', None))(model.parameters(), lr=lr, weight_decay=weight_decay)
        for e in tbar:
            embeddings = model(data)
            pos_loss = F.cosine_embedding_loss(embeddings[pos_edges[0]], embeddings[pos_edges[1]], torch.ones(pos_edges.shape[1]).to(device))
            neg_loss = F.cosine_embedding_loss(embeddings[neg_edges[0]], embeddings[neg_edges[1]], torch.zeros(neg_edges.shape[1]).to(device))
            loss = pos_loss + neg_loss
            tbar.set_postfix(loss=loss.item())
            optimizer.zero_grad()
            trial.report(loss.item(), e)
            if trial.should_prune():
                raise optuna.TrialPruned()
            loss.backward()
            optimizer.step()
        embeddings = model(data)
        y_pred = torch.concat([(embeddings[pos_edges[0]] * embeddings[pos_edges[1]]).sum(axis=1),
                              (embeddings[neg_edges[0]] * embeddings[neg_edges[1]]).sum(axis=1)]).detach().cpu().numpy() > 0.5
        y_true = torch.concat([torch.ones(pos_edges.shape[1]).to(device),
                               torch.zeros(neg_edges.shape[1]).to(device)]).detach().cpu().numpy()
        trial.set_user_attr('model', model)
        trial.set_user_attr('eval', {"模型评估":{
            'F值':metrics.f1_score(y_true, y_pred, average='macro'),
            '准确度':metrics.accuracy_score(y_true, y_pred),
            '召回率':metrics.recall_score(y_true, y_pred, average='macro'),
            '精准度': metrics.precision_score(y_true, y_pred, average='macro')
        }})
        f1 = metrics.f1_score(y_true, y_pred, average='macro')
        return f1
    
    # find best model
    study = optuna.create_study(direction="maximize", pruner=optuna.pruners.NopPruner())
    if not context.op_config.get('automl', False):
        study.enqueue_trial({
            "lr": context.op_config.get('lr', None),
            "weight_decay":context.op_config.get('weight_decay', None),
            "optim":context.op_config.get('optim', None),
            }
        )
        study.optimize(train_model, n_jobs=1, n_trials=1)
    else:
        study = optuna.create_study(direction="maximize")
        study.optimize(train_model, n_jobs=1, n_trials=context.op_config.get('automl_trials', None))
    model = study.best_trial.user_attrs['model']
    # dump best model
    metadata = deepcopy(study.best_params)
    metadata.update(summary_model(model))
    metadata.update(study.best_trial.user_attrs['eval'])

    context.log_event(
        AssetMaterialization(
            asset_key="sage_model", description="Persisted result to storage", metadata=metadata
        )
    )
    
    # display
    from tabulate import tabulate
    import pandas as pd
    stat = study.trials_dataframe().set_index("number")
    stat.loc[study.best_trial.number, 'state'] = '<BEST>'
    tb = tabulate(stat, headers='keys', tablefmt='grid')
    print(tb)
    
    # output
    output = context.op_config.get('output', None)
    if output:
        import os
        import json
        os.makedirs(output, exist_ok=True)
        torch.save(model, f"{output}/model.pth")
        open(f"{output}/reporter.json", "w").write(json.dumps(metadata, indent=4, ensure_ascii=False))
        open(f"{output}/trials.txt", "w").write(tb)
    return model.state_dict() 



@op(config_schema={"model":Field(str, is_required=False, description="模型输出路径"),
                   "output":Field(str, is_required=False, description="预测结果输出路径")})
def grepo_recommend_predict(context, state_dict:Any, dataset:Dataset)->Any:   
    '''预测组件      
    :param state_dict: 输入图模型      
    :param dataset: 输入图数据集      
    '''  
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    modelpath = context.op_config.get('model', None)
    if modelpath:
        model = torch.load(f"{modelpath}/model.pth")
    else:
        model = model = EmbeddingGCN(dataset.num_node_features, dataset.num_classes).to(device)
        model.load_state_dict(state_dict)
        
    data = dataset[0].to(device)
    pos_edges = data.edge_index
    neg_edges = negative_sampling(edge_index=data.edge_index, 
                num_nodes=data.x.shape[0], 
                num_neg_samples=data.edge_index.shape[1])
    embeddings = model(data)

    y_pred = torch.concat([(embeddings[pos_edges[0]] * embeddings[pos_edges[1]]).sum(axis=1),
                            (embeddings[neg_edges[0]] * embeddings[neg_edges[1]]).sum(axis=1)]).detach().cpu().numpy() > 0.5
    y_true = torch.concat([torch.ones(pos_edges.shape[1]).to(device),
                            torch.zeros(neg_edges.shape[1]).to(device)]).detach().cpu().numpy()
    f1 = metrics.f1_score(y_true, y_pred, average='macro')
    
    outputpath = context.op_config.get('output', None)
    if outputpath:
        import pandas as pd
        pd.DataFrame(embeddings.detach().cpu().numpy().tolist()).to_csv(outputpath, index=None, header=None)
    return f1
    