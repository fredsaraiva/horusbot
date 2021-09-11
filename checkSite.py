#
# Testa se um site está no ar
#
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def check(site):
    req = Request(site)
    try:
        urlopen(req)

    except HTTPError:
        return 0

    except URLError:
        return 0

    else:
        return 1
