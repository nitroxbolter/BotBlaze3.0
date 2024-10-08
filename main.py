print("=== Importando Módulos ===")
import threading
from monitoring import start_monitoring, stop_monitoring
import time
from data_save import start_saving
import gui  # Importa o arquivo gui.py

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
        
        print("=== Iniciando Interface ===")
        # Inicia a GUI
        gui.create_gui()
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
