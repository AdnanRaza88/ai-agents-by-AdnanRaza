# Code Review Agent

Expert code reviewer that analyzes bugs, security issues, performance, style, and improvement opportunities.

## Features

- File or inline code input
- Structured review covering 5 dimensions
- Overall quality rating
- Language-agnostic (default Python)

## Tech Stack

- **Framework**: LangChain
- **LLM**: GPT-4o

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## How to Run

```bash
python agent.py --file path/to/code.py
python agent.py --code "def add(a, b): return a + b"
```

---

**Created by Adnan Raza**
