import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import time, random, threading

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
    response = requests.post(MODEL_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.content

st.set_page_config(page_title="Wax Pattern Study", layout="centered")

# --- Init Session ---
if "phase" not in st.session_state:
    st.session_state.phase = "setup"
    st.session_state.images = []
    st.session_state.index = 0

# --- Dropdown options ---
colors = ["Red", "Blue", "Yellow", "Green", "Multicolor"]
shapes = ["Circles", "Squares", "Triangles", "Spirals", "Waves"]
themes = ["Traditional", "Modern", "Abstract"]

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

    prompt = f"Create a {selected_color} African Wax pattern with {selected_shape} and {selected_theme} theme."
    st.markdown("### Prompt")
    st.info(prompt)

    num_images = st.number_input("How many images to generate?", min_value=1, max_value=10, value=3)

    if st.button("Create"):
        start_time = time.time()
        images = []
        status = st.empty()
        elapsed_text = st.empty()

        for i in range(num_images):
            status.info(f"Generating {i + 1} of {num_images}...")

            result = {"ready": False, "bytes": None}

            def generate_with_flag():
                result["bytes"] = generate_image(f"{prompt} Variation {i} {random.randint(0, 99999)}")
                result["ready"] = True

            thread = threading.Thread(target=generate_with_flag)
            thread.start()

            while not result["ready"]:
                elapsed = int(time.time() - start_time)
                elapsed_text.text(f"\u23F1 Time elapsed: {elapsed} seconds")
                time.sleep(0.5)

            thread.join()
            images.append(result["bytes"])

        st.session_state.images = images
        st.session_state.index = 0
        st.session_state.phase = "result"
        st.rerun()

# --- Evaluation Phase ---
elif st.session_state.phase == "result":
    idx = st.session_state.index
    imgs = st.session_state.images

    if idx < len(imgs):
        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            st.subheader(f"Image {idx + 1} of {len(imgs)}")

            img = Image.open(BytesIO(imgs[idx]))
            st.image(img, width=400)

            buffered = BytesIO()
            img.save(buffered, format="PNG")
            st.download_button(
                label="Download Image",
                data=buffered.getvalue(),
                file_name=f"wax_pattern_{idx + 1}.png",
                mime="image/png",
                key=f"download_button_{idx}"
            )

            is_last = idx == len(imgs) - 1
            btn_label = "Done" if is_last else "Next"

            if st.button(btn_label, key=f"nav_button_{idx}"):
                st.session_state.index += 1
                if is_last:
                    for key in ["phase", "images", "index"]:
                        st.session_state.pop(key, None)
                st.rerun()