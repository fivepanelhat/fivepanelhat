#!/usr/bin/env python3
"""Score Coastal Alpine projects against the funding tracker.

Usage:
  python score_fit.py --project "SoilGuard offline edge nutrient control"
  python score_fit.py --project "Weaver multi-tenant RAG" --min-score 70
  python score_fit.py --list

Read-only regarding applications: prints recommendations only.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "tracker.csv"

THEME_ALIASES = {
    "maori": ["maori", "māori", "iwi", "hapu", "hapū", "whenua", "te mana", "indigenous"],
    "agritech": ["agri", "farm", "soil", "water", "crop", "hive", "bee", "wasp", "pasture", "hort", "primary"],
    "deeptech": ["deeptech", "r&d", "research", "npu", "hailo", "inference", "model", "llm", "yolo"],
    "sovereign-ai": ["sovereign", "offline", "edge", "local-first", "on-device", "residency", "airgap"],
    "biosecurity": ["biosecurity", "wasp", "bee", "pest", "sentinel"],
    "water": ["water", "turbidity", "runoff", "aquaguard", "sediment"],
    "soil": ["soil", "npk", "nutrient", "soilguard"],
    "ai": ["ai", "agent", "rag", "ollama", "aether", "weaver"],
    "capacity": ["intern", "student", "graduate", "phd", "masters", "career", "experience"],
    "edge": ["rpi", "raspberry", "firmware", "mqtt", "esp32", "hailo"],
}


def load_rows() -> list[dict[str, str]]:
    if not CSV_PATH.exists():
        print(f"ERROR: missing {CSV_PATH}", file=sys.stderr)
        sys.exit(1)
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def project_themes(text: str) -> set[str]:
    t = text.lower()
    found: set[str] = set()
    for theme, keys in THEME_ALIASES.items():
        if any(k in t for k in keys):
            found.add(theme)
    # always consider deeptech/ai lightly if edge stack nouns present
    if re.search(r"\b(rpi|hailo|ollama|langgraph|mqtt)\b", t):
        found.update({"edge", "deeptech", "sovereign-ai"})
    return found


def score_row(row: dict[str, str], proj_themes: set[str], project: str) -> tuple[int, list[str]]:
    status = (row.get("status") or "").lower()
    if status in {"closed", "paused", "declined"}:
        return 0, [f"status={status}"]

    reasons: list[str] = []
    score = 0

    tags = {t.strip().lower() for t in (row.get("themes") or "").split(";") if t.strip()}
    overlap = proj_themes & tags
    # also soft match: agritech project vs primary tag
    if "agritech" in proj_themes and "primary" in tags:
        overlap.add("primary")
    theme_pts = min(45, 15 * len(overlap))
    score += theme_pts
    if overlap:
        reasons.append(f"theme_overlap={sorted(overlap)} (+{theme_pts})")

    # baseline from tracker expert fit (anchors ranking)
    try:
        base = int(float(row.get("fit_score") or 0))
    except ValueError:
        base = 0
    # blend: 40% expert prior, 60% project overlap dynamics
    # recompute as expert prior boost
    prior = int(base * 0.35)
    score += prior
    reasons.append(f"expert_prior_boost=+{prior} (tracker={base})")

    # status boosts
    if status == "open":
        score += 10
        reasons.append("status=open (+10)")
    elif status == "opens_soon":
        score += 6
        reasons.append("status=opens_soon (+6)")
    elif status in {"watch", "researching"}:
        score += 2
        reasons.append(f"status={status} (+2)")

    p = project.lower()
    if any(x in p for x in ("maori", "māori", "iwi", "whenua")) and "maori" in tags:
        score += 8
        reasons.append("explicit maori pathway (+8)")
    if any(x in p for x in ("offline", "sovereign", "edge", "local")) and (
        "sovereign-ai" in tags or "edge" in tags
    ):
        score += 8
        reasons.append("sovereign/edge alignment (+8)")

    # penalties
    if "maori" in tags and not any(x in p for x in ("maori", "māori", "iwi", "whenua", "partner")):
        score -= 12
        reasons.append("maori-tagged fund without partnership language (-12)")

    score = max(0, min(100, score))
    return score, reasons


def band(score: int) -> str:
    if score >= 85:
        return "pursue_now"
    if score >= 70:
        return "pursue_with_gaps"
    if score >= 55:
        return "watch_or_partner"
    return "skip"


def main() -> None:
    ap = argparse.ArgumentParser(description="Score project fit against funding tracker")
    ap.add_argument("--project", type=str, help="Project description")
    ap.add_argument("--min-score", type=int, default=0)
    ap.add_argument("--list", action="store_true", help="List tracker rows")
    args = ap.parse_args()

    rows = load_rows()
    if args.list or not args.project:
        print(f"{'ID':<12} {'Status':<12} {'Fit':>4}  Name")
        for r in rows:
            print(f"{r['id']:<12} {r['status']:<12} {r['fit_score']:>4}  {r['name']}")
        if not args.project:
            print("\nProvide --project to score.")
            return

    themes = project_themes(args.project)
    print(f"Project: {args.project}")
    print(f"Detected themes: {sorted(themes) or ['(none)']}")
    print()

    scored: list[tuple[int, dict[str, str], list[str]]] = []
    for r in rows:
        s, reasons = score_row(r, themes, args.project)
        if s >= args.min_score:
            scored.append((s, r, reasons))
    scored.sort(key=lambda x: (-x[0], x[1].get("id", "")))

    print(f"{'Score':>5}  {'Band':<18} {'ID':<12} Name")
    print("-" * 72)
    for s, r, reasons in scored:
        print(f"{s:>5}  {band(s):<18} {r['id']:<12} {r['name']}")
        print(f"       next: {r.get('next_action', '')}")
        print(f"       why: {'; '.join(reasons)}")
        print()

    if scored:
        top = scored[0]
        print(f"Top recommendation: {top[1]['id']} — {top[1]['name']} (score {top[0]})")
        print("HITL: human must verify eligibility and funder status before applying.")


if __name__ == "__main__":
    main()
