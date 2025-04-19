import speech_recognition as sr # pip install SpeechRecognition
import pyttsx3     # pip install pyttsx3
import webbrowser   # pip install webbrowser
import datetime      # pip install datetime
import requests   # pip install requests
import os         # pip install os-sys
import pyjokes      # pip install pyjokes
import random       # pip install random
import time         # pip install time
import subprocess   # pip install subprocess

def sptext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speechtx("Say that again please...")
        return "None"
    return query

#sptext()
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()
#speechtx("Hello Nicky, I am JARVIS. How can I help you?")    

if __name__ == "__main__":
    speechtx("Hello Sir, I am JARVIS. How can I help you?")
    while True:
        query = sptext().lower()
        if 'open youtube' in query:
            speechtx("Opening Youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speechtx("Opening Google")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speechtx("Opening StackOverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open facebook' in query:
            speechtx("Opening Facebook")
            webbrowser.open("facebook.com")
        elif 'open whatsapp' in query:
            speechtx("Opening Whatsapp")
            webbrowser.open("web.whatsapp.com")
        elif 'open instagram' in query:
            speechtx("Opening Instagram")
            webbrowser.open("instagram.com")
        elif 'open twitter' in query:
            speechtx("Opening Twitter")
            webbrowser.open("twitter.com")
        elif 'open linkedin' in query:
            speechtx("Opening LinkedIn")
            webbrowser.open("linkedin.com")
        elif 'open github' in query:
            speechtx("Opening Github")
            webbrowser.open("github.com")
        elif 'open code' in query:
            speechtx("Opening Visual Studio Code")
            codePath = "C:\\Users\\Nicky\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'play music' in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S%p") #("%I%M%p")
            speechtx(f"Sir, the time is {strTime}")
        elif 'open notepad' in query:
            speechtx("Opening Notepad")
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        elif 'open command prompt' in query:
            speechtx("Opening Command Prompt")
            subprocess.Popen('C:\\Windows\\System32\\cmd.exe')
        elif 'exit' in query:
            speechtx(f"Goodbye Sir, Have a nice day!") 
            break  
        elif 'hello' in query:
            speechtx(f"Hello Sir, How can I help you?") 
        elif 'how are you' in query:
            speechtx(f"I am fine, Thank you for asking. How can I help you?")
        elif 'warden' in query:
            speechtx(f"Warden MADARCHOD HAI, BEHENCHOD, BHOSDIKA LUND SALA") 
        elif 'jokes' in query:
            joke_1 = pyjokes.get_joke(language='en', category='neutral')
            speechtx(joke_1)
        elif 'search' in query:
            speechtx("What do you want me to search?")
            search = sptext()
            url = f"https://www.google.com/search?q={search}"
            webbrowser.open(url)
        else:
            speechtx("Sorry Sir, I didn't get that. Please say it again.")
            continue
    
    
    
    