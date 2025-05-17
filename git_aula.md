# Aula Git

**Configuração**
 1. ``git config --global user.name "seu_nome";``
 2. ``git config --global user.email "seu_email";``
 3. ``git config --global credential.helper store``
 4. ``git init``
 5. ``git remote add origin link-do-repositório``

**Passo a passo abrindo git push/empurrando**
 1. ``git add .``
 2. ``git commit -m "update";``
 3. ``git push --set-upstream origin main``

**Passo a passo abrindo git pull/puxando**
 1. ``git pull --set-upstream origin main``

**Para comunicar com o repositorio de origem utilize pull/push, conforme necessidade, informe seu usuário para login, quando solicitado a senha informe o token.**

### Comandos básicos:
```bash
git -v # consultar git
git help
git status

git init # inicializar
git add . # adicionar todos
git commit -m "mensagem de commit"
git pull # puxar/atualizar local
git push # enviar/empurrar
git remote add origin link-do-repositório
git remote -v # consultar remote

git push --set-upstream origin main # enviar configurando a branch
git pull --set-upstream origin main # puxar configurando a branch

git branch # listar branch
git checkout nome-da-branch # mudar branch
git checkout -b "branch de origem" "nome da nova branch" # criar nova branch
git merge "branch a receber merge" # fazer merge puxando para a ativa

touch .gitignore

git clone link-do-repositório # clone repositório público
git clone https://seu_token@github.com/usuario/repositorio.git # clone repositório privado

git config --global --unset user.name
git config --global --unset user.email
git config --global --unset credential.helper
git config --system --unset credential.helper
```

**Se já estiver trabalhando em um repositório existente, altere a URL do repositório remoto usando:**
``git remote set-url origin https://seu_token@github.com/seu_usuario/seu_repositorio.git``

## Configurando token

### Configure o Git para usar o token de acesso pessoal:
Isso fará com que o Git armazene suas credenciais em cache no arquivo .git-credentials do seu diretório home. Em seguida, você pode adicionar suas credenciais (seu nome de usuário do GitHub e o token de acesso pessoal) manualmente ao arquivo .git-credentials usando um editor de texto:
 1. ``git config --global credential.helper store``
 2. Diretório do arquivo: C:\Users\seu_usuario\.git-credentials 
 3. Conteúdo do arquivo: https://seu_usuario:seu_token_de_acesso@github.com

### Crie um Personal Access Token:
 1. Acesse o site do GitHub e faça login na sua conta.
 2. Clique na sua foto de perfil no canto superior direito e selecione "Settings" (Configurações).
 3. No menu lateral esquerdo, clique em "Developer settings" (Configurações de desenvolvedor), e em seguida, em "Personal access tokens" (Tokens de acesso pessoal).
 4. Clique em "Generate new token" (Gerar novo token).
 5. Dê um nome descritivo para o token, conceda as permissões necessárias e clique em "Generate token" (Gerar token).
 6. Copie o token gerado. Ele será exibido apenas uma vez, então certifique-se de copiá-lo para algum lugar seguro.