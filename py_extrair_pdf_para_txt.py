import os
import fitz  # PyMuPDF

def extrair_texto_pdf(pdf_path):
    texto = ""
    try:
        with fitz.open(pdf_path) as doc:
            for pagina in doc:
                texto += pagina.get_text()
    except Exception as e:
        print(f"Erro ao processar {pdf_path}: {e}")
    return texto

def converter_pdfs_para_txt(diretorio):
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.lower().endswith(".pdf"):
            caminho_pdf = os.path.join(diretorio, nome_arquivo)
            texto = extrair_texto_pdf(caminho_pdf)
            if texto.strip():
                nome_txt = os.path.splitext(nome_arquivo)[0] + ".txt"
                caminho_txt = os.path.join(diretorio, nome_txt)
                with open(caminho_txt, "w", encoding="utf-8") as txt_file:
                    txt_file.write(texto)
                print(f"Texto extraído de '{nome_arquivo}' para '{nome_txt}'")
            else:
                print(f"Nenhum texto encontrado em '{nome_arquivo}'")

if __name__ == "__main__":
    pasta_alvo = "."  # Altere para outro caminho se necessário
    converter_pdfs_para_txt(pasta_alvo)
