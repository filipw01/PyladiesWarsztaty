from flask import Flask, render_template

app = Flask(__name__)

@app.route("/osoby")
def dash():

    return render_template("3.html", list=osoby)


app.run(debug=True)
