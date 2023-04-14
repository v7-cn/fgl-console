import hashlib
import random
from antlr4 import FileStream, CommonTokenStream
from antlr4.InputStream import InputStream
from .dsl.FGLLexer import FGLLexer
from .dsl.FGLParser import FGLParser
import shelve
import os
import pdb
import json
import pandas as pd
from .support.exceptions import DSLParseException
import logging
os.makedirs(f'{os.path.dirname(__file__)}/data', exist_ok=True)
db = shelve.open(f'{os.path.dirname(__file__)}/data/kv.db', flag='c')
def kvdb():
    return db

def debug(dsl):
    s = CommonTokenStream(FGLLexer(InputStream(dsl)))
    parser = FGLParser(s)
    parse_tree = parser.prog()
    s.fill()
    logging.debug("## ParseTree:\n %s", parse_tree.toStringTree(recog=parser))
    logging.debug("## TOKEN:")
    stat = ""
    for cc in s.tokens:
        stat += f'{cc.text} \033[96m {parser.symbolicNames[cc.type]} \033[0m'
    logging.debug(stat)


def dag2dot(dag):
    # json.dumps(n['node_attrs'])
    def get_attr(a):
        ks, vs = [], []
        for k, v in a.items():
            if k in 'module':
                continue
            if type(v) is list:
                v = ','.join(v)
            if type(v) is dict:
                v = get_attr(v)
            ks.append(str(k) + ":")
            vs.append(str(v))
        if len(ks) == 0:
            return ''
        return f'|{{{"|".join(ks)}}}|{{{"|".join(vs)}}}'
    
    def get_label(n):
        # |{input:|output:}|{{[(?, ?)]}|{[(?, ?)]}}
        return f"{n['name']}\\nID: {n['id']}\\n{n.get('node_attrs', {}).get('module', '')}\\n{get_attr(n['node_attrs'])}"
    
    dag = json.loads(dag) if type(dag) is str else dag
    # pdb.set_trace()
    nodes = '\n'.join([f"{n['id']}[label=\"{get_label(n)}\"]" for n in dag['nodes']])
    edges = '\n'.join([f"{e['source']} -> {e['target']} [label=\"SourcePort: {e['source_port']}\\nTargetPort: {e['target_port']}\"];" for e in dag['edges']])
    dot = f"""
digraph G {{
	node[shape=record fontsize=8]
    edge [fontsize=8]
    subgraph cluster_L {{ \"\" [fontsize=12 color="#b22800" shape=box label=\"Note:\l{dag['canvas']['description']}\l{dag['canvas']['name']}\"] }}
{nodes}
{edges}
}}
    """
    return dot

def dot2svg(src):
   import graphviz
   rt = graphviz.Digraph(body=src[src.index('{'):-src[::-1].index("}")])  
   return rt.pipe(format='svg').decode('utf8')
    
def value2py(v):
    if type(v) is str and len(v) >= 2 and v[0] == '`' and v[-1] == '`':
        v = f"'{v[1:-1]}'"
    # v = ''.join(v.split())
    if v == 'false':
        v = 'False'
    if v == 'true':
        v = 'True'
    
    return eval(v)


def md5(L=32):
    return hashlib.md5(str(random.gauss(0, 1)).encode('utf8')).hexdigest()[:L]


def format(s):
    import re
    s = re.sub(r';[\ \n\r\t]*?;', ';', s)
    s = re.sub(r';[\r\n\ \t]*', ';\n', s)
    s = re.sub(r'^[\ \r\n\t]*', '', s)
    return s

from antlr4.error.ErrorListener import ErrorListener

class DSLErrorListener(ErrorListener):
    def __init__(self):
        super(ErrorListener, self).__init__()
        # self.src = src
        
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        logging.info("reportAmbiguity")
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        logging.info("reportAttemptingFullContext")
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        logging.info("reportContextSensitivity")
        pass

    def syntaxError(self, recog, symbol, line, col, msg, e):
        logging.info("PARSE ERROR:")
        logging.warning(recog, symbol, line, col, msg, e)
        # fmt = "%s\n%s\n%s"
        # marker = "~" * col + "^"
        
        # if msg.startswith("missing"):
        #     err = fmt % (msg, self.src, marker)
        # elif msg.startswith("no viable"):
        #     err = fmt % ("I expected something else here", self.src, marker)
        # elif msg.startswith("mismatched"):
        #     names = PSParser.literalNames
        #     expected = [names[i] for i in e.getExpectedTokens() if i < len(names)]
        #     if expected < 10:
        #         expected = " ".join(expected)
        #         err = (fmt % ("I expected one of these: " + expected,
        #             self.src, marker))
        #     else:
        #         err = (fmt % ("I expected something else here", self.src, marker))
        # else:
        #     err = fmt % ("I don't understand this", self.src, marker)
        raise DSLParseException(f"{recog}, {symbol}, {line}, {col}, {msg}, {e}")


def visit(visitor, dsl, ignore_parse_error = False):
    # lexer.addErrorListener(ErrorListener())
    # print("A")
    lexer = FGLLexer(InputStream(dsl))
    parser = FGLParser(CommonTokenStream(lexer))
    if not ignore_parse_error:
        lexer.addErrorListener(DSLErrorListener())
        parser.addErrorListener(DSLErrorListener())
    r =  visitor.visit(parser.prog())
    # print("B")
    return  r


def extract_mode(statements, default_mode=None):
   import re
   modes = re.findall('(?i)^\s*%(sh|shell|dag|dag\+json|python|py|fgl|dsl|debug|explain|profile)[\s]*[$|\n]', statements)
   if len(modes) > 0:
      m = modes[0]
      return m, statements.replace("%" + m, "")
   return default_mode, statements


def render_notebook_cell(opt, max_cols = 20, max_rows = 20):
    if isinstance(opt, pd.DataFrame):
        return  {
            'content': opt.to_html(classes='table table-stripped', max_cols=max_cols, max_rows=max_rows),
            'mime': 'text/html'
        }
    if isinstance(opt, dict):
        return  {
            'content': json.dumps(opt, indent=4, ensure_ascii=False),
            'mime': 'text/x-json'
        }
    if isinstance(opt, str):
        return {
            'content': opt,
            'mime': 'text/html'
        }
    # print(f"unknown type: {type(opt)}", opt)
    return {"content": opt}


def render_shell(opt):
    from tabulate import tabulate
    if isinstance(opt, pd.DataFrame):
        return  {
            'content': tabulate(opt, headers='keys', tablefmt="psql"),
        }
    if isinstance(opt, dict):
        return  {
            'content': json.dumps(opt, indent=4, ensure_ascii=False),
        }
    if isinstance(opt, str):
        return {
            'content': opt,
        }
    # print(f"unknown type: {type(opt)}", opt)
    return {"content": opt}

def return_status(status='success', **kwargs):
    return {
        'status': status,
        'status_options': kwargs
    }

def render_return(opt, _type='shell', extra={}):
    default_extra = return_status()
    default_extra.update(extra)
    if _type == 'shell':
        opt = render_shell(opt)
        opt.update(extra)
    elif _type == 'notebook':
        opt = render_notebook_cell(opt)
        opt.update(extra)
    else:
        print(f"unknown render type: {_type} {type(opt)}", opt)
    return opt
    
    
def random_df():
    import pandas as pd
    import numpy as np
    return pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                              columns=list('ABCD'))