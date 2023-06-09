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
from libs.utils import summary_model

 
def _fetch_default_params(trial):
    return {'optim': trial.suggest_categorical('optim', ['Adam', 'SGD']),
            'lr': trial.suggest_float('lr', 1e-20, 1e-1),
            'weight_decay': trial.suggest_float('weight_decay', 1e-20, 1e-3)
            }
           
    
class GCN(torch.nn.Module):
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
            return F.log_softmax(x, dim=1)
        


@op(config_schema={"epoch":Field(int, default_value=500, is_required=False, description="训练轮数"),
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
def grepo_gcn_model(context, dataset:Dataset)->dict:
    '''训练模型    
    :param dataset: 数据集      
    :param epoch: 训练轮数      
    :return state_dict: 模型参数     
    '''  
    epoch = context.op_config.get('epoch', None)
    # model train
    def train_model(trial):
        params = _fetch_default_params(trial)
        optim = getattr(torch.optim, params.get('optim', None))
        lr = params.get('lr', None)
        weight_decay = params.get('weight_decay', None)
        
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = GCN(dataset.num_node_features, dataset.num_classes).to(device)
        data = dataset[0].to(device)
        optimizer = optim(model.parameters(), lr=lr, weight_decay=weight_decay)

        model.train()
        for e in tqdm(range(epoch)):
            optimizer.zero_grad()
            out = model(data)
            loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
            trial.report(loss.item(), e)
            if trial.should_prune():
                raise optuna.TrialPruned()
            loss.backward()
            optimizer.step()
            
        y_true, y_pred = data.y.cpu().detach().numpy(), out.cpu().detach().numpy().argmax(axis=1)
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
            asset_key="rgnn_model", description="Persisted result to storage", metadata=metadata
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
def grepo_model_predict(context, state_dict:Any, dataset:Dataset)->np.ndarray:
    '''评估预测  
    :param state_dict: 模型参数  
    :param dataset: 测试数据集  
    :return acc: 预测准确度  
    '''
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    modelpath = context.op_config.get('model', None)
    if modelpath:
        model = torch.load(f"{modelpath}/model.pth")
    else:
        model = GCN(dataset.num_node_features, dataset.num_classes).to(device)
        model.load_state_dict(state_dict)
        
    data = dataset[0].to(device)
    pred = model(data).argmax(dim=1)
    correct = (pred[data.test_mask] == data.y[data.test_mask]).sum()
    acc = int(correct) / int(data.test_mask.sum())
    outputpath = context.op_config.get('output', None)
    if outputpath:
        open(outputpath, "w").write("\n".join([f"{i},{p}" for i, p in enumerate(pred.tolist())]))
    return pred.detach().cpu().numpy()


@op
def grepo_eval_2_classify(dataset, y)->int:
    '''图模型二分类评估  
    :param dataset: 数据集  
    :return y: 预测标签  
    '''
    return sum(y).item() - sum(dataset[0].y).item()


