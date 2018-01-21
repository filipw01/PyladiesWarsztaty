def readFile(filename):
    print(str(filename.read()))

validate = True
while validate:
    try:
        x = input("Input: ")
        if x == "1":
            readFile('x.txt')
        if x == "2":
            readFile('y.txt')
        if x == "3":
            readFile('z.txt')
    except Exception as e:
        print(e)
print(x)