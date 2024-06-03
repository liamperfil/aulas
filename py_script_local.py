with open(r'C:\ambiente_virtual\senha.py', 'rb') as resposta:
    conteudo_arquivo = resposta.read()

exec(conteudo_arquivo.decode())