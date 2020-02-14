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
    # Create API Cookie
    value      = getApiSession.obfuscateApiKey()
    api_cookie = getApiSession.getCookie(value)

    # Receive and Parse Standard Input
    target_urls = sys.argv
    target_urls.pop(0)
    if len(target_urls) == 0:
        print('Please Input URL')
        sys.exit()
    else:
        parsed_target_urls = []
        for i in range(0, len(target_urls)):
            domain = checkUrl(target_urls[i])
            parsed_url = urlparse(target_urls[i])
            parsed_target_urls.append(domain)
        lookupUrlClassification(api_cookie, parsed_target_urls)

### Extract Domain from Standard Input ###
def checkUrl(url):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    if re.match(pattern, url):
        parsed_url = urlparse(url)
        url = parsed_url.netloc
    return url

### Lookup URL Classification by Zscaler ###
def lookupUrlClassification(cookie, urls):

    ### Environment Information ###
    id_value = settings.getId()
    hostname = id_value[3]

    url = 'https://'+hostname+'/api/v1/urlLookup'
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'cookie': cookie
    }
    payload = urls

    response=requests.post( 
        url,
        json.dumps(payload),
        headers=headers
    )
    pprint.pprint(response.json())


### Exection ###
if __name__ == '__main__':
    main()