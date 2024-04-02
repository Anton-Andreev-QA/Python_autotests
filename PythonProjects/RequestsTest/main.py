import requests

URL = 'https://api.pokemonbattle.me/v2'

TOKEN = '85dcb5a41a940dc8975422f79b71e62e'

HEADERS = {'Content-Type' : 'application/json', 
           'trainer_token' : TOKEN}

ID = '15913'

body = {
    "name": "Федя",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

#response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
#print(response.text)

body_1 = {
    "pokemon_id": ID,
    "name": "Жора",
    "photo": "https://dolnikov.ru/pokemons/albums/015.png"
}

#response_1 = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_1)
#print(response_1.text)

body_2 = {
    "pokemon_id": ID
}

response_2 = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_2)
print(response_2.text)
