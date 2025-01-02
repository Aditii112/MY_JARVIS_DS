
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import openai
import datetime
import cv2
import numpy
import subprocess
import os
import time
import random
import pyautogui
from openai import OpenAI
from config import apikey

chatstr=""
def chat(query):
    global chatstr
    print(chatstr)
    client = OpenAI(api_key=apikey)
    chatstr+= f"Aditi: {query}\n Jarvis: "


    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
# todo:Wrap this inside of a try catch block
    speak(response.choices[0].text)
    chatstr+= f"{response.choices[0].text}\n"
    return (response.choices[0].text)
    # with open(f"Openai/prompt- {random.randint(1,2456782)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('ai')[1:]).strip}.txt","w") as f:
        f.write(text)

def ai(prompt):
    client = OpenAI(api_key=apikey)
    text=f"OpenAI response for Prompt: {prompt} \n *************************************\n\n"
    # openai.api_key=apikey

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
# todo:Wrap this inside of a try catch block
    print(response.choices[0].text)
    text+= response.choices[0].text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    # with open(f"Openai/prompt- {random.randint(1,2456782)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('ai')[1:]).strip}.txt","w") as f:
        f.write(text)

def open_paint():
    try:
        os.system("start mspaint")
        print("Paint is now open.")
        time.sleep(2)  # Wait for Paint to open
        draw_circle()
    except Exception as e:
        print("An error occurred:", str(e))


def draw_circle():
    # Move the cursor to the center of the Paint window
    pyautogui.moveTo(500, 300, duration=1)

    # Click to start drawing
    pyautogui.mouseDown()
#
    # Draw a circle
    pyautogui.moveTo(600, 300, duration=1)
    pyautogui.moveTo(600, 400, duration=1)
    pyautogui.moveTo(500, 400, duration=1)
    pyautogui.moveTo(500, 300, duration=1)
    pyautogui.moveTo(550, 300, duration=1)
    pyautogui.mouseUp()

    print("Circle drawn successfully.")

#
# # Test the function
# open_paint()
#
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(" Good morning!")
    elif hour >= 12 and hour < 17:
        speak(" Good afternoon! ")
    else:
        speak("Good Evening! ")

    speak(" I am Jarvis A.I. Mam . Please tell me how may i help you .")


def takeCommand():
    #  It takes microphone input and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source: #with use for ending this command automatically
        print(" Listening... ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognize...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
        print(type(query))

    except Exception as e:
        print("Say that again please ...")
        # print(e)
        return "none"
    return query


def open_paint():
    try:
        os.system("start mspaint")
        print("Paint is now open.")
    except Exception as e:
        print("An error occurred:", str(e))

# Test the function

def open_notepad():
    try:
        os.system("start notepad")
        print("Notepad is now open.")
    except Exception as e:
        print("An error occurred:", str(e))

# Test the function

if __name__ == "__main__":
    # speak("Hi , This is Zira A.I.")
    wishme()

    while True:
          query = takeCommand()
          # print(type(str(query)))
          # query = str(query)
          # query_str = str(query.lower)
          sites = [["youtube", "https://www.youtube.com/"], ["wikipedia", "https://www.wikipedia.com"]
                   , ["google", "https://www.google.com/"]]
          for site in sites:
              if f"open {site[0]}".lower() in query.lower():
                  speak(f"Opening {site[0]} Mam...")
                  webbrowser.open(site[0])

          # if "open music" in query:
          if "the time" in query:
              strfTime = datetime.datetime.now().strftime("%H:%M:%S")
              speak(f"Mam, time is {strfTime}")

          # if "open vs code" in query:
          #     os.system("C:\Users\Aditi Gupta\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code")
          #     speak(f"opening vs code")

          if "open camera" in query.lower():
            video_0 = cv2.VideoCapture(0)
            while(True):
                  ret, frame0 = video_0.read()
                  cv2.imshow('frame',frame0)
                  if cv2.waitKey(1) & 0xFF==ord("a"):
                     break
            video_0.release()
            cv2.destroyAllWindows()
          if "Jarvis" in query.lower():
              print("Yes Sir")
              speak("yes sir")
          if "wikipedia" in query.lower():
            speak('Searching wikipedia mam ...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

          if "open paint" in query.lower():
              speak('Opening Paint mam..')
              open_paint()
          
          if "draw circle" in query.lower():
              draw_circle()

          if "open notepad" in query.lower():
              speak('Opening notepad mam...')
              open_notepad()
          if "Using ai".lower() in query.lower():
              ai(prompt=query)
          if "type" in query.lower():
              query=query.replace("type","")
              pyautogui.typewrite(f"{query}",0.1)
          else:
              chat(query)