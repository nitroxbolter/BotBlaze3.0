import websocket
import json
import os
import csv

# Função para carregar os dados existentes do arquivo CSV
def load_existing_data():
    if os.path.exists('dados.csv'):
        with open('dados.csv', 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            return {row['id']: row for row in reader}
    return {}

# Função para salvar os dados no arquivo CSV
def save_data(data):
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

def on_message(ws, message):
    # Remover print de mensagem recebida
    try:
        # Tente decodificar a mensagem como JSON
        if message.startswith("42"):  # Verifique se a mensagem começa com "42"
            data = json.loads(message[2:])  # Remova os dois primeiros caracteres
        else:
            return  # Retornar se a mensagem não for do formato esperado

        # Verificar se a mensagem é do tipo que queremos processar
        if isinstance(data, list) and len(data) > 1 and data[0] == "data":
            payload = data[1].get("payload", {})
            # Filtrando os dados que você realmente precisa
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

            # Carregar os dados existentes
            existing_data = load_existing_data()

            # Atualizar ou adicionar os dados
            existing_data[filtered_data["id"]] = filtered_data

            # Salvar os dados atualizados
            save_data(existing_data)

            # Remover print de dados salvos
            # print("Dados filtrados salvos em 'dados.csv'")

    except json.JSONDecodeError as e:
        # Remover print de erro ao decodificar JSON
        # print("Erro ao decodificar JSON:", e)
        # print("Mensagem que causou o erro:", message)
        pass  # Opcionalmente, você pode tratar o erro de forma silenciosa

def on_error(ws, error):
    # Remover print de erro
    # print("Erro:", error)
    pass

def on_close(ws):
    # Remover print de conexão fechada
    # print("Conexão fechada")
    pass

def on_open(ws):
    # Enviar a mensagem de inscrição
    subscribe_message = "420" + json.dumps(["cmd", {
        "id": "subscribe",
        "payload": {
            "room": "double_room_1"
        }
    }])
    ws.send(subscribe_message)

if __name__ == "__main__":
    websocket_url = "wss://api-gaming.blaze1.space/replication/?EIO=3&transport=websocket"
    ws = websocket.WebSocketApp(websocket_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    while True:  # Manter o loop rodando
        ws.run_forever()
