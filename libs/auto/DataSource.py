
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field
from torch.utils.data import Dataset
from typing import Any
DataSet = Dataset
NoneType = Any
Grepo = Any
Gmodel = Any
Model = Any

@op(config_schema={"ds_id": Field(str, default_value='', description="数据集")})
def dataset(context, )->Any:   
    '''数据源组件      
    
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    