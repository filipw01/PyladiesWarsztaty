list = [1,2,3,4,5,5,5,"5"]
newlist = []

for item in list:
    if list.count(item) > 1:
        newlist.append(item)
print(newlist)