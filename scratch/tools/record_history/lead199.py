# scratch/tools/record_history/lead199.py
"""Export the event table in LEAD-199's formats, so its own analysis
(scratch/studies/lead-199/analyze.py) can rerun on this extraction:
LEAD-tmpn6mi2's check 1, reproducing CASE-307.

LEAD-199's population is the CLAIMs; its edges are inbound `rests_on` and
`grounds`; a change is substantive if title, role, warrant, defeated_if or
the body outside dated notes changed, and mechanical if the bot made it.
"""
from __future__ import annotations

from collections import defaultdict

from record_history.profile import REVISION

EDGE_FIELDS = ("rests_on", "grounds")


def to_lead199(rows: list[dict], tip: dict[str, set], status: dict[str, str],
               alias: dict[str, str]) -> tuple[list[dict], list[dict], dict[str, dict]]:
    """(revisions, edges, population) as LEAD-199's extract.py writes them."""
    claims = sorted(c for c in tip if c.startswith("CLAIM-"))
    population = {c: {"status": status.get(c, ""),
                      "aliases": sorted(a for a, v in alias.items() if v == c)} for c in claims}
    per: dict[tuple[str, str], list[dict]] = defaultdict(list)
    order: list[tuple[str, str]] = []
    n_claims: dict[str, set] = defaultdict(set)
    edges = []
    for r in rows:
        if r["kind"] in ("relation_add", "relation_remove") and r["field"] in EDGE_FIELDS \
                and r["target"].startswith("CLAIM-"):
            edges.append({"t": r["time"], "h": r["commit"], "src": r["code"], "tgt": r["target"],
                          "op": 1 if r["kind"] == "relation_add" else -1, "a": r["author"]})
        if r["scheme"] != "CLAIM":
            continue
        key = (r["commit"], r["code"])
        if key not in per:
            order.append(key)
        per[key].append(r)
        n_claims[r["commit"]].add(r["code"])
    revs = []
    for key in order:
        evs = per[key]
        first = evs[0]
        kinds = {e["kind"] for e in evs}
        if "created" in kinds:
            kind = "created"
        elif "deleted" in kinds:
            kind = "deleted"
        elif first["bot"]:
            kind = "mechanical"
        elif kinds & REVISION:
            kind = "substantive"
        elif kinds == {"mechanical"}:
            kind = "mechanical"
        else:
            kind = "nonsubstantive"
        revs.append({"t": first["time"], "h": first["commit"], "a": first["author"],
                     "s": first["subject"][:120], "claim": first["code"],
                     "n_claims_in_commit": len(n_claims[first["commit"]]), "kind": kind,
                     "status_change": "status" in kinds, "title_change": "statement" in kinds,
                     "lenient": kind == "substantive", "fields": sorted(kinds & REVISION)})
    return revs, edges, population
