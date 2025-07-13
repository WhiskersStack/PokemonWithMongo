import time
from core.server_api import list_pokemon
import requests

def load_pokemon_list():
    try:
        my_pokemon_list = list_pokemon()            # pulls from Mongo
    except requests.RequestException as err:
        print("Could not reach the Pokémon API:", err)
        my_pokemon_list = []                        # start empty if offline


def check_duplicate(pokemon_id, data):
    """
        Check if a Pokémon with the given ID already exists in the list.
    """
    for pokemon in data:
        if str(pokemon["id"]) == pokemon_id:
            print("\n~~~ You already have this Pokémon ~~~")
            time.sleep(1)
            print(f"\nName: {pokemon['name']}")
            return True
    print("\nYou don't have this Pokémon :(")
    time.sleep(1)
    return False
