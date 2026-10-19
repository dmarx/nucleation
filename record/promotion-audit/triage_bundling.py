# record/promotion-audit/triage_bundling.py
"""Score Proposed mathematics THEORYs by bundling, the wave-2 predictor batch 009 found.

A THEORY bundles when its promote_when asks for more than its title claims, so a
proved core can be promoted apart from the rest. Three points, from metadata only:

  extends   the promote_when asks for something of another kind than a proof
            check: a general or arbitrary case, an experiment, trained networks,
            people, a population limit, or a second source
  compound  the title joins clauses of different kinds ("…, so …", "; ", " and ")
  read      a source LIT has a NOTE with status Read

Ties are broken by the number of claims the THEORY supports. The score orders
review; it decides nothing (ADR-047). Run from the repository root on a freshly
fetched origin/main, skipping codes already in the queue:

    python3 record/promotion-audit/triage_bundling.py --skip_queue=record/promotion-audit/queue.yaml
"""
import re
from pathlib import Path

import fire
import yaml

EXTENSION = re.compile(
    r"\b(general|arbitrary|infinite|experiment\w*|empirical|trained|network\w*|human\w*|"
    r"people|population|in practice|second (?:source|proof)|independent\w*|beyond|extension)\b",
    re.IGNORECASE,
)
COMPOUND = re.compile(r", so |; | and |: ")


def frontmatter(path: Path) -> dict | None:
    text = path.read_text()
    if not text.startswith("---"):
        return None
    try:
        fm = yaml.safe_load(text.split("---", 2)[1])
    except yaml.YAMLError:
        return None
    return fm if isinstance(fm, dict) else None


def score(fm: dict, read_lits: set[str]) -> tuple[int, dict[str, int]]:
    """Return (total, parts) for one THEORY's frontmatter."""
    parts = {
        "extends": int(bool(EXTENSION.search(str(fm.get("promote_when") or "")))),
        "compound": int(bool(COMPOUND.search(str(fm.get("title") or "")))),
        "read": int(any(lit in read_lits for lit in fm.get("source") or [])),
    }
    return sum(parts.values()), parts


def read_sources(record: Path) -> set[str]:
    lits = set()
    for p in (record / "notes.d").glob("NOTE-*.md"):
        fm = frontmatter(p)
        if fm and fm.get("status") == "Read" and fm.get("paper"):
            lits.add(str(fm["paper"]))
    return lits


def main(record: str = "record", skip_queue: str = "", top: int = 20) -> None:
    root = Path(record)
    skip: set[str] = set()
    if skip_queue:
        q = yaml.safe_load(Path(skip_queue).read_text())
        skip = {c["code"] for c in q.get("candidates") or []} | {r["code"] for r in q.get("requeue") or []}
    read_lits = read_sources(root)
    rows = []
    for p in sorted((root / "theory.d").glob("THEORY-*.md")):
        fm = frontmatter(p)
        if not fm or fm.get("status") != "Proposed" or "mathematics" not in (fm.get("tags") or []):
            continue
        if p.stem in skip:
            continue
        total, parts = score(fm, read_lits)
        rows.append((total, len(fm.get("supports") or []), p.stem, parts))
    for total, sup, code, parts in sorted(rows, key=lambda r: (-r[0], -r[1], r[2]))[:top]:
        print(total, code, parts["extends"], parts["compound"], parts["read"], sup)


if __name__ == "__main__":
    fire.Fire(main)
