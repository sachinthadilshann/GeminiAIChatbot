import streamlit as st
import os
from PIL import Image
from streamlit_option_menu import option_menu
from gemini_uitility import *

working_dir = os.path.dirname(os.path.abspath(__file__))
# print(working_dir)

st.set_page_config(
    page_title="Gemini AI",
    layout="centered",
)

with st.sidebar:
    selected = option_menu("Gemini AI",
                           ["Chatbot",
                            "Image Captioning",
                            "Image Captioning",
                            "Embed text",
                            "Ask me anything"])


def translate_role_for_stremlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


if selected == "Chatbot":
    model = load_gemini_pro_model()

    if "Chat Session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(
            history=[]
        )

    st.title("Chatbot")

    for massage in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_stremlit(massage.role)):
            st.markdown(massage.parts[0].text)

    user_prompt = st.chat_input("User: ")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

if selected == "Image Captioning":
    
    st.title("Image Captioning")
    
    upload_image = st.file_uploader("Upload Image....", type=["jpg", "jpeg", "png"])
    
    if st.button("Generate Caption"):
        image = Image.open(upload_image)
        coll1,coll2 = st.columns(2)
        with coll1:
            resize_image = image.resize((800, 500))
            st.image(resize_image)
        dafault_prompt = "Write a caption for this image"
        caption = gemini_pro_vision_captioning(dafault_prompt, image)

        with coll2:
            st.write(caption)
            


