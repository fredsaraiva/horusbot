#
# Embrião de um script para envio de mensagem via bot telegram
#

import sendTelegram as e
import configparser
import checkSite
import time

cfg = configparser.ConfigParser()
cfg.read("confs/config.ini")

my_token = cfg.get('section1', 'token')
my_chat_id = cfg.get('section2', 'chat_id')


if __name__ == '__main__':

    site = "www.ufpb.br"
    r = checkSite.check("http://" + site)
    print(r)

    while 1:
        time.sleep(120)
        if r == 1:
            e.send('Tudo normal com ' + site, my_chat_id, my_token)
        else:
            e.send('Problemas com ' + site, my_chat_id, my_token)
