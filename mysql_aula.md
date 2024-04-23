### Instalação
```s
sudo apt update
sudo apt install mysql-server
```
```s
sudo systemctl start mysql
```
```s
sudo mysql_secure_installation
```
### Status
```s
sudo systemctl status mysql
```
### Start
```s
sudo systemctl start mysql
```
### Start XAMPP
```s
sudo '/opt/lampp/manager-linux-x64.run'
```
### Conexão
```s
sudo mysql -u root
```
```s
mysql -u root -p
```
### Stop
```s
sudo killall mysqld
```
### Remove
```s
sudo systemctl stop mysql
```
```s
sudo apt purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*
```
```s
sudo rm -rf /etc/mysql /var/lib/mysql /var/log/mysql
```
```s
sudo rm -rf /var/run/mysqld
```
```s
sudo apt autoremove
```
```s
sudo apt autoclean
```
### Usuario/senha
super_usuario
senha
phpmyadmin
senha
phpmyadmin@localhost
root2

### Apache2 iniciar, restarte, stop, disable, enable e status
```s
sudo systemctl start apache2
```
```s
sudo systemctl restart apache2
```
```s
sudo systemctl stop apache2
```
```s
sudo systemctl disable apache2
```
```s
sudo systemctl enable apache2
```
```s
sudo systemctl status apache2
```
### Iniciar mysql no socket informado
```s
sudo mysql --socket=/opt/lampp/var/mysql/mysql.sock -u root -p
```
ou
```s
sudo mysql --defaults-file=/opt/lampp/etc/my.cnf --socket=/opt/lampp/var/mysql/mysql.sock -u root -p
```
### Iniciar o xampp
```s
sudo /opt/lampp/lampp start
```
### Criar super usuário
```sql
CREATE USER 'super_usuario'@'%' IDENTIFIED BY 'senha';
GRANT ALL PRIVILEGES ON *.* TO 'super_usuario'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```
### Deletar usuário
```sql
DROP USER 'super_usuario'@'localhost';
```
### Criar database
```sql
CREATE DATABASE liamperfil;
```
### Nova senha modo de segurança
```s
sudo systemctl stop mysql
```
```s
sudo mysqld_safe --skip-grant-tables --skip-networking &
```
```s
mysql -u root
```
```sql
USE mysql;
```
```sql
UPDATE user SET authentication_string=PASSWORD('Minhasenha10') WHERE User='root';
```
```sql
FLUSH PRIVILEGES;
```
```sql
EXIT;
```
```sql
SHOW DATABASES;
```
```s
quit;
```