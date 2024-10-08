import time
import threading
import os
import csv
import json

def load_existing_data():
    """Carrega dados existentes de um arquivo CSV."""
    if os.path.exists('dados.csv'):
        with open('dados.csv', 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            return {row['id']: row for row in reader}
    return {}

def save_data(data):
    """Salva os dados em um arquivo CSV."""
    with open('dados.csv', 'w', newline='') as csv_file:
        fieldnames = [
            "id", "color", "roll", "created_at", "updated_at", "status", "room_id",
            "total_red_eur_bet", "total_red_bets_placed", 
            "total_white_eur_bet", "total_white_bets_placed", 
            "total_black_eur_bet", "total_black_bets_placed"
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data.values())

def process_message(message):
    """Processa a mensagem recebida, extraindo e salvando os dados."""
    try:
        # Filtrar mensagens de controle
        if not message.startswith("42"):
            return  # Ignora mensagens não relevantes

        # A mensagem de dados começa com "42" e é seguida por um JSON
        data = message[2:]  # Remove o prefixo "42"
        data = json.loads(data.replace('""', '"'))  # Corrige as aspas duplas

        # Verificando se a estrutura da mensagem é válida
        if isinstance(data, list) and len(data) > 1 and data[0] == "data":
            payload = data[1]  # Pega o payload da mensagem

            # Verifica se o payload é um dicionário e tem a estrutura correta
            if isinstance(payload, dict) and 'data' in payload:
                game_data = payload['data']

                # Cria um dicionário para armazenar os dados
                processed_data = []

                for entry in game_data:
                    # Crie um dicionário com os dados que você deseja salvar
                    filtered_data = {
                        "id": entry.get("id"),
                        "color": entry.get("color"),
                        "roll": entry.get("roll"),
                        "created_at": entry.get("created_at"),
                        "updated_at": entry.get("updated_at"),
                        "status": entry.get("status"),
                        "room_id": entry.get("room_id"),
                        "total_red_eur_bet": entry.get("total_red_eur_bet"),
                        "total_red_bets_placed": entry.get("total_red_bets_placed"),
                        "total_white_eur_bet": entry.get("total_white_eur_bet"),
                        "total_white_bets_placed": entry.get("total_white_bets_placed"),
                        "total_black_eur_bet": entry.get("total_black_eur_bet"),
                        "total_black_bets_placed": entry.get("total_black_bets_placed"),
                    }
                    
                    # Adiciona os dados filtrados à lista
                    processed_data.append(filtered_data)

                existing_data = load_existing_data()
                # Adiciona novos dados ao existente, evitando duplicatas
                for item in processed_data:
                    if item["id"] not in existing_data:
                        existing_data[item["id"]] = item
                save_data(existing_data)  # Salva os dados atualizados

    except json.JSONDecodeError:
        pass  # Ignora erros de decodificação JSON

def start_saving():
    while True:
        time.sleep(10)  # Altere o intervalo conforme necessário
        existing_data = load_existing_data()
        save_data(existing_data)

# Iniciar o thread para salvar dados
if __name__ == "__main__":
    threading.Thread(target=start_saving, daemon=True).start()
