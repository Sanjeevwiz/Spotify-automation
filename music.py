import pyautogui as p
import time 
p.hotkey("Win")
p.write('spotify')
p.hotkey("enter")
time.sleep(2)
p.moveTo(45,124)
p.sleep(1)
p.click()
p.sleep(1)
p.write('wavy twin', interval=0.2)
p.hotkey("enter")
p.sleep(1)
p.doubleClick(530,238)

