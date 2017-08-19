import urllib.request
import json

url = 'http://services.groupkt.com/country/get/iso2code/IN'


req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))

print(cont)
