#winleft1 -> chrome
#ctrlleft1 -> planilha NF
#ctrlleft2 -> www localhost

import pyautogui
import time
pyautogui.PAUSE = 0.4


def rodar():
    i = 16
    pyautogui.hotkey('winleft', '1') #chrome
    while (i > 0):
        i = i - 1
        pyautogui.hotkey('ctrlleft', '1') # estoque/NF Ent
        pyautogui.press('down')
        pyautogui.hotkey('ctrlleft', 'c')
        pyautogui.hotkey('ctrlleft', '2') # www
        pyautogui.hotkey('ctrlleft', 'v')
        pyautogui.press('enter')
        
rodar()
pyautogui.hotkey('winleft', '2') #prompt
pyautogui.press('up')