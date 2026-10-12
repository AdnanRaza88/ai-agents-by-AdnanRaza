# Stock Research Agent

Fetches live market data via Yahoo Finance and produces an AI-generated investment thesis.

## Features

- Price, market cap, valuation ratios, analyst ratings
- AI Investment Thesis, Strengths, Risks, Verdict

## Tech Stack

- **Framework**: LangChain
- **Data**: yfinance
- **LLM**: GPT-4o-mini

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## How to Run

```bash
python agent.py --ticker AAPL
python agent.py --ticker NVDA
```

---

**Created by Adnan Raza**
