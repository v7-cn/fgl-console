import pandas as pd
import typing
from interpreter import interpreter
import logging
logging.basicConfig(level=logging.INFO)

def execute_dag(dag: str) -> typing.List[typing.Union[typing.Dict, str, list, pd.DataFrame]]:
    '''
   这里对接平台同步执行, 
   考虑一个dag可能有多个输出, 返回Schema约定为 List[dict| pd.DataFrame | str]
   前端会根据形式不同(nb/sh), 自适应选择渲染方式
   '''
    return ["dag raw output test", 
            pd.DataFrame([1,2], columns=['card']), 
            {"aaa": "bbb"}]



# from typing import List

# from fastapi import FastAPI, WebSocket, WebSocketDisconnect

# app = FastAPI()


# class ConnectionManager:
#     def __init__(self):
#         # 存放激活的ws连接对象
#         self.active_connections: List[WebSocket] = []

#     async def connect(self, ws: WebSocket):
#         # 等待连接
#         await ws.accept()
#         # 存储ws连接对象
#         self.active_connections.append(ws)

#     def disconnect(self, ws: WebSocket):
#         # 关闭时 移除ws对象
#         self.active_connections.remove(ws)

#     @staticmethod
#     async def send_personal_message(message: str, ws: WebSocket):
#         # 发送个人消息
#         await ws.send_text(message)

#     async def broadcast(self, message: str):
#         # 广播消息
#         for connection in self.active_connections:
#             await connection.send_text(message)


# manager = ConnectionManager()


# @app.websocket("/ws/{user}")
# async def websocket_endpoint(websocket: WebSocket, user: str):

#     await manager.connect(websocket)

#     await manager.broadcast(f"用户{user}进入聊天室")

#     try:
#         while True:
#             data = await websocket.receive_text()
#             await manager.send_personal_message(f"你说了: {data}", websocket)
#             await manager.broadcast(f"用户:{user} 说: {data}")

#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         await manager.broadcast(f"用户-{user}-离开")


from flask import Flask, request
import uvicorn
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def server():
    return interpreter(context=request.json.get('context',
                                                'shell').lower(),
                        statements=request.json.get('statements', ''),
                        mode=request.json.get('mode', 'direct').lower(),
                        dag_executor=execute_dag)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3308, debug=True)
    # uvicorn.run(app=app, host="0.0.0.0", port=3308)
    
    
    
    