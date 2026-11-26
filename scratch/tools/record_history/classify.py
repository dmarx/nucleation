# scratch/tools/record_history/classify.py
"""Classify the difference between two versions of one entry into events.

Kinds: created, status, title, prose (with line churn), relation_add,
relation_remove (forward fields only), meta (other front matter), and
mechanical (bytes changed, nothing above did: link repair, code
concretization, derived fields, version bookkeeping).
"""
from __future__ import annotations

import difflib

from record_history.entries import Schema, as_codes, normalize_body, normalize_text

PROSE_FIELDS = ("summary", "statement", "defeated_if", "promote_when", "status_note",
                "question", "definition")
BOOKKEEPING = {"version", "history", "formerly", "number", "date", "created"}

Version = tuple[dict, str]


def _churn(old: list[str], new: list[str]) -> tuple[int, int]:
    """Lines added and lines removed between two normalized versions."""
    added = removed = 0
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if tag != "equal":
            removed += i2 - i1
            added += j2 - j1
    return added, removed


def _prose_lines(fields: dict, body: str, alias: dict[str, str]) -> list[str]:
    lines = []
    for f in PROSE_FIELDS:
        if fields.get(f):
            lines.append(f"{f}: " + normalize_text(str(fields[f]), alias))
    return lines + normalize_body(body, alias)


def _relations(fields: dict, scheme: str, schema: Schema, alias: dict[str, str]) -> set[tuple[str, str]]:
    return {(f, c) for f in schema.forward_fields(scheme) for c in as_codes(fields.get(f), alias)}


def diff_entries(old: Version | None, new: Version | None, scheme: str,
                 schema: Schema, alias: dict[str, str]) -> list[dict]:
    """The events that turn version `old` into version `new` (None: absent)."""
    if new is None:
        return [{"kind": "deleted"}] if old is not None else []
    nf, nb = new
    events: list[dict] = []
    new_rel = _relations(nf, scheme, schema, alias)
    if old is None:
        events.append({"kind": "created", "status": str(nf.get("status", "")),
                       "lines": len(_prose_lines(nf, nb, alias))})
        events += [{"kind": "relation_add", "field": f, "target": c} for f, c in sorted(new_rel)]
        return events
    of, ob = old
    if str(of.get("status", "")) != str(nf.get("status", "")):
        events.append({"kind": "status", "old": str(of.get("status", "")), "new": str(nf.get("status", ""))})
    if normalize_text(str(of.get("title", "")), alias) != normalize_text(str(nf.get("title", "")), alias):
        events.append({"kind": "title"})
    added, removed = _churn(_prose_lines(of, ob, alias), _prose_lines(nf, nb, alias))
    if added or removed:  # removed == 0 is accretion (a dated note); else revision
        events.append({"kind": "prose", "churn": added + removed, "added": added, "removed": removed})
    old_rel = _relations(of, scheme, schema, alias)
    events += [{"kind": "relation_add", "field": f, "target": c} for f, c in sorted(new_rel - old_rel)]
    events += [{"kind": "relation_remove", "field": f, "target": c} for f, c in sorted(old_rel - new_rel)]
    skip = (BOOKKEEPING | set(PROSE_FIELDS) | {"status", "title"}
            | schema.forward_fields(scheme) | schema.derived_fields(scheme))
    meta = sorted(k for k in set(of) | set(nf) if k not in skip and of.get(k) != nf.get(k))
    if meta:
        events.append({"kind": "meta", "fields": meta})
    if not events and (of, ob) != (nf, nb):
        events.append({"kind": "mechanical"})
    return events
