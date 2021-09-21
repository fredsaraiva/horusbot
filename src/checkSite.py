#
# Checagem do site
# Autor: Fred Saraiva
# 2021-09-21
#
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

"""

Teste do site

"""


def __check__(site):
    req = Request(site)
    try:
        urlopen(req)

    except HTTPError:
        return 0

    except URLError:
        return 0

    else:
        return 1
