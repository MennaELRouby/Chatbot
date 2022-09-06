# Importing some important libraries
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

# Creating some variables for the format

blueish_white = "#F5FFFA"
dark_blue = "#36648B"
fluorescent_green = "#39c790"

# Creating the window

root = Tk()
root.title("Text To Voice")
root.geometry("900x450")
root.resizable(1, 1)
root.configure(bg=dark_blue)

# Creating speak, speed, voice, save, clear function

engine = pyttsx3.init()


def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if(gender == "Male"):
            engine.setProperty("voice", voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty("voice", voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if(speed == "Very Slow"):
            engine.setProperty("rate", 10)
            setvoice()

        if (speed == "Slow"):
            engine.setProperty("rate", 80)
            setvoice()

        if (speed == "Normal"):
            engine.setProperty("rate", 115)
            setvoice()

        if (speed == "Fast"):
            engine.setProperty("rate", 200)
            setvoice()

        if (speed == "Very Fast"):
            engine.setProperty("rate", 500)
            setvoice()


def clear():
    entry.delete(0, END)


def downloadnow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if (gender == "Male"):
            engine.setProperty("voice", voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, "text.mp3")
            engine.runAndWait()
        else:
            engine.setProperty("voice", voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, "text.mp3")
            engine.runAndWait()

    if (text):
        if (speed == "Very Slow"):
            engine.setProperty("rate", 10)
            setvoice()

        if (speed == "Slow"):
            engine.setProperty("rate", 80)
            setvoice()

        if (speed == "Normal"):
            engine.setProperty("rate", 115)
            setvoice()

        if (speed == "Fast"):
            engine.setProperty("rate", 200)
            setvoice()

        if (speed == "Very Fast"):
            engine.setProperty("rate", 500)
            setvoice()

# Creating the text input area


Label(root, text="Write Here", font="Times 20 bold italic",
      bg=dark_blue, fg=blueish_white).place(x=10, y=10)
text_area = Text(root, font="Times 20 ", bg=blueish_white,
                 relief=GROOVE, wrap=WORD)
text_area.place(x=30, y=50, width=500, height=250)

# Creating different voices

Label(root, text="Voice", font="Times 15 bold italic",
      bg=dark_blue, fg=blueish_white).place(x=580, y=25)
gender_combobox = Combobox(
    root, values=["Male", "Female"], font="Times 14", state="r", width=10)
gender_combobox.place(x=550, y=50)
gender_combobox.set("Male")

# Creating different Speeds

Label(root, text="Speed", font="Times 15 bold italic",
      bg=dark_blue, fg=blueish_white).place(x=760, y=25)
speed_combobox = Combobox(root, values=[
                          "Very Slow", "Slow", "Normal", "Fast", "Very Fast"], font="Times 14", state="r", width=10)
speed_combobox.place(x=730, y=50)
speed_combobox.set("Normal")

# Creating the speak button

speak = PhotoImage(file="Speak.png")
speak_button = Button(root, text="Speak", compound=LEFT, image=speak, width=150, font="Times 25 bold italic",
                      bg=fluorescent_green, fg=blueish_white, command=speaknow)
speak_button.place(x=620, y=150)

# Creating the save button

save = PhotoImage(file="download.png")
save_button = Button(root, text="Save", compound=LEFT, image=save, width=150, font="Times 25 bold italic",
                     bg=fluorescent_green, fg=blueish_white, command=downloadnow)
save_button.place(x=620, y=250)

# Creating the clear button

clear_button = Button(root, text="Clear", width=10, font="Times 25 bold italic",
                      bg=fluorescent_green, fg=blueish_white, command=clear)
clear_button.place(x=597, y=350)

root.mainloop()
