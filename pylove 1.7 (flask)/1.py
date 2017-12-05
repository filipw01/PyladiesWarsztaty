from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/add/<liczba1>/<liczba2>", methods = ["GET","POST"])
def dash(liczba1, liczba2):
    return "{}".format(int(liczba1)+int(liczba2))

app.run(debug= True)