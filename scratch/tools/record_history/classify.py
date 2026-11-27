# scratch/tools/record_history/classify.py
"""Classify the difference between two versions of one entry into events.

The classes are LEAD-tmpn6mi2's, with LEAD-199's normalization (codes
masked in prose, since which code is cited is a relation; HTML comments and
the H1 dropped; link targets stripped):

- created, deleted
- statement: `title` or `statement` changed
- body: the body outside `## Note of ...` sections changed (lines added/removed)
- defeater: `defeated_if` changed
- note: a dated-note section added or changed
- summary: `summary`, `promote_when`, `status_note` and other prose fields
- role: `role` or `warrant` changed from a value (absent to present is a
  backfill, counted under meta)
- status: old and new kept
- relation_add, relation_remove: forward reference fields only
- meta: other front matter
- mechanical: bytes changed and nothing above did
"""
from __future__ import annotations

import difflib
import re

from record_history.entries import CODE_RE, Schema, as_codes, normalize_text

STATEMENT = ("title", "statement")
SUMMARY = ("summary", "promote_when", "status_note", "question", "definition")
ROLE = ("role", "warrant")
BOOKKEEPING = {"version", "history", "formerly", "number", "date", "created"}
_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
_CITE_PAREN_RE = re.compile(r"\(\s*(?:@CODE[\s,;]*(?:and\s*)?)+\)")

Version = tuple[dict, str]


def _prose(text, alias: dict[str, str]) -> str:
    """Normalized prose with codes masked (citations are relations)."""
    s = normalize_text(_COMMENT_RE.sub(" ", str(text or "")), alias)
    s = CODE_RE.sub("@CODE", s)
    s = _CITE_PAREN_RE.sub(" ", s)
    return re.sub(r" ([.,;:)])", r"\1", " ".join(s.split()))


def sections(body: str, alias: dict[str, str]) -> tuple[list[str], list[str]]:
    """(lines outside dated notes, lines inside them), normalized; H1 dropped."""
    outside, notes, in_note = [], [], False
    for line in _COMMENT_RE.sub("", body).splitlines():
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            in_note = line[3:].startswith("Note of")
        text = _prose(line, alias)
        if text:
            (notes if in_note else outside).append(text)
    return outside, notes


def _churn(old: list[str], new: list[str]) -> tuple[int, int]:
    """Lines added and lines removed."""
    added = removed = 0
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if tag != "equal":
            removed += i2 - i1
            added += j2 - j1
    return added, removed


def _relations(fields: dict, scheme: str, schema: Schema, alias: dict[str, str]) -> set[tuple[str, str]]:
    return {(f, c) for f in schema.forward_fields(scheme) for c in as_codes(fields.get(f), alias)}


def diff_entries(old: Version | None, new: Version | None, scheme: str,
                 schema: Schema, alias: dict[str, str]) -> list[dict]:
    """The events that turn version `old` into version `new` (None: absent)."""
    if new is None:
        return [{"kind": "deleted"}] if old is not None else []
    nf, nb = new
    new_rel = _relations(nf, scheme, schema, alias)
    if old is None:
        outside, notes = sections(nb, alias)
        return [{"kind": "created", "status": str(nf.get("status", "")), "lines": len(outside)}] + [
            {"kind": "relation_add", "field": f, "target": c} for f, c in sorted(new_rel)]
    of, ob = old
    ev: list[dict] = []
    if str(of.get("status", "")) != str(nf.get("status", "")):
        ev.append({"kind": "status", "old": str(of.get("status", "")), "new": str(nf.get("status", ""))})
    if any(_prose(of.get(f), alias) != _prose(nf.get(f), alias) for f in STATEMENT):
        ev.append({"kind": "statement"})
    if _prose(of.get("defeated_if"), alias) != _prose(nf.get("defeated_if"), alias):
        ev.append({"kind": "defeater"})
    if any(_prose(of.get(f), alias) != _prose(nf.get(f), alias) for f in SUMMARY):
        ev.append({"kind": "summary"})
    (o_out, o_notes), (n_out, n_notes) = sections(ob, alias), sections(nb, alias)
    added, removed = _churn(o_out, n_out)
    if added or removed:
        ev.append({"kind": "body", "added": added, "removed": removed})
    added, removed = _churn(o_notes, n_notes)
    if added or removed:
        ev.append({"kind": "note", "added": added, "removed": removed})
    role = [f for f in ROLE if of.get(f) not in (None, "") and of.get(f) != nf.get(f)]
    if role:
        ev.append({"kind": "role", "fields": role})
    old_rel = _relations(of, scheme, schema, alias)
    ev += [{"kind": "relation_add", "field": f, "target": c} for f, c in sorted(new_rel - old_rel)]
    ev += [{"kind": "relation_remove", "field": f, "target": c} for f, c in sorted(old_rel - new_rel)]
    skip = (BOOKKEEPING | set(STATEMENT) | set(SUMMARY) | {"status", "defeated_if"}
            | schema.forward_fields(scheme) | schema.derived_fields(scheme))
    meta = sorted(k for k in set(of) | set(nf) if k not in skip and of.get(k) != nf.get(k)
                  and not (k in ROLE and k in role))
    if meta:
        ev.append({"kind": "meta", "fields": meta})
    if not ev and (of, ob) != (nf, nb):
        ev.append({"kind": "mechanical"})
    return ev
