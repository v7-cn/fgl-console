# Generated from FGL.g4 by ANTLR 4.11.1
from ..dsl.FGLVisitor import FGLVisitor
from ..dsl.FGLParser import FGLParser
# This class defines a complete generic visitor for a parse tree produced by FGLParser.
import pdb
from ..utils import kvdb, value2py, visit, md5, format
import json
import ast
from ..support.exceptions import DSLException
import logging

class RewriterVisitor(FGLVisitor):

    def __init__(self, output_identifier=None):
        super().__init__()
        self._replacement = {}

    # Visit a parse tree produced by FGLParser#prog.
    def visitProg(self, ctx: FGLParser.ProgContext):
        self.visitChildren(ctx)
        if ctx.stop is None:
            return ""
        content = ctx.start.getInputStream().getText(ctx.start.start,
                                                     ctx.stop.stop)
        logging.debug("重写前: %s", content)
        for k, v in self._replacement.items():
            content = content.replace(k, v)

        logging.debug("重写后: %s", content)
        return content

    # Visit a parse tree produced by FGLParser#predict.
    def visitPredict(self, ctx: FGLParser.PredictContext):
        _ = self.visitChildren(ctx)
        stat = ctx.start.getInputStream().getText(ctx.start.start,
                                                  ctx.stop.stop)
        assert ctx.module().getText() in ['model']
        args = [('model', ctx.STRING_LITERAL().getText())]
        if ctx.setArguments():
            args += [(a.parameter().getText(), a.expr().getText())
                    for a in ctx.setArguments().setArgument()]

        # pdb.set_trace()
        self._replacement[stat] = f'''RUN Predict WHERE 
            {' AND '.join([f'{k} = {v}' for k, v in args])}
            ''' + (f'AS {ctx.identifier()[0].getText()}' if ctx.identifier() else "")
        # pdb.set_trace()
        return _

    # Visit a parse tree produced by FGLParser#connect.
    def visitConnect(self, ctx: FGLParser.ConnectContext):
        _ = self.visitChildren(ctx)
        # pdb.set_trace()
        stat = ctx.start.getInputStream().getText(ctx.start.start,
                                                  ctx.stop.stop)
        args = [('format', ctx.FORMAT().getText()),
                ('endpoint', ctx.STRING_LITERAL().getText())]
        if ctx.setArguments():
            args += [(a.parameter().getText(), a.expr().getText())
                    for a in ctx.setArguments().setArgument()]

        # pdb.set_trace()
        self._replacement[stat] = f'''RUN CreateDataSource WHERE 
            {' AND '.join([f'{k} = {v}' for k, v in args])}
            ''' + (f'AS {ctx.identifier()[0].getText()}' if ctx.identifier() else "")
        # pdb.set_trace()
        return _

    # Visit a parse tree produced by FGLParser#disconnect.
    def visitDisconnect(self, ctx: FGLParser.DisconnectContext):
        _ = self.visitChildren(ctx)
        # pdb.set_trace()
        stat = ctx.start.getInputStream().getText(ctx.start.start,
                                                  ctx.stop.stop)
        args = [('format', ctx.FORMAT().getText()),
                ('endpoint', ctx.STRING_LITERAL().getText())]
        if ctx.setArguments():
            args += [(a.parameter().getText(), a.expr().getText())
                    for a in ctx.setArguments().setArgument()]

        # pdb.set_trace()
        self._replacement[stat] = f'''RUN DeleteDataSource WHERE 
            {' AND '.join([f'{k} = {v}' for k, v in args])}
            ''' + (f'AS {ctx.identifier()[0].getText()}' if ctx.identifier() else "")
        return _
