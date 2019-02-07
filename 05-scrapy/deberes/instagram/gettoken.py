from instagram.client import InstagramAPI
import requests
import json

client_id = '6f1ac17a8cf441829ab77fe6e3830cad'
client_secret = '932212d0c31140b8acd54acab2f36e1c'
redirect_uri = 'https://www.instagram.com/techunreal7'

api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

code = '1cc76da8a82a4cad97a8bbb6ecc51127'

def exchange_code_for_access_token2(code, redirect_uri, **kwargs):
    url = u'https://api.instagram.com/oauth/access_token'
    data = {
        u'client_id': client_id,
        u'client_secret': client_secret,
        u'code': code,
        u'grant_type': u'authorization_code',
        u'redirect_uri': redirect_uri
    }

    response = requests.post(url, data=data)

    account_data = json.loads(response.content)

    return account_data

access_token = api.exchange_code_for_access_token(code)
print ("access token: " )
print (access_token)