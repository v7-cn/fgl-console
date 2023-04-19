# Generated from fgl/FGL.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FGLParser import FGLParser
else:
    from FGLParser import FGLParser

# This class defines a complete generic visitor for a parse tree produced by FGLParser.

class FGLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FGLParser#prog.
    def visitProg(self, ctx:FGLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#sqlStatement.
    def visitSqlStatement(self, ctx:FGLParser.SqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#dqlStatement.
    def visitDqlStatement(self, ctx:FGLParser.DqlStatementContext):
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


    # Visit a parse tree produced by FGLParser#connect.
    def visitConnect(self, ctx:FGLParser.ConnectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#disconnect.
    def visitDisconnect(self, ctx:FGLParser.DisconnectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#config.
    def visitConfig(self, ctx:FGLParser.ConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#create.
    def visitCreate(self, ctx:FGLParser.CreateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#train.
    def visitTrain(self, ctx:FGLParser.TrainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#predict.
    def visitPredict(self, ctx:FGLParser.PredictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#setArguments.
    def visitSetArguments(self, ctx:FGLParser.SetArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#setArgument.
    def visitSetArgument(self, ctx:FGLParser.SetArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#conditions.
    def visitConditions(self, ctx:FGLParser.ConditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#macro_key.
    def visitMacro_key(self, ctx:FGLParser.Macro_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#call.
    def visitCall(self, ctx:FGLParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#ret.
    def visitRet(self, ctx:FGLParser.RetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#module.
    def visitModule(self, ctx:FGLParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#checkOp.
    def visitCheckOp(self, ctx:FGLParser.CheckOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#conditionOp.
    def visitConditionOp(self, ctx:FGLParser.ConditionOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#contextKey.
    def visitContextKey(self, ctx:FGLParser.ContextKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#createParadigm.
    def visitCreateParadigm(self, ctx:FGLParser.CreateParadigmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#createDatamodel.
    def visitCreateDatamodel(self, ctx:FGLParser.CreateDatamodelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#createJob.
    def visitCreateJob(self, ctx:FGLParser.CreateJobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#showAlls.
    def visitShowAlls(self, ctx:FGLParser.ShowAllsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#showMacro.
    def visitShowMacro(self, ctx:FGLParser.ShowMacroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#show.
    def visitShow(self, ctx:FGLParser.ShowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#deleteMacro.
    def visitDeleteMacro(self, ctx:FGLParser.DeleteMacroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#delete.
    def visitDelete(self, ctx:FGLParser.DeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#begin_block.
    def visitBegin_block(self, ctx:FGLParser.Begin_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#block_content.
    def visitBlock_content(self, ctx:FGLParser.Block_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#argument_typing.
    def visitArgument_typing(self, ctx:FGLParser.Argument_typingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#argument.
    def visitArgument(self, ctx:FGLParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#expr.
    def visitExpr(self, ctx:FGLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#function.
    def visitFunction(self, ctx:FGLParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#ender.
    def visitEnder(self, ctx:FGLParser.EnderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#identifier.
    def visitIdentifier(self, ctx:FGLParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#parameter.
    def visitParameter(self, ctx:FGLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#macro_name.
    def visitMacro_name(self, ctx:FGLParser.Macro_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#json.
    def visitJson(self, ctx:FGLParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#array.
    def visitArray(self, ctx:FGLParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#constant.
    def visitConstant(self, ctx:FGLParser.ConstantContext):
        return self.visitChildren(ctx)



del FGLParser