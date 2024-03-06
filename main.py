import streamlit as st
import os
from PIL import Image
from streamlit_option_menu import option_menu
from gemini_uitility import *

working_dir = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="Gemini AI",
    layout="centered",
)

with st.sidebar:
    selected = option_menu("Gemini AI", [
        "Chatbot",
        "Image Captioning",
        "Ask Me Anything",
    ])


def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "Assistant"
    else:
        return user_role


if selected == "Chatbot":
    model = load_gemini_pro_model()

    if "Chat Session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    st.title("Chatbot")

    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    user_prompt = st.chat_input("User: ")
    if user_prompt:
        st.chat_message("User").markdown(user_prompt)
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

if selected == "Image Captioning":

    st.title("Image Captioning")

    uploaded_image = st.file_uploader("Upload Image...", type=["jpg", "jpeg", "png"])

    if st.button("Generate Caption"):
        if uploaded_image is not None:
            try:
                image = Image.open(uploaded_image)
                coll1, coll2 = st.columns(2)
                with coll1:
                    resize_image = image.resize((800, 500))
                    st.image(resize_image)
                default_prompt = "Write a caption for this image"
                caption = gemini_pro_vision_captioning(default_prompt, image)

                with coll2:
                    st.write(caption)
            except Exception as e:
                st.error(f"Error processing image: {e}")
        else:
            st.warning("Please upload an image first.")

if selected == "Ask me anything":

    st.title("❓ Ask me a question")

    user_prompt = st.text_area(label='', placeholder="Ask me anything...")

    if st.button("Get Response"):
        response = gemini_pro_response(user_prompt)
        st.markdown(response)
