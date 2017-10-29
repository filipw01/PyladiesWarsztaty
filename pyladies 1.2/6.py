import json
with open("dane_statki.json","r")as file_json:
    data_json = json.load(file_json)
z=0
lista=[]
while z<len(data_json):
    cost = 0
    y = 0
    while y<len(data_json):
        if data_json[y]["cost_in_credits"] != "unknown"and cost < int(data_json[y]["cost_in_credits"])and y not in lista:
            cost = int(data_json[y]["cost_in_credits"])
            najdrozszy=y
        y+=1
    z+=1
    if najdrozszy not in lista:
        lista.insert(z,najdrozszy)
lista.reverse()
file_statki = open("lista_statkow","w")
for item in lista:
    file_statki.write(data_json[item]["name"]+" kosztuje "+data_json[item]["cost_in_credits"]+" credits.\n")
file_statki.close()