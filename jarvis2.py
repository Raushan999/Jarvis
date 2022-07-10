import pyttsx3 #pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser #inbuilt module for website.
import os
import smtplib
# import pyaudio 
# before installing pyaudio we need to install pipwin(pip install pipwin)
#  then -> pipwin install pyaudio

#module installed - pyttsx3,speechRecongnition (to take command),
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id) # the voice of male, [1]- for female.
engine.setProperty('voice', voices[0].id)

def speak(audio):  # fun 1, takes string and convert to audio, and say
    engine.say(audio)
    engine.runAndWait()

def wishMe(): #wish a/q dayhour #fun 2
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("how can i help you")  

def takeCommand():
    # it takes microphone input from the user and return string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening......")
        # r.pause_threshold = 1  
        # r.energy_threshold = 50 
        audio = r.listen(source)
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
        # query = r.recognize_google(audio, Language='en-in') # en-in = english india.
        print(f"User said: {query}\n")
    # except:
    #     print("sorry,could not recognize")
    except Exception as e:
        # print("say that again please...") 
        return "None" 
   
    return query 

# sending email to one person only.
def sendEmail(do,content): # (to whome, what to send)
    #  allow less secured app from the same email id from which u r sending mail.
    #  enforce access to less secure apps for all users.
    server = smtplib.SMTP('smtp.gmail.com',587) # smtplib is a package used to send mail using google.
    server.ehlo()
    server.starttls()
    server.login('raushanp414@gmail.com','raushan@1806')
    server.sendmail('raushanp414@gmail.com',to,content)
    server.close()

 # ''' doc string ''' #about the function.

if __name__ == "__main__":  # driver function(Main function).
    wishMe()
    takeCommand()
# #not wrorking ahead.

    while 1:  #(will go running multiple times)
    # if 1:
        query = takeCommand().lower() # for lower case to fit browser audio.
    #logic for executing task based on query.
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("Wikipedia","") #removing wikipedia string and searching the result
            results = wikipedia.summary(query, sentence = 2)
            speak("According to wikipedia")
            print(results)
            speak(results) 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\music' # // to escape the character.
            songs = os.listdir(music_dir) # lists the random songs from that directory.
            print(songs) # print the songs from that directory.
            os.startfile(os.path.join(music_dir,songs[0]))  #first song.
        #    ********** random music player *****************
       
        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code" # for opening the visual studio.
            os.startfile(codePath)

        elif 'tell time' in query: #time asked.
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        
        elif 'send email to roshan' in query: # to send email.
           # can send to multiple or differernt ppl by putting dictionary and accessing them.
            try:
                speak("what should i say?")
                content = takeCommand() # return a string of spoken sentence.
                to = "raushanp414@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e: # any error case
                # print(e)
                speak("sorry, i am not able to send email right now")
        
        elif 'quit' in query:
            exit()