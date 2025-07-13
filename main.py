"""
    Pokemon Card Draw Game
    This is a simple game where users can draw random Pokemon cards.
    The game will display a random Pokemon card and check for duplicates.
    The game will continue until the user decides to stop.
"""

import random
from core.api import get_basic_pokemon_info
from core.display import welcome, ask_draw, draw_animation, say_goodbye
from core.storage import load_pokemon_list, check_duplicate
import metadata
from core.loadingGUI import loading_gui
import os

def main():
    """
    Main function to run the Pokemon Card Draw Game.
    It initializes the game, loads the Pokemon list, and handles user input.
    """
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Create JSON file if it doesn't exist
    if not os.path.exists("data/pokemon_list.json"):
        with open("data/pokemon_list.json", "w", encoding="utf-8") as f:
            f.write("[]")

    
    # Initialize loading GUI
    loading_gui()
    welcome()
    pokemon_list = load_pokemon_list()

    while True:
        if ask_draw():
            draw_animation()

            random_id = str(random.randint(1, metadata.POKEMON_COUNT))

            if check_duplicate(random_id, pokemon_list):
                continue

            get_basic_pokemon_info(random_id, pokemon_list)
        else:
            say_goodbye()
            break


if __name__ == "__main__":
    main()
