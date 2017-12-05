from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/current-status", methods = ["GET","POST"])
def dash():
    global current_status
    if request.method == "POST":
        current_status = request.get_json()["status"]
        return current_status
    if request.method == "GET":
        return "Aktualny status = {}".format(current_status)

app.run(debug= True)