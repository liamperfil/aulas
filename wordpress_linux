Apache 2
$ sudo apt install apache2
$ sudo systemctl status apache2

Php
$ sudo apt install php php-mysql
$ sudo apt install php myadmin
$ sudo apt install php-curl php-gd php-mbstring php-xml php-xmlrpc php-soap php-intl php-zip

$ sudo systemctl restart apache2

Crie um arquivo info.php, ele informa a versão php em forma de site,
essa é uma boa prática, apenas para confirmar o bom funcionamento do php
$ sudo nano /var/www/html/info.php

<?php
phpinfo();
?>

localhost/info.php

Crie uma database e defina usuário para o wordpres:
$ sudo mysql -u root -p
CREATE DATABASE wordpress;
CREATE USER 'wp_user'@'localhost' IDENTIFIED BY 'seu_password';
GRANT ALL ON wordpress_db.* TO 'wp_user'@'localhost' IDENTIFIED BY 'seu_password';
FLUSH PRIVILEGES;
EXIT;

Baixe o wordpress no diretório temporário, faça descompactação e copie
$ cd /tmp && sudo wget https://br.wordpress.org/latest-pt_BR.zip
$ sudo unzip latest-pt_BR.zip
$ sudo cp -R wordpress/* ../var/www/html/

Crie o diretório uploads
$ sudo mkdir /var/www/html/wp-content/uploads

Altere a propriedade, grupo e permissões do diretório
$ sudo chown -R www-data:www-data /var/www/html/
$ sudo chmod -R 755 /var/www/html/

Edite o arquivo de configuração do site (pode ser 000-default.conf, wordpress.conf ou outro, dependendo da sua configuração):
$ cd \ & cd /etc/apache2/sites-available
$ sudo nano /etc/apache2/sites-available/000-default.conf 

Atenção: substitua /var/www/html/ pelo caminho correto do seu diretório root.
Dentro do bloco <VirtualHost>, adicione:
<Directory /var/www/html/>
 AllowOverride All
</Directory>

Após editar salve e feche o arquivo (CTRL + O, Enter, CTRL + X).
Ativando o mod_rewrite e reiniciando o Apache

$ sudo a2enmod rewrite
$ sudo apache2ctl configtest

Se tudo estiver certo, o retorno será: Syntax OK
Reinicie o apache2
$ sudo systemctl restart apache2

No navegador acesse localhost e configure o wordpress
