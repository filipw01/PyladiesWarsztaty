import requests

resp = requests.get('http://py.net/health')
print(resp.text)
print(resp.elapsed)
print(resp.json()["health"])
print("Status aplikacji "+str(resp.status_code))