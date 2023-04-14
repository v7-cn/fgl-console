from antlr4 import FileStream, CommonTokenStream
from antlr4.InputStream import InputStream
from ..dsl.FGLLexer import FGLLexer
from ..dsl.FGLParser import FGLParser
# from .CustomFGLVisitor import CustomFGLVisitor
from .visitors.StatementSplitVisitor import StatementSplitVisitor
from .visitors.MacroExpansionVisitor import MacroExpansionVisitor
from .visitors.DDLVisitor import DDLVisitor
from .visitors.DAGVisitor import DAGVisitor
import pdb
import json
from ..utils import visit, format, dag2dot


def debug(dsl):
    s = CommonTokenStream(FGLLexer(InputStream(dsl)))
    parser = FGLParser(s)
    parse_tree = parser.prog()
    s.fill()
    print("## ParseTree:\n", parse_tree.toStringTree(recog=parser))
    print("## TOKEN:")
    for cc in s.tokens:
        print(f'{cc.text} \033[96m {parser.symbolicNames[cc.type]} \033[0m',
              end="")
    print("")



def debug_pipeline():
    s = '''
    -- 创建一个范式
    CREATE OR REPLACE PARADIGM attribute_transductive(schema json, split_config json)
    BEGIN
      RUN DataModel WHERE schema=$schema.did AND topo=$schema.topo AS d;
      RUN d GrepoSplit WHERE rate=$split_config.rate AS s1, s2;
      TRAIN s1 GrepoRGCN AS m;
      RUN m, s2 GrepoModelPredict AS y_pred;
      RUN y_pred GrepoEvalTwoClassify AS output;
      RETURN output;
    END;
    -- 调用属性传导范式
    CALL PARADIGM attribute_transductive({'did': 'did', 'topo':{'n1':'d1', 'n2':'d2'}}, {'rate':0.8}) AS c;
    '''
    
    # debug(s)
    # 拆分Statements [DDL, DML, DQL, DCL]
    s = visit(StatementSplitVisitor(), s)
    # ddl 语句提升，优先执行
    _ = visit(DDLVisitor(), '\n'.join(s.get('ddl', [])))
    r = '\n'.join(s.get('dml', []))
    # dml 宏展开, 最多展开10层
    for i in range(10):
        _r = format(visit(MacroExpansionVisitor(), r))
        if r == _r: break
        r = _r
    # 生成DAG计划
    r = visit(DAGVisitor(), r)
    r = json.dumps(r, indent=4, ensure_ascii=False)
    print("<<< DAG:\n", r)
    d = dag2dot(r)
    print("<<< DOT:\n", d)



def test_stat_split():
    s = '''
  -- 创建一个UDF
  CREATE OR REPLACE FUNCTION split_and_merge(g string, output string)
  BEGIN
    RUN $g Normalization.'$output' AS b1;
    RUN $g Normalization.'$output' AS b2;
    RUN b1, b2 Normalization.'$output' AS c;
    RETURN c;
  END;
  -- 创建一个范式
  CREATE OR REPLACE PARADIGM attribute_transductive(g string, output string)
  BEGIN
    RUN $g Normalization.'$output' WHERE 
      cols='gender,age' AND
      normal_type='maxmin' AND
      keep_original_col=false AS b;
    SELECT split_and_merge(b, 'bank_mock') AS c; 
    RUN c Normalization.'$output' WHERE 
      cols='gender,age' AND
      normal_type='maxmin' AND
      keep_original_col=false AS d;
    RETURN d;
  END;
  // 读取数据集
  LOAD dataset.`zc_test` AS a;
  LOAD dataset.`zc_test` AS b;
  // 做数据标准化
  RUN a, b Normalization.`` WHERE 
    cols='gender,age' AND
    normal_type='maxmin' AND
    keep_original_col=false AS b1, b2;
  // 调用属性传导范式
  CALL attribute_transductive(b2, 'bank_mock') AS c;
  
  '''
  # A->B, A->C, B->D, C->D
  #   s = '''
  # LOAD dataset.`zc_test` as a;
  # TRAIN a Normalization.`` WHERE 
  #   cols='gender,age' AND
  #   normal_type='maxmin' AND
  #   keep_original_col=false as b;
  # TRAIN a Normalization.`` WHERE 
  #   cols='gender,age' AND
  #   normal_type='maxmin' AND
  #   keep_original_col=false as c;
  # TRAIN b,c Normalization.`` WHERE 
  #   cols='gender,age' AND
  #   normal_type='maxmin' AND
  #   keep_original_col=true as d;
  # '''
    # debug(s)
    # 拆分Statements [DDL, DML, DQL, DCL]
    s = visit(StatementSplitVisitor(), s)
    # ddl 语句提升，优先执行
    _ = visit(DDLVisitor(), '\n'.join(s.get('ddl', [])))
    r = '\n'.join(s.get('dml', []))
    # dml 宏展开, 最多展开10层
    for i in range(10):
        _r = format(visit(MacroExpansionVisitor(), r))
        if r == _r: break
        r = _r
    # 生成DAG计划
    r = visit(DAGVisitor(), r)
    r = json.dumps(r, indent=4, ensure_ascii=False)
    d = dag2dot(r)
    print("<<< DAG:\n", r)
    print("<<< DOT:\n", d)



def test1():
    s = '''
  train hdfs.'asdfsadf';
  '''
    s = '''
  CALL paradigm attribute_transductive('aaa', 'bbb');
  LOAD hdfs.'output' as GraphNode;
  TRAIN GCN_bin2.'' as gcn_biclass_result;
  CREATE OR REPLACE PARADIGM attribute_transductive(dataset string, output string)
  BEGIN
    LOAD hdfs.'$dataset' as GraphEdge;
    LOAD hdfs.'$output' as GraphNode;
    TRAIN GCN_bin2.'' as gcn_biclass_result;
    TRAIN concat() GraphConstractor.`` as graph;
    TRAIN graph GraphSpliter.'' as graph_splited;
    TRAIN GraphFeatureAuthStat.'' as feature_stat;
    RETURN feature_stat;
  END;
  '''

    s = '''
  LOAD dataset.`zc_test` as a;
  TRAIN a Normalization.`` WHERE 
    cols='gender,age' AND
    normal_type='maxmin' AND
    keep_original_col=false;
  CALL PARADIGM attribute_transductive('bank_mock', '/paradigm/bank_model.pth');
  '''
    print("SS:", s[152:228])
    parser = FGLParser(CommonTokenStream(FGLLexer(InputStream(s))))
    parse_tree = parser.prog()
    # pdb.set_trace()
    debug(s)
    r = CustomFGLVisitor().visit(parse_tree)
    print("RR:", r)


def test_dag(s=None, p=''):
    from .. import FGLDSL
    stat = s or '''
  LOAD dataset.`zc_test` as d;
  TRAIN d Normalization.`` WHERE 
    cols='gender,age' AND
    normal_type='maxmin' AND
    keep_original_col=false;
  '''
    # debug(stat)
    dag = FGLDSL().parse_dag(stat, dumps=True)
    print(f">>>>>>: [{p}]\n", stat)
    print(f"<<<<<<: [{p}]\n", dag)


def test_dags():
  #   test_dag(
  #       '''
  # LOAD dataset.`zc_test` as a;
  # TRAIN a Normalization.`` WHERE 
  #   cols='gender,age' AND
  #   normal_type='maxmin' AND
  #   keep_original_col=false;
  # CALL PARADIGM attribute_transductive('bank_mock', '/paradigm/bank_model.pth');
  # ''', 'A->B')
    
    test_dag(
        '''
  LOAD dataset.`zc_test` as a;
  TRAIN a Normalization.`` WHERE 
    cols='gender,age' AND
    normal_type='maxmin' AND
    keep_original_col=false as b;
  CALL PARADIGM attribute_transductive('bank_mock', '/paradigm/bank_model.pth');
  ''', 'A->B,A->C,B->D,C->D')

    # test_dag(
    #     '''
    # LOAD dataset.`zc_test` as a;
    # TRAIN a Normalization.`` WHERE 
    #     cols='gender,age' AND
    #     normal_type='maxmin' AND
    #     keep_original_col=false as b;
    # TRAIN b Normalization.'bank_mock' WHERE 
    #       cols='gender,age' AND
    #       normal_type='maxmin' AND
    #       keep_original_col=false as l_f7d6a5f0_b;
    # TRAIN l_f7d6a5f0_b Normalization.'bank_mock' WHERE 
    #       cols='gender,age' AND
    #       normal_type='maxmin' AND
    #       keep_original_col=false as c;
    #        ''', 'A->P(B)->C')

    # test_dag('''
    # LOAD dataset.`zc_test` as a;
    # TRAIN a Normalization.`` WHERE
    #   cols='gender,age' AND
    #   normal_type='maxmin' AND
    #   keep_original_col=false as b;
    # TRAIN b Normalization.`` WHERE
    #   cols='gender,age' AND
    #   normal_type='maxmin' AND
    #   keep_original_col=false as c;
    # ''', 'A->B->C')

    # test_dag('''
    # LOAD dataset.`zc_test` as a;
    # TRAIN a Normalization.`` WHERE
    #   cols='gender,age' AND
    #   normal_type='maxmin' AND
    #   keep_original_col=false as b;
    # TRAIN a Normalization.`` WHERE
    #   cols='gender,age' AND
    #   normal_type='maxmin' AND
    #   keep_original_col=false as c;
    # ''', 'A->B, A->C')


if __name__ == "__main__":
    # test1()
    # test_dags()
    # test_stat_split()
    debug_pipeline()
