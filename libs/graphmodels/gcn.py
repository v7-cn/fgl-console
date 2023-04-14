import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch.utils.data import Dataset
import numpy as np
from dagster import AssetMaterialization   
from tqdm import tqdm
import typing
from typing import Any


def summary_model(model):
    params = []
    params_collect = []
    for k,p in model.named_parameters():
        params.append(np.prod(p.shape).item())
        params_collect.append("{:>20} {:>20} {:>30} {:>20}".format(str(k), str(p.dtype), str(p.shape), str(np.prod(p.shape))))    
    return {'模型结构':str(model).split("\n"),
    '模型参数量': params_collect,
    "总参数量": sum(params)}
    
    
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
        

    

@op(config_schema={"name":Field(str, default_value='Cora', is_required=False, description="数据集名称")})
def graphrepo(context)->Dataset:
    '''图数据集资产     
    :param name: 数据集名称    
    :return state_dict: 模型参数      
    '''
    from torch_geometric.datasets import Planetoid
    return Planetoid(root='./', name=context.op_config.get('name', None))


@op(config_schema={"epoch":Field(int, default_value=500, is_required=False, description="训练轮数"),
                   "lr":Field(float, default_value=0.001, is_required=False, description="学习率"),
                   "layers":Field(list, default_value=[3,3,3], is_required=False, description="卷积层数"),
                   "automl":Field(bool, default_value=False, is_required=False, description="automl"),
                   "automl_trials":Field(int, default_value=4, is_required=False, description="automl实验次数"),
                   "features":Field(typing.Any, default_value=[], is_required=False, description="特征列表"),
                   "label":Field(str, default_value='asfd', is_required=False, description="标签列"),
                   "label_mask":Field(list, default_value=[], is_required=False, description="是否对label遮挡")})
def grepo_gcn_model(context, dataset:Dataset)->dict:
    '''训练模型    
    :param dataset: 数据集      
    :param epoch: 训练轮数      
    :return state_dict: 模型参数     
    '''  
    epoch = context.op_config.get('epoch', None)
    lr = 0.01
    weight_decay=5e-4
    optim = 'Adam'
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = GCN(dataset.num_node_features, dataset.num_classes).to(device)
    data = dataset[0].to(device)
    optimizer = getattr(torch.optim, optim)(model.parameters(), lr=lr, weight_decay=weight_decay)

    model.train()
    for e in tqdm(range(epoch)):
        optimizer.zero_grad()
        out = model(data)
        loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
        loss.backward()
        optimizer.step()
    metadata = {'epoch': epoch,
                'lr': lr,
                'optim': optim,
                'device': device.type}
    metadata.update(summary_model(model))
    
    try:
        from sklearn import metrics 
        y_true, y_pred = data.y.cpu().detach().numpy(), out.cpu().detach().numpy().argmax(axis=1)
        metadata.update({"模型评估":{
            'F值':metrics.f1_score(y_true, y_pred, average='macro'),
            '准确度':metrics.accuracy_score(y_true, y_pred),
            '召回率':metrics.recall_score(y_true, y_pred, average='macro'),
            '精准度': metrics.precision_score(y_true, y_pred, average='macro')
        }})
    except:
        ...

    context.log_event(
        AssetMaterialization(
            asset_key="rgnn_model", description="Persisted result to storage", metadata=metadata
        )
    )
    return model.state_dict()
    
@op
def grepo_model_predict(context, state_dict:dict, dataset:Dataset)->np.ndarray:
    '''评估预测  
    :param state_dict: 模型参数  
    :param dataset: 测试数据集  
    :return acc: 预测准确度  
    '''
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = GCN(dataset.num_node_features, dataset.num_classes).to(device)
    model.load_state_dict(state_dict)
    data = dataset[0].to(device)
    pred = model(data).argmax(dim=1)
    correct = (pred[data.test_mask] == data.y[data.test_mask]).sum()
    acc = int(correct) / int(data.test_mask.sum())
    
    return pred.detach().cpu().numpy()


@op
def grepo_eval_2_classify(dataset, y)->int:
    '''图模型二分类评估  
    :param dataset: 数据集  
    :return y: 预测标签  
    '''
    return sum(y).item() - sum(dataset[0].y).item()
