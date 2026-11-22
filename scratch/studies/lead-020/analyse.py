"""Summarise results.jsonl: per variant, which configurations lock in, which
are blind, the minimal loops that do not lock in, and which candidate's
removal from a loop that does not lock in makes it lock in.

    python3 -I analyse.py > summary.txt
"""

import json
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CANDS = ("sense", "capture", "body", "commit", "fluency", "others")
FREE, LOCK, BLIND = 0.05, 0.5, 0.5   # thresholds on lock-in rate / first-block tracking


def status(rec):
    if rec["first_block_tracked"] < BLIND or rec["lockin_mean"] is None:
        return "blind"
    li = rec["lockin_mean"]
    return "free" if li <= FREE else "locks" if li >= LOCK else "partial"


def remove(on, c):
    s = set(on) - {c}
    if c == "sense":
        s.discard("capture")
    return frozenset(s)


def main():
    by = defaultdict(dict)   # (variant, mode) -> {frozenset(on): rec}
    with open(os.path.join(HERE, "results.jsonl")) as f:
        for line in f:
            r = json.loads(line)
            on = frozenset(c for c in CANDS if r[c])
            mode = "commit" if r["no_commit_mode"] is None else r["no_commit_mode"]
            # loops with commitment belong to both readings of its absence
            for m in (("regimeA", "posthoc") if mode == "commit" else (mode,)):
                by[(r["variant"], m)][on] = r
    variants = sorted({v for v, _ in by}, key=lambda v: (v != "default", v))
    totals = defaultdict(lambda: defaultdict(int))
    for mode in ("regimeA", "posthoc"):
        print(f"\n######## no-commitment reading: {mode}")
        for v in variants:
            table = by.get((v, mode))
            if not table:
                continue
            st = {on: status(r) for on, r in table.items()}
            full = frozenset(CANDS)
            print(f"\n== {v}  (full loop: {st.get(full)}, lock-in {table[full]['lockin_mean']:.2f})"
                  if full in table else f"\n== {v}")
            singles = {c: st.get(remove(full, c)) for c in CANDS}
            print("  single removals from the full loop:", singles)
            # removal that makes a free loop lock in
            causes = defaultdict(list)
            minimal = []
            for on, s in st.items():
                if s != "free":
                    continue
                outs = {c: st.get(remove(on, c)) for c in on}
                for c, o in outs.items():
                    totals[(mode, c)]["removals_from_free"] += 1
                    if o == "locks":
                        causes[c].append(on)
                        totals[(mode, c)]["locks"] += 1
                    elif o == "blind":
                        totals[(mode, c)]["blind"] += 1
                    elif o == "partial":
                        totals[(mode, c)]["partial"] += 1
                if outs and all(o in ("locks", "blind", "partial") for o in outs.values()):
                    minimal.append((sorted(on), outs))
            print("  removal from a free loop -> locks in (count of free loops):",
                  {c: len(causes[c]) for c in CANDS})
            for on, outs in sorted(minimal):
                print("  minimal free loop:", "+".join(on), "| removing ->", outs)
            # adding a candidate to a free loop that makes it lock in
            harm = []
            for on, s in st.items():
                if s != "free":
                    continue
                for c in CANDS:
                    if c in on or (c == "capture" and "sense" not in on):
                        continue
                    t = on | {c}
                    if st.get(t) in ("locks", "partial"):
                        harm.append((c, "+".join(sorted(on)), st[t], round(table[t]["lockin_mean"], 2)))
            for h in sorted(harm):
                print("  adding", h[0], "to", h[1], "->", h[2], h[3])
    print("\n######## totals over variants: outcome of removing each candidate from a free loop")
    for (mode, c), d in sorted(totals.items()):
        print(f"  {mode:8s} {c:8s}", dict(d))


if __name__ == "__main__":
    main()
