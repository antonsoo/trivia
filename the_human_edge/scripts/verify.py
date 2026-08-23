#!/usr/bin/env python3
"""Validate The Human Edge question bank and standalone build."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "questions.json"
HTML_PATH = ROOT / "index.html"
SCRIPT_RE = re.compile(
    r'<script\s+id="questionData"\s+type="application/json">(.*?)</script>',
    re.DOTALL,
)
DIFFICULTIES = {"Challenging", "Hard", "Very Hard"}
REQUIRED_QUESTION_FIELDS = {
    "id",
    "category",
    "difficulty",
    "points",
    "question",
    "answer",
    "explanation",
    "hints",
    "takeaway",
    "evidence",
    "sources",
}


class IdCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key == "id" and value:
                self.ids.append(value)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate(data: dict[str, Any], html: str) -> list[str]:
    errors: list[str] = []
    categories = data.get("categories", [])
    questions = data.get("questions", [])
    sources = data.get("sources", {})

    category_ids = [c.get("id") for c in categories]
    if len(category_ids) != len(set(category_ids)):
        fail(errors, "Category IDs are not unique.")
    if len(categories) != 12:
        fail(errors, f"Expected 12 categories; found {len(categories)}.")

    question_ids = [q.get("id") for q in questions]
    if len(question_ids) != len(set(question_ids)):
        fail(errors, "Question IDs are not unique.")
    if len(questions) != 120:
        fail(errors, f"Expected 120 questions; found {len(questions)}.")

    numbers = [q.get("number") for q in questions]
    if sorted(numbers) != list(range(1, len(questions) + 1)):
        fail(errors, "Question numbers must be consecutive from 1 through the bank size.")

    for index, question in enumerate(questions, 1):
        qid = question.get("id", f"question #{index}")
        missing = REQUIRED_QUESTION_FIELDS - set(question)
        if missing:
            fail(errors, f"{qid}: missing fields {sorted(missing)}.")
        if question.get("category") not in category_ids:
            fail(errors, f"{qid}: unknown category {question.get('category')!r}.")
        if question.get("difficulty") not in DIFFICULTIES:
            fail(errors, f"{qid}: invalid difficulty {question.get('difficulty')!r}.")
        if not isinstance(question.get("points"), int) or question.get("points", 0) < 2:
            fail(errors, f"{qid}: points must be an integer of at least 2.")
        hints = question.get("hints")
        if not isinstance(hints, list) or len(hints) != 3 or not all(str(h).strip() for h in hints):
            fail(errors, f"{qid}: exactly three non-empty hints are required.")
        for field in ("question", "answer", "explanation", "takeaway", "evidence"):
            if not str(question.get(field, "")).strip():
                fail(errors, f"{qid}: {field} must be non-empty.")
        refs = question.get("sources")
        if not isinstance(refs, list) or not refs:
            fail(errors, f"{qid}: at least one source reference is required.")
        else:
            for source_id in refs:
                if source_id not in sources:
                    fail(errors, f"{qid}: unknown source reference {source_id!r}.")

    match = SCRIPT_RE.search(html)
    if not match:
        fail(errors, "index.html is missing its embedded questionData script.")
    else:
        try:
            embedded = json.loads(match.group(1).replace("<\\/script>", "</script>"))
        except json.JSONDecodeError as exc:
            fail(errors, f"Embedded questionData is invalid JSON: {exc}.")
        else:
            if embedded != data:
                fail(errors, "Embedded data differs from data/questions.json; run sync_questions.py.")

    parser = IdCollector()
    parser.feed(html)
    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        fail(errors, f"Duplicate HTML IDs: {duplicates}.")

    if "prefers-reduced-motion" not in html:
        fail(errors, "Reduced-motion handling is missing from index.html.")
    if "<dialog" not in html:
        fail(errors, "Expected native dialog elements in index.html.")
    if 'class="skip-link"' not in html:
        fail(errors, "Expected a keyboard skip link in index.html.")

    return errors


def main() -> None:
    try:
        data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        html = HTML_PATH.read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Could not read project files: {exc}") from exc

    errors = validate(data, html)
    if errors:
        print("Verification failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        raise SystemExit(1)

    print(
        "Verification passed: "
        f"{len(data['questions'])} questions, "
        f"{len(data['categories'])} categories, "
        f"{sum(len(q['hints']) for q in data['questions'])} hints, "
        f"{len(data['sources'])} sources, and one synchronized standalone build."
    )


if __name__ == "__main__":
    main()
