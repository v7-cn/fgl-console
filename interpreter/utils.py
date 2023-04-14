import random
from fgl import FGL
import time
import json
from dagster_graphql import DagsterGraphQLClient, ReloadRepositoryLocationInfo, ReloadRepositoryLocationStatus
import warnings
warnings.filterwarnings("ignore")


def submit_dag(dag, endpoint="localhost:3000"):
    host, port = endpoint.split(":")
    client = DagsterGraphQLClient(host, port_number=int(port))
    stime = time.time()
    jobname = "job_" + str(int(stime*1000))
    print(f"提交JOB {jobname}")
    open(f"engine/jobs/{jobname}.json", "w").write(json.dumps(dag, ensure_ascii=False, indent=4))
    print(f"加载JOB {jobname}")
    client.reload_repository_location("engine.engine")
    print(f"执行JOB {jobname}")
    runid = client.submit_job_execution(
        jobname,
        run_config={},
    )
    
    while True:
        e = client.get_run_status(runid)
        if e.value == 'SUCCESS':
            break
        if time.time() - stime > 10000:
            break
    print(f"执行JOB成功 {jobname}")
    

def submit_fgl(script, endpoint="localhost:3000"):
    r = FGL().parse_dag(script)
    dag = json.loads(r)
    submit_dag(dag, endpoint)

