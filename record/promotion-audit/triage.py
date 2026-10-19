# record/promotion-audit/triage.py
"""Score Proposed, demonstrated CLAIMs by ADR-047's rubric, from metadata only.

Prints `score code evidence scope downstream cost risk proposed_deps`, best first.
The score orders review; it decides nothing. Run from the repository root,
on a freshly fetched origin/main:

    python3 record/promotion-audit/triage.py
"""
import re
from pathlib import Path

import fire
import yaml

ACTIVE = {"Active", "Read", None}  # None: a code outside this record, e.g. a LIT with another vocabulary


def load(root: Path) -> dict[Path, tuple[dict, str]]:
    docs = {}
    for p in root.rglob("*.md"):
        text = p.read_text()
        if not text.startswith("---"):
            continue
        try:
            fm = yaml.safe_load(text.split("---", 2)[1])
        except yaml.YAMLError:
            continue
        if isinstance(fm, dict):
            docs[p] = (fm, text)
    return docs


def score(fm: dict, cites: int, status: dict[str, str]) -> tuple[int, list[int], list[str]]:
    deps = list(fm.get("rests_on") or []) + list(fm.get("grounds") or [])
    inactive = [d for d in deps if status.get(d) not in ACTIVE]
    line = fm.get("line")
    line = line if isinstance(line, list) else [line]
    objections = len(fm.get("objected_by") or []) + len(fm.get("countered_by") or [])
    reliance = cites + 2 * len(fm.get("supports") or [])
    parts = [
        5 if not inactive else 4 if len(inactive) == 1 else 3,                   # evidence
        4 if line == ["formal-apparatus"] else 3 if "formal-apparatus" in line else 2,  # scope
        4 if reliance >= 20 else 3 if reliance >= 12 else 2 if reliance >= 6 else 1,    # downstream
        4 if not inactive else 2 if len(inactive) <= 2 else 1,                   # cost
        max(0, 3 - objections),                                                  # risk
    ]
    return sum(parts), parts, inactive


def main(record: str = "record") -> None:
    docs = load(Path(record))
    status = {p.stem: fm.get("status") for p, (fm, _) in docs.items()}
    cites: dict[str, int] = {}
    for p, (_, text) in docs.items():
        for code in set(re.findall(r"\b(?:CLAIM|THEORY)-\d{3}\b", text)) - {p.stem}:
            cites[code] = cites.get(code, 0) + 1
    rows = []
    for p, (fm, _) in docs.items():
        if p.parent.name == "claims.d" and fm.get("status") == "Proposed" and fm.get("warrant") == "demonstrated":
            total, parts, inactive = score(fm, cites.get(p.stem, 0), status)
            rows.append((total, p.stem, parts, inactive))
    for total, code, parts, inactive in sorted(rows, key=lambda r: (-r[0], r[1])):
        print(total, code, *parts, ",".join(inactive) or "-")


if __name__ == "__main__":
    fire.Fire(main)
