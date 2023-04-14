
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field
from torch.utils.data import Dataset
from typing import Any
DataSet = Dataset
NoneType = Any
Grepo = Any
Gmodel = Any
Model = Any

@op(config_schema={"split_rate": Field(float, default_value=0.8, description="拆分比例"),
                    "node_type": Field(str, default_value='', description="指定拆分节点类型")})
def grepo_split(context, in0_grepo: Grepo)->Any:   
    '''图数据处理组件      
    :param in0_grepo: 输入图数据集      
    :return out0_grepo: 输出图数据集1     
    :return out1_grepo: 输出图数据集2         
    '''    
    return None  
    

@op(config_schema={"nodes_list": Field(list, default_value=[], description="选择节点类型")})
def grepo_feat(context, in0_grepo: Grepo)->Any:   
    '''图数据处理组件      
    :param in0_grepo: 输入图数据集      
    :return out0_grepo: 输出图数据集         
    '''    
    return None  
    

@op(config_schema={"nodes_list": Field(list, default_value=[], description="选择过滤条件")})
def grepo_filter(context, in0_grepo: Grepo)->Any:   
    '''图数据处理组件      
    :param in0_grepo: 输入图数据集      
    :return out0_grepo: 输出图数据集         
    '''    
    return None  
    