import gtts
from playsound import playsound 
#make request to google to get synthesis
tts = gtts.gTTS("elsalam alikom")
tts.save("hello.mp3")
playsound('hello.mp3')


