import json
from re import match
from typing import Dict, List
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


def fetch_url_categories(isCustomOnly: bool = False) -> str:
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


def create_custom_url_category(
    configured_name: str,
    urls: List[str],
    db_categorized_urls: List[str],
    description: str,
) -> str:
    api_token = login()
    api_endpoint = "{}/urlCategories".format(base.base_url)
    headers = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    payload = {
        "configuredName": configured_name,
        "urls": urls,
        "dbCategorizedUrls": db_categorized_urls,
        "customCategory": True,
        "editable": True,
        "description": description,
        "superCategory": "USER_DEFINED",
        "urlsRetainingParentCategoryCount": 0,
        "type": "URL_CATEGORY",
    }
    response = requests.post(api_endpoint, json.dumps(payload), headers=headers)
    logout(api_token)
    message: str = (
        f"[INFO] {str(response.status_code)} {response.json()['configuredName']}"
        if response.status_code == 200
        else f"[INFO] {str(response.status_code)} {response.json()['message'] }"
    )
    return message


def update_custom_url_category(isCustomOnly: bool = False) -> str:
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


def lookup_url_classification(target_urls: List[str]) -> Dict[str, str]:
    """Lookup url category classifications to given url."""
    api_token = login()
    api_endpoint = "{}/urlLookup".format(base.base_url)
    headers = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    domains = [extract_url_domain(url) for url in target_urls]
    response = requests.post(api_endpoint, json.dumps(domains), headers=headers)
    logout(api_token)

    return response.json()
