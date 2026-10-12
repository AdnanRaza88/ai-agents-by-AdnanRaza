# SQL Query Agent

Natural language interface to SQLite databases. Generates and executes SQL safely (read-only by default).

## Features

- Demo e-commerce database included
- Interactive or single-question mode
- Read-only by default for safety
- Works with any SQLite file

## Tech Stack

- **Framework**: LangChain SQL Agent
- **LLM**: GPT-4o-mini
- **DB**: SQLite

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## How to Run

```bash
python agent.py
python agent.py --question "How many orders were placed in April?"
python agent.py --db mydb.sqlite --question "Show top customers by revenue"
```

---

**Created by Adnan Raza**
