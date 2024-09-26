import threading
from monitoring import start_monitoring  # Importa a função para iniciar o monitoramento
from api import fetch_api  # Importa a função que inicia a API (WebSocket ou similar)

def main():
    # Inicia a thread para monitorar os sinais
    monitoring_thread = threading.Thread(target=start_monitoring)
    monitoring_thread.start()

    # Inicia a thread para a API (se houver uma função para isso)
    api_thread = threading.Thread(target=fetch_api)  # Certifique-se de que fetch_api é a função correta
    api_thread.start()

    # Se houver uma interface, você pode descomentar e iniciar aqui
    # run_interface()

    # Aguarda que ambas as threads terminem (opcional)
    monitoring_thread.join()
    api_thread.join()

if __name__ == "__main__":
    main()
