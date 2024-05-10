# Before running: Run the command 'pip install -q -U google-generativeai' in your terminal.

import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyAiIQLjT6iS7Jivpo2wMK-CbPKmO1gQnPw"
genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

generation_config = {
    "candidate_count": 1,
    "temperature:": 0.5,
    #"top_p"
    #"top_k"
}

safety_settings = {
    # Block_None
    # Block_Few
    # Block_Some
    # Block_Most
    "Harassment": "Block_None",
    "Hate": "Block_None",
    "Sexual": "Block_None",
    "Dangerous": "Block_None",
}