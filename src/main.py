#
# Embrião de um script para envio de mensagem via bot telegram
#

import configparser, time, checkSite, sendTelegram as e

cfg = configparser.ConfigParser()
cfg.read("conf/config.ini")

my_token = cfg.get('section1', 'token')
my_chat_id = cfg.get('section2', 'chat_id')
my_site = cfg.get('section3', 'site')

if __name__ == '__main__':

    r = checkSite.check("http://" + my_site)
    print(r)

    while 1:
        time.sleep(120)
        if r == 1:
            e.send('Tudo normal com ' + my_site, my_chat_id, my_token)
        else:
            e.send('Problemas com ' + my_site, my_chat_id, my_token)
