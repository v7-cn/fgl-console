
from ..utils import visit, format, dag2dot, dot2svg
import unittest
from interpreter import interpreter as _interpreter
import json
import pdb
import typing

def interpreter(*args, **kwargs)->typing.Any:
    r = _interpreter(*args, **kwargs)[0]
    if type(r) is list:
        r = r[0]
    return r

stats = '''
         // 创建一个范式
        CREATE OR REPLACE PARADIGM attribute_transductive(schema  json, split_config json)
        BEGIN
        RUN DataModel WHERE schema=$schema.did AND topo=$schema.topo AS d;
        RUN d GrepoSplit WHERE rate=$split_config.rate AS s1, s2;
        TRAIN s1 GrepoRGCN AS m;
        RUN m, s2 GrepoModelPredict AS y_pred;
        RUN y_pred GrepoEvalTwoClassify AS output;
        RETURN output;
        END;
        // 调用属性传导范式
        CALL PARADIGM attribute_transductive({'did': 'did', 'topo':{'n1':'d1', 'n2':'d2'}}, {'rate':0.8}) AS c;
                    '''
class InterpreterTestCase(unittest.TestCase):
    
    def test_shell_fgl(self):
        fgl = interpreter('shell', stats, 'fgl', dag_executor = lambda x: ['dag_output'])['content']
        dsl = interpreter('shell', stats, 'dsl', dag_executor = lambda x: ['dag_output'])['content']
        self.assertEqual(fgl, dsl)
        self.assertEqual(fgl, 'dag_output')
        
    def test_shell_dag(self):
        dag = interpreter('shell', stats, 'dag')['content']
        self.assertIn("该DAG任务由 DSL 解析器生成",  dag)
        self.assertIn("grepo_rgcn_model",  dag)
        self.assertIn('[label="SourcePort: 1',  dag)
      
    def test_notebook_dag(self):
        dag = interpreter('notebook', stats, 'dag')['content']
        self.assertIn("该DAG任务由 DSL 解析器生成",  dag)
        self.assertIn("grepo_rgcn_model",  dag)
        self.assertIn('<title>node_',  dag)
        
    def test_shell_dagjson(self):
        dag = interpreter('shell', stats, 'dag+json')['content']
        self.assertIn("该DAG任务由 DSL 解析器生成",  dag)
        self.assertIn("GrepoRGCN",  dag)
        self.assertIn('"source_port": 1',  dag)
        
    def test_debug(self):
        r = interpreter('shell', stats, 'debug')
        # pdb.set_trace()
        self.assertEqual(r['content'], 'error result xxx')
        self.assertEqual(r['status'], 'error')
        self.assertEqual(r['status_options']['message'], 'debug content xxx')
        
    
    def test_unknown_mode(self):
        r = interpreter('shell', stats, 'dags')
        # pdb.set_trace()
        self.assertEqual(r['content'], 'error')
        self.assertEqual(r['status'], 'error')
        self.assertEqual(r['status_options']['message'], f'unknown mode dags')

    def test_inline_mode(self):
        for context in ['shell', 'notebook']:
            for mode in ['fgl', 'dsl', 'dag+json', 'dag', 'debug']:
                direct_res = interpreter(context, f"%{mode}\n" + stats, 'direct')['content']
                inline_mode_res = interpreter(context, stats, mode)['content']
                self.assertEqual(direct_res[:20], inline_mode_res[:20])