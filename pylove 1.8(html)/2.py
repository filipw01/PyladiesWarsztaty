from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/hello")
def dash():
    name = request.args.get("name")
    return render_template("3.html", name=name)
app.run(debug= True)
