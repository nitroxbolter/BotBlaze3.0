import telebot

# Token do bot
api = "7277223979:AAFL1497sJw25z6L-rXuH96wzTa6uGZPJhk"  # Substitua pelo seu token do bot
chat_id = "6045775620"  # Substitua pelo ID correto do grupo ou chat

# Inicializa o bot
bot = telebot.TeleBot(api)

def send_message(text):
    bot.send_message(chat_id, text)

