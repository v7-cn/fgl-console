
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field
from torch.utils.data import Dataset
from typing import Any
DataSet = Dataset
NoneType = Any
Grepo = Any
Gmodel = Any
Model = Any

@op(config_schema={"choose_way": Field(str, default_value='pearson', description="相关系数计算方式"),
                    "cols": Field(list, default_value=[], description="检验列")})
def data_correlation_matrix(context, in0_dataset: DataSet)->Any:   
    '''统计分析组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"cols": Field(list, default_value=[], description="检验列")})
def data_cov(context, in0_dataset: DataSet)->Any:   
    '''统计分析组件      
    :param in0_dataset: 输入数据集1      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"cols": Field(str, default_value='', description="检验列"),
                    "mean": Field(int, default_value=0, description="总体均值")})
def data_student_T(context, in0_dataset: DataSet)->Any:   
    '''统计分析组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"cols": Field(list, default_value=[], description="选择要统计的列"),
                    "interval_num": Field(int, default_value=10, description="区间个数")})
def data_histogram(context, in0_dataset: DataSet)->Any:   
    '''统计分析组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"cols": Field(list, default_value=[], description="选择列")})
def data_normal_test(context, in0_dataset: DataSet)->Any:   
    '''统计分析组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"test_col": Field(str, default_value='', description="检验列"),
                    "sort_col": Field(str, default_value='', description="排序列"),
                    "lag": Field(int, default_value=100, description="最大lag")})
def data_auto_regression(context, in0_dataset: DataSet)->Any:   
    '''统计分析组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"feature": Field(str, default_value='', description="特征列"),
                    "label": Field(str, default_value='', description="标签列")})
def data_f_test(context, in0_dataset: DataSet)->Any:   
    '''统计分析组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"cols": Field(list, default_value=[], description="检验列"),
                    "alternative": Field(str, default_value='two-sided', description="替代方式"),
                    "mode": Field(str, default_value='auto', description="计算模式")})
def data_ks_test(context, in0_dataset: DataSet)->Any:   
    '''统计分析组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    