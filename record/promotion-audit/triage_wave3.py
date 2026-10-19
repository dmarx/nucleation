# record/promotion-audit/triage_wave3.py
"""Score Proposed non-mathematics THEORYs for wave 3 of the promotion audit (triage-004).

Wave 3 is the source-backed THEORYs. The record-own re-derivation route of
ADR-047 v2 is rarely open there, so the batch-007 notes name two predictors
instead, both readable from one pass over the entry:

  bundling  0-2  the promote_when asks about something the body's "What this
                 does not say" disclaims: the share of the promote_when's
                 distinctive words (not in the title) that the disclaimer also
                 uses (>= 0.2 gives 1, >= 0.3 gives 2; about the top 45% and 20%
                 of wave 3 on 2026-10-19)
  depth     0-2  how deeply the THEORY's sources were read: the weakest source,
                 each LIT taking its best NOTE. 2 = Read and the version-1
                 history says read in full, closely or step by step; 1 = Read;
                 0 = Skimmed, read only in outline or abstract, or no NOTE
  firsthand 0-1  "What was actually shown" carries no mark of second-hand or
                 partial evidence ("cited to", "asserted", "not read", "in
                 outline", ...), THEORY-106's and THEORY-323's shape
  extends   0-1  triage_bundling.py's extension pattern on the promote_when
  compound  0-1  the title joins clauses with ", so " or "; " (triage_bundling.py's
                 wider pattern matches 96% of wave 3, so it is narrowed here)

Eligible: status Proposed, no `mathematics` tag (those are wave 2), not already
a candidate or requeued in queue.yaml. Ties break on the number of entries the
THEORY supports, then code. A control sample is drawn by a fixed rule from the
eligible codes outside the ranked top. The score orders review; it decides
nothing (ADR-047). Run from the repository root on a freshly fetched origin/main:

    python3 record/promotion-audit/triage_wave3.py --out=record/promotion-audit/triage-004.yaml
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
                        r"not checked|unread|not seen", re.IGNORECASE)
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
    return min((depths.get(s, 0) for s in lits), default=0)


def eligible(record: Path, skip: set[str]) -> list[tuple[str, dict, str]]:
    rows = []
    for p in sorted((record / "theory.d").glob("THEORY-*.md")):
        fm = frontmatter(p)
        if not fm or fm.get("status") != "Proposed" or "mathematics" in (fm.get("tags") or []):
            continue
        if p.stem not in skip:
            rows.append((p.stem, fm, body_of(p)))
    return rows


def control(codes: list[str], exclude: set[str], size: int = 5) -> list[str]:
    """Every k-th of the sorted codes outside `exclude`, starting at k // 2."""
    pool = sorted(c for c in codes if c not in exclude)
    k = max(1, len(pool) // size)
    return pool[k // 2::k][:size]


def queued(queue: Path) -> set[str]:
    q = yaml.safe_load(queue.read_text())
    return {c["code"] for c in q.get("candidates") or []} | {r["code"] for r in q.get("requeue") or []}


def main(record: str = "record", queue: str = "record/promotion-audit/queue.yaml",
         out: str = "", top: int = 20) -> None:
    root = Path(record)
    depths = lit_depths(root)
    rows = []
    for code, fm, body in eligible(root, queued(Path(queue))):
        rubric = {
            "bundling": bundling(fm, section(body, "What this does not say")),
            "depth": theory_depth(fm.get("source") or [], depths),
            "firsthand": firsthand(section(body, "What was actually shown")),
            "extends": int(bool(EXTENSION.search(str(fm.get("promote_when") or "")))),
            "compound": int(bool(COMPOUND.search(str(fm.get("title") or "")))),
        }
        rows.append({"code": code, "wave": 3, "score": sum(rubric.values()), "rubric": rubric,
                     "supports": len(fm.get("supports") or []), "triage": "triage-004",
                     "note": str(fm.get("title") or "")[:140]})
    rows.sort(key=lambda r: (-r["score"], -r["supports"], r["code"]))
    ranked = rows[:top]
    ctrl_codes = control([r["code"] for r in rows], {r["code"] for r in ranked})
    by_code = {r["code"]: r for r in rows}
    hist: dict[int, int] = {}
    for r in rows:
        hist[r["score"]] = hist.get(r["score"], 0) + 1
    logger.info(f"{len(rows)} eligible; score distribution {dict(sorted(hist.items(), reverse=True))}")
    result = {"eligible": len(rows), "distribution": dict(sorted(hist.items(), reverse=True)),
              "ranked": ranked, "control": [by_code[c] for c in ctrl_codes]}
    if out:
        Path(out).write_text(yaml.safe_dump(result, sort_keys=False, allow_unicode=True, width=100))
    else:
        print(yaml.safe_dump(result, sort_keys=False, allow_unicode=True, width=100))


if __name__ == "__main__":
    fire.Fire(main)
