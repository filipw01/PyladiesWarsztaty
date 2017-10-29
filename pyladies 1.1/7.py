import countries
def min_waluty(baza,liczba):
    x = 0
    while x < len(baza):
        if len(baza[x]["currency"]) >= liczba:
            print(baza[x]["currency"])
        x += 1
min_waluty(countries.countries, 2)