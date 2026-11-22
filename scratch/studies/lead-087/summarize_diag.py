"""Post hoc summary of diagnostics.jsonl (and of the pre-registered run,
as variant 'base'): per variant and arm, s_u, s_w, sigma, recovery over
independent, rho, and the paired contrast of sigma against conform.

    python3 -I summarize_diag.py
"""
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ARMS = ("conform", "enforce", "evidential")


def ci(x):
    x = np.asarray(x, float)
    m, se = x.mean(), x.std(ddof=1) / np.sqrt(len(x))
    return f"{m:+.3f} [{m - 1.96 * se:+.3f}, {m + 1.96 * se:+.3f}]"


rows = [dict(json.loads(l), variant="base")
        for l in open(os.path.join(HERE, "results.jsonl"))]
rows += [json.loads(l) for l in open(os.path.join(HERE, "diagnostics.jsonl"))]
by = {}
for r in rows:
    by.setdefault(r["variant"], {}).setdefault(r["arm"], {})[r["seed"]] = r
for v, arms in by.items():
    seeds = sorted(arms["independent"])
    print(f"\n### {v} ({len(seeds)} seeds)")
    for arm in ARMS:
        A = arms[arm]
        print(f"  {arm:10s} s_u {ci([A[s]['s_u'] for s in seeds])}"
              f"  s_w {ci([A[s]['s_w'] for s in seeds])}"
              f"  sigma {ci([A[s]['s_w'] - A[s]['s_u'] for s in seeds])}"
              f"  g-g_ind {ci([A[s]['g_u'] - arms['independent'][s]['g_u'] for s in seeds])}"
              f"  rho {ci([A[s]['s_u'] / A[s]['g_u'] for s in seeds])}")
    for arm in ("enforce", "evidential"):
        d = [(arms[arm][s]["s_w"] - arms[arm][s]["s_u"])
             - (arms["conform"][s]["s_w"] - arms["conform"][s]["s_u"])
             for s in seeds]
        print(f"  sigma({arm}) - sigma(conform): {ci(d)}")
