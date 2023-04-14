# Generated from FGL.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FGLParser import FGLParser
else:
    from FGLParser import FGLParser

# This class defines a complete listener for a parse tree produced by FGLParser.
class FGLListener(ParseTreeListener):

    # Enter a parse tree produced by FGLParser#prog.
    def enterProg(self, ctx:FGLParser.ProgContext):
        pass

    # Exit a parse tree produced by FGLParser#prog.
    def exitProg(self, ctx:FGLParser.ProgContext):
        pass


    # Enter a parse tree produced by FGLParser#sqlStatement.
    def enterSqlStatement(self, ctx:FGLParser.SqlStatementContext):
        pass

    # Exit a parse tree produced by FGLParser#sqlStatement.
    def exitSqlStatement(self, ctx:FGLParser.SqlStatementContext):
        pass


    # Enter a parse tree produced by FGLParser#dqlStatement.
    def enterDqlStatement(self, ctx:FGLParser.DqlStatementContext):
        pass

    # Exit a parse tree produced by FGLParser#dqlStatement.
    def exitDqlStatement(self, ctx:FGLParser.DqlStatementContext):
        pass


    # Enter a parse tree produced by FGLParser#ddlStatement.
    def enterDdlStatement(self, ctx:FGLParser.DdlStatementContext):
        pass

    # Exit a parse tree produced by FGLParser#ddlStatement.
    def exitDdlStatement(self, ctx:FGLParser.DdlStatementContext):
        pass


    # Enter a parse tree produced by FGLParser#dmlStatement.
    def enterDmlStatement(self, ctx:FGLParser.DmlStatementContext):
        pass

    # Exit a parse tree produced by FGLParser#dmlStatement.
    def exitDmlStatement(self, ctx:FGLParser.DmlStatementContext):
        pass


    # Enter a parse tree produced by FGLParser#load.
    def enterLoad(self, ctx:FGLParser.LoadContext):
        pass

    # Exit a parse tree produced by FGLParser#load.
    def exitLoad(self, ctx:FGLParser.LoadContext):
        pass


    # Enter a parse tree produced by FGLParser#save.
    def enterSave(self, ctx:FGLParser.SaveContext):
        pass

    # Exit a parse tree produced by FGLParser#save.
    def exitSave(self, ctx:FGLParser.SaveContext):
        pass


    # Enter a parse tree produced by FGLParser#connect.
    def enterConnect(self, ctx:FGLParser.ConnectContext):
        pass

    # Exit a parse tree produced by FGLParser#connect.
    def exitConnect(self, ctx:FGLParser.ConnectContext):
        pass


    # Enter a parse tree produced by FGLParser#disconnect.
    def enterDisconnect(self, ctx:FGLParser.DisconnectContext):
        pass

    # Exit a parse tree produced by FGLParser#disconnect.
    def exitDisconnect(self, ctx:FGLParser.DisconnectContext):
        pass


    # Enter a parse tree produced by FGLParser#config.
    def enterConfig(self, ctx:FGLParser.ConfigContext):
        pass

    # Exit a parse tree produced by FGLParser#config.
    def exitConfig(self, ctx:FGLParser.ConfigContext):
        pass


    # Enter a parse tree produced by FGLParser#create.
    def enterCreate(self, ctx:FGLParser.CreateContext):
        pass

    # Exit a parse tree produced by FGLParser#create.
    def exitCreate(self, ctx:FGLParser.CreateContext):
        pass


    # Enter a parse tree produced by FGLParser#train.
    def enterTrain(self, ctx:FGLParser.TrainContext):
        pass

    # Exit a parse tree produced by FGLParser#train.
    def exitTrain(self, ctx:FGLParser.TrainContext):
        pass


    # Enter a parse tree produced by FGLParser#predict.
    def enterPredict(self, ctx:FGLParser.PredictContext):
        pass

    # Exit a parse tree produced by FGLParser#predict.
    def exitPredict(self, ctx:FGLParser.PredictContext):
        pass


    # Enter a parse tree produced by FGLParser#setArguments.
    def enterSetArguments(self, ctx:FGLParser.SetArgumentsContext):
        pass

    # Exit a parse tree produced by FGLParser#setArguments.
    def exitSetArguments(self, ctx:FGLParser.SetArgumentsContext):
        pass


    # Enter a parse tree produced by FGLParser#setArgument.
    def enterSetArgument(self, ctx:FGLParser.SetArgumentContext):
        pass

    # Exit a parse tree produced by FGLParser#setArgument.
    def exitSetArgument(self, ctx:FGLParser.SetArgumentContext):
        pass


    # Enter a parse tree produced by FGLParser#conditions.
    def enterConditions(self, ctx:FGLParser.ConditionsContext):
        pass

    # Exit a parse tree produced by FGLParser#conditions.
    def exitConditions(self, ctx:FGLParser.ConditionsContext):
        pass


    # Enter a parse tree produced by FGLParser#macro_key.
    def enterMacro_key(self, ctx:FGLParser.Macro_keyContext):
        pass

    # Exit a parse tree produced by FGLParser#macro_key.
    def exitMacro_key(self, ctx:FGLParser.Macro_keyContext):
        pass


    # Enter a parse tree produced by FGLParser#call.
    def enterCall(self, ctx:FGLParser.CallContext):
        pass

    # Exit a parse tree produced by FGLParser#call.
    def exitCall(self, ctx:FGLParser.CallContext):
        pass


    # Enter a parse tree produced by FGLParser#ret.
    def enterRet(self, ctx:FGLParser.RetContext):
        pass

    # Exit a parse tree produced by FGLParser#ret.
    def exitRet(self, ctx:FGLParser.RetContext):
        pass


    # Enter a parse tree produced by FGLParser#module.
    def enterModule(self, ctx:FGLParser.ModuleContext):
        pass

    # Exit a parse tree produced by FGLParser#module.
    def exitModule(self, ctx:FGLParser.ModuleContext):
        pass


    # Enter a parse tree produced by FGLParser#checkOp.
    def enterCheckOp(self, ctx:FGLParser.CheckOpContext):
        pass

    # Exit a parse tree produced by FGLParser#checkOp.
    def exitCheckOp(self, ctx:FGLParser.CheckOpContext):
        pass


    # Enter a parse tree produced by FGLParser#conditionOp.
    def enterConditionOp(self, ctx:FGLParser.ConditionOpContext):
        pass

    # Exit a parse tree produced by FGLParser#conditionOp.
    def exitConditionOp(self, ctx:FGLParser.ConditionOpContext):
        pass


    # Enter a parse tree produced by FGLParser#createParadigm.
    def enterCreateParadigm(self, ctx:FGLParser.CreateParadigmContext):
        pass

    # Exit a parse tree produced by FGLParser#createParadigm.
    def exitCreateParadigm(self, ctx:FGLParser.CreateParadigmContext):
        pass


    # Enter a parse tree produced by FGLParser#createDatamodel.
    def enterCreateDatamodel(self, ctx:FGLParser.CreateDatamodelContext):
        pass

    # Exit a parse tree produced by FGLParser#createDatamodel.
    def exitCreateDatamodel(self, ctx:FGLParser.CreateDatamodelContext):
        pass


    # Enter a parse tree produced by FGLParser#createJob.
    def enterCreateJob(self, ctx:FGLParser.CreateJobContext):
        pass

    # Exit a parse tree produced by FGLParser#createJob.
    def exitCreateJob(self, ctx:FGLParser.CreateJobContext):
        pass


    # Enter a parse tree produced by FGLParser#showAlls.
    def enterShowAlls(self, ctx:FGLParser.ShowAllsContext):
        pass

    # Exit a parse tree produced by FGLParser#showAlls.
    def exitShowAlls(self, ctx:FGLParser.ShowAllsContext):
        pass


    # Enter a parse tree produced by FGLParser#showMacro.
    def enterShowMacro(self, ctx:FGLParser.ShowMacroContext):
        pass

    # Exit a parse tree produced by FGLParser#showMacro.
    def exitShowMacro(self, ctx:FGLParser.ShowMacroContext):
        pass


    # Enter a parse tree produced by FGLParser#show.
    def enterShow(self, ctx:FGLParser.ShowContext):
        pass

    # Exit a parse tree produced by FGLParser#show.
    def exitShow(self, ctx:FGLParser.ShowContext):
        pass


    # Enter a parse tree produced by FGLParser#deleteMacro.
    def enterDeleteMacro(self, ctx:FGLParser.DeleteMacroContext):
        pass

    # Exit a parse tree produced by FGLParser#deleteMacro.
    def exitDeleteMacro(self, ctx:FGLParser.DeleteMacroContext):
        pass


    # Enter a parse tree produced by FGLParser#delete.
    def enterDelete(self, ctx:FGLParser.DeleteContext):
        pass

    # Exit a parse tree produced by FGLParser#delete.
    def exitDelete(self, ctx:FGLParser.DeleteContext):
        pass


    # Enter a parse tree produced by FGLParser#begin_block.
    def enterBegin_block(self, ctx:FGLParser.Begin_blockContext):
        pass

    # Exit a parse tree produced by FGLParser#begin_block.
    def exitBegin_block(self, ctx:FGLParser.Begin_blockContext):
        pass


    # Enter a parse tree produced by FGLParser#block_content.
    def enterBlock_content(self, ctx:FGLParser.Block_contentContext):
        pass

    # Exit a parse tree produced by FGLParser#block_content.
    def exitBlock_content(self, ctx:FGLParser.Block_contentContext):
        pass


    # Enter a parse tree produced by FGLParser#argument_typing.
    def enterArgument_typing(self, ctx:FGLParser.Argument_typingContext):
        pass

    # Exit a parse tree produced by FGLParser#argument_typing.
    def exitArgument_typing(self, ctx:FGLParser.Argument_typingContext):
        pass


    # Enter a parse tree produced by FGLParser#argument.
    def enterArgument(self, ctx:FGLParser.ArgumentContext):
        pass

    # Exit a parse tree produced by FGLParser#argument.
    def exitArgument(self, ctx:FGLParser.ArgumentContext):
        pass


    # Enter a parse tree produced by FGLParser#expr.
    def enterExpr(self, ctx:FGLParser.ExprContext):
        pass

    # Exit a parse tree produced by FGLParser#expr.
    def exitExpr(self, ctx:FGLParser.ExprContext):
        pass


    # Enter a parse tree produced by FGLParser#function.
    def enterFunction(self, ctx:FGLParser.FunctionContext):
        pass

    # Exit a parse tree produced by FGLParser#function.
    def exitFunction(self, ctx:FGLParser.FunctionContext):
        pass


    # Enter a parse tree produced by FGLParser#ender.
    def enterEnder(self, ctx:FGLParser.EnderContext):
        pass

    # Exit a parse tree produced by FGLParser#ender.
    def exitEnder(self, ctx:FGLParser.EnderContext):
        pass


    # Enter a parse tree produced by FGLParser#identifier.
    def enterIdentifier(self, ctx:FGLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by FGLParser#identifier.
    def exitIdentifier(self, ctx:FGLParser.IdentifierContext):
        pass


    # Enter a parse tree produced by FGLParser#parameter.
    def enterParameter(self, ctx:FGLParser.ParameterContext):
        pass

    # Exit a parse tree produced by FGLParser#parameter.
    def exitParameter(self, ctx:FGLParser.ParameterContext):
        pass


    # Enter a parse tree produced by FGLParser#macro_name.
    def enterMacro_name(self, ctx:FGLParser.Macro_nameContext):
        pass

    # Exit a parse tree produced by FGLParser#macro_name.
    def exitMacro_name(self, ctx:FGLParser.Macro_nameContext):
        pass


    # Enter a parse tree produced by FGLParser#json.
    def enterJson(self, ctx:FGLParser.JsonContext):
        pass

    # Exit a parse tree produced by FGLParser#json.
    def exitJson(self, ctx:FGLParser.JsonContext):
        pass


    # Enter a parse tree produced by FGLParser#array.
    def enterArray(self, ctx:FGLParser.ArrayContext):
        pass

    # Exit a parse tree produced by FGLParser#array.
    def exitArray(self, ctx:FGLParser.ArrayContext):
        pass


    # Enter a parse tree produced by FGLParser#constant.
    def enterConstant(self, ctx:FGLParser.ConstantContext):
        pass

    # Exit a parse tree produced by FGLParser#constant.
    def exitConstant(self, ctx:FGLParser.ConstantContext):
        pass



del FGLParser