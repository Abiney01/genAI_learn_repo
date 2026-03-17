import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)
    print("Audio captured successfully...")