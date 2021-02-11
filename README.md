# Slurm Quick Tour

## First Steps
- What’s slurm? 
- Login to the head node. 

## Basic Commands

### sinfo
  - Take a look at your available partitions.
  - What's partition? 
  
### srun
  - start an interactive job for debugging purpose
  ```
  srun -p $PARTITION_NAME -c 1 --pty bash 
  ```
  
### sbatch 
  - Example: Factorial Computation
  ```
  cd examples/
  python factorial.py $OPTIONAL_NUMBER (default: 5)
  ```

  - submit a job
  ```
  cd examples/
  sbatch -p $PARTITION_NAME -c 1 factorial.sh 
  sbatch -p $PARTITION_NAME -c 1 factorial.sh 10
  ```
  `-c: --cpus-per-task`


  - submit an array job
  ```
  cd examples/
  sbatch -p $PARTITION_NAME -c 1 -a 3-5 factorial_array.sh 
  ```

  - submit a series of jobs (dealing with time limit)
  ```
  cd examples/
  sbatch -p $PARTITION_NAME -c 1 -J factcomp -d singleton factorial_array.sh 
  ```

  - summary of common options

  `-p`: partition <br>
  `-c`: requested CPU number <br>
  `--gpus-per-node` (not on TTIC slurm): requested GPU number<br>
  `-J`: usually with `-d singleton`, series name <br>
  `-a`: array IDs <br>
  <br>
  Some nodes are down somehow: exclude them! <br>
  `-x`: exclusive nodes  <br>
  <br>
  Output files are too messy: specify the file names! <br>
  `-o`: slurm stdout <br>
  `-e`: slurm stderr <br>
  
### squeue
  ```
  # check all
  squeue
  # check yours
  squeue -u $USER_NAME
  # Freda's favorite:
  squeue -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R %n %x" -u $$USER_NAME
  ```

### scancel 
  If you submitted a wrong job with id `$JOB_ID`, you probably wish to run
  ```
  scancel $JOB_ID
  ```

All (and more) details can be found at  https://slurm.schedmd.com/quickstart.html or the doc of your slurm cluster. 

## Advanced
### Submitit
  Call your own function as an array job
  ```
  cd examples/
  python factorial_submitit.py
  ```

### Freda's protocol with json-style dictionary
  ```
  cd examples/
  python factorial_json.py
  sbatch -p $PARTITION_NAME -c 1 -a 0-5 -J fact -d singleton factorial_json.sh
  ```

### You may design your own protocol as well! 
