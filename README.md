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
        <pre><code>git clone https://github.com/yourusername/Fashiongan.git
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
  <li><strong>Curated Images Without Truncation</strong><br>
    <code>python generate.py --outdir=out --trunc=1 --seeds=85,265,297,849 --network=selected_models/styleGAN2ada_Africanwax.pkl</code>
  </li>
  <li><strong>Uncurated Images With Truncation</strong><br>
    <code>python generate.py --outdir=out --trunc=0.7 --seeds=600-605 --network=selected_models/styleGAN2ada_Africanwax.pkl</code>
  </li>
  <li><strong>Rendering Images from Projected W</strong><br>
    <code>python generate.py --outdir=out --projected_w=projected_w.npz --network=selected_models/styleGAN2ada_Africanwax.pkl</code>
  </li>
</ol>

<h4>Generating Images with StyleGAN3 Models</h4>
<ol>
  <li><strong>Image Generation with Truncation</strong><br>
    <code>python gen_images.py --outdir=out --trunc=1 --seeds=2 --network=selected_models/styleGAN3_Africanwax.pkl</code>
  </li>
  <li><strong>Generating Uncurated Images with Truncation</strong><br>
    <code>python gen_images.py --outdir=out --trunc=0.7 --seeds=600-605 --network=selected_models/styleGAN3_Africanwax.pkl</code>
  </li>
</ol>

