def liczba_odwaznikow(odwaznik1,odwaznik2):
    wielokrotnosc1,wielokrotnosc2=odwaznik1,odwaznik2
    ilosc1,ilosc2=1,1
    while wielokrotnosc1 != wielokrotnosc2:
        while wielokrotnosc1 < wielokrotnosc2:
            wielokrotnosc1+=odwaznik1
            ilosc1+=1
        if wielokrotnosc1>wielokrotnosc2:
            wielokrotnosc2+=odwaznik2
            ilosc2+=1
    print(str(ilosc1) + " "+ str(ilosc2))
liczba_odwaznikow(2,8)
liczba_odwaznikow(4,6)