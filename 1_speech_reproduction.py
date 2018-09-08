from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
import wikipedia

def search_wiki(word):
   definition = wikipedia.summary(word, sentences = 1)
   return definition

# The text that you want to convert to audio
mytext = search_wiki("Love")

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")