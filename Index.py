# Before running: Run the command 'pip install -q -U google-generativeai' in your terminal.

# Installing the Python SDK for the Gemini API
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyAiIQLjT6iS7Jivpo2wMK-CbPKmO1gQnPw"
genai.configure(api_key=GOOGLE_API_KEY)

# Setting up the model parameters
#for m in genai.list_models():
#    if 'generateContent' in m.supported_generation_methods:
#        print(m.name)

text_Generation_Filter = {
    "candidate_count": 1,
    "temperature": 0.5,
    #"top_p"
    #"top_k"
}

safety_Text_Filter = {
    # Block_None
    # Block_Few
    # Block_Some
    # Block_Most
    "Harassment": "Block_None",
    "Hate": "Block_None",
    "Sexual": "Block_None",
    "Dangerous": "Block_None",
}

# Initializing the model
model = genai.GenerativeModel(model_name="gemini-1.0-pro-latest",
                              generation_config=text_Generation_Filter,
                              safety_settings=safety_Text_Filter)


response = model.generate_content("Ola, tudo bem?")
print(response.text)

chat = model.start_chat(history=[])
prompt = input("Esperando prompt: ")

while prompt != "fim":
    response = chat.send_message(prompt)
    print("Resposta: ", response.text, "\n")
    prompt = input("Esperando prompt: ")


# Melhorando a visualização
# Código disponível em https://ai.google.dev/tutorials/python/quickstart#import_packages
import textwrap
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  """Formata o texto para Markdown para melhor visualização no notebook."""
  text = text.replace("`", r"\`")
  return Markdown(textwrap.indent(text, "  ", predicate=lambda _: True))

# Imprimindo o histórico:
for message in chat_history:
  display(to_markdown(f"**{message.role}:** {message.parts[0].text}"))
  print("---")