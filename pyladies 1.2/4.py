import json
with open("dane.json","r")as file_json:
    data_json = json.load(file_json)
x=0
file_women=open("sw_women","w")
file_men=open("sw_men","w")
while x<len(data_json):
    if data_json[x]["gender"] == "female":
        file_women.writelines(data_json[x]["name"]+"\n")
    if data_json[x]["gender"] == "male":
        file_men.writelines(data_json[x]["name"]+"\n")
    x+=1
file_women.close()
file_men.close()
