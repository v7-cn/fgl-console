# Generated from FGL.g4 by ANTLR 4.11.1
from ..dsl.FGLVisitor import FGLVisitor
from ..dsl.FGLParser import FGLParser
# This class defines a complete generic visitor for a parse tree produced by FGLParser.
import pdb
from ..utils import kvdb, value2py, visit, md5, format
import json
import ast
from ..support.exceptions import DSLException

class VariableMapperVisitor(FGLVisitor):

    def __init__(self, output_identifier=None):
        super().__init__()
        self.variable_replacement = {}
        self.ret_replacement = {}
        self.output_identifier = output_identifier
        self.output_identifier_replaced = None

    # Visit a parse tree produced by FGLParser#prog.
    def visitProg(self, ctx: FGLParser.ProgContext):
        self.visitChildren(ctx)
        if ctx.stop is None:
            return ""
        content = ctx.start.getInputStream().getText(ctx.start.start,
                                                     ctx.stop.stop)
        stack_lable = f'l_{md5(8)}_'
        content_with_index = list(enumerate(content))
        # pdb.set_trace()
        for (s, e), v in self.variable_replacement.items():
            if v.startswith('$'):
                continue
            sn = list(
                filter(lambda r: r[1][0] == s,
                       enumerate(content_with_index)))[0][0]
            en = list(
                filter(lambda r: r[1][0] == e,
                       enumerate(content_with_index)))[0][0]
            rr = [(None, c) for c in (self.output_identifier if (
                v == self.output_identifier_replaced and self.
                output_identifier is not None) else ('_' if v == '_' else f'{stack_lable}{v}'))]
            content_with_index = content_with_index[:
                                                    sn] + rr + content_with_index[
                                                        en:]
        for (s, e), v in self.ret_replacement.items():
            sn = list(
                filter(lambda r: r[1][0] == s,
                       enumerate(content_with_index)))[0][0]
            en = list(
                filter(lambda r: r[1][0] == e,
                       enumerate(content_with_index)))[0][0]
            content_with_index = content_with_index[:sn] + [
                (None, c) for c in v
            ] + content_with_index[en:]
        content = ''.join([c for _, c in content_with_index])
        content = format(content)
        return content

    def visitIdentifier(self, ctx: FGLParser.IdentifierContext):
        self.variable_replacement[(ctx.start.start,
                                   ctx.stop.stop + 1)] = ctx.getText()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#ret.
    def visitRet(self, ctx: FGLParser.RetContext):
        self.output_identifier_replaced = ctx.expr().getText()
        self.ret_replacement[(ctx.start.start, ctx.stop.stop + 1)] = ''

        return self.visitChildren(ctx)


class MacroExpansionVisitor(FGLVisitor):

    def __init__(self):
        super().__init__()
        self.replacement = {}
        self.ipt_replacement = {}
        self.block_index_head = 0

    # Visit a parse tree produced by FGLParser#prog.
    def visitProg(self, ctx: FGLParser.ProgContext):
        _ = self.visitChildren(ctx)
        # pdb.set_trace()
        content = ctx.start.getInputStream().getText(ctx.start.start,
                                                     ctx.stop.stop)
        for (s, e), c in self.replacement.items():
            content = content[:s] + c + content[e + 1:]
        for k,v in self.ipt_replacement.items():
            content = content.replace(k, v)
        # print(content)
        # return 'asfasfds'
        return content

    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            aggregate = []
        if (type(nextResult) is list and len(nextResult) > 0) or \
            (type(nextResult) is not list and  nextResult is not None):
            aggregate.append(nextResult)
        return aggregate

    # Visit a parse tree produced by FGLParser#sqlStatement.
    def visitSqlStatement(self, ctx: FGLParser.SqlStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#identifier.
    def visitIdentifier(self, ctx: FGLParser.IdentifierContext):
        # pdb.set_trace()
        # print("Iden:", ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#ddlStatement.
    def visitDdlStatement(self, ctx: FGLParser.DdlStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#dmlStatement.
    def visitDmlStatement(self, ctx: FGLParser.DmlStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#load.
    def visitLoad(self, ctx: FGLParser.LoadContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#save.
    def visitSave(self, ctx: FGLParser.SaveContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#train.
    def visitTrain(self, ctx: FGLParser.TrainContext):
        return self.visitChildren(ctx)

    def _getMacroKey(self, ctx):
        for key in ['PARADIGM', 'DATAMODEL', 'JOB', 
                    'PARADIGMS', 'DATAMODELS', 'JOBS']:
            if hasattr(ctx, key) and getattr(ctx, key)():
                return key
            
    def _getCallKey(self, ctx):
        for c in ['CALL', "TRAIN", "PREDICT"]:
            if hasattr(ctx, c) and getattr(ctx, c)() is not None:
                return c
        return ""
        
    # Visit a parse tree produced by FGLParser#call.
    def visitCall(self, ctx: FGLParser.CallContext):
        ids = ctx.identifier()
        dname = ctx.macro_name().getText()
        key = self._getMacroKey(ctx.macro_key())
        # pdb.set_trace()
        output_identifier = None if ctx.identifier() is None else ctx.identifier().getText()
        # args = [e.getText() for e in ctx.argument().expr()]
        
        callKey = self._getCallKey(ctx)
        try:
            try:
                macro = kvdb()[f'{key}.{callKey}_{dname}']
            except:
                macro = kvdb()[f'{key}_{dname}']
        except KeyError:
            raise DSLException(f"{key} {dname} not defined")
        content = macro['block_content']
        # pdb.set_trace()
        # params
        
        param_type = {n:t for n, t in macro['parameters']}
        
        arguments = {}
        
        for (n, t), a in zip(macro['parameters'],  [] if ctx.argument() is None else ctx.argument().expr()):
            arguments[n] = (t, a)
        if ctx.setArguments() is not None:
            for arg in ctx.setArguments().setArgument():
                n, a = arg.parameter().getText(), arg.expr()
                t = param_type[n]
                arguments[n] = (t, a)
                
        for n, (t, a) in arguments.items():
            v = a.getText()
            def str_wrap(v):
                if type(v) is str:
                    return f"'{v}'"
                return str(v)
            try:
                v =  value2py(v)
            except:
                pass
            # content = content.replace(f"${n}", v)
            if t.lower() == 'json':
                # pdb.set_trace()
                for sl, con in zip(a.constant().json().STRING_LITERAL(), a.constant().json().constant()):
                    self.ipt_replacement[f"${n}.{sl.getText()[1:-1]}"] = str_wrap(con.getText())
            else:
                self.ipt_replacement[f"${n}"] = str_wrap(v)
                
        # print(self.ipt_replacement)
        # pdb.set_trace()
        content = visit(VariableMapperVisitor(output_identifier), content, ignore_parse_error=True)
        # pdb.set_trace()
        self.replacement[(self.block_index_head + ctx.start.start,
                          self.block_index_head + ctx.stop.stop + 1)] = content
        self.block_index_head += len(content) - (ctx.stop.stop + 2 - ctx.start.start)
        return self.visitChildren(ctx)

    def visitParadigm_block(self, ctx: FGLParser.Begin_blockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#expr.
    def visitExpr(self, ctx: FGLParser.ExprContext):
        return self.visitChildren(ctx)
