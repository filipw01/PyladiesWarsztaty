import countries
def wyszukiwarka_krajowbez(baza,teren):
    x=0
    while x < len(baza):
        if baza[x]["region"]!=teren:
            print(baza[x]["name"]["official"])
        x+=1
wyszukiwarka_krajowbez(countries.countries, "Africa")