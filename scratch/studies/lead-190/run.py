"""LEAD-190 experiments. Each writes results/<name>.json when it finishes.

python3 -I run.py [name ...]   (OMP_NUM_THREADS=1); about ten minutes in all.
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(OUT, exist_ok=True)
SEEDS = range(30)


def save(name, obj):
    with open(os.path.join(OUT, name + ".json"), "w") as f:
        json.dump(obj, f, indent=1, default=float)
    print(name, json.dumps(obj, default=float)[:800], flush=True)


def summarize(rows):
    keys = rows[0].keys()
    out = {}
    for k in keys:
        v = np.array([r[k] for r in rows], float)
        v = v[~np.isnan(v)]
        out[k] = dict(mean=float(v.mean()), sd=float(v.std()), min=float(v.min()),
                      max=float(v.max())) if len(v) else None
    return out


def start(pop, kind, seed):
    if kind == "polar":
        return 0.2 * pop["s"]
    return 0.01 * np.random.default_rng(1000 + seed).normal(size=pop["N"])


def e1_schemes():
    """CLAIM-281: the five grant schemes on 30 populations, mean field."""
    res = {}
    for phs in (0.0, 0.2):
        for b in (0.0, 0.05):
            P = M.params(b=b, phi_s=phs, phi=0.3 - phs / 2)
            for st in ("polar", "noisy"):
                for sch in M.SCHEMES:
                    rows = []
                    for sd in SEEDS:
                        pop = M.population(N=20, seed=sd)
                        m, W, E = M.run_scheme(sch, pop, P, T=1000, m0=start(pop, st, sd), seed=sd)
                        rows.append(M.meaning_measures(m, W, E, pop, P))
                    res[f"phi_s={phs} b={b} {st} {sch}"] = summarize(rows)
    save("e1_schemes", dict(params=M.params(), N=20, seeds=len(SEEDS), T=1000, results=res))


def e2_agent_level():
    """The same comparison with the agent-level step (k = 50 items), 20 seeds."""
    res = {}
    for b in (0.0, 0.05):
        P = M.params(b=b)
        for sch in M.SCHEMES:
            rows = []
            for sd in range(20):
                pop = M.population(N=20, seed=sd)
                m, W, E = M.run_scheme(sch, pop, P, T=1500, m0=start(pop, "polar", sd),
                                       stochastic=True, seed=sd)
                rows.append(M.meaning_measures(m, W, E, pop, P))
            res[f"b={b} polar {sch}"] = summarize(rows)
    save("e2_agent_level", dict(params=M.params(), N=20, seeds=20, T=1500, results=res))


def e3_independence():
    """How independent must the critic score be? Sweep zeta in the role scheme
    against the closed-form thresholds of population_jacobian."""
    out = []
    for phs in (0.0, 0.2):
        P0 = M.params(phi_s=phs, phi=0.3 - phs / 2)
        lhs1, uni, diff = M.meaning_threshold(dict(P0, zeta=1.0))
        for z in np.round(np.arange(0, 1.0001, 0.05), 3):
            P = dict(P0, zeta=float(z))
            rows = []
            for sd in range(10):
                pop = M.population(N=20, seed=sd)
                m, W, E = M.run_scheme("role", pop, P, T=3000, m0=start(pop, "polar", sd), seed=sd)
                rows.append(M.meaning_measures(m, W, E, pop, P))
            s = summarize(rows)
            out.append(dict(phi_s=phs, zeta=float(z), lhs=float(lhs1 * z),
                            gap=s["gap"]["mean"], onesided=s["onesided"]["mean"],
                            own_side_reading=s["own_side_reading"]["mean"],
                            spread=s["spread"]["mean"], m_mean=s["m_mean"]["mean"],
                            factions_in=int(sum(r["gap"] > 0.2 for r in rows))))
        out.append(dict(phi_s=phs, zeta_star_uniform=float(uni / lhs1),
                        zeta_star_differentiating=float(diff / lhs1)))
    save("e3_independence", dict(params=M.params(), rows=out))


def e4_grant_game():
    """CLAIM-285: aggregation rule x objective, 30 populations, two costs."""
    res = {}
    for cost, lam, lr, T in (("quadratic", 0.02, 0.5, 2000), ("linear", 0.005, 0.5, 2000)):
        for agg in ("one-hop", "loo", "recursive"):
            for obj in ("policy", "authority"):
                P = M.params(agg=agg, objective=obj, cost=cost, lam=lam, lr=lr)
                rows = []
                t = time.time()
                for sd in SEEDS:
                    pop = M.population(N=20, seed=sd)
                    _, Ea, conv = M.run_game(pop, P, T=T, seed=sd)
                    r = M.grant_measures(Ea, pop)
                    r.update(M.reach_measures(Ea, pop, P))
                    r["convergence"] = conv
                    rows.append(r)
                res[f"{cost} {agg} {obj}"] = summarize(rows)
                print(cost, agg, obj, round(time.time() - t, 1), flush=True)
    save("e4_grant_game", dict(N=20, seeds=len(SEEDS), eta=M.params()["eta"], results=res))


def e5_size():
    """The bound and unbound cells at N = 40, 10 populations (quadratic cost)."""
    res = {}
    for agg, obj in (("one-hop", "policy"), ("loo", "policy"), ("recursive", "authority")):
        P = M.params(agg=agg, objective=obj)
        rows = []
        for sd in range(10):
            pop = M.population(N=40, seed=sd)
            _, Ea, conv = M.run_game(pop, P, T=2000, seed=sd)
            r = M.grant_measures(Ea, pop)
            r.update(M.reach_measures(Ea, pop, P))
            r["convergence"] = conv
            rows.append(r)
        res[f"{agg} {obj}"] = summarize(rows)
    # and the meaning-layer schemes at N = 40
    P = M.params(b=0.0)
    for sch in ("scalar-agree", "scalar-policy", "role"):
        rows = []
        for sd in range(10):
            pop = M.population(N=40, seed=sd)
            m, W, E = M.run_scheme(sch, pop, P, T=1000, m0=start(pop, "polar", sd), seed=sd)
            rows.append(M.meaning_measures(m, W, E, pop, P))
        res[f"scheme {sch} b=0 polar"] = summarize(rows)
    save("e5_size", dict(N=40, results=res))


EXPS = dict(e1=e1_schemes, e2=e2_agent_level, e3=e3_independence, e4=e4_grant_game,
            e5=e5_size)

if __name__ == "__main__":
    names = sys.argv[1:] or list(EXPS)
    for n in names:
        t = time.time()
        EXPS[n]()
        print(n, "done in", round(time.time() - t, 1), "s", flush=True)
