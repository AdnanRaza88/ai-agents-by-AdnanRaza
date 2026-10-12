# Web Research Agent

Searches the web via Tavily, then synthesizes results into a clear, structured research report using LangGraph.

## Features

- Real-time web search (Tavily)
- Structured report: Summary, Key Findings, Sources
- Configurable research query via CLI

## Architecture

```
Query → Tavily Search → Synthesize Report
```

## Tech Stack

- **Framework**: LangGraph
- **Search**: Tavily
- **LLM**: GPT-4o-mini

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add OPENAI_API_KEY and TAVILY_API_KEY
```

## How to Run

```bash
python agent.py --query "latest advances in quantum computing"
```

---

**Created by Adnan Raza**
