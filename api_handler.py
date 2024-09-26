import requests
import json

def fetch_api():
    try:
        req = requests.get('https://blaze.com/api/singleplayer-originals/originals/roulette_games/recent/1')
        req.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx e 5xx
        a = json.loads(req.content)
        jogo = [x['roll'] for x in a]
        return jogo
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return []  # Retorne uma lista vazia em caso de erro
