from flask import Flask, render_template

app = Flask(__name__)

@app.route("/osoby")
def dash():
    osoby = []

    class Osoba:
        def __init__(self, name, surname, age):
            self.name = name
            self.surname = surname
            self.age = age
            osoby.append(self)

    Osoba("Adam", "Wyrwa", 19)
    Osoba("Jan", "Kat", 43)
    Osoba("Adam", "Wyrwa", 19)
    Osoba("Jan", "Kat", 43)
    Osoba("Adam", "Wyrwwda", 12139)
    Osoba("Jan", "Kawwwt", 43)
    Osoba("Adam", "Wyraadwa", 19)
    Osoba("Jan", "Kat", 43)
    Osoba("Adam", "Wyrwwada", 19)
    Osoba("Jan", "Kat", 43)
    return render_template("3.html", list=osoby)


app.run(debug=True)
