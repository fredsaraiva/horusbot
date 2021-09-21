import telebot

def send(msg, chat_id, token):
    """
    Envio da mensagem

    """
    bot = telebot.TeleBot(token)
    bot.send_message(chat_id, msg)