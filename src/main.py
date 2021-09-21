#
# Bot que usa o telegram para monitoramento de queda de site
# Autor: Fred Saraiva
# 2021-09-21
#

import configparser
import time
import checkSite
import sendTelegram

cfg = configparser.ConfigParser()
cfg.read("conf/config.ini")

my_token = cfg.get('section1', 'token')
my_chat_id = cfg.get('section2', 'chat_id')
my_site = cfg.get('section3', 'site')


"""
Estado de alerta

"""


def __alerta__():

    print('Alerta em ' + my_site)
    while 1:
        time.sleep(60)
        if r == 1:
            sendTelegram.send('Voltou ' + my_site, my_chat_id, my_token)
            __monitorar__()


"""

Estado de monitoramento

"""


def __monitorar__():

    print('Monitorando ' + my_site)
    while 1:
        time.sleep(120)
        if r == 0:
            sendTelegram.send('Queda do site ' + my_site, my_chat_id, my_token)
            __alerta__()


"""

Main

"""

if __name__ == '__main__':

    r = checkSite.__check__("http://" + my_site)
    __monitorar__()
