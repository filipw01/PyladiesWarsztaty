from flask import Flask, request, render_template, url_for
import requests
app = Flask(__name__)

@app.route("/planet-details", methods = ["GET","POST"])
def dash():
    zapytanie = requests.get("https://swapi.co/api/planets/?search={}".format(request.args.get("planet")))
    return zapytanie.text

app.run(debug= True)