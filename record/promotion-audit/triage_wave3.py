# record/promotion-audit/triage_wave3.py
"""Score Proposed THEORYs outside the queue for wave 3 of the promotion audit (triage-004, -005).

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

  formal    0-1  the title states a formal result (bound, theorem, identity,
                 exact, optimal, eigenvalues, ...) AND "What was actually
                 shown" names a theorem, proof or derivation. Formal entries
                 take route `re-derivation`; the rest take route `source`.

Eligible: status Proposed and not already a candidate or requeued in
queue.yaml. The `mathematics` tag no longer excludes an entry: batch 011 found
tagged measurements and batches 016-017 untagged theorems. Ties break on the
number of entries the THEORY supports, then code. The score orders review; it
decides nothing (ADR-047). Run from the repository root on a freshly fetched
origin/main:

    python3 record/promotion-audit/triage_wave3.py --out=record/promotion-audit/triage-005.yaml
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
FORMAL_SHOWN = re.compile(r"\b(?:theorem|proposition|lemma|corollary|proof|proved|proves|derived?|"
                          r"derives|derivation|eq\.|equation|inequality|bound)\b", re.IGNORECASE)
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


def words(text: str) -> set[str]:
    return {w.rstrip("'s") for w in WORD.findall(text.lower())} - STOP


def bundling(fm: dict, disclaim: str) -> int:
    asked = words(str(fm.get("promote_when") or "")) - words(str(fm.get("title") or ""))
    share = len(asked & words(disclaim)) / max(1, len(asked))
    return 2 if share >= 0.3 else 1 if share >= 0.2 else 0


def firsthand(shown: str) -> int:
    return int(not SECONDHAND.search(shown))


def formal(title: str, shown: str) -> int:
    return int(bool(FORMAL_TITLE.search(title)) and bool(FORMAL_SHOWN.search(shown)))


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


def score(code: str, fm: dict, body: str, depths: dict[str, int]) -> dict:
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
    is_formal = formal(title, shown)
    return {"code": code, "wave": 3, "score": sum(rubric.values()),
            "rubric": {**rubric, "formal": is_formal},
            "route": "re-derivation" if is_formal else "source",
            "supports": len(fm.get("supports") or []), "triage": "triage-005", "note": title[:140]}


def score_rows(record: Path, skip: set[str]) -> list[dict]:
    depths = lit_depths(record)
    rows = [score(code, fm, body, depths) for code, fm, body in eligible(record, skip)]
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


def backtest(record: Path, queue: Path, batches: tuple[str, ...]) -> list[dict]:
    """Score already-reviewed wave-3 candidates of `batches` as if new, beside their dispositions."""
    q = yaml.safe_load(queue.read_text())
    depths = lit_depths(record)
    out = []
    for c in q.get("candidates") or []:
        if c.get("batch") not in batches:
            continue
        p = record / "theory.d" / f"{c['code']}.md"
        fm = frontmatter(p)
        r = score(c["code"], fm, body_of(p), depths)
        out.append({"code": c["code"], "batch": c["batch"], "disposition": c["disposition"],
                    "yielded": c["disposition"] in {"promote", "narrow-and-promote", "split"},
                    "route": r["route"], "score": r["score"], "rubric": r["rubric"]})
    return sorted(out, key=lambda r: r["code"])


def main(record: str = "record", queue: str = "record/promotion-audit/queue.yaml",
         out: str = "", top: int = 15) -> None:
    root, qpath = Path(record), Path(queue)
    rows = score_rows(root, queued(qpath))
    formal_rows = [r for r in rows if r["route"] == "re-derivation"]
    source_rows = [r for r in rows if r["route"] == "source"]
    ranked = source_rows[:top]
    ctrl_codes = control([r["code"] for r in source_rows], {r["code"] for r in ranked})
    by_code = {r["code"]: r for r in rows}
    hist: dict[int, int] = {}
    for r in source_rows:
        hist[r["score"]] = hist.get(r["score"], 0) + 1
    logger.info(f"{len(rows)} eligible; {len(formal_rows)} routed to re-derivation; "
                f"source-route distribution {dict(sorted(hist.items(), reverse=True))}")
    result = {"eligible": len(rows), "formal_routed": len(formal_rows),
              "distribution": dict(sorted(hist.items(), reverse=True)),
              "formal_route": formal_rows[:top], "ranked": ranked,
              "control": [by_code[c] for c in ctrl_codes],
              "backtest": backtest(root, qpath, ("batch-016", "batch-017"))}
    text = yaml.safe_dump(result, sort_keys=False, allow_unicode=True, width=100)
    if out:
        Path(out).write_text(text)
    else:
        print(text)


if __name__ == "__main__":
    fire.Fire(main)
