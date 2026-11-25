import streamlit as st
import requests
import urllib.parse

st.title("Mera AI Image App")
st.write("Likho kya banana hai, AI bana dega!")

prompt = st.text_input("Image kaisa chahiye? Example: a cat riding a bike in Lahore")
style = st.selectbox("Style choose karo:", ["Real Photo", "Cartoon", "3D", "Anime", "Painting"])

if st.button("Image Banao ✨"):
    if prompt:
        full_prompt = prompt + " , " + style + " style, high quality"
        encoded = urllib.parse.quote(full_prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&seed=42&nologo=true"
        
        with st.spinner("AI bana raha hai... thoda wait karo..."):
            try:
                st.image(image_url, caption=prompt)
                st.success("Ho gaya! Neeche download kar sakte ho")
                st.markdown(f"[Image Download Karo]({image_url})")
            except Exception as e:
                st.error("Dobara try karo, AI busy hai")
    else:
        st.warning("Pehle kuch likho!")
