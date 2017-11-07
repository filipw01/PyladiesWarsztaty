import requests

user = {'name':'Admin Kozak','password': 'SerioAdminKozak'}
req = requests.post('http://py.net/auth',json=user)
print(req.json()['api_key'])