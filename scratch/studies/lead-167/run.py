"""LEAD-167: Bourrat's two individuality measures on a scaffolding model.

python3 -I run.py  ->  results.json, summary.txt (about a minute on a CPU).
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import coarse  # noqa: E402
import measures as M  # noqa: E402
import model  # noqa: E402

LAMS = [0.0, 0.25, 0.5, 0.75, 0.875, 1.0]
HORIZONS = [1, 4]
KAPPAS = np.round(np.arange(0.0, 0.0501, 0.0005), 4)
CANDIDATES = {
    "cell": [0],
    "pair-in-patch": [0, 1],
    "patch": [0, 1, 2],
    "patch+scaffold": [0, 1, 2, 6],
    "cross-pair": [0, 3],
    "cross-triple": [0, 1, 3],
    "all-cells": [0, 1, 2, 3, 4, 5],
}
NAMED = {
    "identity": [[i] for i in range(6)],
    "patches": [[0, 1, 2], [3, 4, 5]],
    "one-block": [[0, 1, 2, 3, 4, 5]],
    "cross-pairs": [[0, 3], [1, 4], [2, 5]],
}
PARTS = list(coarse.set_partitions(range(6)))


def key(p):
    return frozenset(frozenset(b) for b in p)


def label(p):
    return "|".join("".join(str(i) for i in sorted(b))
                    for b in sorted(p, key=lambda b: min(b)))


def ahat_block(P, pi):
    out = {}
    for name, S in CANDIDATES.items():
        obs = M.observational(P, pi, model.N_VARS, S)
        au, aun = M.ahat(P, pi, model.N_VARS, S, "uniform")
        ap, apn = M.ahat(P, pi, model.N_VARS, S, "population")
        c2 = M.c2_profile(P, model.N_VARS, S)
        out[name] = dict(
            **obs, Ahat_uniform=au, Ahat_uniform_norm=aun,
            Ahat_pop=ap, Ahat_pop_norm=apn,
            C2_mean=c2["mean"], C2_var=c2["var"], C2_sd=c2["sd"],
            C2_min=c2["min"], C2_max=c2["max"],
            I_Eprime_Shat=M.effect_on_environment(P, pi, model.N_VARS, S))
    return out


def dc_block(P, pi):
    out = {}
    for h in HORIZONS:
        Ph = np.linalg.matrix_power(P, h)
        for dist in (False, True):
            rows = []
            for p in PARTS:
                r = coarse.delta_c(Ph, pi, p, model.N_VARS, model.N_CELLS,
                                   model.R_VAR, dist=dist)
                rows.append((p, r))
            tag = f"h{h}_{'dist' if dist else 'mean'}"
            res = {}
            for field in ("dC", "dC_E"):
                vals = np.array([r[field] for _, r in rows])
                order = np.argsort(vals, kind="stable")
                rank = {key(rows[i][0]): k + 1 for k, i in enumerate(order)}
                vmin = vals.min()
                ties = [rows[i][0] for i in range(len(rows))
                        if vals[i] <= vmin + 1e-9]
                coarsest_tie = min(ties, key=len)
                res[field] = dict(
                    named={n: dict(value=float(vals[[key(r[0]) for r in rows]
                                                     .index(key(q))]),
                                   rank=rank[key(q)])
                           for n, q in NAMED.items()},
                    min=float(vmin), n_at_min=len(ties),
                    coarsest_at_min=label(coarsest_tie),
                    best5=[(label(rows[i][0]), float(vals[i]))
                           for i in order[:5]],
                    best_nontrivial=[(label(rows[i][0]), float(vals[i]))
                                     for i in order
                                     if 1 < len(rows[i][0]) < 6][:3])
                # an accuracy-plus-cost objective (not Bourrat's): dC + kappa*k
                ks = np.array([len(r[0]) for r in rows])
                win = []
                for kap in KAPPAS:
                    J = vals + kap * ks
                    j = J.min()
                    w = [label(rows[i][0]) for i in range(len(rows))
                         if J[i] <= j + 1e-12]
                    win.append((float(kap), " / ".join(w)))
                ranges = {}
                for kap, w in win:
                    ranges.setdefault(w, []).append(kap)
                res[field]["cost_winners"] = [
                    dict(winners=w, kappa_min=min(k), kappa_max=max(k))
                    for w, k in ranges.items()]
            out[tag] = res
    return out


def sensitivity():
    """Key Ahat quantities at the ends of the path, other parameters."""
    rows = []
    for a in (0.1, 0.3, 0.5):
        for d in (0.0, 0.05, 0.2):
            row = dict(a=a, d=d)
            for lam in (0.0, 1.0):
                P = model.scaffold_kernel(lam, a=a, d=d)
                pi = model.stationary(P)
                for name in ("cell", "patch", "cross-triple", "patch+scaffold"):
                    S = CANDIDATES[name]
                    row[f"{name}_norm_{lam}"] = M.ahat(P, pi, model.N_VARS,
                                                       S)[1]
                    row[f"{name}_C2var_{lam}"] = M.c2_profile(
                        P, model.N_VARS, S)["var"]
            P = model.common_input_kernel(a=a)
            pi = model.stationary(P)
            for name in ("cell", "pair-in-patch", "cross-pair"):
                row[f"control_{name}_norm"] = M.ahat(
                    P, pi, model.N_VARS, CANDIDATES[name])[1]
            rows.append(row)
    return rows


def main():
    results = {"params": dict(a=0.3, eps=0.05, d=0.05, q_on=0.2, q_off=0.2,
                              lams=LAMS, horizons=HORIZONS),
               "scaffold": {}, "control": {}}
    for lam in LAMS:
        P = model.scaffold_kernel(lam)
        pi = model.stationary(P)
        results["scaffold"][str(lam)] = dict(ahat=ahat_block(P, pi),
                                             dc=dc_block(P, pi))
        print("lam", lam, "done", flush=True)
    P = model.common_input_kernel()
    pi = model.stationary(P)
    results["control"] = dict(ahat=ahat_block(P, pi), dc=dc_block(P, pi))
    P = model.common_input_kernel(asymmetric=True)
    pi = model.stationary(P)
    results["control_asym"] = dict(ahat=ahat_block(P, pi), dc=dc_block(P, pi))
    results["sensitivity"] = sensitivity()
    # C1 against the cell at theta_0 (lam = 0)
    base = results["scaffold"]["0.0"]["ahat"]["cell"]["Ahat_uniform_norm"]
    results["C1_reference_cell_lam0"] = base
    (HERE / "results.json").write_text(json.dumps(results, indent=1,
                                                  default=str))
    write_summary(results)


def fmt(x):
    return f"{x:.4f}"


def write_summary(R):
    L = []
    base = R["C1_reference_cell_lam0"]
    L.append("Bourrat 2024 (LIT-005): Ahat, uniform input; C1 reference = "
             f"cell at lam=0, normalised Ahat {fmt(base)}")
    L.append("")
    for arm, rows in [("scaffold lam=" + k, v["ahat"])
                      for k, v in R["scaffold"].items()] + \
                     [("control (common input)", R["control"]["ahat"]),
                      ("control, asymmetric", R["control_asym"]["ahat"])]:
        L.append(f"== {arm}")
        L.append(f"{'candidate':16s} {'A*':>7s} {'A':>7s} {'nC':>7s} "
                 f"{'Ahat':>7s} {'Ah/H':>7s} {'AhPop':>7s} {'C1':>3s} "
                 f"{'C2mean':>7s} {'C2var':>8s} {'I(E;S^)':>8s}")
        for name, r in rows.items():
            c1 = "yes" if r["Ahat_uniform_norm"] >= base - 1e-12 else "no"
            L.append(f"{name:16s} {fmt(r['Astar']):>7s} {fmt(r['A']):>7s} "
                     f"{fmt(r['nC']):>7s} {fmt(r['Ahat_uniform']):>7s} "
                     f"{fmt(r['Ahat_uniform_norm']):>7s} "
                     f"{fmt(r['Ahat_pop']):>7s} {c1:>3s} "
                     f"{fmt(r['C2_mean']):>7s} {r['C2_var']:8.5f} "
                     f"{fmt(r['I_Eprime_Shat']):>8s}")
        L.append("")
    L.append("Bourrat 2023 (LIT-049): dC over all 203 partitions of the cells")
    L.append("")
    for arm, blk in [("scaffold lam=" + k, v["dc"])
                     for k, v in R["scaffold"].items()] + \
                    [("control (common input)", R["control"]["dc"]),
                     ("control, asymmetric", R["control_asym"]["dc"])]:
        L.append(f"== {arm}")
        for tag, res in blk.items():
            for field in ("dC", "dC_E"):
                r = res[field]
                named = ", ".join(f"{n} {r['named'][n]['value']:.4f}"
                                  f"(#{r['named'][n]['rank']})"
                                  for n in NAMED)
                L.append(f"  {tag:10s} {field:5s} min {r['min']:.4f} "
                         f"({r['n_at_min']} at min; coarsest "
                         f"{r['coarsest_at_min']}); {named}")
                L.append(f"  {'':10s} {'':5s} best non-trivial: "
                         + "; ".join(f"{a} {b:.4f}"
                                     for a, b in r["best_nontrivial"]))
                def short(w):
                    w = w.split(" / ")
                    return w[0] if len(w) == 1 else f"{len(w)}-way tie"
                L.append(f"  {'':10s} {'':5s} dC+kappa*k winners: "
                         + "; ".join(f"{short(c['winners'])} for kappa "
                                     f"{c['kappa_min']}-{c['kappa_max']}"
                                     for c in r["cost_winners"]))
        L.append("")
    L.append("Sensitivity (Ahat/H and C2 variance at lam 0 -> 1; control)")
    for r in R["sensitivity"]:
        L.append(f"  a={r['a']} d={r['d']}: "
                 + ", ".join(f"{n} {r[n + '_norm_0.0']:.3f}->"
                             f"{r[n + '_norm_1.0']:.3f} "
                             f"var {r[n + '_C2var_0.0']:.4f}->"
                             f"{r[n + '_C2var_1.0']:.4f}"
                             for n in ("cell", "patch", "cross-triple",
                                       "patch+scaffold"))
                 + "; control cell/pair-in/cross-pair "
                 + "/".join(f"{r['control_' + n + '_norm']:.3f}"
                            for n in ("cell", "pair-in-patch",
                                      "cross-pair")))
    (HERE / "summary.txt").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
