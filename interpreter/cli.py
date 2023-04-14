import json
from fgl import FGL
import click
from .utils import submit_fgl
import click
            
@click.group()
def fgl():
    ...
   
@fgl.command()
@click.option("-c", '--command', default=None, help='命令行')
@click.option("-d", '--debug', default=False, is_flag=True, help='调试模式')
@click.option("-r", '--submit', default=False, is_flag=True, help='远端提交模式')
@click.option("-e", '--endpoint', default="localhost:3000", help='服务地址')
def exec(command, debug, submit, endpoint):
    '''
    范式化建模语言
    '''
    command = command or '''
            CALL PARADIGM attribute_transductive('Cora', 300);
            '''
    if not submit:
        print(">> MODE(local)")
        print(">> COMAMND: %s \n" % command)
        r = FGL().parse_dag(command)
        dag = json.loads(r)
        from engine.engine import fgljobs
        fgljobs([dag])[0].execute_in_process(run_config={'loggers':{'console':{'config':{'log_level':'DEBUG' if debug else 'ERROR'}}}})
    else:
        print(">> MODE(remote)")
        submit_fgl(command, endpoint)
        
    
@fgl.command()
@click.option('--epoch', default=100, help="训练轮数")
@click.option("-d", '--debug', default=False, is_flag=True, help='调试模式')
@click.option("-r", '--submit', default=False, is_flag=True, help='远端提交模式')
@click.option("-e", '--endpoint', default="localhost:3000", help='服务地址')
def attribute_transduction(epoch, debug, submit, endpoint):
    '''
    属性传导方式
    '''
    exec.callback(f'''
         CALL PARADIGM attribute_transductive('Cora', {epoch})
         ''',
         debug, submit, endpoint)
    


if __name__ == '__main__':
    fgl()
    
    


