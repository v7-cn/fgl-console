
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field
from torch.utils.data import Dataset
from typing import Any
DataSet = Dataset
NoneType = Any
Grepo = Any
Gmodel = Any
Model = Any


@op(config_schema={"graph_schema": Field(list, default_value=[], description="构图配置")})
def build_graph(context, in0_dataset: DataSet, in1_dataset: DataSet)->Any:   
    '''图数据集组件      
    :param in0_dataset: 输入数据集1      
    :param in1_dataset: 输入数据集2      
    :return out0_grepo: 输出图数据集         
    '''    
    return None  
    