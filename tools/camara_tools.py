import requests
import os
from langchain_openai import ChatOpenAI

def get_projetos_de_lei(inputs):
    keyword = inputs.get("keyword")
    date_start = inputs.get("date_start")
    date_end = inputs.get("date_end")

    if not keyword:
        return {"error": "A palavra-chave é obrigatória."}

    url = "https://dadosabertos.camara.leg.br/api/v2/proposicoes"
    params = {
        "keywords": keyword,
        "dataApresentacaoInicio": date_start,
        "dataApresentacaoFim": date_end,
        "ordem": "DESC",
        "ordenarPor": "ano"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"Erro na requisição: {str(e)}"}

def summarize_and_extract(inputs):
    text = inputs.get("text")
    if not text:
        return {"error": "Texto não fornecido para resumo."}

    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo",
        temperature=0
    )

    prompt = f"Resuma o seguinte texto e extraia palavras-chave:\n\n{text}"
    try:
        response = llm(prompt)
        return response.content
    except Exception as e:
        return {"error": f"Erro ao processar o texto: {str(e)}"}
