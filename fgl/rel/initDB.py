# -*- coding: UTF-8 -*-
import os
import sys


modules = [
    {"DataSource": [
        {
            "_id": "DataSet",
            "name": "数据集",
            "category": "数据源组件",
            "type": "DataSource",
            "index": 0,
            "subindex": 5,
            "maindef": ["libs.datamodel.datasource.dataset", "dataset"],
            "input_port_num": 0,
            "output_port_num": 1,
            "input_ports": [],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "ds_id",
                    "value": "",
                    "default": "",
                    "label": "数据集",
                    "isdepand": False,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "dataset"
                    }
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"DataProcess": [
        {
            "_id": "Distinct",
            "name": "数据去重",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 5,
            "maindef": ["libs.datamodel.dataprocess.data_distinct", "data_distinct"],
            "attrs": [
                {
                    "name": "distinct_type",
                    "value": "row",
                    "default": "row",
                    "label": "去重方式",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["row", "col"]
                    }
                },
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "label": "选择去重列",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Union",
            "name": "数据Union",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 8,
            "maindef": ["libs.datamodel.dataprocess.data_union", "data_union"],
            "input_port_num": 2,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集1",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                },
                {
                    "id": 1,
                    "default": [],
                    "label": "输入数据集2",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "attrs": [],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Select",
            "name": "列选择",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 5,
            "maindef": ["libs.datamodel.dataprocess.data_select", "data_select"],
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "label": "选择列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Rename",
            "name": "列重命名",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 5,
            "maindef": ["libs.datamodel.dataprocess.data_rename", "data_rename"],
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "label": "选择列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Filter",
            "name": "数据过滤",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 5,
            "maindef": ["libs.datamodel.dataprocess.data_filter", "data_filter"],
            "attrs": [
                {
                    "name": "condition",
                    "value": {},
                    "default": {},
                    "label": "过滤条件",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Join",
            "name": "数据Join",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 9,
            "maindef": ["libs.datamodel.dataprocess.data_join", "data_join"],
            "input_port_num": 2,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集1",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                },
                {
                    "id": 1,
                    "default": [],
                    "label": "输入数据集2",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "join_type",
                    "value": "inner",
                    "default": "inner",
                    "label": "join类型",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["inner", "left", "right", "outer"]
                    }
                }, {
                    "name": "left_key_col",
                    "value": "",
                    "default": "",
                    "isdepand": True,
                    "isupdate": False,
                    "label": "左侧数据集连接列"
                }, {
                    "name": "right_key_col",
                    "value": "",
                    "default": "",
                    "isdepand": True,
                    "isupdate": False,
                    "label": "右侧数据集连接列"
                }, {
                    "name": "left_output_cols",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": True,
                    "label": "左侧数据集输出列"
                }, {
                    "name": "right_output_cols",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": True,
                    "label": "右侧数据集输出列"
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Split",
            "name": "数据拆分",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 7,
            "maindef": ["libs.datamodel.dataprocess.data_split", "data_split"],
            "input_port_num": 1,
            "output_port_num": 2,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集1",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                },
                {
                    "id": 1,
                    "default": [],
                    "label": "输出数据集2",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "split_rate",
                    "type": "float",
                    "value": 0.8,
                    "default": 0.8,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "拆分比例",
                    "selected": {
                        "type": "list",
                        "option": [0.5, 0.6, 0.7, 0.8, 0.9]
                    }
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "CastType",
            "name": "数据类型转换",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 6,
            "maindef": ["libs.datamodel.dataprocess.data_cast_type", "data_cast_type"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "选择列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "cast_type",
                    "value": "STRING",
                    "default": "STRING",
                    "isdepand": False,
                    "isupdate": False,
                    "label": "数据转换类型",
                    "selected": {
                        "type": "list",
                        "option": ["STRING", "INT", "BIGINT", "FLOAT", "DOUBLE"]
                    }
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "CustomSpark",
            "name": "自定义pyspark脚本",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 10,
            "maindef": ["libs.datamodel.dataprocess.data_custom_spark", "data_custom_spark"],
            "input_port_num": 4,
            "output_port_num": 4,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集1",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": False
                },
                {
                    "id": 1,
                    "default": [],
                    "label": "输入数据集2",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": False
                },
                {
                    "id": 2,
                    "default": [],
                    "label": "输入数据集3",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": False
                },
                {
                    "id": 3,
                    "default": [],
                    "label": "输入数据集4",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": False
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集1",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": False

                },
                {
                    "id": 1,
                    "default": [],
                    "label": "输出数据集2",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": False
                },
                {
                    "id": 2,
                    "default": [],
                    "label": "输出数据集3",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": False
                },
                {
                    "id": 3,
                    "default": [],
                    "label": "输出数据集4",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": False
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "codeContent",
                    "value": "IyAtKi0gY29kaW5nOiBVVEYtOCAtKi0KIyMjCiMg6Ieq5a6a5LmJc3BhcmvohJrmnKzmqKHniYh2MS4wCiMjIwoKIyDms6jmhI/kuovpobnvvJoKIyAx44CB6Ieq5a6a5LmJ5qih54mI5Ye95pWw5ZCN56ew5LiN6IO95L+u5pS5CiMgMuOAgeWHveaVsOWPguaVsOS4jeiDveS/ruaUue+8jOaUr+aMgei+k+WFpeacgOWkmjTkuKpzcGFyayBEYXRhRnJhbWXvvIzmjInnhafoioLngrnovpPlhaXnq6/lj6Pku47lt6bliLDlj7Ppobrluo/lr7nlupRkZjHjgIFkZjLjgIFkZjPjgIFkZjQKIyAz44CB5Ye95pWw6L6T5Ye65pWw6YeP5b+F6aG75Li6NOS4qu+8jOWPr+S7peaYr3NwYXJrIERhdGFGcmFtZeaIlk5vbmXvvIzmjInnhafoioLngrnovpPlh7rnq6/lj6Pku47lt6bliLDlj7Plr7nlupQKIyA044CB5Ye95pWw5YaF57yW6L6R6Ieq5a6a5LmJc3Bhcmvku6PnoIHvvIzku4XmlK/mjIFweXNwYXJr55u45YWz5bqTYXBp6LCD55SoCmRlZiBjdXN0b21fc3BhcmsoZGYxLCBkZjIsIGRmMywgZGY0LCBzcGFyayk6CiAgICAiIiIKICAgIOWHveaVsOWGhee8lui+keiHquWumuS5ieeahHNwYXJr6ISa5pys5Luj56CBCiAgICAiIiIKICAgICMg6LCD55SocHlzcGFya+ebuOWFs2Fwaeagt+S+i++8mgogICAgIyBmcm9tIHB5c3Bhcmsuc3FsLmZ1bmN0aW9ucyBpbXBvcnQgKgogICAgcmV0dXJuIGRmMSwgZGYyLCBkZjMsIGRmNAoK",
                    "default": "IyAtKi0gY29kaW5nOiBVVEYtOCAtKi0KIyMjCiMg6Ieq5a6a5LmJc3BhcmvohJrmnKzmqKHniYh2MS4wCiMjIwoKIyDms6jmhI/kuovpobnvvJoKIyAx44CB6Ieq5a6a5LmJ5qih54mI5Ye95pWw5ZCN56ew5LiN6IO95L+u5pS5CiMgMuOAgeWHveaVsOWPguaVsOS4jeiDveS/ruaUue+8jOaUr+aMgei+k+WFpeacgOWkmjTkuKpzcGFyayBEYXRhRnJhbWXvvIzmjInnhafoioLngrnovpPlhaXnq6/lj6Pku47lt6bliLDlj7Ppobrluo/lr7nlupRkZjHjgIFkZjLjgIFkZjPjgIFkZjQKIyAz44CB5Ye95pWw6L6T5Ye65pWw6YeP5b+F6aG75Li6NOS4qu+8jOWPr+S7peaYr3NwYXJrIERhdGFGcmFtZeaIlk5vbmXvvIzmjInnhafoioLngrnovpPlh7rnq6/lj6Pku47lt6bliLDlj7Plr7nlupQKIyA044CB5Ye95pWw5YaF57yW6L6R6Ieq5a6a5LmJc3Bhcmvku6PnoIHvvIzku4XmlK/mjIFweXNwYXJr55u45YWz5bqTYXBp6LCD55SoCmRlZiBjdXN0b21fc3BhcmsoZGYxLCBkZjIsIGRmMywgZGY0LCBzcGFyayk6CiAgICAiIiIKICAgIOWHveaVsOWGhee8lui+keiHquWumuS5ieeahHNwYXJr6ISa5pys5Luj56CBCiAgICAiIiIKICAgICMg6LCD55SocHlzcGFya+ebuOWFs2Fwaeagt+S+i++8mgogICAgIyBmcm9tIHB5c3Bhcmsuc3FsLmZ1bmN0aW9ucyBpbXBvcnQgKgogICAgcmV0dXJuIGRmMSwgZGYyLCBkZjMsIGRmNAoK",
                    "isdepand": False,
                    "isupdate": False,
                    "label": "自定义代码"
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "EasySample",  # id
            "name": "简单采样",  # 组件名
            "category": "数据处理组件",  # 组件分类
            "type": "DataProcess",  # 组件类型
            "index": 5,  # 组件类别
            "subindex": 18,  # 组件索引
            "maindef": ["libs.datamodel.dataprocess.data_easy_sample", "data_easy_sample"],
            "attrs": [  # 组件配置信息
                {
                    "name": "sample_mode",
                    "value": 'random_sample',  # 存储参数配置的值
                    "default": 'random_sample',  # 参数默认值
                    "label": "采样方法",
                    "isdepand": False,  # 是否依赖输入数据,若依赖,输入改变则配置为默认值
                    "isupdate": False,  # 是否影响输出数据,若影响,输出改变则使输出节点配置重置为默认
                    "selected": {
                        "type": "list",
                        "option": ["random_sample", "stratified_sampling"]
                    }
                },
                {
                    "name": "fraction",
                    "value": 0.5,
                    "default": 0.5,
                    "label": "采样比例",
                    "isdepand": False,
                    "isupdate": False,
                },
                {
                    "name": "number",
                    "value": 100,
                    "default": 100,
                    "label": "采样数量",
                    "isdepand": False,
                    "isupdate": False,  # 是否影响输出数据
                },
                {
                    "name": "sample_calculation_method",
                    "value": 'ratio',  # 存储参数配置的值
                    "default": 'ratio',  # 参数默认值
                    "label": "采样方式",
                    "isdepand": False,  # 是否依赖输入数据,若依赖,输入改变则配置为默认值
                    "isupdate": False,  # 是否影响输出数据,若影响,输出改变则使输出节点配置重置为默认
                    "selected": {
                        "type": "list",
                        "option": ["ratio", "number"]
                    }
                },
                {
                    "name": "seed",
                    "value": 0,
                    "default": 0,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                },
                {
                    "name": "with_replacement",
                    "value": False,  # 存储参数配置的值
                    "default": False,  # 参数默认值
                    "label": "是否放回",
                    "isdepand": False,  # 是否依赖输入数据,若依赖,输入改变则配置为默认值
                    "isupdate": False,  # 是否影响输出数据,若影响,输出改变则使输出节点配置重置为默认
                    "selected": {
                        "type": "list",
                        "option": [True, False]
                    }
                },
                {
                    "name": "label_col",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                },
            ],
            "input_port_num": 1,  # 输入端口数量
            "output_port_num": 1,  # 输出端口数量
            "input_ports": [  # 输入端口信息
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [  # 输出端口信息
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [  # 组件菜单栏支持操作
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "NegativeSample",  # id
            "name": "欠采样",  # 组件名
            "category": "数据处理组件",  # 组件分类
            "type": "DataProcess",  # 组件类型
            "index": 5,  # 组件类别
            "subindex": 11,  # 组件索引
            "maindef": ["libs.datamodel.dataprocess.data_negative_sample", "data_negative_sample"],
            "attrs": [  # 组件配置信息
                {
                    "name": "sample_rate",
                    "value": 0.1,  # 存储参数配置的值
                    "default": 0.1,  # 参数默认值
                    "label": "采样率",
                    "isdepand": False,  # 是否依赖输入数据,若依赖,输入改变则配置为默认值
                    "isupdate": False,  # 是否影响输出数据,若影响,输出改变则使输出节点配置重置为默认

                },
                {
                    "name": "label_col",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",  # 前端通过此类型判断如何交互
                        "option": "schema"
                    }

                },
                {
                    "name": "label_value",
                    "value": None,
                    "default": None,
                    "label": "标签值",
                    "isdepand": True,
                    "isupdate": False,  # 是否影响输出数据
                }
            ],
            "input_port_num": 1,  # 输入端口数量
            "output_port_num": 1,  # 输出端口数量
            "input_ports": [  # 输入端口信息
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [  # 输出端口信息
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [  # 组件菜单栏支持操作
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "ExportMysql",
            "name": "导出Mysql",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 99,
            "maindef": ["libs.datamodel.dataprocess.data_ds_to_mysql", "data_ds_to_mysql"],
            "attrs": [
                {
                    "name": "host",
                    "value": "",
                    "default": "",
                    "label": "HOST",
                    "isdepand": False,
                    "isupdate": False,  # 是否影响输出数据
                },
                {
                    "name": "port",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "PORT",
                    "isdepand": False,
                    "isupdate": False,  # 是否影响输出数据
                },
                {
                    "name": "db_name",
                    "value": "",
                    "default": "",
                    "label": "数据库名",
                    "isdepand": False,
                    "isupdate": False,  # 是否影响输出数据
                },
                {
                    "name": "table_name",
                    "value": "",
                    "default": "",
                    "label": "表名",
                    "isdepand": False,
                    "isupdate": False,  # 是否影响输出数据
                },
                {
                    "name": "user",
                    "value": "",
                    "default": "",
                    "label": "用户名",
                    "isdepand": False,
                    "isupdate": False,  # 是否影响输出数据
                },
                {
                    "name": "password",
                    "value": "",
                    "default": "",
                    "label": "密码",
                    "isdepand": False,
                    "isupdate": False,  # 是否影响输出数据
                },
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "ExportHBase",
            "name": "导出HBase",
            "category": "数据处理组件",
            "type": "DataProcess",
            "index": 5,
            "subindex": 5,
            "maindef": ["libs.datamodel.dataprocess.data_export_hbase", "data_export_hbase"],
            "attrs": [
                {
                    "name": "host",
                    "value": "",
                    "default": "",
                    "label": "HOST",
                    "isdepand": False,
                    "isupdate": False
                }, {
                    "name": "port",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "PORT",
                    "isdepand": False,
                    "isupdate": False
                }, {
                    "name": "zk_hosts",
                    "value": "",
                    "default": "",
                    "label": "zk地址",
                    "isdepand": False,
                    "isupdate": False
                },
                # {
                #     "name": "namespace",
                #     "value": "",
                #     "default": "",
                #     "label": "命名空间",
                #     "isdepand": False,
                #     "isupdate": False
                # },
                {
                    "name": "tablename",
                    "value": "",
                    "default": "",
                    "label": "表名",
                    "isdepand": False,
                    "isupdate": False
                }, {
                    "name": "rowkey",
                    "value": "",
                    "default": "",
                    "label": "选择rowkey列",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",  # 前端通过此类型判断如何交互
                        "option": "schema"
                    }
                }, {
                    "name": "column_family",
                    "value": [],
                    "default": [],
                    "label": "配置列族",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",  # 前端通过此类型判断如何交互
                        "option": "schema"
                    }
                }
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"StatisticalAnalysis": [
        {
            "_id": "CorrelationMatrix",
            "name": "相关系数矩阵",
            "category": "统计分析组件",
            "type": "StatisticalAnalysis",
            "index": 10,
            "subindex": 1,
            "maindef": ["libs.datamodel.dataprocess.data_correlation_matrix", "data_correlation_matrix"],
            "attrs": [  # 组件配置信息
                {
                    "name": "choose_way",
                    "value": "pearson",
                    "default": "pearson",  # 参数默认值
                    "label": "相关系数计算方式",
                    "isdepand": False,  # 是否依赖输入数据,若依赖,输入改变则配置为默认值
                    "isupdate": False,  # 是否影响输出数据,若影响,输出改变则使输出节点配置重置为默认
                    "selected": {
                        "type": "list",
                        "option": ["pearson", "spearman"]
                    }
                },
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "label": "检验列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                },
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewStat",
                    "label": "查看相关系数结果"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Cov",
            "name": "数据协方差",
            "category": "统计分析组件",
            "type": "StatisticalAnalysis",
            "index": 10,
            "subindex": 2,
            "maindef": ["libs.datamodel.dataprocess.data_cov", "data_cov"],
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "label": "检验列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                },
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集1",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewStat",
                    "label": "查看协方差结果"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Student_T",
            "name": "单样本T检验",
            "category": "统计分析组件",
            "type": "StatisticalAnalysis",
            "index": 10,
            "subindex": 3,
            "maindef": ["libs.datamodel.dataprocess.data_student_T", "data_student_T"],
            "attrs": [  # 组件配置信息
                {
                    "name": "cols",
                    "value": "",
                    "default": "",
                    "label": "检验列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                },
                {
                    "name": "mean",
                    "value": 0,
                    "default": 0,  # 参数默认值
                    "label": "总体均值",
                    "isdepand": False,  # 是否依赖输入数据,若依赖,输入改变则配置为默认值
                    "isupdate": False,  # 是否影响输出数据,若影响,输出改变则使输出节点配置重置为默认

                }
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewStat",
                    "label": "查看单样本T检验结果"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Histogram",
            "name": "直方图",
            "category": "统计分析组件",
            "type": "StatisticalAnalysis",
            "index": 10,
            "subindex": 15,
            "maindef": ["libs.datamodel.dataprocess.data_histogram", "data_histogram"],
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "label": "选择要统计的列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                },
                {
                    "name": "interval_num",
                    "type": "int",
                    "value": 10,
                    "default": 10,
                    "label": "区间个数",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewStat",
                    "label": "查看直方图统计结果"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "exportDataset",
                    "label": "导出数据集"
                },
                {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Normal_test",
            "name": "正态检验",
            "category": "统计分析组件",
            "type": "StatisticalAnalysis",
            "index": 10,
            "subindex": 17,
            "maindef": ["libs.datamodel.dataprocess.data_normal_test", "data_normal_test"],
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "label": "选择列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                },
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewStat",
                    "label": "查看正态检验结果"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "exportDataset",
                    "label": "导出数据集"
                },
                {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "AutoRegression",
            "name": "AutoRegression",
            "category": "统计分析组件",
            "type": "StatisticalAnalysis",
            "index": 10,
            "subindex": 18,
            "maindef": ["libs.datamodel.dataprocess.data_auto_regression", "data_auto_regression"],
            "attrs": [  # 组件配置信息
                {
                    "name": "test_col",
                    "value": "",
                    "default": "",
                    "label": "检验列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                },
                {
                    "name": "sort_col",
                    "value": "",
                    "default": "",
                    "label": "排序列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                },
                {
                    "name": "lag",
                    "type": "int",
                    "value": 100,
                    "default": 100,  # 参数默认值
                    "label": "最大lag",
                    "isdepand": False,  # 是否依赖输入数据,若依赖,输入改变则配置为默认值
                    "isupdate": False,  # 是否影响输出数据,若影响,输出改变则使输出节点配置重置为默认
                }
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewStat",
                    "label": "查看AR统计结果"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "F_Test",
            "name": "F检验",
            "category": "统计分析组件",
            "type": "StatisticalAnalysis",
            "index": 10,
            "subindex": 12,
            "maindef": ["libs.datamodel.dataprocess.data_f_test", "data_f_test"],
            "attrs": [
                {
                    "name": "feature",
                    "value": "",
                    "default": "",
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                },
                {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewStat",
                    "label": "查看F检验统计结果"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                },
                {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "KSTest",
            "name": "KS检验",
            "category": "统计分析组件",
            "type": "StatisticalAnalysis",
            "index": 10,
            "subindex": 13,
            "maindef": ["libs.datamodel.dataprocess.data_ks_test", "data_ks_test"],
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "label": "检验列",
                    "isdepand": True,
                    "isupdate": False,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                },
                {
                    "name": "alternative",
                    "value": "two-sided",
                    "default": "two-sided",
                    "label": "替代方式",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["two-sided", "less", "greater"]
                    }
                },
                {
                    "name": "mode",
                    "value": "auto",
                    "default": "auto",
                    "label": "计算模式",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["auto", "asym", "exact"]
                    }
                },
            ],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewStat",
                    "label": "查看KS检验结果"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                },
                {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]
    },
    {"FeatureEngineering": [
        {
            "_id": "Normalization",
            "name": "归一化",
            "category": "特征工程组件",
            "type": "FeatureEngineering",
            "index": 10,
            "subindex": 5,
            "maindef": ["libs.datamodel.dataprocess.data_normalization", "data_normalization"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "label": "选择列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "normal_type",
                    "value": "maxmin",
                    "default": "maxmin",
                    "label": "归一化方式",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["maxmin", "zscore", "lognormal"]
                    }
                }, {
                    "name": "keep_original_col",
                    "value": False,
                    "default": False,
                    "label": "是否保留原始列",
                    "isdepand": False,
                    "isupdate": True,
                    "selected": {
                        "type": "list",
                        "option": [False, True]
                    }
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "OutlierHandle",
            "name": "异常值处理",
            "category": "特征工程组件",
            "type": "FeatureEngineering",
            "index": 10,
            "subindex": 6,
            "maindef": ["libs.datamodel.dataprocess.data_handle_outlier", "data_handle_outlier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "选择列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "outlier_type",
                    "value": "",
                    "default": "",
                    "isdepand": True,
                    "isupdate": False,
                    "label": "异常值类型",
                    "selected": {
                        "type": "list",
                        "option": ["NULL", "NAN", "NULLORNAN", "EMPTY", "NULLOREMPTY"]
                    }
                }, {
                    "name": "replace_type",
                    "value": "CUSTOMVALUE",
                    "default": "CUSTOMVALUE",
                    "isdepand": True,
                    "isupdate": False,
                    "label": "填充类型",
                    "selected": {
                        "type": "list",
                        "option": ["MIN", "MAX", "MEAN", "QUANTILE", "MODE", "RANDOM", "CUSTOMVALUE"]
                    }
                }, {
                    "name": "quantile_value",
                    "value": 0.5,
                    "default": 0.5,
                    "isdepand": True,
                    "isupdate": False,
                    "label": "分位数值",
                    "selected": {
                        "type": "list",
                        "option": [0.25, 0.5, 0.75]
                    },
                    "cod": {"replace_type": "QUANTILE"}
                }, {
                    "name": "custom_value",
                    "value": "",
                    "default": "",
                    "isdepand": True,
                    "isupdate": False,
                    "label": "自定义值",
                    "cod": {"replace_type": "CUSTOMVALUE"}
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Binning",
            "name": "分箱",
            "category": "特征工程组件",
            "type": "FeatureEngineering",
            "index": 10,
            "subindex": 7,
            "maindef": ["libs.datamodel.dataprocess.data_binning", "data_binning"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": True,
                    "label": "选择列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "bin_type",
                    "value": "QUANTILES",
                    "default": "QUANTILES",
                    "isdepand": False,
                    "isupdate": False,
                    "label": "分箱方式",
                    "selected": {
                        "type": "list",
                        "option": ["QUANTILES", "CUSTOMRANGE"]
                    }
                }, {
                    "name": "bin_num",
                    "type": "int",
                    "value": 10,
                    "default": 10,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "分箱数量",
                    "cod": {"bin_type": "QUANTILES"}
                }, {
                    "name": "custom_bin_num",
                    "type": "int",
                    "value": "",
                    "default": "",
                    "isdepand": True,
                    "isupdate": False,
                    "label": "自定义分箱数量",
                    "sample": "col1:5;col2:8",
                    "cod": {"bin_type": "QUANTILES"}
                }, {
                    "name": "custom_expression",
                    "value": "",
                    "default": "",
                    "isdepand": True,
                    "isupdate": False,
                    "label": "自定义分箱区间",
                    "sample": "0,10;col1:1,5;col2:2,6",
                    "cod": {"bin_type": "CUSTOMRANGE"}
                }, {
                    "name": "keep_original_col",
                    "value": False,
                    "default": False,
                    "isdepand": False,
                    "isupdate": True,
                    "label": "是否保留原始列",
                    "selected": {
                        "type": "list",
                        "option": [False, True]
                    }
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "ValueReplace",
            "name": "数值替换",
            "category": "特征工程组件",
            "type": "FeatureEngineering",
            "index": 10,
            "subindex": 8,
            "maindef": ["libs.datamodel.dataprocess.data_replace_value", "data_replace_value"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "commands",
                    "value": [],
                    "dafault": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "数值替换指令",
                    "sample": [
                        {
                            "expression": ["age", "<", 10], "replace_value": 9
                        }
                    ]
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "OneHot",
            "name": "onehot编码",
            "category": "特征工程组件",
            "type": "FeatureEngineering",
            "index": 10,
            "subindex": 9,
            "maindef": ["libs.datamodel.dataprocess.data_onehot", "data_onehot"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }, {
                    "id": "debugConsole",
                    "label": "命令行调试"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "cols",
                    "value": [],
                    "default": [],
                    "label": "选择列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "onehot_type",
                    "value": "onehot",
                    "default": "onehot",
                    "label": "编码方式",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["onehot"]
                    }
                }, {
                    "name": "keep_original_col",
                    "value": False,
                    "default": False,
                    "label": "是否保留原始列",
                    "isdepand": False,
                    "isupdate": True,
                    "selected": {
                        "type": "list",
                        "option": [False, True]
                    }
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": True,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"Algorithm": [
        {
            "_id": "DTBinaryClassifier",
            "name": "决策树二分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 5,
            "maindef": ["libs.datamodel.mlalgorithm.DTBinaryClassifier", "DTBinaryClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_structure",
                    "label": "查看解释性"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树最大深度",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 100,
                            "step": 2,
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 100,
                            "step": 2,
                        }
                    }
                }, {
                    "name": "criterion",
                    "value": "gini",
                    "default": "gini",
                    "label": "信息增益计算策略",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["gini", "entropy"]
                    }
                }, {
                    "name": "max_leaf_nodes",
                    "type": "int",
                    "value": 32,
                    "default": 32,
                    "label": "最大分支数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2,
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2,
                        }
                    }
                }, {
                    "name": "min_impurity_decrease",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "最小信息熵增益",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "min_samples_split",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "节点最小样本数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2,
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2,
                        }
                    }
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }

            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "二分类算法",
                "algorithm_name": "决策树二分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "DTMultiClassifier",
            "name": "决策树多分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 10,
            "maindef": ["libs.datamodel.mlalgorithm.DTMultiClassifier", "DTMultiClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_structure",
                    "label": "查看解释性"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树最大深度",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 100,
                            "step": 2,
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 100,
                            "step": 2,
                        }
                    }
                }, {
                    "name": "criterion",
                    "value": "gini",
                    "default": "gini",
                    "label": "信息增益计算策略",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["gini", "entropy"]
                    }
                }, {
                    "name": "max_leaf_nodes",
                    "type": "int",
                    "value": 32,
                    "default": 32,
                    "label": "最大分支数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2,
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2,
                        }
                    }
                }, {
                    "name": "min_impurity_decrease",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "最小信息熵增益",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "min_samples_split",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "节点最小样本数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2,
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2,
                        }
                    }
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "多分类算法",
                "algorithm_name": "决策树多分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "DTRegressor",
            "name": "决策树回归",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 15,
            "maindef": ["libs.datamodel.mlalgorithm.DTRegressor", "DTRegressor"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树最大深度",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 100,
                            "step": 2,
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 100,
                            "step": 2,
                        }
                    }
                }, {
                    "name": "max_leaf_nodes",
                    "type": "int",
                    "value": 32,
                    "default": 32,
                    "label": "最大分支数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 100,
                            "step": 2
                        }
                    }
                }, {
                    "name": "min_impurity_decrease",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "最小信息熵增益",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "min_samples_split",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "节点最小样本数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    }
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "回归算法",
                "algorithm_name": "决策树回归",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "RFBinaryClassifier",
            "name": "随机森林二分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 20,
            "maindef": ["libs.datamodel.mlalgorithm.RFBinaryClassifier", "RFBinaryClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "max_features",
                    "value": "auto",
                    "default": "auto",
                    "label": "特征采样数量",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["number", "auto", "all", "log2", "sqrt", "part"]
                    }
                }, {
                    "name": "n_estimators",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树的数量",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树最大深度",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "criterion",
                    "value": "gini",
                    "default": "gini",
                    "label": "信息增益计算策略",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["gini", "entropy"]
                    }
                }, {
                    "name": "min_impurity_decrease",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "最小信息熵增益",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "min_samples_split",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "节点最小样本数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    }
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "int": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "二分类算法",
                "algorithm_name": "随机森林二分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "RFMultiClassifier",
            "name": "随机森林多分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 25,
            "maindef": ["libs.datamodel.mlalgorithm.RFMultiClassifier", "RFMultiClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "max_features",
                    "value": "auto",
                    "default": "auto",
                    "label": "特征采样数量",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["number", "auto", "all", "log2", "sqrt", "part"]
                    }
                }, {
                    "name": "n_estimators",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树的数量",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树最大深度",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "criterion",
                    "value": "gini",
                    "default": "gini",
                    "label": "信息增益计算策略",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["gini", "entropy"]
                    }
                }, {
                    "name": "min_impurity_decrease",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "最小信息熵增益",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "min_samples_split",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "节点最小样本数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    }
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "多分类算法",
                "algorithm_name": "随机森林多分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "RFRegressor",
            "name": "随机森林回归",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 30,
            "maindef": ["libs.datamodel.mlalgorithm.RFRegressor", "RFRegressor"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "max_features",
                    "value": "auto",
                    "default": "auto",
                    "label": "特征采样数量",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["number", "auto", "all", "log2", "sqrt", "part"]
                    }
                }, {
                    "name": "n_estimators",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树的数量",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树最大深度",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "criterion",
                    "value": "gini",
                    "default": "gini",
                    "label": "信息增益计算策略",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["gini", "entropy"]
                    }
                }, {
                    "name": "min_impurity_decrease",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "最小信息熵增益",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "min_samples_split",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "节点最小样本数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    },

                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "回归算法",
                "algorithm_name": "随机森林回归",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GBDTBinaryClassifier",
            "name": "GBDT二分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 35,
            "maindef": ["libs.datamodel.mlalgorithm.GBDTBinaryClassifier", "GBDTBinaryClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树最大深度",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 0,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 0,
                            "high": 100,
                            "step": 2
                        }
                    }
                }, {
                    "name": "max_leaf_nodes",
                    "type": "int",
                    "value": 32,
                    "default": 32,
                    "label": "最大分支数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    }
                }, {
                    "name": "min_impurity_decrease",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "最小信息熵增益",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "min_samples_split",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "节点最小样本数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 20,
                            "step": 1
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 20,
                            "step": 1
                        }
                    }
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "subsample",
                    "type": "float",
                    "value": 1.0,
                    "default": 1.0,
                    "label": "训练基百分比",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "float",
                        "config": {
                            "low": 0.1,
                            "high": 1.0,
                            "step": 0.1
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 0.1,
                            "high": 1.0,
                            "step": 0.1
                        }
                    }
                }, {
                    "name": "n_estimators",
                    "type": "int",
                    "value": 100,
                    "default": 100,
                    "label": "最大迭代次数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 200,
                            "step": 10
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 200,
                            "step": 10
                        }
                    }
                }, {
                    "name": "learning_rate",
                    "type": "float",
                    "value": 0.1,
                    "default": 0.1,
                    "label": "学习率",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "二分类算法",
                "algorithm_name": "GBDT二分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GBDTMultiClassifier",
            "name": "GBDT多分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 40,
            "maindef": ["libs.datamodel.mlalgorithm.GBDTMultiClassifier", "GBDTMultiClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树最大深度",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 0,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 0,
                            "high": 100,
                            "step": 2
                        }
                    }
                }, {
                    "name": "max_leaf_nodes",
                    "type": "int",
                    "value": 32,
                    "default": 32,
                    "label": "最大分支数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    }
                }, {
                    "name": "min_impurity_decrease",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "最小信息熵增益",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "min_samples_split",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "节点最小样本数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 20,
                            "step": 1
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 20,
                            "step": 1
                        }
                    }
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "subsample",
                    "type": "float",
                    "value": 1.0,
                    "default": 1.0,
                    "label": "训练基百分比",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "float",
                        "config": {
                            "low": 0.1,
                            "high": 1.0,
                            "step": 0.1
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 0.1,
                            "high": 1.0,
                            "step": 0.1
                        }
                    }
                }, {
                    "name": "n_estimators",
                    "type": "int",
                    "value": 100,
                    "default": 100,
                    "label": "最大迭代次数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 200,
                            "step": 10
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 200,
                            "step": 10
                        }
                    }
                }, {
                    "name": "learning_rate",
                    "type": "float",
                    "value": 0.1,
                    "default": 0.1,
                    "label": "学习率",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "多分类算法",
                "algorithm_name": "GBDT多分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GBDTRegressor",
            "name": "GBDT回归",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 45,
            "maindef": ["libs.datamodel.mlalgorithm.GBDTRegressor", "GBDTRegressor"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "树最大深度",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 0,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 0,
                            "high": 100,
                            "step": 2
                        }
                    }
                }, {
                    "name": "max_leaf_nodes",
                    "type": "int",
                    "value": 32,
                    "default": 32,
                    "label": "最大分支数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 2,
                            "high": 100,
                            "step": 2
                        }
                    }
                }, {
                    "name": "min_impurity_decrease",
                    "type": "int",
                    "value": 0,
                    "default": 0,
                    "label": "最小信息熵增益",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "min_samples_split",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "节点最小样本数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 20,
                            "step": 1
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 20,
                            "step": 1
                        }
                    }
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "subsample",
                    "type": "float",
                    "value": 1.0,
                    "default": 1.0,
                    "label": "训练基百分比",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "float",
                        "config": {
                            "low": 0.1,
                            "high": 1.0,
                            "step": 0.1
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 0.1,
                            "high": 1.0,
                            "step": 0.1
                        }
                    }
                }, {
                    "name": "n_estimators",
                    "type": "int",
                    "value": 100,
                    "default": 100,
                    "label": "最大迭代次数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 200,
                            "step": 10
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 200,
                            "step": 10
                        }
                    }
                }, {
                    "name": "learning_rate",
                    "type": "float",
                    "value": 0.1,
                    "default": 0.1,
                    "label": "学习率",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "回归算法",
                "algorithm_name": "GBDT回归",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "MLPBinaryClassifier",
            "name": "dnn二分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 50,
            "maindef": ["libs.datamodel.mlalgorithm.MLPBinaryClassifier", "MLPBinaryClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "hidden_layer_sizes",
                    "type": "int",
                    "value": (100,),
                    "default": (100,),
                    "label": "隐藏层",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "learning_rate_init",
                    "type": "float",
                    "value": "0.001",
                    "default": "0.001",
                    "label": "学习率",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "float",
                        "config": {
                            "low": 0.0001,
                            "high": 0.01,
                            "step": 0.0002
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 0.0001,
                            "high": 0.01,
                            "step": 0.0002
                        }
                    }
                }, {
                    "name": "max_iter",
                    "type": "int",
                    "value": 200,
                    "default": 200,
                    "label": "最大迭代轮数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 2000,
                            "step": 10
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 10,
                            "high": 2000,
                            "step": 10
                        }
                    }
                }, {
                    "name": "tol",
                    "type": "float",
                    "value": 1e-4,
                    "default": 1e-4,
                    "label": "目标收敛阈值",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "二分类算法",
                "algorithm_name": "dnn二分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "MLPMultiClassifier",
            "name": "dnn多分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 55,
            "maindef": ["libs.datamodel.mlalgorithm.MLPMultiClassifier", "MLPMultiClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "hidden_layer_sizes",
                    "type": "int",
                    "value": (100,),
                    "default": (100,),
                    "label": "隐藏层",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "learning_rate_init",
                    "type": "float",
                    "value": "0.001",
                    "default": "0.001",
                    "label": "学习率",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "float",
                        "config": {
                            "low": 0.0001,
                            "high": 0.01,
                            "step": 0.0002
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 0.0001,
                            "high": 0.01,
                            "step": 0.0002
                        }
                    }
                }, {
                    "name": "max_iter",
                    "type": "int",
                    "value": 200,
                    "default": 200,
                    "label": "最大迭代轮数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 2000,
                            "step": 10
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 10,
                            "high": 2000,
                            "step": 10
                        }
                    }
                }, {
                    "name": "tol",
                    "type": "float",
                    "value": 1e-4,
                    "default": 1e-4,
                    "label": "目标收敛阈值",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "多分类算法",
                "algorithm_name": "dnn多分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "MLPRegression",
            "name": "dnn回归",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 60,
            "maindef": ["libs.datamodel.mlalgorithm.MLPRegression", "MLPRegression"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "hidden_layer_sizes",
                    "type": "int",
                    "value": (100,),
                    "default": (100,),
                    "label": "隐藏层",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "learning_rate_init",
                    "type": "float",
                    "value": "0.001",
                    "default": "0.001",
                    "label": "学习率",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "float",
                        "config": {
                            "low": 0.0001,
                            "high": 0.01,
                            "step": 0.0002
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 0.0001,
                            "high": 0.01,
                            "step": 0.0002
                        }
                    }
                }, {
                    "name": "max_iter",
                    "type": "int",
                    "value": 200,
                    "default": 200,
                    "label": "最大迭代轮数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 2000,
                            "step": 10
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 10,
                            "high": 2000,
                            "step": 10
                        }
                    }
                }, {
                    "name": "tol",
                    "type": "float",
                    "value": 1e-4,
                    "default": 1e-4,
                    "label": "目标收敛阈值",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "回归算法",
                "algorithm_name": "dnn回归",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "LRBinaryClassifier",
            "name": "逻辑回归二分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 65,
            "maindef": ["libs.datamodel.mlalgorithm.LRBinaryClassifier", "LRBinaryClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "solver",
                    "value": "lbfgs",
                    "default": "lbfgs",
                    "label": "优化器",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["lbfgs", "saga"]
                    }
                }, {
                    "name": "max_iter",
                    "type": "int",
                    "value": 20,
                    "default": 20,
                    "label": "最大迭代轮数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 1000,
                            "step": 10
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 1000,
                            "step": 10
                        }
                    },
                }, {
                    "name": "tol",
                    "type": "float",
                    "value": 1e-4,
                    "default": 1e-4,
                    "label": "目标收敛阈值",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "二分类算法",
                "algorithm_name": "逻辑回归二分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "LRMultiClassifier",
            "name": "逻辑回归多分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 70,
            "maindef": ["libs.datamodel.mlalgorithm.LRMultiClassifier", "LRMultiClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "solver",
                    "value": "lbfgs",
                    "default": "lbfgs",
                    "label": "优化器",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ["lbfgs", "saga"]
                    }
                }, {
                    "name": "max_iter",
                    "type": "int",
                    "value": 20,
                    "default": 20,
                    "label": "最大迭代轮数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 1000,
                            "step": 10
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 1000,
                            "step": 10
                        }
                    },
                }, {
                    "name": "tol",
                    "type": "float",
                    "value": 1e-4,
                    "default": 1e-4,
                    "label": "目标收敛阈值",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "多分类算法",
                "algorithm_name": "逻辑回归多分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "LinearRegression",
            "name": "线性回归",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 75,
            "maindef": ["libs.datamodel.mlalgorithm.LinearRegression", "LinearRegression"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "回归算法",
                "algorithm_name": "线性回归",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "Ridge",
            "name": "岭回归",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 80,
            "maindef": ["libs.datamodel.mlalgorithm.Ridge", "Ridge"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "value": [],
                    "default": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "alpha",
                    "type": "float",
                    "value": "1.0",
                    "default": "1.0",
                    "label": "正则化强度",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "float",
                        "config": {
                            "low": 0.0,
                            "high": 2.0,
                            "step": 0.1
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 0.0,
                            "high": 2.0,
                            "step": 0.1
                        }
                    }

                }, {
                    "name": "max_iter",
                    "type": "int",
                    "value": 20,
                    "default": 20,
                    "label": "最大迭代轮数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 1000,
                            "step": 10
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 1000,
                            "step": 10
                        }
                    }
                }, {
                    "name": "tol",
                    "type": "float",
                    "value": 1e-4,
                    "default": 1e-4,
                    "label": "目标收敛阈值",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "random_state",
                    "type": "int",
                    "value": 5,
                    "default": 5,
                    "label": "随机种子",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "value": False,
                    "default": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "value": 4,
                    "default": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "回归算法",
                "algorithm_name": "岭回归",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "XGBoostClassifier",
            "name": "XGBoost分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 100,
            "maindef": ["libs.datamodel.mlalgorithm.XGBoostClassifier", "XGBoostClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "default": [],
                    "value": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "default": "",
                    "value": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "n_estimators",
                    "type": "int",
                    "default": 100,
                    "value": 100,
                    "label": "树的数量",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 100,
                            "high": 1000,
                            "step": 100
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 100,
                            "high": 1000,
                            "step": 100
                        }
                    }
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "default": 6,
                    "value": 6,
                    "label": "树的最大深度",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 100,
                            "step": 1
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 100,
                            "step": 1
                        }
                    }
                }, {
                    "name": "learning_rate",
                    "type": "float",
                    "default": 0.3,
                    "value": 0.3,
                    "label": "学习率",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "float",
                        "config": {
                            "low": 0,
                            "high": 1,
                            "step": 0.005
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 0,
                            "high": 1,
                            "step": 0.005
                        }
                    }
                }, {
                    "name": "min_child_weight",
                    "default": 1,
                    "value": 1,
                    "label": "最小叶子节点样本权重和",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": [1, 3, 5, 7]
                    }
                }, {
                    "name": "subsample",
                    "type": "int",
                    "default": 0.6,
                    "value": 0.6,
                    "label": "子样本",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": [0.6, 0.7, 0.8, 0.9, 1.0]
                    }
                }, {
                    "name": "gmma",
                    "type": "int",
                    "default": 0,
                    "value": 0,
                    "label": "节点分裂所需的最小函数",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "alpha",
                    "type": "float",
                    "default": 0,
                    "value": 0,
                    "label": "L1正则化系数",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "reg_lambda",
                    "type": "float",
                    "default": 1,
                    "value": 1,
                    "label": "L2正则化系数",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "default": False,
                    "value": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "default": 4,
                    "value": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "分类算法",
                "algorithm_name": "XGBoost分类",
            },
            "code_path": "",
            "deleted": "0"},
        {
            "_id": "XGBoostRegression",
            "name": "XGBoost回归",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 100,
            "maindef": ["libs.datamodel.mlalgorithm.XGBoostRegression", "XGBoostRegression"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
                {
                    "id": "model_importance",
                    "label": "查看特征重要度"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "default": [],
                    "value": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "default": "",
                    "value": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "n_estimators",
                    "type": "int",
                    "default": 100,
                    "value": 100,
                    "label": "树的数量",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 100,
                            "high": 1000,
                            "step": 100
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 100,
                            "high": 1000,
                            "step": 100
                        }
                    }
                }, {
                    "name": "max_depth",
                    "type": "int",
                    "default": 6,
                    "value": 6,
                    "label": "树的最大深度",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 100,
                            "step": 1
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": 1,
                            "high": 100,
                            "step": 1
                        }
                    }
                }, {
                    "name": "learning_rate",
                    "type": "float",
                    "default": 0.3,
                    "value": 0.3,
                    "label": "学习率",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "float",
                        "config": {
                            "low": 0,
                            "high": 1,
                            "step": 0.005
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 0,
                            "high": 1,
                            "step": 0.005
                        }
                    }
                }, {
                    "name": "min_child_weight",
                    "default": 1,
                    "value": 1,
                    "label": "最小叶子节点样本权重和",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": [1, 3, 5, 7]
                    }
                }, {
                    "name": "subsample",
                    "type": "int",
                    "default": 0.6,
                    "value": 0.6,
                    "label": "子样本",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": [0.6, 0.7, 0.8, 0.9, 1.0]
                    }
                }, {
                    "name": "gmma",
                    "type": "int",
                    "default": 0,
                    "value": 0,
                    "label": "节点分裂所需的最小函数",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "alpha",
                    "type": "float",
                    "default": 0,
                    "value": 0,
                    "label": "L1正则化系数",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "reg_lambda",
                    "type": "float",
                    "default": 1,
                    "value": 1,
                    "label": "L2正则化系数",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "default": False,
                    "value": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "default": 4,
                    "value": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "回归算法",
                "algorithm_name": "XGBoost回归",
            },
            "code_path": "",
            "deleted": "0"},
        {
            "_id": "SvmSvcClassifier",
            "name": "SVM分类",
            "category": "算法组件",
            "type": "Algorithm",
            "index": 15,
            "subindex": 90,
            "maindef": ["libs.datamodel.mlalgorithm.SvmSvcClassifier", "SvmSvcClassifier"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                },
                {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                },
            ],
            "style": {},
            "attrs": [
                {
                    "name": "feature",
                    "default": [],
                    "value": [],
                    "label": "特征列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label",
                    "default": "",
                    "value": "",
                    "label": "标签列",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "C",
                    "type": "float",
                    "default": 1.0,
                    "value": 1.0,
                    "label": "惩罚系数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "float",
                        "config": {
                            "low": 0.1,
                            "high": 3.0,
                            "step": 0.1
                        }
                    },
                    "resetAutoml": {
                        "type": "float",
                        "config": {
                            "low": 0.1,
                            "high": 3.0,
                            "step": 0.1
                        }
                    }
                }, {
                    "name": "max_iter",
                    "type": "int",
                    "default": -1,
                    "value": -1,
                    "label": "最大迭代轮数",
                    "isdepand": False,
                    "isupdate": False,
                    "automl": {
                        "type": "int",
                        "config": {
                            "low": -1,
                            "high": 1000,
                            "step": 10
                        }
                    },
                    "resetAutoml": {
                        "type": "int",
                        "config": {
                            "low": -1,
                            "high": 1000,
                            "step": 10
                        }
                    }
                }, {
                    "name": "gmma",
                    "default": "scale",
                    "value": "scale",
                    "label": "核函数系数",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ['scale', 'auto']}
                }, {
                    "name": "kernal",
                    "default": "rbf",
                    "value": "rbf",
                    "label": "核函数",
                    "isdepand": False,
                    "isupdate": False,
                    "selected": {
                        "type": "list",
                        "option": ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']}
                }, {
                    "name": "tol",
                    "type": "float",
                    "default": 1e-3,
                    "value": 1e-3,
                    "label": "目标收敛阈值",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl",
                    "type": "bool",
                    "default": False,
                    "value": False,
                    "label": "是否自动化训练",
                    "isdepand": False,
                    "isupdate": False,
                }, {
                    "name": "automl_trials",
                    "type": "int",
                    "default": 4,
                    "value": 4,
                    "label": "创建模型数量",
                    "isdepand": False,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "sklearn",
                "algorithm_type": "分类算法",
                "algorithm_name": "支持向量机分类",
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"Predict": [
        {
            "_id": "Predict",
            "name": "模型预测",
            "category": "预测组件",
            "type": "Predict",
            "index": 20,
            "subindex": 5,
            "maindef": ["libs.datamodel.predict.predict", "predict"],
            "input_port_num": 2,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                },
                {
                    "id": 1,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewData",
                    "label": "查看数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportDataset",
                    "label": "导出数据集"
                }
            ],
            "style": {},
            "attrs": [],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"Eval": [
        {
            "_id": "MlEvalTwoClassify",
            "name": "二分类评估",
            "category": "评估组件",
            "type": "Eval",
            "index": 23,
            "subindex": 5,
            "maindef": ["libs.datamodel.eval.ml_eval_2_classify", "ml_eval_2_classify"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出评估结果",
                    "port_type": "Eval",
                    "support_types": ["Eval"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewEvalData",
                    "label": "查看评估结果"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }
            ],
            "style": {},
            "attrs": [],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "MlEvalClassify",
            "name": "多分类评估",
            "category": "评估组件",
            "type": "Eval",
            "index": 23,
            "subindex": 10,
            "maindef": ["libs.datamodel.eval.ml_eval_classify", "ml_eval_classify"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出评估结果",
                    "port_type": "Eval",
                    "support_types": ["Eval"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewEvalData",
                    "label": "查看评估结果"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }
            ],
            "style": {},
            "attrs": [],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "MlEvalRegressor",
            "name": "回归评估",
            "category": "评估组件",
            "type": "Eval",
            "index": 23,
            "subindex": 15,
            "maindef": ["libs.datamodel.eval.ml_eval_regressor", "ml_eval_regressor"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出评估结果",
                    "port_type": "Eval",
                    "support_types": ["Eval"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewEvalData",
                    "label": "查看评估结果"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }
            ],
            "style": {},
            "attrs": [],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"DataModel": [
        {
            "_id": "DataModel",
            "name": "数据模型",
            "category": "数据模型组件",
            "type": "DataModel",
            "index": 25,
            "subindex": 5,
            "maindef": ["libs.datamodel.datamodel.data_model", "data_model"],
            "input_port_num": 0,
            "output_port_num": 1,
            "input_ports": [],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出数据模型",
                    "port_type": "Grepo",
                    "support_types": ["Grepo", "DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "datamodel_id",
                    "value": "",
                    "default": "",
                    "isdepand": False,
                    "isupdate": True,
                    "label": "数据模型",
                    "selected": {
                        "type": "interface",
                        "option": "datamodel"
                    }
                },
                {
                    "name": "datamodel_topo",
                    "value": {},
                    "default": {},
                    "isdepand": True,
                    "isupdate": True,
                    "label": "数据模型配置",
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"GraphDataSource": [
        {
            "_id": "GraphRepo",
            "name": "图数据集",
            "category": "图数据集组件",
            "type": "GraphDataSource",
            "index": 30,
            "subindex": 5,
            "maindef": ["libs.datamodel.graphsource.graphrepo", "graphrepo"],
            "input_port_num": 0,
            "output_port_num": 1,
            "input_ports": [],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewGraphData",
                    "label": "查看图数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportGraphrepo",
                    "label": "导出图数据集"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "grepo_id",
                    "value": "",
                    "default": "",
                    "isdepand": False,
                    "isupdate": True,
                    "label": "图数据集",
                    "selected": {
                        "type": "interface",
                        "option": "graphrepo"
                    }
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GraphRepoBuild",
            "name": "构图组件",
            "category": "图数据集组件",
            "type": "GraphDataSource",
            "index": 30,
            "subindex": 6,
            "maindef": ["libs.datamodel.graphsource.build_graph", "build_graph"],
            "input_port_num": 2,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集1",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                },
                {
                    "id": 1,
                    "default": [],
                    "label": "输入数据集2",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "increase",
                    "label": "增加输入port"
                },
                {
                    "id": "decrease",
                    "label": "减少输入port"
                },
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewGraphData",
                    "label": "查看图数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportGraphrepo",
                    "label": "导出图数据集"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "graph_schema",
                    "value": [],
                    "default": [],
                    "label": "构图配置",
                    "isdepand": True,
                    "isupdate": False,
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"GraphDataProcess": [
        {
            "_id": "GrepoSplit",
            "name": "图数据拆分",
            "category": "图数据处理组件",
            "type": "GraphDataProcess",
            "index": 35,
            "subindex": 5,
            "maindef": ["libs.datamodel.graphprocess.grepo_split", "grepo_split"],
            "input_port_num": 1,
            "output_port_num": 2,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图数据集1",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                },
                {
                    "id": 1,
                    "default": [],
                    "label": "输出图数据集2",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewGraphData",
                    "label": "查看图数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportGraphrepo",
                    "label": "导出图数据集"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "split_rate",
                    "type": "float",
                    "value": 0.8,
                    "default": 0.8,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "拆分比例",
                    "selected": {
                        "type": "list",
                        "option": [0.5, 0.6, 0.7, 0.8, 0.9]
                    }
                }, {
                    "name": "node_type",
                    "value": "",
                    "default": "",
                    "isdepand": True,
                    "isupdate": False,
                    "label": "指定拆分节点类型"
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GrepoFeat",
            "name": "图自动特征统计",
            "category": "图数据处理组件",
            "type": "GraphDataProcess",
            "index": 35,
            "subindex": 6,
            "maindef": ["libs.datamodel.graphprocess.grepo_feat", "grepo_feat"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewGraphData",
                    "label": "查看图数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportGraphrepo",
                    "label": "导出图数据集"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "nodes_list",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": True,
                    "label": "选择节点类型",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GrepoFilter",
            "name": "图节点过滤",
            "category": "图数据处理组件",
            "type": "GraphDataProcess",
            "index": 35,
            "subindex": 7,
            "maindef": ["libs.datamodel.graphprocess.grepo_filter", "grepo_filter"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewGraphData",
                    "label": "查看图数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportGraphrepo",
                    "label": "导出图数据集"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "nodes_list",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "选择过滤条件",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"GraphAlgorithm": [
        {
            "_id": "GrepoGCN",
            "name": "GCN二分类",
            "category": "图算法组件",
            "type": "GraphAlgorithm",
            "index": 40,
            "subindex": 5,
            "maindef": ["libs.datamodel.graphalgorithm.grepo_gcn_model", "grepo_gcn_model"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图模型",
                    "port_type": "Gmodel",
                    "support_types": ["Gmodel"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "epoch",
                    "type": "int",
                    "value": 100,
                    "default": 100,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "训练epoch"
                }, {
                    "name": "lr",
                    "type": "float",
                    "value": 0.001,
                    "default": 0.001,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "学习率"
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "isdepand": True,
                    "isupdate": False,
                    "label": "标签列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label_mask",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "有效标签范围",
                    "selected": {
                        "type": "range",
                    }
                }, {
                    "name": "features",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "特征列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "layers",
                    "type": "int",
                    "value": [50],
                    "default": [50],
                    "isdepand": False,
                    "isupdate": False,
                    "label": "隐藏层节点数"
                }, {
                    "name": "automl",
                    "value": False,
                    "default": False,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "是否自动化训练",
                    "dsiplay": False
                }, {
                    "name": "automl_trials",
                    "value": 4,
                    "default": 4,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "创建模型数量",
                    "dsiplay": False
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "pytorch",
                "algorithm_type": "图节点二分类",
                "algorithm_name": "GCN二分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GrepoSAGE",
            "name": "SAGE二分类",
            "category": "图算法组件",
            "type": "GraphAlgorithm",
            "index": 40,
            "subindex": 6,
            "maindef": ["libs.datamodel.graphalgorithm.grepo_sage_model", "grepo_sage_model"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图模型",
                    "port_type": "Gmodel",
                    "support_types": ["Gmodel"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "epoch",
                    "type": "int",
                    "value": 100,
                    "default": 100,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "训练epoch"
                }, {
                    "name": "lr",
                    "type": "float",
                    "value": 0.001,
                    "default": 0.001,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "学习率"
                }, {
                    "name": "label",
                    "value": "",
                    "default": "",
                    "isdepand": True,
                    "isupdate": False,
                    "label": "标签列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label_mask",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "有效标签范围",
                    "selected": {
                        "type": "range",
                    }
                }, {
                    "name": "features",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "特征列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "layers",
                    "type": "int",
                    "value": [50],
                    "default": [50],
                    "isdepand": False,
                    "isupdate": False,
                    "label": "隐藏层节点数"
                }, {
                    "name": "automl",
                    "value": False,
                    "default": False,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "是否自动化训练",
                    "dsiplay": False
                }, {
                    "name": "automl_trials",
                    "value": 4,
                    "default": 4,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "创建模型数量",
                    "dsiplay": False
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "pytorch",
                "algorithm_type": "图节点二分类",
                "algorithm_name": "SAGE二分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GrepoRGCN",
            "name": "RGCN二分类",
            "category": "图算法组件",
            "type": "GraphAlgorithm",
            "index": 40,
            "subindex": 7,
            "maindef": ["libs.datamodel.graphalgorithm.grepo_rgcn_model", "grepo_rgcn_model"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图模型",
                    "port_type": "Gmodel",
                    "support_types": ["Gmodel"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "epoch",
                    "type": "int",
                    "value": 100,
                    "default": 100,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "训练epoch"
                }, {
                    "name": "lr",
                    "type": "float",
                    "value": 0.001,
                    "default": 0.001,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "学习率"
                }, {
                    "name": "label",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "标签列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label_mask",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "有效标签范围",
                    "selected": {
                        "type": "range",
                    }
                }, {
                    "name": "features",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "特征列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "layers",
                    "type": "int",
                    "value": [50],
                    "default": [50],
                    "isdepand": False,
                    "isupdate": False,
                    "label": "隐藏层节点数"
                }, {
                    "name": "edge_list",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "指定边类型"
                }, {
                    "name": "automl",
                    "value": False,
                    "default": False,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "是否自动化训练",
                    "dsiplay": False
                }, {
                    "name": "automl_trials",
                    "value": 4,
                    "default": 4,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "创建模型数量",
                    "dsiplay": False
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "pytorch",
                "algorithm_type": "图节点二分类",
                "algorithm_name": "RGCN二分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GrepoRSAGE",
            "name": "RSAGE二分类",
            "category": "图算法组件",
            "type": "GraphAlgorithm",
            "index": 40,
            "subindex": 8,
            "maindef": ["libs.datamodel.graphalgorithm.grepo_rsage_model", "grepo_rsage_model"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图模型",
                    "port_type": "Gmodel",
                    "support_types": ["Gmodel"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "epoch",
                    "type": "int",
                    "value": 100,
                    "default": 100,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "训练epoch"
                }, {
                    "name": "lr",
                    "type": "float",
                    "value": 0.001,
                    "default": 0.001,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "学习率"
                }, {
                    "name": "label",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "标签列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "label_mask",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "有效标签范围",
                    "selected": {
                        "type": "range",
                    }
                }, {
                    "name": "features",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "特征列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "layers",
                    "type": "int",
                    "value": [50],
                    "default": [50],
                    "isdepand": False,
                    "isupdate": False,
                    "label": "隐藏层节点数"
                }, {
                    "name": "edge_list",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "指定边类型"
                }, {
                    "name": "automl",
                    "value": False,
                    "default": False,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "是否自动化训练",
                    "dsiplay": False
                }, {
                    "name": "automl_trials",
                    "value": 4,
                    "default": 4,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "创建模型数量",
                    "dsiplay": False
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "pytorch",
                "algorithm_type": "图节点二分类",
                "algorithm_name": "RSAGE二分类",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GrepoRecommend",
            "name": "图推荐算法",
            "category": "图算法组件",
            "type": "GraphAlgorithm",
            "index": 40,
            "subindex": 9,
            "maindef": ["libs.datamodel.graphalgorithm.grepo_recommend_model", "grepo_recommend_model"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图模型",
                    "port_type": "Gmodel",
                    "support_types": ["Gmodel"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "tensorboard",
                    "label": "查看训练过程"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "epoch",
                    "type": "int",
                    "value": 100,
                    "default": 100,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "训练epoch"
                }, {
                    "name": "lr",
                    "type": "float",
                    "value": 0.001,
                    "default": 0.001,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "学习率"
                }, {
                    "name": "metapath",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "正样本路径",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "neg_metapath",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "负样本路径",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "features",
                    "value": [],
                    "default": [],
                    "isdepand": True,
                    "isupdate": False,
                    "label": "特征列",
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "output_dim",
                    "type": "int",
                    "value": 16,
                    "default": 16,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "输出向量维度"
                }, {
                    "name": "layers",
                    "type": "int",
                    "value": [50],
                    "default": [50],
                    "isdepand": False,
                    "isupdate": False,
                    "label": "隐藏层节点数"
                }, {
                    "name": "automl",
                    "value": False,
                    "default": False,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "是否自动化训练",
                    "dsiplay": False
                }, {
                    "name": "automl_trials",
                    "value": 4,
                    "default": 4,
                    "isdepand": False,
                    "isupdate": False,
                    "label": "创建模型数量",
                    "dsiplay": False
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "pytorch",
                "algorithm_type": "图向量算法",
                "algorithm_name": "向量化召回",
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "CausalInference",
            "name": "因果推理",
            "category": "图算法组件",
            "type": "GraphAlgorithm",
            "index": 40,
            "subindex": 10,
            "maindef": ["libs.datamodel.graphalgorithm.CausalInference", "CausalInference"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入数据集",
                    "port_type": "DataSet",
                    "support_types": ["DataSet"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出模型",
                    "port_type": "Model",
                    "support_types": ["Model"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                }
            ],
            "style": {},
            "attrs": [
                {
                    "name": "graph",
                    "value": {},
                    "default": {},
                    "label": "因果图",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "causalmodel"
                    }
                }, {
                    "name": "do",
                    "value": [],
                    "default": [],
                    "label": "干预节点",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "evidence",
                    "value": [],
                    "default": [],
                    "label": "证据节点",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }, {
                    "name": "variables",
                    "value": [],
                    "default": [],
                    "label": "查询节点",
                    "isdepand": True,
                    "isupdate": True,
                    "selected": {
                        "type": "interface",
                        "option": "schema"
                    }
                }
            ],
            "config": {
                "use_spark": True,
                "model_dep": False,
                "frame_type": "pgmpy",
                "algorithm_type": "因果算法",
                "algorithm_name": "因果算法",
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"GraphPredict": [
        {
            "_id": "GrepoModelPredict",
            "name": "图模型预测",
            "category": "预测组件",
            "type": "GraphPredict",
            "index": 45,
            "subindex": 5,
            "maindef": ["libs.datamodel.graphpredict.grepo_model_predict", "grepo_model_predict"],
            "input_port_num": 2,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图模型",
                    "port_type": "Gmodel",
                    "support_types": ["Gmodel"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                },
                {
                    "id": 1,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewGraphData",
                    "label": "查看图数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportGraphrepo",
                    "label": "导出图数据集"
                }
            ],
            "style": {},
            "attrs": [],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "GrepoRecommendPredict",
            "name": "图推荐预测",
            "category": "预测组件",
            "type": "GraphPredict",
            "index": 45,
            "subindex": 6,
            "maindef": ["libs.datamodel.graphpredict.grepo_recommend_predict", "grepo_recommend_predict"],
            "input_port_num": 2,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图模型",
                    "port_type": "Gmodel",
                    "support_types": ["Gmodel"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                },
                {
                    "id": 1,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewGraphData",
                    "label": "查看图数据信息"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }, {
                    "id": "exportGraphrepo",
                    "label": "导出图数据集"
                }
            ],
            "style": {},
            "attrs": [],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
    {"GraphEval": [
        {
            "_id": "GrepoEvalTwoClassify",
            "name": "图二分类评估",
            "category": "评估组件",
            "type": "GraphEval",
            "index": 50,
            "subindex": 5,
            "maindef": ["libs.datamodel.grapheval.grepo_eval_2_classify", "grepo_eval_2_classify"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出评估结果",
                    "port_type": "Eval",
                    "support_types": ["Eval"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewEvalData",
                    "label": "查看评估结果"
                }, {
                    "id": "viewLog",
                    "label": "查看日志"
                }
            ],
            "style": {},
            "attrs": [],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
        {
            "_id": "LabelTaskClassify",
            "name": "属性传导评估",
            "category": "评估组件",
            "type": "GraphEval",
            "index": 50,
            "subindex": 10,
            "maindef": ["libs.datamodel.grapheval.label_task_classify", "label_task_classify"],
            "input_port_num": 1,
            "output_port_num": 1,
            "input_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输入图数据集",
                    "port_type": "Grepo",
                    "support_types": ["Grepo"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "output_ports": [
                {
                    "id": 0,
                    "default": [],
                    "label": "输出评估结果",
                    "port_type": "LabelTaskEval",
                    "support_types": ["LabelTaskEval"],
                    "schema": {},
                    "config": {},
                    "reader": "",
                    "writer": "",
                    "isrequired": True
                }
            ],
            "actions": [
                {
                    "id": "rename",
                    "label": "重命名"
                },
                {
                    "id": "delete",
                    "label": "删除"
                },
                {
                    "id": "fromnode",
                    "label": "从本节点开始运行"
                },
                {
                    "id": "tonode",
                    "label": "运行到本节点"
                },
                {
                    "id": "viewLog",
                    "label": "查看日志"
                }
            ],
            "style": {},
            "attrs": [],
            "config": {
                "use_spark": True,
                "model_dep": False,
            },
            "code_path": "",
            "deleted": "0"
        },
    ]},
]

if __name__ == '__main__':
    for i in range(len(modules)):
        item_list = list(modules[i].values())[0]
        for j in range(len(item_list)):
            item = item_list[j]
            item["index"] = i
            item["subindex"] = j
            server_mgo.cvs_modules.find_one_and_update({"_id": item["_id"]}, {"$set": item}, upsert=True)