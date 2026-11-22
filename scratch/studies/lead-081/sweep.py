"""LEAD-081 sweep. Writes results/summary.json and results/summary.md.

Every configuration runs on the same N instances, the same initial states and
the same initial weights (paired by seed), so differences between allocation
rules are differences of allocation alone.
"""
import json
import sys
import time
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import numpy as np
import model as M

N = 200          # instances with jointly satisfiable demands
N_STRUCT = 100   # instances with no common region (structural control)
T = 200
BASE = dict(r=0.1, gamma=8.0, delta=0.9, noise=0.0, cond=1.0)
KEYS = ["violation", "realized_violation", "gov_frustration", "unreachable",
        "structural", "regret", "final_unmet", "final_wmax", "leader_is_initial",
        "leader_is_nearest"]


def setup(seed, overlap=True, cond=1.0):
    rng = np.random.default_rng(seed)
    while True:
        dem = M.random_instance(rng, overlap=overlap, cond=cond)
        if M.common_region_nonempty(dem) == overlap:
            break
    a = rng.uniform(0, 2 * np.pi)
    theta0 = 2.2 * np.array([np.cos(a), np.sin(a)])
    w0 = np.full(3, 1 / 3) + rng.normal(0, 0.02, 3)
    w0 = np.clip(w0, 0.01, None); w0 /= w0.sum()
    wfix = rng.dirichlet(np.ones(3))
    return dem, theta0, w0, wfix


def job(args):
    seed, rule, cfg, overlap = args
    cfg = {**BASE, **cfg}
    dem, theta0, w0, wfix = setup(seed, overlap, cfg["cond"])
    w_init = w0
    if rule == "fixed_uniform":
        rule_, w_init = "fixed", np.full(3, 1 / 3)
    elif rule == "fixed_random":
        rule_, w_init = "fixed", wfix
    else:
        rule_ = rule
    rec, s = M.run(dem, theta0, w_init, rule_, T=T, r=cfg["r"], gamma=cfg["gamma"],
                   delta=cfg["delta"], noise=cfg["noise"],
                   rng=np.random.default_rng(10_000 + seed))
    # hysteresis: is the component that ends on top the initial leader, or the
    # one whose demand region the start is nearest?
    s["leader_is_initial"] = float(s["final_leader"] == int(np.argmax(w_init)))
    s["leader_is_nearest"] = float(s["final_leader"] == int(np.argmin(
        np.linalg.norm(dem.c - theta0, axis=1))))
    return seed, rule, json.dumps(cfg, sort_keys=True), overlap, s


def agg(rows):
    out = {}
    for k in KEYS:
        v = np.array([r[k] for r in rows], float)
        out[k] = (float(v.mean()), float(1.96 * v.std(ddof=1) / np.sqrt(len(v))))
    out["all_met_final"] = float(np.mean([r["final_unmet"] == 0 for r in rows]))
    out["captured"] = float(np.mean([r["final_wmax"] > 0.9 for r in rows]))
    out["n"] = len(rows)
    return out


def main():
    jobs = []
    rules = ["fixed_uniform", "fixed_random", "A", "B", "oracle"]
    # 1. allocation intervention, everything else at BASE
    for seed in range(N):
        for rule in rules:
            jobs.append((seed, rule, {}, True))
    # 2. optimizer and information controls, under A and B (and fixed_uniform)
    controls = [{"r": 0.05}, {"r": 0.2}, {"r": 0.4}, {"noise": 0.1}, {"noise": 0.3},
                {"cond": 5.0}]
    for c in controls:
        for seed in range(N):
            for rule in ["fixed_uniform", "A", "B", "oracle"]:
                jobs.append((seed, rule, c, True))
    # 3. conferral parameters under A
    for g in [0.0, 1.0, 2.0, 4.0, 8.0, 16.0]:
        for dl in [0.5, 0.8, 0.9, 0.95]:
            if (g, dl) == (BASE["gamma"], BASE["delta"]):
                continue
            for seed in range(N):
                jobs.append((seed, "A", {"gamma": g, "delta": dl}, True))
    # 4. structural control
    for seed in range(N_STRUCT):
        for rule in rules:
            jobs.append((100_000 + seed, rule, {}, False))

    t0 = time.time()
    with Pool(4) as pool:
        res = pool.map(job, jobs, chunksize=20)
    elapsed = time.time() - t0

    groups = {}
    for seed, rule, cfg, overlap, s in res:
        groups.setdefault((rule, cfg, overlap), []).append((seed, s))
    summary = []
    for (rule, cfg, overlap), rows in sorted(groups.items()):
        a = agg([s for _, s in rows])
        summary.append({"rule": rule, "cfg": json.loads(cfg), "overlap": overlap, **a})

    # paired comparisons at BASE: gov_frustration of A minus that of each other rule
    base_cfg = json.dumps({**BASE}, sort_keys=True)
    by = {rule: dict(groups[(rule, base_cfg, True)]) for rule in rules}
    paired = {}
    for other in rules:
        if other == "A":
            continue
        diff = np.array([by["A"][s]["gov_frustration"] - by[other][s]["gov_frustration"]
                         for s in range(N)])
        paired[f"A_minus_{other}"] = {
            "mean": float(diff.mean()), "ci95": float(1.96 * diff.std(ddof=1) / np.sqrt(N)),
            "A_worse": int((diff > 0).sum()), "A_better": int((diff < 0).sum()),
            "tied": int((diff == 0).sum())}
    out = {"N": N, "N_struct": N_STRUCT, "T": T, "base": BASE,
           "elapsed_s": elapsed, "cpu_s_approx": elapsed * 4,
           "summary": summary, "paired_base": paired}
    (HERE / "results").mkdir(exist_ok=True)
    (HERE / "results" / "summary.json").write_text(json.dumps(out, indent=1))
    write_md(out)
    print(f"done in {elapsed:.0f}s")


def fmt(x):
    return f"{x[0]:.3f} ± {x[1]:.3f}"


def write_md(out):
    L = [f"# LEAD-081 sweep results\n",
         f"N = {out['N']} satisfiable instances, {out['N_struct']} structural; T = {out['T']} "
         f"steps, measures over the last half. Base: {out['base']}. Wall {out['elapsed_s']:.0f}s on 4 cores.\n",
         "gov_frustration: share of steps on which the actual update violates a declared "
         "requirement while some allocation, with the same gradients and update map, meets "
         "them all. realized_violation: violated while some admissible update meets all "
         "(Phi <= 0). structural: Phi > 0. ± is 1.96 standard errors over instances.\n",
         "| rule | cfg | overlap | violation | realized_viol | gov_frustration | unreachable | structural | regret | all met at end | captured |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in out["summary"]:
        cfg = {k: v for k, v in s["cfg"].items() if out["base"].get(k) != v}
        L.append(f"| {s['rule']} | {cfg or 'base'} | {s['overlap']} | {fmt(s['violation'])} | "
                 f"{fmt(s['realized_violation'])} | {fmt(s['gov_frustration'])} | "
                 f"{fmt(s['unreachable'])} | {fmt(s['structural'])} | {fmt(s['regret'])} | "
                 f"{s['all_met_final']:.3f} | {s['captured']:.3f} |")
    L.append("\n## Paired at base (A minus other, gov_frustration)\n")
    for k, v in out["paired_base"].items():
        L.append(f"- {k}: {v['mean']:.3f} ± {v['ci95']:.3f}; A worse on {v['A_worse']}, "
                 f"better on {v['A_better']}, tied on {v['tied']}")
    (HERE / "results" / "summary.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
