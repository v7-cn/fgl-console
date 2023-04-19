import json
import graphviz
from fgl import FGL
from fgl.utils import visit, format, dag2dot, dot2svg, extract_mode, render_return, return_status
import pandas as pd
import typing
import pdb
from fgl.support.exceptions import DSLException, DSLParseException
import json
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import logging
'''
解释器协议
Requests:
    {
        context: 'shell',
        statements: 'xxxx
                    xxx',
        mode: 'direct'
    }
    
Response:
    DAG实际执行的result为多行
     [{
            content:,
            mime:,
            status:,
            status_options:,
        }]
        
    'reference_change': false, # 参考手册是否发生了变动, 通知vscode更新侧边栏
    
'''


def _interpreter(
        context,
        statements,
        mode,
        debug=False,
        dag_executor=lambda dag: ['undefine']) -> typing.List[typing.Any]:
    assert context in ['shell', 'notebook']
    # 解析查询语句中的 mode 关键字
    _mode, statements = extract_mode(statements, default_mode='fgl')
    # 全局配置解析模式优先级更高
    mode = _mode if mode == 'direct' else mode
    output = []
    if debug:
        logging.debug(("CONTEXT", context, "MODE:", mode, "Statements:", statements))
    if mode in ['fgl', 'dsl', 'dag', 'dag+json', 'debug']:
        # 解析: DAG
        res = FGL().parse(statements, dumps=True)
        output = res.get("output", [])
        # Render DAG
        dag = res.get("dag", None)
        logging.debug("dag: %s %s", dag, type(dag))
        if dag not in [None, "", "null"]:
            dag = json.loads(res.get("dag", ""))
            if mode in ['fgl', 'dsl']:
                dag_output = dag_executor(dag)
                assert type(dag_output) is list
                output += [{'statement': 'dag', 'output': o} for o in dag_output]
            elif mode in ['dag+json']:
                yield render_return(dag, context)
            elif mode in ['dag']:
                dag_res = dag2dot(dag)
                if context == 'notebook':
                    dag_res = dot2svg(dag_res)
                yield render_return(dag_res, context)
            # 调试模式
            elif mode in ['debug']:
                yield render_return('error result xxx',
                                    context,
                                    extra=return_status(
                                        'error', message='debug content xxx'))
        # 该dag执行会改变meta
        yield None, {'reference_change': res.get('reference_change', False)}
    # python 模式
    elif mode in ['python']:
        import io
        from contextlib import redirect_stdout
        with io.StringIO() as buf, redirect_stdout(buf):
            exec("def _anoymous_function():\n" + "\n    ".join((statements).split("\n")))
            _opt = eval("_anoymous_function()")
            popt = buf.getvalue()
            if popt not in ["", None]:
                yield render_return(popt,
                                    context)
            if _opt is not None:
                yield render_return(_opt,
                                context)
        
    elif mode in ['sh', 'shell']:
        import os
        yield render_return(os.popen(statements).read(),
                            context)
    
    # 不支持的运行 mode
    else:
        yield render_return('error',
                            context,
                            extra=return_status(
                                'error', message=f'unknown mode {mode}'))

    for opt in output:
        assert type(opt) in [str, pd.DataFrame, list, dict
                             ], f'{type(opt)}({opt}) not support auto render'

    # Render output item
    for opt in output:
        if mode in ['dag+json'] and isinstance(opt['output'], pd.DataFrame):
            opt['output'] = opt['output'].to_dict('records')
        yield render_return(opt['output'],
                            context,
                            extra={'statement': opt['statement']})

    


def interpreter(*args, **kwargs):
    # try:
    _res = list(_interpreter(*args, **kwargs))
    logging.debug("_RES: %s", _res)
    result = list(filter(lambda x: type(x) is not tuple, _res))
    config = dict(sum(map(lambda x: list(x[1].items()), 
                     filter(lambda x: type(x) is tuple, _res)), []))
    return result, config


class ConnectionManager:

    def __init__(self):
        # 存放激活的ws连接对象
        self.active_connections: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        self.active_connections.append(ws)

    def disconnect(self, ws: WebSocket):
        # 关闭时 移除ws对象
        self.active_connections.remove(ws)

    @staticmethod
    async def send_personal_message(message: str, ws: WebSocket):
        # 发送个人消息
        await ws.send_text(message)

    async def broadcast(self, message: str):
        # 广播消息
        for connection in self.active_connections:
            await connection.send_text(message)

import traceback
def interpreter_websocket(execute_dag):
    manager = ConnectionManager()

    async def websocket_endpoint(websocket: WebSocket):
        token, resp = "", {}
        await manager.connect(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                r = json.loads(data)
                token, req = r['token'], r['request']
                result, config = interpreter(context=req.get('context', 'shell').lower(),
                                   statements=req.get('statements', ''),
                                   mode=req.get('mode', 'direct').lower(),
                                   dag_executor=execute_dag)
                await manager.send_personal_message(
                    json.dumps({
                        'token': token,
                        'response': result
                    }), websocket)
                actions = []
                if config.get('reference_change', False):
                    actions.append("refresh_macro_view")
                if len(actions) > 0:
                    await manager.broadcast(json.dumps({'actions': actions}))
                # await manager.broadcast(f"用户:{user} 说: {data}")

        except WebSocketDisconnect:
            manager.disconnect(websocket)
            # await manager.broadcast(f"用户-{user}-离开")
        except Exception:
            error = [{
                'content':  traceback.format_exc(),
                'mime': 'text/plain',
                'status': None,
                'status_options': None
            }]
            await manager.send_personal_message(
                json.dumps({
                    'token': token,
                    'response': error
                }), websocket)

    return websocket_endpoint
