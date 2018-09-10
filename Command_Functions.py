import wolframalpha
from playsound import playsound
#split_file = voicecommand.split(' ')

def verbalize (mytext, language): # setting up the computer's ability to answer orally
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("welcome.mp3")
    #os.system("mpg321 welcome.mp3")
    playsound('welcome.mp3')

def Q_and_A(voicecommand, language): #2 variables: voiceommand = input, language (linguistic setting)
    app_id = "A87QVU-TU925YT9UR" #from my Wolfram account
    client = wolframalpha.Client(app_id) #defining me, the voice commander

    try: #sub-function that executes the body.
        res = client.query(voicecommand) #client asks a question
        answer = next(res.results).text  #wolfram API responds by text.
        return verbalize(answer, language) # returns answer orally
    except: #  the equivalent of 'else' that handles a value error. 
        print("No answer. Please ask another question.")
        answer = "No answer. Please ask another question." #v
        return verbalize(answer, language) # if not understood, returns answer orally

