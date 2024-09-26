import websocket
import json
from data_handler import process_message

def on_message(ws, message):
    process_message(message)

def on_error(ws, error):
    pass

def on_close(ws):
    pass

def on_open(ws):
    subscribe_message = "420" + json.dumps(["cmd", {
        "id": "subscribe",
        "payload": {
            "room": "double_room_1"
        }
    }])
    ws.send(subscribe_message)

def start_websocket():
    websocket_url = "wss://api-gaming.blaze1.space/replication/?EIO=3&transport=websocket"
    ws = websocket.WebSocketApp(websocket_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    while True:  # Manter o loop rodando
        ws.run_forever()
