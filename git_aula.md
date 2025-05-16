# Aula Git

### Instalar o Git no linux:
``sudo apt update;``
``sudo apt install git;``

**Passo a passo abrindo git**
 0. ``git config --global user.name "liamperfil";``
 0. ``git config --global user.email "jeancarlos.ramos@live.com";``
 1. ``git init``
 2. ``git add .``
 3. ``git commit -m "update";``
 4. ``git remote add origin link-do-repositório``
 5. ``git config --global credential.helper store``
 6. ``git push --set-upstream origin main``

**Para se comunicar com o repositorio de origem utilizasse pull ou push, quando solicitado login use seu email, quando solicitado a senha use o token.**
### Comandos básicos:
```bash
git status
git init # inicializar
git add .; # adicionar todos
git commit -m "mensagem de commit";
git pull; # puxar/atualizar local
git push; # empurrar/enviar
git push origin main; # empurrar na main
git push link-do-repositorio main; # empurrar na main
git branch; # listar branch
git checkout nome-da-branch; # mudar branch
git checkout -b "branch de origem" "nome da nova branch"; # criar nova branch
git merge "branch a receber merge"; # fazer merge puxando para a ativa
touch .gitignore;
git remote -v; # consultar remote
git remote add origin link-do-repositório
git push --set-upstream origin main # setando a branch
git clone link-do-repositório # clone repositório público
git clone https://seu_token@github.com/usuario/repositorio.git # clone repositório privado
```

**Se já estiver trabalhando em um repositório existente, altere a URL do repositório remoto usando:**
```
git remote set-url origin https://seu_token@github.com/seu_usuario/seu_repositorio.git
```
### Configure o Git para usar o token de acesso pessoal:
Isso fará com que o Git armazene suas credenciais em cache no arquivo .git-credentials do seu diretório home. Em seguida, você pode adicionar suas credenciais (seu nome de usuário do GitHub e o token de acesso pessoal) manualmente ao arquivo .git-credentials usando um editor de texto:
 1. git config --global credential.helper store
 2. em C:\Users\seu_usuario\.git-credentials https://seu_usuario:seu_token_de_acesso@github.com

### Crie um Personal Access Token:
1. Acesse o site do GitHub e faça login na sua conta.
2. Clique na sua foto de perfil no canto superior direito e selecione "Settings" (Configurações).
3. No menu lateral esquerdo, clique em "Developer settings" (Configurações de desenvolvedor), e em seguida, em "Personal access tokens" (Tokens de acesso pessoal).
4. Clique em "Generate new token" (Gerar novo token).
5. Dê um nome descritivo para o token, conceda as permissões necessárias e clique em "Generate token" (Gerar token).
6. Copie o token gerado. Ele será exibido apenas uma vez, então certifique-se de copiá-lo para algum lugar seguro.