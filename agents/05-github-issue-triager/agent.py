"""
GitHub Issue Triager using LangChain.

Analyzes a GitHub issue and produces severity, category,
labels, and suggested assignee type.

Usage:
    python agent.py --title "Login fails on mobile Safari" --body "When I try..."
    python agent.py --issue-url https://github.com/owner/repo/issues/123
"""

import argparse
import json
import logging
import os
import re

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

TRIAGE_PROMPT = """You are a GitHub issue triager. Analyze the issue and return a JSON object with:
{
  "severity": "critical|high|medium|low",
  "category": "bug|feature|documentation|question|performance|security",
  "priority_score": 1-10,
  "labels": ["list", "of", "suggested", "labels"],
  "summary": "one sentence summary",
  "reproduction_clear": true/false,
  "assignee_type": "frontend|backend|devops|documentation|security|any",
  "needs_more_info": true/false,
  "triage_notes": "2-3 sentences of triager notes"
}
Return only valid JSON, no markdown."""


def parse_json_response(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)
    return json.loads(cleaned)


def triage_issue(title: str, body: str, labels: list[str] | None = None) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    issue_text = f"Title: {title}\n\nBody:\n{body}"
    if labels:
        issue_text += f"\n\nExisting labels: {', '.join(labels)}"

    messages = [
        SystemMessage(content=TRIAGE_PROMPT),
        HumanMessage(content=issue_text),
    ]

    response = llm.invoke(messages)
    return parse_json_response(response.content)


def fetch_github_issue(url: str) -> tuple[str, str, list]:
    import requests

    match = re.match(r"https://github.com/([^/]+)/([^/]+)/issues/(\d+)", url)
    if not match:
        raise ValueError(f"Invalid GitHub issue URL: {url}")

    owner, repo, issue_num = match.groups()
    api_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_num}"
    headers = {}
    if token := os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = f"token {token}"

    r = requests.get(api_url, headers=headers, timeout=10)
    r.raise_for_status()
    data = r.json()
    return data["title"], data.get("body", ""), [l["name"] for l in data.get("labels", [])]


def main() -> None:
    parser = argparse.ArgumentParser(description="GitHub Issue Triager")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--issue-url", help="GitHub issue URL")
    group.add_argument("--title", help="Issue title (use with --body)")
    parser.add_argument("--body", default="", help="Issue body text")
    args = parser.parse_args()

    if args.issue_url:
        print("\nFetching issue from GitHub...")
        title, body, labels = fetch_github_issue(args.issue_url)
    else:
        title, body, labels = args.title, args.body, []

    print(f"\nTriaging: {title}\n")
    result = triage_issue(title, body, labels)

    severity = result.get("severity", "medium")
    labels_out = result.get("labels", [])

    print("=" * 60)
    print("TRIAGE REPORT")
    print("=" * 60)
    print(f"Severity: {severity.upper()} (Priority: {result.get('priority_score', 'N/A')}/10)")
    print(f"Category: {result.get('category', 'N/A')}")
    print(f"Assignee: {result.get('assignee_type', 'any')} team")
    print(f"Labels: {', '.join(labels_out)}")
    print(f"Summary: {result.get('summary', 'N/A')}")
    print(f"Needs more info: {'Yes' if result.get('needs_more_info') else 'No'}")
    print(f"Reproduction clear: {'Yes' if result.get('reproduction_clear') else 'No'}")
    print(f"\nNotes: {result.get('triage_notes', 'N/A')}")


if __name__ == "__main__":
    main()
