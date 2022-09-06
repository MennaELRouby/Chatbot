from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer, UbuntuCorpusTrainer
from nltk.corpus import brown
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as ScrolledText
import time
from tkinter import *
import keyboard


"""
Fetures Done:
Best Match 
Math solver
Time telling
Timer
Internet Search
Weather
"""

#Database

#Login Sgin up system

#Learn from convos and save as .yml

#Emotion recognition
#Face Recognition
#Voice recognition

#10 hour forcast weather
#Simple GUI

#Music Play (pause, continue, stop)
#YouTube play

bot = ChatBot(
    #Bot name
    "Elon",

    storage_adapter="chatterbot.storage.SQLStorageAdapter",

    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],


    logic_adapters= [
        #Best Match Adapter
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90,
            "statement_comparison_function": "chatterbot.comparisons.SpacySimilarity",
        },

        #Math Adapter
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        },

        #Specefic Response adapter 1
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'who are you',
            'output_text': 'I am Elon your virtiual assistant'
        },

        #Time Adapter
        {
            "import_path": "logic.time_adapters.WhatTimeAdapter"
        },

        #Timer Adapter
        {
            "import_path": "logic.time_adapters.TimerAdapter"
        },

        #Temp Adapter
        {
            "import_path": "logic.weather_adapter.WhatTempAdapter"
        },

        #Weather Adpater
        {
            "import_path": "logic.weather_adapter.WhatWeatherAdapter"
        },

        #Internet Search
        {
            "import_path": "logic.search_internet.WIKISearch"
        },

        {
            "import_path": "logic.apps.Calculator_App"
        },

        {
            "import_path": "logic.apps.Translator_App"
        }
    ]
)


def text_state():
    #Introduction
    print('\n\nHi i am Elon your virtiual assistant\n')
    #Code loop
    while True:
        user_input = input('You: ')
        bot_response = bot.get_response(user_input)
        print(f'Elon: {bot_response}' + '\n')

def voice_state():
    import speech_recognition as sr
    from speech_recognition import Microphone, Recognizer
    from webbrowser import get
    import pyttsx3

    while True:
        recog = sr.Recognizer()
        mic= sr.Microphone()


        with mic:
            print("Speak....")
            audio = recog.listen(mic, 3)

        recognized = recog.recognize_google(audio, language = "en")

        print(f'You: {recognized}')

        bot_response = bot.get_response(recognized) 

        engine = pyttsx3.init()

        engine.setProperty('rate', 160)

        voices = engine.getProperty('voices')
        engine.setProperty('voices', voices[1].id)

        print(f'Elon: {bot_response}' + '\n')

        engine.say(bot_response)
        engine.runAndWait()  

class TkinterGUIExample(tk.Tk):

    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Chatterbot")

        self.initialize()

    def initialize(self):
        """
        Set window layout.
        """
        global res
        self.grid()

        self.respond = Button(self, text='Get Response', command=self.get_response)
        self.respond.grid(column=1, row=3, sticky='nesw', padx=5, pady=20)

        res = self.respond

        self.usr_input = Entry(self, state='normal')
        self.usr_input.grid(column=0, row=3, sticky='nesw', padx=5, pady=20)

        self.conversation_lbl = Label(self, anchor=tk.E, text='Conversation:')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)

    if keyboard.is_pressed('enter'):
        print('Enter')
        res.invoke()

    def get_response(self):
        """
        Get a response from the chatbot and display it.
        """
        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        response = bot.get_response(user_input)

        self.conversation['state'] = 'normal'
        self.conversation.insert(
            tk.END, "Human: " + user_input + "\n" + "ChatBot: " + str(response) + "\n"
        )
        self.conversation['state'] = 'disabled'

        time.sleep(0.5)

trainer = ChatterBotCorpusTrainer(bot)

trainer.train()

gui_example = TkinterGUIExample()
gui_example.mainloop()