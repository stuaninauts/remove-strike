import requests
from bs4 import BeautifulSoup
import streamlit as st

def baixar_html_e_limpar(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    resposta = requests.get(url, headers=headers, timeout=10)
    resposta.raise_for_status()
    soup = BeautifulSoup(resposta.text, "html.parser")
    for tag in soup.find_all("strike"):
        tag.decompose()
    return soup.prettify()

st.title("Remover coisa chata da pagina da lei chata")
st.image("./foto.png", width=200)

url = st.text_input("Insira a URL da página:")
nome_arquivo = st.text_input("Nome do arquivo de saída:", value="saida.html")

if st.button("Processar e baixar"):
    if url and nome_arquivo:
        try:
            html_limpo = baixar_html_e_limpar(url)
            st.success("Processamento concluído!")
            st.download_button(
                label="Baixar HTML limpo",
                data=html_limpo,
                file_name=nome_arquivo,
                mime="text/html"
            )
        except Exception as e:
            st.error(f"Erro: {e}")
    else:
        st.warning("Preencha todos os campos.")
