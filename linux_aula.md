Atualizar o apt-get é uma boa pratica
```
sudo apt-get update
```
Instalar pip
```
sudo apt install python3-pip
```
Ambiente virtual em projeto python
```
sudo apt-get install python3-venv
```

Instalar programa .deb
```
sudo dpkg -i nome_do_arquivo.deb
```

Criar ambiente venv
```
python3 -m venv venv
```

Ativar ambiente venv
```
source venv/bin/activate
```

Desativar
```
deactivate
```

Executar um arquivo
```
xdg-open index.html
```

Mover diretorio
mv origem destino, exemplo:
```
sudo mv home/jean/Downloads/estoque /var/www/html
```

### Resetando a senha de seu usuário no WSL
1. Abra o PowerShell e verifique de qual a distribuição você quer resetar a senha
```
wsl -l # lista as distribuições instaladas
```
2. Acesse o usuário root da distribuição, por padrão o “root” é o principal
```
wsl -d distribution --user root
# exemplo: 
# wsl -d Ubuntu-20.04 --user root
```
3. Digite passwd seguido do nome do usuário que você deseja resetar a senha
```
passwd username
# exemplo:
# passwd exemploUser
```

### Java
```java
java -jar nome_do_arquivo.jar
```

### Configurando em aplicação desktop
Crie um arquivo .desktop, salve em /usr/share/applications/
Configure conforme sua necessidade, exemplo:
portablesigner.desktop
```
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=java -jar /snap/PortableSigner/PortableSigner.jar
Name=PortableSigner
Comment=Assinar documentos PDF
Icon=/snap/PortableSigner/icon2.png
```
Execute o seguinte
```
chmod +x portablesigner.desktop
```

### ativar super usuário
```
sudo su -
```