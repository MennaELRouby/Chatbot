#Importing some important libraries
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

#Creating some variables for the format

blueish_white = "#F5FFFA"
dark_blue = "#36648B"
fluorescent_green = "#39c790"
black = "#0F0F0F"

#Creating the window

root = Tk()
root.title("Translator")
root.geometry("821x400")
root.resizable(1, 1)
root.configure(bg=dark_blue)

#Creating the translate and clear functions

def translate_it():

    #Delete any previous translation

    output_text.delete(1.0, END)

    #Get languages from dictionary keys, Get the from language keys, Get the to language keys

    try:
        for key, value in languages.items():
            if (value == input_combo.get()):
                from_language_key = key

        for key, value in languages.items():
            if (value == output_combo.get()):
                to_language_key = key

        #Turning input_Text into a TextBlob

        words = textblob.TextBlob(input_text.get(1.0, END))

        #Translate text

        words = words.translate(from_lang=from_language_key ,to=to_language_key)

        #Output translated text to screen

        output_text.insert(1.0, words)
    except Exception as e:
        messagebox.showerror("ERORR", e)

def clear():
    input_text.delete(1.0, END)
    output_text.delete(1.0, END)

#Get language list from googletrans library

languages = googletrans.LANGUAGES

#Convert language_list to a python list

language_list = list(languages.values())

#Creating text boxes

input_text = Text(root, height=8, width=33, font=("Times 14"), bg=blueish_white, fg=black)
input_text.grid(row=0,column=0, pady=20, padx=10)

output_text = Text(root, height=8, width=33, font=("Times 14"), bg=blueish_white, fg=black)
output_text.grid(row=0,column=2, pady=20, padx=10)

#Creating translate button

translate_button = Button(root, text="Translate", font=("Times 24 bold"), bg=fluorescent_green, fg=black, command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

#Creating comboboxes

input_combo = ttk.Combobox(root, width=40, value=language_list)
input_combo.current(21)
input_combo.grid(row=2, column=0)

output_combo = ttk.Combobox(root, width=40, value=language_list)
output_combo.current(30)
output_combo.grid(row=2, column=2)

#Creating clear button

clear_button = Button(root, text="Clear", font=("Times 18 bold"), bg=fluorescent_green, fg=black, command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()