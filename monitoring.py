import threading
import time
from telegram_bot import send_message
from api import fetch_api
from patterns import check_patterns  # Importa a função de padrões

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
    print("Sistema resetado.")  # Print de reset

def martingale():
    global entrada
    entrada += 1
    if entrada <= max_gale:
        send_message(f"⚠️ Gale {entrada} ⚠️")
        print(f"Martingale ativado: Gale {entrada}")  # Print de martingale
    else:
        loss()
        reset()

def win():
    global win_count
    send_message("✅")
    win_count += 1
    print("Vitória registrada!")  # Print de vitória

def loss():
    global loss_count
    send_message("❌")
    loss_count += 1
    print("Derrota registrada.")  # Print de derrota

def enviar_sinal(cor, padrao):
    send_message(f'''
🚨 Sinal encontrado 🚨

⏯️ Padrão: {padrao}

💶 Entrar no {cor}

🦾 Proteger no ⚪️

🐓 2 martingale: (opcional)''')
    print(f"Sinal enviado: Entrar no {cor} com padrão {padrao}")  # Print do sinal enviado

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

def get_color_from_roll(roll):
    """Retorna a cor correspondente ao valor do roll."""
    if 1 <= roll <= 7:
        return 'V'  # Vermelho
    elif 8 <= roll <= 14:
        return 'P'  # Preto
    elif roll == 0:
        return 'B'  # Branco
    else:
        return None  # Para rolagens fora do intervalo conhecido

def start_monitoring():
    global running
    running = True
    send_message("Sistema iniciado! Prepare-se para os sinais.")
    print("Monitoramento iniciado.")  # Print de início do monitoramento
    while running:
        try:
            resultado = fetch_api()
            if resultado != check_resultado:
                check_resultado[:] = resultado
                print(f"Resultado recebido: {resultado}")  # Print dos resultados recebidos
                estrategia(resultado)
        except Exception as e:
            send_message(f"Erro ao buscar dados: {e}")
            print(f"Erro ao buscar dados: {e}")  # Print de erro
        time.sleep(5)

def estrategia(resultado):
    global analise_sinal, cor_sinal

    cores = []  # Inicializa a lista de cores
    for data in resultado:
        roll = data.get("roll")  # Captura o valor do roll
        if roll is not None:  # Verifica se roll não é None
            try:
                roll = int(roll)  # Converte o valor para inteiro
                print(f"Roll recebido: {roll}")  # Print do roll recebido
                color = get_color_from_roll(roll)  # Converte o roll em cor
                if color:  # Verifica se a cor é válida
                    cores.append(color)
                    print(f"Cor transformada: {color}")  # Print da cor transformada
                else:
                    print(f"Cor inválida para o roll: {roll}")  # Print para cor inválida
            except ValueError:
                print(f"Valor de roll inválido: {roll}")  # Log para valor inválido

    # Exibe apenas as cores
    print(f"Cores geradas: {cores}")  # Exibe as cores geradas no console

    # Chama a função de verificação de padrões
    analise_sinal, cor_sinal = check_patterns(cores, enviar_sinal, correcao, analise_sinal, cor_sinal)

    # Print para análise de padrão
    if analise_sinal:
        print(f"Padrão encontrado: {cor_sinal}")  # Print do padrão encontrado
    else:
        print("Nenhum padrão encontrado.")  # Print caso não encontre padrão

def stop_monitoring():
    global running
    running = False
    send_message(f"🏁 Encerramento da Sessão 🏁\n\n✅ Wins: {win_count}\n❌ Losses: {loss_count}\n\nObrigado por usar nosso serviço! Até a próxima sessão.")
    print(f"Relatório:\nWins: {win_count}\nLosses: {loss_count}")  # Print do relatório

# Para iniciar a monitorização, use o seguinte código:
if __name__ == "__main__":
    monitoring_thread = threading.Thread(target=start_monitoring)
    monitoring_thread.start()
