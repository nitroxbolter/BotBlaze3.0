import threading
from monitoring import start_monitoring  # Importa a função para iniciar o monitoramento
from api import start_api  # Presumindo que você tenha uma função para iniciar a API

def main():
    # Inicia a thread para monitorar os sinais
    monitoring_thread = threading.Thread(target=start_monitoring)
    monitoring_thread.start()

    # Se houver uma API para ser iniciada, descomente a linha abaixo
    # api_thread = threading.Thread(target=start_api)
    # api_thread.start()

    # Se houver uma interface, inicie-a
    # run_interface()

if __name__ == "__main__":
    main()
