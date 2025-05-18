# Aula Git

Este documento cobre os comandos e configurações básicas do Git.

## Configuração

1. **Definir nome de usuário:**
2. **Definir email:**
3. **Armazenar credenciais (opcional, use com cautela):**
4. **Inicializar um novo repositório:**
5. **Adicionar o repositório remoto (origin):**
```bash
git config --global user.name "seu_nome"
git config --global user.email "seu_email"
git config --global credential.helper store
git init
git remote add origin <link-do-repositório>
```

## Fluxo de Trabalho Básico

### Git Push (Enviar para o Repositório Remoto)

1. **Adicionar arquivos modificados à área de staging:**
2. **Criar um commit com uma mensagem descritiva:**
3. **Enviar o commit para o repositório remoto (e definir a branch upstream na primeira vez):**
```bash
git add . 
git commit -m "Mensagem descritiva da alteração"
git push --set-upstream origin main
```

### Git Pull (Receber Atualizações do Repositório Remoto)

1. **Receber as últimas alterações do repositório remoto (e definir a branch upstream na primeira vez):**
```bash
git pull --set-upstream origin main
```

**Nota:** Para interagir com o repositório remoto, use `git pull` para baixar as mudanças e `git push` para enviar suas alterações. Ao usar um token, ele será solicitado ou deverá ser incluído na URL.

## Comandos Básicos do Git

```bash
git --version  # Consultar a versão do Git
git help       # Exibir a ajuda do Git
git status     # Verificar o status do diretório de trabalho

git init       # Inicializar um novo repositório Git
git add .        # Adicionar todos os arquivos modificados
git commit -m "Mensagem" # Criar um novo commit com uma mensagem
git pull       # Baixar e mesclar as alterações do repositório remoto
git push       # Enviar as alterações para o repositório remoto
git remote add origin <link-do-repositório> # Adicionar um repositório remoto
git remote -v  # Listar os repositórios remotos

git push --set-upstream origin main # Enviar e configurar a branch upstream
git pull --set-upstream origin main # Baixar e configurar a branch upstream

git branch     # Listar as branches locais
git checkout <nome-da-branch> # Mudar para outra branch
git checkout -b <nome-da-nova-branch> # Criar e mudar para uma nova branch
git merge <branch-a-receber-merge>  # Mesclar uma branch na branch atual

touch .gitignore # Criar um arquivo .gitignore para ignorar arquivos

git clone <link-do-repositório> # Clonar um repositório público
git clone https://<seu_token>@[github.com/](https://github.com/)<usuario>/<repositorio>.git # Clonar um repositório privado

git config --global --unset user.name     # Remover nome de usuário da configuração global
git config --global --unset user.email    # Remover email da configuração global
git config --global --unset credential.helper # Remover o helper de credenciais global
git config --system --unset credential.helper # Remover o helper de credenciais do sistema
```

### Alterar a URL de um repositório remoto existente:
```bash
git remote set-url origin https://<seu_token>@[github.com/](https://github.com/)<seu_usuario>/<seu_repositorio>.git
```

## Configurando um Token de Acesso Pessoal (Personal Access Token - PAT) no GitHub

**Configurar o Git para usar o Token (Armazenamento em Cache - Use com cautela)**

### Configure o Git para usar o token de acesso pessoal:
Isso fará com que o Git armazene suas credenciais em cache no arquivo .git-credentials do seu diretório home. Em seguida, você pode adicionar suas credenciais (seu nome de usuário do GitHub e o token de acesso pessoal) manualmente ao arquivo .git-credentials usando um editor de texto:
1.  **Configurar o Git para armazenar as credenciais:**
    ```bash
    git config --global credential.helper store
    ```
2.  **Localização do arquivo de credenciais:** ``C:\Users\<seu_usuario>\.git-credentials``
3.  **Conteúdo do arquivo** ``.git-credentials`` **(CUIDADO: mantenha este arquivo seguro!):**
    ``https://<seu_usuario>:<seu_token_de_acesso>@github.com``

### Criar um Personal Access Token no GitHub
 1. Acesse o site do GitHub e faça login.
 2. Clique na foto de perfil (canto superior direito) e selecione **Settings**.
 3. No menu lateral esquerdo, clique em **Developer settings**, clique em **Personal access tokens**.
 4. Clique em **Generate new token**.
 5. Dê um nome ao token, selecione as permissões necessárias (geralmente ``repo`` para acesso completo ao repositório) e clique em **Generate token**.
 6. **Importante:** Copie o token gerado imediatamente e guarde-o em um lugar seguro. Você não poderá vê-lo novamente.