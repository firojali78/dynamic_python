import requests
import json
from requests_ntlm import HttpNtlmAuth

def fetch_item_list():
    url = "http://20.235.83.237:8049/BodycareLive/ODataV4/Company('Bodycare%20Creations%20Ltd.')/ItemListWebApp"

    payload = {}
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload, auth=HttpNtlmAuth(url + "VMServer1\Ankit", "bcpl@123"))


    contents = response.json().get('value')
    No = [item.get('No') for item in contents]
    desc = [item.get('Description') for item in contents]
    print(len(No), len(desc))
    merge = [str(a)+'~' + str(b) for a,b in zip(No,desc)]

    return merge
#a = fetch_item_list()
#print(a)