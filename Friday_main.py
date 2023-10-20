import calendar
import datetime
import os
import pyautogui
import pyjokes
import random
import time
import webbrowser
import geocoder
import keyboard
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from datetime import date
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)


def GoogleMaps(place):
    Url_Place = "https://www.google.com/maps/place/" + str(place)
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place, addressdetails=True)
    target_latlon = location.latitude, location.longitude
    location = location.raw['address']
    target = {'city': location.get('city', ''), 'state': location.get('state', ''),
              'country': location.get('country', '')}
    current_loca = geocoder.ip('me')
    current_location = current_loca.latlng
    distance = str(great_circle(current_location, target_latlon))
    distance = str(distance.split(' ', 1)[0])
    distance = round(float(distance), 2)
    webbrowser.open(url=Url_Place)

    speak(target)
    speak(f"Sir, {place} is {distance} kilometers away from Location. ")


def music():
    music_dir = "C:\\Music"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir, rd))


def Temp(where):
    search = "temperature in" + str(where)
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"current{search} is {temp}")


def Weather(where):
    search = "weather in" + str(where)
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"current{search} is {temp}")


def YouTube():
    speak("Opening Youtube")
    webbrowser.open("www.youtube.com")


def YoutubeAuto():
    speak("what's your command ?")
    comm = takecommand()

    if 'pause' in comm:
        keyboard.press('space bar')
    elif 'restart' in comm:
        keyboard.press('o')
    elif 'mute' in comm:
        keyboard.press('m')
    elif 'skip' in comm:
        keyboard.press('i')
    elif 'back' in comm:
        keyboard.press('j')
    elif 'full screen' in comm:
        keyboard.press('f')
    elif 'film mode' in comm:
        keyboard.press('t')
        speak("done sir!")


def google():
    speak("What should i search on google, Sir")
    qn = takecommand().lower()
    webbrowser.open(f"https://www.google.com/search?q={qn}")


def wiki():
    speak("What do you want to search on wikipedia")
    qn = takecommand().lower()
    result = wikipedia.summary(qn, sentences=2)
    speak(f"According to wikipedia{result}")
    print(result)


def play_yt():
    speak("What video do you want to play")
    name = takecommand()
    speak("Playing" + name)
    pywhatkit.playonyt(name)


def whats_up():
    speak("Enter the number")
    no = input("Enter the number:")
    speak("Tell me the message")
    msg = takecommand()
    speak("Please specify the time")
    hour = int(input("Enter the hour"))
    min = int(input("Enter the minutes"))
    pywhatkit.sendwhatmsg(no, msg, hour, min)


def close_notepad():
    speak("Closing notepad")
    os.system("taskkill /f /im notepad.exe")


def notepad():
    speak("Opening Notepad")
    path = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2302.26.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad"
    os.startfile(path)


def cmd():
    speak("opening Command Prompt")
    os.system("start cmd")


def takecommand():
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=2, phrase_time_limit=5)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except:
        speak("Say that again Please")

    return query


def day():
    d = date.today()
    x = calendar.day_name[d.weekday()]
    speak(f"Today is {x}")


def ip_address():
    ip = requests.get("https://api.ipify.org").text
    speak(f"Your ip address is {ip}")


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I %M %p")

    if 0 <= hour <= 12:
        a = "Good Morning Sir, Good Morning"
        speak(random.choice(a) + "It's " + tt)
    elif 12 <= hour < 18:
        a = "Good Afternoon Sir, Good Afternoon"
        speak(random.choice(a) + "It's " + tt)
    else:
        a = "Good Evening Sir, Good Evening"
        speak(random.choice(a) + "It's " + tt)

    b = "How may i help you Sir", "give me a command Sir", "Online and ready Sir"
    speak("I am Friday " + random.choice(b))


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        if "open notepad" in query:
            notepad()
        elif "hello" in query:
            speak("hello sir")
        elif "how are you" in query:
            speak("i am great, What about you, sir!")
        elif "open cmd" in query:
            cmd()
        elif "close notepad" in query:
            close_notepad()
        elif "bye" in query:
            speak("okay bye, sir!")
            break
        elif "ip address" in query:
            ip_address()
        elif "play music" in query:
            music()
        elif "google search" in query:
            speak("this is what i found for your search sir!")
            query = query.replace("friday", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak("done sir!")
        elif "open youtube" in query:
            YouTube()
        elif "website" in query:
            speak("ok sir, launching....")
            query = query.replace("friday", "")
            query = query.replace("website", "")
            web1 = query.replace("open", "")
            web2 = "https://www." + web1 + ".com"
            webbrowser.open(web2)
            speak("launched")
        elif "launch" in query:
            speak("Tell the name of the website")
            name = takecommand()
            web = "https://www." + name + ".com"
            webbrowser.open(web)
            speak("done sir!")
        elif "open google" in query:
            google()
        elif "search on wikipedia" in query:
            wiki()
        elif "play on youtube" in query:
            play_yt()
        elif "set alarm" in query:
            speak("Enter the time! ")
            time = input(": Enter the time :")
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("time to wake up sir!")
                    playsound("Oneplus_Ringtone_Remix(256k).mp3")
                    speak("Alarm closed")
                elif now > time:
                    break
        elif "send message" in query:
            whats_up()
        elif "screenshot" in query:
            kk = pyautogui.screenshot()
            kk.save("C:\\")
        elif "where is" in query:
            place = query.replace("where is ", "")
            place = place.replace("friday", "")
            GoogleMaps(place)
        elif "temperature in" in query:
            where = query.replace("temperature in", "")
            where = where.replace("friday", "")
            Temp(where)
        elif "what is the day today" or "day":
            day()
        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('o')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('i')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'film mode' in query:
            keyboard.press('t')
        elif 'youtube tool' in query:
            YoutubeAuto()
        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)
        elif "repeat my word" in query:
            speak('speak sir')
            jj = takecommand()
            speak(f"you said : {jj}")
