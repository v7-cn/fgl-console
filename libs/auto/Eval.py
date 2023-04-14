
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field
from torch.utils.data import Dataset
from typing import Any
DataSet = Dataset
NoneType = Any
Grepo = Any
Gmodel = Any
Model = Any

@op(config_schema={})
def ml_eval_2_classify(context, in0_dataset: DataSet)->Any:   
    '''评估组件      
    :param in0_dataset: 输入数据集      
    :return out0_eval: 输出评估结果         
    '''    
    return None  
    

@op(config_schema={})
def ml_eval_classify(context, in0_dataset: DataSet)->Any:   
    '''评估组件      
    :param in0_dataset: 输入数据集      
    :return out0_eval: 输出评估结果         
    '''    
    return None  
    

@op(config_schema={})
def ml_eval_regressor(context, in0_dataset: DataSet)->Any:   
    '''评估组件      
    :param in0_dataset: 输入数据集      
    :return out0_eval: 输出评估结果         
    '''    
    return None  
    