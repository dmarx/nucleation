"""Summarize results/runs_*.jsonl into results/summary.md and summary.json."""
import glob
import json
import os
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
R = 3


def load():
    recs = []
    for p in sorted(glob.glob(os.path.join(RES, "runs_*.jsonl"))):
        with open(p) as f:
            for line in f:
                try:
                    recs.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return recs


def ms(v, fmt="{:.3g}"):
    v = np.array([x for x in v if x is not None and np.isfinite(x)], float)
    if len(v) == 0:
        return "—"
    return (fmt + " [" + fmt + "–" + fmt + "]").format(np.median(v), v.min(), v.max())


def frac(v):
    v = list(v)
    return f"{sum(v)}/{len(v)}"


def main():
    recs = load()
    by = defaultdict(list)
    for r in recs:
        by[(r["rule"], r["K"], r["arm"])].append(r)
    rules = [x for x in ("moe", "moe_aux", "moe_bias", "rep", "uniform")
             if any(k[0] == x for k in by)]
    out = {}
    L = ["# LEAD-016 results", "",
         "Medians [min–max] over seeds. R is the rare context (p = 0.02). "
         "Risks are held-out relative risks (1 = predicting zero).", ""]

    L += ["## Differentiation (40,000 steps)", "",
          "| rule | K | seeds | I(op;ctx) | H(usage) | collective risk, common | collective risk, R | R specialist own risk | distinct R specialist | operators with usage > 1% | max share of a spare |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for rule in rules:
        for K in (4, 6):
            rs = by.get((rule, K, "diff"), [])
            if not rs:
                continue
            P = [np.array(r["P"]) for r in rs]
            orisk = [np.array(r["own_risk"]) for r in rs]
            spec = [int(p[R].argmax()) for p in P]
            distinct = [s not in set(p[:R].argmax(1)) and o[s, R] < 0.1
                        for s, p, o in zip(spec, P, orisk)]
            nused = [int((np.array(r["usage"]) > 0.01).sum()) for r in rs]
            spare = []
            for p in P:
                holders = set(p.argmax(1))
                others = [j for j in range(K) if j not in holders]
                spare.append(max([p[:, j].max() for j in others], default=0.0))
            L.append(f"| {rule} | {K} | {len(rs)} | {ms([r['MI'] for r in rs])} | "
                     f"{ms([r['H_usage'] for r in rs])} | "
                     f"{ms([np.mean(r['coll_risk'][:R]) for r in rs])} | "
                     f"{ms([r['coll_risk'][R] for r in rs])} | "
                     f"{ms([o[s, R] for o, s in zip(orisk, spec)])} | {frac(distinct)} | "
                     f"{ms(nused, '{:.0f}')} | {ms(spare)} |")
            out[f"{rule}/{K}/diff"] = {"distinct": int(sum(distinct)), "n": len(rs)}
    L.append("")

    L += ["## Recovery when rare (R specialist set to share ε in R, no further intervention, 20,000 steps ≈ 3,200 R samples)", "",
          "λ is the initial growth rate of log share per R sample; 'recovered' is final share > 0.5.", "",
          "| rule | K | arm | λ per R sample | R samples to share 0.5 | recovered | final share | R held at end by another operator, competent (own risk < 0.1) |",
          "|---|---|---|---|---|---|---|---|"]
    for rule in rules:
        for K in (4, 6):
            for arm in ("rare_frozen_e2", "rare_frozen_e3", "rare_frozen_e5", "rare_train_e3",
                        "sham_frozen_e3"):
                rs = by.get((rule, K, arm), [])
                if not rs:
                    continue
                L.append(f"| {rule} | {K} | {arm} | {ms([r['lam_cond'] for r in rs])} | "
                         f"{ms([r['nR_to_half'] for r in rs], '{:.0f}')} | "
                         f"{frac(r['final_share'] > 0.5 for r in rs)} | "
                         f"{ms([r['final_share'] for r in rs])} | "
                         f"{frac(r['traj'][-1][4] != r['spec'] and r['traj'][-1][3] < 0.1 for r in rs)} |")
                out[f"{rule}/{K}/{arm}"] = {
                    "lam": float(np.median([r["lam_cond"] for r in rs])),
                    "recovered": int(sum(r["final_share"] > 0.5 for r in rs)), "n": len(rs)}
    L.append("")

    L += ["## Removal of the R specialist (20,000 steps after)", "",
          "| rule | K | collective risk R, just after | collective risk R, end | collective risk common, end | R holder's own risk, end | refilled (risk R < 0.1) |",
          "|---|---|---|---|---|---|---|"]
    for rule in rules:
        for K in (4, 6):
            rs = by.get((rule, K, "remove"), [])
            if not rs:
                continue
            L.append(f"| {rule} | {K} | {ms([r['risk_after_removal'][R] for r in rs])} | "
                     f"{ms([r['traj'][-1][3] for r in rs])} | "
                     f"{ms([r['traj'][-1][5] for r in rs])} | "
                     f"{ms([r['holder_own_risk_R'] for r in rs])} | "
                     f"{frac(r['traj'][-1][3] < 0.1 for r in rs)} |")
            out[f"{rule}/{K}/remove"] = {
                "refilled": int(sum(r["traj"][-1][3] < 0.1 for r in rs)), "n": len(rs),
                "risk_end": float(np.median([r["traj"][-1][3] for r in rs]))}
    L.append("")

    L += ["## Suppression (QUESTION-134): share clamped at 10⁻³ in R for 20,000 steps, then released", "",
          "Access is the specialist's mean exposure per R sample during suppression. Competence is its own held-out risk in R.", "",
          "| rule | K | arm | access during | own risk R before | at release | end | R samples to share 0.5 after release | recovered | rival's own risk R at release |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for rule in rules:
        for K in (4, 6):
            for arm in ("suppress_coupled_wd0", "suppress_decoupled_wd0", "suppress_coupled_wd",
                        "suppress_decoupled_wd", "suppress_coupled_wd_frozen"):
                rs = by.get((rule, K, arm), [])
                if not rs:
                    continue
                L.append(f"| {rule} | {K} | {arm} | {ms([r['access_during'] for r in rs])} | "
                         f"{ms([r['own_risk_R_before'] for r in rs])} | "
                         f"{ms([r['own_risk_R_at_release'] for r in rs])} | "
                         f"{ms([r['own_risk_R_final'] for r in rs])} | "
                         f"{ms([r['nR_to_half'] for r in rs], '{:.0f}')} | "
                         f"{frac(r['final_share'] > 0.5 for r in rs)} | "
                         f"{ms([r['holder_risk_at_release'] for r in rs])} |")
                out[f"{rule}/{K}/{arm}"] = {
                    "risk_release": float(np.median([r["own_risk_R_at_release"] for r in rs])),
                    "recovered": int(sum(r["final_share"] > 0.5 for r in rs)), "n": len(rs)}
    L.append("")
    with open(os.path.join(RES, "summary.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(RES, "summary.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("\n".join(L))


if __name__ == "__main__":
    main()
