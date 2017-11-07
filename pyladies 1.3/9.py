import requests

req = requests.get("https://swapi.co/api/films")
for number in range(req.json()['count']):
    if req.json()['results'][number]['title'] == 'The Empire Strikes Back':
        for char in range(len(req.json()['results'][number]['characters'])):
            temp_req = requests.get((req.json()['results'][number]['characters'][char]))
            print(temp_req.json()['name'])