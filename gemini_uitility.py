import os
import json
import google.generativeai as ga
import streamlit as st

working_dir = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_dir}/config.json"
config_data = json.load(open(config_file_path))

GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

ga.configure(api_key=GOOGLE_API_KEY)


def load_gemini_pro_model():
    gemini_pro_model = ga.GenerativeModel("gemini-pro")
    return gemini_pro_model
