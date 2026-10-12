# Competitive Intelligence Agent

Multi-step LangGraph agent that identifies competitors, analyzes strengths/weaknesses, and produces a strategic competitive report.

## Features

- Automatic competitor identification for any company + industry
- Structured analysis of each competitor (products, strengths, weaknesses, pricing)
- Full strategic report with recommendations and threat assessment
- Configurable company and industry via CLI

## Architecture

```
Identify Competitors → Analyze Each → Generate Strategic Report
```

## Tech Stack

- **Framework**: LangGraph
- **LLM**: GPT-4o / GPT-4o-mini

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## How to Run

```bash
python agent.py --company "Notion" --industry "productivity software"
python agent.py --company "Stripe" --industry "fintech payments"
```

## Example Output

The agent returns a structured report containing:
- Executive Summary
- Competitive Landscape
- Market Gaps & Opportunities
- Strategic Recommendations
- Threat Assessment

---

**Created by Adnan Raza**
