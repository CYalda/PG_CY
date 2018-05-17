import pyautogui as pg
import time
import webbrowser

points = 0

#Question 1

answer = pg.prompt(
"""
Where would rather go

a) Tiltied Towers
b) Dusty Depot 
c) Loot Lake 
d) Greasy Grove
"""
    )

# Give points

if answer == "a": 
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4 

#Question 2

answer = pg.prompt(
"""
What would you choose first:

a) Big Slurp 
b) Shiled potion 
c) Mini Shields
d) Trap 
"""
    )

# Give points

if answer == "a": 
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

#Question 3

answer = pg.prompt(
"""
Whats your weapon of choice:

a) Sniper Rifle
b) SCAR
c) Assult Rifle
d) Revolver
"""
    )

# Give points

if answer == "a": 
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4


# END OF SURVEY

pg. alert ("You are a...")

# Expert
if points >= 7:
    pg.alert("Expert Skilled Fortnite Payer")
    webbrowser.open("https://royalebattlebucks.com/wp-content/uploads/2017/12/Win-in-Fortnite-Battle-Royale.jpg")

# Medium
elif points <=7 and points <10:
    pg.alert("Medium Skilled Fornite Player")
    webbrowser.open("http://cdn.gamer-network.net/2017/usgamer/Fortnite-Battle-Royale-Shot-01.jpg")

# Noob
elif points >=10:
    pg.alert("Noob skilled Fornite Player")
    webbrowser.open("https://i.ytimg.com/vi/TiLjPg27plQ/maxresdefault.jpg")


    










    


