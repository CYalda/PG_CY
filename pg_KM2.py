import pyautogui as pg
import time

pg.hotkey('winleft','ctrl','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')
pg.typewrite('youtube\n',0.5)
time.sleep(3)
pg.hotkey('ctrl','t')
pg.typewrite('sephora.com\n',0.5)
pg.hotkey('ctrl','t')
pg.typewrite('images.google.com\n',0.5)
pg.hotkey('ctrl','t')
