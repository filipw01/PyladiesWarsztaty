import requests

user = {'name':'Admin Kozak','password': 'SerioAdminKozak'}
req = requests.post('http://py.net/register',json=user)
print(req.status_code)
