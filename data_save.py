import requests
import time  # Certifique-se de que esta linha esteja presente
import json

def fetch_all_rolls():
    """Busca todos os valores de roll e seus minutos da API."""
    try:
        response = requests.get('https://blaze.com/api/singleplayer-originals/originals/roulette_games/recent/1')
        response.raise_for_status()  # Levanta um erro se a requisição falhar
        data = response.json()

        results = []
        for result in data:
            number = result['roll']
            created_at = result['created_at']
            minute = created_at.split(':')[1] if ':' in created_at else '00'  # Garante que o índice exista
            results.append({"number": number, "minute": minute})

        return results
    except Exception as e:
        return []  # Retorna lista vazia em caso de erro

def start_saving():
    """Inicia o loop para salvar dados em tempo real."""
    while True:
        all_rolls = fetch_all_rolls()
        data_to_save = {"results": all_rolls}

        with open('data.json', 'w') as json_file:  # Salva os dados em data.json
            json.dump(data_to_save, json_file, indent=4)  # Com indentação

        time.sleep(5)  # Espera 5 segundos antes da próxima atualização

if __name__ == "__main__":
    start_saving()
