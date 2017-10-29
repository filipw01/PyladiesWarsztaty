import countries
def liczba_granic(baza):
    x = 0
    granice = 0
    while x < len(baza):
        if granice < len(baza[x]["borders"]):
            granice = len(baza[x]["borders"])
            y = x
        x += 1
    print(baza[y]["name"]["official"] + " " + str(granice))
liczba_granic(countries.countries)