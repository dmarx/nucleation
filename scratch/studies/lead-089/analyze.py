"""Summarize results/runs.jsonl into results/summary.json and a printed table.

    python3 -I analyze.py
"""
import json
import os
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "results", "runs.jsonl")
OUT = os.path.join(HERE, "results", "summary.json")
CONTROL = ["C0", "C1", "C2", "C3"]


def main():
    rows = [json.loads(l) for l in open(RUNS)]
    groups = defaultdict(list)
    for r in rows:
        groups[(r["world"], r["n"])].append(r)
    summary = []
    for (world, n), rs in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        ent = {"world": world, "n_per_arrangement": n, "seeds": len(rs)}
        # ln BF of WO against the best control-only model, per seed
        bf = [r["models"]["WO"]["log_evidence"]
              - max(r["models"][c]["log_evidence"] for c in CONTROL) for r in rs]
        best_c = [max(CONTROL, key=lambda c: r["models"][c]["log_evidence"]) for r in rs]
        ent["lnBF_WO_vs_best_control"] = {
            "median": float(np.median(bf)), "min": float(np.min(bf)),
            "max": float(np.max(bf)), "WO_wins": int(sum(b > 0 for b in bf))}
        ent["best_control_by_evidence"] = {c: best_c.count(c) for c in CONTROL}
        for key in ("lp_seen", "lp_new"):
            ent[key] = {}
            for m in ["WO"] + CONTROL:
                gap = [r["truth"][key] - r["models"][m][key] for r in rs]
                ent[key][m] = float(np.mean(gap))  # nats/episode above truth
        ent["lp_new_WO_minus_best_control"] = float(np.mean(
            [r["models"]["WO"]["lp_new"] - max(r["models"][c]["lp_new"] for c in CONTROL)
             for r in rs]))
        summary.append(ent)
    with open(OUT, "w") as fh:
        json.dump(summary, fh, indent=1)
    print(f"{'world':14s} {'n':>5s} {'lnBF med':>9s} {'[min,max]':>18s} {'WO wins':>7s}  "
          "regret on unseen arrangements, nats/episode: WO C0 C1 C2 C3")
    for e in summary:
        b = e["lnBF_WO_vs_best_control"]
        g = e["lp_new"]
        print(f"{e['world']:14s} {e['n_per_arrangement']:5d} {b['median']:9.1f} "
              f"[{b['min']:7.1f},{b['max']:7.1f}] {b['WO_wins']:4d}/{e['seeds']}  "
              + " ".join(f"{g[m]:.3f}" for m in ["WO"] + CONTROL))


if __name__ == "__main__":
    main()
