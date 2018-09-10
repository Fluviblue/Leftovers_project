import time
import speech_recognition as sr # speech recognition google api
from gtts import gTTS # speech reproduction part
import os # speech reproduction
import wikipedia # wiki api
import requests

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
   definition = wikipedia.summary(word, sentences = 1)
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

if __name__ == "__main__":



    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    valid_voice_input = False

    key_words = ['weather', 'search','exit']

    while valid_voice_input == False:

        instructions = ("Please say something in 3 seconds!")
        print(instructions)

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
            voicecommand = " ".join(voicecommand[1:])
            answer = "exit program"
            valid_voice_input = True

        """
        Reproduction Part
        """
    #mytext = search_wiki(voicecommand)
    # Language in which you want to convert
    language = 'en'

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
