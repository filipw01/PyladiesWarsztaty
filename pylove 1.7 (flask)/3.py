from flask import Flask, request, render_template, url_for
import json
app = Flask(__name__)

@app.route("/user/<username>/set-password", methods = ["POST"])
def dash(username):
    if request.method == "POST":
        password = request.get_json()["pass"]
        x = {username:password}
        with open("database.json", "w") as database:
            json.dump(x, database)
        return "Gratulacje haslo ustawione.{}".format(password)
@app.route("/user/<username>/login", methods = ["POST"])
def login(username):
    if request.method == "POST":
        with open("database.json") as database:
            data = json.load(database)
            if username in data:
                if data[username] == request.get_json()["pass"]:
                    return "Zalogowano pomyslnie"
                else:
                    return "Zle dane"
            else:
                return "Nie ma takiego uzytkownika"

app.run(debug= True)