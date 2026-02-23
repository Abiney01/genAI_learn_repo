import speech_recognition as sr
import os
from dotenv import load_dotenv
from openai import OpenAI
import pyttsx3
load_dotenv()

engine = pyttsx3.init()

def speak(text):
    engine.setProperty('rate', 170)   # Speed of speech
    engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

def main():
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
    )
    SYSTEM_PROMPT = '''
    You're a expert voice agent. You will be given the transcription of what the user has said and you have to reply accordingly.
    Whatever you have said it will be transcribed using an AI
'''


    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        print("Speak something...")
        audio = r.listen(source)

        print("Processing audio..")
        stt = r.recognize_google(audio)

        print("Processed audio is:", stt)
        print("Waiting for llm respone...")
        
        response = client.chat.completions.create(
            model="gemini-3-flash-preview",
            messages=[
                {"role" : "system" , "content" : SYSTEM_PROMPT},
                {"role" : "user" , "content" : stt}
            ]
        )
        ai_response = response.choices[0].message.content
        print("AI response :", ai_response)
        speak(ai_response)
main()