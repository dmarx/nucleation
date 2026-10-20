# record/promotion-audit/triage_narrowing.py
"""Triage-008 digest: what each narrowing or as-is promotion dropped.

For every THEORY whose audit disposition is narrow-and-promote or promote,
collect the last Proposed title, the current title, the decision's
scope.excluded text, and the Proposed THEORY/CLAIMs and QUESTIONs already
linked to it. The kind of each dropped clause (1-4, see ADR-047 v4 draft)
is assigned by hand from this digest; the script only gathers.

    python record/promotion-audit/triage_narrowing.py digest out.json
    python record/promotion-audit/triage_narrowing.py plan triage-008.yaml
"""
import json
import re
import subprocess
from pathlib import Path

import fire
import yaml

ROOT = Path(__file__).resolve().parents[2]
REC = ROOT / "record"
DEC = REC / "promotion-audit" / "decisions"
DISPOSITIONS = ("narrow-and-promote", "promote")
CARRIER_KEYS = ("extends", "refines", "complements", "extended_by", "refined_by", "complemented_by")
FM = re.compile(r"\A---\n(.*?)\n---", re.S)


def frontmatter(text: str) -> dict:
    m = FM.match(text)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def last_proposed(path: Path, root: Path = ROOT) -> dict:
    """Frontmatter of the newest committed revision of `path` with status Proposed."""
    rel = str(path.relative_to(root))
    revs = subprocess.check_output(["git", "-C", str(root), "log", "--format=%H", "--", rel], text=True).split()
    for r in revs:
        try:
            t = subprocess.check_output(["git", "-C", str(root), "show", f"{r}:{rel}"], text=True, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            continue
        f = frontmatter(t)
        if f.get("status") == "Proposed":
            return f
    return {}


def links(fm: dict) -> set[str]:
    out = set()
    for k in CARRIER_KEYS:
        for v in fm.get(k) or []:
            if isinstance(v, str):
                out.add(v)
    return out


def carriers(code: str, docs: dict[str, dict]) -> list[str]:
    """Proposed THEORY/CLAIMs linked to `code` by a carrier relation, either direction."""
    mine = links(docs.get(code, {}))
    hits = []
    for k, f in docs.items():
        if k == code or k.split("-")[0] not in ("THEORY", "CLAIM") or f.get("status") != "Proposed":
            continue
        if code in links(f) or k in mine:
            hits.append(k)
    return sorted(hits)


def questions(code: str, docs: dict[str, dict]) -> list[str]:
    return sorted(k for k, f in docs.items() if k.startswith("QUESTION") and code in json.dumps(f, default=str))


def load_docs() -> dict[str, dict]:
    docs = {}
    for d in ("theory.d", "claims.d", "questions.d"):
        for p in (REC / d).glob("*.md"):
            docs[p.stem] = frontmatter(p.read_text())
    return docs


def digest(out: str, extra: str = ""):
    """Write the digest JSON. `extra`: comma-separated codes to include whatever their disposition."""
    docs = load_docs()
    rows = []
    want = set(filter(None, extra.split(",")))
    for f in sorted(DEC.glob("THEORY-*.yaml")):
        d = yaml.safe_load(f.read_text()) or {}
        if d.get("disposition") not in DISPOSITIONS and f.stem not in want:
            continue
        code = f.stem
        cur = docs.get(code, {})
        old = last_proposed(REC / "theory.d" / f"{code}.md")
        scope = d.get("scope") or {}
        rows.append({
            "code": code, "disposition": d.get("disposition"), "status": cur.get("status"),
            "old_title": old.get("title", ""), "new_title": cur.get("title", ""),
            "excluded": " ".join(str(scope.get("excluded", "")).split()),
            "old_promote_when": " ".join(str(old.get("promote_when", "")).split()),
            "source": cur.get("source") or [], "carriers": carriers(code, docs), "questions": questions(code, docs),
        })
    Path(out).write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(len(rows), "rows")


_TEXTS: dict[Path, list[tuple[str, str]]] = {}


def cited(code: str, root: Path = REC) -> int:
    """Number of record files (Markdown, so not promotion-audit/'s YAML) that name `code`."""
    if root not in _TEXTS:
        _TEXTS[root] = [(p.stem, p.read_text()) for p in root.rglob("*.md")]
    pat = re.compile(rf"\b{re.escape(code)}\b")
    return sum(1 for stem, text in _TEXTS[root] if stem != code and pat.search(text))


def summarize(entries: dict[str, list[dict]], cites: dict[str, int], size: int = 5) -> dict:
    """Counts by kind, and the filing order: codes with a kind-1 clause first, then kind-2 only,
    most-cited first within each, clauses already carried by an existing entry left out."""
    counts = {k: 0 for k in (1, 2, 3, 4)}
    need: dict[str, int] = {}
    for code, clauses in entries.items():
        for c in clauses:
            counts[c["kind"]] += 1
            if c["kind"] in (1, 2) and not c.get("existing_carrier"):
                need[code] = min(need.get(code, 9), c["kind"])
    order = sorted(need, key=lambda c: (need[c], -cites.get(c, 0), c))
    batches = [order[i:i + size] for i in range(0, len(order), size)]
    return {"clauses_by_kind": counts, "codes_to_file": len(order),
            "kind1_codes": sum(1 for c in order if need[c] == 1), "kind2_only_codes": sum(1 for c in order if need[c] == 2),
            "batches": [{"batch": i + 1, "codes": b} for i, b in enumerate(batches)]}


def plan(path: str):
    """Recompute triage-008.yaml's summary block from its entries, with citation counts."""
    p = Path(path)
    doc = yaml.safe_load(p.read_text())
    cites = {code: cited(code) for code in doc["entries"]}
    for code, n in cites.items():
        doc["cited_by_files"][code] = n
    doc["summary"] = summarize(doc["entries"], cites)
    p.write_text(yaml.safe_dump(doc, sort_keys=False, width=100, allow_unicode=True))
    print(doc["summary"]["clauses_by_kind"], doc["summary"]["codes_to_file"], "codes to file")


if __name__ == "__main__":
    fire.Fire({"digest": digest, "plan": plan})
