"""Apply the criterion stated in advance (TERM-tmpsu4df, TERM-tmpo4pxh,
README "Stated in advance") to results.jsonl and print the verdict table.

    python3 -I summarize.py [results.jsonl]
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EPS, MARGIN, F = 0.05, 0.3, 0.2
RHO_MAX = F / (1 - F) / 2
ARMS = ("independent", "learned-cut", "conform", "enforce", "evidential")


def ci(x):
    x = np.asarray(x, float)
    m, se = x.mean(), x.std(ddof=1) / np.sqrt(len(x))
    return m, m - 1.96 * se, m + 1.96 * se


def fmt(c):
    return f"{c[0]:+.3f} [{c[1]:+.3f}, {c[2]:+.3f}]"


def main(path):
    rows = [json.loads(l) for l in open(path) if l.strip()]
    by = {}
    for r in rows:
        by.setdefault(r["arm"], {})[r["seed"]] = r
    seeds = sorted(set.intersection(*(set(v) for v in by.values())))
    ind = by["independent"]
    out = {}
    print(f"seeds: {len(seeds)}; eps={EPS}, margin={MARGIN}, rho_max={RHO_MAX}")
    for arm in ARMS:
        A = [by[arm][s] for s in seeds]
        get = lambda k: [r[k] for r in A]  # noqa: E731
        conc = ci([r["concordance"] - r["concordance_diff"] for r in A])
        s_u, s_w = ci(get("s_u")), ci(get("s_w"))
        smax = s_u if s_u[0] >= s_w[0] else s_w
        recip = ci([by[arm][s]["g_u"] - ind[s]["g_u"] for s in seeds])
        sigma = ci([r["s_w"] - r["s_u"] for r in A])
        rho = ci([r["s_u"] / r["g_u"] if r["g_u"] > 0 else np.inf for r in A])
        av, an = ci(get("agency_vote")), ci(get("agency_none"))
        v = dict(
            C1=conc[1] > MARGIN,
            C2=smax[1] > EPS and recip[1] > EPS,
            C3_evidential=sigma[1] > EPS,
            C3_restorative=recip[1] > EPS and rho[2] < RHO_MAX,
            CA_vote=av[1] > 0.25,
            CA_none=an[1] > 0.25,
        )
        out[arm] = dict(verdict=v, concordance_margin=conc, s_u=s_u, s_w=s_w,
                        recovery_vs_indep=recip, sigma=sigma, rho=rho,
                        agency_vote=av, agency_none=an,
                        concordance=ci(get("concordance")),
                        agreement=ci(get("agreement")),
                        g_u=ci(get("g_u")), g_w=ci(get("g_w")))
        print(f"\n== {arm}")
        for k in ("concordance", "agreement", "concordance_margin", "s_u",
                  "s_w", "g_u", "g_w", "recovery_vs_indep", "sigma", "rho",
                  "agency_vote", "agency_none"):
            print(f"  {k:20s} {fmt(out[arm][k])}")
        print("  verdict", {k: ("pass" if b else "fail") for k, b in v.items()})
    return out


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "results.jsonl"))
