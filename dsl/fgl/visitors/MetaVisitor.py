# Generated from FGL.g4 by ANTLR 4.11.1
from ..dsl.FGLVisitor import FGLVisitor
from ..dsl.FGLParser import FGLParser
# This class defines a complete generic visitor for a parse tree produced by FGLParser.
import pdb
from collections import defaultdict
from ..utils import kvdb
import json
import pandas as pd

class MetaVisitor(FGLVisitor):
    
    def __init__(self, *args, **kwargs):
        self.output = []
        self.is_macro_change = False
        super().__init__(*args, **kwargs)
        
    # Visit a parse tree produced by FGLParser#prog.
    def visitProg(self, ctx: FGLParser.ProgContext):
        r = self.visitChildren(ctx)
        return  self.is_macro_change, self.output

    # Visit a parse tree produced by FGLParser#sqlStatement.
    def visitSqlStatement(self, ctx: FGLParser.SqlStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#identifier.
    def visitIdentifier(self, ctx: FGLParser.IdentifierContext):
        # pdb.set_trace()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FGLParser#ddlStatement.
    def visitDqlStatement(self, ctx: FGLParser.DqlStatementContext):
        # pdb.set_trace()
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

    # Visit a parse tree produced by FGLParser#createParadigm.
    def visitCreateParadigm(self, ctx: FGLParser.CreateParadigmContext):
        return self.visitChildren(ctx)
    
    def _output(self, statement,output):
        return {'statement': statement, 'output':output}
        
    
    def _showMacro(self, ctx, KEY):
        # pdb.set_trace()
        stat = ctx.start.getInputStream().getText(ctx.start.start, ctx.stop.stop)
        iden = None
        if hasattr(ctx, 'identifier') and ctx.identifier() is not None:
            iden = ctx.identifier().getText()
        tb = []
        for k, v in kvdb().items():
            if k.startswith(f'{KEY}_'):
                if iden is None or k == f'{KEY}_{iden}': 
                    tb.append({'type':KEY,
                               'config': v
                               })
                    # tb = json.dumps(v, indent=4, ensure_ascii=True)
                    
        self.output.append(self._output(stat, pd.DataFrame(tb)))
                    # print('>> SHOW PARADIGM\n', k, json.dumps(v, indent=4, ensure_ascii=True))

    # # Visit a parse tree produced by FGLParser#showParadigm.
    # Visit a parse tree produced by FGLParser#showMacro.
    def visitShowMacro(self, ctx:FGLParser.ShowMacroContext):
        # pdb.set_trace()
        self._showMacro(ctx, self._getMacroKey(ctx))
        return self.visitChildren(ctx)

    def _getMacroKey(self, ctx):
        for key in ['PARADIGM', 'DATAMODEL', 'JOB', 
                    'PARADIGMS', 'DATAMODELS', 'JOBS']:
            if hasattr(ctx, key) and getattr(ctx, key)():
                return key
            
    # Visit a parse tree produced by FGLParser#showParadigm.
    def visitDeleteMacro(self, ctx:FGLParser.DeleteMacroContext):
        # pdb.set_trace()
        key = self._getMacroKey(ctx)
        iden = None
        if hasattr(ctx, 'identifier') and ctx.identifier() is not None:
            iden = ctx.identifier().getText()
        for k, v in kvdb().items():
            if k.startswith(f'{key}_'):
                if iden is None or k == f'{key}_{iden}': 
                    del kvdb()[k]
                    self.is_macro_change = True
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FGLParser#showParadigm.
    def visitShowAlls(self, ctx:FGLParser.ShowAllsContext):
        key = self._getMacroKey(ctx)
        assert key in ['PARADIGMS', "DATAMODELS", "JOBS"]
        key = key[:-1]
        keys = []
        for k, v in kvdb().items():
            if k.startswith(f'{key}_'):
                keys.append("_".join(k.split("_")[1:]))
        stat = ctx.start.getInputStream().getText(ctx.start.start, ctx.stop.stop)
        self.output.append(self._output(stat, pd.DataFrame(keys, columns=['name'])))
        return self.visitChildren(ctx)

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
