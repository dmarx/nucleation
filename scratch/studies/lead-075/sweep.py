"""LEAD-075 sweep: bottleneck budget, least time and readiness over parameters.

Writes results.jsonl (one line per experiment item, appended as produced;
items already present are skipped on rerun) and prints a summary.
Run: OPENBLAS_NUM_THREADS=1 python3 sweep.py   (from this directory)
"""
import json
import math
import os
import sys
from collections import Counter
from dataclasses import asdict, replace

import numpy as np

from staging_model import (Params, bottleneck, time_profile,
                           capacity_for_deadline, readiness, classify, KINDS)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results.jsonl")


def done_keys():
    if not os.path.exists(OUT):
        return set()
    with open(OUT) as f:
        return {json.loads(line)["key"] for line in f if line.strip()}


def emit(rec):
    rec = {k: (None if isinstance(v, float) and math.isinf(v) else v)
           for k, v in rec.items()}
    with open(OUT, "a") as f:
        f.write(json.dumps(rec) + "\n")


def fin(x):
    return None if not np.isfinite(x) else round(float(x), 6)


VARIANTS = {
    "base (CASE-198)": Params(),
    "home gap": Params(gap=True),
    "home gap, switch only left of it": Params(gap=True, switch_ok=(0.0, 0.4)),
    "dear staging (h1=1.0)": Params(h1=1.0),
}


def phase(name, p, bs, rhos):
    rA, rB = float(p.r()[0][0]), float(p.r()[0][-1])
    Bh, Ba = bottleneck(p, (0,)), bottleneck(p, (0, 1))
    grid = {}
    for b in bs:
        for rho in rhos:
            grid[f"{b:.3f},{rho:.3f}"] = classify(Bh, Ba, b, rho, rA, rB)
    return Bh, Ba, grid


def main():
    seen = done_keys()

    # 1. The four kinds: phase diagrams over budget b and reserve rho.
    bs = np.round(np.arange(0.60, 1.501, 0.025), 3)
    rhos = np.round(np.arange(0.0, 0.601, 0.025), 3)
    for name, p in VARIANTS.items():
        key = f"phase:{name}"
        if key in seen:
            continue
        Bh, Ba, grid = phase(name, p, bs, rhos)
        bsZ, tsZ = time_profile(p, (0, 1))
        bsH, tsH = time_profile(p, (0,))
        emit(dict(key=key, variant=name, params=asdict(p),
                  B_home=fin(Bh), B_staging_admitted=fin(Ba),
                  time_profile_staging=[[fin(b), fin(t)] for b, t in zip(bsZ, tsZ)],
                  time_profile_home=[[fin(b), fin(t)] for b, t in zip(bsH, tsH)],
                  counts=dict(Counter(grid.values())), grid=grid))

    # 1b. The same kinds under a deadline: c_tau replaces B* per repertoire.
    for name in ("base (CASE-198)", "home gap"):
        p = VARIANTS[name]
        rA, rB = float(p.r()[0][0]), float(p.r()[0][-1])
        for tau in (2.0, 2.8, 3.0):
            key = f"phase-deadline:{name}:tau={tau}"
            if key in seen:
                continue
            ch, ca = capacity_for_deadline(p, tau, (0,)), capacity_for_deadline(p, tau, (0, 1))
            Bu = bottleneck(p, (0, 1))
            grid = {f"{b:.3f},{rho:.3f}": classify(ch, ca, b, rho, rA, rB, B_untimed=Bu)
                    for b in bs for rho in rhos}
            emit(dict(key=key, variant=name, tau=tau, c_tau_home=fin(ch),
                      c_tau_staging_admitted=fin(ca),
                      counts=dict(Counter(grid.values())), grid=grid))

    # 2. Readiness against budget, per repertoire and deadline (base model).
    p = Params()
    for tau in (1.0, 2.0, 2.8, 3.0, 4.0):
        for Z in ((0,), (0, 1)):
            for rho, pr in ((0.0, 0.0), (0.2, 0.5)):
                key = f"readiness:tau={tau}:Z={Z}:rho={rho}:p={pr}"
                if key in seen:
                    continue
                c_tau = capacity_for_deadline(p, tau, Z)
                curve = [[float(b), round(readiness(p, b, tau, Z, rho=rho, p_res=pr,
                                                    u_max=0.3), 6)]
                         for b in np.round(np.arange(0.7, 1.801, 0.05), 3)]
                emit(dict(key=key, tau=tau, Z=list(Z), rho=rho, p_res=pr,
                          u_max=0.3, c_tau=fin(c_tau), curve=curve))

    # 3. Parameter sweep: what admitting the staging architecture does.
    key = "sweep:staging-effect"
    if key not in seen:
        rows = []
        for gap in (False, True):
            for beta0 in (0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.2):
                for h1 in (0.7, 0.8, 0.9, 1.0, 1.2):
                    for s in (0.0, 0.1, 0.2, 0.4):
                        for beta1 in (0.0, 0.4, 1.2):
                            p = Params(gap=gap, beta0=beta0, h1=h1, s=s, beta1=beta1, n=101)
                            Bh, Ba = bottleneck(p, (0,)), bottleneck(p, (0, 1))
                            if not np.isfinite(Bh) and np.isfinite(Ba):
                                eff = "creates reachability"
                            elif np.isfinite(Bh) and Ba < Bh - 1e-9:
                                eff = "lowers B*"
                            elif not np.isfinite(Ba):
                                eff = "unreachable either way"
                            else:
                                eff = "no change in B*"
                            # least time at the smaller of the two budgets that work
                            tZ = time_profile(p, (0, 1))[1]
                            tH = time_profile(p, (0,))[1]
                            rows.append(dict(gap=gap, beta0=beta0, h1=h1, s=s, beta1=beta1,
                                             B_home=fin(Bh), B_all=fin(Ba), effect=eff,
                                             T_at_Bstar_all=fin(tZ[0]) if len(tZ) else None,
                                             T_at_Bstar_home=fin(tH[0]) if len(tH) else None,
                                             T_min_all=fin(tZ[-1]) if len(tZ) else None))
        emit(dict(key=key, rows=rows,
                  counts={str(g): dict(Counter(r["effect"] for r in rows if r["gap"] == g))
                          for g in (False, True)}))

    summarize()


def summarize():
    with open(OUT) as f:
        recs = [json.loads(l) for l in f if l.strip()]
    for r in recs:
        if r["key"].startswith("phase:"):
            print(f"\n== {r['variant']}: B*_home={r['B_home']} B*_staging={r['B_staging_admitted']}")
            print("   T*(b) staging admitted:", r["time_profile_staging"])
            print("   T*(b) home only:      ", r["time_profile_home"])
            for k in KINDS:
                if k in r["counts"]:
                    print(f"   {k:38s} {r['counts'][k]}")
        elif r["key"].startswith("readiness:"):
            print(r["key"], "c_tau", r["c_tau"], [c[1] for c in r["curve"]][::2])
        elif r["key"].startswith("phase-deadline:"):
            print(f"\n== {r['variant']} tau={r['tau']}: c_tau home={r['c_tau_home']} "
                  f"staging={r['c_tau_staging_admitted']}  {r['counts']}")
        elif r["key"].startswith("sweep:"):
            print("\n== staging effect counts by gap:", r["counts"])
            # closed form: entering staging at q=0 and leaving at q=1 is best
            bad = 0
            for x in r["rows"]:
                S = max(max(0.7, x["h1"]) + x["s"], x["h1"] + x["beta1"] / 4)
                Bh = math.inf if x["B_home"] is None else x["B_home"]
                pred = min(Bh, S)
                if x["B_all"] is None or abs(pred - x["B_all"]) > 1e-6:
                    bad += 1
            print(f"   B*_all = min(B*_home, max(max(h0,h1)+s, h1+beta1/4)) fails in {bad} of {len(r['rows'])} rows")
            ts = [x["T_at_Bstar_all"] for x in r["rows"] if x["effect"] != "no change in B*"]
            print(f"   where staging matters, T* at B*_all ranges {min(ts)}..{max(ts)}; "
                  f"home crossing time is 1.0")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "summary":
        summarize()
    else:
        main()
