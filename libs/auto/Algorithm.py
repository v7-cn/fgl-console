
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field
from torch.utils.data import Dataset
from typing import Any
DataSet = Dataset
NoneType = Any
Grepo = Any
Gmodel = Any
Model = Any

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "max_depth": Field(int, default_value=5, description="树最大深度"),
                    "criterion": Field(str, default_value='gini', description="信息增益计算策略"),
                    "max_leaf_nodes": Field(int, default_value=32, description="最大分支数"),
                    "min_impurity_decrease": Field(int, default_value=0, description="最小信息熵增益"),
                    "min_samples_split": Field(int, default_value=5, description="节点最小样本数"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def DTBinaryClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "max_depth": Field(int, default_value=5, description="树最大深度"),
                    "criterion": Field(str, default_value='gini', description="信息增益计算策略"),
                    "max_leaf_nodes": Field(int, default_value=32, description="最大分支数"),
                    "min_impurity_decrease": Field(int, default_value=0, description="最小信息熵增益"),
                    "min_samples_split": Field(int, default_value=5, description="节点最小样本数"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def DTMultiClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "max_depth": Field(int, default_value=5, description="树最大深度"),
                    "max_leaf_nodes": Field(int, default_value=32, description="最大分支数"),
                    "min_impurity_decrease": Field(int, default_value=0, description="最小信息熵增益"),
                    "min_samples_split": Field(int, default_value=5, description="节点最小样本数"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def DTRegressor(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "max_features": Field(str, default_value='auto', description="特征采样数量"),
                    "n_estimators": Field(int, default_value=5, description="树的数量"),
                    "max_depth": Field(int, default_value=5, description="树最大深度"),
                    "criterion": Field(str, default_value='gini', description="信息增益计算策略"),
                    "min_impurity_decrease": Field(int, default_value=0, description="最小信息熵增益"),
                    "min_samples_split": Field(int, default_value=5, description="节点最小样本数"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def RFBinaryClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "max_features": Field(str, default_value='auto', description="特征采样数量"),
                    "n_estimators": Field(int, default_value=5, description="树的数量"),
                    "max_depth": Field(int, default_value=5, description="树最大深度"),
                    "criterion": Field(str, default_value='gini', description="信息增益计算策略"),
                    "min_impurity_decrease": Field(int, default_value=0, description="最小信息熵增益"),
                    "min_samples_split": Field(int, default_value=5, description="节点最小样本数"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def RFMultiClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "max_features": Field(str, default_value='auto', description="特征采样数量"),
                    "n_estimators": Field(int, default_value=5, description="树的数量"),
                    "max_depth": Field(int, default_value=5, description="树最大深度"),
                    "criterion": Field(str, default_value='gini', description="信息增益计算策略"),
                    "min_impurity_decrease": Field(int, default_value=0, description="最小信息熵增益"),
                    "min_samples_split": Field(int, default_value=5, description="节点最小样本数"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def RFRegressor(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "max_depth": Field(int, default_value=5, description="树最大深度"),
                    "max_leaf_nodes": Field(int, default_value=32, description="最大分支数"),
                    "min_impurity_decrease": Field(int, default_value=0, description="最小信息熵增益"),
                    "min_samples_split": Field(int, default_value=5, description="节点最小样本数"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "subsample": Field(float, default_value=1.0, description="训练基百分比"),
                    "n_estimators": Field(int, default_value=100, description="最大迭代次数"),
                    "learning_rate": Field(float, default_value=0.1, description="学习率"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def GBDTBinaryClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "max_depth": Field(int, default_value=5, description="树最大深度"),
                    "max_leaf_nodes": Field(int, default_value=32, description="最大分支数"),
                    "min_impurity_decrease": Field(int, default_value=0, description="最小信息熵增益"),
                    "min_samples_split": Field(int, default_value=5, description="节点最小样本数"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "subsample": Field(float, default_value=1.0, description="训练基百分比"),
                    "n_estimators": Field(int, default_value=100, description="最大迭代次数"),
                    "learning_rate": Field(float, default_value=0.1, description="学习率"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def GBDTMultiClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "max_depth": Field(int, default_value=5, description="树最大深度"),
                    "max_leaf_nodes": Field(int, default_value=32, description="最大分支数"),
                    "min_impurity_decrease": Field(int, default_value=0, description="最小信息熵增益"),
                    "min_samples_split": Field(int, default_value=5, description="节点最小样本数"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "subsample": Field(float, default_value=1.0, description="训练基百分比"),
                    "n_estimators": Field(int, default_value=100, description="最大迭代次数"),
                    "learning_rate": Field(float, default_value=0.1, description="学习率"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def GBDTRegressor(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "hidden_layer_sizes": Field(list, default_value=[100], description="隐藏层"),
                    "learning_rate_init": Field(str, default_value='0.001', description="学习率"),
                    "max_iter": Field(int, default_value=200, description="最大迭代轮数"),
                    "tol": Field(float, default_value=0.0001, description="目标收敛阈值"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def MLPBinaryClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "hidden_layer_sizes": Field(list, default_value=[100], description="隐藏层"),
                    "learning_rate_init": Field(str, default_value='0.001', description="学习率"),
                    "max_iter": Field(int, default_value=200, description="最大迭代轮数"),
                    "tol": Field(float, default_value=0.0001, description="目标收敛阈值"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def MLPMultiClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "hidden_layer_sizes": Field(list, default_value=[100], description="隐藏层"),
                    "learning_rate_init": Field(str, default_value='0.001', description="学习率"),
                    "max_iter": Field(int, default_value=200, description="最大迭代轮数"),
                    "tol": Field(float, default_value=0.0001, description="目标收敛阈值"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def MLPRegression(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "solver": Field(str, default_value='lbfgs', description="优化器"),
                    "max_iter": Field(int, default_value=20, description="最大迭代轮数"),
                    "tol": Field(float, default_value=0.0001, description="目标收敛阈值"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def LRBinaryClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "solver": Field(str, default_value='lbfgs', description="优化器"),
                    "max_iter": Field(int, default_value=20, description="最大迭代轮数"),
                    "tol": Field(float, default_value=0.0001, description="目标收敛阈值"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def LRMultiClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def LinearRegression(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "alpha": Field(str, default_value='1.0', description="正则化强度"),
                    "max_iter": Field(int, default_value=20, description="最大迭代轮数"),
                    "tol": Field(float, default_value=0.0001, description="目标收敛阈值"),
                    "random_state": Field(int, default_value=5, description="随机种子"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def Ridge(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "n_estimators": Field(int, default_value=100, description="树的数量"),
                    "max_depth": Field(int, default_value=6, description="树的最大深度"),
                    "learning_rate": Field(float, default_value=0.3, description="学习率"),
                    "min_child_weight": Field(int, default_value=1, description="最小叶子节点样本权重和"),
                    "subsample": Field(float, default_value=0.6, description="子样本"),
                    "gmma": Field(int, default_value=0, description="节点分裂所需的最小函数"),
                    "alpha": Field(int, default_value=0, description="L1正则化系数"),
                    "reg_lambda": Field(int, default_value=1, description="L2正则化系数"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def XGBoostClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "n_estimators": Field(int, default_value=100, description="树的数量"),
                    "max_depth": Field(int, default_value=6, description="树的最大深度"),
                    "learning_rate": Field(float, default_value=0.3, description="学习率"),
                    "min_child_weight": Field(int, default_value=1, description="最小叶子节点样本权重和"),
                    "subsample": Field(float, default_value=0.6, description="子样本"),
                    "gmma": Field(int, default_value=0, description="节点分裂所需的最小函数"),
                    "alpha": Field(int, default_value=0, description="L1正则化系数"),
                    "reg_lambda": Field(int, default_value=1, description="L2正则化系数"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def XGBoostRegression(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    

@op(config_schema={"feature": Field(list, default_value=[], description="特征列"),
                    "label": Field(str, default_value='', description="标签列"),
                    "C": Field(float, default_value=1.0, description="惩罚系数"),
                    "max_iter": Field(int, default_value=-1, description="最大迭代轮数"),
                    "gmma": Field(str, default_value='scale', description="核函数系数"),
                    "kernal": Field(str, default_value='rbf', description="核函数"),
                    "tol": Field(float, default_value=0.001, description="目标收敛阈值"),
                    "automl": Field(bool, default_value=False, description="是否自动化训练"),
                    "automl_trials": Field(int, default_value=4, description="创建模型数量")})
def SvmSvcClassifier(context, in0_dataset: DataSet)->Any:   
    '''算法组件      
    :param in0_dataset: 输入数据集      
    :return out0_model: 输出模型         
    '''    
    return None  
    