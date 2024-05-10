# pip install SpeechRecognition google-generativeai pygame <==== Rode em seu terminal antes de executar o código.

import speech_recognition as sr
import google.generativeai as genai
import pygame

def pagina_inicial():
    print("╭─────────────────────────────────────────────╮\n"
          "│                                             │\n"
          "│                 ChatBot                     │\n"
          "│                                             │\n"
          "│           Selecione o idioma:               │\n"
          "│               1. Português                  │\n"
          "│               2. English                    │\n"
          "│                                             │\n"
          "│          Digite o número do idioma:         │\n"
          "│                                             │\n"
          "╰─────────────────────────────────────────────╯\n"
          "│         Para alterar o idioma, diga:        │\n"
          "│           - \"alterar o idioma\"              │\n"
          "│           - \"change language\"               │\n"
          "│       Para finalizar a conversa, diga:      │\n"
          "│           - \"Até mais Gemini\"               │\n"
          "│           - \"See you Gemini\"                │\n"
          "│                                             │\n"
          "╰─────────────────────────────────────────────╯")

def idioma():
    while True:
        decisao = input("\nEscolha o idioma (1 para Português, 2 para English): ")
        if decisao == "1":
            return "pt-BR"
        elif decisao == "2":
            return "en-US"
        else:
            print("Opção inválida. Por favor, escolha 1 para Português ou 2 para English.")

def inicializacao(idioma):
    genai.configure(api_key="AIzaSyAiIQLjT6iS7Jivpo2wMK-CbPKmO1gQnPw") # <===================== INSIRA A SUA CHAVE API AQUI
    configuracao_geracao = {"temperature": 0.5, 
                            "top_p": 0.5, 
                            "top_k": 4, 
                            "max_output_tokens": 2048}
    
    configuracao_seguranca = [{"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                              {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                              {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                              {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}]
    
    return genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=configuracao_geracao,
                                 safety_settings=configuracao_seguranca)

def captura_audio():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Diga algo...")
            audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language="pt-BR").lower()
        except sr.UnknownValueError:
            print("Desculpe, não entendi o que você disse. Por favor, repita.")
        except sr.RequestError:
            print("O serviço de reconhecimento de fala não está disponível no momento. Por favor, tente novamente mais tarde.")

def tocar_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    pagina_inicial()
    idioma_selecionado = idioma()
    modelo_chatbot = inicializacao(idioma_selecionado)
    print("Bem-vindo ao ChatBot! Agora você pode começar a conversar.")
    while True:
        entrada_usuario = captura_audio()
        if "alterar o idioma" in entrada_usuario or "change language" in entrada_usuario:
            pagina_inicial()
            idioma_selecionado = idioma()
            modelo_chatbot = inicializacao(idioma_selecionado)
            print("O idioma foi alterado para", idioma_selecionado)
            continue
        if "até mais gemini" in entrada_usuario or "see you gemini" in entrada_usuario:
            tocar_audio("goodbye.wav")  
            print("Até mais! Encerrando o ChatBot.")
            break
        partes_prompt = [f"input: {entrada_usuario}"]
        resposta = modelo_chatbot.generate_content(partes_prompt)
        print("Gemini:", resposta.text)
        tocar_audio("notification.wav")

main()
