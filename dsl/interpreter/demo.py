import pandas as pd
import typing
from interpreter import interpreter_websocket
from fastapi import FastAPI
import logging
config = {
    'level': logging.DEBUG, 
    'format': '[%(levelname)s] [%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d: %(message)s',
    'datefmt': '%Y-%m-%d %H:%M:%S',
}
logging.basicConfig(**config)


app = FastAPI()
@app.websocket("/ws")
@interpreter_websocket
def execute_dag(dag: str) -> typing.List[typing.Union[typing.Dict, str, list, pd.DataFrame]]:
    '''
   这里对接平台同步执行, 
   考虑一个dag可能有多个输出, 返回Schema约定为 List[dict| pd.DataFrame | str]
   前端会根据形式不同(nb/sh), 自适应选择渲染方式
   '''
    return ["dag raw output test", 
            pd.DataFrame([1,2], columns=['card']), 
            {"aaa": "bbb"}]
    
import uvicorn
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=3308, debug=True)
    uvicorn.run(app=app, host="0.0.0.0", port=3308)
    
    
    
    