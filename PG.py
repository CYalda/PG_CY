import pyautogui as pg
import time 

pg. hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n','.5')
time.sleep(.5)
pg.hotkey('winleft','up')

pg.typewrite('supremenewyork.com\n','.2')
pg.moveTo(280,171,.2)
pg.click ()
pg.moveTo()


