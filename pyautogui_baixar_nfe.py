# 1- navegador modo ANONIMO, tela cheia, como primeiro programa da barra: aba 1 estoque, aba 2 nfe
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
    i = 40
    while (i > 0):
        print(i)
        i -= 1
        pyautogui.hotkey('ctrlleft', '1') # aba 1 planilha
        pyautogui.press('down')
        pyautogui.hotkey('ctrlleft', 'c')
              
        pyautogui.hotkey('ctrlleft', '2') # aba 2 portal nfe
        
        pyautogui.click(x=1078, y=470)
        pyautogui.hotkey('ctrlleft', 'v') # formulario chave nfe
        
        pyautogui.press('tab', presses=5, interval=0.04)
        pyautogui.press('enter') # continuar
        time.sleep(2)

        pyautogui.press('tab', presses=39, interval=0.08)
        
        # bloco de depuração
        # pyautogui.hotkey('winleft', '2') #prompt
        # input("Tudo certo até aqui? Pressione ENTER")
        # pyautogui.hotkey('winleft', '1') #navegador
        
        time.sleep(1)
        pyautogui.press('enter') # download
        pyautogui.press('espace') # download
        time.sleep(1.5)
        
        pyautogui.press('enter') # dialogo alerta
        time.sleep(1.5)
        
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.press('enter', presses=3, interval=0.3) # nova consulta
        time.sleep(1)

        pyautogui.click(x=1033, y=530)
        pyautogui.click(x=1033, y=530)

rodar()
pyautogui.hotkey('winleft', '2') #prompt
pyautogui.press('up')
