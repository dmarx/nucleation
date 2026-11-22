"""Summarize part 2, split into clean runs and degenerate ones, with Theorem C's full hypothesis.
Run: python3 -I analyze_part2.py   (writes results/part2_analysis.json)"""
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, "results")
runs = [json.loads(l) for l in open(os.path.join(R, "part2_runs.jsonl")) if l.strip()]
cc = {(r["k"], r["w"], r["seed"]): r for r in
      (json.loads(l) for l in open(os.path.join(R, "condC_check.jsonl")) if l.strip())}


def clean(r):
    return r["theorem_A"]["holds"] and r["grad_norm_free"] < 1e-8 and r["gram_min_eig"] > 1e-6


out = {}
for label, sel in (("clean", [r for r in runs if clean(r)]), ("degenerate", [r for r in runs if not clean(r)])):
    rems = [(r, x, cc[(r["k"], r["w"], r["seed"])]["removals"][x["i"]]) for r in sel for x in r["removals"]]
    out[label] = dict(
        runs=[f"k={r['k']},w={r['w']},s={r['seed']}" for r in sel],
        min_trait_gap=min(r["min_trait_gap"] for r in sel),
        max_jacobian_re=max(r["theorem_A"]["jac_max_re"] for r in sel),
        max_jac_pred_gap=max(abs(r["theorem_A"]["jac_max_re"] - r["theorem_A"]["pred_max_re"]) for r in sel),
        n_removals=len(rems),
        frozen_positive=sum(x["lam_frozen"] > 0 for _, x, _ in rems),
        frozen_ge_bound=sum(x["lam_frozen"] >= x["bound"] - 1e-9 for _, x, _ in rems),
        frozen_secondary=sum(x["secondary"] for _, x, _ in rems),
        adapted_positive=sum(x["lam_adapted"] > 0 for _, x, _ in rems),
        adapted_over_frozen=[float(np.min([x["lam_adapted"] / x["lam_frozen"] for _, x, _ in rems if x["lam_frozen"] > 1e-9] or [np.nan])),
                             float(np.median([x["lam_adapted"] / x["lam_frozen"] for _, x, _ in rems if x["lam_frozen"] > 1e-9] or [np.nan]))],
        max_trait_shift=max(x["trait_shift"] for _, x, _ in rems),
        hypothesis_C=sum(c["hypothesis_C"] for _, _, c in rems),
        recovered_half=sum(x["recovered_fraction"] > 0.5 for _, x, _ in rems),
        returned_to_same_L=sum(abs(x["L_return_gap"]) < 1e-8 for _, x, _ in rems),
        per_run=[dict(run=f"k={r['k']},w={r['w']}", min_adapted=min(x["lam_adapted"] for x in r["removals"]),
                      min_frozen=min(x["lam_frozen"] for x in r["removals"]),
                      min_recovered=min(x["recovered_fraction"] for x in r["removals"]),
                      grad=r["grad_norm_free"], gram_min=r["gram_min_eig"], gap=r["min_trait_gap"])
                 for r in sel if r["seed"] == 0],
    )
json.dump(out, open(os.path.join(R, "part2_analysis.json"), "w"), indent=1)
print(json.dumps(out, indent=1))
