import json
with open("dane.json","r")as file_json:
    data_json = json.load(file_json)
x=0
file_heros = open("sw_all_heros","w")
while x<len(data_json):
    file_heros.writelines(data_json[x]["name"]+" wazy "+data_json[x]["mass"]+"kg jest "+data_json[x]["gender"]+" i pochodzi z "+data_json[x]["homeworld"]+".\n")
    x+=1