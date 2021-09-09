import json
from re import match
from sys import exit
from urllib.parse import urlparse

import requests


class urlCategories(object):
    """ This class manages administrator settings"""

    def extract_url_domain(self, target_url):
        """Extract domain from url given by user."""
        url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
        if match(url_pattern, target_url):
            parsed_url = urlparse(target_url)
            domain = parsed_url.netloc
            return domain
        else:
            return target_url

    def get_url_categories(self, mode="all"):
        """Get Zscaler's url catergories."""
        self.login()
        if mode == "all":
            api_endpoint = "{}/urlCategories".format(self.base_url)
        elif mode == "customonly":
            api_endpoint = "{}/urlCategories?customOnly=true".format(self.base_url)
        else:
            print("wrong option name : {}".format(mode))
            exit()
        headers = {
            "content-type": "application/json",
            "cache-control": "no-cache",
            "cookie": self.api_token,
        }
        response = requests.get(api_endpoint, headers=headers)
        self.logout()
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
