from translate import Translator

langauage = input("choose a language")

translator= Translator(from_lang="english",to_lang= langauage)
text = input("what do you want to translate?")
translation = translator.translate(text)

print(translation)

