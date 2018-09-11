import time
import speech_recognition as sr # speech recognition google api
from gtts import gTTS # speech reproduction part
import os # speech reproduction
import wolframalpha
from playsound import playsound
#split_file = voicecommand.split(' ')

def speak_up(text, language):
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    print("Done")

def _on_button_press(self):
    speak_up("Good afternoon.")
    self.turn_on.on()

def on_button_release(self):
    speak_up("Hope I could help. Goodbye.")
    self.turn_off.off()

def on_button_hold(self):
    print(f"Long button press detected -> stopping...")
    self._keep_running = False

def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("'microphone' must be `Microphone` instance")

  # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source,  phrase_time_limit=8)

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

'''def verbalize (mytext, language): # setting up the computer's ability to answer orally
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("welcome.mp3")
    #os.system("mpg321 welcome.mp3")
    playsound('welcome.mp3')'''

def Q_and_A(voicecommand, language): #2 variables: voiceommand = input, language (linguistic setting)
    app_id = "A87QVU-TU925YT9UR" #from my Wolfram account
    client = wolframalpha.Client(app_id) #defining me, the voice commander

    try: #sub-function that executes the body.
        res = client.query(voicecommand) #client asks a question
        answer = next(res.results).text  #wolfram API responds by text.
        return answer #recognize_speech_from_mic(answer, language) # returns answer orally
    except: #  the equivalent of 'else' that handles a value error. 
        print("No answer. Please ask another question.")
        answer = "What the fuck. Please ask another question." #v
        return answer #recognize_speech_from_mic(answer, language) # if not understood, returns answer orally

if __name__ == "__main__":

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    instructions = ("Please say something!")
    print(instructions)
    time.sleep(1)
    print('You can talk now')
    voicecommand = recognize_speech_from_mic(recognizer, microphone)

    print("You said: {}".format(voicecommand["transcription"]))
    voicecommand = voicecommand["transcription"]

    """
    Reproduction Part
    """

    mytext = Q_and_A(voicecommand,'en')

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    print("Saved")
    myobj.save("welcome.mp3")

    # Playing the converted file
    os.system('mpg321 welcome.mp3')
    print("Done")


