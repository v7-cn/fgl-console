import time
from dagster import Definitions, load_assets_from_modules, op,job, JobDefinition
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field, in_process_executor, load_assets_from_current_module
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch.utils.data import Dataset
import numpy as np
from .utils import *
import os
import sys
sys.path.insert(0, os.path.dirname(__file__) + "/../../")
from libs import ops


def fgljobs(dags, names=None):
    from copy import deepcopy
    jobs = []
    if names is None:
        names = [None] * len(dags)
    for dag, name in zip(dags, names):
        r = canvas_node_prefix_module(dag)
        config = {}
        for n in r['nodes']:
            cfg = deepcopy(n['node_attrs'])
            if 'module' in cfg.keys():
                del cfg['module']
            config[n['id']] = {'config': cfg}
        config = {'ops': config}
        job = construct_graph_with_canvas(r, ops, name).to_job(name=name or "attribute_transducation", config=config, executor_def=in_process_executor)
        jobs.append(job)
    return jobs
    
import sys
import os
from fgl import FGL
import json

def load_jobs_from_location(loc):
    import glob
    dags, keys = zip(*[(json.loads(open(f).read()), os.path.basename(f).replace(".json", "")) for f in glob.glob(loc + "/*.json")])
    all_ops = construct_graph_with_op_defs(ops, None).to_job(name="all_ops", executor_def=in_process_executor)
    return fgljobs(dags, keys) + [all_ops]

_ = Definitions(
    # jobs=[]
    jobs=load_jobs_from_location(os.path.dirname(__file__) + "/../jobs")
)

