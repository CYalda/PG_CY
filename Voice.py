import win32com.client as wincl
import webbrowser as wb
import pyautogui as pg 

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your name")
answer = pg.prompt ("Enter your name.")

speak.Speak("Hello " + answer + "How was your day?")
day = pg.prompt("Enter how your day was.")

if day == "Good":
    speak.Speak("i am Happy to hear that!")

elif day == "Bad":
    speak.Speak("i am sorry to hear that")

else:
    speak.Speak("It was nice to meet you!")

speak.Speak("What kind of video would you like to watch??")
video = pg.prompt("Enter a video to watch")
speak.Speak("OK, you want to watch visdeos about" + video)

wb.open("https://www.youtube.com/results?search_query=" + video)
            
            
    

