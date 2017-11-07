import requests

dicti = {"status":"new state"}
req = requests.post('http://py.net/status/set', json=dicti)
reqGet = requests.get('http://py.net/status')
print(reqGet.text)

