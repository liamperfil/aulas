### Super admin
```bat
Net user administrador /active:no
```
cd .. cd nome_diretorio
### Iniciar site
```bat
@echo off
echo Bem-vindo ao meu arquivo Batch Script!
start "" "https://www.example.com"
rem pause
```
### Iniciar ambiente virtual e script
```bat
@echo off
title BOT SERVER CONSOLE
:start
echo Bem vindo ao comprasnet bot server console
call venv\Scripts\activate && echo Aperte ENTER para iniciar
pause >nul && call python main.py
```
### Instalar modulos
```bat
@echo off
echo Bem-vindo ao meu arquivo Batch Script!

choice /C YN /M "Deseja instalar o ambiente virtual? (Y/N)"
if errorlevel 2 (
    echo Você escolheu não instalar o ambiente virtual
) else (
    call python -m venv venv
)

choice /C YN /M "Deseja ativar ambiente virtual? (Y/N)"
if errorlevel 2 (
    echo Você escolheu não ativar o ambiente virtual
) else (
    call venv\Scripts\activate
)

choice /C YN /M "Deseja instalar o modulo selenium? (Y/N)"
if errorlevel 2 (
    echo Você escolheu não instalar o modulo selenium
) else (
    call pip install selenium
)

choice /C YN /M "Deseja instalar o modulo webdriver? (Y/N)"
if errorlevel 2 (
    echo Você escolheu não instalar o modulo webdriver
) else (
    call pip install webdriver-manager
)

choice /C YN /M "Deseja instalar o modulo chromedriver-binary? (Y/N)"
if errorlevel 2 (
    echo Você escolheu não instalar o modulo chromedriver-binary
) else (
    call pip install chromedriver-binary
)

choice /C YN /M "Deseja instalar o modulo chromedriver-binary? (Y/N)"
if errorlevel 2 (
    echo Você escolheu não instalar o modulo getpass
) else (
    call pip install getpass
)

pause
```
