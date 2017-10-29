def cezar(tekst,przemieszczenie):
    zaszyfrowane=""
    for letter in tekst:
        if letter.isalpha():
            if chr(ord(letter)+przemieszczenie).isalpha():
                zaszyfrowane+=chr(ord(letter)+przemieszczenie)
            else:
                zaszyfrowane+=chr(ord(letter)+przemieszczenie+26)
        else:
            zaszyfrowane+=letter
    print(zaszyfrowane)
cezar("abc", 2)
cezar("abc", -2)