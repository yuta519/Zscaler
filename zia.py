import json
from re import match
from sys import exit
import time
from urllib.parse import urlparse

import requests


class Zia(object):

    def __init__(self, cloud_name, api_key, admin_username, admin_password,
                api_token=''):
        self.cloud_name = cloud_name
        self.api_key = api_key
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.base_url = 'https://admin.{}/api/v1'.format(cloud_name)
        self.api_token = api_token

    def obfuscateApiKey(self):
        """Parse API Key to use zscaler api. 
        This functions are supplied by Zscaler.
        More information of this function is below.
        Reference : Zscaler help pages.
            https://help.zscaler.com/zia/api-getting-started
        """
        seed = self.api_key
        now = int(time.time() * 1000)
        n = str(now)[-6:]
        r = str(int(n) >> 1).zfill(6)
        key = ""
        for i in range(0, len(str(n)), 1):
            key += seed[int(str(n)[i])]
        for j in range(0, len(str(r)), 1):
            key += seed[int(str(r)[j])+2]
        obfuscate_api_key = [now, key]
        return obfuscate_api_key
    
    def login(self):
        """Login to Zscaler and create an api session."""
        obfuscate_api_key = self.obfuscateApiKey()
        api_endpoint = '{}/authenticatedSession'.format(self.base_url)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        payload = {
            'username': self.admin_username,
            'password': self.admin_password,
            'timestamp': obfuscate_api_key[0],
            'apiKey': obfuscate_api_key[1]
        }
        response = requests.post(
            api_endpoint,
            json.dumps(payload),
            headers=headers)
        cookie = response.cookies.get_dict()
        api_token = 'JSESSIONID=' + cookie['JSESSIONID']
        self.api_token = api_token

    def activate_configuration(self):
        """ """
        # TODO (yuta.kawamura)
        pass

    def logout(self):
        """Logout from API sesion."""
        api_endpoint = '{}/authenticatedSession'.format(self.base_url)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache", 
            'cookie': self.api_token
        }
        requests.delete(api_endpoint, headers=headers)


class ZiaLookupUrl(Zia):
    """Handle the api to lookup a given url."""
    
    def extract_url_domain(self, target_url):
        """Extract domain from url given by user."""
        url_pattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'
        if match(url_pattern, target_url):
            parsed_url = urlparse(target_url)
            domain = parsed_url.netloc
            return domain
        else:
            return target_url

    def get_url_categories(self, mode='all'):
        """Get Zscaler's url catergories."""
        self.login()
        if mode == 'all':
            api_endpoint = '{}/urlCategories'.format(self.base_url)
        elif mode == 'customonly':
            api_endpoint = '{}/urlCategories?customOnly=true'.format(
                            self.base_url)
        else:
            print('wrong option name : {}'.format(mode))
            exit()
        headers = {
            'content-type': 'application/json',
            'cache-control': 'no-cache', 
            'cookie': self.api_token
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
        api_endpoint = '{}/urlLookup'.format(self.base_url)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'cookie': self.api_token
        }
        response = requests.post( 
            api_endpoint,
            json.dumps(parsed_target_urls),
            headers=headers)
        json_results = response.json()
        self.logout()
        return json_results
