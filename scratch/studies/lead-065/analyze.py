"""Summarize results/runs.json into results/summary.md (tables, across seeds).

Usage: python3 -I analyze.py [results/runs.json]
"""

import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ARMS = ["control", "remove_periph", "remove_core", "remove_half_core", "suppress_core"]


def stat(vals, nd=1):
    v = np.asarray(vals, dtype=float)
    sd = v.std(ddof=1) if len(v) > 1 else 0.0
    lo = f"{v.min():.0f}" if nd == 1 else f"{v.min():.{nd}f}"
    hi = f"{v.max():.0f}" if nd == 1 else f"{v.max():.{nd}f}"
    return f"{v.mean():.{nd}f} ± {sd:.{nd}f} [{lo}–{hi}]"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "results", "runs.json")
    d = json.load(open(path))
    runs, meta = d["runs"], d["meta"]
    L = []
    L.append(f"# LEAD-065 results ({len(runs)} seeds)\n")
    L.append(f"Parameters: {json.dumps(meta)}\n")
    L.append("Cells: mean ± sd [min–max] across seeds. Core = time-averaged W_out > 1 "
             f"over the last {meta['win']} steps; 'snap' = the paper's snapshot criterion "
             "(out-degree > 20 (M-1)/99).\n")

    g = [r["grown"] for r in runs]
    L.append("## At the end of growth (t0)\n")
    L.append("| quantity | value |\n|---|---|")
    L.append(f"| core size (W_out > 1) | {stat([x['core_size'] for x in g])} |")
    L.append(f"| core size (snapshot, paper) | {stat([x['snap_core_size'] for x in g])} |")
    L.append(f"| units on which the two criteria agree (of 100) | {stat([r['snap_core_agrees'] for r in runs])} |")
    L.append(f"| core size 10^6 steps earlier | {stat([r['core_early_size'] for r in runs])} |")
    L.append(f"| of the final core, also core 10^6 steps earlier | {stat([r['core_overlap_early_late'] for r in runs])} |")
    for b in ["CC", "CP", "PC", "PP"]:
        L.append(f"| snapshot {b} strong connections | {stat([x['snap_blocks'][b] for x in g])} |")
    gaps = []
    for x in g:
        wo = np.asarray(x["wout_sorted"])
        k = x["core_size"]
        gaps.append(wo[k - 1] / max(wo[k], 1e-12))
    L.append(f"| W_out ratio, smallest core unit to largest periphery unit | {stat(gaps, 2)} |")
    L.append("")

    cps = [rec["t"] for rec in runs[0]["arms"]["control"]]
    L.append("## After the intervention\n")
    L.append("k = original core size. 'from periphery' = units in the core now that were "
             "periphery at t0; 'from core' = units in the core now that were core at t0.\n")
    L.append("| arm | t after | units M | core size | from core | from periphery | snap core | snap PC |")
    L.append("|---|---|---|---|---|---|---|---|")
    summary = {}
    for arm in ARMS:
        for i, t in enumerate(cps):
            recs = [r["arms"][arm][i] for r in runs]
            row = {
                "M": [x["M"] for x in recs],
                "core": [x["core_size"] for x in recs],
                "from_core": [x["core_from_orig_core"] for x in recs],
                "from_periph": [x["core_from_orig_periph"] for x in recs],
                "snap": [x["snap_core_size"] for x in recs],
                "snapPC": [x["snap_blocks"]["PC"] for x in recs],
            }
            summary[f"{arm}@{t}"] = {k: v for k, v in row.items()}
            L.append(f"| {arm} | {t:,} | {stat(row['M'])} | {stat(row['core'])} | "
                     f"{stat(row['from_core'])} | {stat(row['from_periph'])} | "
                     f"{stat(row['snap'])} | {stat(row['snapPC'])} |")
    L.append("")

    # refill ratios at the last checkpoint
    last = len(cps) - 1
    k0 = np.array([x["core_size"] for x in g], float)
    rc = np.array([r["arms"]["remove_core"][last]["core_size"] for r in runs], float)
    rp = np.array([r["arms"]["remove_periph"][last]["core_size"] for r in runs], float)
    ctl = np.array([r["arms"]["control"][last]["core_size"] for r in runs], float)
    hc = np.array([r["arms"]["remove_half_core"][last]["core_size"] for r in runs], float)
    sup_c = np.array([r["arms"]["suppress_core"][last]["core_from_orig_core"] for r in runs], float)
    sup_p = np.array([r["arms"]["suppress_core"][last]["core_from_orig_periph"] for r in runs], float)
    L.append(f"## Ratios at t = {cps[last]:,} after the intervention\n")
    L.append("| ratio | value |\n|---|---|")
    L.append(f"| remove_core: new core / original core | {stat(rc / k0, 2)} |")
    L.append(f"| remove_core: new core / remove_periph core (same M) | {stat(rc / rp, 2)} |")
    L.append(f"| remove_half_core: core / original core | {stat(hc / k0, 2)} |")
    L.append(f"| control: core / original core | {stat(ctl / k0, 2)} |")
    L.append(f"| suppress_core: original-core share of core | {stat(sup_c / (sup_c + sup_p), 2)} |")
    L.append(f"| seeds in which remove_core's core has at least half the original size | "
             f"{int((rc >= 0.5 * k0).sum())} of {len(runs)} |")
    out = os.path.join(os.path.dirname(path), "summary.md")
    open(out, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
