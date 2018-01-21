from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "klawy sekret"


@app.route("/")
def dash():
    return redirect("/konto/")



class Money:
    def __init__(self):
        self.money = 1000
        self.przelewy = []
    def moneyGet(self):
        return self.money
    def moneySet(self,new_money):
        self.money=new_money
    def przelewyGet(self):
        return self.przelewy
    def przelewyAppend(self,przelew):
        self.przelewy.append(przelew)

nowe_srodki = Money()
@app.route("/konto/", methods = ["GET","POST"])
def konto():
    if request.method=="POST":
        try:
            kwota_przelewu = int(request.form['kwota'])
            numer_konta = int(request.form['numer_konta'])
        except Exception:
            flash("Zarowno kwota przelewu jak i numer konta musi byc liczba")
            numer_konta = 0
            kwota_przelewu =0
        nowe_srodki.moneySet(nowe_srodki.moneyGet() -kwota_przelewu)
        nowe_srodki.przelewyAppend({'kwota':kwota_przelewu,"numer_konta":numer_konta})
        return redirect("/konto/")

    return render_template("3.html", money=nowe_srodki.moneyGet(), przelewy = nowe_srodki.przelewyGet())


app.run(debug=True)