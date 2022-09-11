import speech_recognition as sr
import sounddevice
from playsound import playsound

def read_mic():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)

        print("Diga")

        audio = mic.listen(source)

        sentence = mic.recognize_google(audio, language='pt-BR')

        print(sentence)

        # if "acelera" in sentence:
        #     playsound("/home/vitindafixa/Downloads/lambo.mp3")

while True:
    read_mic()