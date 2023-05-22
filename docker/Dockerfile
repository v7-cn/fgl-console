FROM python:3.9
RUN python3 -m pip install antlr4-python3-runtime==4.11.1 antlr4-tools==0.1 graphviz==0.20.1 tabulate==0.9.0 \
    coverage==7.1.0 uvicorn==0.20.0 contextvars==2.4 pandas numpy scipy ipython \
    fastapi dagster dagit torch optuna -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python3 -m pip install torch_geometric torch_geometric_temporal -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN echo '#!/usr/local/bin/python3.9  \nimport sys\nsys.path.append("/data")\nfrom interpreter.cli import fgl\nfgl()'  > /usr/bin/fgl && chmod +x /usr/bin/fgl
WORKDIR /data
