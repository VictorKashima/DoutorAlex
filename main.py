import speech_recognition as sr
import sounddevice
from playsound import playsound
import Speaker

def read_mic():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)

        print("Diga")

        audio = mic.listen(source)

        sentence = mic.recognize_google(audio, language='pt-br')

        print(sentence)

        Speaker.speak(sentence)

while True:
    read_mic()