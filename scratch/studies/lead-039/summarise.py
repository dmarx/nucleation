"""Summarise the LEAD-039 studies into results.md. python3 -I summarise.py"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(HERE, name)) as fh:
        return [json.loads(l) for l in fh if l.strip()]


out = ["# LEAD-039 results", ""]
s1 = load("s1_two_rows.jsonl")
out += ["## S1: two distinct rows of p(Y|x), |Y| = 2..6, grid 1/4000, 40 betas in [1.05, 80]", "",
        f"- sources: {len(s1)}; decoder intervals nested at every consecutive beta: "
        f"{sum(r['nested'] for r in s1)}; largest violation {max(r['max_violation'] for r in s1):.2e}",
        f"- by |Y|: " + ", ".join(f"{k}: {sum(r['ny'] == k for r in s1)}" for k in range(2, 7)),
        f"- mean number of betas with a nontrivial optimum (width > 3 grid steps): "
        f"{sum(r['nontrivial'] for r in s1) / len(s1):.1f} of 40", ""]
s2 = load("s2_three_states.jsonl")
out += ["## S2: three distinct rows, |Y| = 2 or 3, grid 1/300, 16 betas in [1.5, 60]", "",
        "L1 distance of the coarse decoder points from the fine hull (uncertified: optima not proved unique).", "",
        "| |Y| | sources | threshold | sources failing some adjacent pair | adjacent pairs failing | sources failing a far pair (5 steps apart) | sources with no failure at all |",
        "|---|---|---|---|---|---|---|"]
for ny in (2, 3):
    S = [r for r in s2 if r["ny"] == ny]
    for thr in (0.01, 0.02, 0.05):
        a = sum(max(r["adjacent"]) > thr for r in S)
        pf = sum(sum(x > thr for x in r["adjacent"]) for r in S)
        n = sum(len(r["adjacent"]) for r in S)
        f = sum(max(r["far"]) > thr for r in S)
        none = sum(max(r["adjacent"] + r["far"]) <= thr for r in S)
        out.append(f"| {ny} | {len(S)} | {thr} | {a} | {pf}/{n} | {f} | {none} |")
out += ["", "The three largest failures were recomputed on a grid of 1/700 and kept their size "
        "(0.302 -> 0.275, 0.183 -> 0.184, 0.164 -> 0.162).", ""]
s3 = load("s3_products.jsonl")
gaps = [x["gap"] for r in s3 for x in r["rows"]]
out += ["## S3: products of two independent two-row pairs, 4-state grid 1/40, beta in {2, 4, 8, 16}", "",
        f"- items: {len(s3)} ({len(gaps)} source-beta pairs)",
        f"- grid envelope minus the sum of the factors' envelopes: min {min(gaps):.1e}, max {max(gaps):.1e}",
        "  (tensorization predicts >= 0, and small at a fine enough grid)", ""]
with open(os.path.join(HERE, "results.md"), "w") as fh:
    fh.write("\n".join(out))
print("\n".join(out))
