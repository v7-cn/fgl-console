# Generated from FGL.g4 by ANTLR 4.11.1
from ..dsl.FGLVisitor import FGLVisitor
from ..dsl.FGLParser import FGLParser
# This class defines a complete generic visitor for a parse tree produced by FGLParser.
import pdb
from collections import defaultdict
from ..utils import kvdb
import json


class DDLVisitor(FGLVisitor):
    def __init__(self, *args, **kwargs):
        self.is_macro_change = False
        super().__init__(*args, **kwargs)
        
    # Visit a parse tree produced by FGLParser#prog.
    def visitProg(self, ctx: FGLParser.ProgContext):
        self.visitChildren(ctx)
        return self.is_macro_change

    def aggregateResult(self, aggregate, nextResult):
        # print(aggregate, nextResult)
        if aggregate is None:
            aggregate = []
        if (type(nextResult) is list and len(nextResult) > 0) or \
            (type(nextResult) is not list and  nextResult is not None):
            aggregate.append(nextResult)
        return aggregate

    # Visit a parse tree produced by FGLParser#sqlStatement.
    def visitSqlStatement(self, ctx: FGLParser.SqlStatementContext):
        return self.visitChildren(ctx)
        # pdb.set_trace()
        # stats = defaultdict(list)
        # for child in ctx.children:
        #     statement_sql = child.start.getInputStream().getText(child.start.start, child.stop.stop)
        #     stats[FGLParser.ruleNames[child.getRuleIndex()]].append(statement_sql + ';')
        # return dict(stats)

    # Visit a parse tree produced by FGLParser#identifier.
    def visitIdentifier(self, ctx: FGLParser.IdentifierContext):
        # pdb.set_trace()
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
        # print(ctx)
        # pdb.set_trace()
        return self.visitChildren(ctx)

    def _createMacro(self, ctx, KEY):

        name = ctx.IDENTIFIER().getText()
        if hasattr(ctx, 'argument_typing'):
            args = [(k.getText(), v.getText())
                    for k, v in zip(ctx.argument_typing().expr(),
                                    ctx.argument_typing().TYPING())]
        else:
            args = []
        origin_sql = ctx.start.getInputStream().getText(
            ctx.start.start, ctx.stop.stop)
        block_content = ctx.start.getInputStream().getText(
            ctx.begin_block().block_content().start.start,
            ctx.begin_block().block_content().stop.stop)
        # pdb.set_trace()
        # print(paradigm_name, paradigm_args, block_content)
        arguments = {}
        if KEY == 'JOB':
            if ctx.setArguments() is not None:
                for a in ctx.setArguments().setArgument():
                    arguments[a.parameter().getText()] = a.expr().getText()
        
        if hasattr(ctx, 'contextKey'):
            sub_macro = ctx.contextKey().getText().upper()
        else:
            sub_macro = ""
        kvdb()[f'{KEY}{sub_macro}_{name}'] = {
            'parameters': args,
            'origin_sql': origin_sql,
            'block_content': block_content,
            'arguments': arguments
        }
        self.is_macro_change = True

    # Visit a parse tree produced by FGLParser#createParadigm.
    def visitCreateParadigm(self, ctx: FGLParser.CreateParadigmContext):
        self._createMacro(ctx, 'PARADIGM')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#createParadigm.
    def visitCreateDatamodel(self, ctx: FGLParser.CreateParadigmContext):
        # print("A")
        self._createMacro(ctx, 'DATAMODEL')
        return self.visitChildren(ctx)

    def visitCreateJob(self, ctx: FGLParser.CreateParadigmContext):
        self._createMacro(ctx, 'JOB')
        return self.visitChildren(ctx)

    # def _showMacro(self, ctx, KEY):
    #     # pdb.set_trace()
    #     iden = None
    #     if hasattr(ctx, 'identifier') and ctx.identifier() is not None:
    #         iden = ctx.identifier().getText()
    #     for k, v in kvdb().items():
    #         if k.startswith(f'{KEY}_'):
    #             if iden is None or k == f'{KEY}_{iden}':
    #                 pass
    #                 # print('>> SHOW PARADIGM\n', k, json.dumps(v, indent=4, ensure_ascii=True))

    # # # Visit a parse tree produced by FGLParser#showParadigm.
    # # Visit a parse tree produced by FGLParser#showMacro.
    # def visitShowMacro(self, ctx:FGLParser.ShowMacroContext):
    #     # pdb.set_trace()
    #     return self.visitChildren(ctx)

    def visitParadigm_block(self, ctx: FGLParser.Begin_blockContext):
        # statement_sql = ctx.block_content().start.getTokenSource(
        # ).inputStream.getText(ctx.block_content().start.start,
        #                       ctx.block_content().stop.stop)
        # print("Block:", statement_sql)
        # pdb.set_trace()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#expr.
    def visitExpr(self, ctx: FGLParser.ExprContext):
        return self.visitChildren(ctx)
