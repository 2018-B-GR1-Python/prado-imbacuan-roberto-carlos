from instagram.client import InstagramAPI
import requests
import json

client_id = '6f1ac17a8cf441829ab77fe6e3830cad'
client_secret = '932212d0c31140b8acd54acab2f36e1c'
redirect_uri = 'https://www.instagram.com/techunreal7'

api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
redirect_uri = api.get_authorize_login_url(scope = ["basic"])
print(redirect_uri)


code = '9138a3a6bce6479384732f0f6391b47d'
