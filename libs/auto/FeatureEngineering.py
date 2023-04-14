
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field
from torch.utils.data import Dataset
from typing import Any
DataSet = Dataset
NoneType = Any
Grepo = Any
Gmodel = Any
Model = Any

@op(config_schema={"cols": Field(list, default_value=[], description="选择列"),
                    "normal_type": Field(str, default_value='maxmin', description="归一化方式"),
                    "keep_original_col": Field(bool, default_value=False, description="是否保留原始列")})
def data_normalization(context, in0_dataset: DataSet)->Any:   
    '''特征工程组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"cols": Field(list, default_value=[], description="选择列"),
                    "outlier_type": Field(str, default_value='', description="异常值类型"),
                    "replace_type": Field(str, default_value='CUSTOMVALUE', description="填充类型"),
                    "quantile_value": Field(float, default_value=0.5, description="分位数值"),
                    "custom_value": Field(str, default_value='', description="自定义值")})
def data_handle_outlier(context, in0_dataset: DataSet)->Any:   
    '''特征工程组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"cols": Field(list, default_value=[], description="选择列"),
                    "bin_type": Field(str, default_value='QUANTILES', description="分箱方式"),
                    "bin_num": Field(int, default_value=10, description="分箱数量"),
                    "custom_bin_num": Field(str, default_value='', description="自定义分箱数量"),
                    "custom_expression": Field(str, default_value='', description="自定义分箱区间"),
                    "keep_original_col": Field(bool, default_value=False, description="是否保留原始列")})
def data_binning(context, in0_dataset: DataSet)->Any:   
    '''特征工程组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"commands": Field(list, default_value=[], description="数值替换指令")})
def data_replace_value(context, in0_dataset: DataSet)->Any:   
    '''特征工程组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"cols": Field(list, default_value=[], description="选择列"),
                    "onehot_type": Field(str, default_value='onehot', description="编码方式"),
                    "keep_original_col": Field(bool, default_value=False, description="是否保留原始列")})
def data_onehot(context, in0_dataset: DataSet)->Any:   
    '''特征工程组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    