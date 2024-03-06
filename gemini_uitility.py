import os
import json
import google.generativeai as ga


working_dir = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_dir}/config.json"
config_data = json.load(open(config_file_path))

GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

ga.configure(api_key=GOOGLE_API_KEY)


def load_gemini_pro_model():
    gemini_pro_model = ga.GenerativeModel("gemini-pro")
    return gemini_pro_model


def gemini_pro_vision_captioning(prompt, image):
    gemini_pro_vision_model = ga.GenerativeModel("gemini-pro-vision")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result
