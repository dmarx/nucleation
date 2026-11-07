# scratch/formal/synthesis_candidates.py: score the record for synthesis opportunities (the synthesis-review skill, stage 1)
# run: python3 -I scratch/formal/synthesis_candidates.py [--top N]
"""Stage 1 of a synthesis review is mechanical: it ranks places where an
integration may be hiding. It decides nothing. Stage 2, the audit and the
admission test of ADR-tmpe7y42, is judgement and is done by reading.

Arm A, migration candidates: CLAIMs that may be syntheses filed as claims.
  signals: premises (rests_on) spanning lines; premises that are themselves
  theses; the word "synthesis" or an account-shaped summary; a curation entry
  that says it filed a synthesis as a claim.

Arm B, unpersisted opportunities: integrations the record holds the parts of
but no entry states.
  B1 complements clusters: `complements` means "answers a different part of
     the same question", so a connected cluster of three to twelve in-force
     claims within one line is a synthesis in waiting (across lines the
     relation joins most of the record into one component);
  B2 questions with two or more in-force answers or bearings from different
     lines;
  B3 deep rests_on chains (depth >= 3) ending in an in-force thesis that no
     synthesis integrates.

Anything a SYNTHESIS already integrates is dropped from Arm B, and a CLAIM a
SYNTHESIS supersedes is dropped from Arm A.
"""
import collections
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
IN_FORCE = {"CLAIM": "Active", "QUESTION": "Open"}

def load(d):
    out = {}
    for f in sorted((ROOT / "record" / d).glob("*.md")):
        if f.name.startswith("_"):
            continue
        try:
            fm = yaml.safe_load(f.read_text().split("---")[1])
        except Exception:
            continue
        if isinstance(fm, dict):
            out[f.stem] = fm
    return out

def lst(v):
    return v if isinstance(v, list) else ([v] if v else [])

def main(top):
    claims, questions, syns = load("claims.d"), load("questions.d"), load("syntheses.d")
    integrated = {c for s in syns.values() for c in lst(s.get("integrates"))}
    superseded_into_syn = {c for s in syns.values() for c in lst(s.get("supersedes"))}
    live = {c: d for c, d in claims.items() if d.get("status") in ("Active", "Proposed")}
    line_of = {c: set(lst(d.get("line"))) for c, d in claims.items()}

    # ---- Arm A
    a_rows = []
    for c, d in live.items():
        if c in superseded_into_syn:
            continue
        prem = [p for p in lst(d.get("rests_on")) if p in claims]
        lines = set().union(*(line_of.get(p, set()) for p in prem)) | line_of[c]
        thesis_prem = [p for p in prem if claims[p].get("role") == "thesis"]
        text = (str(d.get("title", "")) + " " + str(d.get("summary", ""))).lower()
        words = sum(w in text for w in ("synthesis", "positive account", "the account", "integrat", "unif"))
        score = len(prem) + 2 * max(0, len(lines) - 1) + len(thesis_prem) + 3 * words
        if len(prem) >= 3 and len(lines) >= 2:
            a_rows.append((score, c, d.get("status"), len(prem), sorted(lines), words, str(d.get("title", ""))[:110]))
    a_rows.sort(reverse=True)

    # ---- Arm B1: complements clusters within one line, among in-force claims,
    # not already integrated. Across all lines, complements joins most of the
    # record into one component, which says nothing; within a line a cluster
    # is a set of claims answering parts of one question.
    clusters = []
    all_lines = sorted(set().union(*line_of.values()))
    for ln in all_lines:
        members = {c for c in live if ln in line_of[c]}
        adj = collections.defaultdict(set)
        for c in members:
            for o in lst(live[c].get("complements")):
                if o in members:
                    adj[c].add(o); adj[o].add(c)
        seen = set()
        for c in adj:
            if c in seen:
                continue
            comp, stack = set(), [c]
            while stack:
                x = stack.pop()
                if x in comp:
                    continue
                comp.add(x); stack.extend(adj[x] - comp)
            seen |= comp
            fresh = comp - integrated
            if 3 <= len(fresh) <= 12:
                edges = sum(len(adj[x] & comp) for x in comp) // 2
                clusters.append((edges, sorted(comp), [ln]))
    clusters.sort(reverse=True)

    # ---- Arm B2: questions with several in-force answers or bearings across lines
    q_rows = []
    for q, qd in questions.items():
        if qd.get("status") != "Open":
            continue
        ans = [c for c, d in live.items() if q in lst(d.get("answers")) + lst(d.get("bears_on"))]
        ans = [c for c in ans if c not in integrated]
        lines = set().union(*(line_of[c] for c in ans)) if ans else set()
        if len(ans) >= 3 and len(lines) >= 2:
            q_rows.append((len(ans) + len(lines), q, len(ans), sorted(lines), str(qd.get("title", ""))[:100]))
    q_rows.sort(reverse=True)

    # ---- Arm B3: deep rests_on chains ending in an in-force thesis
    depth_memo = {}
    def depth(c, stack=()):
        if c in depth_memo:
            return depth_memo[c]
        if c in stack or c not in claims:
            return 0
        ps = [p for p in lst(claims[c].get("rests_on")) if p in claims]
        v = 1 + max((depth(p, stack + (c,)) for p in ps), default=0)
        depth_memo[c] = v
        return v
    chains = sorted(((depth(c), c, str(d.get("title", ""))[:100]) for c, d in live.items()
                     if d.get("status") == "Active" and d.get("role") == "thesis" and c not in integrated
                     and depth(c) >= 3), reverse=True)

    print(f"# Synthesis candidates (stage 1, mechanical)\n\nclaims {len(claims)}, live {len(live)}, syntheses {len(syns)}\n")
    print(f"## Arm A: CLAIMs that may be syntheses ({len(a_rows)} with >=3 premises across >=2 lines; top {top})\n")
    for r in a_rows[:top]:
        print(f"- {r[1]} [{r[2]}] score {r[0]}: {r[3]} premises, lines {', '.join(r[4])}, account-words {r[5]}: {r[6]}")
    print(f"\n## Arm B1: complements clusters of 3-12 claims within one line, unintegrated ({len(clusters)}; top {top}, by edges)\n")
    for r in clusters[:top]:
        print(f"- {len(r[1])} claims, {r[0]} complements edges, line {r[2][0]}: {', '.join(r[1])}")
    print(f"\n## Arm B2: open questions with >=3 unintegrated answers/bearings across lines ({len(q_rows)}; top {top})\n")
    for r in q_rows[:top]:
        print(f"- {r[1]}: {r[2]} claims, lines {', '.join(r[3])}: {r[4]}")
    print(f"\n## Arm B3: Active theses at rests_on depth >= 3, unintegrated ({len(chains)}; top {top})\n")
    for r in chains[:top]:
        print(f"- {r[1]} depth {r[0]}: {r[2]}")

if __name__ == "__main__":
    n = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 12
    main(n)
