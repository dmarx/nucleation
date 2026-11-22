"""Summarize results/*.jsonl into results/summary.txt (python3 -I summarize.py)."""
import json
import os
from collections import defaultdict

import numpy as np
from scipy.stats import spearmanr

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, "results")
out = []
A = [json.loads(l) for l in open(os.path.join(R, "analogy.jsonl"))]
out.append("ANALOGY (median per family; null = random quadruples of the family's words)")
for d in A:
    out.append(f"{d['key']:28s} n={d['n']:5d} acc={d['acc_3cosadd']:.2f} int_share={d['rho_median']:.3f} "
               f"int_share_noise_corr={d['rho_corr_median']:.3f} null={d['rho_null_median']:.3f} "
               f"acc_by_int_tercile(low..high)={[round(x, 2) for x in d['acc_by_rho_tercile']]}")
acc = [d["acc_3cosadd"] for d in A]
rc = [d["rho_corr_median"] for d in A]
rho, p = spearmanr(acc, rc)
out.append(f"across families: Spearman(acc, int_share_noise_corr) = {rho:.2f} (p = {p:.3f}, n = {len(A)})")
low = np.mean([d["acc_by_rho_tercile"][0] for d in A])
high = np.mean([d["acc_by_rho_tercile"][2] for d in A])
out.append(f"within families: mean acc in lowest-interaction tercile {low:.2f}, highest {high:.2f}; "
           f"families where low > high: {sum(d['acc_by_rho_tercile'][0] > d['acc_by_rho_tercile'][2] for d in A)}/{len(A)}")

H = [json.loads(l) for l in open(os.path.join(R, "hierarchy.jsonl"))]
out.append("\nHIERARCHY")
for d in H:
    if d["key"] == "summary":
        out.append(json.dumps(d))
    elif d["key"].startswith("cv_"):
        out.append(f"{d['key']:14s} attrs={d['n_attrs']:4d} R2_cv={d['r2_cv']:.4f} permuted={np.mean(d['r2_cv_permuted']):.4f}")
probes = [d for d in H if d["key"].startswith("probe_")]
by = defaultdict(list)
for d in probes:
    by[(d["rank"], min(d["depth"], 9))].append(d)
for r in sorted({d["rank"] for d in probes}):
    row = []
    for dep in range(1, 10):
        g = by.get((r, dep), [])
        if g:
            row.append(f"d{dep}{'+' if dep == 9 else ''}:{np.mean([x['bal_acc'] for x in g]):.2f}(n{len(g)})")
    out.append(f"probe rank {r:3d} balanced acc by depth: " + " ".join(row))
    g = [d for d in probes if d["rank"] == r and "fp_in_parent" in d]
    if g:
        fp = np.mean([d["fp_in_parent"] for d in g])
        base = np.mean([d["neg_in_parent"] for d in g])
        out.append(f"   false positives inside the parent: {fp:.3f} vs parent's share of negatives {base:.3f} "
                   f"(enrichment {fp / base:.1f}x, {len(g)} attributes)")
pa = os.path.join(R, "hierarchy_alpha.jsonl")
if os.path.exists(pa):
    for l in open(pa):
        d = json.loads(l)
        out.append(f"refit {d['key']:22s} attrs={d['n_attrs']:4d} R2_cv={d['r2_cv']:.4f} permuted={d['r2_cv_permuted']:.4f}")
open(os.path.join(R, "summary.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
