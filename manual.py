#!/usr/bin/env python
"""
A simple example of a few buttons and click handlers.
"""
from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box, Button, Frame, Label, TextArea
from prompt_toolkit.formatted_text import ANSI, HTML
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl

# Event handlers for all the buttons.
attribute_transduction = HTML('''\
<u>属性传导范式</u>
    <b>* 训练(内置数据集)</b>
    > TRAIN PARADIGM attribute_transduction WHERE name='Cora' AND automl=true AND trials=10 AND output='model'
    
    <b>* 预测  </b>
    > PREDICT PARADIGM attribute_transduction WHERE name='Cora' AND model='model' AND output='classes.txt'
    
    <b>* 训练(外部数据集)</b>
    > TRAIN PARADIGM attribute_transduction WHERE name='./data/cora.json' AND automl=true AND trials=10 AND output='model'
    
    <b>* 查看模型文件</b>
    > !ls model
    
    <b>* 查看预测结果</b>
    > !cat classes.txt
''')

vector_matching = HTML('''\
<u>向量化匹配范式</u>
    <b>* 训练(内置数据集)</b>
    > TRAIN PARADIGM vector_matching WHERE name='./data/cora.json' AND automl=true AND trials=10 AND output='model'
    
    <b>* 预测  </b>
    > PREDICT PARADIGM vector_matching WHERE name='./data/cora.json' AND model='model' AND output='embedding.txt'
    
    <b>* 查看模型文件</b>
    > !ls model
    
    <b>* 查看预测结果</b>
    > !cat embedding.txt
''')


temporal_evolution = HTML('''\
<u>时序图演变范式</u>
    <b>* 训练(内置数据集)</b>
    > TRAIN PARADIGM temporal_evolution WHERE name='chickenpox' AND automl=true AND trials=10 AND output='model'
    
    <b>* 预测  </b>
    > PREDICT PARADIGM temporal_evolution WHERE name='./data/chickenpox.json' AND model='model' AND output='temporal.txt'
    
    <b>* 查看模型文件</b>
    > !ls model
    
    <b>* 查看预测结果</b>
    > !cat temporal.txt
''')

def button1_clicked():
    text_area.content.text = attribute_transduction


def button2_clicked():
    text_area.content.text = vector_matching


def button3_clicked():
    text_area.content.text = temporal_evolution


def exit_clicked():
    get_app().exit()


# All the widgets for the UI.
button1 = Button("* 属性传导范式", handler=button1_clicked, width=25)
button2 = Button("* 向量化匹配范式", handler=button2_clicked, width=25)
button3 = Button("* 时序图演变范式", handler=button3_clicked, width=25)
button4 = Button("Exit", handler=exit_clicked)
text_area = Window(content=FormattedTextControl(text=attribute_transduction))


# Combine all the widgets in a UI.
# The `Box` object ensures that padding will be inserted around the containing
# widget. It adapts automatically, unless an explicit `padding` amount is given.



# Key bindings.
kb = KeyBindings()
kb.add("tab")(focus_next)
kb.add("s-tab")(focus_previous)


# Styling.
style = Style(
    [
        ("left-pane", "bg:#888800 #000000"),
        ("right-pane", "bg:#00aa00 #000000"),
        ("button", "#000000"),
        ("button-arrow", "#000000"),
        ("button focused", "bg:#ff0000"),
        ("text-area focused", "bg:#ff0000"),
    ]
)


# Build a main application object.

def manual(size):
    root_container = Box(
        HSplit(
            [
                Label(text="Press `Tab` to move the focus."),
                VSplit(
                    [
                        Box(
                            body=HSplit([button1, button2, button3, button4], padding=1),
                            padding=1,
                            style="class:left-pane",
                            # width=50,
                        ),
                        Box(body=Frame(text_area), width=size.columns - 50, height=size.rows - 5, padding=1, style="class:right-pane"),
                    ]
                ),
            ]
        ),
    )

    layout = Layout(container=root_container, focused_element=button1)

    application = Application(layout=layout, key_bindings=kb, style=style, full_screen=True)


    application.run(in_thread=True)


# if __name__ == "__main__":
#     main()
