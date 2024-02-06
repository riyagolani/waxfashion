#!/bin/bash -x
#SBATCH --job-name=stylegan3
#SBATCH --nodes=1
#SBATCH --output=%j_out.out
#SBATCH --error=%j_err.out
#SBATCH --time=158:00:00
#SBATCH --gres=gpu:2

### change 5-digit MASTER_PORT as you wish, slurm will raise Error if duplicated with others
### change WORLD_SIZE as gpus/node * num_nodes
# export MASTER_PORT=12340
# export WORLD_SIZE=4

# ### get the first node name as master address
# echo "NODELIST="${SLURM_NODELIST}
# master_addr=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
# export MASTER_ADDR=$master_addr
# echo "MASTER_ADDR="$MASTER_ADDR


# Activate Conda environment
source /home/PACE/sm98741n/miniconda3/etc/profile.d/conda.sh
conda activate venv

srun python /home/PACE/sm98741n/FashionGAN-capstone/stylegan2-ada-pytorch/train.py --outdir=../exp1_training_runs --cfg=auto --data=/home/PACE/sm98741n/datasets/1KD512.zip --gpus=2 --batch=32 --kimg=5000 --snap=25