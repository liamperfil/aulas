<!-- bat comandos básicos -->
net user Administrador /active:yes
@echo off <!-- os comandos nao aparecem no console -->
echo Bem-vindo ao meu arquivo Batch Script!
start <!-- iniciar algo ex: start index.htm -->
start "" "https://www.example.com" <!-- inicia um site -->
rem <!-- usado para comentar -->
pause
set /p nome=Digite seu nome: <!-- set setar variavel, /p entrada do usuario -->
%nome% <!-- usando a variavel -->

**script abre o console e solicita um comando ao usuario**
```bat
@echo off
echo Exemplo: python teste.py
set /p userCommand=Digite um comando: 
%userCommand%
pause
```

<!-- Apache /etc/apache2/sites-available/000-default.conf -->
DocumentRoot: /var/www/html

1. **bash comandos básicos**
   - dir
   - cd <!-- navegar -->
   - cd ..
   - pwd <!-- ver arquivos e pastas -->
   - dir <!-- ver arquivos e pastas -->
   - ls -a <!-- ver arquivos e pastas inclusive ocultos --> 
   - rm -rf meu_diretorio/ <!-- apagar diretório -->
   - mkdir <!-- criar diretório -->
   - clear <!-- limpar -->
   - ip a <!-- ip e info de redes -->
   - su - <!-- acessar super usuário -->
   - sudo apt update && sudo apt upgrade -y <!-- atualizar instalador -->
   - sudo apt install curl -y <!-- instalar o curl ip -->
   - sudo apt install zip -y
   - sudo apt install default-jdk <!-- java -->
   - curl ifconfig.me <!-- ip externo -->
   - unzip /home/group343071/pasta.zip -d /home/group343071/
   - mv <!-- mover ex: mv /home/group343071/GameServer_loop.sh /home/group343071/l2server/gameserver/ -->
   - ./ <!-- executar ex: ./Start_GameServer.sh -->
   - cat <!-- exibir conteúdo ex: cat teste.txt -->
   - nohup <!-- executar em segundo plano, ex: nohup ./Start_GameServer.sh -->
   - ls -l <!-- verificar se o script pode ser executado ex: ls -l ./Start_GameServer.sh -->
   - chmod +x LoginServer_loop.sh <!-- permitir que o script seja executado -->
   - dos2unix <!-- converter arquivo copiado de outro SO, Windows/DOS para o formato Unix/Linux (LF) -->
   - sudo nano <!-- abrir no nano editor, ex: sudo nano teste.txt -->
   - ps aux | grep bash <!-- scripts em execução -->
   - ps aux | grep GameServer_loop.sh <!-- verificar o processo -->
   - kill <PID> <!-- matar o processo -->
   - kill -9 <PID> <!-- forçar matar o processo -->
   - sudo reboot <!-- reiniciar imediatamente -->
   - sudo reboot -f <!-- forçar reinício (sem desligamento limpo) -->
   - sudo shutdown -r now <!-- reiniciar agora -->
   - sudo shutdown -r +5 <!-- shutdown em 5 minutos -->
   - sudo shutdown -h now <!-- desligar agora -->
   - sudo shutdown -h +10 <!-- desligar em 10 minutos -->
   - sudo shutdown -c <!-- cancelar um desligamento agendado -->
   - sudo shutdown -h 23:30 <!-- agendar desligamento às 23:30 -->
   - sudo poweroff <!-- desligar -->
   - sudo poweroff -f <!-- forçar o desligamento (caso o sistema esteja travado) -->
2. **ver processos**
   - ps aux | grep nohup
   - cat nohup.out
   - tail -f nohup.out
3. **ver processo especifico**
   - ps aux | grep LoginServer_loop.sh
   - ps aux | grep GameServer_loop.sh
4. **consultar uso da porta**
   - ss -tulnp | grep -E "2106|7777"
   - cd /home/group343071/.ssh/
5. **banco de dados**
   - sudo apt install mariadb-server -y
   - sudo systemctl status mariadb
   - sudo systemctl start mariadb
   - sudo systemctl restart mariadb
   - sudo systemctl enable mariadb
   - sudo mysql_secure_installation
   - sudo mysql -u root -p
   - GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'senha_root' WITH GRANT OPTION;
   - GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '' WITH GRANT OPTION;
   - SELECT User, Host FROM mysql.user;
   - show databases;
   - use database_name;
   - show tables;
   - SELECT NOW();

**alterar o fuso**
sudo mysql_tzinfo_to_sql /usr/share/zoneinfo | sudo mysql -u root mysql
sudo nano /etc/mysql/my.cnf
default-time-zone = 'America/Sao_Paulo'

**config para aceitar login externo 0.0.0.0 default 127.0.0.1**
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
bind-address = 0.0.0.0
sudo systemctl restart mariadb

**apache**
sudo apt install apache2
sudo systemctl start apache2
sudo systemctl status apache2

**php**
sudo apt install php php-mysql
sudo apt install phpmyadmin
sudo apt install php-curl php-gd php-mbstring php-xml php-xmlrpc php-soap php-intl php-zip
php -v

**habilitar**
sudo a2enconf phpmyadmin
**caso não exista, crie o arquivo phpmyadmin.conf**
sudo nano /etc/apache2/conf-available/phpmyadmin.conf
**dentro do arquivo contém:**
```php conf
Alias /phpmyadmin /usr/share/phpmyadmin

<Directory /usr/share/phpmyadmin>
    Options Indexes FollowSymLinks
    DirectoryIndex index.php
    AllowOverride All
    Require all granted
</Directory>

<Directory /usr/share/phpmyadmin/setup>
    Require all denied
</Directory>

# Protect the phpMyAdmin directory

<Directory /usr/share/phpmyadmin>
    <IfModule mod_authz_host.c>
        Require ip 127.0.0.1
        Require ip ::1
    </IfModule>
</Directory>
```

sudo systemctl restart apache2

- **atalhos nano**
   - Ctrl + Shift + 6 → Para iniciar a seleção.
   - Alt + A → Para iniciar a seleção.
   - Ctrl + V → Para ir rapidamente até o final do arquivo.
   - Ctrl + Y → Vai para o início do arquivo (página anterior).
   - Ctrl + K → Para cortar/deletar o conteúdo selecionado.
   - Alt + 6 → Para copiar
   - Ctrl + U → Para colar
   - Ctrl + X → Para sair
   - Ctrl + O → Para salvar/escrever
   - Ctrl + R → Para ler??
   - Ctrl + C → Para receber localização do cursor, ex: [ line  3/4 (75%), col  6/ 6 (100%), char 18/19 (94%) ]
   - Ctrl + T → Para executar

```bash
#!/bin/bash
dos2unix Start_LoginServer.sh Start_GameServer.sh
chmod +x Start_LoginServer.sh Start_GameServer.sh
cd gameserver
dos2unix GameServer_loop.sh
chmod +x GameServer_loop.sh
cd ../loginserver
dos2unix LoginServer_loop.sh
chmod +x LoginServer_loop.sh
cd ..
sudo ./Start_GameServer.sh
sudo ./Start_LoginServer.sh
echo "Servidores iniciados"
```

```bash
#!/bin/bash

#Verifica se dos2unix está instalado
if ! command -v dos2unix &> /dev/null; then
    echo "Erro: dos2unix não está instalado! Instale com: sudo apt install dos2unix"
    exit 1
fi

echo "Convertendo arquivos para formato Unix..."
dos2unix Start_LoginServer.sh Start_GameServer.sh

echo "Dando permissões de execução..."
chmod +x Start_LoginServer.sh Start_GameServer.sh

echo "Entrando no diretório gameserver..."
if cd gameserver; then
    dos2unix GameServer_loop.sh
    chmod +x GameServer_loop.sh
    cd ..
else
    echo "Erro: Diretório 'gameserver' não encontrado!"
    exit 1
fi

echo "Entrando no diretório loginserver..."
if cd loginserver; then
    dos2unix LoginServer_loop.sh
    chmod +x LoginServer_loop.sh
    cd ..
else
    echo "Erro: Diretório 'loginserver' não encontrado!"
    exit 1
fi

echo "Iniciando servidores..."
./Start_GameServer.sh
./Start_LoginServer.sh

echo "Servidores iniciados com sucesso!"
```

**inicia ambiente virtual e script**
```bat
@echo off
title BOT SERVER CONSOLE
:start
echo Bem vindo ao comprasnet bot server console
call venv\Scripts\activate && echo Aperte ENTER para iniciar
pause >nul && call python main.py
```

**exemplo: instalar modulos**
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
