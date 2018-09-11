from gtts import gTTS # speech reproduction part
import os # speech repro
import pyaudio
import speech_recognition as sr # speech recognition google api

def speak_up(text, language):
   myobj = gTTS(text=text, lang=language, slow=False)
   myobj.save("welcome.mp3")
   # Playing the converted file
   os.system("mpg321 welcome.mp3")
   print("Done")





hello = ("Hello Master! I am so happy to see you today., My name is Nyx, and I am your personal learning assistant., I am programmed to assist you in your daily tasks, such as: weather forecasting, searching for definitions or general questions, and assist you with all the provisions you need to pass your law exam,. For example, in order to answer one of your general questions or if you want to know how is the weather in a city of your choice, you just need to activate me with specific voice commands, and then ask your question. To answer your questions, I make use of API's including:, OpenWeatherMap, Wikipedia, and Wolfram Alpha., Each of these functionalities has a different activation voice command, If you want to ask me general questions, you can begin with 'Find'. If you are curious about the weather you can tell me, 'weather' followed by the name of the city., To retrieve specific definitions, you can activate me by saying 'wiki', and for the a personal law assistance you can awake me with 'article'., In fact, thanks to my multiple functionalities, I can also help students to search for a word directed to a specific legal provision., This support is connected to www.admin.ch with the use of Web Scraping, which allows to the information to be always up to date., So, how do you start?, You can begin by personalize my assistance according to your preferences, with upcomming updates you will be able to select from a wide range of languages.")
speak_up.(hello,"en")

german = ("Hallo, ich heisse Gertrud und bin ihr persoenlicher Assistent")
speak_up(german, "de")
french = ("Salut, je suis Bernadette, et je suis pret a repondre a toutes vos questions")
speak_up(french, "fr")
italian = ("Ciao, sono Mario e mi piacerebbe aiutarti a rispondere alle tue domande.")
speak_up(italian, "it")
end = (", What are you waiting for?, Just test me.")
speak_up(end, "en")
print("done")
