import time
import speech_recognition as sr # speech recognition google api
from gtts import gTTS # speech reproduction part
import os # speech reproduction
import wikipedia # wiki api

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
        audio = recognizer.listen(source,  phrase_time_limit=5)

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

if __name__ == "__main__":

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    instructions = ("Please say something!")
    print(instructions)
    time.sleep(2)
    print('You can talk now')
    voicecommand = recognize_speech_from_mic(recognizer, microphone)

    print("You said: {}".format(voicecommand["transcription"]))
    voicecommand = voicecommand["transcription"]

    """
    Reproduction Part
    """

    mytext = search_wiki(voicecommand)

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