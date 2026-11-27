import streamlit as st
import urllib.parse
import random

st.set_page_config(page_title="Mera AI Image App", page_icon="🎨")

st.title("🎨 Mera AI Image App")
st.write("Likho kya banana hai, AI bana dega!")

prompt = st.text_input("Image kaisa chahiye?", placeholder="Example: a cat riding a bike in Lahore")
style = st.selectbox("Style choose karo:", ["Real Photo", "Cartoon", "3D", "Anime", "Painting"])

if st.button("Image Banao ✨"):
    if not prompt:
        st.warning("⚠️ Pehle kuch likho!")
    else:
        full_prompt = prompt + ", " + style + " style, ultra detailed, high quality"
        encoded = urllib.parse.quote(full_prompt)
        seed = random.randint(1, 99999)
        
        # YAHAN APNA TOKEN LAGAO - pk_ wala code paste karo
        TOKEN = "sk_B8VzFuFlq0AOhacS9C9WiVe5pg0eHlS1"
        
        image_url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&seed={seed}&model=flux&nologo=true&token={TOKEN}"
        
        with st.spinner("⏳ AI bana raha hai... 10-20 second lagega..."):
            st.image(image_url, caption=prompt, use_container_width=True)
        
        st.success("✅ Ho gaya! Image ban gayi!")
        st.markdown(f"### [📥 Image Download Karo]({image_url})")
