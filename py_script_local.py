# Este código abre o arquivo 'dados.py' em modo binário, lê todo o seu conteúdo,
# decodifica de bytes para string e executa o código Python contido nele usando a função exec().
with open(r'C:\Users\jeanc\OneDrive\Github\aulas\arquivo.py', 'rb') as resposta:
    conteudo_arquivo = resposta.read()
exec(conteudo_arquivo.decode())

# Uma forma mais eficiente é importar o módulo diretamente, se ele estiver no mesmo diretório:
import arquivo
# Agora você pode usar as funções e variáveis definidas no módulo 'arquivo.py'