import urllib.request
import json

url = 'http://services.groupkt.com/country/get/iso2code/IN'

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

res = response(url).decode()

print(json.loads(res))
