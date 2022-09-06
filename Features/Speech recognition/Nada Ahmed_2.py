import speech_recognition as sr
from speech_recognition import Microphone, Recognizer

Microphone = sr.Recognizer()

with Microphone as mic:
    
    audio_text = Microphone.listen(mic)
    

    try:
        
        text = Microphone.recognize_google(audio_text)
        print('Converting audio to text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')