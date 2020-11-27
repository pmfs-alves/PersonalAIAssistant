import speech_recognition as speechr #speech recognition
import pyttsx3      #text to speech library
import wikipedia # for fast wikipedia search
import ecapture         #to get some images
import time             #time display
import datetime         #for datetime manipulations
import os               # to interact with OS
import webbrowser       #for web connection
import subprocess       #processing system commands
import json             #to manipulate json files
import request          #for http requests
import wolframalpha    #an API from Wolfram to compute expert-level answers
import json             #storing and retrieving preconfigured text strings
import random

#setting up speech engine

engine = pyttsx3.init('sapi5') #sapi5 is a text to speech engine from MS
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')  # 0 for male voice, 1 for female

#Getting behaviour speech
with open("Phrases.json", 'r') as f:
    textdict: dict = json.load(f)


def speak(text):
    """
    gets texts and outputs as speach. Blocks new requests while pending requests not completed.
    """
    print(text)
    engine.say(text)
    engine.runAndWait()


def give_answer(type_answer, extra_beg="",extra_end=""):
    """
    Selects a random phrase from a given set
    Prints it and speaks it
    :return:
    """
    my_answer = random.choice(textdict[type_answer])
    speak(extra_beg, my_answer,extra_end)

def greetings():
    """
    Checks time of day and greets accordingly
    """
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour <12:
        greeting= "Hello, Good Morning"
    elif hour >= 12 and hour <18:
        greeting= "Hello, Good Afternoon"
    else:
        greeting= "Hello, Good Evening"
    speak("Small_greet", extra_end=greeting)


def accept_command():
    """
    Listen for a human voice command using google voice recognition
    :return: str  "None" if no command was perceived
    """
    recorder = speechr.Recognizer()
    with speechr.Microfone() as source:
        print("Waiting Command...")
        speak ("Waiting Command")
        audio= recorder.listen(source)

        try:
            statement= recorder.recognize_google(audio,language = " en-us")
            print("Your Command was: ", statement)

        except:
            speak(give_answer("Repeat"))
            return "None"
        return statement


####
#Skills on the assistant



def youtube_opener(statement):
    statement = statement.replace("youtube","")
    speak("".join(["Searhing Youtube for ", statement]))
    webbrowser.open_new_tab("".join([
        "https://www.youtube.com/results?search_query=",
        statement]))
    time.sleep(5)

#Setting skills selector dictionary and list of commands
dispatch: dict = {
    "youtube": youtube_opener,
    "wikipedia": self.strategy_random,
    }

commands: list =dispatch.keys()

#use skill dispatcher
def skills_selection(statement):
    no_command_found: bool=True
    for word in statement:
        if word in commands:
            dispatch[statement]()
            command_found = False
            break
    if no_command_found:
        speak(give_answer("No_command"))


if __name__=='__main__':

    print("Loading Assistant")
    greetings()
    while True:
        speak("How can i help you?")
        statement = accept_command().lower()
        if statement == "None":
            speak("Sorry, could not understand the command. Could you repeat?")
            continue

        else:
            commands =[dispatch.keys()]()
            for word in statement:


#TODO: command to add more phrases

#TDOD: adapt with a language model
