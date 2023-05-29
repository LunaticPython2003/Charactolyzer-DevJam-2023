import streamlit as st
import json
from PIL import Image

from streamlit_lottie import st_lottie
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title='Charactolyzer', page_icon = 'assets/nav-icon.jpg', initial_sidebar_state = 'auto')

def get(path: str):
    with open(path, "r") as p:
        return json.load(p)


robot = get("./assets/welcome-animation.json")
explore = get("./assets/explore.json")

col1, col2 = st.columns([1.4, 4.3], gap="medium")

with col1:    
    image = Image.open('./assets/devjam.png')
    st.image(image, caption='Devjam Season 1')

with col2:
    image = Image.open('./assets/devfolio-icon.png')
    st.image(image, caption='')


## Multiple screen
with st.container():
    st.markdown("<h1 style='text-align: center;'>Charactolyser</h1>",
                unsafe_allow_html=True)
    st.write("<div style='text-align: center;'>Welcome to our Personality Detector website!</div>", unsafe_allow_html=True)

    st.write("<div style='text-align: center;'><br> Have you ever wondered what makes you unique? Are you curious to uncover the hidden aspects of your personality? Look no further! Our cutting-edge Personality Detector is here to provide you with deep insights into the intricate layers of your individuality.Discovering and understanding our personalities is a journey that can shape our lives and relationships. Whether you're seeking personal growth, professional development, or simply satisfying your curiosity, our state-of-the-art tool is designed to decode the enigma of who you truly are. <br><br><br></div>", unsafe_allow_html=True)

    st.markdown("<div style='text-align: center;'><h3>How does it work?</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1], gap="small")

with col1:
    st.markdown("")

with col2:
    st_lottie(robot, height=350, width=350)

with col3:
    st.markdown("")


with st.container():
    st.markdown("")
    st.write("<div style='text-align: center;'>Our <b>Personality Detector</b> combines advanced artificial intelligence algorithms with psychological theories to analyze various aspects of your behavior, preferences, and thought patterns with the help of your text. <br><br>Our mission is to empower you with knowledge about your personality that can lead to personal transformation, improved self-awareness, and enhanced decision-making. By gaining insights into your unique strengths, weaknesses, and motivations, you'll be equipped to make more informed choices, forge deeper connections, and navigate life's challenges with confidence. Get started now and embrace the power of self-discovery! Remember, the more we understand ourselves, the better equipped we are to embrace our strengths, improve our weaknesses, and live a life that is truly authentic.<br><br><h3> Let the journey begin!</h3></div>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 3, 1], gap="small")

with col1:
    st.markdown("")

with col2:
    st_lottie(explore, height=500, width=500)

with col3:
    st.markdown("")