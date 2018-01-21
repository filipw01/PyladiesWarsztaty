try:
    x = input("Input: ")
    kwota = ""
    for i in range(len(x)):
        if x[i].isdigit():
            kwota+=str(x[i])
        else:
            break

    for i in range(len(x)):
        if x[i].isdigit():
            pass
        elif x[i]=="$":
            waluta = "$"
            break
        elif x[i]=="€":
            waluta = "€"
            break
        elif x[i]=="¥":
            waluta = "¥"
            break
        elif x[i]=="z" and x[i+1]=="ł":
            waluta = "zł"
            break

    found = False
    for i in range(len(x)):
        if x[i] == "t" and x[i+1] == "o":
            found = True
        if found:
            if x[i] == "$":
                przelicznik = "$"
                break
            elif x[i] == "€":
                przelicznik = "€"
                break
            elif x[i] == "¥":
                przelicznik = "¥"
                break
            elif x[i] == "z" and x[i + 1] == "ł":
                przelicznik = "zł"
                break

    kwota=int(kwota)

    if waluta=="$":
        kwota/=1000
    if waluta=="€":
        kwota/=4505
    if waluta=="¥":
        kwota/=100

    if przelicznik=="$":
        nowaKwota = kwota*1000
    if przelicznik=="€":
        nowaKwota = kwota * 4505
    if przelicznik=="¥":
        nowaKwota = kwota * 100
    if przelicznik=="zł":
        nowaKwota = kwota

except Exception as e:
    print(e)
print(kwota)
print(waluta)
print(przelicznik)
print(nowaKwota)