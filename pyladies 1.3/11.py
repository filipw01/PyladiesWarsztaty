import requests
import random
req_base = requests.get("https://swapi.co/api/species")
req = req_base
page = 1
wookieList=[]
while True:
    try:
        for number in range(req.json()['count']):
            if req.json()['results'][number]['name'] == 'Gungan':
                for person in range(len(req.json()['results'][number]['people'])):
                    temp_req = requests.get((req.json()['results'][number]['people'][person]))
                    wookie = ""
                    for integ in range(random.randrange(10)):
                        i=random.randrange(10)
                        if i%2==0:
                            wookie+='a'
                        else:
                            wookie+='r'
                    if wookie not in wookieList:
                        wookieList.append(wookie)
                    elif 'Grarrararaarr'not in wookieList:
                        wookie = 'Grarrararaarr'
                    else:
                        wookie = 'Grrararrrarrar'
                    print("G"+wookie+" ""<"+str(temp_req.json()['name'])+">")
                exit()
    except IndexError:
        page+=1
        req = requests.get(req_base.url + "?page=" + str(page))
