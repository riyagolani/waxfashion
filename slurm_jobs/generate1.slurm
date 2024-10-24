#!/bin/sh

#SBATCH --ntasks=1
#SBATCH --gres=gpu:1

export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64/

echo $CUDA_VISIBLE_DEVICES

# If you didn't add the shell hook when installing miniconda:
eval "$($HOME/miniconda3/bin/conda shell.bash hook)"
conda activate Fashiongan-env

#cd stylegan2-ada-pytorch

python generate.py --outdir=out --trunc=1 --seeds=85,265,297,849 --network=../selected_models
/styleGAN2ada_Africanwax.pkl
