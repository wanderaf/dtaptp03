import streamlit as st
from agent import create_agent

st.title("Agente Inteligente - Câmara dos Deputados")

query = st.text_input("Digite uma palavra-chave:")
date_start = st.date_input("Data de início")
date_end = st.date_input("Data de fim")
text_to_summarize = st.text_area("Texto para resumo (opcional):")

if st.button("Pesquisar"):
    inputs = {}
    if text_to_summarize:
        inputs = {"text": text_to_summarize}
    elif query:
        inputs = {
            "keyword": query,
            "date_start": date_start.strftime("%Y-%m-%d") if date_start else None,
            "date_end": date_end.strftime("%Y-%m-%d") if date_end else None
        }

    try:
        agent = create_agent()
        st.write("Executando agente...")
        result = agent.invoke({"input": inputs})
        st.json(result)
    except Exception as e:
        st.error(f"Erro: {e}")