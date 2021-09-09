import json

import requests
from requests.models import Response

from auth import login
from auth import logout
from base import Base


base = Base()


def fetch_adminusers(**kwargs):
    """Get Zscaler's url catergories."""
    api_token: str = login()
    api_endpoint: str = "{}/adminUsers".format(base.base_url)
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    response: Response = requests.get(api_endpoint, headers=headers)
    logout(api_token)
    return response.text


def url_lookup(self, target_urls):
    """Lookup url category classifications to given url."""
    self.login()
    parsed_target_urls = []
    for target_url in target_urls:
        parsed_target_url = self.extract_url_domain(target_url)
        parsed_target_urls.append(parsed_target_url)
    api_endpoint = "{}/urlLookup".format(self.base_url)
    headers = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": self.api_token,
    }
    response = requests.post(
        api_endpoint, json.dumps(parsed_target_urls), headers=headers
    )
    json_results = response.json()
    self.logout()
    return json_results
