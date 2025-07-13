import requests
from core.display import show_pokemon
import metadata
from core import server_api


def get_basic_pokemon_info(pokemon_id, my_pokemon_list):
    """
        Fetch basic Pokémon information from the API and display it.    
    """
    url = metadata.BASE_URL + metadata.ENDPOINTS["pokemon"] + pokemon_id
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        print("Error:", response.status_code)
        return

    data = response.json()

    pokemon_info = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
    }

    show_pokemon(pokemon_info)
    my_pokemon_list.append(pokemon_info)




    server_api.save_pokemon(pokemon_info)

    print(f"Pokémon {pokemon_info['name']} added to your collection.")
