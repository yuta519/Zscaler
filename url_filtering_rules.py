import json
from typing import Dict
from typing import List
from typing import Union

import requests
from requests import status_codes
from requests.models import Response

from auth import login
from auth import logout
from base import Base

base = Base()


def fetch_all_url_filering_rules(isFull: bool = False) -> Dict[str, str]:
    """Get Zscaler's url filtering rules."""
    api_endpoint: str = f"{base.base_url}/urlFilteringRules"
    api_token: str = login()
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    response: Response = requests.get(api_endpoint, headers=headers)
    logout(api_token)

    url_filtering_rules: list = response.json()

    if not isFull:
        try:
            for url_filtering_rule in url_filtering_rules:
                del (
                    url_filtering_rule['rank'],
                    url_filtering_rule['requestMethods'],
                    url_filtering_rule['blockOverride'],
                    url_filtering_rule['enforceTimeValidity'],
                    url_filtering_rule['cbiProfileId'],
                )
        except:
            pass
    url_filtering_rules = sorted(url_filtering_rules, key=lambda x:x['order'])
    
    return url_filtering_rules


def fetch_specific_url_filering_rules():
    pass


def create_url_filering_rules(
    name: str,
    order: int,
    protocols: List[str],
    locations: List[str],
    groups: List[str],
    departments: List[str],
    users: List[str],
    url_categories: List[str],
    state: str,
    rank: int,
    action: str
) -> str:
    api_endpoint: str = f"{base.base_url}/urlFilteringRules"
    api_token: str = login()
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }

    payload: Dict[str, Union[str, int, List[str]]] = {
        "name": name,
        "order": order,
        "protocols": protocols,
        "locations": locations,
        "groups": groups,
        "departments": departments,
        "users": users,
        "urlCategories": url_categories,
        "state": state,
        "rank": rank,
        "action": action,
    }
    response: Response = requests.post(
        api_endpoint, json.dumps(payload), headers=headers
    )
    logout(api_token)

    message =(
        f"Success: '{response.json()['name']}' is created" if response.status_code == 200 
        else f"Failed: { response.status_code } { response.json()['message'] }"
    )
    return message
