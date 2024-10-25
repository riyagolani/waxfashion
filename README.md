# AfricanWaxFashionGan

## Datasets

## Setting Up the Environment

### Prerequisites

* Ensure you have <a href="https://www.anaconda.com/products/distribution">Anaconda</a> or <a href="https://docs.conda.io/en/latest/miniconda.html">Miniconda</a> installed on your system.</li>
* To install Miniconda on a Linux-x86_64 server 

<pre><code>wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh</code></pre>

### Clone this repository 

<pre><code>git clone https://github.com/researchpace/waxfashiongan.git
cd Fashiongan</code></pre>

### Create the conda environment to run this code

* Use the provided <code>environment.yml</code> file to create a new conda environment. The environement is called Fashionfan-env

<pre><code>conda env create -f environment.yml</code></pre>
      
* Activate the environment
  
<pre><code>conda activate Fashiongan-env</code></pre>
  
* Verify the environment
 
<pre><code>conda list</code></pre>

### Additional information to manage the environment

* Deactivate the environment
  
<pre><code>conda deactivate</code></pre>

* Update the environment
  
<pre><code>conda env update -f environment.yml</code></pre>

* Remove the environment
  
<pre><code>conda env remove -n Fashiongan-env</code></pre>
    
## Use the selected StyleGAN models

The models are in the <code>selected_models</code> directories. 

Run the following scrips in Slurm jobs. Sample Slurm files are provided.

<pre><code>sbatch slurmfile.slurm</code></pre>

The output of each job is put into a file called <code>slurm-<jobid>.out</code>, so you can look at the output of a job run if there are errors or any important data.  

The generated images are in the <code>out</code> directory. 

### Generating patterns with StyleGAN2-ADA models

<pre><code>cd stylegan2-ada-pytorch</code></pre>

* Curated Images Without Truncation

<code>python generate.py --outdir=out --trunc=1 --seeds=85,265,297,849 --network=../selected_models/styleGAN2ada_Africanwax.pkl</code>

* Uncurated Images With Truncation

<code>python generate.py --outdir=out --trunc=0.7 --seeds=600-605 --network=../selected_models/styleGAN2ada_Africanwax.pkl</code>

* Rendering Images from Projected W

<code>python generate.py --outdir=out --projected_w=projected_w.npz --network=../selected_models/styleGAN2ada_Africanwax.pkl</code>

### Generating patterns with StyleGAN3 models

<pre><code>cd stylegan3</code></pre>

* Image Generation with Truncation

<code>python gen_images.py --outdir=out --trunc=1 --seeds=2 --network=../selected_models/styleGAN3_Africanwax.pkl</code>

* Generating Uncurated Images with Truncation

python gen_images.py --outdir=out --trunc=0.7 --seeds=600-605 --network=../selected_models/styleGAN3_Africanwax.pkl</code>

## Use the selected StyleGAN models from Hugging Face

## Use the Stable Diffusion models from Hugging Face

<p>This section provides instructions on how to use the Stable Diffusion model refined on SDXL, which is hosted on a Hugging Face repository.</p>

<h4>Installation Requirements</h4>
<p>Ensure you have the necessary libraries installed:</p>
<ul>
  <li><code>pip install diffusers --upgrade</code></li>
  <li><code>pip install invisible_watermark transformers accelerate safetensors</code></li>
</ul>

<h4>Using the Base Model</h4>
<p>To use the base model, follow these steps:</p>
<ol>
  <li>Import the necessary libraries:
    <pre><code>from diffusers import DiffusionPipeline
import torch</code></pre>
  </li>
  <li>Load the model:
    <pre><code>pipe = DiffusionPipeline.from_pretrained("MSamyak/SDXL_AfricanWax", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")</code></pre>
  </li>
  <li>Optional: Enable memory-efficient attention for torch < 2.0:
    <pre><code># pipe.enable_xformers_memory_efficient_attention()</code></pre>
  </li>
  <li>Generate an image:
    <pre><code>prompt = "Afwapa, Beautiful African Wax Pattern with orange and black design"
images = pipe(prompt=prompt).images[0]</code></pre>
  </li>
</ol>
