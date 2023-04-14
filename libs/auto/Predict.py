
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
def predict(context, in0_model: Model, in1_dataset: DataSet)->Any:   
    '''预测组件      
    :param in0_model: 输入模型      
    :param in1_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    