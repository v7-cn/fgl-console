'''
基于图数据集(传文件路径) 的属性传导范式调用
'''

attribute_transductive = '''
    -- 创建一个范式
    CREATE OR REPLACE PARADIGM attribute_transductive(path string, split_config json, gcn_config json)
    BEGIN
      RUN GraphRepo WHERE path=$path as d;
      RUN d GrepoSplit WHERE split_rate=$split_config.split_rate AND node_type=$split_config.node_type AS s1, s2;
      TRAIN s1 GrepoRGCN WHERE label=$gcn_config.label AND features=$gcn_config.features AND edge_list=$gcn_config.edge_list AS m;
      RUN m, s2 GrepoModelPredict AS y_pred;
      RUN y_pred LabelTaskClassify AS output;
      RETURN output;
    END;
    -- 调用属性传导范式
    CALL PARADIGM attribute_transductive("test_graph_dataset_path",
    {'split_rate':0.8, 'node_type': 'customer'},
    {
      'label': 'customer.label',
      'features': [
        "customer.gender", "customer.employer_type",
        "customer.educ_level", "customer.co_manager_flag",
        "customer.acct_bal", "customer.indivbank_flag",
        "company.type",
        "merchant.type",
        "bankout_customer.type"
      ],
      -- edge_list
      'edge_list': ["consum_trans", "bankin_trans", "invest_trans", "bankout_trans"]
    }) AS c;
'''

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../dsl")
from fgl import FGL

def execute_fgl(dag):
    '''
    
    '''
    ...

dag = FGL().parse_dag(attribute_transductive, dumps=True)
assert execute_fgl(dag) is not None, "dag 未被执行"

