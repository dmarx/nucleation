#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LEAD-122: census of filing dispositions in the workbench reconstructions.

Run (CPU only, no network):

    python3 -I scratch/studies/lead-122/census.py \
        --workbench record/workbench.d --out scratch/studies/lead-122/results.json

What it does
------------
The workbench reconstructions mark how each move of a working session was
handled, using a small set of the record's own bold labels (``**Filed:**``,
``**Missed:**``, ``**Not filed:**``, ``**Struck:**``, ``**Held, not filed:**``,
``**Corrected:**``, ...). Each such label introduces a *disposition item* -- a
span of text describing one or more moves and what became of them. This script
treats each label span as one MOVE, bins it as filed / not-filed / corrected /
other, reads its CONTRIBUTOR from the attribution tokens in and around it
(owner turns ``U\\d``, assistant turns ``A\\d``, the reconstruction's readers),
and reads its KIND from the scheme codes it names. It then tallies the share
filed by contributor and by kind.

This is a coarse, string-level pass. Its limits are stated in README.md and in
the CASE filed from it; chiefly, it captures only label-bearing entries, and it
cannot verify that moves it compares are of "comparable content".
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# --- label -> disposition bin -------------------------------------------------
# Labels are matched as **Label:** (bold, trailing colon inside the asterisks).
FILED_LABELS = {"filed"}
NOT_FILED_LABELS = {
    "missed", "also missed", "missed by a", "not filed", "not filed, and why",
    "struck", "held, not filed",
}
CORRECTED_LABELS = {"corrected", "reworded", "reversed", "split", "renamed"}
# Everything else (Right, Wrong, Already held, On file, Checked, Registered...)
# is reported under 'other' and excluded from the filed / not-filed shares.

LABEL_RE = re.compile(r"\*\*([A-Z][A-Za-z ,]{0,40}?):\*\*")
# Codes of the record's schemes.
CODE_RE = re.compile(r"\b(CLAIM|QUESTION|TERM|CASE|ARG|THEORY|LIT|NOTE|SYNTHESIS)-"
                     r"(?:tmp[0-9a-z]+|\d+)\b")
OWNER_TURN_RE = re.compile(r"\bU\d+\b")
ASSISTANT_TURN_RE = re.compile(r"\bA\d+\b")
OWNER_WORD_RE = re.compile(r"\bowner('s|s'|)\b", re.IGNORECASE)
ASSISTANT_WORD_RE = re.compile(r"\b(the assistant|assistant's|A's)\b")
READER_RE = re.compile(
    r"\b(the readers?|derived by the reader|checked by (?:simulation|"
    r"linear programming|the reader)|redid the mathematics|by the reader)\b",
    re.IGNORECASE,
)


def disposition_of(label):
    """Bin a label (lowercased, no colon) into a disposition class."""
    key = label.strip().lower()
    if key in FILED_LABELS:
        return "filed"
    if key in NOT_FILED_LABELS:
        return "not_filed"
    if key in CORRECTED_LABELS:
        return "corrected"
    return "other"


def _block_start(text, pos):
    """Index of the start of the Markdown block (bullet / paragraph) holding
    ``pos``: the most recent blank line or list-marker line break before it."""
    # Walk back to the start of the current line's bullet or paragraph.
    para = text.rfind("\n\n", 0, pos)
    para = para + 2 if para != -1 else 0
    # If a list item ("- " or "  - ") begins after the paragraph break and
    # before pos, start the context there instead (tighter attribution).
    bullet = max(
        (m.start() for m in re.finditer(r"(?m)^\s*[-*] ", text[para:pos])),
        default=None,
    )
    if bullet is not None:
        return para + bullet
    return para


def extract_moves(text):
    """Yield one dict per label span in ``text``.

    Each span runs from just after its label to the next label or the end of
    the enclosing block. ``context`` is the enclosing block head (for
    bullet-level attribution) plus the span text.
    """
    labels = list(LABEL_RE.finditer(text))
    moves = []
    for i, m in enumerate(labels):
        label = m.group(1)
        span_start = m.end()
        # Span ends at the next label, or the end of its block, whichever first.
        nxt = labels[i + 1].start() if i + 1 < len(labels) else len(text)
        block_end = text.find("\n\n", span_start)
        block_end = block_end if block_end != -1 else len(text)
        span_end = min(nxt, block_end)
        span = text[span_start:span_end]
        context = text[_block_start(text, m.start()):span_end]
        moves.append({
            "label": label,
            "disposition": disposition_of(label),
            "span": span,
            "context": context,
        })
    return moves


def classify_contributor(context):
    """owner / assistant / both / reader / unattributed, from a move's context.

    Owner turns are U-numbered, assistant turns A-numbered (workbench
    convention). 'reader' is the reconstruction's own deriving readers.
    """
    owner = bool(OWNER_TURN_RE.search(context) or OWNER_WORD_RE.search(context))
    assistant = bool(ASSISTANT_TURN_RE.search(context)
                     or ASSISTANT_WORD_RE.search(context))
    reader = bool(READER_RE.search(context))
    if owner and assistant:
        return "both"
    if owner:
        return "owner"
    if assistant:
        return "assistant"
    if reader:
        return "reader"
    return "unattributed"


def classify_kind(span):
    """Kind of the move, from the scheme codes it names.

    A span that says 'note on' / 'notes on' is a note added to a held entry.
    Otherwise the kind is the first scheme code's type; 'work' for LIT
    (a work registered); 'unclassified' when no code is named.
    """
    if re.search(r"\bnotes? on\b", span, re.IGNORECASE):
        return "note"
    m = CODE_RE.search(span)
    if not m:
        if re.search(r"\bwork(s)? registered\b|\bregistered\b", span, re.IGNORECASE):
            return "work"
        return "unclassified"
    scheme = m.group(1)
    return {
        "CLAIM": "claim", "QUESTION": "question", "TERM": "term",
        "CASE": "case", "ARG": "arg", "THEORY": "theory",
        "LIT": "work", "NOTE": "note", "SYNTHESIS": "synthesis",
    }[scheme]


def _cross_tab(fn):
    """(contributor, kind) -> Counter of dispositions, over filed/not-filed."""
    tab = defaultdict(lambda: Counter())
    for mv in fn:
        tab[(mv["contributor"], mv["kind"])][mv["disposition"]] += 1
    return tab


def census(workbench_dir):
    wdir = Path(workbench_dir)
    files = sorted(p for p in wdir.rglob("*.md") if p.name != "_template.md")
    per_file = []
    moves = []
    labeled_files = 0
    for p in files:
        text = p.read_text(encoding="utf-8")
        fmoves = extract_moves(text)
        if fmoves:
            labeled_files += 1
        for mv in fmoves:
            mv["contributor"] = classify_contributor(mv["context"])
            mv["contributor_span_only"] = classify_contributor(mv["span"])
            mv["kind"] = classify_kind(mv["span"])
            mv["file"] = str(p.relative_to(wdir))
            moves.append(mv)
        per_file.append({"file": str(p.relative_to(wdir)), "n_labels": len(fmoves)})

    # --- tallies --------------------------------------------------------------
    disp = Counter(mv["disposition"] for mv in moves)
    # filed / not-filed universe (exclude corrected & other from shares)
    fn = [mv for mv in moves if mv["disposition"] in ("filed", "not_filed")]

    def share_table(group_key):
        tab = defaultdict(lambda: Counter())
        for mv in fn:
            tab[mv[group_key]][mv["disposition"]] += 1
        out = {}
        for g, c in sorted(tab.items()):
            total = c["filed"] + c["not_filed"]
            out[g] = {
                "filed": c["filed"], "not_filed": c["not_filed"],
                "total": total,
                "share_filed": round(c["filed"] / total, 4) if total else None,
            }
        return out

    # distinct filed vs not-filed codes by scheme (supplementary, finer grain)
    code_by_disp = defaultdict(lambda: Counter())
    for mv in fn:
        for code in set(m.group(0) for m in CODE_RE.finditer(mv["span"])):
            scheme = code.split("-", 1)[0]
            code_by_disp[scheme][mv["disposition"]] += 1
    code_table = {}
    for scheme, c in sorted(code_by_disp.items()):
        total = c["filed"] + c["not_filed"]
        code_table[scheme] = {
            "filed_mentions": c["filed"], "not_filed_mentions": c["not_filed"],
            "total": total,
            "share_filed": round(c["filed"] / total, 4) if total else None,
        }

    return {
        "n_workbench_files": len(files),
        "n_files_with_labels": labeled_files,
        "n_files_without_labels": len(files) - labeled_files,
        "n_moves_total": len(moves),
        "n_moves_filed_or_notfiled": len(fn),
        "dispositions": dict(disp),
        "by_contributor": share_table("contributor"),
        "by_contributor_span_only": share_table("contributor_span_only"),
        "by_kind": share_table("kind"),
        "by_contributor_and_kind": {
            f"{g1}|{g2}": {"filed": v["filed"], "not_filed": v["not_filed"]}
            for (g1, g2), v in sorted(
                ((key, {"filed": c["filed"], "not_filed": c["not_filed"]})
                 for key, c in _cross_tab(fn).items()))
        },
        "code_mentions_by_scheme": code_table,
        "moves": [
            {k: mv[k] for k in ("file", "label", "disposition",
                                "contributor", "contributor_span_only", "kind")}
            for mv in moves
        ],
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--workbench", default="record/workbench.d")
    ap.add_argument("--out", default="scratch/studies/lead-122/results.json")
    args = ap.parse_args(argv)
    result = census(args.workbench)
    Path(args.out).write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    # terminal summary
    r = result
    print(f"workbench files: {r['n_workbench_files']} "
          f"(with labels: {r['n_files_with_labels']}, "
          f"without: {r['n_files_without_labels']})")
    print(f"moves (label spans): {r['n_moves_total']}  "
          f"filed+not_filed: {r['n_moves_filed_or_notfiled']}")
    print(f"dispositions: {r['dispositions']}")
    print("\nshare filed by contributor (block context):")
    for g, d in r["by_contributor"].items():
        print(f"  {g:13s} filed {d['filed']:3d} / {d['total']:3d}"
              f"  = {d['share_filed']}")
    print("\nshare filed by contributor (span only, sensitivity):")
    for g, d in r["by_contributor_span_only"].items():
        print(f"  {g:13s} filed {d['filed']:3d} / {d['total']:3d}"
              f"  = {d['share_filed']}")
    print("\nshare filed by kind of move:")
    for g, d in r["by_kind"].items():
        print(f"  {g:13s} filed {d['filed']:3d} / {d['total']:3d}"
              f"  = {d['share_filed']}")
    print("\ncode mentions by scheme (filed vs not-filed spans):")
    for s, d in r["code_mentions_by_scheme"].items():
        print(f"  {s:10s} filed {d['filed_mentions']:3d} / {d['total']:3d}"
              f"  = {d['share_filed']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
