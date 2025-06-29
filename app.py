import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("🧠 Stable Diffusion Image Generator (FREE)")
st.markdown("Generate AI images using Hugging Face Stable Diffusion – No API Key Needed")

prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if prompt.strip():
        with st.spinner("Generating image... please wait..."):
            try:
                # Using Hugging Face space (public)
                url = "https://huggingface.co/spaces/stabilityai/stable-diffusion"
                payload = {"inputs": prompt}
                headers = {"Content-Type": "application/json"}

                response = requests.post(
                    "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4",
                    headers={"Authorization": f"Bearer hf_SFjHYNA3XUOaMBqzCTDLkxVtuBGGloOUUS"},
                    json=payload,
                )

                if response.status_code == 200:
                    image = Image.open(BytesIO(response.content))
                    st.image(image, caption="🎨 AI Generated Image", use_column_width=True)
                else:
                    st.error("❌ Failed to generate image. Try again later.")
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a prompt.")
