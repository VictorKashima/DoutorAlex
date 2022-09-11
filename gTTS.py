from operator import gt
from gtts import gTTS
from playsound import playsound

def speak(text):
    tts = gTTS(text=text, lang="ja")
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)

speak("konnichiwa")