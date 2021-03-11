
'''
       Created on 05-Mar-2021 @author: Omkar Jagdale
'''

import pyttsx3
from email.mime import audio
from pyttsx3.drivers import sapi5
from _datetime import datetime
import speech_recognition as sr
from idlelib.idle_test.test_colorizer import source
from chardet.metadata.languages import Language
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
print(voices[1].id)                   

engine.setProperty('voice', voices[1].id)   
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good morning omkar sir, have a great day, your jarvis")
    elif hour >= 12 and hour < 17 :
        speak("Good afternoon omkar sir, stay motivated, your jarvis")
    elif hour >= 18 and hour < 21 :
        speak("Good evening omkar sir, please have your tea, your jarvis")
    elif hour >= 22 and hour < 1 :
        speak("Good night omkar sir, sleep well, your jarvis")

def takeCommand():
    r = sr.Recognizer()         
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1   
        audio = r.listen(source)
        
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said : "+str(query))
    except Exception as e :
        #print(e)
        print("please say it again")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com', '******')
    server.sendmail('xyz@gmail.com', to, content)
    server.close()

if __name__ =="__main__":
    speak("Hello omkar sir, I am jarvis, how can i help you")
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print("searching wikipedia...")
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Omkar Jagdale\\Desktop\\songs'
            songs = os.listdir(music_dir)       
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))             
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak("sir, the time is "+str(strTime))
            
        elif 'email to omkar' in query:
            try:
                speak("sir please tell me what you want to send")
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendEmail(to, content)
                speak("sir, your mail has been sent")
            except Exception as e:
                #print(e)
                speak("sorry sir, you mail has not been delivered")
                print("sorry sir, you mail has not been delivered")
   
            
            