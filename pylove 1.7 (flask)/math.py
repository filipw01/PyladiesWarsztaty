x = 2
table = []
hash ="1"
while not x==1000:
    if x >9:
        if int(hash+str(0)+str(x))%x == 0:
            table.append(x)
    elif x >99:
        if int(hash + str(x))%x == 0:
            table.append(x)
    else:
        if int(hash + str(x) + str(x)+str(x))%x == 0:
            table.append(x)
    x+=1
print(table)