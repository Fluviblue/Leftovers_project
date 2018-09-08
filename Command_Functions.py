import wolframalpha
#split_file = voicecommand.split(' ')

def Q_and_A(voicecommand, language):
    app_id = "A87QVU-TU925YT9UR"
    client = wolframalpha.Client(app_id)

    try:
        res = client.query(voicecommand)
        answer = next(res.results).text
        return verbalize(answer, language)
    except:
        print("No answer. Please ask another question.")
        answer = "No answer. Please ask another question."
        return verbalize(answer, language)

def verbalize (mytext, language):
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")