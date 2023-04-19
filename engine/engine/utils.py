
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op, Field, in_process_executor, load_assets_from_current_module


def canvas_node_prefix_module(dag:dict)->dict:
    '''基于canvas dag 美化
    '''
    from copy import deepcopy
    from collections import defaultdict
    r = deepcopy(dag)
    node_ids,node_type_set = {}, defaultdict(set)
    
    for n in r['nodes']:
        node_type_set[n['module_id']].add(n['id'])
    
    for n in r['nodes']:
        node_ids[n['id']] = n['module_id'] + ('@' + n['id'].replace("node_", "") if len(node_type_set[n['module_id']]) > 1 else "")
        n['id'] = node_ids[n['id']]
        
    for e in r['edges']:
        e['source'] = node_ids.get(e['source'], e['source'])
        e['target'] = node_ids.get(e['target'], e['target'])
    return r

def get_module_input_pos_name(op_defs, module_name:str, pos:int):
    '''获取module指定位置的参数名称
    '''
    for op in op_defs:
        if op.__name__ == module_name:
            return op.input_defs[pos].name
    return None

import typing
from dagster import DependencyDefinition, GraphDefinition, NodeInvocation, op
@op
def op_output_any()->typing.Any:
    '''返回Any, 可供所有op链接
    '''
    return None

def construct_graph_with_op_defs(op_defs, name=None) -> GraphDefinition:
    ''' 构建 dagster DAG of all ops
    '''
    deps = {}
    for op in op_defs:
        op_deps_entry = {}
        for opipt in op.input_defs:
            op_deps_entry[opipt.name] = DependencyDefinition(
                node='op_output_any', output='result'
            )
        deps[NodeInvocation(name=op.__name__, alias=op.__name__)] = op_deps_entry
    return GraphDefinition(
        name='operators_list',
        description='Operators List',
        node_defs=op_defs + [op_output_any],
        dependencies=deps,
        node_input_source_assets=None
    )
    

def construct_graph_with_canvas(dag, op_defs, name=None) -> GraphDefinition:
    '''基于canvas dag 构建 dagster DAG
    '''
    assert isinstance(dag, dict)
    deps = {}
    ops_needed = {}
    for ncfg in dag["nodes"]:
        def_name = ncfg["node_attrs"]["module"]
        ops_needed[def_name] = list(filter(lambda m: m.__name__ == def_name, op_defs))[0]
    ops_needed_mapper = {k:v for k,v in ops_needed.items()}
    ops_needed = list(ops_needed.values())
    # fill none default
    # for op in op_defs:
    #     for ipt in op.input_defs:
    #         deps[NodeInvocation(name=op.__name__, alias=ipt.name)] = None
    # fill edge value
    non_op_used = False
    for ncfg in dag["nodes"]:
        def_name = ncfg["node_attrs"]["module"]
        alias = ncfg.get("id", "def_name")
        op_deps_entry = {}
        # for op in op_defs:
        # import pdb
        # pdb.set_trace()
        for ipt in ops_needed_mapper[def_name].input_defs:
            op_deps_entry[ipt.name] = DependencyDefinition(
                node='op_output_any', output='result'
            )
        for edge in list(filter(lambda x: x['target'] == alias, dag['edges'])):
            op_deps_entry[get_module_input_pos_name(ops_needed, def_name, edge['target_port'])] = DependencyDefinition(
                node=edge['source'], output='result'
            )
        # print("OPDE:", op_deps_entry)
        # import pdb
        # pdb.set_trace()
        # print(op_deps_entry)
        for _, v in op_deps_entry.items():
            if v.node == 'op_output_any':
                non_op_used = True
        deps[NodeInvocation(name=def_name, alias=alias)] = op_deps_entry
    return GraphDefinition(
        name=name or dag['canvas']["name"].replace("-", "_"),
        description=dag['canvas']["description"],
        node_defs=ops_needed + ([op_output_any] if non_op_used else []),
        dependencies=deps,
        node_input_source_assets=None
    )