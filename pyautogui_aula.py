import pyautogui
import time
pyautogui.PAUSE = 0.2 #

# https://pyautogui.readthedocs.io/en/latest/keyboard.html
# python position.py

import pyautogui
import time

print("Olá mundo!")

pyautogui.PAUSE = 2.5 # tempo antes de cada comando pyautogui
time.sleep(0.5) # tempo antes do proximo comando

pyautogui.hotkey('winleft', '1') # 
pyautogui.hotkey('ctrlleft', '1') #
pyautogui.hotkey('ctrlleft', 'v') #
 
pyautogui.press('right', presses=8) #
pyautogui.press('tab') #
pyautogui.press(['left', 'left', 'left']) #

pyautogui.write('Hello world!') #
pyautogui.write('Hello world!', interval=0.25) #

print(pyautogui.position())
pyautogui.click(x=68, y=100)
pyautogui.rightClick(x=68, y=100)
pyautogui.doubleClick(x=68, y=100)
pyautogui.click(x=1629, y=590, clicks=2, interval=0.25)
pyautogui.click(clicks=2, interval=0.25)
pyautogui.click(button='right', clicks=3, interval=0.25)

pyautogui.keyDown('shift')  # mantenha pressionada a tecla shift
pyautogui.press('left')     # pressione a tecla de seta para a esquerda
pyautogui.press('left')     # pressione a tecla de seta para a esquerda
pyautogui.press('left')     # pressione a tecla de seta para a esquerda
pyautogui.keyUp('shift')    # solte a tecla shift

with pyautogui.hold('shift'):
    pyautogui.press(['left', 'left', 'left'])
    
def repetir():
    i = 3
    while i > 0:
        i = i - 1
repetir()