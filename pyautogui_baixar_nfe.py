# python pyautogui_baixar_nfe.py
# navegador como primeiro programa da barra
#   primeira aba do navegador planilha nf com foco na chave de acesso https://docs.google.com/spreadsheets/d/1b2Nr-pdD6nDzkVTzLoq0l9YzGiykN4SCcIdT7X3Eerc/edit#gid=285781729
#   segunda aba do navegador portal nfe com o captcha já marcado
# prompt como segundo programa da barra
# ATENÇÃO fazer a primeira vez manualmente para reconhecer o certificado

import pyautogui
import time
pyautogui.PAUSE = 0.5

def rodar():
    i = 1 #número de repetição
    pyautogui.hotkey('winleft', '1') #navegador
    while (i > 0):
        i -= 1;
        pyautogui.hotkey('ctrlleft', '1') #estoque/NF Ent
        pyautogui.press('down')
        pyautogui.hotkey('ctrlleft', 'c')
              
        pyautogui.hotkey('ctrlleft', '2') #nfe
        pyautogui.click(x=1061, y=475) #campo chave
        pyautogui.hotkey('ctrlleft', 'v')
        pyautogui.click(x=1129, y=598) #continuar
        time.sleep(2.3)
        pyautogui.click(x=1137, y=441) #download
        pyautogui.click(x=1137, y=441) #download
        time.sleep(0.4)
        pyautogui.click(x=1351, y=248) #alerta
        time.sleep(0.4)
        pyautogui.click(x=872, y=441) #nova consulta 
        time.sleep(0.2)
        pyautogui.click(x=1036, y=538) #captcha
        pyautogui.click(x=1036, y=538) #captcha

rodar()
pyautogui.hotkey('winleft', '2') #prompt
pyautogui.press('up')
