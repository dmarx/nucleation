# record/promotion-audit/check.py
"""Check that the promotion audit's queue and its decision files agree (ADR-047).

The queue is hand-maintained, so it can drift from decisions/. This guards the
property instead of the list (DP-2): every decided candidate has a decision
file with the same disposition, every decision file is decided in the queue,
the per-wave counts are what the candidates say, and every batch file parses.

    python3 record/promotion-audit/check.py            # exits 1 on any problem
"""
from pathlib import Path

import fire
import yaml

DISPOSITIONS = {"promote", "narrow-and-promote", "split", "retain-proposed", "needs-correction", "defer"}
PROMOTION_PATHS = {"promote", "narrow-and-promote", "split"}
HERE = Path(__file__).parent


def problems(root: Path = HERE) -> list[str]:
    queue = yaml.safe_load((root / "queue.yaml").read_text())
    found: list[str] = []
    for p in sorted((root / "batches").glob("*.yaml")):
        try:
            yaml.safe_load(p.read_text())
        except yaml.YAMLError as e:
            found.append(f"batches/{p.name} does not parse: {str(e).splitlines()[0]}")
    files = {p.stem: yaml.safe_load(p.read_text()) for p in sorted((root / "decisions").glob("*.yaml"))}
    seen: set[str] = set()
    for c in queue.get("candidates") or []:
        code = c["code"]
        if code in seen:
            found.append(f"{code} appears twice in the queue")
        seen.add(code)
        if c.get("state") != "decided":
            continue
        d = files.get(code)
        if d is None:
            found.append(f"{code} is decided in the queue but has no decision file")
            continue
        if c.get("disposition") != d.get("disposition"):
            found.append(f"{code}: queue disposition {c.get('disposition')!r} != file {d.get('disposition')!r}")
    for code, d in files.items():
        if d.get("id") != code:
            found.append(f"decisions/{code}.yaml has id {d.get('id')!r}")
        if d.get("disposition") not in DISPOSITIONS:
            found.append(f"{code}: disposition {d.get('disposition')!r} is not one of {sorted(DISPOSITIONS)}")
        if not d.get("reviewed_revision"):
            found.append(f"{code}: no reviewed_revision")
        if not any(c["code"] == code and c.get("state") == "decided" for c in queue.get("candidates") or []):
            found.append(f"decisions/{code}.yaml is not decided in the queue")
    in_review = [c["code"] for c in queue.get("candidates") or [] if c.get("state") == "in_review"]
    if len(in_review) > 1:
        found.append(f"more than one candidate in_review: {in_review}")
    for w in queue.get("waves") or []:
        mine = [c for c in queue["candidates"] if c.get("wave") == w["wave"] and c.get("state") == "decided"]
        paths = sum(c.get("disposition") in PROMOTION_PATHS for c in mine)
        if (w.get("reviewed"), w.get("promotion_paths")) != (len(mine), paths):
            found.append(f"wave {w['wave']}: counts say {w.get('reviewed')}/{w.get('promotion_paths')}, "
                         f"candidates say {len(mine)}/{paths}")
    return found


def main(root: str = str(HERE)) -> None:
    found = problems(Path(root))
    for p in found:
        print(p)
    print(f"{len(found)} problem(s)")
    raise SystemExit(1 if found else 0)


if __name__ == "__main__":
    fire.Fire(main)
