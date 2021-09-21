#
# Envio de mensagem pelo telegram
# Autor: Fred Saraiva
# 2021-09-21
#

import telebot

"""
 Envio da mensagem

"""


def __send__(msg, chat_id, token):

    bot = telebot.TeleBot(token)
    bot.send_message(chat_id, msg)
