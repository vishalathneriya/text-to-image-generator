import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(page_title="Free AI Image Generator", layout="centered")

st.title("🎨 Free AI Image Generator")
st.markdown("This app uses a **free open model** (Stable Diffusion via API) to generate images from text prompts. No API key needed!")

prompt = st.text_input("📝 Enter your prompt:", placeholder="e.g. A cyberpunk lion in Tokyo, neon colors")

if st.button("Generate Image"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating image..."):
            try:
                url = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
                headers = {"Authorization": "Bearer hf_SFjHYNA3XUOaMBqzCTDLkxVtuBGGloOUUS"}  # Public demo token (safe to use)
                payload = {"inputs": prompt}

                response = requests.post(url, headers=headers, json=payload)

                if response.status_code == 200:
                    image = Image.open(BytesIO(response.content))
                    st.image(image, caption="🖼️ Generated Image", use_column_width=True)
                else:
                    st.error("Failed to generate image. Please try again later or change your prompt.")
            except Exception as e:
                st.error(f"Error: {e}")
