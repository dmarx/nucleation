# scratch/tools/record_history/events.py
"""Replay the history into an event table, one row per (commit, entry, event)."""
from __future__ import annotations

from collections import Counter
from pathlib import Path

from loguru import logger

from record_history.classify import diff_entries
from record_history.entries import Schema, as_codes, canonical, code_of_path, parse_entry
from record_history.gitlog import BlobReader, Commit


def alias_map(commits: list[Commit], formerly: dict[str, list[str]] | None = None,
              live: set[str] | None = None) -> dict[str, str]:
    """Old code to new code, from renames of entry files and `formerly` fields.

    A code in `live` (a file at the tip) is its own entry and never an alias,
    even if it was once renamed away: codes have been handed back and reused.
    """
    alias: dict[str, str] = {}
    for c in commits:
        for ch in c.changes:
            if ch.status == "R" and ch.old_path and ch.new_path:
                old, new = code_of_path(ch.old_path), code_of_path(ch.new_path)
                if old and new and old != new:
                    alias[old] = new
    for code, olds in (formerly or {}).items():
        for old in olds:
            if old != code:
                alias.setdefault(old, code)
    return {k: v for k, v in alias.items() if k not in (live or set())}


def formerly_on_disk(repo: Path, schema_dirs: list[str]) -> dict[str, list[str]]:
    """`formerly:` of every entry in the checkout, the record's own alias list."""
    out: dict[str, list[str]] = {}
    for d in schema_dirs:
        for p in (repo / d).glob("*.md"):
            code = code_of_path(str(p))
            if not code:
                continue
            fields, _ = parse_entry(p.read_text(errors="replace"))
            olds = fields.get("formerly") or []
            if olds:
                out[code] = [str(o) for o in (olds if isinstance(olds, list) else [olds])]
    return out


def replay(commits: list[Commit], blobs: BlobReader, schema: Schema,
           alias: dict[str, str]) -> list[dict]:
    """Event rows for every entry change, diffed against the entry's last version."""
    cache: dict[str, tuple[dict, str]] = {}

    def version(sha: str | None):
        if sha is None:
            return None
        if sha not in cache:
            cache[sha] = parse_entry(blobs.read(sha))
        return cache[sha]

    last: dict[str, tuple[dict, str]] = {}
    rows: list[dict] = []
    for i, c in enumerate(commits):
        start = len(rows)
        # one entry can appear twice in a commit (a concrete file added while
        # its temporary twin is deleted): it is deleted only if every change is
        grouped: dict[str, list] = {}
        for ch in c.changes:
            raw = code_of_path(ch.new_path or ch.old_path or "")
            if raw:
                grouped.setdefault(canonical(raw, alias), []).append(ch)
        codes = Counter()
        for code, chs in grouped.items():
            scheme = schema.scheme_of(code)
            if scheme is None:
                continue
            codes[code] += 1
            kept = [ch for ch in chs if ch.status != "D"]
            new = version(kept[-1].new_sha) if kept else None
            old = last.get(code)
            if new is None and old is None:
                continue
            for ev in diff_entries(old, new, scheme, schema, alias):
                rows.append({"commit": c.sha, "time": c.time, "bot": c.bot, "author": c.author,
                             "subject": c.subject, "code": code, "scheme": scheme, **ev})
            if new is None:
                last.pop(code, None)
            else:
                last[code] = new
        breadth = len(codes)
        for row in rows[start:]:
            row["breadth"] = breadth
        if i % 500 == 0:
            logger.info(f"replayed {i}/{len(commits)} commits, {len(rows)} events")
    return rows


def tree_entries(blobs: BlobReader, tree: dict[str, str], schema: Schema,
                 alias: dict[str, str]) -> dict[str, set[tuple[str, str]]]:
    """Each live entry at the tip, with its forward edges (canonical codes)."""
    out: dict[str, set[tuple[str, str]]] = {}
    for path, sha in tree.items():
        raw = code_of_path(path)
        if not raw:
            continue
        code = canonical(raw, alias)
        scheme = schema.scheme_of(code)
        if scheme is None:
            continue
        fields, _ = parse_entry(blobs.read(sha))
        out[code] = {(f, c) for f in schema.forward_fields(scheme)
                     for c in as_codes(fields.get(f), alias)}
    return out


def final_state(rows: list[dict]) -> dict[str, dict]:
    """Each live entry's last status and current forward edges, from the events."""
    state: dict[str, dict] = {}
    for r in rows:
        s = state.setdefault(r["code"], {"scheme": r["scheme"], "status": "", "edges": set(),
                                         "created": r["time"], "deleted": False})
        k = r["kind"]
        if k == "created":
            s["status"] = r.get("status", "")
            s["deleted"] = False
        elif k == "status":
            s["status"] = r["new"]
        elif k == "relation_add":
            s["edges"].add((r["field"], r["target"]))
        elif k == "relation_remove":
            s["edges"].discard((r["field"], r["target"]))
        elif k == "deleted":
            s["deleted"] = True
            s["edges"] = set()
    return state

