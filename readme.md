# API Test Automation

Este projeto é um testador de API que automatiza todo o processo de geração de cenários de teste, execução dos testes e geração de relatórios. Utiliza tecnologias como LangChain (agentes e ferramentas), OpenAI e outras bibliotecas para garantir a qualidade e funcionalidade das APIs.

## Tecnologias Utilizadas

- **LangChain**: Para criação de agentes e ferramentas que automatizam o processo de teste.
- **OpenAI**: Para geração de cenários de teste e relatórios utilizando modelos de linguagem.
- **dotenv**: Para carregar variáveis de ambiente.
- **ShellTool**: Ferramenta da langchain para executar comandos de terminal durante os testes.

## Estrutura do Projeto

- `app/main.py`: Script principal que orquestra todo o processo de teste.
- `doc_QA/`: Diretório contendo arquivos de configuração e exemplos para os agentes de QA.
- `.env`: Arquivo de configuração com as credenciais da API do Azure OpenAI.

## Como Iniciar a Aplicação

1. **Clone o repositório**:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2. **Instale as dependências**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure as variáveis de ambiente**:
    Preencha o arquivo  com suas credenciais do Azure OpenAI:
    ```env
    AZURE_OPENAI_ENDPOINT="COLE AQUI"
    OPENAI_API_VERSION="2024-02-15-preview"
    AZURE_OPENAI_API_KEY="COLE AQUI"
    AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4o"
    ```

4. **Execute o script principal**:
    ```sh
    streamlit run app/main.py
    ```

## Funcionamento

1. **Carregamento de Dependências**: O script carrega as dependências e configurações necessárias.
2. **Geração de Cenários de Teste**: Utiliza o modelo OpenAI para gerar cenários de teste baseados na documentação da API.
3. **Execução dos Testes**: Utiliza o  para executar os testes de API via comandos `curl`.
4. **Geração de Relatórios**: Analisa os resultados dos testes e gera um relatório detalhado.

## Licença

Este projeto está licenciado sob a MIT License.