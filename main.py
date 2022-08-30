from zipapp import get_interpreter
import speech_recognition as sr

#Reconhecedor
r = sr.Recognizer()
m = sr.Microphone()
print(r)
with m as source:
    print(source)
    audio = r.listen(source)
    try:
        said = r.recognize_google(audio)
        print(said)
    except Exception as e:
        print("Exception: " + str(e))