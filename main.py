import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init()
def speak(text):


    engine.say(text)
    engine.runAndWait()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 130)
    engine.setProperty('voice', voices[1 ].id)
def greet():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time < "12:00:00":
        speak("good morning ")
    elif "12:00:00" <= current_time < "18:00:00":
        speak("Good afternoon")
    else:
        speak("Good evening")
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:   bn
        speak("listening")
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        speak("recognizing")
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print(f"You: {query}")
        return query
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Sorry, I couldn't understand your request. Please try again.")
        return ""
def virtual_assistant():
    greet()
    speak("hello every one . i am gwen . an virtual assistant ")
    while True:
        query = listen().lower()
        if "wikipedia" in query:
            speak("Searching in wikipedia")
            query = query.replace("wikipedia", "")  # miran""
            result = wikipedia.summary(query, sentences=2, chars=0, auto_suggest=True, redirect=True)
            speak("According to wikipedia")
            speak(result)
            print(result)
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com")
        elif "open calender" in query:
            speak("opening calender")
            power = r"C:\Users\sabar\OneDrive\Desktop\Calculator - Shortcut.lnk"
            os.startfile(power)
        elif "open terminal" in query:
            speak("opening terminal")
            power = r"C:\Users\sabar\OneDrive\Desktop\Command Prompt.lnk"
            os.startfile(power)
        elif "open flipkart" in query:
            speak("opening flipkart")
            webbrowser.open("www.flipkart.com")
        elif "play vsb video" in query:
            speak("here you go")
            pywhatkit.playonyt("https://youtu.be/FOBzAL5xydo?feature=shared")
        elif "open paint" in query:
            speak("opening paint")
            power = r"C:\Users\sabar\OneDrive\Desktop\Paint - Shortcut.lnk"
            os.startfile(power)
        elif "open notepad" in query:
            speak("opening query")
            power = r"C:\Users\sabar\OneDrive\Desktop\Notepad - Shortcut.lnk"
            os.startfile(power)
        elif "open edge" in query:
            speak("opening edge")
            power = r"C:\Users\Public\Desktop\Microsoft Edge.lnk"
            os.startfile(power)
        elif "open store" in query:
            speak("opening microsoft store")
            power = r"C:\Users\sabar\OneDrive\Desktop\Microsoft Store - Shortcut.lnk"
            os.startfile(power)
        elif "open mail" in query:
            speak("opening mail")
            power = r"C:\Users\AS US\Desktop\Mail.lnk"
            os.startfile(power)
        elif "open calculator" in query:
            speak("opening calculator")
            power = r"C:\Users\sabar\OneDrive\Desktop\Calculator - Shortcut.lnk"
            os.startfile(power)
        elif "open google" in query:
            speak("opening google")
            webbrowser.open("https://www.google.com")
        elif "open whatsapp" in query:
            speak("opening whatsapp")
            power = r"C:\Users\sabar\OneDrive\Desktop\WhatsApp Beta - Shortcut.lnk"
            os.startfile(power)
        elif "play music" in query:
            music_dir = r"C:\Users\sabar\Music\Badass-MassTamilan.dev.mp3"
            os.startfile(music_dir)
        elif 'wikipedia' in query:
            speak('opening Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "where are you now" in query:
            speak("iam in vsb enginnering college i   t lab 1")
        elif 'open stack overflow' in query:
            speak("opening stack overflow")
            webbrowser.open("www.stackoverflow.com")
        elif "what is the configuration of this laptop" in query:
            speak("this is hp personal laptop")
        elif 'open music' in query:
            speak("Here you go with music")
            codePath = r"C:\Users\sabar\OneDrive\Desktop\Media Player - Shortcut.lnk"
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")
        elif 'open chrome' in query:
            speak("opening chrome")
            codePath = r"C:\Users\Public\Desktop\Google Chrome.lnk"
            os.startfile(codePath)
        elif "open amazon" in query:
            speak("opening amazon")
            webbrowser.open("www.amazon.com")
        elif "open shop c" in query:
            speak("opening shopsy")
            webbrowser.open("www.shopsy.in")
        elif "open meesho" in query:
            speak("opening shopsy")
            webbrowser.open("www.meesho.in")
        elif "open impress" in query:
            speak("opening v s b e c impress")
            webbrowser.open("http://login.vsbec.com")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
        elif "what's your name" in query or "What is your name" in query:
            speak("My name is gwen")
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by students of i   t department in VSB engineering college")
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)
        elif "which is your favourite place in world" in query:
            speak("my favourite place is your device")
        elif "why you came to world" in query:
            speak("i came to the world in order to assist humans ")
        elif 'open blender' in query:
            speak("opening blender")
            power = r"C:\Users\ASUS\Desktop\Blender 3.5.lnk"
            os.startfile(power)
        elif "open video editor" in query:
            speak("opening editor")
            power = r"C:\Users\ASUS\Desktop\Clipchamp – Video Editor.lnk"
            os.startfile(power)
        elif "open photoshop" in query:
            speak("opening photoshop")
            power = r"C:\Users\sabar\OneDrive\Desktop\Adobe Photoshop 2022.lnk"
            os.startfile(codePath)
        elif "open files" in query:
            speak("opening files")
            codePath = r"C:\Users\ASUS"
            os.startfile(codePath)
        elif "open euro trucks" in query:
            speak("opening euro trucks")
            codePath = r"C:\Users\ASUS\Desktop\eurotrucks2.exe - Shortcut.lnk"
            os.startfile(codePath)
        elif"where are you now" in query:
             speak(" i am in i t lab one in v s b engineering college . karur")
        elif "what is love" in query:
            speak("It is 7th sense that destroy all other senses")
        elif "who are you" in query:
            speak(" my name is gwen i am an virtual assistant ")
        elif "will you marry me" in query:
            speak("sorry i can't marry you beacause iam a virtual machine")
        elif "are you single" in query:
            speak("not at all iam in a relation ship with the internet")
        elif "in which language you were developed" in query:
            speak("i was created using python")
        elif "which application was used to develop you" in query:
            speak("i was developed in pycharm")
        elif 'what is the reason for you' in query:
            speak("I was created as a Minor project")
        elif "do you like me" in query:
            speak("yes i like everyone who use me")
        elif "who is our chief guest now" in query:
            speak("respected chairman sir is our chief guest now")
        elif "which is your favourite place in the world" in query:
            speak("my favourite place is my users device")
        elif "which was the first programming language found in the world" in query:
            speak("FORTRAN is the first programming language found in the world")
        elif "when was fortran found" in query:
            speak("it was found in 1955")
        elif "who is the founder of vsb institutions" in query:
            speak("respected v s balusamy sir is the founder of vsb institutions")
        elif "when was c++ developed" in query:
            speak(" c++ was found in the year 1979")
        elif "when was python developed" in query:
            speak("python was found in 1991")
        elif "when was c sharp developed" in query:
            speak("it was developed in 2000")
        elif "who is the defence minister of India" in query:
            speak("India's defence minister is rajnath Singh")
        elif "who is the prime minister of India" in query:
            speak("the prime minister of India is Narendra Modi")
        elif "when was vsb institutions started" in query:
            speak("vsb institutions was started in the year 2000")
        elif "who is head of i t department" in query:
            speak("k . manivannan is the head of i  t department")
        elif 'exit' in query:
            speak("Thank you everybody for visiting our college on this wonderfull day")
            exit()
if __name__ == "__main__":
    virtual_assistant()