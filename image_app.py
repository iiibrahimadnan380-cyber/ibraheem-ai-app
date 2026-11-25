import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("🎨 Mera AI Image App")
st.write("Likho kya banana hai, AI bana dega!")

prompt = st.text_input("Image kaisa chahiye? Example: a cat riding a bike in Lahore")

style = st.selectbox("Style choose karo:", ["Real Photo", "Cartoon", "Anime", "3D", "Painting"])

if st.button("Image Banao ✨"):
    if prompt:
        with st.spinner("AI bana raha hai... 10 sec ruko..."):
            full_prompt = f"{prompt}, {style} style, high quality"
            url = f"https://image.pollinations.ai/prompt/{full_prompt}"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            st.image(img, caption=prompt)
            st.download_button("Download Karo 📥", response.content, "my_image.png", "image/png")
    else:
        st.warning("Pehle kuch likho to sahi!")