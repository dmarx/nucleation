# record/promotion-audit/triage_title.py
"""Sort wave-3 Proposed THEORYs by what their title asserts (triage-007).

Triage-006's formal flag is exhausted (score >= 3: 17 of 20 promoted; the
score-2 band 40 of 54). Across rounds 031-057 the sort batch 020 introduced,
by what the title asserts, predicted nearly every outcome: a theorem goes to
re-derivation (ADR-047 v2), a measurement read in full to ADR-047 v3, an
argument to wave 5, and a title that only reports what a source argues or
conjectures waits on the owner's ruling on report titles. This script makes
that sort a transparent rule set over the title and the body:

  report       3  the title says a source argues, conjectures or proposes
  theorem      2  the title states a formal result (triage-006's FORMAL_TITLE
                  or THEOREM_TITLE: for every, if and only if, exactly, at most,
                  invariant, closed under, ...)
               +1 the evidence cites a numbered Theorem, Lemma, Proposition or
                  Corollary
               +1 "What was actually shown" speaks of a theorem, proof or
                  derivation
               +1 a source's NOTE records a marked proof (triage-006 `derived`)
  measurement  2  the title reports what was measured (a percentage, "in X's
                  experiments", participants, datasets, trained networks, ...)
               +1 "What was actually shown" cites a table, figure, n or p
               +1 it speaks of experiments, runs, seeds, simulations or data
  argument     2  the title says what something is, means or should be
                  (thesis, account, meaning, explains, concept, ...)

The highest score wins; ties go report, theorem, measurement, argument,
except that argument beats a theorem score earned by the title alone, and a
measurement whose title fired beats an equal theorem. No signal at all is an
argument. The margin over the runner-up orders a route. The rules were fitted
to the labelled reviewed entries (labels()), so the labelled check measures
fit, not accuracy on new entries.

    python3 record/promotion-audit/triage_title.py --out=record/promotion-audit/triage-007.yaml \\
        --audit=<promotion-audit dir holding the labels>
"""
import re
import subprocess
import sys
from pathlib import Path

import fire
import yaml
from loguru import logger

sys.path.insert(0, str(Path(__file__).parent))
import triage_wave3 as t3  # noqa: E402

CLASSES = ["report", "theorem", "measurement", "argument"]
REPORT = re.compile(r"\b(?:argues?|conjectures?|proposes?|contends?|maintains?|hypothesi[sz]es?)\s+that\b|"
                    r"\b(?:is|are)\s+(?:argued|conjectured|proposed|hypothesi[sz]ed)\b|\bconjectur\w+", re.I)
ARGUMENT = re.compile(r"\b(?:thesis|account|should|ought|explains?|explanation|explanatory|"
                      r"is best (?:understood|seen|read)|meaning|constitut\w+|consists? in|nature of|amounts? to|"
                      r"normative|ethic\w*|moral\w*|selfhood|ownership|agency|concepts?|conceptual|reasons|"
                      r"responsib\w+|values?|purpose|individuat\w+|is what|is part of|refers? to|ontolog\w+|"
                      r"emergen\w+|controlled by|principle)\b", re.I)
MEASUREMENT = re.compile(r"\d+(?:\.\d+)?\s?%|\bin [A-Z][^,;]{1,60}?['’]s?\s(?:experiments?|runs?|simulations?|data|"
                         r"study|studies|surveys?|corpus|benchmarks?|games|trace|logs?)\b|"
                         r"\b(?:measured|measurements?|experiments?|experimental|participants|subjects|trials|"
                         r"datasets?|benchmarks?|surveys?|empirical\w*|observed|recordings?|"
                         r"trained (?:networks?|models?|classifiers?|transformers?)|corpus|"
                         r"on (?:MNIST|CIFAR|ImageNet|SVHN)|mice|rats|monkeys|humans|people|patients|children|adults|"
                         r"listeners|speakers|traders|respondents|languages|rodents|animals)\b", re.I)
SHOWN_STRONG = re.compile(r"\bTables? \d|\bFig(?:ure)?s?\.? ?\d|\bn ?= ?\d|\bp ?[<=] ?0?\.\d|"
                          r"\bstandard (?:error|deviation)|\bconfidence interval", re.I)
SHOWN_DATA = re.compile(r"\bmeasured\b|\bparticipants\b|\bdatasets?\b|\bexperiments?\b|\bruns\b|\bseeds?\b|"
                        r"\bsimulat\w+|\bempirical\w*", re.I)
THEOREM_TITLE = re.compile(r"\bfor (?:every|any|all|each)\b|\bif and only if\b|\bexactly\b|\biff\b|\bbounded\b|"
                           r"\bat most\b|\bat least\b|\bthere (?:is|exists)\b|\bunique(?:ly)?\b|\bequals?\b|"
                           r"\bimplies\b|\bnecessary and sufficient\b|\bonly if\b|\bwhenever\b|\bminimi[sz]\w*|"
                           r"\bmaximi[sz]\w*|\binvariant\b|\bclosed under\b|\btwice\b|\bincompatible\b|"
                           r"\bcan(?:not)? (?:be )?(?:reproduce|represent|express|realis|realiz|carry)\w*|"
                           r"\bsatisf\w+|\bconverg\w+|\bprices?\b|\bentropy\b|\bmetric\b|\bprobability\b|"
                           r"\bdistribution\b", re.I)
SHOWN_THEOREM = re.compile(r"\b(?:Theorem|Lemma|Proposition|Corollary)\b|\bproofs?\b|\bprove[sdn]?\b|"
                           r"\bderiv\w+|\bidentity\b", re.I)


def signals(title: str, body: str, derived: int = 0) -> dict[str, int]:
    shown, ev = t3.section(body, "What was actually shown"), t3.evidence(body)
    return {
        "report_title": int(bool(REPORT.search(title))),
        "theorem_title": int(bool(t3.FORMAL_TITLE.search(title) or THEOREM_TITLE.search(title))),
        "cites": t3.cites_theorem(ev),
        "shown_thm": int(bool(SHOWN_THEOREM.search(shown))),
        "derived": int(derived),
        "measurement_title": int(bool(MEASUREMENT.search(title))),
        "shown_strong": int(bool(SHOWN_STRONG.search(shown))),
        "shown_data": int(bool(SHOWN_DATA.search(shown))),
        "argument_title": int(bool(ARGUMENT.search(title) or t3.PHILOSOPHICAL.search(title))),
    }


def scores(s: dict[str, int]) -> dict[str, int]:
    return {"report": 3 * s["report_title"],
            "theorem": 2 * s["theorem_title"] + s["cites"] + s["shown_thm"] + s["derived"],
            "measurement": 2 * s["measurement_title"] + s["shown_strong"] + s["shown_data"],
            "argument": 2 * s["argument_title"]}


def classify(s: dict[str, int]) -> tuple[str, int]:
    """The class and its margin over the runner-up."""
    sc = scores(s)
    top = max(sc.values())
    if top == 0:
        return "argument", 0
    if s["report_title"]:
        # a title that reports someone's claim is a report whatever the evidence holds
        rest = max(v for k, v in sc.items() if k != "report")
        return "report", sc["report"] - rest
    evidence = s["cites"] + s["shown_thm"] + s["derived"]
    if sc["argument"] == top and sc["theorem"] == top and not evidence:
        return "argument", 0
    if sc["measurement"] == top and sc["theorem"] == top and s["measurement_title"]:
        return "measurement", 0
    order = sorted(sc.items(), key=lambda kv: (-kv[1], CLASSES.index(kv[0])))
    return order[0][0], order[0][1] - order[1][1]


def label_classes(text: str) -> list[str]:
    """A reviewer's sort note to the classes it accepts; a compound accepts either part."""
    v = text.lower()
    if v.startswith("report"):
        return ["report"]
    if re.match(r"(?:argument|explanatory|principle|thesis|general principle)", v):
        return ["argument"]
    out = []
    if re.search(r"theorem|derivation|identity|algebra|construction", v):
        out.append("theorem")
    if "measurement" in v:
        out.append("measurement")
    return out or ["theorem", "measurement"]


def labels(audit: Path) -> dict[str, tuple[list[str], str, str]]:
    """Reviewed THEORYs with a recorded sort: code -> (classes, reviewed revision, note).

    Batch files' `sort:` maps come first; decision files' `title_asserts` or
    `title_type` fill the rest. The revision is the decision's reviewed_revision.
    """
    notes: dict[str, str] = {}
    for f in sorted((audit / "batches").glob("batch-*.yaml")):
        sort = (yaml.safe_load(f.read_text()) or {}).get("sort")
        if isinstance(sort, dict):
            for code, val in sort.items():
                if str(code).startswith("THEORY-"):
                    notes.setdefault(str(code), str(val))
    revs: dict[str, str] = {}
    for f in sorted((audit / "decisions").glob("THEORY-*.yaml")):
        d = yaml.safe_load(f.read_text()) or {}
        revs[f.stem] = str(d.get("reviewed_revision") or "")
        v = d.get("title_asserts") or d.get("title_type")
        if v:
            notes.setdefault(f.stem, str(v))
    return {c: (label_classes(n), revs.get(c, ""), n) for c, n in sorted(notes.items())}


def class_precision_recall(rows: list[tuple[str, list[str]]]) -> dict:
    """(predicted, accepted) pairs to per-class counts; a compound label counts for each part."""
    out = {}
    for c in CLASSES:
        tp = sum(1 for p, ok in rows if p == c and c in ok)
        fp = sum(1 for p, ok in rows if p == c and c not in ok)
        fn = sum(1 for p, ok in rows if c in ok and p not in ok)
        out[c] = {"tp": tp, "fp": fp, "fn": fn, "precision": round(tp / max(1, tp + fp), 2),
                  "recall": round(tp / max(1, tp + fn), 2)}
    return out


def accuracy(rows: list[tuple[str, list[str]]]) -> float:
    return round(sum(1 for p, ok in rows if p in ok) / max(1, len(rows)), 2)


def control(rows: list[dict], size: int = 5) -> list[str]:
    """Every k-th sorted code of the argument and report classes, starting at k // 2."""
    pool = sorted(r["code"] for r in rows if r["class"] in ("argument", "report"))
    k = max(1, len(pool) // size)
    return pool[k // 2::k][:size]


def show(rev: str, code: str) -> str | None:
    try:
        return subprocess.check_output(["git", "show", f"{rev}:record/theory.d/{code}.md"], text=True,
                                       stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return None


def labelled_check(audit: Path) -> dict:
    """Classify each labelled entry as it stood when reviewed (git show at its reviewed_revision)."""
    rows, entries = [], []
    for code, (ok, rev, note) in labels(audit).items():
        text = show(rev, code) if rev else None
        if text is None:
            continue
        parts = text.split("---", 2)
        fm = (yaml.safe_load(parts[1]) or {}) if len(parts) == 3 else {}
        pred, margin = classify(signals(str(fm.get("title") or ""), parts[2] if len(parts) == 3 else ""))
        rows.append((pred, ok))
        entries.append({"code": code, "label": ok, "predicted": pred, "margin": margin,
                        "agree": pred in ok, "note": note[:90]})
    return {"fitted_to_these_labels": True, "n": len(rows), "accuracy": accuracy(rows),
            "per_class": class_precision_recall(rows), "entries": entries}


def main(record: str = "record", queue: str = "record/promotion-audit/queue.yaml", audit: str = "",
         out: str = "", top_theorem: int = 30, top_measurement: int = 20) -> None:
    root = Path(record)
    rows = t3.score_rows(root, t3.queued(Path(queue)))
    derived = t3.lit_derived(root)
    by_code = {p.stem: p for p in (root / "theory.d").glob("THEORY-*.md")}
    sorted_rows = []
    for r in rows:
        p = by_code[r["code"]]
        fm = t3.frontmatter(p)
        s = signals(str(fm.get("title") or ""), t3.body_of(p), t3.theory_derived(fm.get("source") or [], derived))
        cls, margin = classify(s)
        sorted_rows.append({"code": r["code"], "class": cls, "margin": margin, "scores": scores(s),
                            "signals": [k for k, v in s.items() if v], "rubric_score": r["score"],
                            "supports": r["supports"], "triage": "triage-007", "note": r["note"]})
    counts = {c: sum(1 for r in sorted_rows if r["class"] == c) for c in CLASSES}

    def route(c: str, n: int) -> list[dict]:
        rs = [r for r in sorted_rows if r["class"] == c]
        rs.sort(key=lambda r: (-r["margin"], -r["rubric_score"], -r["supports"], r["code"]))
        return rs[:n]

    by = {r["code"]: r for r in sorted_rows}
    result = {"eligible": len(sorted_rows), "counts": counts,
              "theorem_route": route("theorem", top_theorem),
              "measurement_route": route("measurement", top_measurement),
              "control": [by[c] for c in control(sorted_rows)]}
    if audit:
        result["labelled_check"] = labelled_check(Path(audit))
    logger.info(f"{len(sorted_rows)} eligible; {counts}")
    text = yaml.safe_dump(result, sort_keys=False, allow_unicode=True, width=100)
    if out:
        Path(out).write_text(text)
    else:
        print(text)


if __name__ == "__main__":
    fire.Fire(main)
