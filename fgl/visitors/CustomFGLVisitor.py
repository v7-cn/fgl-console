# Generated from FGL.g4 by ANTLR 4.11.1
from antlr4 import FileStream, CommonTokenStream
from antlr4.InputStream import InputStream
from ..dsl.FGLLexer import FGLLexer
from ..dsl.FGLParser import FGLParser
from ..dsl.FGLVisitor import FGLVisitor
from ..dsl.FGLParser import FGLParser
from ..MacroExpansionVisitor import MacroExpansionVisitor
# This class defines a complete generic visitor for a parse tree produced by FGLParser.
import pdb


class CustomFGLVisitor(FGLVisitor):

    # Visit a parse tree produced by FGLParser#prog.
    def visitProg(self, ctx: FGLParser.ProgContext):
        r = self.visitChildren(ctx)
        print("Prog:", r)
        return 'asfasdf'
        return r

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
        statement_type = FGLParser.ruleNames[ctx.getChild(
            0).getRuleIndex()]
        statement_sql = ctx.start.getTokenSource().inputStream.getText(
            ctx.start.start, ctx.stop.stop)
        if statement_type == 'dmlStatement':
            print('dmlStatement:', statement_sql)
            return statement_sql
        else:

            return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#call.
    def visitCall(self, ctx: FGLParser.CallContext):
        pdb.set_trace()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#identifier.
    def visitIdentifier(self, ctx: FGLParser.IdentifierContext):
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

    def visitParadigm_block(self, ctx: FGLParser.Paradigm_blockContext):

        block = ctx.block_content().start.getTokenSource().inputStream.getText(
            ctx.block_content().start.start,
            ctx.block_content().stop.stop)

        block_after = MacroRewriterVisitor().visit(
            FGLParser(CommonTokenStream(FGLLexer(
                InputStream(block)))).prog())

        print("Block:", block, block_after)
        # pdb.set_trace()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#expr.
    def visitExpr(self, ctx: FGLParser.ExprContext):
        return self.visitChildren(ctx)


# del FGLParser