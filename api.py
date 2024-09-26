import websocket
import json
from data_handler import process_message

def on_message(ws, message):
    """Callback para mensagens recebidas."""
    process_message(message)

def on_error(ws, error):
    """Callback para erros."""
    print(f"Erro: {error}")  # Log de erro

def on_close(ws):
    """Callback para fechamento da conexão."""
    print("Conexão fechada")  # Log de fechamento
    # Aqui você pode adicionar lógica para tentar reconectar

def on_open(ws):
    """Callback para conexão aberta."""
    subscribe_message = "420" + json.dumps(["cmd", {
        "id": "subscribe",
        "payload": {
            "room": "double_room_1"
        }
    }])
    ws.send(subscribe_message)
    print("Inscrito na sala: double_room_1")  # Log de inscrição

def start_websocket():
    """Inicia a conexão websocket e mantém o loop rodando."""
    websocket_url = "wss://api-gaming.blaze1.space/replication/?EIO=3&transport=websocket"
    ws = websocket.WebSocketApp(websocket_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    while True:  # Manter o loop rodando
        ws.run_forever()
