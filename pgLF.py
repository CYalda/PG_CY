import pyautogui as pg
pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.1)
pg.hotkey('winleft','up')
pg.typewrite('supremenewyork.com/shop\n',0.3)
pg.moveTo(1359,116,0.3)
pg.dragTo(1354,285,0.3)
pg.moveto(366,448,0.3)
pg.click(366,488,0.4)