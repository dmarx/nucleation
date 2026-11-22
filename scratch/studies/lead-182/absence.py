"""Size and power of the conservative absence bound (cbd.absence_upper_bound), LEAD-182.

Run from the repository root: python3 -I scratch/studies/lead-182/absence.py
Writes absence.jsonl a cell at a time and resumes; about a minute. Prints a table.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cbd  # noqa: E402
from power import lo_with_signalling, SIGNS  # noqa: E402

OUT = os.path.join(HERE, "absence.jsonl")
REPS = 4000
NS = (100, 400, 1000, 1600, 2500, 4000)


def main():
    done = set()
    if os.path.exists(OUT):
        done = {(r["model"], r["dc"], r["signal"], r["n"]) for r in map(json.loads, open(OUT))}
    i = 0
    for model in ("lo", "symmetric"):
        for dc in ([None] if model == "lo" else [-0.3, -0.15, 0.0, 0.1, 0.19]):
            for sig in (0.0, 0.1, 0.3, 0.6):
                for n in NS:
                    i += 1
                    if (model, dc, sig, n) in done:
                        continue
                    P = lo_with_signalling(sig) if model == "lo" else cbd.true_system(dc, sig)
                    rng = np.random.default_rng(1000 + i)
                    counts = np.stack([rng.multinomial(n, P[k], size=REPS) for k in range(4)], axis=1)
                    u = cbd.absence_upper_bound(counts, SIGNS)
                    rec = {"model": model, "dc": dc, "signal": sig, "n": n, "reps": REPS, "seed": 1000 + i,
                           "true_dc": float(cbd.delta_c(P, SIGNS)),
                           "absent_bonferroni": float((u < 0).mean())}
                    with open(OUT, "a") as f:
                        f.write(json.dumps(rec) + "\n")
    rows = [json.loads(l) for l in open(OUT)]
    g = {}
    for r in rows:
        g.setdefault((r["model"], round(r["true_dc"], 3), r["signal"]), {})[r["n"]] = r["absent_bonferroni"]
    print("| model | true Δ_C | signalling Δ | " + " | ".join(f"n={n}" for n in NS) + " |")
    print("|---|---|---|" + "---|" * len(NS))
    for k in sorted(g, key=lambda k: (k[1], k[2])):
        print(f"| {k[0]} | {k[1]:.3f} | {k[2]} | " + " | ".join(f"{g[k][n]:.3f}" for n in NS) + " |")


if __name__ == "__main__":
    main()
