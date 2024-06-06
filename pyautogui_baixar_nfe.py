# 1- navegador modo convidado em tela cheia como primeiro programa da barra
# 2- prompt como segundo programa da barra
# 3- fazer a primeira vez manualmente para reconhecer o certificado antes de executar o programa

# https://docs.google.com/spreadsheets/d/1b2Nr-pdD6nDzkVTzLoq0l9YzGiykN4SCcIdT7X3Eerc/edit#gid=285781729
# https://www.nfe.fazenda.gov.br/

# C:\ambiente_virtual\Scripts\activate
# python C:\Users\jeanc\OneDrive\GitHub\aulas\pyautogui_baixar_nfe.py

# 2 tab enter
# 39 tab enter
# 2 shift tab enter

import pyautogui
import time
pyautogui.PAUSE = 0.4

def rodar():
    pyautogui.hotkey('winleft', '1') #navegador
    i = 22
    while (i > 0):
        i -= 1
        pyautogui.hotkey('ctrlleft', '1') # estoque/NF Ent
        pyautogui.press('down')
        pyautogui.hotkey('ctrlleft', 'c')
              
        pyautogui.hotkey('ctrlleft', '2') # nfe
        pyautogui.click(x=1040, y=441) # campo chave from pyautogui import position; print(position())
        pyautogui.hotkey('ctrlleft', 'v')
        pyautogui.click(x=1130, y=562) # continuar
        time.sleep(0.8)
        pyautogui.click(x=1137, y=406) # download
        pyautogui.click(x=1137, y=406) # download
        time.sleep(0.4)
        pyautogui.click(x=1195, y=231) # dialogo alerta
        pyautogui.press('enter')
        time.sleep(0.4)
        pyautogui.click(x=767, y=594) # dialogo salvar
        pyautogui.press('enter')
        time.sleep(0.4)
        pyautogui.click(x=872, y=407) #nova consulta 
        time.sleep(0.2)
        pyautogui.click(x=1036, y=501) #captcha
        pyautogui.click(x=1036, y=501) #captcha

rodar()
pyautogui.hotkey('winleft', '2') #prompt
pyautogui.press('up')
