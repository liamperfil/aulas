# Aula Git

### Instalar o Git:
```
sudo apt update;
sudo apt install git;
```
```
git config --global user.name "liamperfil";
git config --global user.email "jeancarlos.ramos@live.com";
```
### Git commit e up, enviar alterações para o GitHub:
```
git add .;
git commit -m "Sua mensagem de commit";
git push origin main;
```
### Atualizar os repositórios locais:
Navegue até seu repositório/diretório
```
git pull origin main
```
### Inicialize um repositório Git na pasta local
Se você ainda não iniciou um repositório Git na sua pasta local, faça isso usando o comando git init:
Navegue até seu repositório/diretório
```
git init
```
### Clonando repositório privado
```
git clone https://seu_token@github.com/seu_usuario/seu_repositorio.git
```
### Clonando repositório público
```
git clone https://github.com/seu_usuario/seu_repositorio.git
```
**Se já estiver trabalhando em um repositório existente, altere a URL do repositório remoto usando:**
```
git remote set-url origin https://seu_token@github.com/seu_usuario/seu_repositorio.git
```
### Obs
```
git remote add origin https://liamperfil:seu_token_de_acesso@github.com/liamperfil/seu_repositório
```
### Configure o Git para usar o token de acesso pessoal:
Isso fará com que o Git armazene suas credenciais em cache no arquivo .git-credentials do seu diretório home. Em seguida, você pode adicionar suas credenciais (seu nome de usuário do GitHub e o token de acesso pessoal) manualmente ao arquivo .git-credentials usando um editor de texto:
```
git config --global credential.helper store
```
https://seu_usuario:seu_token_de_acesso@github.com
### Crie um Personal Access Token:
1. Acesse o site do GitHub e faça login na sua conta.
2. Clique na sua foto de perfil no canto superior direito e selecione "Settings" (Configurações).
3. No menu lateral esquerdo, clique em "Developer settings" (Configurações de desenvolvedor), e em seguida, em "Personal access tokens" (Tokens de acesso pessoal).
4. Clique em "Generate new token" (Gerar novo token).
5. Dê um nome descritivo para o token, conceda as permissões necessárias e clique em "Generate token" (Gerar token).
6. Copie o token gerado. Ele será exibido apenas uma vez, então certifique-se de copiá-lo para algum lugar seguro.