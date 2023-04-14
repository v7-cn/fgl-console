# from graphaidsl.rel.initDB import modules
# module_configs = {}
# mm = list(modules[0].values())[0][0]
# for mds in modules:
#     for mds in mds.values():
#         for mm in mds:
#             m = {'name': mm['name'], 'module': mm['maindef'][-1], 'module_id':mm['_id']}
#             module_configs[m['module_id'].lower()] = m
# import json
# print(json.dumps(module_configs, indent=4, ensure_ascii=False))

module_configs = {
    # Custom Utils
    "ExplainerGraphMask": {
        "name": "基于图遮挡的可解释",
        "module": "explainer",
        "module_id": "GraphMask"
    },
    "CreateDataSource": {
        "name": "创建数据源",
        "module": "datasource",
        "module_id": "CreateDataSource"
    },
    "DeleteDataSource": {
        "name": "删除数据源",
        "module": "datasource",
        "module_id": "DeleteDataSource"
    },
    # From initdb
    "dataset": {
        "name": "数据集",
        "module": "dataset",
        "module_id": "DataSet"
    },
    "distinct": {
        "name": "数据去重",
        "module": "data_distinct",
        "module_id": "Distinct"
    },
    "union": {
        "name": "数据Union",
        "module": "data_union",
        "module_id": "Union"
    },
    "select": {
        "name": "列选择",
        "module": "data_select",
        "module_id": "Select"
    },
    "rename": {
        "name": "列重命名",
        "module": "data_rename",
        "module_id": "Rename"
    },
    "filter": {
        "name": "数据过滤",
        "module": "data_filter",
        "module_id": "Filter"
    },
    "join": {
        "name": "数据Join",
        "module": "data_join",
        "module_id": "Join"
    },
    "split": {
        "name": "数据拆分",
        "module": "data_split",
        "module_id": "Split"
    },
    "casttype": {
        "name": "数据类型转换",
        "module": "data_cast_type",
        "module_id": "CastType"
    },
    "customspark": {
        "name": "自定义pyspark脚本",
        "module": "data_custom_spark",
        "module_id": "CustomSpark"
    },
    "easysample": {
        "name": "简单采样",
        "module": "data_easy_sample",
        "module_id": "EasySample"
    },
    "negativesample": {
        "name": "欠采样",
        "module": "data_negative_sample",
        "module_id": "NegativeSample"
    },
    "exportmysql": {
        "name": "导出Mysql",
        "module": "data_ds_to_mysql",
        "module_id": "ExportMysql"
    },
    "exporthbase": {
        "name": "导出HBase",
        "module": "data_export_hbase",
        "module_id": "ExportHBase"
    },
    "correlationmatrix": {
        "name": "相关系数矩阵",
        "module": "data_correlation_matrix",
        "module_id": "CorrelationMatrix"
    },
    "cov": {
        "name": "数据协方差",
        "module": "data_cov",
        "module_id": "Cov"
    },
    "student_t": {
        "name": "单样本T检验",
        "module": "data_student_T",
        "module_id": "Student_T"
    },
    "histogram": {
        "name": "直方图",
        "module": "data_histogram",
        "module_id": "Histogram"
    },
    "normal_test": {
        "name": "正态检验",
        "module": "data_normal_test",
        "module_id": "Normal_test"
    },
    "autoregression": {
        "name": "AutoRegression",
        "module": "data_auto_regression",
        "module_id": "AutoRegression"
    },
    "f_test": {
        "name": "F检验",
        "module": "data_f_test",
        "module_id": "F_Test"
    },
    "kstest": {
        "name": "KS检验",
        "module": "data_ks_test",
        "module_id": "KSTest"
    },
    "normalization": {
        "name": "归一化",
        "module": "data_normalization",
        "module_id": "Normalization"
    },
    "outlierhandle": {
        "name": "异常值处理",
        "module": "data_handle_outlier",
        "module_id": "OutlierHandle"
    },
    "binning": {
        "name": "分箱",
        "module": "data_binning",
        "module_id": "Binning"
    },
    "valuereplace": {
        "name": "数值替换",
        "module": "data_replace_value",
        "module_id": "ValueReplace"
    },
    "onehot": {
        "name": "onehot编码",
        "module": "data_onehot",
        "module_id": "OneHot"
    },
    "dtbinaryclassifier": {
        "name": "决策树二分类",
        "module": "DTBinaryClassifier",
        "module_id": "DTBinaryClassifier"
    },
    "dtmulticlassifier": {
        "name": "决策树多分类",
        "module": "DTMultiClassifier",
        "module_id": "DTMultiClassifier"
    },
    "dtregressor": {
        "name": "决策树回归",
        "module": "DTRegressor",
        "module_id": "DTRegressor"
    },
    "rfbinaryclassifier": {
        "name": "随机森林二分类",
        "module": "RFBinaryClassifier",
        "module_id": "RFBinaryClassifier"
    },
    "rfmulticlassifier": {
        "name": "随机森林多分类",
        "module": "RFMultiClassifier",
        "module_id": "RFMultiClassifier"
    },
    "rfregressor": {
        "name": "随机森林回归",
        "module": "RFRegressor",
        "module_id": "RFRegressor"
    },
    "gbdtbinaryclassifier": {
        "name": "GBDT二分类",
        "module": "GBDTBinaryClassifier",
        "module_id": "GBDTBinaryClassifier"
    },
    "gbdtmulticlassifier": {
        "name": "GBDT多分类",
        "module": "GBDTMultiClassifier",
        "module_id": "GBDTMultiClassifier"
    },
    "gbdtregressor": {
        "name": "GBDT回归",
        "module": "GBDTRegressor",
        "module_id": "GBDTRegressor"
    },
    "mlpbinaryclassifier": {
        "name": "dnn二分类",
        "module": "MLPBinaryClassifier",
        "module_id": "MLPBinaryClassifier"
    },
    "mlpmulticlassifier": {
        "name": "dnn多分类",
        "module": "MLPMultiClassifier",
        "module_id": "MLPMultiClassifier"
    },
    "mlpregression": {
        "name": "dnn回归",
        "module": "MLPRegression",
        "module_id": "MLPRegression"
    },
    "lrbinaryclassifier": {
        "name": "逻辑回归二分类",
        "module": "LRBinaryClassifier",
        "module_id": "LRBinaryClassifier"
    },
    "lrmulticlassifier": {
        "name": "逻辑回归多分类",
        "module": "LRMultiClassifier",
        "module_id": "LRMultiClassifier"
    },
    "linearregression": {
        "name": "线性回归",
        "module": "LinearRegression",
        "module_id": "LinearRegression"
    },
    "ridge": {
        "name": "岭回归",
        "module": "Ridge",
        "module_id": "Ridge"
    },
    "xgboostclassifier": {
        "name": "XGBoost分类",
        "module": "XGBoostClassifier",
        "module_id": "XGBoostClassifier"
    },
    "xgboostregression": {
        "name": "XGBoost回归",
        "module": "XGBoostRegression",
        "module_id": "XGBoostRegression"
    },
    "svmsvcclassifier": {
        "name": "SVM分类",
        "module": "SvmSvcClassifier",
        "module_id": "SvmSvcClassifier"
    },
    "predict": {
        "name": "模型预测",
        "module": "predict",
        "module_id": "Predict"
    },
    "mlevaltwoclassify": {
        "name": "二分类评估",
        "module": "ml_eval_2_classify",
        "module_id": "MlEvalTwoClassify"
    },
    "mlevalclassify": {
        "name": "多分类评估",
        "module": "ml_eval_classify",
        "module_id": "MlEvalClassify"
    },
    "mlevalregressor": {
        "name": "回归评估",
        "module": "ml_eval_regressor",
        "module_id": "MlEvalRegressor"
    },
    "datamodel": {
        "name": "数据模型",
        "module": "data_model",
        "module_id": "DataModel"
    },
    "graphrepo": {
        "name": "图数据集",
        "module": "graphrepo",
        "module_id": "GraphRepo"
    },
    "graphrepobuild": {
        "name": "构图组件",
        "module": "build_graph",
        "module_id": "GraphRepoBuild"
    },
    "greposplit": {
        "name": "图数据拆分",
        "module": "grepo_split",
        "module_id": "GrepoSplit"
    },
    "grepofeat": {
        "name": "图自动特征统计",
        "module": "grepo_feat",
        "module_id": "GrepoFeat"
    },
    "grepofilter": {
        "name": "图节点过滤",
        "module": "grepo_filter",
        "module_id": "GrepoFilter"
    },
    "grepogcn": {
        "name": "GCN二分类",
        "module": "grepo_gcn_model",
        "module_id": "GrepoGCN"
    },
    "greposage": {
        "name": "SAGE二分类",
        "module": "grepo_sage_model",
        "module_id": "GrepoSAGE"
    },
    "greporgcn": {
        "name": "RGCN二分类",
        "module": "grepo_rgcn_model",
        "module_id": "GrepoRGCN"
    },
    "greporsage": {
        "name": "RSAGE二分类",
        "module": "grepo_rsage_model",
        "module_id": "GrepoRSAGE"
    },
    "greporecommend": {
        "name": "图推荐算法",
        "module": "grepo_recommend_model",
        "module_id": "GrepoRecommend"
    },
    "causalinference": {
        "name": "因果推理",
        "module": "CausalInference",
        "module_id": "CausalInference"
    },
    "grepomodelpredict": {
        "name": "图模型预测",
        "module": "grepo_model_predict",
        "module_id": "GrepoModelPredict"
    },
    "greporecommendpredict": {
        "name": "图推荐预测",
        "module": "grepo_recommend_predict",
        "module_id": "GrepoRecommendPredict"
    },
    "grepoevaltwoclassify": {
        "name": "图二分类评估",
        "module": "grepo_eval_2_classify",
        "module_id": "GrepoEvalTwoClassify"
    },
    "labeltaskclassify": {
        "name": "属性传导评估",
        "module": "label_task_classify",
        "module_id": "LabelTaskClassify"
    }
}

module_configs = {k.lower():v for k,v in module_configs.items()}