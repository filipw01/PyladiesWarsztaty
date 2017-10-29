file = open("plik",'r')
data = file.readlines()
slownik = {}
x=0
for lines in data:
    name = data[x][lines.find('.')+2:lines.find(' has ')]
    color = data[x][lines.find(' has ')+5:lines.find(' and ')]
    height = data[x][lines.find(' is ')+4:lines.find(' cm ')]
    x+=1
    slownik[name] = {'height':height,'eyes':color}
file.close()
for names in slownik:
    if int(slownik[names]['height']) > 200:
        with open('hero_200_plus','a') as file:
            file.write(names+'\n')
    else:
        with open('hero_short','a') as file:
            file.write(names +'\n')
