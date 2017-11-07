import requests

req = requests.get("http://py.net/query_string?aha=rozumiem")
print(req.json())