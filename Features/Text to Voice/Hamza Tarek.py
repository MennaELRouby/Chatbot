
import os
from gtts import gTTS

user_text = input('write your text: ')

    
tts = gTTS(text=user_text,slow=False,lang = 'en',tld ='co.in')
#accents in tld I use mainly: com.au , co.in, co.uk#
tts.save('user_text.wav')

audio_file = 'user_text.wav'

os.system(f'start {audio_file}')
    