# GitHub Issue Triager

Analyzes a GitHub issue (from URL or title/body) and returns severity, category, suggested labels, assignee type, and triage notes.

## Features

- Fetch issue directly from GitHub URL (optional GITHUB_TOKEN)
- Structured JSON triage output
- Severity, priority score, category, labels, assignee recommendation
- Reproduction clarity and “needs more info” flags

## Tech Stack

- **Framework**: LangChain
- **LLM**: GPT-4o-mini
- **API**: GitHub REST (optional)

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## How to Run

```bash
python agent.py --title "Login fails on mobile Safari" --body "When I try to log in on iOS Safari the page freezes."
python agent.py --issue-url https://github.com/owner/repo/issues/123
```

---

**Created by Adnan Raza**
