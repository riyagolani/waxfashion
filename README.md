# fashiongan

## Usage

<h3>Setting Up the Environment</h3>

<ul>
  <li><strong>Prerequisites</strong>
    <ul>
      <li>Ensure you have <a href="https://www.anaconda.com/products/distribution">Anaconda</a> or <a href="https://docs.conda.io/en/latest/miniconda.html">Miniconda</a> installed on your system.</li>
    </ul>
  </li>

  <li><strong>Steps to Create the Environment</strong>
    <ol>
      <li><strong>Clone the Repository</strong><br>
        Clone your GitHub repository to your local machine using Git.<br>
        <pre><code>git clone https://github.com/researchpace/waxfashiongan.git
cd Fashiongan</code></pre>
      </li>
      <li><strong>Create the Conda Environment</strong><br>
        Use the provided <code>.yml</code> file to create a new Conda environment.<br>
        <pre><code>conda env create -f environment.yml</code></pre>
      </li>
      <li><strong>Activate the Environment</strong><br>
        Once the environment is created, activate it.<br>
        <pre><code>conda activate Fashiongan-env</code></pre>
      </li>
      <li><strong>Verify the Environment</strong><br>
        Ensure that the environment is set up correctly.<br>
        <pre><code>conda list</code></pre>
      </li>
      <li><strong>Running the Project</strong><br>
        Run the scripts or use the models as per the instructions in the <strong>Usage</strong> section.<br>
      </li>
    </ol>
  </li>

  <li><strong>Additional Information</strong>
    <ul>
      <li><strong>Deactivating the Environment</strong><br>
        <pre><code>conda deactivate</code></pre>
      </li>
      <li><strong>Updating the Environment</strong><br>
        <pre><code>conda env update -f environment.yml</code></pre>
      </li>
      <li><strong>Removing the Environment</strong><br>
        <pre><code>conda env remove -n Fashiongan-env</code></pre>
      </li>
    </ul>
  </li>
</ul>

<h3>Usage Examples with Selected Models</h3>
<p>This section provides examples of how to generate images using models from the "selected_models" folder, using the syntax similar to StyleGAN2-ADA and StyleGAN3 models.</p>

<h4>Generating Images with StyleGAN2-ADA Models</h4>
<ol>
  <pre><code>cd stylegan2-ada-pytorch</code></pre>
  <li><strong>Curated Images Without Truncation</strong><br>
    <code>python generate.py --outdir=out --trunc=1 --seeds=85,265,297,849 --network=.../selected_models/styleGAN2ada_Africanwax.pkl</code>
  </li>
  <li><strong>Uncurated Images With Truncation</strong><br>
    <code>python generate.py --outdir=out --trunc=0.7 --seeds=600-605 --network=../selected_models/styleGAN2ada_Africanwax.pkl</code>
  </li>
  <li><strong>Rendering Images from Projected W</strong><br>
    <code>python generate.py --outdir=out --projected_w=projected_w.npz --network=../selected_models/styleGAN2ada_Africanwax.pkl</code>
  </li>
</ol>

<h4>Generating Images with StyleGAN3 Models</h4>
<ol>
  <pre><code>cd stylegan3</code></pre>
  <li><strong>Image Generation with Truncation</strong><br>
    <code>python gen_images.py --outdir=out --trunc=1 --seeds=2 --network=../selected_models/styleGAN3_Africanwax.pkl</code>
  </li>
  <li><strong>Generating Uncurated Images with Truncation</strong><br>
    <code>python gen_images.py --outdir=out --trunc=0.7 --seeds=600-605 --network=../selected_models/styleGAN3_Africanwax.pkl</code>
  </li>
</ol>
<h3>Using the Stable Diffusion Model from Hugging Face</h3>
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
