import threading
import time
import csv  # Importa a biblioteca CSV para salvar os dados
from bot_handler import send_message
from api import fetch_api
from patterns import check_patterns

# Definições de variáveis globais
analise_sinal = False
entrada = 0
max_gale = 2
check_resultado = []
win_count = 0
loss_count = 0
running = False
cor_sinal = None

def reset():
    global analise_sinal, entrada
    entrada = 0
    analise_sinal = False

def martingale():
    global entrada
    entrada += 1
    if entrada <= max_gale:
        send_message(f"⚠️ Gale {entrada} ⚠️")
    else:
        loss()
        reset()

def win():
    global win_count
    send_message("✅")
    win_count += 1

def loss():
    global loss_count
    send_message("❌")
    loss_count += 1

def enviar_sinal(cor, padrao):
    send_message(f'''
🚨 Sinal encontrado 🚨

⏯️ Padrão: {padrao}

💶 Entrar no {cor}

🦾 Proteger no ⚪️

🐓 2 martingale: (opcional)''')

def correcao(results, color):
    if results[0:1] == ['P'] and color == '⚫️':
        win()
        reset()
    elif results[0:1] == ['V'] and color == '🛑':
        win()
        reset()
    elif results[0:1] == ['P'] and color == '🛑':
        martingale()
    elif results[0:1] == ['V'] and color == '⚫️':
        martingale()
    elif results[0:1] == ['B']:
        win()
        reset()

def save_data_to_csv(data):
    with open('sinais.csv', 'a', newline='') as csvfile:
        fieldnames = ['id', 'color', 'roll', 'created_at', 'updated_at', 'status',
                      'room_id', 'total_red_eur_bet', 'total_red_bets_placed',
                      'total_white_eur_bet', 'total_white_bets_placed',
                      'total_black_eur_bet', 'total_black_bets_placed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)

def start_monitoring():
    global running
    running = True
    send_message("Sistema iniciado! Prepare-se para os sinais.")
    
    while running:
        try:
            resultado = fetch_api()
            if resultado != check_resultado:
                check_resultado[:] = resultado
                estrategia(resultado)

                # Salvar dados em CSV
                save_data_to_csv(resultado)  # Aqui você salva os resultados a cada iteração

        except Exception as e:
            send_message(f"Erro ao buscar dados: {e}")

        time.sleep(5)

def estrategia(resultado):
    global analise_sinal, cor_sinal, cores

    cores = []  # Inicializa a lista de cores
    for x in resultado:
        if x >= 1 and x <= 7:
            color = 'V'  # Verde
        elif x >= 8 and x <= 14:
            color = 'P'  # Preto
        else:
            color = 'B'  # Branco
        cores.append(color)

    # Exibe apenas as cores
    print(f"Cores geradas: {cores}")  # Exibe as cores geradas no console

    if analise_sinal:
        correcao(cores, cor_sinal)
    else:
        patterns = {
            'Samurai': {'pattern': ['V', 'P'], 'name': '🥷🏼Samurai🥷🏼'},
            'King': {'pattern': ['V', 'P', 'V'], 'name': '👑King👑'},
        }

        for num, pat in patterns.items():
            if cores[:len(pat['pattern'])] == pat['pattern']:
                cor_sinal = '⚫️' if pat['pattern'][0] in ['P', 'V'] else '⚪️'
                enviar_sinal(cor_sinal, pat['name'])
                print(f"Sinal enviado: {pat['name']}")  # Exibe mensagem no console
                analise_sinal = True
                break

def stop_monitoring():
    global running
    running = False
    send_message(f"🏁 Encerramento da Sessão 🏁\n\n✅ Wins: {win_count}\n❌ Losses: {loss_count}\n\nObrigado por usar nosso serviço! Até a próxima sessão.")
    print(f"Relatório:\nWins: {win_count}\nLosses: {loss_count}")

# Para iniciar a monitorização, use o seguinte código:
if __name__ == "__main__":
    monitoring_thread = threading.Thread(target=start_monitoring)
    monitoring_thread.start()
