from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image
import json
import model

st.set_page_config(page_title="Analysis", page_icon="📈")


def get(path: str):
    with open(path, "r") as p:
        return json.load(p)

with st.container():
    st.markdown("<h1 style='text-align: center;'> Charactolyser</h1>",
            unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Unlock the secrets of your conversations with our Charactolyser</h4>",
            unsafe_allow_html=True)
    st.write("<div style='text-align: center;'><b>Upload</b> your chat history today and unlock a new level of self-awareness, enriched relationships, and personal growth. Your conversations hold the key to a deeper understanding of yourself and those around you. Let's embark on this transformative journey together!<br><br></div>", unsafe_allow_html=True)


analyse = get("./assets/analyse.json")
col1, col2, col3 = st.columns([1, 3, 1], gap="small")

with col1:
    st.markdown("")

with col2:
    st_lottie(analyse, height=350, width=350)

with col3:
    st.markdown("")

uploaded_file = st.file_uploader("Choose a .txt file", type=['txt'])
if uploaded_file is not None:
    file = uploaded_file.read()
    with open('uploads/test.txt', "wb") as temp:
        temp.write(file)

    if st.button('Analyse'):
        scores = model.main()
        st.write(scores)