import streamlit as st

st.set_page_config(layout="wide")
st.title("🧠 AI Image Generator (LIVE UI) – Free")

st.markdown("""
Generate amazing AI images using Hugging Face's public space — No API key needed.  
Prompt likho niche Hugging Face ke embedded tool mein 👇 and get instant results!
""")

# Hugging Face public space embedded
st.components.v1.iframe("https://huggingface.co/spaces/stabilityai/stable-diffusion", height=720)
