from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_community.tools import ShellTool
from langchain.agents import AgentType, initialize_agent
import os
import openai

# carregar dependencias
shell_tool = ShellTool()
load_dotenv()

# Configurações da Azure OpenAI
AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME')
openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = "2023-05-15"
openai.api_key = AZURE_OPENAI_API_KEY

# LLM para Agente langchain
llm = AzureChatOpenAI(
    temperature=0,
    deployment_name="gpt-4o",
)

# Temporario - carregar doc
os.chdir("/doc_QA")
with open("QA_api.txt", "r", encoding="utf-8") as file:
    QA_DOCS = file.read()

# exemplo de cenario
os.chdir("/doc_QA")
with open("exemplo_cenario.txt", "r", encoding="utf-8") as file:
    exemplo_cenario = file.read()

# exemplo de relatorio
os.chdir("/doc_QA")
with open("exemplo_relatorio.txt", "r", encoding="utf-8") as file:
    exemplo_relatorio = file.read()

# prompt agente de cenario
os.chdir("/doc_QA")
with open("agente_QA_cenario_caderno.txt", "r", encoding="utf-8") as file:
    agente_QA_cenario = file.read()

# prompt agente de relatorio
os.chdir("/doc_QA")
with open("agente_QA_relatorio.txt", "r", encoding="utf-8") as file:
    agente_QA_relatorio = file.read()

# prompt agente de teste
os.chdir("/doc_QA")
with open("agente_QA_teste.txt", "r", encoding="utf-8") as file:
    agente_QA_teste = file.read()

# Agente de geração de cenários 
response = openai.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT_NAME,
    messages=[{"role": "system", "content": f"{agente_QA_cenario}\
               cade cenario deve seguir o seguinte exemplo de formatação:\n\n\n \
                {exemplo_cenario}"},
          {"role": "user", "content": f"gerar 7 cenarios de teste, Segue a documentação da API que deve ser gerada caderno de testes: {QA_DOCS}"}],
temperature=0
)

# Recebendo os cenarios de teste do agente de QA
cenarios = response.choices[0].message.content

# cortar cenarios e salvar em uma lista
cenarios = cenarios.split("----")
cenarios = [cenario for cenario in cenarios if cenario]

# Agente de testes da API
relatorio = []
for cenario in cenarios:
    shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace(
        "{", "{{").replace("}", "}}")

    self_ask_with_search = initialize_agent(
        [shell_tool], llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors=True)

    retorno = self_ask_with_search.run(
        f"{agente_QA_teste}\
        \n\n Segue cenário a ser testado:\
        {cenario}"
    )
    relatorio.append(retorno)

# Agente de geração de relatório
response_test = openai.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT_NAME,
    messages=[{"role": "system", "content": f"{agente_QA_relatorio}, seguem exemplo do relátorio:\
               \n\n {exemplo_relatorio}"},
          {"role": "user", "content": f"segue relatorio dos testes para analisar:\n\n {relatorio}"}],
temperature=0
)

print("Resultado analise:\n\n",response_test.choices[0].message.content)
