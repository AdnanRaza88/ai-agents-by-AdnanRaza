# AI Agents by Adnan Raza

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.3-green)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2-purple)
![CrewAI](https://img.shields.io/badge/CrewAI-0.x-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Production-ready AI Agents built with LangChain, LangGraph, and CrewAI**

A curated portfolio of 10 high-quality, independently runnable AI agents demonstrating multi-agent systems, RAG, tool use, structured output, and real-world workflows.

Built by **Adnan Raza** — AI Engineer specializing in Generative AI, multi-agent systems, RAG pipelines, and AI automation.

---

## Agents Overview

| # | Agent | Description | Framework |
|---|-------|-------------|-----------|
| 01 | [Smart Support Agent](agents/01-smart-support-agent/) | RAG-powered customer support with automatic escalation | LangGraph + FAISS |
| 02 | [Competitive Intelligence Agent](agents/02-competitive-intelligence-agent/) | Multi-step competitor analysis and strategic report | LangGraph |
| 03 | [Multi-Agent Debate System](agents/03-multi-agent-debate-system/) | Structured debate between opposing agents with judge | LangChain |
| 04 | [Web Research Agent](agents/04-web-research-agent/) | Web search + synthesis into structured research reports | LangGraph + Tavily |
| 05 | [GitHub Issue Triager](agents/05-github-issue-triager/) | Severity, category, labels, and assignee suggestions | LangChain |
| 06 | [Code Review Agent](agents/06-code-review-agent/) | Deep code review covering bugs, security, style, performance | LangChain |
| 07 | [SQL Query Agent](agents/07-sql-query-agent/) | Natural language to SQL with demo e-commerce database | LangChain |
| 08 | [Data Analysis Agent](agents/08-data-analysis-agent/) | Pandas-powered natural language data analysis | LangChain |
| 09 | [Stock Research Agent](agents/09-stock-research-agent/) | Yahoo Finance data + AI investment thesis | LangChain + yfinance |
| 10 | [Job Application Agent](agents/10-job-application-agent/) | Tailored cover letter, resume bullets, interview prep | CrewAI |

---

## Tech Stack

- **Frameworks**: LangChain, LangGraph, CrewAI
- **LLMs**: OpenAI GPT-4o / GPT-4o-mini
- **Tools**: Tavily Search, FAISS, yfinance, pandas, SQLite
- **Language**: Python 3.10+

---

## Quick Start

```bash
git clone https://github.com/AdnanRaza88/ai-agents-by-AdnanRaza.git
cd ai-agents-by-AdnanRaza

# Pick any agent
cd agents/01-smart-support-agent
pip install -r requirements.txt
cp .env.example .env   # add your OPENAI_API_KEY
python agent.py
```

Each agent is self-contained and can be run independently.

---

## Project Structure

```
ai-agents-by-AdnanRaza/
├── README.md
├── LICENSE
├── .gitignore
└── agents/
    ├── 01-smart-support-agent/
    ├── 02-competitive-intelligence-agent/
    ├── 03-multi-agent-debate-system/
    ├── 04-web-research-agent/
    ├── 05-github-issue-triager/
    ├── 06-code-review-agent/
    ├── 07-sql-query-agent/
    ├── 08-data-analysis-agent/
    ├── 09-stock-research-agent/
    └── 10-job-application-agent/
```

---

## License

MIT License — see [LICENSE](LICENSE)

---

**Built with ❤️ by Adnan Raza**
