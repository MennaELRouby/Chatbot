import speech_recognition as sr
from speech_recognition import Microphone, Recognizer
recog = sr.Recognizer()
mic= sr.Microphone()


with mic:
    print("speak....")
    audio = recog.listen(mic, 3)


recognized = recog.recognize_google(audio, language = "en")
print("you said:", recognized)    

