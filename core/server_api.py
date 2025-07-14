"""
Thin client that the game uses to talk to your Flask service
running on the other EC2 instance (the one that keeps Mongo private).
"""

import os
import requests

# set this in ~/.bashrc or a .env file so you don’t hard-code IPs
BASE_URL = os.getenv("POKE_API_URL", "http://172.31.45.214:5000")


def save_pokemon(pokemon: dict) -> None:
    """
    POST one captured Pokémon to the Flask backend.
    The backend is expected to insert/update it in MongoDB.
    """
    r = requests.post(f"{BASE_URL}/pokemon", json=pokemon, timeout=5)
    r.raise_for_status()                 # surface problems fast


def list_pokemon() -> list[dict]:
    """
    Retrieve your whole collection from the backend.
    """
    r = requests.get(f"{BASE_URL}/pokemon", timeout=5)
    r.raise_for_status()
    return r.json()
