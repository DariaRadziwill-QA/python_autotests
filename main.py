import requests
import json

token = '2b0f5f961229fdc58596b4083a66e739'

response = requests.post ('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token' : token},
json = {
    "name": "Kongo",
    "photo": "https://freepngimg.com/thumb/pokemon/104765-and-pokemon-mythical-sword-shield.png"
})
print(response.text)

response_rename = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
   "pokemon_id": 5309,
    "name": "Bongo",
    "photo": "https://freepngimg.com/thumb/pokemon/104765-and-pokemon-mythical-sword-shield.png"
})
print(response_rename.text)

response_catch = requests.post('https://pokemonbattle.me:5000//trainers/add_pokeball', headers={'trainer_token' : token}, json={
   "pokemon_id": "5309"
})
print(response_catch.text)