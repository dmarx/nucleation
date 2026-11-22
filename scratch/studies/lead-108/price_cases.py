"""Price the cockpit's speed bugs, a filed argument and a LEGO bin with the
one cost model in costmodel.py (LEAD-108).

Run:  python3 -I price_cases.py      (writes results.json and results.md)

Every parameter is tagged with where it comes from: a number from a source
the record holds, or "illustrative" (a value chosen to exercise the term,
whose verdict the sweeps below test). Hutchins measured nothing, so every
cockpit number is illustrative; the verdict that matters there is which
terms decide, and the sweep shows it holds over a range.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from costmodel import (INF, Demands, OnDemand, Store, availability_on_demand,
                       availability_store, break_even_n, lifetime)


def run(name, s, a, ds, notes, bound=None):
    r = lifetime(s, a, ds)
    out = {
        "scenario": name,
        "store": round(r["store"], 3),
        "on_demand": round(r["on_demand"], 3),
        "saving": round(r["saving"], 3),
        "store_by_party": {k: round(v, 3) for k, v in r["store_by_party"].items()},
        "on_demand_by_party": {k: round(v, 3) for k, v in r["on_demand_by_party"].items()},
        "availability_store": [round(availability_store(s, a, d), 4) for d in ds],
        "availability_on_demand": [round(availability_on_demand(a, d), 4) for d in ds],
        "break_even_n": [None if break_even_n(s, a, d) == INF
                         else round(break_even_n(s, a, d), 3) for d in ds],
        "undetected_wrong_store": round(s.sigma * (1 - s.delta), 5),
        "undetected_wrong_on_demand": a.sigma_A,
        "notes": notes,
    }
    if bound is not None:
        out["error_bound"] = bound
        out["store_meets_bound"] = out["undetected_wrong_store"] <= bound
        out["on_demand_meets_bound"] = a.sigma_A <= bound
    return out


# ---------------------------------------------------------------- cockpit
# Hutchins (NOTE-867): speeds computed 25-30 min before landing at light
# workload, read 10-15 min later by judgement of spatial proximity; the
# task is fixed, mandated and known (pi = 1); bugs are reset every approach
# (store life = one approach, so U = 0 and F recurs per approach); the card
# booklet is computed once by another party for the life of the airplane.
# Staleness is held as a bound, not priced: a wrong speed is a "killer"
# item and cross-checks are mandated, so L = 0 and the check is reported.
def cockpit():
    res = []
    lam_low, lam_high = 1.0, 3.0           # illustrative load ratio
    a = OnDemand(c=1.5, sigma_A=0.02)       # recall, read scale, compare
    bugs = Store(F=8, lam_F=lam_low, rho=0.2, v=0.1, sigma=0.01, delta=0.9,
                 eps=0.0)
    bound = 0.005                           # illustrative tolerated undetected-wrong chance
    calls = Demands(n=4, lam=lam_high, B=1.0)        # four flap/slat calls
    reads = Demands(n=24, lam=lam_high, B=1.0)       # calls plus salmon-bug checks
    res.append(run("cockpit: calls only, phase-priced", bugs, a, [calls],
                   "4 reads at high load; construction at low load", bound))
    res.append(run("cockpit: calls only, flat price", bugs, a,
                   [Demands(n=4, lam=lam_low, B=INF)],
                   "same work, no load difference and no budget: reuse alone", bound))
    res.append(run("cockpit: calls and monitoring, phase-priced", bugs, a, [reads],
                   "24 reads in the approach", bound))
    booklet = Store(F=8 + 2000 / 10_000, lam_F=lam_low, rho=0.2, v=0.1,
                    sigma=0.01, delta=0.9)
    booklet.party_F = "crew"
    res.append(run("cockpit: booklet's share counted (boundary widened)",
                   booklet, a, [calls],
                   "card booklet: 2000 units spread over 10,000 approaches "
                   "(illustrative), paid by the maker, folded into F", bound))
    # sweep: where do the bugs pay on lifetime, calls only?
    sweep = []
    for ratio in (1.0, 1.5, 2.0, 3.0, 5.0):
        for n in (4, 24):
            s = Store(F=8, lam_F=1.0, rho=0.2, v=0.1, sigma=0.01, delta=0.9)
            r = lifetime(s, a, [Demands(n=n, lam=ratio, B=1.0)])
            sweep.append({"lam_high/lam_low": ratio, "n": n,
                          "saving": round(r["saving"], 3)})
    # erosion: weighted by the chance of falling back, so it barely enters
    eros = []
    for eps in (0.0, 0.5, 1.0, 3.0):
        s = Store(F=8, lam_F=1.0, rho=0.2, v=0.1, sigma=0.01, delta=0.9, eps=eps)
        eros.append({"eps": eps,
                     "saving": round(lifetime(s, a, [calls])["saving"], 3)})
    return {"scenarios": res, "sweep_load_ratio": sweep, "sweep_erosion": eros}


# ---------------------------------------------------------- filed argument
# CASE-088 (A11's CASE B): reconstruct and answer 15, file 25, retrieve and
# check 3, three further uses. Split of the 3 into retrieval 1 and
# verification 2 is illustrative.
def filing():
    res = []
    a = OnDemand(c=15)
    base = Store(F=25, rho=1, v=2)
    three = Demands(n=3)
    res.append(run("filing: CASE-088 as filed", base, a, [three],
                   "reduces to CLAIM-303: F + n(c_a + u) < n c_r"))
    stale = Store(F=25, rho=1, v=2, sigma=0.1, delta=0.5, L=60, R=5)
    res.append(run("filing: staleness priced", stale, a, [three],
                   "illustrative: 1 use in 10 finds it out of date; checking "
                   "catches half; an undetected stale answer costs 4 "
                   "reconstructions; revision 5"))
    res.append(run("filing: staleness bound instead of priced", Store(
        F=25, rho=1, v=5, sigma=0.1, delta=0.95, L=0, R=5), a, [three],
        "the bound regime: checking raised from 2 to 5 to catch 95%", 0.01))
    grown = Store(F=25, rho=1 + 2, v=2, U=2, spill=0.01, n_other=300)
    res.append(run("filing: in a large store", grown, a, [three],
                   "illustrative: recognition by search adds 2 per use "
                   "(CLAIM-314); upkeep 2 (lint, link repair, CI); each "
                   "filing adds 0.01 to each of 300 other reuses"))
    owner = Store(F=20, U=0, rho=1, v=2)
    owner_share = Store(F=20 + 5 * 4, rho=1, v=2)
    res.append(run("filing: owner's review counted at its price (alt A2)",
                   owner_share, a, [three],
                   "illustrative: 5 of the 25 units are the owner's review, "
                   "priced at 4x the session's work"))
    res.append(run("filing: session's work only (alt A1)", owner, a, [three],
                   "the owner's review left outside the boundary"))
    res.append(run("filing: owner reconstructs, erosion counted (alt B2)",
                   Store(F=25, rho=1, v=2, eps=0.5), a,
                   [Demands(n=3, pi=0.7)],
                   "illustrative: 3 in 10 uses are not served by the filing; "
                   "the owner's own reconstruction has become 50% dearer"))
    res.append(run("filing: fresh session reconstructs (alt B1)",
                   Store(F=25, rho=1, v=2, eps=0.0), a,
                   [Demands(n=3, pi=0.7)],
                   "a session has no internal route to erode"))
    return {"scenarios": res,
            "claim_308_ratio_without_forecast": round(2 - 3 / 15, 3)}


# ---------------------------------------------------------------- LEGO bin
# CLAIM-307: c copies among m = 200 similar items, expected search m/(c+1)
# items examined; deadline D = 12 items. CASE-094: the bin is made when the
# brick is found, so construction is little more than the bin (5 here,
# illustrative). A tiny bin's content is seen at a glance (v = 0); a moved
# brick is noticed at once (delta = 1) and costs a full search.
def lego():
    res = []
    m, D = 200, 12
    for c, label in ((1, "one copy, similar to binmates"),
                     (20, "twenty copies")):
        a = OnDemand(c=m / (c + 1))
        s = Store(F=5, rho=2, v=0, sigma=0.05, delta=1.0, R=1, U=1)
        res.append(run(f"lego: {label}, labelled bins", s, a,
                       [Demands(n=10, B=D)],
                       "10 uses over the horizon (illustrative)"))
    a = OnDemand(c=1.0)       # pop-out: a black brick among white ones
    s = Store(F=5, rho=2, v=0, sigma=0.05, delta=1.0, R=1, U=1)
    res.append(run("lego: black brick among white (pop-out)", s, a,
                   [Demands(n=10, B=D)],
                   "feature search, about one look (CLAIM-310 part 3)"))
    a = OnDemand(c=m / 2)
    s = Store(F=5, rho=2, v=0, sigma=0.05, delta=1.0, R=1, U=1,
              spill=0.5, n_other=200)
    res.append(run("lego: one copy, bins found by scanning", s, a,
                   [Demands(n=10, B=D)],
                   "one more bin adds half a bin-look to each of 200 other "
                   "searches (CLAIM-310's k/2)"))
    return {"scenarios": res,
            "file_at_once": "F = 5 is less than one search's overpayment "
                            "(100 - 2), so CLAIM-308's rule makes the bin at "
                            "the first find, as CASE-094 does"}


def to_md(results):
    lines = ["| scenario | store | on demand | saving | break-even n | "
             "avail. store | avail. on demand | undetected wrong (store / on demand) |",
             "|---|---:|---:|---:|---:|---:|---:|---|"]
    for case in ("cockpit", "filing", "lego"):
        for r in results[case]["scenarios"]:
            be = r["break_even_n"][0]
            lines.append(
                f"| {r['scenario']} | {r['store']} | {r['on_demand']} | "
                f"{r['saving']} | {'never' if be is None else be} | "
                f"{r['availability_store'][0]} | {r['availability_on_demand'][0]} | "
                f"{r['undetected_wrong_store']} / {r['undetected_wrong_on_demand']} |")
    lines += ["", "Cockpit, saving by load ratio (calls only n = 4; with monitoring n = 24):", "",
              "| lam_high/lam_low | n | saving |", "|---:|---:|---:|"]
    for row in results["cockpit"]["sweep_load_ratio"]:
        lines.append(f"| {row['lam_high/lam_low']} | {row['n']} | {row['saving']} |")
    lines += ["", "Cockpit, saving by erosion (calls only):", "",
              "| eps | saving |", "|---:|---:|"]
    for row in results["cockpit"]["sweep_erosion"]:
        lines.append(f"| {row['eps']} | {row['saving']} |")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    results = {"cockpit": cockpit(), "filing": filing(), "lego": lego()}
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=1)
    with open(os.path.join(HERE, "results.md"), "w") as f:
        f.write(to_md(results))
    print(to_md(results))
