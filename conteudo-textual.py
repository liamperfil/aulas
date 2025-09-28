import requests
from bs4 import BeautifulSoup

def salvar_conteudo_site(url, nome_arquivo="conteudo_site.txt"):
    """
    Acessa uma URL, extrai o conteúdo textual e o salva em um arquivo de texto.

    Args:
        url (str): A URL do site a ser acessado.
        nome_arquivo (str, optional): O nome do arquivo para salvar o conteúdo.
                                      Padrão é "conteudo_site.txt".
    """
    try:
        # Faz a requisição HTTP para a URL
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins (4xx ou 5xx)

        # Usa BeautifulSoup para fazer o parsing do HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrai o texto visível da página
        # Remove tags de script e estilo para pegar apenas o conteúdo principal
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
        
        texto_limpo = soup.get_text(separator='\n', strip=True)

        # Salva o conteúdo em um arquivo .txt
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(texto_limpo)

        print(f"Conteúdo do site '{url}' salvo com sucesso em '{nome_arquivo}'")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # Exemplo de uso:
    url_do_site = "https://g1.globo.com/ba/bahia/noticia/2025/06/06/empresa-oferece-vagas-para-curso-gratuito-em-salvador.ghtml" #input("Por favor, digite a URL do site (ex: https://www.google.com): ")
    
    if url_do_site:
        salvar_conteudo_site(url_do_site)
    else:
        print("URL inválida. Por favor, forneça uma URL.")