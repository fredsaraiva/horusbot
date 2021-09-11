# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import telebot

my_token = '1954316953:AAFDWSMUrNwHx54IN7xfx5mMuNLvqWW-8yM'

def send(msg, chat_id, token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telebot.TeleBot(my_token)
    bot.send_message(chat_id,msg)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send('Teste do telegram',-536575991,my_token)


