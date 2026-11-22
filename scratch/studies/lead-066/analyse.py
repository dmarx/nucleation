"""Summaries of results/E1.jsonl, E2.jsonl, E4.jsonl -> results/summary.json and stdout.

    python3 -I analyse.py
"""
import json
import os
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")


def load(name):
    p = os.path.join(RES, name)
    if not os.path.exists(p):
        return []
    with open(p) as f:
        return [json.loads(x) for x in f if x.strip()]


def num(x):
    return np.inf if x == "inf" else (np.nan if x is None else float(x))


def interval(delta, eps, lam, Lam):
    """Corollary 2, as bound.time_interval."""
    sd = np.sqrt(delta)
    lower = 0.0 if sd + eps >= 1 else np.log(1 / (sd + eps)) / Lam
    upper = np.inf if eps >= sd else np.log(1 / (sd - eps)) / lam
    return lower, upper


def pairs_of(r):
    """Recompute the pair records (as run.py wrote them before compact.py) from
    the stored rates, bounds and times."""
    if "pairs" in r:
        return r["pairs"]
    lv = r["levels"]
    mu = [num(x) for x in r["mu"]]
    out = []
    for dl_s, ts in r["times"].items():
        dl = float(dl_s)
        T = dict(zip(lv, [num(t) for t in ts]))
        iv = {l: interval(dl, num(r["eps"][l]), num(r["lam"][l]), num(r["Lam"][l])) for l in lv}
        for i, l in enumerate(lv):
            for m in lv[i + 1:]:
                if abs(mu[l] - mu[m]) <= 1e-9 * max(mu[l], mu[m]):
                    base = 0
                else:
                    base = 1 if mu[l] > mu[m] else -1
                actual = 0 if np.isclose(T[l], T[m], rtol=1e-9) else (1 if T[l] < T[m] else -1)
                first, second = (l, m) if base >= 0 else (m, l)
                cert = base != 0 and iv[first][1] < iv[second][0]
                out.append(dict(delta=dl, l=l, m=m, base=base, actual=actual, certified=bool(cert)))
    return out


def e1(rows):
    out = {}
    out["items"] = len(rows)
    # sigma = 0: the commutators are rounding (exact symmetry); the ratio checks
    # below are taken off it, where a ratio of two rounding errors means nothing
    sym = [r for r in rows if r["sigma"] == 0]
    out["sigma0_max_commutator"] = max(max(num(x) for x in r["eta"]) for r in sym) if sym else None
    rows_all, rows = rows, [r for r in rows if r["sigma"] > 0]
    out["thm1_max_ratio"] = max(num(r["thm1_max_ratio"]) for r in rows)
    out["dk_max_ratio"] = max(num(r["dk_max_ratio"]) for r in rows)
    out["contained"] = [sum(r["contained"] for r in rows), sum(r["checked"] for r in rows)]
    out["certified_but_violated"] = sum(1 for r in rows for p in pairs_of(r)
                                        if p["certified"] and p["actual"] != p["base"])
    lin = [r for r in rows if r["kernel"] == "linear" and r["sigma"] > 0]
    out["linear_data_bound_holds"] = all(num(r["data_bound"]) >= num(r["Eop"]) * (1 - 1e-9) for r in lin)
    out["eta_le_Eop"] = all(max(num(x) for x in r["eta"]) <= num(r["Eop"]) * (1 + 1e-9) + 1e-15 for r in rows)

    by = defaultdict(list)
    for r in rows_all:
        by[(r["kernel"], r["sigma"])].append(r)
    table = []
    for (k, s), rs in sorted(by.items()):
        row = dict(kernel=k, sigma=s)
        row["Eop_over_mu_gap"] = float(np.median([num(r["Eop"]) / np.min(np.abs(np.diff(sorted([num(m) for m in np.array(r["mu"])[r["levels"]]]))) + 1e-300) for r in rs]))
        row["eps_median"] = float(np.median([num(e) for r in rs for l, e in enumerate(r["eps"]) if l in r["levels"]]))
        if s > 0:
            row["sup_over_uniform_median"] = float(np.median([num(r["thm1_sup_over_uniform"]) for r in rs]))
            row["sup_over_uniform_max"] = float(np.max([num(r["thm1_sup_over_uniform"]) for r in rs]))
        for dl in (0.1, 0.01, 1e-12):
            ps = [p for r in rs for p in pairs_of(r) if p["delta"] == dl and p["base"] != 0]
            row[f"preserved@{dl}"] = float(np.mean([p["actual"] == p["base"] for p in ps]))
            row[f"certified@{dl}"] = float(np.mean([p["certified"] for p in ps]))
        # resolution limit: spread of acquisition times across levels
        for dl in ("0.1", "1e-12"):
            row[f"Tspread@{dl}"] = float(np.median([max(num(t) for t in r["times"][dl]) / min(num(t) for t in r["times"][dl]) for r in rs]))
        table.append(row)
    out["by_kernel_sigma"] = table

    # target share: which pairs flip, by the weaker level's target share
    flips = defaultdict(lambda: [0, 0])
    for r in rows:
        if r["sigma"] < 0.1:
            continue
        for p in pairs_of(r):
            if p["delta"] != 0.1 or p["base"] == 0:
                continue
            key = r["g"]
            pair = (p["l"], p["m"])
            if 4 in pair:
                flips[(key, "with level 4")][0] += int(p["actual"] != p["base"])
                flips[(key, "with level 4")][1] += 1
            else:
                flips[(key, "without level 4")][0] += int(p["actual"] != p["base"])
                flips[(key, "without level 4")][1] += 1
    out["flip_rate_sigma_ge_0.1_delta_0.1"] = {f"{k[0]} {k[1]}": [v[0], v[1], v[0] / v[1]] for k, v in sorted(flips.items())}
    return out


def e2(rows):
    return [dict(eta_over_mu1=r["eta_over_mu1"], mu2_over_mu1=r["mu2_over_mu1"], ratio=r["ratio"]) for r in rows]


def e4(rows):
    out = {"items": len(rows)}
    if not rows:
        return out
    out["damped_bound_max_ratio"] = max(num(r["damped_bound_max_ratio"]) for r in rows)
    out["integral_bound_max_ratio"] = max(num(r["integral_bound_max_ratio"]) for r in rows)
    by = defaultdict(list)
    for r in rows:
        by[(r["width"], r["sigma"], r["scale"])].append(r)
    table = []
    for (m, s, sc), rs in sorted(by.items()):
        lv = [str(l) for l in rs[0]["levels"]]
        def med(field):
            return float(np.median([num(r[field][l]) for r in rs for l in lv]))
        order_same = []
        order_coarse = []
        for r in rs:
            for dl in ("0.1", "0.01"):
                T = [num(r["T"][f"{l}|{dl}"]) for l in lv]
                TD = [num(r["TD"][f"{l}|{dl}"]) for l in lv]
                order_same.append(list(np.argsort(T, kind="stable")) == list(np.argsort(TD, kind="stable")))
                order_coarse.append(all(T[i] <= T[i + 1] for i in range(len(T) - 1)))
        table.append(dict(width=m, sigma=s, scale=sc,
                          eta_init_median=float(np.median([num(x) for r in rs for x in r["eta_init"][1:]])),
                          int_commutator_median=med("int_commutator"),
                          max_rel_dev_median=med("max_rel_dev"),
                          max_rel_dev_max=float(np.max([num(r["max_rel_dev"][l]) for r in rs for l in lv])),
                          damped_bound_final_median=med("damped_bound_rel_final"),
                          integral_bound_final_median=med("integral_bound_rel_final"),
                          order_matches_decoupled=float(np.mean(order_same)),
                          coarse_first=float(np.mean(order_coarse))))
    out["by_width_sigma_scale"] = table
    return out


if __name__ == "__main__":
    summary = {"E1": e1(load("E1.jsonl")), "E2": e2(load("E2.jsonl")), "E4": e4(load("E4.jsonl"))}
    with open(os.path.join(RES, "summary.json"), "w") as f:
        json.dump(summary, f, indent=1)
    print(json.dumps(summary, indent=1))
