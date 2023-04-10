'''
基于数据模型(传topo) 的属性传导范式调用
'''


attribute_transductive = '''
    -- 创建一个范式
    CREATE OR REPLACE PARADIGM attribute_transductive(schema json, split_config json, gcn_config json)
    BEGIN
      RUN DataModel WHERE datamodel_id=$schema.datamodel_id AND topo=$schema.topo AS d;
      RUN d GrepoSplit WHERE split_rate=$split_config.split_rate AND node_type=$split_config.node_type AS s1, s2;
      TRAIN s1 GrepoRGCN WHERE label=$gcn_config.label AND features=$gcn_config.features AND edge_list=$gcn_config.edge_list AS m;
      RUN m, s2 GrepoModelPredict AS y_pred;
      RUN y_pred LabelTaskClassify AS output;
      RETURN output;
    END;
    -- 调用属性传导范式
    CALL PARADIGM attribute_transductive({
      'datamodel_id': 'dmodel_yncjxadunuibiwr1',
      'topo': {
        'node_7qv4w3ezx5bb1n6d': 'ds_e7v0ifwh4f7k3mv0',
        'node_q7g9f3b9sst6f6td': 'ds_ajbkskk6wgm5drnx',
        'node_kkctpt59zimqyjuf': 'ds_p22zf3wrhfca4x4g',
        'node_6avgj0agsda18gf7': 'ds_4c0y3jnic73g7bty',
        'node_nj4t7tbw3rrn6jh3': 'ds_5cdump3ptfbqh7ci',
        'node_cnxykqzy7inycyu5': 'ds_eiamjmyqtf7cdm71',
        'node_9uqjevuisbf8bh4s': 'ds_gpnzqkn41av9aanq',
        'node_tapmvn8fhshb5w1w': 'ds_ntfdczg7qrc3rv1s'
      }
    },
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

