import requests
from typing import Dict, Optional
from random import randint
from pokemon import Pokemon, Statistics

POKEMON_ENDPOIT = "https://pokeapi.co/api/v2/pokemon/"


def get_random_pokemon() -> Dict[str, str]:
    pokeomn_id = 1
    pokemon = requests.get(f"{POKEMON_ENDPOIT}{pokeomn_id}")
    return pokemon


print(get_random_pokemon())
