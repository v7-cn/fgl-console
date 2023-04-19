      
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
from torch_geometric_temporal.nn.recurrent import EvolveGCNH
from libs.utils import summary_model

# from libs.utils import _fetch_default_params
def _fetch_default_params(trial):
    return {'optim': trial.suggest_categorical('optim', ['Adam', 'SGD']),
            'lr': trial.suggest_float('lr', 1e-20, 1e-1),
            'weight_decay': trial.suggest_float('weight_decay', 1e-20, 1e-3)
            }
     
class RecurrentGCN(torch.nn.Module):
    def __init__(self, node_count, node_features, out_channels=1):
        super(RecurrentGCN, self).__init__()
        self.recurrent = EvolveGCNH(node_count, node_features)
        self.linear = torch.nn.Linear(node_features, out_channels)

    def forward(self, x, edge_index, edge_weight):
        h = self.recurrent(x, edge_index, edge_weight)
        h = F.relu(h)
        h = self.linear(h)
        return h   
        
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
def grepo_egcn_model(context, dataset)->Any:   
    '''图算法组件      
    :param in0_grepo: 输入图数据集      
    :return out0_gmodel: 输出图模型         
    '''    
    
    epoch = context.op_config.get('epoch', None)
    def train_model(trial):
        params = _fetch_default_params(trial)
        optim = getattr(torch.optim, params.get('optim', None))
        lr = params.get('lr', None)
        weight_decay = params.get('weight_decay', None)
        
        
        model = RecurrentGCN(node_features = 4, node_count = 20)
        optimizer = optim(model.parameters(), lr=weight_decay, weight_decay=weight_decay)
        model.train()
        tbar = tqdm(range(epoch))
        for e in tbar:
            cost = 0
            for time, snapshot in enumerate(dataset):
                y_hat = model(snapshot.x, snapshot.edge_index, snapshot.edge_attr)
                cost = cost + torch.mean((y_hat-snapshot.y)**2)
            cost = cost / (time+1)
            tbar.set_postfix(loss=cost.item())
            cost.backward()
            optimizer.step()
            optimizer.zero_grad()
        trial.set_user_attr('model', model)
        trial.set_user_attr('eval', {"模型评估":{
            'MSE值':cost.item()
        }})
        return cost.item()
    # find best model
    study = optuna.create_study(direction="minimize", pruner=optuna.pruners.NopPruner())
    if not context.op_config.get('automl', False):
        study.enqueue_trial({
            "lr": context.op_config.get('lr', None),
            "weight_decay":context.op_config.get('weight_decay', None),
            "optim":context.op_config.get('optim', None),
            }
        )
        study.optimize(train_model, n_jobs=1, n_trials=1)
    else:
        study = optuna.create_study(direction="minimize")
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
def ml_eval_regressor(context, state_dict:Any, dataset:Any)->float:
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
        model = RecurrentGCN(node_features = 4, node_count = 20)
        model.load_state_dict(state_dict)
    y_hats = []
    cost = 0
    for time, snapshot in enumerate(dataset):
        y_hat = model(snapshot.x, snapshot.edge_index, snapshot.edge_attr)
        cost = cost + torch.mean((y_hat-snapshot.y)**2)
        y_hats.append(y_hat.flatten().detach().numpy())
    cost = cost / (time+1)
    outputpath = context.op_config.get('output', None)
    if outputpath:
        open(outputpath, "w").write("\n".join([f"{i}|{str(y_hat.tolist())}" for i, y_hat in enumerate(y_hats)]))
    return cost.item()
