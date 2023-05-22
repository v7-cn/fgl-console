#!/usr/bin/env python
import sqlite3
import sys
import os

from pygments.lexers.sql import SqlLexer, RegexLexer, bygroups
from pygments.token import *
from pygments.lexer import include
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style, style_from_pygments_cls
from interpreter.cli import execute_fgl
from prompt_toolkit.formatted_text import ANSI, HTML
from prompt_toolkit.layout import FloatContainer, Float
from prompt_toolkit.widgets import Label, TextArea, Dialog, Frame
from manual import manual
from prompt import prompt

from pygments.style import Style as BaseStyle
from pygments.token import Token, Comment, Keyword, Name, String, \
     Error, Generic, Number, Operator


from pygments.lexer import RegexLexer
from pygments.token import *

class FGLLexer(RegexLexer):
    name = 'fgl'
    aliases = 'fgl'
    filenames = ['*.fgl']

    tokens = {
        'root': [
            (r'[^/]+', Text),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*?$', Comment.Singleline),
            (r'/', Text)
        ],
        'comment': [
            (r'[^*/]+', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ]
    }
    

    tokens = {
        # 'keywords': [
        #     (r'(\s+)(class|concept|typename)(\s+)', Keyword)],
        'root': [
            # (r' .*\n', Text),
            (r'\s', Whitespace),
            (r'\s[a-z][A-Z][0-9]\b', Token),
            (r'(?i)(train|predict|run|paradigm|where|and|or|not)(\b)', Keyword),
            (r'(?i)(help|exit)(\b)',  Keyword.Pseudo),
            (r'(?i)(attribute_transduction|vector_matching|temporal_evolution)(\b)', Name.Function),
             (r'(?i)(\+|\-|\=)', Operator),
            (r'(?i)(true|false)\b',Token.Literal),
            (r'\'.*?\'',String.Single),
            (r'\".*?\"',String.Double),
            
            # (r'(class|concept|typename)(\s+)', bygroups(Keyword, Whitespace)),
            # (r'\+.*(\s+)', Generic.Inserted),
            # (r'-.*(\s+)', Generic.Deleted),
            # (r'@.*(\s+)', Generic.Subheading),
            # (r'Index.*(\s+)', Generic.Heading),
            # (r'=.*(\s+)', Generic.Heading),
            include("numbers"),
            # (r'.*\n', Text),
           

        ],
        'numbers': [
            (r'(\d(?:_?\d)*\.(?:\d(?:_?\d)*)?|(?:\d(?:_?\d)*)?\.\d(?:_?\d)*)'
             r'([eE][+-]?\d(?:_?\d)*)?', Number.Float),
            (r'\d(?:_?\d)*[eE][+-]?\d(?:_?\d)*j?', Number.Float),
            (r'0[oO](?:_?[0-7])+', Number.Oct),
            (r'0[bB](?:_?[01])+', Number.Bin),
            (r'0[xX](?:_?[a-fA-F0-9])+', Number.Hex),
            (r'\d(?:_?\d)*', Number.Integer),
        ],
        'comment': [
            (r'[^*/]+', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ]
    }
    
class FGLStyle(BaseStyle):

    styles = {
        Token.Literal: "#00f",
        String: '#555',
        Number: "#00f",
        Token:                  'bold #a0a',
        Operator: '#ee2233',
        Comment:                'italic #888',
        Keyword:                'bold #0000d1',
         Keyword.Pseudo: 'bold #aa2',
        # Name:                   '#f00',
        Name.Class:             'bold #0f0',
        Name.Function:          '#2d2',
        # String:                 'bg:#eee #111',
        Text: 'bg:#eee',

        
    }
                                                
# lex = FGLLexer()
    
# print([e for e in FGLLexer().get_tokens("TRAIN PARADIGM temporal_evolution WHERE name='chickenpox' AND automl=true AND trials=10 AND output='model'")])
# exit()
from prompt_toolkit import print_formatted_text 



print_formatted_text(HTML('''\
┌─────────────[ FGL Console ]─────────────┐
│   <b>FGL</b> (<style fg="blue">Formalized Graph AI Language</style>)    │
│   Type "<b>help</b>" for more information.     │
└─────────────────────────────────────────┘\
'''))

sql_completer = WordCompleter(
    [
        "TRAIN",
        "PREDICT",
        "PARADIGM",
        "WHERE",
        "AND",
        "OR",
        
        "attribute_transduction",
        "vector_matching",
        "temporal_evolution",
    ],
    ignore_case=True,
)


    
# style = Style.from_dict(
#     {
        
#         "completion-menu.completion": "bg:#008888 #ffffff",
#         "completion-menu.completion.current": "bg:#00aaaa #000000",
#         "scrollbar.background": "bg:#88aaaa",
#         "scrollbar.button": "bg:#222222",
#         "pygments.text": "#f00",
#          "pygments.name": "#f00",
#         "pygments.generic.deleted": "#0f0",
     
#         "pygments.literal.number.float": "#00f",
#            "pygments.literal.number.integer": "#f0f",
#     }
# )
style = style_from_pygments_cls(FGLStyle)
import pdb
# pdb.set_trace()

def show_dialog():
    from prompt_toolkit.shortcuts import input_dialog
    result = input_dialog(
        title="Input dialog example", text="Please type your name:"
    ).run()
    print(result)
    
import threading
global session
def refresh_bottom_bar():
    global session
    import time
    t = 0
    while True:
        time.sleep(0.2)
        session.bottom_toolbar = get_bottom_bar(session.output.get_size().columns)
        t += 1

from pynvml import *
import psutil
nvmlInit()
nvmlHandler = nvmlDeviceGetHandleByIndex(0)
def get_bottom_bar(w=100):
    import datetime

    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent()
    gpu = nvmlDeviceGetMemoryInfo(nvmlHandler)
    html_template = ('<style bg="gray">[F1] Manual [F2] Prompt [F3] Tools [F4] Exit</style>'
             f'#@#'
             f'   <style bg="yellow">[FGL] </style>'
             f'<style fg="#ff0000"> CPU:{int(psutil.cpu_percent())}% </style>'
             f'<style fg="#00f0ff"> MEM:{int(mem.used / mem.total * 100)}%/{int(mem.used // (1024**3))}/{int(mem.total // (1024**3))}G </style>' 
             f'<style fg="#0ff000"> GPU:{int(gpu.used/gpu.total*100)}%/{gpu.used // (1024**2)}/{gpu.total // (1024**2)}M </style>'
                    )
    html_template = ('<style bg="gray">[F1] Manual [F2] Prompt [F3] Tools [F4] Exit</style>'
                      f'  <style bg="yellow">[FGL] </style>'
         f'#@#'
         f'<style bg="#ff0000"> CPU:{int(psutil.cpu_percent())}% </style>'
         f'<style bg="#00f0ff"> MEM:{int(mem.used / mem.total * 100)}%/{int(mem.used // (1024**3))}/{int(mem.total // (1024**3))}G </style>' 
         f'<style bg="#0ff000"> GPU:{int(gpu.used/gpu.total*100)}%/{gpu.used // (1024**3)}/{gpu.total // (1024**3)}G </style>'
        f'<style bg="#f0f0f0"> {datetime.datetime.now().strftime("%H:%M:%S")}</style>'
                )
    html =  HTML(html_template)
    return HTML(html_template.replace("#@#", 
                                      (w + 2 - len("".join([e[1] for e in html.formatted_text]))) * " "))
    
    
def get_rprompt_text():
    return [
        ("", " "),
        ("bg:#f00", "<FGL>"),
        ("", " "),
    ]

from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
history = InMemoryHistory()
for h in ["TRAIN PARADIGM attribute_transduction WHERE name='Cora' AND automl=true AND trials=10 AND output='model'",
         "PREDICT PARADIGM attribute_transduction WHERE name='Cora' AND model='model' AND output='classes.txt'",
         "TRAIN PARADIGM vector_matching WHERE name='./data/cora.json' AND automl=true AND trials=10 AND output='model'",
         "PREDICT PARADIGM vector_matching WHERE name='./data/cora.json' AND model='model' AND output='embedding.txt'",
         "TRAIN PARADIGM temporal_evolution WHERE name='chickenpox' AND automl=true AND trials=10 AND output='model'",
         "PREDICT PARADIGM temporal_evolution WHERE name='./data/chickenpox.json' AND model='model' AND output='temporal.txt'"]:
    history.append_string(h)
    # history.append_string(h.lower())

from prompt_toolkit.key_binding import KeyBindings
kb = KeyBindings()

@kb.add('f1')
def _(event):
    # pdb.set_trace()
    manual(event.app.output.get_size())

@kb.add('f2')
def _(event):
    prompt()
    
@kb.add('f3')
def _(event):   
    from prompt_toolkit.shortcuts import message_dialog
    message_dialog(
        title='Example dialog window',
        text='Do you want to continue?\nPress ENTER to quit.').run(in_thread=True)

from prompt_toolkit.application.current import get_app                                                                  
@kb.add('f4')
def _(event):   
    event.app.exit(result='exit')

def help():
    print('''
Commands:
    % :  fgl command
    !%: shell command
    
Shortcuts:
    F1: Manual
    F2: Prompt
    F3: Tools
    F4: Exit
    Ctrl-C: Interrupt
    Ctrl-D: Exit
    ''')
                                                                   
def main():
    global session
    
    session = PromptSession(
        refresh_interval=1,
        key_bindings=kb,
        lexer=PygmentsLexer(FGLLexer), completer=sql_completer, style=style,
                                    history=history,
                                    auto_suggest=AutoSuggestFromHistory(),
                                    enable_history_search=True
        
    )
    # pdb.set_trace()
    session.bottom_toolbar=get_bottom_bar(session.output.get_size().columns)
    
#     session.app.layout = FloatContainer(
#                             content=Label(""), 
#                             floats=[Float(xcursor=True,
#                                     ycursor=True,content=Frame(body=Label(text="Left frame\ncontent")), top=0, left=10, z_index=100)])
    
    
#     session.app.layout.container.children.insert(0, FloatContainer(
#                                                                 content=Label("########################"), 
#                                                                 floats=[Float(xcursor=True,
#                         ycursor=True,content=Frame(body=Label(text="Left frame\ncontent")), top=0, left=10, z_index=100)]))

    # pdb.set_trace()
    # exit()
    threading.Thread(target=refresh_bottom_bar, daemon=True).start()
    # pdb.set_trace()
    while True:
        try:
            text = session.prompt(HTML("<b>>>> </b>"))
            if text.startswith("!"):
                print(os.popen(text[1:]).read())
                continue
            if text.lower() == 'help':
                help()
                continue
            if text == 'exit':
                break
                
            try:
                messages = execute_fgl(text)
            except Exception as e:
                ...
            else:
                for message in messages:
                    print(message)
            # text = await session.prompt_async(HTML("<b>>>> </b>"))
            # text = await session.prompt_async()
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            break  # Control-D pressed.
        except:
            continue



    print("See You Next Time!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        db = ":memory:"
    else:
        db = sys.argv[1]

    main()
    # import asyncio
    # asyncio.run(main())
    # asyncio.run(main())