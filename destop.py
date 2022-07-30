import os
import smtplib
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import cv2
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   # os.startfile("C:\\Program Files\\Rainmeter\\Rainmeter.exe")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("I am ZIRA sir. Please tell me how may I help you")
def takeCommand():
    # It take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.starttls()
    server.ehlo()
    server.login('mayav7856@gmail.com', 'add password0')
    server.sendmail('mayav154@gmail.com', to, content)
    server.close()

    try:
        speak("what should i say sir?")
        content = takeCommand()
        to = "mayav75454@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent!")

    except Exception as e:
        print(e)
        speak("Sorry Dear ")


wishMe()
# speak("hii sir")

while True:
    query = takeCommand().lower()

    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=4)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open command prompt' in query:
        os.system("start cmd")

    elif 'open notepad' in query:
       npath = "C:\\WINDOWS\\system32\\notepad.exe"
       os.startfile(npath)


    elif 'open google' in query:
        speak("sir, what should i search on google")
        cm = takeCommand().lower()
        webbrowser.open(f"{cm}")

    elif 'open camera' in query:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)

        cap.release()
        cv2.destroyAllWindows()



    elif 'play music' in query:
        music_dir = 'D:\\Non Critical\\song\\Favorite Songa2'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.part.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
        speak(f"The facebook is open sir")

    elif 'open book' in query:
        npath = "C:\\Users\\mayav\\OneDrive\\Desktop"
        os.startfile(npath)

    elif 'open code' in query:
        codePath = "C:\\Users\\mayav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'no thank you' in query:
        speak("thanks for using me sir, have a good day")
        sys.exit()
    speak("sir do you have any other work")



