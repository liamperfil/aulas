1. Instalação
 - sudo apt update
 - sudo apt install mysql-server
 - sudo systemctl start mysql
 - sudo mysql_secure_installation
2. Outros comandos
 - sudo systemctl status mysql
 - sudo systemctl start mysql
 - ``sudo '/opt/lampp/manager-linux-x64.run'`` xampp
 - sudo /opt/lampp/lampp start
 - sudo mysql -u root -p
 - sudo killall mysqld
 - sudo systemctl stop mysql
 - sudo apt purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*
 - sudo rm -rf /etc/mysql /var/lib/mysql /var/log/mysql
 - sudo rm -rf /var/run/mysqld
 - sudo apt autoremove
 - sudo apt autoclean
 - ``sudo mysql --socket=/opt/lampp/var/mysql/mysql.sock -u root -p`` Iniciar mysql no socket informado
 - sudo mysql --defaults-file=/opt/lampp/etc/my.cnf --socket=/opt/lampp/var/mysql/mysql.sock -u root -p
3. Apache2 iniciar, restarte, stop, disable, enable e status
 - sudo systemctl start apache2
 - sudo systemctl restart apache2
 - sudo systemctl stop apache2
 - sudo systemctl disable apache2
 - sudo systemctl enable apache2
 - sudo systemctl status apache2

### Criar super usuário
```sql
CREATE USER 'super_usuario'@'%' IDENTIFIED BY 'senha';
GRANT ALL PRIVILEGES ON *.* TO 'super_usuario'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

### Nova senha modo de segurança
 - sudo systemctl stop mysql
 - sudo mysqld_safe --skip-grant-tables --skip-networking &
 - mysql -u root
 - USE mysql;
 - UPDATE user SET authentication_string=PASSWORD('Minhasenha10') WHERE User='root';
 - FLUSH PRIVILEGES;
 - EXIT;