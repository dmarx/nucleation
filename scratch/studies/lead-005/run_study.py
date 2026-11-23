"""LEAD-005 study: reproduce Still et al. (2012) without feedback, then add
feedback.  Writes results/*.jsonl (one line per instance, append-only and
resumable) and results/summary.md.  Run:  python3 -I run_study.py
(about a minute on one CPU core)."""
from __future__ import annotations

import json
import os
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np  # noqa: E402

from feedback_toy import (MEMORIES, decode, describe, env_T, evaluate,  # noqa: E402
                          interventional_partition, predictive_partition)
from still2012 import random_model, run_exact, run_paths, sample  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
TAU = 6
N_NOFB = 300
N_FB = 500
N_MC = 20          # instances also checked by Monte Carlo
MC_SAMPLES = 200_000


def done_ids(path):
    if not os.path.exists(path):
        return set()
    with open(path) as f:
        return {json.loads(l)["id"] for l in f if l.strip()}


def record_instance(i, feedback, rng_seed):
    rng = np.random.default_rng(rng_seed)
    m = random_model(rng, feedback=feedback)
    r = run_exact(m, TAU)
    T = r.totals
    out = dict(
        id=i, seed=rng_seed, feedback=feedback,
        err_eq14=max(abs(s["Wdiss_switch"] - s["nostalgia"]) for s in r.steps),
        err_eq17=abs(T["Wdiss"] - (T["nostalgia"] - T["dF_relax"])),
        err_eq19=abs(-T["Q"] - (T["Ie"] + T["Wdiss"])),
        err_first_law=abs(T["dE"] - T["W"] - T["Q"]),
        min_step_nostalgia=min(s["nostalgia"] for s in r.steps),
        nostalgia=T["nostalgia"], dF_relax=T["dF_relax"], Wdiss=T["Wdiss"],
        Wex=T["Wex"], Ie=T["Ie"], heat_out=-T["Q"], W=T["W"], Q=T["Q"],
    )
    if not feedback:
        P = run_paths(m, TAU)
        out.update(Wdiss_path=P["Wdiss"], Wex_path=P["Wex"])
    if i < N_MC:
        mc = sample(m, TAU, MC_SAMPLES, np.random.default_rng(rng_seed + 10_000))
        out.update(mc_W=mc["W"], mc_W_se=mc["W_se"], mc_Q=mc["Q"], mc_Q_se=mc["Q_se"])
    return out


def sweep(name, n, feedback, base_seed):
    path = os.path.join(RES, f"{name}.jsonl")
    have = done_ids(path)
    with open(path, "a") as f:
        for i in range(n):
            if i in have:
                continue
            f.write(json.dumps(record_instance(i, feedback, base_seed + i)) + "\n")
            f.flush()
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def toy_rows():
    path = os.path.join(RES, "toy.jsonl")
    rows = []
    grid = [(0.1, 0.05, 6.0), (0.02, 0.0, 10.0), (0.3, 0.1, 4.0), (0.1, 0.05, 12.0)]
    policies = {"best": None, "a=0": (lambda s: 0)}
    for eps, delta, gap in grid:
        for name in MEMORIES:
            for pol_name, pol in policies.items():
                if pol_name != "best" and name != "interventional {u}":
                    continue
                r = evaluate(name, pol, eps, delta, gap)
                r.update(eps=eps, delta=delta, gap=gap, policy=pol_name)
                rows.append(r)
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    return rows


def main():
    os.makedirs(RES, exist_ok=True)
    nofb = sweep("nofeedback", N_NOFB, False, 1_000)
    fb = sweep("feedback", N_FB, True, 50_000)
    toy = toy_rows()

    def mc_ok(rows):
        ok = tot = 0
        for r in rows:
            if "mc_W" in r:
                tot += 1
                ok += (abs(r["mc_W"] - r["W"]) < 4 * r["mc_W_se"]
                       and abs(r["mc_Q"] - r["Q"]) < 4 * r["mc_Q_se"])
        return ok, tot

    L = ["# LEAD-005 results", "",
         f"Random systems: 4 states, 3-symbol Markov drive, Metropolis kernels (one sweep), "
         f"energies uniform in [0, 3] k_BT, tau = {TAU} steps, started in equilibrium.", ""]
    for label, rows in (("Without feedback (the paper's setting)", nofb),
                        ("With feedback (drive depends on the system's state)", fb)):
        n = len(rows)
        L += [f"## {label}: {n} instances", ""]
        L.append(f"- max |error| of Eq. 14 per step: {max(r['err_eq14'] for r in rows):.1e}; "
                 f"Eq. 17: {max(r['err_eq17'] for r in rows):.1e}; "
                 f"Eq. 19: {max(r['err_eq19'] for r in rows):.1e}; "
                 f"first law: {max(r['err_first_law'] for r in rows):.1e}")
        ok, tot = mc_ok(rows)
        L.append(f"- Monte Carlo ({MC_SAMPLES} trajectories) agrees with exact <W> and <Q> "
                 f"within 4 s.e. in {ok} of {tot} instances")
        L.append(f"- relaxation term sum dF_relax <= 0 in "
                 f"{sum(r['dF_relax'] <= 1e-12 for r in rows)} of {n}")
        L.append(f"- Eq. 18 lower bound (nostalgia <= beta W_diss) holds in "
                 f"{sum(r['Wdiss'] - r['nostalgia'] >= -1e-12 for r in rows)} of {n}; "
                 f"min slack {min(r['Wdiss'] - r['nostalgia'] for r in rows):.4f}")
        L.append(f"- Eq. 21 (heat out >= I_e + nostalgia) holds in "
                 f"{sum(r['heat_out'] - r['Ie'] - r['nostalgia'] >= -1e-12 for r in rows)} of {n}")
        L.append(f"- some step's nostalgia negative in "
                 f"{sum(r['min_step_nostalgia'] < -1e-12 for r in rows)} of {n}; "
                 f"summed nostalgia negative in {sum(r['nostalgia'] < -1e-12 for r in rows)}; "
                 f"W_diss negative in {sum(r['Wdiss'] < -1e-12 for r in rows)}; "
                 f"W_ex negative in {sum(r['Wex'] < -1e-12 for r in rows)}; "
                 f"min W_ex {min(r['Wex'] for r in rows):.4f}")
        if "Wdiss_path" in rows[0]:
            L.append(f"- per-protocol reading of Eqs. 9-10: bound holds in "
                     f"{sum(r['Wdiss_path'] - r['nostalgia'] >= -1e-12 for r in rows)} of {n}; "
                     f"min slack {min(r['Wdiss_path'] - r['nostalgia'] for r in rows):.4f}")
        L.append("")

    T = env_T(0.1, 0.05)
    rand = np.full((8, 2), 0.5)
    a0 = np.zeros((8, 2)); a0[:, 0] = 1
    au = np.zeros((8, 2))
    for x in range(8):
        au[x, decode(x)[0]] = 1
    L += ["## Feedback toy: partitions of the percept (u, v, y)", "",
          f"- predictive, random actions: {describe(predictive_partition(T, rand))}",
          f"- predictive, own closed loop a = u: {describe(predictive_partition(T, au))}",
          f"- predictive, fixed action a = 0: {describe(predictive_partition(T, a0))}",
          f"- interventional, target the outcome y: {describe(interventional_partition(T, 'y'))}",
          f"- interventional, target the whole next percept: {describe(interventional_partition(T, 'x'))}",
          "", "## Feedback toy: memories (per step, stationary, nats)", "",
          "| eps | delta | gap | memory | policy | success | I_mem | I_pred | nostalgia | relax | heat/step | H[S_t|S_t+1] |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in toy:
        L.append(f"| {r['eps']} | {r['delta']} | {r['gap']} | {r['memory']} | {r['policy']} | "
                 f"{r['success']:.3f} | {r['I_mem']:.3f} | {r['I_pred']:.3f} | {r['nostalgia']:.3f} | "
                 f"{r['relax']:.3f} | {r['heat_step']:.3f} | {r['H_overwrite']:.3f} |")
    with open(os.path.join(RES, "summary.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
