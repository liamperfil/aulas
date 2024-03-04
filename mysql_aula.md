### Nova senha modo de segurança

sudo systemctl stop mysql
sudo mysqld_safe --skip-grant-tables --skip-networking &
mysql -u root

USE mysql;
UPDATE user SET authentication_string=PASSWORD('Minhasenha10') WHERE User='root';
FLUSH PRIVILEGES;
EXIT;

### Instalação

sudo apt update
sudo apt install mysql-server

sudo systemctl start mysql
sudo mysql_secure_installation

### Status

sudo systemctl status mysql


### Start

sudo systemctl start mysql

### Conexão

sudo mysql -u root

mysql -u root -p

SHOW DATABASES;

quit;

### Criar super usuário
CREATE USER 'super_usuario'@'%' IDENTIFIED BY 'senha';
GRANT ALL PRIVILEGES ON *.* TO 'super_usuario'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

### Deletar usuário

DROP USER 'super_usuario'@'localhost';

### Criar database

CREATE DATABASE liamperfil;


### Stop

sudo killall mysqld

### Remove
sudo systemctl stop mysql
sudo apt purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*
sudo rm -rf /etc/mysql /var/lib/mysql /var/log/mysql
sudo rm -rf /var/run/mysqld
sudo apt autoremove
sudo apt autoclean


### usuario/senha
super_usuario
senha
phpmyadmin
senha
phpmyadmin@localhost
root2

