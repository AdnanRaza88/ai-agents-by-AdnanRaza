# Job Application Agent

CrewAI multi-agent system that analyzes a job description and candidate profile to produce a tailored cover letter, resume bullets, interview questions, and salary range estimate.

## Features

- Two specialized agents (Requirements Analyst + Career Writer)
- Sequential workflow
- Sample job + candidate included for quick demo

## Architecture

```
Job Analyst → Application Writer → Final Package
```

## Tech Stack

- **Framework**: CrewAI
- **LLM**: GPT-4o-mini

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## How to Run

```bash
python agent.py
python agent.py --job-desc "..." --candidate "..."
```

---

**Created by Adnan Raza**
