import requests

req_base = requests.get("https://swapi.co/api/planets")
req = req_base
page = 1
while True:
    try:
        for number in range(req.json()['count']):
            if req.json()['results'][number]['name'] == 'Tatooine':
                for resident in range(len(req.json()['results'][number]['residents'])):
                    temp_req = requests.get((req.json()['results'][number]['residents'][resident]))
                    print(temp_req.json()['name'])
                exit()
    except IndexError:
        page+=1
        req = requests.get(req_base.url + "?page=" + str(page))
