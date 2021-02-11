#! /bin/bash 
source ~/.bashrc

# (depending on your cluster): check, install and activate 
#   anaconda envioronment on each node
if ! ( conda env list &> /dev/null )
then
    wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
    mkdir -p /scratch/freda
    bash ./Anaconda3-2019.03-Linux-x86_64.sh -b -p /scratch/freda/anaconda3
    rm Anaconda3-2019.03-Linux-x86_64.sh
fi
source ~/.bashrc
# conda remove --name factorial --all
if ! ( conda activate factorial &> /dev/null )
then
    conda create -n factorial python=3.6 -y
    conda activate factorial
    conda install regex -y
    pip install submitit
    pip install flexible-dotdict
    echo $SLURMD_NODENAME, success >> ./host_info.txt
    echo $SLURMD_NODENAME
fi

source ~/.bashrc 
conda activate factorial

# run the script!
python factorial_json.py $SLURM_ARRAY_TASK_ID