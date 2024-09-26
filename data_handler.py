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
            "id", "color", "roll", "created_at", "updated_at", "status",
            "room_id", "total_red_eur_bet", "total_red_bets_placed",
            "total_white_eur_bet", "total_white_bets_placed",
            "total_black_eur_bet", "total_black_bets_placed"
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data.values())

def process_message(message):
    """Processa a mensagem recebida, extraindo e salvando os dados."""
    try:
        if message.startswith("42"):
            data = json.loads(message[2:])
        else:
            return

        if isinstance(data, list) and len(data) > 1 and data[0] == "data":
            payload = data[1].get("payload", {})
            filtered_data = {
                "id": payload.get("id"),
                "color": payload.get("color"),
                "roll": payload.get("roll"),
                "created_at": payload.get("created_at"),
                "updated_at": payload.get("updated_at"),
                "status": payload.get("status"),
                "room_id": payload.get("room_id"),
                "total_red_eur_bet": payload.get("total_red_eur_bet"),
                "total_red_bets_placed": payload.get("total_red_bets_placed"),
                "total_white_eur_bet": payload.get("total_white_eur_bet"),
                "total_white_bets_placed": payload.get("total_white_bets_placed"),
                "total_black_eur_bet": payload.get("total_black_eur_bet"),
                "total_black_bets_placed": payload.get("total_black_bets_placed"),
            }

            existing_data = load_existing_data()
            existing_data[filtered_data["id"]] = filtered_data
            save_data(existing_data)

    except json.JSONDecodeError:
        print("Erro ao decodificar JSON.")  # Adiciona um log de erro
