import json
import getApiSession
import requests
import pprint
import sys
import settings
from urllib.parse import urlparse
import re

### Main Functions ###
def main():
    # Account Information
    id_value = settings.getId()
    api_key  = id_value[0]
    username = id_value[1] 
    password = id_value[2]
    hostname = id_value[3]
        
    # Create API Cookie
    obfuscate_api_key = getApiSession.obfuscateApiKey(api_key)
    api_cookie = getApiSession.getCookie(hostname, obfuscate_api_key, username, password)
    # print(api_cookie)

    response = createUrlFilteringRules(hostname, api_cookie)
    # pprint.pprint(response)
    print(response.text)


### Create URL Fitering Rules ###
def createUrlFilteringRules(hostname, cookie):
    url = 'https://'+hostname+'/api/v1/urlFilteringRules'
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'cookie': cookie
    }

    payload = {
        "name": "Test Policy 01",
        "order": 1,
        "protocols": [
            "ANY_RULE"
        ],
        "rank": 7,
        "action": "BLOCK",
        "urlCategories": ["OTHER_ADULT_MATERIAL"]
    }

    # payload = json.dumps(payload)
    # print(payload)

    response=requests.post( 
        url,
        json.dumps(payload),
        headers=headers
    )
    # res = response.json()
    res = response
    return res

### Exection ###
if __name__ == '__main__':
    main()