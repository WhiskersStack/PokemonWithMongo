# Pokémon with DynamoDB

A simple Python project that fetches basic Pokémon data from the public **PokéAPI** and stores it in an **AWS DynamoDB** table. The codebase is intentionally minimal so you can focus on learning `boto3`, batch writes, and AWS credentials management.

## Features

- Retrieve random Pokémon metadata from PokéAPI.
- Insert or update items in DynamoDB using batched writes for speed.
- One‑command table creation (no manual console steps).
- Minimal external dependencies (`boto3` and `requests`).
- Clear, commented code so you can extend or repurpose it.

## Architecture (high‑level)

```
+--------------+       HTTPS        +----------------+
|              |  PokéAPI v2 REST   |                |
|  main.py     +------------------->+   PokéAPI      |
|              |                    |                |
+------+-------+                    +--------+-------+
       |                                     ^
       | boto3                               |
       v                                     |
+------+-------+                    +--------+-------+
|              |     DynamoDB      |                |
| DynamoUpdate +------------------->  DynamoDB      |
|              |    (batch put)    |  Table         |
+--------------+                    +----------------+
```

## Prerequisites

- **Python 3.10+**
- An AWS account with programmatic credentials that can create and write to DynamoDB
- Your chosen AWS Region (e.g. `us‑west‑2`)

## Quick Start

**Clone the repo :**

```bash
git clone https://github.com/<your‑handle>/PokemonWithDynamoDB.git
    cd PokemonWithDynamoDB
```

**Create & activate a virtual environment :**

```bash
python3 -m venv .venv
    source .venv/bin/activate
```

**Install dependencies :**

```bash
pip install boto3 requests
```

**Configure AWS credentials :**

```bash
aws configure --profile pokemon
    export AWS_PROFILE=pokemon
```

**Create the DynamoDB table (one‑time) :**

```bash
python3 core/ensure_table.py --table Pokemon --region us‑west‑2
```

**Seed the table with a demo Pokémon :**

```bash
python3 main.py
```

By default `main.py` picks a random ID (1‑1010) and writes the item. Pass `--pokemon-id 25` (for Pikachu) if you want something specific.

## Table Schema

| Attribute | Type | Key  | Example                                 |
| --------- | ---- | ---- | --------------------------------------- |
| id        | N    | HASH | `25`                                    |
| name      | S    |      | `pikachu`                               |
| height    | N    |      | `4`                                     |
| weight    | N    |      | `60`                                    |
| sprites   | S    |      | `https://raw.githubusercontent.com/...` |

Feel free to add extra attributes; DynamoDB is schemaless beyond the partition key.

## Project Layout

```
PokemonWithDynamoDB/
├── core/
│   ├── api.py            # PokéAPI helpers
│   ├── dynamoUpdate.py   # batch_write wrapper
│   └── ensure_table.py   # create table if absent
├── data/
│   └── pokemon_list.json # pre‑downloaded list
├── main.py               # entry point
└── README.md
```

## Common Issues

- \`\` – Credentials are missing or profile env var is wrong. Check `aws sts get-caller-identity`.
- \`\` – Make sure every item includes the partition key `id`.

## Roadmap

-

---

Happy catching!

