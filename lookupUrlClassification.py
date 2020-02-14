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

    # Receive and Parse Standard Input
    target_urls = sys.argv
    target_urls.pop(0)
    if len(target_urls) == 0:
        print('Please Input URL')
        sys.exit()
    else:
        # Parse Input URL 
        parsed_target_urls = []
        for i in range(0, len(target_urls)):
            domain = checkUrl(target_urls[i])
            parsed_url = urlparse(target_urls[i])
            parsed_target_urls.append(domain)
        
        # Create API Cookie
        obfuscate_api_key = getApiSession.obfuscateApiKey(api_key)
        api_cookie = getApiSession.getCookie(hostname, obfuscate_api_key, username, password)

        response = lookupUrlClassification(hostname, api_cookie, parsed_target_urls)
        for res in response:
            print(res)


### Extract Domain from Standard Input ("HTTPS" and "HTTP" are excluded)###
def checkUrl(url):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    if re.match(pattern, url):
        parsed_url = urlparse(url)
        url = parsed_url.netloc
    return url

### Lookup URL Classification by Zscaler ###
def lookupUrlClassification(hostname, cookie, urls):
    url = 'https://'+hostname+'/api/v1/urlLookup'
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'cookie': cookie
    }
    response=requests.post( 
        url,
        json.dumps(urls),
        headers=headers
    )
    res = response.json()
    return res

### Exection ###
if __name__ == '__main__':
    main()