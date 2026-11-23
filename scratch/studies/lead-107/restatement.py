"""LEAD-107: restatement events in the workbench reconstructions.

Codes each restatement event the reconstructions report (re-derived as new,
retrieved by citation, conflicting cues, or neutral), whether its item had a
code when it was restated, and, where the restatement is quoted, its lexical
distance from the coded original. Rules: CODEBOOK.md. Reads only.

    python3 -I scratch/studies/lead-107/restatement.py --root . \
        --out scratch/studies/lead-107/results.json
"""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from scipy import stats

ITEM_KINDS = ("CLAIM", "TERM", "QUESTION", "CASE", "ARG", "THEORY", "LIT", "NOTE")
KIND_DIR = {
    "CLAIM": "claims.d", "TERM": "terms.d", "QUESTION": "questions.d",
    "CASE": "cases.d", "ARG": "arguments.d", "THEORY": "theory.d",
    "LIT": "literature.d", "NOTE": "notes.d",
}
CODE_RE = re.compile(r"\b(" + "|".join(ITEM_KINDS) + r")-(\d+)\b")
LINK_RE = re.compile(r"\[([A-Z]+-[0-9a-z]+)\]\([^)]*\)")
LABEL_RE = re.compile(r"\b[UATB]\d{1,3}\b")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
TITLE_START = re.compile(r"^(Session|Sessions|Exchange|The exchange|Branch)\b")

NEW_PATTERNS = [
    r"\bre-?deriv\w*", r"\bas though new\b", r"\bas if new\b", r"\bas new\b",
    r"\bwithout citing\b", r"\bwithout citation\b", r"\bwithout its code\b",
    r"\buncited\b", r"\bnot cited\b", r"\bcited little\b", r"\bcited none\b",
    r"\bwithout (a )?back-?reference\b", r"\brediscover\w*", r"\bre-?propos\w*",
    r"\breintroduc\w*", r"\bre-?recommend\w*", r"\bre-ask\w*", r"\bunlinked\b",
]
PROOF_RE = re.compile(r"proof|by hand|checker|script|numeric|\.py\b|computed|step by step", re.I)
PROPOSAL_RE = re.compile(r"\bpropos\w*|\brecommend\w*|\boffer\w*|\bput forward\b|\bpresent\w*|\bsuggest\w*", re.I)
RETRIEVED_PATTERNS = [r"\bby its code\b", r"\bwith its code\b", r"\bpoint(ing|s) back\b", r"\brecap\w*"]
CITE_RE = re.compile(r"\bcit(es|ed|ing)\b", re.I)
RECUR_PATTERNS = [
    r"\brestat\w*", r"\b(came|comes|come) back\b", r"\brecur\w*", r"\bagain\b",
    r"\balready held\b", r"\bduplicat\w*", r"\brepeat\w*",
    r"\b(second|third|fourth|fifth|sixth) time\b",
    r"\b(\d+|two|three|four|five|six|seven|eight) (or more )?times\b",
]

STOP = set("""a an the and or of to in on at by for with from as is are was were be
been being it its this that these those which who whom what not no nor but if
then than so such into onto over under about between through their there they
them his her he she we our you your i me my do does did done has have had can
could may might must shall should will would one two all any each every some
more most less only also just even very own same other another where when how
why while whose""".split())


def strip_frontmatter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return yaml.safe_load(text[3:end]) or {}, text[end + 4:]
    return {}, text


def normalise(body: str) -> str:
    body = re.sub(r"<!--.*?-->", " ", body, flags=re.S)
    return LINK_RE.sub(r"\1", body)


def is_exchange_reconstruction(meta: dict, body: str) -> bool:
    title = str(meta.get("title", ""))
    if not TITLE_START.match(title):
        return False
    labels = len(LABEL_RE.findall(body))
    return labels >= 10 or "shared exchange" in body


def exchange_date(meta: dict) -> tuple[str, bool]:
    m = DATE_RE.search(str(meta.get("title", "")))
    if m:
        return m.group(0), False
    return str(meta.get("created", ""))[:10], True


def sentences(body: str) -> list[str]:
    out = []
    # bullets and blank lines are hard boundaries; wrapped lines are joined
    blocks = re.split(r"\n\s*\n|\n\s*[-*] |\n\s*\d+\. |\n\s*\|", body)
    for block in blocks:
        block = re.sub(r"^[-*]\s+", "", " ".join(block.split()))
        if not block:
            continue
        for s in re.split(r"(?<=[.;?!])\s+(?=[A-Z\"“(\[*])", block):
            s = s.strip()
            if s:
                out.append(s)
    return out


def _any(patterns, s):
    return any(re.search(p, s, re.I) for p in patterns)


NEGATORS_V1 = ("without", "not", "never")
NEGATORS_V2 = NEGATORS_V1 + ("no", "none", "nothing")
META_RE = re.compile(r"\brecurring (strength|weakness)", re.I)
STATUS_AGAIN_RE = re.compile(r"\b(Proposed|Active|Deferred|status\w*) again\b", re.I)


def has_retrieved_cue(s: str, rules: str = "v1") -> bool:
    if rules == "v2" and not (CODE_RE.search(s) or LABEL_RE.search(s)):
        return False
    if _any(RETRIEVED_PATTERNS, s):
        return True
    negators = NEGATORS_V2 if rules == "v2" else NEGATORS_V1
    for m in CITE_RE.finditer(s):
        before = s[: m.start()].lower().split()[-3:]
        after = s[m.end():].lower().split()[:1]
        if any(w in negators or w.startswith("un") for w in before):
            continue
        if after and after[0].strip(".,;") in ("little", "none"):
            continue
        return True
    return False


def has_new_cue(s: str) -> bool:
    for p in NEW_PATTERNS:
        if re.search(p, s, re.I):
            if p.startswith(r"\bre-?deriv") and PROOF_RE.search(s):
                continue
            return True
    if re.search(r"\balready held\b", s, re.I) and (LABEL_RE.search(s) or PROPOSAL_RE.search(s)):
        return True
    return False


def classify(s: str, rules: str = "v1") -> str | None:
    """Y for a sentence, or None when it is not a restatement event.

    v1 is the codebook as fixed before the run; v2 adds the four post-hoc
    repairs listed in CODEBOOK.md ("Deviation: rules v2")."""
    if rules == "v2":
        if META_RE.search(s):
            return None
        s_rec = STATUS_AGAIN_RE.sub(" ", s)
    else:
        s_rec = s
    new, ret, rec = has_new_cue(s), has_retrieved_cue(s, rules), _any(RECUR_PATTERNS, s_rec)
    if new and ret:
        return "conflict"
    if new:
        return "new"
    if ret and rec:
        return "retrieved"
    if rec:
        return "neutral"
    return None


def items_of(s: str) -> list[str]:
    seen = []
    for kind, num in CODE_RE.findall(s):
        code = f"{kind}-{int(num):03d}"
        if code not in seen:
            seen.append(code)
    return seen


def coded_at_time(code_date: str | None, ex_date: str, same_day_coded: bool = False) -> bool:
    if not code_date:
        return False
    return code_date < ex_date or (same_day_coded and code_date == ex_date)


# ---- distance -------------------------------------------------------------

QUOTE_RE = re.compile(r"\"([^\"]+)\"|“([^”]+)”")


def stem(w: str) -> str:
    for suf in ("ations", "ation", "ings", "ing", "edly", "ed", "ies", "es", "ly", "s"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def content_stems(text: str) -> list[str]:
    return [stem(w) for w in re.findall(r"[a-z]+", text.lower()) if w not in STOP and len(w) > 1]


def quotes(s: str) -> list[str]:
    return [a or b for a, b in QUOTE_RE.findall(s)]


def char_ngrams(text: str, n: int = 4) -> Counter:
    t = " ".join(re.findall(r"[a-z]+", text.lower()))
    return Counter(t[i:i + n] for i in range(max(0, len(t) - n + 1)))


def distance(restatement: str, original: str) -> dict:
    a, b = set(content_stems(restatement)), set(content_stems(original))
    jac = len(a & b) / len(a | b) if a | b else 0.0
    ca, cb = char_ngrams(restatement), char_ngrams(original)
    dot = sum(ca[k] * cb[k] for k in ca)
    na = math.sqrt(sum(v * v for v in ca.values()))
    nb = math.sqrt(sum(v * v for v in cb.values()))
    cos = dot / (na * nb) if na and nb else 0.0
    cov = len(a & b) / len(a) if a else 0.0
    return {"d_jac": 1 - jac, "d_chr": 1 - cos, "d_cov": 1 - cov}


# ---- record access --------------------------------------------------------

def load_entry(root: Path, code: str) -> dict | None:
    kind = code.split("-")[0]
    p = root / "record" / KIND_DIR[kind] / f"{code}.md"
    if not p.exists():
        return None
    meta, _ = strip_frontmatter(p.read_text(encoding="utf-8"))
    return {"date": str(meta.get("date", ""))[:10] or None,
            "title": str(meta.get("title", "")), "summary": str(meta.get("summary", ""))}


def extract_events(root: Path, rules: str = "v1") -> tuple[list[dict], list[dict]]:
    events, corpus = [], []
    for p in sorted((root / "record" / "workbench.d").rglob("*.md")):
        if p.name.startswith("_"):
            continue
        meta, body = strip_frontmatter(p.read_text(encoding="utf-8"))
        body = normalise(body)
        if not is_exchange_reconstruction(meta, body):
            continue
        ex_date, uncertain = exchange_date(meta)
        rel = str(p.relative_to(root))
        corpus.append({"file": rel, "date": ex_date, "date_uncertain": uncertain})
        for i, s in enumerate(sentences(body)):
            y = classify(s, rules)
            if y is None:
                continue
            events.append({"file": rel, "ex_date": ex_date, "date_uncertain": uncertain,
                           "sent": i, "y": y, "items": items_of(s), "text": s})
    return events, corpus


# ---- analysis -------------------------------------------------------------

def fisher(a, b, c, d):
    if min(a + b, c + d) == 0:
        return None
    return float(stats.fisher_exact([[a, b], [c, d]])[1])


def collapse(events, entries, same_day_coded=False, exclude_uncertain=False):
    units = {}
    order = {"new": 3, "retrieved": 2, "conflict": 1, "neutral": 0}
    anon = []
    for e in events:
        if exclude_uncertain and e["date_uncertain"]:
            continue
        if not e["items"]:
            anon.append({"y": e["y"], "coded": False, "anon": True})
            continue
        for code in e["items"]:
            ent = entries.get(code)
            coded = coded_at_time(ent["date"] if ent else None, e["ex_date"], same_day_coded)
            key = (e["file"], code)
            if key not in units or order[e["y"]] > order[units[key]["y"]]:
                units[key] = {"y": e["y"], "coded": coded}
    return list(units.values()) + anon


def coded_table(units):
    t = {g: Counter(u["y"] for u in units if u["coded"] == g) for g in (True, False)}
    out = {}
    for g, name in ((True, "coded"), (False, "uncoded")):
        c = t[g]
        nr = c["new"] + c["retrieved"]
        out[name] = {**{k: c[k] for k in ("new", "retrieved", "conflict", "neutral")},
                     "p_new_of_new_or_retrieved": round(c["new"] / nr, 3) if nr else None}
    out["fisher_p"] = fisher(t[True]["new"], t[True]["retrieved"], t[False]["new"], t[False]["retrieved"])
    return out


def before_after(events, entries, corpus):
    by_code = defaultdict(lambda: {"pre": Counter(), "post": Counter(), "pre_files": set(), "post_files": set()})
    for e in events:
        for code in e["items"]:
            ent = entries.get(code)
            if not ent or not ent["date"]:
                continue
            side = "post" if ent["date"] < e["ex_date"] else "pre"
            by_code[code][side][e["y"]] += 1
            by_code[code][side + "_files"].add(e["file"])
    dates = sorted(c["date"] for c in corpus)
    rows = []
    for code, v in sorted(by_code.items()):
        d = entries[code]["date"]
        rows.append({"code": code, "date": d,
                     "pre": dict(v["pre"]), "post": dict(v["post"]),
                     "post_exposure": sum(1 for x in dates if x > d)})
    both = [r for r in rows if r["pre"] and r["post"]]
    pre_new = [r for r in rows if r["pre"].get("new")]
    summary = {
        "codes_with_events": len(rows),
        "codes_with_pre_events": sum(1 for r in rows if r["pre"]),
        "codes_with_post_events": sum(1 for r in rows if r["post"]),
        "codes_with_both": len(both),
        "codes_rederived_pre": len(pre_new),
        "of_those_rederived_again_post": sum(1 for r in pre_new if r["post"].get("new")),
        "of_those_cited_post": sum(1 for r in pre_new if r["post"].get("retrieved")),
        "of_those_any_post_event": sum(1 for r in pre_new if r["post"]),
        "pre_totals": dict(sum((Counter(r["pre"]) for r in rows), Counter())),
        "post_totals": dict(sum((Counter(r["post"]) for r in rows), Counter())),
    }
    return summary, both


def distance_rows(events, entries):
    rows = []
    for e in events:
        if len(e["items"]) != 1:
            continue
        q = " ".join(quotes(e["text"]))
        if len(content_stems(q)) < 3:
            continue
        ent = entries.get(e["items"][0])
        if not ent:
            continue
        d1 = distance(q, ent["title"])
        d2 = distance(q, ent["title"] + " " + ent["summary"])
        rows.append({"file": e["file"], "sent": e["sent"], "code": e["items"][0], "y": e["y"],
                     "coded": coded_at_time(ent["date"], e["ex_date"]),
                     **{k: round(v, 3) for k, v in d1.items()},
                     **{k + "_ts": round(v, 3) for k, v in d2.items()}})
    return rows


def compare(rows, key, a="new", b="retrieved"):
    xa = [r[key] for r in rows if r["y"] == a]
    xb = [r[key] for r in rows if r["y"] == b]
    if not xa or not xb:
        return {"n_" + a: len(xa), "n_" + b: len(xb)}
    u, p = stats.mannwhitneyu(xa, xb, alternative="two-sided")
    return {"n_" + a: len(xa), "n_" + b: len(xb),
            "median_" + a: round(float(sorted(xa)[len(xa) // 2]), 3),
            "median_" + b: round(float(sorted(xb)[len(xb) // 2]), 3),
            "auc_" + a + "_further": round(float(u) / (len(xa) * len(xb)), 3), "p": round(float(p), 4)}


def analyse(root: Path, rules: str = "v1") -> dict:
    events, corpus = extract_events(root, rules)
    codes = sorted({c for e in events for c in e["items"]})
    entries = {c: ent for c in codes if (ent := load_entry(root, c))}
    primary = collapse(events, entries)
    drows = distance_rows(events, entries)
    ba_summary, ba_both = before_after(events, entries, corpus)
    res = {
        "rules": rules,
        "corpus": {"reconstructions": len(corpus),
                   "date_uncertain": sum(c["date_uncertain"] for c in corpus),
                   "files": [c["file"] for c in corpus]},
        "events": {"sentences": len(events), "by_y": dict(Counter(e["y"] for e in events)),
                   "with_codes": sum(1 for e in events if e["items"]),
                   "codes_missing_from_record": sorted(set(codes) - set(entries))},
        "coded_vs_uncoded": {
            "primary": coded_table(primary),
            "same_day_coded": coded_table(collapse(events, entries, same_day_coded=True)),
            "exclude_uncertain_dates": coded_table(collapse(events, entries, exclude_uncertain=True)),
            "named_items_only": coded_table([u for u in primary if not u.get("anon")]),
        },
        "before_after": {"summary": ba_summary, "codes_with_both": ba_both},
        "distance": {
            "n": len(drows),
            "title": {k: compare(drows, k) for k in ("d_jac", "d_chr", "d_cov")},
            "title_summary": {k: compare(drows, k + "_ts") for k in ("d_jac", "d_chr", "d_cov")},
            "new_vs_neutral_title": {k: compare(drows, k, "new", "neutral") for k in ("d_jac", "d_chr", "d_cov")},
            "rows": drows,
        },
    }
    return res, events


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default="scratch/studies/lead-107/results.json")
    ap.add_argument("--events", default="scratch/studies/lead-107/events.jsonl")
    ap.add_argument("--rules", choices=("v1", "v2"), default="v1")
    args = ap.parse_args()
    root = Path(args.root)
    res, events = analyse(root, args.rules)
    Path(args.out).write_text(json.dumps(res, indent=1, sort_keys=True) + "\n")
    with open(args.events, "w") as f:
        for e in events:
            f.write(json.dumps({k: (v[:160] if k == "text" else v) for k, v in e.items()}) + "\n")
    show = {k: v for k, v in res.items() if k != "distance"}
    show["distance"] = {k: v for k, v in res["distance"].items() if k != "rows"}
    show["before_after"] = {"summary": res["before_after"]["summary"]}
    show["corpus"] = {k: v for k, v in res["corpus"].items() if k != "files"}
    print(json.dumps(show, indent=1))


if __name__ == "__main__":
    main()
