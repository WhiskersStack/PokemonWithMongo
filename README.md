# 🎮 Pokémon Card Draw Game

[![Python](https://img.shields.io/badge/Built%20With-Python-3776AB?logo=python)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/Interface-GUI-blueviolet)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A standalone desktop-based Pokémon card draw game written in Python. Users can draw cards, check for duplicates, and track history — all within a simple graphical user interface (GUI).

---

## ⚙️ Features

* 🃏 Draw random Pokémon cards
* 🚫 Duplicate-checking logic
* 💾 Local in-memory tracking
* 🖥️ Simple GUI interface (no web browser required)
* 🧠 Modular architecture with dedicated logic and display layers

---

## 🏗️ Project Structure

```bash
PokemonWithMongo/
├── core/                    # Core game and GUI modules
│   ├── api.py              # Pokémon data handling logic
│   ├── server_api.py       # External API or mock logic
│   ├── display.py          # Main display elements
│   ├── loadingGUI.py       # Startup/loading screen
│   └── storage.py          # Card tracking / duplicate detection
├── main.py                 # Application entry point
├── metadata.py             # Project-level metadata
├── global_var_init.sh      # Optional shell init script
└── .gitignore
```

---

## 🚀 How to Run

### 🧪 Requirements

* Python 3.10+
* No additional libraries required (standard library only)

### ▶️ Run Locally

```bash
python3 main.py
```

If using Unix/Linux:

```bash
chmod +x global_var_init.sh
./global_var_init.sh
python3 main.py
```

---

## 📚 Gameplay Flow

1. Welcome screen with loading animation
2. User clicks to draw a card
3. System selects a Pokémon and displays its name
4. Game checks for duplicates
5. Option to draw again or quit

---

## 🌱 Future Enhancements

* 🖼️ Add Pokémon card images
* 💾 Save drawn history to local file
* 🌐 Integrate real-time Pokémon data API
* 🏆 Add scoring and levels

---

## 📄 License

MIT © 2025

---

## 💬 Feedback

Open an issue or share ideas for improvements!
