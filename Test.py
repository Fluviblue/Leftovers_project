'''def Search_Wiki(word):
    if voicecommand = [word]:
    definition = wikipedia.summary(word, sentences=1)
    return myobj = gTTS(text=definition, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")'''

import wikipedia

def search_wiki(word):
    definition = wikipedia.summary(word, sentences=1)
    return definition

print(search_wiki("love"))
