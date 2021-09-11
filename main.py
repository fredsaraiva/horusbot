#
# Embrião de um script para envio de mensagem via bot telegram
#

import sendTelegram as e
import configparser

cfg = configparser.ConfigParser()
cfg.read("confs/config.ini")

my_token = cfg.get('section1', 'token')
my_chat_id = cfg.get('section2', 'chat_id')


if __name__ == '__main__':

    e.send('Teste', my_chat_id, my_token)
    print("Enviado")
