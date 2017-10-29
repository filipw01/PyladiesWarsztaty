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
srednia = {}
listaKolorow =[]
for nameOne in slownik:
    srednia[slownik[nameOne]['eyes']] = {'heightSum':int(slownik[nameOne]['height']),'count':1}
    for nameTwo in slownik:
        if slownik[nameOne]['eyes'] == slownik[nameTwo]['eyes'] and slownik[nameOne]!=slownik[nameTwo]:
            srednia[slownik[nameOne]['eyes']]['heightSum'] += int(slownik[nameTwo]['height'])
            srednia[slownik[nameOne]['eyes']]['count'] += 1
    if slownik[nameOne]['eyes'] not in listaKolorow:
        print("People with "+slownik[nameOne]['eyes']+" eyes are average "+str(srednia[slownik[nameOne]['eyes']]['heightSum']/srednia[slownik[nameOne]['eyes']]['count'])+"cm height.")
        listaKolorow.append(slownik[nameOne]['eyes'])