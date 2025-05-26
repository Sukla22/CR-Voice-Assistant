import eel
import time
import pyttsx3
import speech_recognition as sr

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5') #sapi5 
    voices = engine.getProperty('voices')
    #print(voices)
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',170)  
    eel.DisplayMessage(text) 
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

# C2- @eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language = 'en')
        print(f'User said: {query}')
        #speak(query)
        time.sleep(2)
        eel.DisplayMessage(query)
         # c3- line was upper
       
        
    except Exception as e:
      #  print("error:", e)
        return ""
    
    return query.lower()

# text = takeCommand()

# speak(text)

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takeCommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        if not query:
            speak("Sorry, I didn't catch that.")
            return
        if 'open' in query:
            from engine.features import openCommand
            openCommand(query)
        elif 'on youtube' in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
        elif "send message" in query or "video call" in query or "phone call" in query:
            from engine.features import findContact, whatsapp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):
                if "send message" in query:
                    flag = 'message'
                    speak("what message you want to send")
                    query = takeCommand()
                    
                elif "phone call" in query:
                    flag = 'call'

                else:
                    flag = 'video call'
                print(f"contact_no: {contact_no}, name: {name}, flag: {flag}, query: {query}")
                whatsapp(contact_no, query, flag, name)
        else:
            from engine.features import chatBot
            chatBot(query)
    except Exception as e:
        print("error:", e)
    eel.ShowHood()