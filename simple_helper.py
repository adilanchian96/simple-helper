'''Simple AI module to take voice as input,
convert that input to text using google's
speech recognition API, and perform actions
based on that input. Created by Andrew Dilanchian'''


import speech_recognition as sr
import pyttsx3
import os

#--------------Initialize needed components--------------
def simple_helper():
    recognizer = sr.Recognizer()                                       #Google's speech recognizer
    engine = pyttsx3.init()                                            #text-to-speech engine
    engine.setProperty('volume',0.9)

    print("Say something")
    with sr.Microphone() as source:                                    #'Microphone()' captures the system's default mic
        audio = recognizer.listen(source)                              #puts an audio capture into 'audio'

    while recognizer.recognize_google(audio) != "stop":
        if recognizer.recognize_google(audio) == "Start Safari":       #translates that capture into text!
            engine.say("Starting Safari now.")
            engine.runAndWait()                                        #tells the TTS engine to say what it needs to
            os.system("open -a Safari")
        else:
            print("You said " + recognizer.recognize_google(audio))    #a simple way to see what you're actually saying
        with sr.Microphone() as source:
            print("Still listening...")                                #reprompt the user to say something
            audio = recognizer.listen(source)

simple_helper()