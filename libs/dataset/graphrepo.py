import os
import json
import urllib
import numpy as np
from torch_geometric_temporal.signal import StaticGraphTemporalSignal
import time
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field, In
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch.utils.data import Dataset
import numpy as np
from dagster import AssetMaterialization   
from tqdm import tqdm
import typing
from typing import Any
import optuna
from copy import deepcopy
from sklearn import metrics
from tabulate import tabulate
from libs.utils import json2data

class ChickenpoxDatasetLoader(object):
    """A dataset of county level chicken pox cases in Hungary between 2004
    and 2014. We made it public during the development of PyTorch Geometric
    Temporal. The underlying graph is static - vertices are counties and
    edges are neighbourhoods. Vertex features are lagged weekly counts of the
    chickenpox cases (we included 4 lags). The target is the weekly number of
    cases for the upcoming week (signed integers). Our dataset consist of more
    than 500 snapshots (weeks).
    """

    def __init__(self, path=None):
        self.path = path
        self._read_web_data()

    def _read_web_data(self):
        self._dataset = json.loads(open(self.path or "data/chickenpox.json").read())

    def _get_edges(self):
        self._edges = np.array(self._dataset["edges"]).T

    def _get_edge_weights(self):
        self._edge_weights = np.ones(self._edges.shape[1])

    def _get_targets_and_features(self):
        stacked_target = np.array(self._dataset["FX"])
        self.features = [
            stacked_target[i : i + self.lags, :].T
            for i in range(stacked_target.shape[0] - self.lags)
        ]
        self.targets = [
            stacked_target[i + self.lags, :].T
            for i in range(stacked_target.shape[0] - self.lags)
        ]

    def get_dataset(self, lags: int = 4) -> StaticGraphTemporalSignal:
        """Returning the Chickenpox Hungary data iterator.
        Args types:
            * **lags** *(int)* - The number of time lags.
        Return types:
            * **dataset** *(StaticGraphTemporalSignal)* - The Chickenpox Hungary dataset.
        """
        self.lags = lags
        self._get_edges()
        self._get_edge_weights()
        self._get_targets_and_features()
        dataset = StaticGraphTemporalSignal(
            self._edges, self._edge_weights, self.features, self.targets
        )
        return dataset
    
@op(config_schema={"name":Field(str, default_value='Cora', is_required=False, description="数据集名称/路径"),
                   "temporal":Field(bool, default_value=False, is_required=False, description="是否为时序图")})
def graphrepo(context)->Any:
    '''图数据集资产     
    :param name: 数据集名称    
    :return state_dict: 模型参数      
    '''
    from torch_geometric.datasets import Planetoid
    name = context.op_config['name']
    path = None
    if '/' in name or os.path.isfile(name):
        path = name
    if not context.op_config['temporal']:
        if path is not None:
            return json2data(json.loads(open(path, "r").read()))
        return Planetoid(root='./', name=context.op_config.get('name', None))
    else:
        if path is not None:
            loader = ChickenpoxDatasetLoader(path)
            dataset = loader.get_dataset()
            return dataset
        if name == 'chickenpox':
            loader = ChickenpoxDatasetLoader()
            dataset = loader.get_dataset()
            return dataset
        raise IndexError(f"Temporal dataset name: {name} unknown")