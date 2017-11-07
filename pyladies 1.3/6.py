import requests

req = requests.get("http://py.net/cat")
with open('file.png','wb') as file:
    file.write(req.content)

