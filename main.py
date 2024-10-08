print("=== Importando Módulos ===")
import threading
import time
from monitoring import start_monitoring, stop_monitoring
from data_handler import save_data, load_existing_data  # Se necessário
from data_handler import start_saving  # Importando a função start_saving
from api import fetch_api  # Importando a função fetch_api

def main():
    try:
        print("=== Iniciando monitoramento ===")
        # Cria uma thread para o monitoramento
        monitoring_thread = threading.Thread(target=start_monitoring)
        monitoring_thread.daemon = True  # Permite que o programa feche quando a thread principal termina
        monitoring_thread.start()
        print("Monitoramento iniciado")
        
        print("=== Iniciando save data ===")
        # Cria uma thread para salvar dados em tempo real
        saving_thread = threading.Thread(target=start_saving)
        saving_thread.daemon = True  # Permite que o programa feche quando a thread principal termina
        saving_thread.start()
        
        print("=== Iniciando conexão WebSocket ===")
        # Inicia a conexão WebSocket
        fetch_api()
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
