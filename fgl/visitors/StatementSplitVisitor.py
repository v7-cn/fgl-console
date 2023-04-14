# Generated from FGL.g4 by ANTLR 4.11.1
from ..dsl.FGLVisitor import FGLVisitor
from ..dsl.FGLParser import FGLParser
# This class defines a complete generic visitor for a parse tree produced by FGLParser.
import pdb
from collections import defaultdict


class StatementSplitVisitor(FGLVisitor):

    # Visit a parse tree produced by FGLParser#prog.
    def visitProg(self, ctx:FGLParser.ProgContext):
        # pdb.set_trace()
        stats = defaultdict(list)
        for child in ctx.children:
            if hasattr(child, 'start'):
                statement_sql = child.start.getTokenSource().inputStream.getText(child.start.start, child.stop.stop) + ';'
                if hasattr(child, 'ddlStatement') and child.ddlStatement() is not None:
                    stats['ddl'].append(statement_sql)
                elif hasattr(child, 'dmlStatement') and child.dmlStatement() is not None:
                    stats['dml'].append(statement_sql)
                elif hasattr(child, 'dqlStatement') and child.dqlStatement() is not None:
                    stats['dql'].append(statement_sql)
                # print(child.getRuleIndex(), statement_sql)
        return dict(stats)
        # r = self.visitChildren(ctx)[0]
        # return 'asfasfds'
        return r

    def aggregateResult(self, aggregate, nextResult):
        # print(aggregate, nextResult)
        if aggregate is None:
            aggregate = []
        if (type(nextResult) is list and len(nextResult) > 0) or \
            (type(nextResult) is not list and  nextResult is not None):
            aggregate.append(nextResult)
        return aggregate

    # Visit a parse tree produced by FGLParser#sqlStatement.
    def visitSqlStatement(self, ctx:FGLParser.SqlStatementContext):
        pdb.set_trace()
        stats = defaultdict(list)
        for child in ctx.children:
            statement_sql = child.start.getTokenSource().inputStream.getText(child.start.start, child.stop.stop)
            stats[FGLParser.ruleNames[child.getRuleIndex()]].append(statement_sql + ';')
        return dict(stats)
        
    # Visit a parse tree produced by FGLParser#identifier.
    def visitIdentifier(self, ctx:FGLParser.IdentifierContext):
        # pdb.set_trace()
        print("Iden:", ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#ddlStatement.
    def visitDdlStatement(self, ctx:FGLParser.DdlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#dmlStatement.
    def visitDmlStatement(self, ctx:FGLParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#load.
    def visitLoad(self, ctx:FGLParser.LoadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#save.
    def visitSave(self, ctx:FGLParser.SaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#train.
    def visitTrain(self, ctx:FGLParser.TrainContext):
        # print(ctx)
        # pdb.set_trace()
        return self.visitChildren(ctx)

    def visitParadigm_block(self, ctx:FGLParser.Begin_blockContext):
        
        statement_sql = ctx.block_content().start.getTokenSource().inputStream.getText(
            ctx.block_content().start.start,
            ctx.block_content().stop.stop)
        # pdb.set_trace()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#expr.
    def visitExpr(self, ctx:FGLParser.ExprContext):
        return self.visitChildren(ctx)


