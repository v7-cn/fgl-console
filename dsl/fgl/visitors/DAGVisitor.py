# Generated from FGL.g4 by ANTLR 4.11.1
from antlr4 import FileStream, CommonTokenStream
from antlr4.InputStream import InputStream
from ..dsl.FGLLexer import FGLLexer
from ..dsl.FGLParser import FGLParser
from ..dsl.FGLVisitor import FGLVisitor
from ..dsl.FGLParser import FGLParser
# from .MacroExpendorVisitor import MacroRewriterVisitor
from ..utils import value2py, md5
from ..config import module_configs
# This class defines a complete generic visitor for a parse tree produced by FGLParser.
import pdb
from collections import defaultdict


class DAGVisitor(FGLVisitor):

    # Visit a parse tree produced by FGLParser#prog.
    def visitProg(self, ctx: FGLParser.ProgContext):
        link_couple = defaultdict(lambda: defaultdict(list))
        rr = self.visitChildren(ctx)
        nodes = []
        for _sql_results in rr:
            sql_results = []
            for sr in _sql_results:
                if type(sr) is list:
                    for s in sr:
                        if type(s) is list:
                            sql_results += s
                        else:
                            sql_results.append(s)
                else:
                    sql_results.append(sr)
            # pdb.set_trace()
            for sql_result in sql_results:
                # sql_result = sql_result[0]
                if sql_result.get('payload', None) is not None:
                    nodes.append(sql_result['payload'])
                out_id = sql_result.get('out_id', None)
                in_id = sql_result.get('in_id', None)
                node_id = sql_result.get('payload', {}).get('id', None)
                if node_id is not None:
                    if out_id is not None:
                        for port_id, out_id_s in enumerate(out_id):
                            link_couple[out_id_s]['out'].append(
                                (node_id, port_id))
                    if in_id is not None:
                        for port_id, in_id_s in enumerate(in_id):
                            link_couple[in_id_s]['in'].append(
                                (node_id, port_id))
        edges = []
        for iden, ports in link_couple.items():
            # assert len(ports['out']) <= 1, f"Variable {iden} product by {len(ports['out'])} nodes"

            if len(ports['in']) > 0:
                assert len(
                    ports['out']) > 0, f'Variable {iden} used but not declared'
            for dest, dport in ports['in']:
                for src, sport in ports['out']:
                    if src == '_' or dest == '_':
                        continue
                    edges.append({
                        "source": src,
                        "target": dest,
                        "source_port": sport,
                        "target_port": dport
                    })

        if len(nodes) == 0 and len(edges) == 0:
            return None
        ret = {
            "version": "1.0.0",
            "canvas": {
                "name": f"DSL-autogen-{md5()}",
                "description": f"该DAG任务由 DSL 解析器生成",
                "position": "dsl"
            },
            'nodes': nodes,
            'edges': edges
        }
        return ret

    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            aggregate = []
        if (type(nextResult) is list and len(nextResult) > 0) or \
            (type(nextResult) is not list and  nextResult is not None):
            aggregate.append(nextResult)
        return aggregate

    # Visit a parse tree produced by FGLParser#sqlStatement.
    def visitSqlStatement(self, ctx: FGLParser.SqlStatementContext):
        # pdb.set_trace()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#identifier.
    def visitIdentifier(self, ctx: FGLParser.IdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#ddlStatement.
    def visitDdlStatement(self, ctx: FGLParser.DdlStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#dmlStatement.
    def visitDmlStatement(self, ctx: FGLParser.DmlStatementContext):
        rr = self.visitChildren(ctx)
        return rr

    # Visit a parse tree produced by FGLParser#load.
    def visitLoad(self, ctx: FGLParser.LoadContext):

        format = ctx.FORMAT().getText()
        path = ctx.STRING_LITERAL().getText()[1:-1]
        out_id = ctx.identifier().getText()
        # m = module_configs[f'format_{format}']
        m = module_configs[f'{format}'.lower()]
        config = self._setArguments2config(ctx.setArguments())
        config['module'] = m['module']
        config['ds_name'] = path
        ret = {
            'out_id': out_id,
            'payload': {
                'id': f'node_{md5(8)}',
                'name': path,
                'module_id': m['module_id'],
                'node_attrs': config
            }
        }
        return ret

    def _setArguments2config(self, setArguments):
        config = {}
        if setArguments is not None:
            for child in setArguments.getChildren():
                if hasattr(child, 'getRuleIndex'):
                    if FGLParser.ruleNames[
                            child.getRuleIndex()] == 'setArgument':
                        key, value = child.parameter().getText(), \
                            child.expr().getText()
                        try:
                            value = value2py(value)
                        except:
                            pass
                        if key == 'cols':
                            value = value.split(",")
                        config[key] = value

        return config

    # Visit a parse tree produced by FGLParser#save.
    def visitSave(self, ctx: FGLParser.SaveContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#train.
    def visitTrain(self, ctx: FGLParser.TrainContext):
        # config = {}
        # if ctx.setArguments() is not None:
        #     for child in ctx.setArguments().getChildren():
        #         if hasattr(child, 'getRuleIndex'):
        #             if FGLParser.ruleNames[
        #                     child.getRuleIndex()] == 'setArgument':
        #                 key, value = child.parameter().getText(), child.expr(
        #                 ).getText()
        #                 value = value2py(value)
        #                 if key == 'cols':
        #                     value = value.split(",")
        #                 config[key] = value
        
        config = self._setArguments2config(ctx.setArguments())
        m = module_configs[ctx.module().getText().lower()]
        config['module'] = m['module']

        ret = {
            'in_id': [expr.getText() for expr in ctx.expr()],
            'payload': {
                "id": f"node_{md5(8)}",
                "name": m['name'],
                'module_id': m['module_id'],
                'node_attrs': config
            }
        }
        if hasattr(ctx, 'identifier') and ctx.identifier() is not None:
            ret.update({'out_id': [i.getText() for i in ctx.identifier()]})
            # rets.append(ret)
        return ret

    def visitParadigm_block(self, ctx: FGLParser.Begin_blockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#expr.
    def visitExpr(self, ctx: FGLParser.ExprContext):
        return self.visitChildren(ctx)

    def visitConditions(self, ctx: FGLParser.ConditionsContext):
        # pdb.set_trace()
        return self.visitChildren(ctx)


# del FGLParser