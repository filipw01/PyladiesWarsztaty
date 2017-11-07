import requests

req_base = requests.get("https://swapi.co/api/starships")
req = req_base
page = 1
while True:
    try:
        for number in range(req.json()['count']):
            if req.json()['results'][number]['name'] == 'Millennium Falcon':
                for pilot in range(len(req.json()['results'][number]['pilots'])):
                    temp_req = requests.get((req.json()['results'][number]['pilots'][pilot]))
                    temp_bmi = int(temp_req.json()['mass'])/(int(temp_req.json()['height'])/100)**2
                    print(temp_req.json()['name']+" "+str(temp_bmi))
                exit()
    except IndexError:
        page+=1
        req = requests.get(req_base.url + "?page=" + str(page))
