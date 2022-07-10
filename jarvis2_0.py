# ******** IMPORTING LIBRARIES ***************
import subprocess  # get system subprocess details like, shutdown, sleep. comes built-in.
import wolframalpha # compute expert-level answers [pip install wolframalpha]
import pyttsx3  # conversion of text to speech, works offline.[pip install pyttsx3]
import tkinter  # for building GUI, built-in
import json   
import random  # for generating any random no.
import operator
import speech_recognition as sr # recognizes the voice cmnd [pip install SpeechRecognition]
import datetime  # getting the current time,data {built-in}
import wikipedia # information from wikipedia [pip install wikipedia]
import webbrowser # perform web searches {built-in}
import os
import winshell
import pyjokes # jokes over internet [pip install pyjokes]
import feedparser
import smtplib
import ctypes
import time
import requests # make GET and POST request[pip install requests]
import shutil #provides function of high-level operations on files/collection of files: copying and removal of files,directories.
from twilio.rest import client # making calls and messages [pip install twilio]
from clint.textui import progress
from ecapture import ecapture as ec # capture image from camera, [pip install ecapture]
from bs4 import BeautifulSoup  # to scrap information from web pages, [ pip install beautifulsoup4]
import win32com.client as wincl
from urllib.request import urlopen


# **********************************************

# setting our engine to Pyttsx3, used for text --> speech.
# sapi5 is a microsoft speech application platform interface.

engine = pyttsx3.init('sapi5')
voice  = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # 0 -> male. 1->female.

# ******

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wishing according to the daytime hour.
def wishMe():
    hour = int(datatime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>18 and hour<20:
        speak("Good Evening Sir!")
    else:
        speek("Good Night Sir, Have Sweet dreams!")

# taking user name
def username():  
    speak("what should i call you sir")
    user_name = takeCommand()
    speak("welome" + user_name) 
    terminal_size = shutil.get_terminal_size() 
    print("############".center(terminal_size))
    print("welcome. ", user_name(terminal_size))
    print("############".center(terminal_size))

    speak("How can i help you, sir!")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("Reconginzing....")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        print(e)
        print("Unable to recognize your voice.")
        # speak
        return "None"
    
    return query # returning the string formate of the speech of the user.


# ************* SENDING EMIL **** SMTP SERVER-simple mail transfer protocol***

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587) # modern mail servers use 587 port for secure submission of email for delivery.
    server.ehlo()
    server.starttls()

    server.login('your mail id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close() 
    """ Close the connection to the SMTP server """

# *********MAIN FUNCTION*************

if __name__ == '__main__':
    clear = lambda:os.system('cls') #clean previous commands
    clear()
    wishMe()
    username()

    while True:
        query = takeCommand().lower() #stores all the commands said by the user.

        if 'wikipedia' in query:
            speak('searcing wikipedia...')
            query = query.replace("wikipeida","")
            results = wikipedia.summary(query, sentences = 3) #only first 3 sentences.
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak('here you go to youtube\n')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google\n')
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            speak('opening stack overflow')
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query or "play song" in query:
            speak('Please wait few seconds, playing music')
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            print(songs) #lists all the songs in the folder/file
            random = os.startfile(os.path.join(music_dir,songs[1])) #random song played

        elif 'the time' in query:
            strtTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtTime}")

        elif 'email to raushan' in query:
            try:
                speak("what should i say to him?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("i am unable to send the mail right now!")
        
        elif 'send a mail' in query:
            try:
                speak('what should i say?')
                content = takeCommand()
                speak("whome should i send the mail")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("i am unable to send the email right now!")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'calculate' in query: 
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx +1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("the answer is " + answer)
            speak("the answer is " + answer)
        
        elif 'search' in query or 'play' in query:
            query = query.replace("search","")
            query = query.replace("play","")
            webbrowser.open(query)
        
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfow(20,0,"location of wallpaper",0)
            speak("desktop background changed successfully")
        
# ***** code to read news ***
 
# ***************************
        elif 'shutdown system' in query:
            speak('hold a second! shutting down')
            subprocess.call('shutdown /p /f')
        elif 'lock window' in query:
            speak("locking the device!")
            ctypes.windll.user32.LockWorkStation()

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("user asked to locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/"+location +"")

        elif 'camera' in query or "take a photo" in query:
            ec.capture(0,"jarvis camera","img.jpg")




 


        elif 'exit' in query:
            speak('thanks for giving me your time, good bye!')
            exit()
        



