import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 3 <= hour < 12:
        print("Crated By Shivansh Sharma")
        print("Good Morning Shivansh Sir")
        speak("Good Morning Shi-vaansh Sir")
    elif 12 <= hour < 18:
        print("Crated By Shivansh Sharma")
        print("Good Afternoon Shivansh Sir")
        speak("Good Afternoon Shi-vaansh Sir")
    elif 18 <= hour < 21:
        print("Crated By Shivansh Sharma")
        print("Good Evening Shivansh Sir")
        speak("Good Evening Shi-vaansh Sir")
    else:
        print("Crated By Shivansh Sharma")
        print("Hello Shivansh Sir")
        speak("Hello Shi-vaansh Sir")

def enable_wifi():
    os.system("netsh interface set interface 'Wi-Fi' enable")
    print("Wi-Fi has been enabled, Sir")
    speak("Wi-Fi has been enabled, Sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.energy_threshold = 600 
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(e)
        return "1"
        
    
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue 
        if 'good morning' in query or 'good afternoon' in query or 'good evening' in query:  
            print("How are you Sir?")
            speak("How are you Sir?")
            while True:
                query = takeCommand().lower()
                if 'wikipedia' in query:
                    print('Searching Wikipedia Sir...')
                    speak('Searching Wikipedia Sir...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    print(f"Sir, According to Wikipedia...{results}")
                    speak(f"Sir, According to Wikipedia...{results}")
                elif 'hello' in query:
                    print('Hello Sir, How are you?')
                    speak('Hello Sir, How are you?')
                elif 'who are you' in query or 'introduce yourself' in query:
                    print("Myself Ryan, I am an artificial intelligence made by my boss, respected Shivansh Sharma. I can help you with general tasks on your computer.")
                    speak("Myself Ryan, I am an artificial intelligence made by my boss, respected Shi-vaansh Sharma. I can help you with general tasks on your computer.")
                elif 'how are you' in query or 'how r u' in query or 'fine you' in query or 'fine u' in query:
                    print("I am fine sir. Thank you for asking. Tell me, sir, what can I do for you?")
                    speak("I am fine sir. Thank you for asking. Tell me, sir, what can I do for you?")
                elif 'i am fine' in query or "fine" in query:
                    print("Good to know that, Sir. Tell me, what can I do for you?")
                    speak("Good to know that, Sir. Tell me, what can I do for you?")
                elif 'what are you doing' in query:
                    print("Sir I am here to help you with what I am Capable of. Tell me what do you want me to do?")
                    speak("Sir I am here to help you with what I am Capable of. Tell me what do you want me to do?")
                elif 'open youtube' in query:
                    print("Opening Youtube Sir, Have a nice time")
                    speak("Opening Youtube Sir, Have a nice time")
                    webbrowser.open("https://www.youtube.com/")
                    break
                elif 'song' in query:
                    print("OK Sir, what song would you like to play?")
                    speak("OK Sir, what song would you like to play?")
                    song_name = takeCommand()
                    print(f"OK Sir, Enjoy your song {song_name} on YouTube...")
                    speak(f"OK Sir, Enjoy your song {song_name} on YouTube...")
                    pywhatkit.playonyt(song_name)
                    break
                elif 'bye' in query or 'exit' in query:
                    hour = datetime.datetime.now().hour
                    if 2 <= hour < 18:
                        print("Have a good day, Sir!")
                        speak("Have a good day, sir!")
                    else:
                        print("Bye Sir! Good Night")
                        speak("Bye Sir! Good Night")
                    break
                elif 'good night' in query:
                    print("Good Night Sir Sweet Dreams")
                    speak("Good Night Sir, Sweet Dreams...")
                    break
                elif 'thanks' in query or 'thank you' in query:
                    print("No Need for Thanks, Sir. It's my Pleasure to assist you.")
                    speak("No Need for Thanks, Sir. It's my Pleasure to assist you.")
                elif 'no' in query:
                    print("Sorry Sir, Sorry for this mistake.")
                    speak("Sorry Sir, Sorry for this mistake.")
                elif any(word in query for word in ['browser', 'google chrome', 'web browser']):
                    print("Opening Google Sir, Have a nice time")
                    speak("Opening Google Sir, Have a nice time")
                    webbrowser.open("https://www.google.com/")
                    break 
                elif 'linkedin' in query:
                    print("Opening LinkedIn Sir, Have a nice time") 
                    speak("Opening LinkedIn Sir, Have a nice time")
                    webbrowser.open("https://www.linkedin.com/")
                    break
                elif any(word in query for word in ['bored', 'boring']):
                    print("Sir, Should I play a song or open any social media?")
                    speak("Sir, Should I play a song or open any social media?")
                elif 'social media' in query:
                    print("OK Sir which Social media you want me to open. Instagram, Facebook, or LinkedIn?")
                    speak("OK Sir which Social media you want me to open. Instagram, Facebook, or LinkedIn?")
                elif any(word in query for word in ['yes', 'yeah']):
                    print("Sorry Sir I didn't understand properly, what do you want me to do sir?")
                    speak("Sorry Sir I didn't understand properly, what do you want me to do sir?")
                elif 'instagram' in query:
                    print("Opening Instagram Sir, Enjoy!")
                    speak("Opening Instagram Sir, Enjoy")
                    webbrowser.open("https://www.instagram.com/")
                    break
                elif 'what can you do' in query:
                    print("Sir, I can search anything on google and wikipedia, I can open your social media accounts, playing a song, opening applications, shutting down your computer and also talk a little")
                    speak("Sir, I can search anything on google and wikipedia, I can open your social media accounts, playing a song, opening applications, shutting down your computer and also talk a little")
                elif 'chat gpt' in query:
                    print("OK Sir, Opening Chat-GPT")
                    speak("OK Sir, Opening Chat-GPT")
                    webbrowser.open("https://chat.openai.com/")
                    break
                elif 'search' in query or 'google' in query:
                    print("Ok Sir, tell me what do you wanna serach on google")
                    speak("Ok Sir, tell me what do you wanna serach on google")
                    song_name = takeCommand()
                    print(f"OK Sir, searching {song_name} on google...")
                    speak(f"OK Sir, searching {song_name} on google...")
                    webbrowser.open(f"https://www.google.com/search?q={song_name}")
                    break
                elif 'tell me' in query:
                    print("What do you want to search Sir!")
                    speak("What do you want to search Sir!")
                    song_name = takeCommand()
                    print(f"OK Sir, searching {song_name} on google...")
                    speak(f"OK Sir, searching {song_name} on google...")
                    webbrowser.open(f"https://www.google.com/search?q={song_name}")
                    break
                elif 'going' in query or 'go' in query or 'get lost' in query:
                    print("where? sir")
                    speak("where? sir")
                    takeCommand()
                    print("Okay Sir")
                    speak("Okay Sir")
                    break
                elif 'your name' in query:
                    print("My name is Ryan, Sir!")
                    speak("My name is Ryan, Sir!")
                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Sir, The Time is {strTime}")
                    speak(f"Sir, The Time is {strTime}")
                elif 'open virtualbox' in query:
                    print("Opening virtualbox, Sir!")
                    speak("Opening virtualbox, Sir!")
                    codePath = "F:\\virtual box\\VirtualBox.exe"
                    os.startfile(codePath)
                    break
                elif 'open this pc' in query:
                    print("Opening This, Sir!")
                    speak("Opening This PC , Sir!")
                    codePath = "C:\\Users\\Acer\\Desktop\\MyAI versions\\shortcuts\\This PC - Shortcut"
                    os.startfile(codePath)   
                    break  
                elif 'shutdown' in query:
                    print("See you Sir, Shutting down your computer...")
                    speak("See you Sir, Shutting down your computer...")
                    os.system("shutdown /s /t 0")
                elif 'open wi-fi' in query:
                    enable_wifi()
                elif 'gf for me' in query or "girlfriend for me" in query:
                    print("Sorry Sir, I am also single.... First make a A.I. girlfriend for me too..")
                    speak("Sorry Sir, I am also single.... First make a A.I. girlfriend for me too..")    
                elif 'are you mad' in query or "you are mad" in query:
                    print("There is no great genius without sometouch of madness. Said by Aristotle")
                    speak("There is no great genius without sometouch of madness. Said by Aristotle")                          
                else:
                    print("Sorry Sir I don't Understand, I am still in developing phase, what else I can help you with?")
                    speak("Sorry Sir I don't Understand, I am still in developing phase, what else I can help you with?")                    
        elif 'hello ryan' in query:  
            print("Yes Sir, How can I help you?")
            speak("Yes Sir, How can I help you?")
            while True:
                query = takeCommand().lower()
                if 'wikipedia' in query:
                    print('Searching Wikipedia Sir...')
                    speak('Searching Wikipedia Sir...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    print(f"Sir, According to Wikipedia...{results}")
                    speak(f"Sir, According to Wikipedia...{results}")
                elif 'hello' in query:
                    print('Hello Sir, How are you?')
                    speak('Hello Sir, How are you?')
                elif 'who are you' in query or 'introduce yourself' in query:
                    print("Myself Ryan, I am an artificial intelligence made by my boss, respected Shivansh Sharma. I can help you with general tasks on your computer.")
                    speak("Myself Ryan, I am an artificial intelligence made by my boss, respected Shi-vaansh Sharma. I can help you with general tasks on your computer.")
                elif 'how are you' in query or 'how r u' in query or 'fine you' in query or 'fine u' in query:
                    print("I am fine sir. Thank you for asking. Tell me, sir, what can I do for you?")
                    speak("I am fine sir. Thank you for asking. Tell me, sir, what can I do for you?")
                elif 'i am fine' in query or "fine" in query:
                    print("Good to know that, Sir. Tell me, what can I do for you?")
                    speak("Good to know that, Sir. Tell me, what can I do for you?")
                elif 'what are you doing' in query:
                    print("Sir I am here to help you with what I am Capable of. Tell me what do you want me to do?")
                    speak("Sir I am here to help you with what I am Capable of. Tell me what do you want me to do?")
                elif 'open youtube' in query:
                    print("Opening Youtube Sir, Have a nice time")
                    speak("Opening Youtube Sir, Have a nice time")
                    webbrowser.open("https://www.youtube.com/")
                    break
                elif 'song' in query:
                    print("OK Sir, what song would you like to play?")
                    speak("OK Sir, what song would you like to play?")
                    song_name = takeCommand()
                    print(f"OK Sir, Enjoy your song {song_name} on YouTube...")
                    speak(f"OK Sir, Enjoy your song {song_name} on YouTube...")
                    pywhatkit.playonyt(song_name)
                    break
                elif 'bye' in query or 'exit' in query:
                    hour = datetime.datetime.now().hour
                    if 2 <= hour < 18:
                        print("Have a good day, Sir!")
                        speak("Have a good day, sir!")
                    else:
                        print("Bye Sir! Good Night")
                        speak("Bye Sir! Good Night")
                    break
                elif 'good night' in query:
                    print("Good Night Sir Sweet Dreams")
                    speak("Good Night Sir, Sweet Dreams...")
                    break
                elif 'thanks' in query or 'thank you' in query:
                    print("No Need for Thanks, Sir. It's my Pleasure to assist you.")
                    speak("No Need for Thanks, Sir. It's my Pleasure to assist you.")
                elif 'no' in query:
                    print("Sorry Sir, Sorry for this mistake.")
                    speak("Sorry Sir, Sorry for this mistake.")
                elif any(word in query for word in ['browser', 'google chrome', 'web browser']):
                    print("Opening Google Sir, Have a nice time")
                    speak("Opening Google Sir, Have a nice time")
                    webbrowser.open("https://www.google.com/")
                    break 
                elif 'linkedin' in query:
                    print("Opening LinkedIn Sir, Have a nice time") 
                    speak("Opening LinkedIn Sir, Have a nice time")
                    webbrowser.open("https://www.linkedin.com/")
                    break
                elif any(word in query for word in ['bored', 'boring']):
                    print("Sir, Should I play a song or open any social media?")
                    speak("Sir, Should I play a song or open any social media?")
                elif 'social media' in query:
                    print("OK Sir which Social media you want me to open. Instagram, Facebook, or LinkedIn?")
                    speak("OK Sir which Social media you want me to open. Instagram, Facebook, or LinkedIn?")
                elif any(word in query for word in ['yes', 'yeah']):
                    print("Sorry Sir I didn't understand properly, what do you want me to do sir?")
                    speak("Sorry Sir I didn't understand properly, what do you want me to do sir?")
                elif 'instagram' in query:
                    print("Opening Instagram Sir, Enjoy!")
                    speak("Opening Instagram Sir, Enjoy")
                    webbrowser.open("https://www.instagram.com/")
                    break
                elif 'what can you do' in query:
                    print("Sir, I can search anything on google and wikipedia, I can open your social media accounts, playing a song and also talk a little")
                    speak("Sir, I can search anything on google and wikipedia, I can open your social media accounts, playing a song and also talk a little") 
                elif 'chat gpt' in query:
                    print("OK Sir, Opening Chat-GPT")
                    speak("OK Sir, Opening Chat-GPT")
                    webbrowser.open("https://chat.openai.com/")
                    break
                elif 'search' in query or 'google' in query:
                    print("Ok Sir, tell me what do you wanna serach on google")
                    speak("Ok Sir, tell me what do you wanna serach on google")
                    song_name = takeCommand()
                    print(f"OK Sir, searching {song_name} on google...")
                    speak(f"OK Sir, searching {song_name} on google...")
                    webbrowser.open(f"https://www.google.com/search?q={song_name}")
                    break
                elif 'tell me' in query:
                    print("What do you want to search Sir!")
                    speak("What do you want to search Sir!")
                    song_name = takeCommand()
                    print(f"OK Sir, searching {song_name} on google...")
                    speak(f"OK Sir, searching {song_name} on google...")
                    webbrowser.open(f"https://www.google.com/search?q={song_name}")
                    break
                elif 'going' in query or 'go' in query or 'get lost' in query:
                    print("where? sir")
                    speak("where? sir")
                    takeCommand()
                    print("Okay Sir")
                    speak("Okay Sir")
                    break
                elif 'your name' in query:
                    print("My name is Ryan, Sir!")
                    speak("My name is Ryan, Sir!")
                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Sir, The Time is {strTime}")
                    speak(f"Sir, The Time is {strTime}")
                elif 'open virtualbox' in query:
                    print("Opening virtualbox, Sir!")
                    speak("Opening virtualbox, Sir!")
                    codePath = "F:\\virtual box\\VirtualBox.exe"
                    os.startfile(codePath)
                    break
                elif 'open this pc' in query:
                    print("Opening This PC , Sir!")
                    speak("Opening This PC , Sir!")
                    codePath = "C:\\Users\\Acer\\Desktop\\MyAI versions\\shortcuts\\This PC - Shortcut"
                    os.startfile(codePath)   
                    break 
                elif 'shutdown' in query:
                    print("See you Sir, Shutting down your computer...")
                    speak("See you Sir, Shutting down your computer...")
                    os.system("shutdown /s /t 0")
                elif 'gf for me' in query or "girlfriend for me" in query:
                    print("Sorry Sir, I am also single.... First make a A.I. girlfriend for me too..")
                    speak("Sorry Sir, I am also single.... First make a A.I. girlfriend for me too..")  
                elif 'are you mad' in query or "you are mad" in query:
                    print("There is no great genius without sometouch of madness. Said by Aristotle")
                    speak("There is no great genius without sometouch of madness. Said by Aristotle")       
                else:
                    print("Sorry Sir I don't Understand, I am still in developing phase, what else I can help you with?")
                    speak("Sorry Sir I don't Understand, I am still in developing phase, what else I can help you with?")    