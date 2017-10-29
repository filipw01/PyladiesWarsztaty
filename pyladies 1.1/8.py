import countries
def stolice_na(baza,litera):
    x = 0
    while x < len(baza):
        if baza[x]["capital"].startswith(litera):
            print(baza[x]["name"]["official"]+" "+baza[x]["capital"])
        x += 1
stolice_na(countries.countries, "W")