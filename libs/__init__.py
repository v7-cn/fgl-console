
import os
from dagster import OpDefinition
def scan_modules(path):
    '''扫描组件，返回组件列表
    '''
    def fetch_modules(module):
        return [module.__dict__[attr] for attr in module.__dict__ if isinstance(module.__dict__[attr], OpDefinition)]

    modules = []
    for root, dirs, files in os.walk(path):
        for file in files:
            fname, extension = os.path.splitext(file)
            fname = root  + "/" + fname
            if extension == '.module' and os.path.exists(fname + ".py"):
                from pydoc import importfile
                m = importfile(fname + ".py")
                modules += fetch_modules(m)
    return modules


ops = scan_modules(os.path.dirname(__file__))
