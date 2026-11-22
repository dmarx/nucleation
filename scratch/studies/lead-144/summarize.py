"""Summarize results.jsonl: mean (and sd) over seeds, per world and arm."""
import json
import sys

import numpy as np

rows = [json.loads(line) for line in open(sys.argv[1]) if line.strip()]
# An organization whose coupled world is not stationary (spectral radius of
# the coupling >= 1) gives NaN there and a degenerate matched null; drop the
# seed from every world.
bad = {r["seed"] for r in rows if r["world"] == "coupled" and r["within_corr"] != r["within_corr"]}
if bad:
    print(f"dropped seeds (coupled world not stationary): {sorted(bad)}\n")
rows = [r for r in rows if r["seed"] not in bad]
worlds = ["coupled", "driver", "mixed"]
metrics = ["pulse_rmse_heldout", "cut_mae", "pred_cut_mean", "r2_onestep",
           "n_features", "group_jaccard", "offdiag_abs_mean"]
for w in worlds:
    rs = [r for r in rows if r["world"] == w]
    if not rs:
        continue
    print(f"## {w} (n = {len(rs)} seeds)")
    print(f"  true within-group corr {np.mean([r['within_corr'] for r in rs]):.3f}; "
          f"true cut change {np.mean([r['true_cut_mean'] for r in rs]):+.3f}; "
          f"true |spill| h=1 {np.mean([r['true_spill_h1'] for r in rs]):.4f}")
    for m in metrics:
        arms = rs[0][m].keys()
        cells = []
        for a in arms:
            v = np.array([r[m][a] for r in rs], float)
            cells.append(f"{a} {v.mean():.3f}±{v.std(ddof=1) if len(v) > 1 else 0:.3f}")
        print(f"  {m}: " + "; ".join(cells))
    print()
