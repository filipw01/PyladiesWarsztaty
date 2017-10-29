def droga_pokonana(czas, przyspieszenie, vs=0):
    print(przyspieszenie*czas*czas/2+ vs *czas)
droga_pokonana(5,5)
droga_pokonana(10,10,vs=100)