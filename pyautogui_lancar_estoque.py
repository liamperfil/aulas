# winleft1 -> chrome
# ctrlleft1 -> https://docs.google.com/spreadsheets/d/1b2Nr-pdD6nDzkVTzLoq0l9YzGiykN4SCcIdT7X3Eerc/edit#gid=285781729
# ctrlleft2 -> localhost

# C:\ambiente_virtual\Scripts\activate
# python C:\Users\jeanc\OneDrive\GitHub\aulas\pyautogui_lancar_estoque.py

# https://docs.google.com/spreadsheets/d/1b2Nr-pdD6nDzkVTzLoq0l9YzGiykN4SCcIdT7X3Eerc/edit#gid=285781729

import pyautogui
import time
pyautogui.PAUSE = 0.4

def rodar():
    i = 103
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
