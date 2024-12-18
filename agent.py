from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.memory import ConversationBufferMemory
from tools.camara_tools import get_projetos_de_lei, summarize_and_extract
import os

def create_agent():
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo",
        temperature=0
    )
    tools = [
        Tool(
            name="Get Projetos de Lei",
            func=get_projetos_de_lei,
            description="Consulta projetos de lei com palavras-chave e intervalo de datas."
        ),
        Tool(
            name="Resumo e Palavras-Chave",
            func=summarize_and_extract,
            description="Gera resumo e palavras-chave de textos fornecidos."
        )
    ]
    memory = ConversationBufferMemory(return_messages=True)
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        memory=memory,
        verbose=True
    )
    return agent
