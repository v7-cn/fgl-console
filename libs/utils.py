
import numpy as np
def summary_model(model):
    params = []
    params_collect = []
    for k,p in model.named_parameters():
        params.append(np.prod(p.shape).item())
        params_collect.append("{:>20} {:>20} {:>30} {:>20}".format(str(k), str(p.dtype), str(p.shape), str(np.prod(p.shape))))    
    return {'模型结构':str(model).split("\n"),
    '模型参数量': params_collect,
    "总参数量": sum(params)}
    
from torch_geometric.data.data import Data
import numpy as np
from torch_geometric.data.data import Data
import numpy as np
import torch
def data2json(data):
    features = {k:v for k,v in enumerate(data.x.tolist()[:10])}
    edges = [{'source':f.item(), 'target': t.item()} for f,t in data.edge_index.T.detach().numpy()]
    return {"nodes":features, 'edges': edges, 'y': data.y.tolist()}

def json2data(obj):
    obj['nodes'] = {int(k):v for k,v in obj['nodes'].items()}
    features = np.zeros((max(list(obj['nodes'].keys())) + 1, len(list(obj['nodes'].values())[0])))
    for nid in range(max(obj['nodes'].keys())):
        features[nid] = obj['nodes'][nid]
    edges = np.array([[e['source'], e['target']] for e in obj['edges']]).T
    y = obj['y']
    mask = torch.ones(len(y), dtype=torch.long)
    return ListDataset([Data(x=torch.Tensor(features), 
                             edge_index=torch.LongTensor(edges), 
                             y=torch.LongTensor(y), 
                             train_mask=mask, 
                             test_mask=mask, 
                             valid_mask=mask)])


from torch.utils.data import Dataset
class ListDataset(Dataset):

    def __init__(self, records):
        self.records = records
        d = records[0]
        self.num_node_features = len(d.x[0])
        self.num_classes = len(set(d.y))

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        return self.records[idx]