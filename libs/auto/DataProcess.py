
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field
from torch.utils.data import Dataset
from typing import Any
DataSet = Dataset
NoneType = Any
Grepo = Any
Gmodel = Any
Model = Any

@op(config_schema={"distinct_type": Field(str, default_value='row', description="去重方式"),
                    "cols": Field(list, default_value=[], description="选择去重列")})
def data_distinct(context, in0_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={})
def data_union(context, in0_dataset: DataSet, in1_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集1      
    :param in1_dataset: 输入数据集2      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"cols": Field(list, default_value=[], description="选择列")})
def data_select(context, in0_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"rename": Field(list, default_value=[], description="列重命名")})
def data_rename(context, in0_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"condition": Field(dict, default_value={}, description="过滤条件")})
def data_filter(context, in0_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"join_type": Field(str, default_value='inner', description="join类型"),
                    "left_key_col": Field(str, default_value='', description="左侧数据集连接列"),
                    "right_key_col": Field(str, default_value='', description="右侧数据集连接列"),
                    "left_output_cols": Field(list, default_value=[], description="左侧数据集输出列"),
                    "right_output_cols": Field(list, default_value=[], description="右侧数据集输出列")})
def data_join(context, in0_dataset: DataSet, in1_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集1      
    :param in1_dataset: 输入数据集2      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"split_rate": Field(float, default_value=0.8, description="拆分比例")})
def data_split(context, in0_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集1     
    :return out1_dataset: 输出数据集2         
    '''    
    return None  
    

@op(config_schema={"cols": Field(list, default_value=[], description="选择列"),
                    "cast_type": Field(str, default_value='STRING', description="数据转换类型")})
def data_cast_type(context, in0_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"codeContent": Field(str, default_value='IyAtKi0gY29kaW5nOiBVVEYtOCAtKi0KIyMjCiMg6Ieq5a6a5LmJc3BhcmvohJrmnKzmqKHniYh2MS4wCiMjIwoKIyDms6jmhI/kuovpobnvvJoKIyAx44CB6Ieq5a6a5LmJ5qih54mI5Ye95pWw5ZCN56ew5LiN6IO95L+u5pS5CiMgMuOAgeWHveaVsOWPguaVsOS4jeiDveS/ruaUue+8jOaUr+aMgei+k+WFpeacgOWkmjTkuKpzcGFyayBEYXRhRnJhbWXvvIzmjInnhafoioLngrnovpPlhaXnq6/lj6Pku47lt6bliLDlj7Ppobrluo/lr7nlupRkZjHjgIFkZjLjgIFkZjPjgIFkZjQKIyAz44CB5Ye95pWw6L6T5Ye65pWw6YeP5b+F6aG75Li6NOS4qu+8jOWPr+S7peaYr3NwYXJrIERhdGFGcmFtZeaIlk5vbmXvvIzmjInnhafoioLngrnovpPlh7rnq6/lj6Pku47lt6bliLDlj7Plr7nlupQKIyA044CB5Ye95pWw5YaF57yW6L6R6Ieq5a6a5LmJc3Bhcmvku6PnoIHvvIzku4XmlK/mjIFweXNwYXJr55u45YWz5bqTYXBp6LCD55SoCmRlZiBjdXN0b21fc3BhcmsoZGYxLCBkZjIsIGRmMywgZGY0LCBzcGFyayk6CiAgICAiIiIKICAgIOWHveaVsOWGhee8lui+keiHquWumuS5ieeahHNwYXJr6ISa5pys5Luj56CBCiAgICAiIiIKICAgICMg6LCD55SocHlzcGFya+ebuOWFs2Fwaeagt+S+i++8mgogICAgIyBmcm9tIHB5c3Bhcmsuc3FsLmZ1bmN0aW9ucyBpbXBvcnQgKgogICAgcmV0dXJuIGRmMSwgZGYyLCBkZjMsIGRmNAoK', description="自定义代码")})
def data_custom_spark(context, in0_dataset: DataSet, in1_dataset: DataSet, in2_dataset: DataSet, in3_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集1      
    :param in1_dataset: 输入数据集2      
    :param in2_dataset: 输入数据集3      
    :param in3_dataset: 输入数据集4      
    :return out0_dataset: 输出数据集1     
    :return out1_dataset: 输出数据集2     
    :return out2_dataset: 输出数据集3     
    :return out3_dataset: 输出数据集4         
    '''    
    return None  
    

@op(config_schema={"sample_mode": Field(str, default_value='random_sample', description="采样方法"),
                    "fraction": Field(float, default_value=0.5, description="采样比例"),
                    "number": Field(int, default_value=100, description="采样数量"),
                    "sample_calculation_method": Field(str, default_value='ratio', description="采样方式"),
                    "seed": Field(int, default_value=0, description="随机种子"),
                    "with_replacement": Field(bool, default_value=False, description="是否放回"),
                    "label_col": Field(str, default_value='', description="标签列")})
def data_easy_sample(context, in0_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"sample_rate": Field(float, default_value=0.1, description="采样率"),
                    "label_col": Field(str, default_value='', description="标签列"),
                    "label_value": Field(NoneType, default_value=None, description="标签值")})
def data_negative_sample(context, in0_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"host": Field(str, default_value='', description="HOST"),
                    "port": Field(int, default_value=0, description="PORT"),
                    "db_name": Field(str, default_value='', description="数据库名"),
                    "table_name": Field(str, default_value='', description="表名"),
                    "user": Field(str, default_value='', description="用户名"),
                    "password": Field(str, default_value='', description="密码")})
def data_ds_to_mysql(context, in0_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    

@op(config_schema={"host": Field(str, default_value='', description="HOST"),
                    "port": Field(int, default_value=0, description="PORT"),
                    "zk_hosts": Field(str, default_value='', description="zk地址"),
                    "tablename": Field(str, default_value='', description="表名"),
                    "rowkey": Field(str, default_value='', description="选择rowkey列"),
                    "column_family": Field(list, default_value=[], description="配置列族")})
def data_export_hbase(context, in0_dataset: DataSet)->Any:   
    '''数据处理组件      
    :param in0_dataset: 输入数据集      
    :return out0_dataset: 输出数据集         
    '''    
    return None  
    