from gtts import gTTS
from playsound import playsound

def speak(text):
    tts = gTTS(text=text, lang="pt")
    voip = "voip.mp3"
    tts.save("audios/voip.mp3")
    playsound("audios/voip.mp3")

def welcome():
    playsound("audios/welcome.mp3")