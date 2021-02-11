import os
import sys
import submitit
from tqdm import tqdm
from factorial import F


def slurm_job_babysit(executor, job_func, jobs, config_list):
    resubmit_ids = list()
    new_configs = list()
    problematic_jobs = list()
    cnt_complete = 0
    bar = tqdm(jobs)
    for idx, job in enumerate(bar):
        state = job.state
        if state != 'RUNNING' and state != 'COMPLETED' and \
                state != 'PENDING' and state != 'UNKNOWN':
            new_configs.append(config_list[idx])
            resubmit_ids.append(idx)
            problematic_jobs.append(job)
        elif state == 'COMPLETED':
            cnt_complete += 1
        bar.set_description(
            f'{cnt_complete} jobs finished, '
            f'{len(resubmit_ids)} jobs resubmitting'
        )
    print(f'{cnt_complete} jobs finished!')
    print(resubmit_ids)
    print([jobs[x] for x in resubmit_ids])
    if len(resubmit_ids) > 0:
        new_jobs = executor.map_array(job_func, new_configs)
        for idx, job in enumerate(new_jobs):
            jobs[resubmit_ids[idx]] = job
    return cnt_complete, problematic_jobs


log_folder = './logs/'
os.system(f'mkdir -p {log_folder}')
executor = submitit.AutoExecutor(folder=log_folder)
executor.update_parameters(
    timeout_min=60, slurm_partition=sys.argv[1],
    cpus_per_task=1, nodes=1,
    slurm_array_parallelism=2048,
    slurm_additional_parameters={
        'nodelist': 'cpu19'
    } 
)
config_list = [3, 4, 5]
jobs = executor.map_array(F, config_list)
from IPython import embed; embed(using=False)