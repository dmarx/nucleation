# record/promotion-audit/triage_wave3.py
"""Score Proposed THEORYs outside the queue for wave 3 of the promotion audit (triage-004, -005, -006).

Wave 3 is the source-backed THEORYs. Batches 016 and 017 found its yield in
its formal members, the entries a re-derivation can settle (ADR-047 v2), and
none of triage-004's components separated yielders from the rest. Triage-005
therefore routes formal entries apart and scores the rest by:

  bundling  0-2  the promote_when asks about something the body's "What this
                 does not say" disclaims: the share of the promote_when's
                 distinctive words (not in the title) that the disclaimer also
                 uses (>= 0.2 gives 1, >= 0.3 gives 2)
  depth     0-2  how deeply the THEORY's sources were read: the best source,
                 each LIT taking its best NOTE (triage-004 took the weakest,
                 which hid THEORY-078's fully read core). 2 = Read and the
                 version-1 history says read in full, closely or step by step;
                 1 = Read; 0 = Skimmed, read only in outline or abstract, or no NOTE
  firsthand 0-1  "What was actually shown" carries no mark of second-hand,
                 partial or absent evidence ("cited to", "asserted", "nothing
                 is measured", "no theorems", "followed as statements", ...)
  extends   0-1  triage_bundling.py's extension pattern on the promote_when
  compound  0-1  the title joins clauses with ", so " or "; "
  empirical_hedged 0-1  the title reports one measured signature against an
                 explicit contrast ("the signature of X, not of Y"), the shape
                 ADR-047 v3 lets one fully read study promote

and flags, without scoring it:

  formal    0-1  formal_score >= 2. Formal entries take route
                 `re-derivation`; the rest take route `source`.

formal_score (triage-006) counts four signals and one penalty, since triage-005's
title-and-shown rule missed THEORY-187, -211, -566 and -176 and flagged the
arguments THEORY-590 and -690 (batches 026, 027):

  title     1  the title states a formal result (bound, theorem, identity,
               exact, optimal, eigenvalues, ...)
  cites     1  the evidence cites a numbered Theorem, Lemma, Proposition or
               Corollary
  relation  1  the evidence states an equation or inequality between
               expressions (a setting such as "d = 6" is not one) or uses an
               operator such as ‖·‖, ∑, ∫ or ∘
  derived   1  a source's NOTE has a claims-table row saying "proved",
               "derivation" or "re-derived" (not "not re-derived"), and the row
               or the NOTE's version-1 history says "followed step by step" or
               "read in full"
  philosophical -1  the title says thesis, argument, account or should

The evidence is the body without its "What this does not say", "What it
bears on" and "Connections" sections and without HTML comments.

Eligible: status Proposed and not already a candidate or requeued in
queue.yaml. The `mathematics` tag no longer excludes an entry: batch 011 found
tagged measurements and batches 016-017 untagged theorems. Ties break on the
number of entries the THEORY supports, then code. The score orders review; it
decides nothing (ADR-047). Run from the repository root on a freshly fetched
origin/main:

    python3 record/promotion-audit/triage_wave3.py --out=record/promotion-audit/triage-006.yaml

`--snapshots` maps a revision to an extracted record (git archive REV
record/theory.d record/notes.d | tar -x -C DIR; pass DIR/record) and scores
LABELLED, the reviewed entries, as they stood before review.
"""
import re
import sys
from pathlib import Path

import fire
import yaml
from loguru import logger

sys.path.insert(0, str(Path(__file__).parent))
from triage_bundling import EXTENSION, frontmatter  # noqa: E402

WORD = re.compile(r"[a-z][a-z'-]{3,}")
STOP = set(
    "that this with from what when which where their there these those than then them they "
    "into onto upon over under about after before between through would could should shown "
    "show shows does done said says also only more most less such some each both either "
    "other being been were have has having whether while within without itself record "
    "entry claim claims theory note reading read source sources paper promote promoted "
    "proposed active case cases same another first second given here once".split()
)
FULL = re.compile(r"read in full|read closely|in full\b|every (?:section|proof)|step by step|"
                  r"followed (?:every|each|the proof)", re.IGNORECASE)
SHALLOW = re.compile(r"in outline|outline only|abstract only|only the abstract|"
                     r"from the abstract|not read in full", re.IGNORECASE)
COMPOUND = re.compile(r", so |; ")
SECONDHAND = re.compile(r"cited to|\bcites\b|not read|second-hand|secondhand|in outline|asserted|"
                        r"not checked|unread|not seen|nothing is measured|nothing was (?:measured|tested)|"
                        r"no theorems?\b|not computed|stated by no source|filer's synthesis|"
                        r"followed as statements", re.IGNORECASE)
FORMAL_TITLE = re.compile(r"\b(?:bound|theorem|lemma|equivalen\w*|isometr\w*|identity|exact(?:ly)?|"
                          r"proved?|optimal|eigenvalues?|spectrum|if and only if|realized by|"
                          r"converges?|interpolation|fixed point|minimi[sz]\w*|inequality)\b|[=≤≥∈‖∑∫]",
                          re.IGNORECASE)
TRIAGE_005_SHOWN = re.compile(r"\b(?:theorem|proposition|lemma|corollary|proof|proved|proves|derived?|"
                              r"derives|derivation|eq\.|equation|inequality|bound)\b", re.IGNORECASE)
CITES = re.compile(r"\b(?:Theorem|Lemma|Proposition|Corollary)s?\s+(?:[A-Z]?\d|[IVX]+\b|[A-Z]\b|\()")
RELATION = re.compile(r"(?<![\w.])(?:[^\s\d,;:(][^\s,;:]*|\))\s?(?:=|≤|≥|≠|≈|<(?!-)|(?<![-=])>|∝)\s?"
                      r"(?!\d+(?:\.\d+)?\b)[^\s,.;:]")
OPERATOR = re.compile(r"[∑∫∘⊕∇∂∝]|‖[^‖\n]+‖")
PHILOSOPHICAL = re.compile(r"\b(?:thesis|argument|account|should)\b", re.IGNORECASE)
DERIVED = re.compile(r"(?<!not )\b(?:proved|derivation|re-derived)\b", re.IGNORECASE)
MARKED = re.compile(r"followed step by step|read in full", re.IGNORECASE)
COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
NOT_EVIDENCE = {"What this does not say", "What it bears on", "Connections"}
HEDGED = re.compile(r"\b(?:signature|profile|pattern|shape|statistics) of\b[^.;]*?,\s*not\b", re.IGNORECASE)
HEADING = re.compile(r"^#{1,6} +(.+?) *$", re.MULTILINE)


def body_of(path: Path) -> str:
    parts = path.read_text().split("---", 2)
    return parts[2] if len(parts) == 3 else ""


def section(body: str, name: str) -> str:
    """Text under the heading `name`, up to the next heading."""
    heads = list(HEADING.finditer(body))
    for i, h in enumerate(heads):
        if h.group(1).strip() == name:
            end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
            return body[h.end():end]
    return ""


def evidence(body: str) -> str:
    """The body without HTML comments and the sections that disclaim or point elsewhere."""
    body = COMMENT.sub("", body)
    heads = list(HEADING.finditer(body))
    keep = [body[:heads[0].start()] if heads else body]
    for i, h in enumerate(heads):
        if h.group(1).strip() not in NOT_EVIDENCE:
            keep.append(body[h.start():heads[i + 1].start() if i + 1 < len(heads) else len(body)])
    return "".join(keep)


def words(text: str) -> set[str]:
    return {w.rstrip("'s") for w in WORD.findall(text.lower())} - STOP


def bundling(fm: dict, disclaim: str) -> int:
    asked = words(str(fm.get("promote_when") or "")) - words(str(fm.get("title") or ""))
    share = len(asked & words(disclaim)) / max(1, len(asked))
    return 2 if share >= 0.3 else 1 if share >= 0.2 else 0


def firsthand(shown: str) -> int:
    return int(not SECONDHAND.search(shown))


def cites_theorem(text: str) -> int:
    return int(bool(CITES.search(text)))


def relations(text: str) -> int:
    return len(RELATION.findall(text)) + len(OPERATOR.findall(text))


def philosophical(title: str) -> int:
    return int(bool(PHILOSOPHICAL.search(title)))


def formal_signals(title: str, text: str, derived: int = 0) -> dict[str, int]:
    return {"title": int(bool(FORMAL_TITLE.search(title))), "cites": cites_theorem(text),
            "relation": int(relations(text) > 0), "derived": derived,
            "philosophical": -philosophical(title)}


def formal_score(title: str, text: str, derived: int = 0) -> int:
    return sum(formal_signals(title, text, derived).values())


def formal(title: str, text: str, derived: int = 0) -> int:
    return int(formal_score(title, text, derived) >= 2)


def empirical_hedged(title: str) -> int:
    return int(bool(HEDGED.search(title)))


def note_depth(status: str | None, v1: str) -> int:
    if status != "Read" or SHALLOW.search(v1):
        return 0
    return 2 if FULL.search(v1) else 1


def lit_depths(record: Path) -> dict[str, int]:
    best: dict[str, int] = {}
    for p in sorted((record / "notes.d").glob("NOTE-*.md")):
        fm = frontmatter(p)
        if not fm or not fm.get("paper"):
            continue
        v1 = " ".join(str(h.get("note") or "") for h in fm.get("history") or []
                      if isinstance(h, dict) and h.get("version") == 1)
        lit = str(fm["paper"])
        best[lit] = max(best.get(lit, 0), note_depth(fm.get("status"), v1))
    return best


def lit_derived(record: Path) -> set[str]:
    """LITs with a NOTE whose claims table has a marked proof or derivation."""
    out: set[str] = set()
    for p in sorted((record / "notes.d").glob("NOTE-*.md")):
        fm = frontmatter(p)
        if not fm or not fm.get("paper"):
            continue
        v1 = " ".join(str(h.get("note") or "") for h in fm.get("history") or []
                      if isinstance(h, dict) and h.get("version") == 1)
        rows = [r for r in section(body_of(p), "Claims").splitlines() if r.startswith("|")]
        if any(DERIVED.search(r) and (MARKED.search(r) or MARKED.search(v1)) for r in rows):
            out.add(str(fm["paper"]))
    return out


def theory_derived(sources: list[str], derived: set[str]) -> int:
    return int(any(str(s) in derived for s in sources))


def theory_depth(sources: list[str], depths: dict[str, int]) -> int:
    lits = [s for s in sources if str(s).startswith("LIT-")]
    return max((depths.get(s, 0) for s in lits), default=0)


def eligible(record: Path, skip: set[str]) -> list[tuple[str, dict, str]]:
    rows = []
    for p in sorted((record / "theory.d").glob("THEORY-*.md")):
        fm = frontmatter(p)
        if fm and fm.get("status") == "Proposed" and p.stem not in skip:
            rows.append((p.stem, fm, body_of(p)))
    return rows


def score(code: str, fm: dict, body: str, depths: dict[str, int], derived: set[str]) -> dict:
    title = str(fm.get("title") or "")
    shown = section(body, "What was actually shown")
    rubric = {
        "bundling": bundling(fm, section(body, "What this does not say")),
        "depth": theory_depth(fm.get("source") or [], depths),
        "firsthand": firsthand(shown),
        "extends": int(bool(EXTENSION.search(str(fm.get("promote_when") or "")))),
        "compound": int(bool(COMPOUND.search(title))),
        "empirical_hedged": empirical_hedged(title),
    }
    signals = formal_signals(title, evidence(body), theory_derived(fm.get("source") or [], derived))
    fscore = sum(signals.values())
    return {"code": code, "wave": 3, "score": sum(rubric.values()),
            "rubric": {**rubric, "formal": int(fscore >= 2), "formal_score": fscore},
            "formal_signals": [k for k, v in signals.items() if v],
            "route": "re-derivation" if fscore >= 2 else "source",
            "supports": len(fm.get("supports") or []), "triage": "triage-006", "note": title[:140]}


def score_rows(record: Path, skip: set[str]) -> list[dict]:
    depths, derived = lit_depths(record), lit_derived(record)
    rows = [score(code, fm, body, depths, derived) for code, fm, body in eligible(record, skip)]
    rows.sort(key=lambda r: (-r["score"], -r["supports"], r["code"]))
    return rows


def control(codes: list[str], exclude: set[str], size: int = 5) -> list[str]:
    """Every k-th of the sorted codes outside `exclude`, starting at k // 2."""
    pool = sorted(c for c in codes if c not in exclude)
    k = max(1, len(pool) // size)
    return pool[k // 2::k][:size]


def queued(queue: Path) -> set[str]:
    q = yaml.safe_load(queue.read_text())
    return {c["code"] for c in q.get("candidates") or []} | {r["code"] for r in q.get("requeue") or []}


# The reviewed wave-3 entries, by the revision they were triaged at: formal (1) when
# the review's path went through a re-derivation (ADR-047 v2), 0 when it went by
# measurement (ADR-047 v3) or retained the entry as argument or non-formal.
LABELLED: dict[str, dict[str, tuple[int, str]]] = {
    "9ca3a0dc": {  # batches 016, 017 (triage-004)
        "THEORY-078": (1, "batch-017 split, formal algebra"),
        "THEORY-079": (0, "batch-016 retained"),
        "THEORY-111": (1, "batch-016 split, formal core"),
        "THEORY-170": (0, "batch-016 retained"),
        "THEORY-199": (0, "batch-017 retained, annealed mean-field only"),
        "THEORY-309": (1, "batch-017 promoted"),
        "THEORY-369": (1, "batch-016 narrowed and promoted"),
        "THEORY-470": (0, "batch-017 retained"),
        "THEORY-481": (1, "batch-016 needs correction, a derivation error"),
        "THEORY-625": (0, "batch-017 retained"),
    },
    "8999ea61": {  # batches 024-027 (triage-005)
        "THEORY-169": (1, "batch-024 re-derivation"),
        "THEORY-182": (1, "batch-024 re-derivation"),
        "THEORY-186": (1, "batch-024 re-derivation"),
        "THEORY-283": (1, "batch-024 re-derivation"),
        "THEORY-286": (1, "batch-024 re-derivation"),
        "THEORY-308": (1, "batch-025 re-derivation"),
        "THEORY-314": (1, "batch-025 re-derivation"),
        "THEORY-320": (1, "batch-025 re-derivation"),
        "THEORY-391": (0, "batch-025 narrowed, by measurement (v3)"),
        "THEORY-472": (1, "batch-025 narrowed, v3 with a re-derived part"),
        "THEORY-231": (1, "batch-026 re-derivation"),
        "THEORY-478": (1, "batch-026 re-derivation"),
        "THEORY-590": (0, "batch-026 argument, retained"),
        "THEORY-614": (1, "batch-026 needs correction"),
        "THEORY-690": (0, "batch-026 argument, retained"),
        "THEORY-176": (1, "batch-027 re-derivation"),
        "THEORY-187": (1, "batch-027 re-derivation"),
        "THEORY-195": (0, "batch-027 measurement (v3)"),
        "THEORY-211": (1, "batch-027 re-derivation"),
        "THEORY-566": (1, "batch-027 re-derivation"),
    },
}


def precision_recall(pairs: list[tuple[int, int]]) -> dict:
    """(flag, label) pairs to counts, precision and recall, rounded to two places."""
    tp = sum(1 for f, y in pairs if f and y)
    fp = sum(1 for f, y in pairs if f and not y)
    fn = sum(1 for f, y in pairs if not f and y)
    return {"tp": tp, "fp": fp, "fn": fn, "tn": len(pairs) - tp - fp - fn,
            "precision": round(tp / max(1, tp + fp), 2), "recall": round(tp / max(1, tp + fn), 2)}


def labelled_check(snapshots: dict[str, str]) -> dict:
    """Score LABELLED in the records they were triaged from; triage-005's flag beside the new one."""
    rows = []
    for rev, labels in LABELLED.items():
        rec = Path(snapshots[rev])
        depths, derived = lit_depths(rec), lit_derived(rec)
        for code, (label, outcome) in labels.items():
            p = rec / "theory.d" / f"{code}.md"
            fm, body = frontmatter(p), body_of(p)
            r = score(code, fm, body, depths, derived)
            old = int(bool(FORMAL_TITLE.search(str(fm.get("title") or "")))
                      and bool(TRIAGE_005_SHOWN.search(section(body, "What was actually shown"))))
            rows.append({"code": code, "revision": rev, "label": label, "outcome": outcome,
                         "formal": r["rubric"]["formal"], "formal_score": r["rubric"]["formal_score"],
                         "triage_005": old})
    rows.sort(key=lambda r: r["code"])
    return {"triage_006": precision_recall([(r["formal"], r["label"]) for r in rows]),
            "triage_005": precision_recall([(r["triage_005"], r["label"]) for r in rows]),
            "entries": rows}


def main(record: str = "record", queue: str = "record/promotion-audit/queue.yaml",
         out: str = "", top: int = 20, snapshots: dict | None = None) -> None:
    root, qpath = Path(record), Path(queue)
    rows = score_rows(root, queued(qpath))
    # the route's question is formal content, so it orders by formal_score, then score
    formal_rows = sorted((r for r in rows if r["route"] == "re-derivation"),
                         key=lambda r: (-r["rubric"]["formal_score"], -r["score"], -r["supports"], r["code"]))
    routed = formal_rows[:top]
    ctrl_codes = control([r["code"] for r in formal_rows], {r["code"] for r in routed})
    by_code = {r["code"]: r for r in rows}
    logger.info(f"{len(rows)} eligible; {len(formal_rows)} flagged formal")
    result = {"eligible": len(rows), "formal_flagged": len(formal_rows),
              "formal_route": routed, "control": [by_code[c] for c in ctrl_codes]}
    if snapshots:
        result["labelled_check"] = labelled_check({str(k): v for k, v in snapshots.items()})
    else:
        logger.warning("no --snapshots; labelled_check skipped")
    text = yaml.safe_dump(result, sort_keys=False, allow_unicode=True, width=100)
    if out:
        Path(out).write_text(text)
    else:
        print(text)


if __name__ == "__main__":
    fire.Fire(main)
