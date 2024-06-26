# 1- navegador modo convidado em tela cheia como primeiro programa da barra: 1 estoque 2 nfe
# 2- prompt como segundo programa da barra
# 3- fazer a primeira vez manualmente para reconhecer o certificado antes de executar o programa

# https://docs.google.com/spreadsheets/d/1b2Nr-pdD6nDzkVTzLoq0l9YzGiykN4SCcIdT7X3Eerc/edit#gid=285781729
# https://www.nfe.fazenda.gov.br/

# C:\ambiente_virtual\Scripts\activate
# python C:\Users\jeanc\OneDrive\GitHub\aulas\pyautogui_baixar_nfe.py

import pyautogui
import time
pyautogui.PAUSE = 0.4

def rodar():
    pyautogui.hotkey('winleft', '1') #navegador
    i = 7
    while (i > 0):
        i -= 1
        pyautogui.hotkey('ctrlleft', '1') # aba 1 planilha
        pyautogui.press('down')
        pyautogui.hotkey('ctrlleft', 'c')
              
        pyautogui.hotkey('ctrlleft', '2') # aba 2 portal nfe
        pyautogui.press('tab', presses=37, interval=0.1)
        pyautogui.hotkey('ctrlleft', 'v') # formulario chave nfe
        
        pyautogui.press('tab', presses=2, interval=0.3)
        pyautogui.click(x=1035, y=506) # captcha
        pyautogui.click(x=1035, y=506) # captcha
        # pyautogui.press('enter', presses=3, interval=0.3) # captcha
        
        #pyautogui.press('tab')
        pyautogui.press('tab', presses=2, interval=0.3)
        time.sleep(0.6)
        pyautogui.press('enter') # continuar
        time.sleep(0.6)

        pyautogui.press('tab', presses=39, interval=0.1)
        time.sleep(0.6)
        pyautogui.press('enter') # download
        pyautogui.press('espace') # download
        time.sleep(3)
        
        pyautogui.press('enter') # dialogo alerta
        time.sleep(0.8)
        
        pyautogui.press('tab', presses=3, interval=0.2)
        pyautogui.press('enter') # dialogo salvar
        time.sleep(0.6)
        
        pyautogui.hotkey('shift', 'tab')
        time.sleep(0.6)
        pyautogui.hotkey('shift', 'tab')
        time.sleep(1)
        pyautogui.press('enter', presses=3, interval=0.3) # nova consulta
        time.sleep(2)

rodar()
pyautogui.hotkey('winleft', '2') #prompt
pyautogui.press('up')