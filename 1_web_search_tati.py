import wikipedia

def search_wiki(word):
    definition = wikipedia.summary(word, sentences=1)
    return definition

