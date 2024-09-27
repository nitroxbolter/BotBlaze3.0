import threading
from monitoring import start_monitoring

if __name__ == "__main__":
    # Cria e inicia o thread para o monitoramento
    monitoring_thread = threading.Thread(target=start_monitoring)
    monitoring_thread.start()
