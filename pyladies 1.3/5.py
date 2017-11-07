import requests

user = {'name':'Admin Kozak','password': 'SerioAdminKozak'}
req_auth = requests.post('http://py.net/auth',json=user)
my_status = {"api_key" : req_auth.json()['api_key'], "status" : "Admin jest po prostu kozakiem. Pozdrawiam maminke i tatinka. Sledzicie mnie?"}
req_statusSet = requests.post("http://py.net/status/set", json=my_status)

req_status = requests.get('http://py.net/user_status')
print(req_status.text)


