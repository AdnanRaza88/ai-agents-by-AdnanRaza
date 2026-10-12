# Multi-Agent Debate System

Two specialized AI agents debate a topic from opposing sides. An impartial judge evaluates the arguments and declares a winner with a structured verdict.

## Features

- Configurable number of debate rounds (1–4)
- Distinct agent personas with domain expertise
- Evidence-based, persuasive argumentation
- Judge produces winner, scores, strongest arguments, and synthesis

## Architecture

```
Pro Agent ↔ Con Agent  (multiple rounds)
          ↓
     Judge Verdict
```

## Tech Stack

- **Framework**: LangChain
- **LLM**: GPT-4o-mini (debaters) + GPT-4o (judge)

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## How to Run

```bash
python agent.py --topic "AI will eliminate more jobs than it creates"
python agent.py --topic "Remote work is better than office work" --rounds 3
```

---

**Created by Adnan Raza**
