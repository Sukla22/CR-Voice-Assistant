import os
import struct
import subprocess
import time
from playsound import playsound #c4
import eel
import sqlite3
import webbrowser

import pyaudio
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import re
from engine.helper import extract_yt_term, remove_words

import pyautogui 
import pvporcupine
from urllib.parse import quote
from hugchat import hugchat

conn = sqlite3.connect("crassistant.db")
cursor = conn.cursor()
# sound function for playing sounds
def playAssistantSound():
    music_dir = "www\\assets\\audio\\joon_voice.mp3"
    playsound(music_dir)


# sound function for click sound in mic
@eel.expose
def playClickSound():
    music_dir = "www\\assets\\audio\\click.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "").strip().lower()

    if query != "":
        try:
            #Try to find the application in sys_command table
            cursor.execute('SELECT path FROM sys_command WHERE LOWER(name) =?', (query,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+ query)
                os.startfile(results[0][0])
                #return
            #If not found, try to find the URL in web_command table
            elif len(results) == 0:
                cursor.execute('SELECT url FROM web_command WHERE LOWER(name) = ?', (query,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening "+ query)
                    webbrowser.open(results[0][0])
                    #return
                else:
                    #If not found, try to open using os.system
                    speak("Opening "+ query)
                try:
                    os.system('start '+ query)
                except Exception as e:
                    speak(f"Unable to open {query}. Error: {str(e)}")
        except Exception as e:
            speak(f"Something went wrong: {str(e)}")




def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("please say the name of the song or video you want to play")

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None 

#find contacts
def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp','']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%'+ query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_no_str = str(results[0][0])
        if not mobile_no_str.startswith('+880'):
           mobile_no_str = '+880' + mobile_no_str
        
        return mobile_no_str, query
    except:
        speak('not exist in contacts')
        return 0, 0

def whatsapp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 13
        message = ''
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name
    
    elif flag == 'video call':
        target_tab = 6
        message = ''
        jarvis_message = "starting video call with "+name

    #Encoding the msg for url
    encoded_message = quote(message)
    print(encoded_message) #it was not here initially debug

    #Contruct the url
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    #Contract the full command
    full_command = f'start "" "{whatsapp_url}"'

    #Open whatsapp url with constracted url using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)

    pyautogui.hotkey('ctrl','f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')
    
    pyautogui.hotkey('enter')
    speak(jarvis_message)

#Chatbot message
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine/cookies_google.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response