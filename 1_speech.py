import time
import speech_recognition as sr # speech recognition google api
from gtts import gTTS # speech reproduction part
import os # speech reproduction
import wikipedia # wiki api
import requests
import wolframalpha
import urllib.request #use urllib2 for python 2.7
from bs4 import BeautifulSoup
import json
from unidecode import unidecode


def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source,  phrase_time_limit=4)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def search_wiki(word):
   definition = wikipedia.summary(word, sentences = 3)
   return definition

def search_weather(voicecommand):
    city = voicecommand
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=eb75bcb7f27a558426f5dc71d4ba6dbc&units=metric'.format(city)
    json_data = requests.get(url)
    data = json_data.json()
    temp = data['main']['temp']
    clouds = data['weather'][0]['description']

    phrase1= 'the Temperature is' + str(temp) + 'Degrees Celsius in' + city + 'with' + str(clouds)
    return phrase1

def Q_and_A(voicecommand):
    app_id = "A87QVU-TU925YT9UR"
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(voicecommand)
        result = next(res.results).text
        return result
    except Exception as e:
        print("No answer. Please ask another question.")
        result = "No answer. Please ask another question."  # v
        return result


def remove_non_ascii(text):
    return unidecode(unicode(text, encoding= "utf'8"))

def scrape_admin():
    # specify the url
    quote_page = 'https://www.admin.ch/opc/en/classified-compilation/19110009/index.html#indexni1'

    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(quote_page)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    print(type(soup))

    # specify the url
    quote_page = 'https://www.admin.ch/opc/en/classified-compilation/19110009/index.html#indexni1'

    list_articles = soup.find_all("h5")
    list_content = soup.find_all("div", attrs = {"class" : "collapseableArticle"})
    print("got the list")

    list_of_articles = []

    x = 0
    for i in range (0, (len(list_articles) - 1)):  # exclude last article it has different format

        articles = {
            "article_name" : list_articles[i].text.strip(), #.decode('utf-8', 'ignore').encode('utf-8'),   # name of the article
            "article_number" : list_articles[i].text.strip().split(" ")[1],
            "article_content" : list_content[i].text.strip().split('1', 1)[-1]
        }

        list_of_articles.append(articles)
        x = x +1

    with open('scrape_admin_all.txt', 'w') as file:
        file.write(json.dumps(list_of_articles))
        file.close()

    return list_of_articles

def search_article(voicecommand):
    search_word= voicecommand  # link to voice HERE
    list_of_articles = scrape_admin()
    list_of_results=[]
    list_of_articles_numbers= []

    for article in list_of_articles:

        if search_word in article["article_content"].lower().split(" "):
            list_of_results.append(article)
            list_of_articles_numbers.append(article["article_number"])


    with open('scrape_admin.txt', 'w') as file:
        file.write(json.dumps(list_of_articles_numbers))
        file.close()

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    answer = "Your search word appears in total of " + str(len(list_of_articles_numbers)) + " articles among them are , article " + ", article ,".join(list_of_articles_numbers[0:2]) + ".. For an overview of the whole list of articles, please check the file scrape admin.txt"

    return answer


if __name__ == "__main__":

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    valid_voice_input = False

    key_words = ['weather','search','exit','find','article']

    speak_up("welcome master", "en")
    speak up("Je m'appelle Nyx", 'fr')
    speak up('Como posso aiutarti?', 'it')
    speak_up("Please select a language", "ru")

    voicecommand = recognize_speech_from_mic(recognizer, microphone)

    speak_up("You've selected {}".format(voicecommand["transcription"]), "en")

    while valid_voice_input == False:
        # Language in which you want to convert
        language = 'en'
        instructions = ("How may I help you?")
        print(instructions)
        myobj = gTTS(text=instructions, lang=language, slow=False)
        # Saving the converted audio in a mp3 file named
        # welcome
        myobj.save("welcome.mp3")
        # Playing the converted file
        os.system("mpg321 welcome.mp3")
        time.sleep(2)
        print('GO!')
        voicecommand = recognize_speech_from_mic(recognizer, microphone)

        print("You said: {}".format(voicecommand["transcription"]))
        voicecommand = voicecommand["transcription"]

        if voicecommand == None : continue

        voicecommand = voicecommand.split()

        if voicecommand[0].lower() == 'weather':
            voicecommand = " ".join(voicecommand[1:])
            answer = search_weather(voicecommand)
            valid_voice_input = True
        if voicecommand[0].lower() == 'search':
            voicecommand = " ".join(voicecommand[1:])
            answer = search_wiki(voicecommand)
            valid_voice_input = True

        if voicecommand[0].lower() == 'exit':
            voicecommand= " ".join(voicecommand[1:])
            answer = "exit program"
            valid_voice_input = True

        if voicecommand[0].lower() == 'find':
            voicecommand= " ".join(voicecommand[1:])
            answer = Q_and_A(voicecommand)
            valid_voice_input = True

        if voicecommand[0].lower() == 'article':
            voicecommand = " ".join(voicecommand[1:])
            answer = search_article(voicecommand)
            valid_voice_input = True

        """
        Reproduction Part     
        """
    #mytext = search_wiki(voicecommand)


    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed

    myobj = gTTS(text=answer, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")
    # Playing the converted file
    os.system("mpg321 welcome.mp3")
    print("Done")