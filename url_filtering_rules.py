from typing import Dict
import requests
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
                    url_filtering_rule['protocols'],
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



    pass


def fetch_specific_url_filering_rules():
    pass

def create_url_filering_rules():
    pass