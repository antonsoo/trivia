#!/usr/bin/env python3
"""Embed data/questions.json into the standalone index.html build."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "questions.json"
HTML_PATH = ROOT / "index.html"
SCRIPT_RE = re.compile(
    r'(<script\s+id="questionData"\s+type="application/json">)(.*?)(</script>)',
    re.DOTALL,
)


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    blob = blob.replace("</script>", "<\\/script>")

    html = HTML_PATH.read_text(encoding="utf-8")
    updated, replacements = SCRIPT_RE.subn(
        lambda match: f"{match.group(1)}{blob}{match.group(3)}", html, count=1
    )
    if replacements != 1:
        raise SystemExit("Could not find exactly one embedded questionData script in index.html")

    HTML_PATH.write_text(updated, encoding="utf-8")
    print(
        f"Embedded {len(data.get('questions', []))} questions and "
        f"{len(data.get('sources', {}))} sources into {HTML_PATH.relative_to(ROOT)}."
    )


if __name__ == "__main__":
    main()
