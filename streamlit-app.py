import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI
import base64
import openai


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Just kidding", page_icon=":shark:", layout="centered")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- HEADER SECTION ----
st.header("Welcome to Witzworld :shark: ")

with st.container():
    selected = option_menu(None, ["jb1", 'jb2', 'jb3'], icons=['house', 'file', 'envelope'], menu_icon="cast", default_index=0, orientation="horizontal", )

    if selected == "jb1":
        # ----- USER TEXT BOX ------
        # get the user's input by calling the get_text function
        def get_text():
            input_text = st.text_input("Once you are ready, you can write your theme for a joke and hit enter to hear from JOKE agent, JB1!", key="input")
            return input_text

        user_input = get_text()
        
    if selected == "jb2":
        st.title("Jokebot2")
        
    if selected == "jb3":
        st.title("Jokebot3")

