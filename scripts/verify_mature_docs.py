#!/usr/bin/env python3
"""Fail if public docs claim a maturity the status table does not support."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED = {"Prototype", "Architecture", "Commercial/private"}
BANNED = (
    "SOC 2 certified",
    "SOC 2 Type II certified",
    "Algorithm Charter signatory",
    "Crown endorsement",
    "we are certified",
    "production deployment",
    "in production",
)
NEGATION = ("not", "no ", "never", "must not", "without ", "is not")


def status_rows(text: str) -> list[tuple[str, str]]:
    rows = []
    for line in text.splitlines():
        if not line.startswith("|") or "---" in line or "Component" in line or "Marker" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        rows.append((cells[0], cells[1]))
    return rows


def banned_hits(path: Path, text: str) -> list[str]:
    hits = []
    low = text.lower()
    for phrase in BANNED:
        start = 0
        needle = phrase.lower()
        while True:
            idx = low.find(needle, start)
            if idx < 0:
                break
            window = low[max(0, idx - 80): idx + len(needle)]
            if not any(token in window for token in NEGATION):
                hits.append(f"{path}: unnegated claim {phrase!r}")
            start = idx + len(needle)
    return hits


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    status = root / "COMPONENT_STATUS.md"
    validation = root / "VALIDATION.md"
    if not validation.is_file():
        problems.append("VALIDATION.md missing")
    else:
        v = validation.read_text(encoding="utf-8")
        if "GitHub popularity will not substitute" not in v:
            problems.append("VALIDATION.md missing the popularity denial")
        if "Not claimed" not in v:
            problems.append("VALIDATION.md must keep customer, pilot, and partnership as not claimed")
    problems: list[str] = []
    if not status.is_file():
        problems.append("COMPONENT_STATUS.md missing")
    else:
        text = status.read_text(encoding="utf-8")
        if "Nothing in this table is Production or Pilot." not in text:
            problems.append("status page missing the no-production sentence")
        for name, label in status_rows(text):
            if name in {"Production", "Pilot", "Prototype", "Architecture", "Commercial/private"}:
                continue
            if label not in ALLOWED:
                problems.append(f"component {name!r} has label {label!r}; allowed {sorted(ALLOWED)}")
    for path in root.rglob("*.md"):
        if any(part.startswith(".") for part in path.parts):
            continue
        problems.extend(banned_hits(path, path.read_text(encoding="utf-8", errors="replace")))
    if problems:
        print("\n".join(problems))
        raise SystemExit(1)
    print("mature-docs ok")


if __name__ == "__main__":
    main()
