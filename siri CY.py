import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.Spvoice")

r = sr.Recognizer()
with sr. Microphone()as source:
    speak.Speak("Hello Christian, What whould you like to search for?")
    print("Listening")
    audio = r.listen(source)
    print("Thinking...")

try:
    words = r.recognize_google(audio)
    speak.Speak("Ok Christian, let's look for " + r.recognize_google(audio) + " on Google.")
    wb.open("https://www.google.com/search?q=" + words)

except sire.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service;{0}".format(e))
    
    
