import countries
def najwieksza_powierzchnia(baza):
    x = 0
    powierzchnia = 0
    while x < len(baza):
        if powierzchnia < baza[x]["area"]:
            powierzchnia = baza[x]["area"]
            y=x
        x += 1
    print(baza[y]["name"]["official"]+" "+baza[y]["capital"])
najwieksza_powierzchnia(countries.countries)