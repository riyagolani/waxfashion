#!/bin/bash -x
#SBATCH --job-name=stablediff
#SBATCH --nodes=1
#SBATCH --output=%j_out.out
#SBATCH --error=%j_err.out
#SBATCH --time=7:00:00
#SBATCH --gres=gpu:2

# ### Uncomment below if you need to get the first node name as master address
# echo "NODELIST="${SLURM_NODELIST}
# master_addr=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
# export MASTER_ADDR=$master_addr
# echo "MASTER_ADDR="$MASTER_ADDR

# Activate Conda environment
# Replace '/path/to/miniconda3' with your actual path to Miniconda3
source /path/to/miniconda3/etc/profile.d/conda.sh
conda activate <your_environment_name>

# Replace '/path/to/your/project' with the actual path to your project directory
cd /path/to/your/project
source /path/to/your/project/<your_environment_name>/bin/activate

# Training command
# Modify the paths and parameters below according to your project setup
accelerate launch --num_cpu_threads_per_process=2 "./sdxl_train.py" \
--enable_bucket \
--min_bucket_reso=256 \
--max_bucket_reso=2048 \
--pretrained_model_name_or_path="stabilityai/stable-diffusion-xl-base-1.0" \
--train_data_dir="/path/to/your/training_data/captioned/img" \
--resolution="1024,1024" \
--output_dir="/path/to/your/output_dir/captioned/model" \
--logging_dir="/path/to/your/logging_dir/captioned/log" \
--save_model_as=safetensors \
--output_name="last" \
--lr_scheduler_num_cycles="1" \
--max_data_loader_n_workers="0" \
--learning_rate_te1="1e-05" \
--learning_rate_te2="1e-05" \
--learning_rate="1e-05" \
--lr_scheduler="cosine" \
--lr_warmup_steps="2015" \
--train_batch_size="2" \
--max_train_steps="20150" \
--save_every_n_epochs="1" \
--mixed_precision="fp16" \
--save_precision="fp16" \
--caption_extension=".txt" \
--cache_latents \
--cache_latents_to_disk \
--optimizer_type="AdamW8bit" \
--max_data_loader_n_workers="0" \
--bucket_reso_steps=64 \
--save_every_n_steps="2000" \
--gradient_checkpointing \
--xformers \
--bucket_no_upscale \
--noise_offset=0.0 \
--no_half_vae \
--sample_sampler=euler_a \
--sample_prompts="/path/to/your/sample_prompts.txt" \
--sample_every_n_steps="1000"

# Add any additional notes or comments here
