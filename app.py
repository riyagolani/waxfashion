import streamlit as st
import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import time
import random
import threading

# --- Hugging Face API Setup ---
HF_API_KEY = st.secrets["HUGGING_FACE_API_KEY"]
headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Accept": "image/png",
    "Content-Type": "application/json"
}
MODEL_API_URL = "https://jvjrtjxevy6pdyw9.us-east4.gcp.endpoints.huggingface.cloud"

def generate_image(prompt):
    data = {"inputs": prompt, "parameters": {}}
    try:
        response = requests.post(
            MODEL_API_URL,
            headers=headers,
            json=data,
            timeout=900
        )
        response.raise_for_status()
        # Debug print: log response content type + size
        st.write("Response headers:", response.headers)
        st.write("Response content size (bytes):", len(response.content))
        st.write("Response content preview:", response.content[:500])

        img_bytes = response.content
        if len(img_bytes) < 1000:
            raise ValueError("The response was too small, likely not a valid image.")

        Image.open(BytesIO(img_bytes)).verify()
        return img_bytes

    except requests.Timeout:
        raise RuntimeError(f"The request timed out after {900 // 60} minutes.")
    except requests.RequestException as e:
        raise RuntimeError(f"An error occurred while contacting the API: {e}")
    except (UnidentifiedImageError, Exception) as e:
        raise RuntimeError(f"Failed to process image: {e}")

st.set_page_config(page_title="Wax Pattern Study", layout="centered")

# --- Add Border Using CSS ---
st.markdown("""
    <style>
    .stApp {
        border-left: 30px solid transparent;
        border-right: 30px solid transparent;
        border-bottom: 30px solid transparent;
        box-sizing: border-box;
        border-image: url("https://i.imgur.com/eWbCs47.png") 60 round;
    }
    [data-testid="stAppViewContainer"] {
        padding: 30px;
    }
    .stImage > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

# --- Init Session ---
if "phase" not in st.session_state:
    st.session_state.phase = "setup"
    st.session_state.images = []
    st.session_state.index = 0
    st.session_state.prompt = ""

# --- Dropdown options ---
colors = ["Red", "Blue", "Yellow", "Green", "Multicolor"]
shapes = ["Circles", "Squares", "Triangles", "Spirals", "Waves"]
themes = ["Traditional", "Modern", "Abstract"]

# --- Example Pattern URLs ---
example_images = [
    {
        "url": "https://i.imgur.com/m7a9sZk.png",
        "caption": "Blue & White Wavy Pattern"
    },
    {
        "url": "https://i.imgur.com/3GJarE9.png",
        "caption": "Olive & White Tribal Ovals"
    },
    {
        "url": "https://i.imgur.com/xa6QOnC.png",
        "caption": "Red & Gold Swirling Lines"
    }
]

# --- Setup Phase ---
if st.session_state.phase == "setup":
    st.title("Create Your Own African Wax Pattern")

    col1, col2, col3 = st.columns(3)
    with col1:
        selected_color = st.selectbox("Color", colors)
    with col2:
        selected_shape = st.selectbox("Shape", shapes)
    with col3:
        selected_theme = st.selectbox("Theme", themes)

    prompt = f"Generate a {selected_theme} {selected_color} African Wax pattern with {selected_shape}."
    st.markdown("### Prompt")
    st.info(prompt)

    num_images = st.number_input("How many images to generate?", min_value=1, max_value=3, value=1)
    st.caption("⚠️ Note - Each image may take up to 5 minutes to generate. Maximum 3 images per batch.")

    if st.button("Generate"):
        images = []
        status = st.empty()
        elapsed_text = st.empty()

        st.session_state.prompt = prompt  # Save the prompt

        # Show previous example patterns
        st.markdown("### Previous Examples")
        cols = st.columns(3)
        for col, ex in zip(cols, example_images):
            with col:
                st.image(ex["url"], caption=ex["caption"], use_container_width='always')

        for i in range(num_images):
            status.info(f"Generating {i + 1} of {num_images}...")
            elapsed_text.text(f"⏳ Time elapsed - 0 seconds")
            result = {"bytes": None, "error": None, "done": False}

            def worker():
                try:
                    img_bytes = generate_image(f"{prompt} Variation {i} {random.randint(0, 99999)}")
                    result["bytes"] = img_bytes
                except Exception as e:
                    result["error"] = str(e)
                finally:
                    result["done"] = True

            thread = threading.Thread(target=worker)
            thread.start()

            elapsed = 0
            while not result["done"]:
                elapsed += 1
                elapsed_text.text(f"⏳ Time elapsed - {elapsed} seconds")
                time.sleep(1)

            thread.join()

            if result["error"]:
                st.error(f"❗ Failed to generate image {i + 1} - {result['error']}")
            elif result["bytes"]:
                images.append(result["bytes"])

        if images:
            st.session_state.images = images
            st.session_state.index = 0
            st.session_state.phase = "result"
            st.rerun()
        else:
            st.warning("No images were successfully generated. Please try again.")

# --- Evaluation Phase ---
elif st.session_state.phase == "result":
    st.title("Your Generated Wax Pattern")
    st.subheader("Prompt Used")
    st.info(st.session_state.get("prompt", "No prompt found."))

    idx = st.session_state.index
    imgs = st.session_state.images

    if idx < len(imgs):
        st.subheader(f"Image {idx + 1} of {len(imgs)}")

        img = Image.open(BytesIO(imgs[idx]))
        st.image(img, width=400)

        buffered = BytesIO()
        img.save(buffered, format="PNG")

        # Download button
        st.download_button(
            label="Download Image",
            data=buffered.getvalue(),
            file_name=f"wax_pattern_{idx + 1}.png",
            mime="image/png",
            key=f"download_button_{idx}"
        )

        # Done/Next button
        is_last = idx == len(imgs) - 1
        btn_label = "Done" if is_last else "Next"

        if st.button(btn_label, key=f"nav_button_{idx}"):
            st.session_state.index += 1
            if is_last:
                for key in ["phase", "images", "index", "prompt"]:
                    st.session_state.pop(key, None)
            st.rerun()
