from flask import Flask, request, render_template, url_for
import requests
app = Flask(__name__)

@app.route("/users/add", methods = ["POST"])
def dash():
    imie = request.get_json()["imie"]
    wiek = request.get_json()["wiek"]
    plec = request.get_json()["plec"]
    return "Imie: {}, Wiek: {}, Plec: {}".format(imie, wiek, plec)
app.run(debug= True)