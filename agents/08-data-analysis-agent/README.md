# Data Analysis Agent

Natural language interface to CSV/Excel data using LangChain’s pandas agent.

## Features

- Sample sales dataset included
- Interactive or single-question mode
- Requires explicit `--allow-dangerous-code` flag for safety

## Tech Stack

- **Framework**: LangChain Experimental
- **LLM**: GPT-4o
- **Data**: pandas

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## How to Run

```bash
python agent.py --allow-dangerous-code
python agent.py --file sales.csv --question "What is the monthly revenue trend?" --allow-dangerous-code
```

---

**Created by Adnan Raza**
