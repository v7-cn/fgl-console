
from ..utils import visit, format, dag2dot, dot2svg
import unittest
stat = '''
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
class FormatTestCase(unittest.TestCase):

    def dag(self):
        from fgl import FGL
        # A -> B -> C
        return FGL().parse_dag(stat, dumps=True)
        
    def output(self, opt):
        pass
        # print('\n' + '>' * 50 + '\n', opt)
        
        
    def test_dag(self):
        dag = self.dag()
        # print('\n' + '<' * 50 + "\n", dag)
        self.assertIn("该DAG任务由 FGL 解析器生成",  dag)
        self.assertIn("GrepoRGCN",  dag)
        self.assertIn('"source_port": 1',  dag)
        pass

    def test_dot(self):
        dot = dag2dot(self.dag())
        self.output(dot)
        self.assertIn("该DAG任务由 FGL 解析器生成",  dot)
        self.assertIn("grepo_rgcn_model",  dot)
        self.assertIn('[label="SourcePort: 1',  dot)
        with open("t.dot", "w") as opt:
            opt.write(dot)
        pass

    def test_svg(self):
        svg = dot2svg(dag2dot(self.dag()))
        self.output(svg)
        self.assertIn("该DAG任务由 FGL 解析器生成",  svg)
        self.assertIn("grepo_rgcn_model",  svg)
        self.assertIn('<title>node_',  svg)
        pass
    