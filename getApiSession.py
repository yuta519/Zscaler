import requests
import http.client
import http.cookies
import json
import time
import pprint
import settings


### Parse API Key ###
def obfuscateApiKey (seed):
    now = int(time.time() * 1000)
    n = str(now)[-6:]
    r = str(int(n) >> 1).zfill(6)
    key = ""
    for i in range(0, len(str(n)), 1):
        key += seed[int(str(n)[i])]
    for j in range(0, len(str(r)), 1):
        key += seed[int(str(r)[j])+2]
    obfuscate_api_key = [now, key]
    # print(now, key)
    return obfuscate_api_key

### Get API Cookie ###
def getCookie(hostname, obfuscate_api_key, username, password):
    url = 'https://'+hostname+'/api/v1/authenticatedSession'
    payload = {
        'username': username,
        'password': password,
        'apiKey': obfuscate_api_key[1],
        'timestamp': obfuscate_api_key[0]
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
    }
    response=requests.post(
        url,
        json.dumps(payload),
        headers=headers)
    # pprint.pprint(response.json())
    cookie = response.cookies.get_dict()
    api_token = 'JSESSIONID=' + cookie['JSESSIONID']
    # print(api_token)
    return api_token

def getAuditLogs(hostname, cookie):
    url = 'https://'+hostname+'/api/v1/auditlogEntryReport'

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'cookie': cookie
    }
    response =requests.get(url, headers=headers)
    # pprint.pprint(response.json())
