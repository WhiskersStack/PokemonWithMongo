"""
core/storage.py
---------------
Helpers that keep ALL persistence behind the Flask + Mongo API.
Nothing on disk, no JSON cache.

Functions
~~~~~~~~~
load_pokemon_list() -> list[dict]
    Pulls your collection from the backend. Always returns a list
    (falls back to [] if the API is down).

check_duplicate(pokemon_id, data) -> bool
    True if that Pokémon ID is already in *data*.
"""

from __future__ import annotations

import time
import requests

from core.server_api import list_pokemon


# ────────────────────────────────────────────────────────────────────────── #
# Public helpers                                                            #
# ────────────────────────────────────────────────────────────────────────── #
def load_pokemon_list() -> list[dict]:
    """
    Retrieve the full collection from the Flask + Mongo backend.

    Returns
    -------
    list[dict]
        A list of Pokémon docs. Never None.
        If the API is unreachable, returns an empty list so callers
        can still iterate safely.
    """
    try:
        data = list_pokemon()                     # network call
        # Unwrap if the backend responds with {"pokemon": [...]}
        if isinstance(data, dict):
            data = data.get("pokemon", [])
        return data or []
    except requests.RequestException as err:
        print("⚠️  Could not reach the Pokémon API:", err)
        return []


def check_duplicate(pokemon_id: str | int, data: list[dict]) -> bool:
    """
    Check whether *pokemon_id* is already in *data*.

    Parameters
    ----------
    pokemon_id : str | int
        The ID we’re about to add.
    data : list[dict]
        Current collection (e.g. load_pokemon_list()).

    Returns
    -------
    bool
        True  – Pokémon already present  
        False – Pokémon not found
    """
    str_id = str(pokemon_id)
    for pokemon in data:
        if str(pokemon.get("id")) == str_id:
            print("\n~~~ You already have this Pokémon ~~~")
            time.sleep(1)
            print(f"\nName: {pokemon.get('name', '<unknown>')}")
            return True

    print("\nYou don't have this Pokémon :(")
    time.sleep(1)
    return False
