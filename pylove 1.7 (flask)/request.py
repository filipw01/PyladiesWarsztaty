import requests

post_result = requests.post(
    "http://127.0.0.1:5000/users/stats",
    json={"imie": "Grzegorz", "wiek": "26", "plec": "m"}
)
print(post_result.text)

post_result = requests.post(
    "http://127.0.0.1:5000/users/stats",
    json={"imie": "asz", "wiek": "2216", "plec": "am"}
)
print(post_result.text)

post_result = requests.post(
    "http://127.0.0.1:5000/users/stats",
    json={"imie": "asz", "wiek": "2216", "plec": "am"}
)
print(post_result.text)

