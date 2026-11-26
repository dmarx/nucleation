# scratch/tools/record_history/handcheck.py
"""Draw LEAD-tmpn6mi2's hand-check samples (checks 2 and 4) and write, for
each, what a reader needs to judge it blind: the commit, the file and its
diff, but not the class the extraction gave.
"""
from __future__ import annotations

import random
import subprocess
from pathlib import Path

CLASSES = {"revised": ("statement", "body"), "relation_add": ("relation_add",),
           "status": ("status",), "note": ("note",), "mechanical": ("mechanical",)}


def stratified(rows: list[dict], k: int = 10, seed: int = 0) -> dict[str, list[dict]]:
    """k events per class, one per (commit, entry), drawn with a fixed seed."""
    rng = random.Random(seed)
    out = {}
    for name, kinds in CLASSES.items():
        seen, pool = set(), []
        for r in rows:
            key = (r["commit"], r["code"])
            if r["kind"] in kinds and key not in seen and (name == "mechanical" or not r["bot"]):
                seen.add(key)
                pool.append(r)
        out[name] = rng.sample(pool, min(k, len(pool)))
    return out


def path_at(repo: Path, commit: str, code: str) -> str | None:
    """The file of `code` (or a temporary alias) touched by `commit`."""
    out = subprocess.run(["git", "-C", str(repo), "show", "--name-only", "--format=", commit],
                         capture_output=True, text=True).stdout.split()
    hits = [p for p in out if p.endswith(f"/{code}.md")]
    return hits[0] if hits else None


def blind_sheet(repo: Path, samples: dict[str, list[dict]], alias: dict[str, str]) -> tuple[str, str]:
    """(sheet for the reader, key for the lead). Items are shuffled across classes."""
    items = [(name, r) for name, rs in samples.items() for r in rs]
    random.Random(1).shuffle(items)
    sheet, key = [], []
    olds = {}
    for a, c in alias.items():
        olds.setdefault(c, []).append(a)
    for i, (name, r) in enumerate(items, 1):
        path = None
        for code in [r["code"], *olds.get(r["code"], [])]:
            path = path_at(repo, r["commit"], code)
            if path:
                break
        diff = subprocess.run(["git", "-C", str(repo), "show", "--format=%H %an%n%s", r["commit"], "--",
                               path or "."], capture_output=True, text=True).stdout if path else "(file not found)"
        sheet.append(f"### Item {i}: {r['code']} in {r['commit'][:9]}\n\n```diff\n{diff[:6000]}\n```\n")
        detail = {k: r[k] for k in ("field", "target", "old", "new", "added", "removed") if r.get(k) not in (None, "")}
        key.append(f"{i}\t{name}\t{r['kind']}\t{r['code']}\t{r['commit'][:9]}\t{detail}")
    return "\n".join(sheet), "\n".join(key) + "\n"
