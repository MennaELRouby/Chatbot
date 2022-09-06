from webbrowser import get
import pyttsx3
import time

engine = pyttsx3.init()

engine.setProperty('rate', 160)

voices = engine.getProperty('voices')

print(voices)

engine.setProperty('voice', voices[0])
answer = ('what do you want to say?')
engine.say(answer)
engine.runAndWait()
   