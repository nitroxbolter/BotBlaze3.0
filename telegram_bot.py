import telebot

API_TOKEN = "7277223979:AAFL1497sJw25z6L-rXuH96wzTa6uGZPJhk"  # Substitua pelo seu token do bot
CHAT_ID = "6045775620"  # Substitua pelo ID correto do grupo ou chat

# Inicializa o bot
bot = telebot.TeleBot(API_TOKEN)

def send_message(text):
    """Envia uma mensagem para o chat especificado."""
    try:
        bot.send_message(CHAT_ID, text)
        print(f"Mensagem enviada: {text}")  # Log da mensagem enviada
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")  # Log de erro
