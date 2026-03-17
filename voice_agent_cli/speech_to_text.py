import speech_recognition as sr
recognizer = sr.Recognizer()

def listen_command():  
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing")
        text = recognizer.recognize_google(audio)
        print("You said :",text)
        return text.lower()
    except:
        print("Couldn't recognize audio")
