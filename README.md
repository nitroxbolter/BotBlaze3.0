# BotBlaze3.0


Este projeto é um bot para análise de dados da Blaze, que monitora resultados e identifica padrões, lançando sinais com base nas informações recebidas. O bot é modular e organizado em diferentes arquivos para facilitar a manutenção e o desenvolvimento.

## Estrutura do Projeto

blaze_bot/ 
├── main.py # Ponto de entrada do bot, inicia a execução do programa. 
├── api.py # Gerencia a conexão com a API e o WebSocket para receber dados. 
├── data_handler.py # Trata os dados recebidos e salva em um arquivo CSV. 
├── monitoramento.py # Monitora os dados e lança sinais com base nas análises. 
├── bot_handler.py # Responsável pela gestão e envio dos sinais identificados. 
├── patterns.py # Define e gerencia os padrões de análise a serem utilizados. 
├── config.py # Armazena configurações e parâmetros do bot. 
└── interface.py # Contém toda a interface de interação do programa.

## Descrição dos Arquivos

- **`main.py`**: Arquivo principal que inicia a execução do bot, chamando os módulos necessários.
  
- **`api.py`**: Este módulo estabelece a conexão WebSocket e gerencia as mensagens recebidas da API, chamando o `data_handler` para processar os dados.

- **`data_handler.py`**: Lida com a carga e salvamento dos dados em um arquivo CSV. Processa as mensagens recebidas e extrai as informações relevantes.

- **`monitoramento.py`**: Monitora os dados recebidos, identifica tendências e padrões, e gera sinais com base nas análises realizadas.

- **`bot_handler.py`**: Responsável pela gestão dos sinais identificados, enviando notificações ou mensagens conforme necessário.

- **`patterns.py`**: Define os padrões que o bot deve observar e analisar, permitindo identificar combinações relevantes nos dados.

- **`config.py`**: Contém as configurações do bot, como parâmetros de conexão, opções de análise e outros ajustes que podem ser modificados conforme necessário.

- **`interface.py`**: Gerencia a interface de interação do programa, permitindo a interação do usuário e a visualização de resultados e sinais.

## Como Executar

1. Clone o repositório para sua máquina local.
2. Instale as dependências necessárias (caso haja).
3. Execute o arquivo `main.py` para iniciar o bot:

```bash
python main.py

