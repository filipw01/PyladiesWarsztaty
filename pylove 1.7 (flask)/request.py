import requests

post_result = requests.post(
    "http://127.0.0.1:5000/user/filip/set-password",
    json={"pass": "password"}
)
print(post_result.text)

login = requests.post(
    "http://127.0.0.1:5000/user/filip/login",
    json={"pass": "password"}
)
print(login.text)
login2 = requests.post(
    "http://127.0.0.1:5000/user/filia/login",
    json={"pass": "wrong_password"}
)
print(login2.text)


