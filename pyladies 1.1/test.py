def cenzura_cyfr(wyraz):
    ciag=''
    for letter in wyraz:
        try:
            letter=int(letter)
            ciag+='#'
        except ValueError:
            ciag+=letter
    print (ciag)
cenzura_cyfr("password12345")
cenzura_cyfr('a1a ma k0ta')