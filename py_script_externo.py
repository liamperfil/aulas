import urllib.request

# URL do script externo
url_script = "https://raw.exemplo.com/exemplo.py"

# Baixar, ler e decodificar o conteúdo do script externo
with urllib.request.urlopen(url_script) as response:
    script_content = response.read().decode()

# Executar o conteúdo do script baixado
exec(script_content)