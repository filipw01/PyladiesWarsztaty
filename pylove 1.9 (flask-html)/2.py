from flask import Flask, render_template

app = Flask(__name__)

imiona=[]
nazwiska=[]
place=[]
ids=[]
opisy=[]

class Pracownik():
    def __init__(self,ID,imie,nazwisko,placa=0,opis="Brak opisu"):
        self.ID = ID
        self.imie=imie
        self.nazwisko=nazwisko
        self.placa=placa
        self.opis=opis
        place.append(self.placa)
        ids.append(self.ID)
        opisy.append(self.opis)
        imiona.append(self.imie)
        nazwiska.append(self.nazwisko)
    def imieGet(self):
        return self.imie
    def nazwiskoGet(self):
        return self.nazwisko
    def placaGet(self):
        return self.placa
    def opisGet(self):
        return self.opis

adam= Pracownik(0,"Adam","Korba")
filip= Pracownik(1,"Filip","Fiuczynski")
ewa= Pracownik(2,"Ewa","Boska")
aga= Pracownik(3,"Aga","Grabowska")

@app.route("/pracownicy/")
def pracownicy():
    ilosc = len(imiona)
    return render_template("4.html",id = None, imie=imiona,nazwisko = nazwiska,ilosc=ilosc,opis=None,placa=None)

@app.route("/pracownicy/<id>")
def pracownicyDetailed(id):
    ilosc = 1
    imie=[]
    nazwisko=[]
    placa=[]
    opis=[]
    for i in range(len(imiona)):
        if ids[i]==int(id):
           imie.append(imiona[i])
           opis.append(opisy[i])
           placa.append(place[i])
           nazwisko.append(nazwiska[i])


    return render_template("4.html",id=id, imie=imie,nazwisko = nazwisko,placa = placa,opis=opis,ilosc=ilosc)


app.run(debug=True)
