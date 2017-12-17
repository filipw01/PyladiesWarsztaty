from flask import Flask, request, render_template, url_for
import requests
app = Flask(__name__)

@app.route("/planet-details", methods = ["GET","POST"])
def dash():
    zapytanie = requests.get("https://swapi.co/api/planets/?search={}".format(request.args.get("planet")))
    if zapytanie.json()["count"]!=0:
        return zapytanie.text
    else:
        return "Planet {} does not exist".format(request.args.get("planet"))

app.run(debug= True)