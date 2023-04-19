
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field
from torch.utils.data import Dataset
from typing import Any
DataSet = Dataset
NoneType = Any
Grepo = Any
Gmodel = Any
Model = Any


@op(config_schema={"epoch": Field(int, default_value=100, description="训练epoch"),
                    "lr": Field(float, default_value=0.001, description="学习率"),
                    "label": Field(str, default_value='', description="标签列"),
                    "label_mask": Field(list, default_value=[], description="有效标签范围"),
                    "features": Field(list, default_value=[], description="特征列"),
                    "layers": Field(list, default_value=[50], description="隐藏层节点数"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def grepo_sage_model(context, in0_grepo: Grepo)->Any:   
    '''图算法组件      
    :param in0_grepo: 输入图数据集      
    :return out0_gmodel: 输出图模型         
    '''    
    return None  
    

@op(config_schema={"epoch": Field(int, default_value=100, description="训练epoch"),
                    "lr": Field(float, default_value=0.001, description="学习率"),
                    "label": Field(list, default_value=[], description="标签列"),
                    "label_mask": Field(list, default_value=[], description="有效标签范围"),
                    "features": Field(list, default_value=[], description="特征列"),
                    "layers": Field(list, default_value=[50], description="隐藏层节点数"),
                    "edge_list": Field(list, default_value=[], description="指定边类型"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def grepo_rgcn_model(context, in0_grepo: Grepo)->Any:   
    '''图算法组件      
    :param in0_grepo: 输入图数据集      
    :return out0_gmodel: 输出图模型         
    '''    
    return None  
    

@op(config_schema={"epoch": Field(int, default_value=100, description="训练epoch"),
                    "lr": Field(float, default_value=0.001, description="学习率"),
                    "label": Field(list, default_value=[], description="标签列"),
                    "label_mask": Field(list, default_value=[], description="有效标签范围"),
                    "features": Field(list, default_value=[], description="特征列"),
                    "layers": Field(list, default_value=[50], description="隐藏层节点数"),
                    "edge_list": Field(list, default_value=[], description="指定边类型"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def grepo_rsage_model(context, in0_grepo: Grepo)->Any:   
    '''图算法组件      
    :param in0_grepo: 输入图数据集      
    :return out0_gmodel: 输出图模型         
    '''    
    return None  
    


    

@op(config_schema={"graph": Field(dict, default_value={}, description="因果图"),
                    "do": Field(list, default_value=[], description="干预节点"),
                    "evidence": Field(list, default_value=[], description="证据节点"),
                    "variables": Field(list, default_value=[], description="查询节点")})
def CausalInference(context, in0_dataset: DataSet)->Any:   
    '''图算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    