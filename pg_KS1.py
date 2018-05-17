import pyautogui as pg
import time

pg.hotkey("winleft","ctrl","d")
pg.hotkey("winleft")
pg.typewrite("chrome\n",0.3)
pg.hotkey("winleft","up")
pg.typewrite("youtube.com\n")
time.sleep(3)
pg.hotkey("ctrl","t")
pg.typewrite("glossier.com\n",0.3)
             
