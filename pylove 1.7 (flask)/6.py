from flask import Flask, request, render_template, url_for
import json, operator
app = Flask(__name__)

użytkownicy = []
imiona = {}
@app.route("/users/stats", methods = ["POST"])
def dash():
    użytkownicy.append(request.get_json())
    wiek = 0
    for i in range(len(użytkownicy)):
        wiek += int(użytkownicy[i]["wiek"])
        if użytkownicy[i]["imie"] in imiona:
            imiona[użytkownicy[i]["imie"]] += 1
        else:
            imiona[użytkownicy[i]["imie"]] = 1
    najpopularniesze_imie = max(imiona, key=imiona.get)
    return "Ilosc osob: {}, Sredni wiek: {}, Najpopularniejsze imie: {},".format(len(użytkownicy), wiek/len(użytkownicy), najpopularniesze_imie)
app.run(debug= True)
