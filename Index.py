# Before running: Run the command 'pip install -q -U google-generativeai' in your terminal

import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyAiIQLjT6iS7Jivpo2wMK-CbPKmO1gQnPw"
genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)