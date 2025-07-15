# 🃏 Pokémon Card Draw Game

[![Python](https://img.shields.io/badge/Built%20With-Python-3776AB?logo=python)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/Interface-GUI-blueviolet)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, standalone Pokémon card draw game built with Python. Users can randomly draw Pokémon cards, avoid duplicates, and track drawn cards — all through a simple, clean desktop GUI.

---

## ✨ Key Features

* 🎴 Draw a random Pokémon card
* ❌ Automatically avoids duplicates
* 💾 Tracks drawn cards in-memory
* 🖥️ Lightweight GUI (no browser needed)
* 🧩 Modular design: separate logic, display, and data handling

---

## 🗂️ Project Structure

```bash
PokemonWithMongo/
├── core/                    # Game logic and GUI modules
│   ├── api.py              # Pokémon data logic
│   ├── server_api.py       # Optional external/mock API logic
│   ├── display.py          # Main visual interface
│   ├── loadingGUI.py       # Splash/loading animations
│   └── storage.py          # Duplicate check + card memory
├── main.py                 # Application launcher
├── metadata.py             # Game metadata and info
├── global_var_init.sh      # Optional shell initialization script
└── .gitignore
```

---

## 🚀 Getting Started

### ✅ Requirements

* Python 3.10+
* No external libraries needed (uses standard library only)

### ▶️ Run the Game

```bash
python3 main.py
```

For Unix/Linux users:

```bash
chmod +x global_var_init.sh
./global_var_init.sh
python3 main.py
```

---

## 🎮 Gameplay Flow

1. Launch the game (welcome screen appears)
2. Click to draw a Pokémon card
3. The game displays a random Pokémon name
4. If it's a duplicate, you're notified
5. Draw again or exit

---

## 🌟 Planned Improvements

* 🖼️ Display official Pokémon card images
* 💾 Save drawn history to file for later sessions
* 🌐 Integrate real Pokémon data from an API
* 🏆 Add scoring, streaks, or level-ups

---

## 📄 License

MIT License © 2025

---

## 💬 Feedback & Contributions

Found a bug or have a feature idea? Open an issue or submit a pull request!

Thanks for playing! 🎉
