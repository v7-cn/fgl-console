from antlr4 import FileStream, CommonTokenStream
from antlr4.InputStream import InputStream
from .dsl.FGLLexer import FGLLexer
from .dsl.FGLParser import FGLParser
from .visitors.DAGVisitor import DAGVisitor
from .visitors.DDLVisitor import DDLVisitor
from .visitors.DAGVisitor import DAGVisitor
from .visitors.StatementSplitVisitor import StatementSplitVisitor
from .visitors.MacroExpansionVisitor import MacroExpansionVisitor
from .visitors.DDLVisitor import DDLVisitor
from .visitors.DAGVisitor import DAGVisitor
from .visitors.MetaVisitor import MetaVisitor
from .visitors.RewriterVisitor import RewriterVisitor
import pdb
import json
from .utils import visit, format, dag2dot, debug
from .support.exceptions import DSLException, DSLParseException
import logging

class FGL():

    def __init__(self):
        pass

    def parse_dag(self, dsl, dumps=True):
        r = self.parse(dsl, dumps)
        return r['dag']

    def parse(self, dsl, dumps=True):
        debug(dsl)
        s = visit(StatementSplitVisitor(), dsl)
        logging.debug("DML: %s", s.get("dml", []))
        logging.info("DQL: %s", s.get("dql", []))
        logging.debug("DDL: %s", s.get("ddl", []))
        # ddl 语句提升，优先执行
        is_macro_change_ddl = visit(DDLVisitor(),
                                    '\n'.join(s.get('ddl', [])))
        r = '\n'.join(s.get('dml', []))
        logging.debug("Macro 展开前: %s", r)
        # dml 宏展开, 最多展开10层
        for i in range(10):
            if len(r) == 0:
                break
            logging.debug("Macro 展开1: %s", r)
            _r = format(visit(MacroExpansionVisitor(), r, ignore_parse_error=True))
            logging.debug("Macro 展开2: %s", _r)
            if r == _r: break
            r = _r
        logging.debug("Macro 展开后: %s", r)
        # FGL改写
        r = visit(RewriterVisitor(), r)
        # 部分语句由 FGL 中间件负责解释
        is_macro_change_dql, output = visit(
            MetaVisitor(),
            ";\n".join(s.get("ddl", []) + s.get("dql", [])) + r)
        # 生成DAG计划
        dag = visit(DAGVisitor(), r)
        if dumps:
            dag = json.dumps(dag, indent=4, ensure_ascii=False)

        return {
            'dag': dag,
            'output': output,
            'reference_change': is_macro_change_ddl or is_macro_change_dql
        }


import pandas as pd
from io import StringIO

from IPython.core.magic import (register_line_magic, register_cell_magic)


def parse_pipeline(stat):
    s = visit(StatementSplitVisitor(), stat)
    # ddl 语句提升，优先执行
    _ = visit(DDLVisitor(), '\n'.join(s.get('ddl', [])))
    r = '\n'.join(s.get('dml', []))
    # dml 宏展开, 最多展开10层
    for i in range(10):
        _r = format(visit(MacroExpansionVisitor(), r))
        if r == _r: break
        r = _r
    # 生成DAG计划
    rj = r = visit(DAGVisitor(), r)
    r = json.dumps(r, indent=4, ensure_ascii=False)
    d = dag2dot(r)
    return rj, d


try:

    @register_line_magic
    @register_cell_magic
    def gsql(line, cell=None):
        dag, dot = parse_pipeline(cell)
        return dag
        return json.dumps(dag, indent=4, ensure_ascii=True)

    @register_line_magic
    @register_cell_magic
    def gdag(line, cell=None):
        import graphviz
        from IPython.display import display
        dag, dot = parse_pipeline(cell)
        display(graphviz.Source(dot))
        # return dot
except:
    pass