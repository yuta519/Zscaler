import json
import time
from typing import List
from typing import Union


import requests
from requests.models import Response

from base import Base


base = Base()


def obfuscateApiKey() -> List[Union[int, str]]:
    """Parse API Key to use zscaler api.
    This functions are supplied by Zscaler.
    More information of this function is below.
    Reference : Zscaler help pages.
        https://help.zscaler.com/zia/api-getting-started
    """
    seed = base.api_key
    now = int(time.time() * 1000)
    n = str(now)[-6:]
    r = str(int(n) >> 1).zfill(6)
    key = ""
    for i in range(0, len(str(n)), 1):
        key += seed[int(str(n)[i])]
    for j in range(0, len(str(r)), 1):
        key += seed[int(str(r)[j]) + 2]
    obfuscate_api_key = [now, key]
    return obfuscate_api_key


def login() -> str:
    """Login to Zscaler and create an api session."""
    obfuscate_api_key: List[int, str] = obfuscateApiKey()

    api_endpoint: str = "{}/authenticatedSession".format(base.base_url)
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
    }
    payload: dict[str, str] = {
        "username": base.admin_user,
        "password": base.admin_password,
        "timestamp": obfuscate_api_key[0],
        "apiKey": obfuscate_api_key[1],
    }

    response: Response = requests.post(
        api_endpoint, json.dumps(payload), headers=headers
    )
    cookie: dict[str, str] = response.cookies.get_dict()
    api_token: str = "JSESSIONID=" + cookie["JSESSIONID"]

    return api_token


def activate_configuration() -> None:
    """ """
    # TODO (yuta.kawamura)
    pass


def logout(api_token) -> None:
    """Logout from API sesion."""
    api_endpoint: str = f"{base.base_url}/authenticatedSession"
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    requests.delete(api_endpoint, headers=headers)
