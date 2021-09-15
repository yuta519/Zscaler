import json
from re import match
from sys import exit
from urllib.parse import urlparse

import requests

from auth import login
from auth import logout
from base import Base


base = Base()


def extract_url_domain(target_url):
    """Extract domain from url given by user."""
    url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    if match(url_pattern, target_url):
        parsed_url = urlparse(target_url)
        domain = parsed_url.netloc
        return domain
    else:
        return target_url


def fetch_url_categories(isCustomOnly: bool=False) -> str:
    """Get Zscaler's url catergories."""
    api_token = login()
    api_endpoint = (
        "{}/urlCategories?customOnly=true".format(base.base_url) 
        if isCustomOnly 
        else "{}/urlCategories".format(base.base_url)
    )
    headers = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    response = requests.get(api_endpoint, headers=headers)
    logout(api_token)

    return response.json()


# def lookup_url_classification(target_urls):
#     """Lookup url category classifications to given url."""
#     api_token = login()
#     target_domains = []
#     for target_url in target_urls:
#         parsed_target_url = self.extract_url_domain(target_url)
#         target_domains.append(parsed_target_url)
#     api_endpoint = "{}/urlLookup".format(self.base_url)
#     headers = {
#         "content-type": "application/json",
#         "cache-control": "no-cache",
#         "cookie": self.api_token,
#     }
#     response = requests.post(
#         api_endpoint, json.dumps(target_domains), headers=headers
#     )
#     json_results = response.json()
#     self.logout()
#     return json_results
