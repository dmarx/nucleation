"""Power simulation for a Contextuality-by-Default test on a rank-4 cyclic system (LEAD-182).

Run from the repository root:

    python3 -I scratch/studies/lead-182/power.py            # full grid
    python3 -I scratch/studies/lead-182/power.py --quick    # a few cells, for timing

Each grid cell is written as one JSON line to results.jsonl as soon as it is
computed; a rerun skips cells already written (resume). Nothing is held in
memory to be written at the end.

Design simulated: between-subjects, each respondent sees one of the four
contexts and gives two binary answers; n respondents a context (after
exclusions). The true model is cbd.true_system(dc, signal, base) or the
Lo et al. (2023) table. Tests, all one-sided at alpha = 0.05 unless named:

- detect_boot_fixed: percentile-bootstrap lower bound of Delta_C, with the
  sign pattern fixed in advance, above 0;
- detect_boot_max: the same with s_odd taken as the maximum over the eight
  odd sign patterns, recomputed in each resample;
- detect_wald_fixed: delta-method lower bound, fixed signs, above 0;
- detect_boot_fixed_k8: bootstrap lower bound at alpha = 0.05/8 (eight
  items, Bonferroni), above 0;
- detect_boot_shrink: bootstrap lower bound, fixed signs, each content's
  |difference| soft-thresholded by one standard error (cbd.system_moments);
- absent_boot_fixed / absent_wald_fixed / absent_boot_shrink: upper bound below 0 (noncontextual
  with confidence; meaningful only when the true Delta_C is below 0).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cbd  # noqa: E402

SIGNS = (1, 1, 1, -1)
ALPHA = 0.05
ALPHA_K8 = 0.05 / 8
Z = 1.6448536269514722


def lo_system():
    t = np.array([[0.402, 0.097, 0.097, 0.402],
                  [0.044, 0.455, 0.455, 0.044],
                  [0.345, 0.154, 0.154, 0.345],
                  [0.344, 0.155, 0.155, 0.344]])
    t = t / t.sum(axis=1, keepdims=True)
    swap = lambda r: r[[0, 2, 1, 3]]
    return np.array([t[0], swap(t[2]), t[3], swap(t[1])])


def lo_with_signalling(signal: float):
    """Lo et al.'s correlations kept, marginals shifted by +/- signal/8 per variable."""
    P = lo_system()
    e, _ = cbd.system_moments(P)
    h = signal / 8.0
    Q = np.array([cbd.cells_from_moments(h, -h, e[k]) for k in range(4)])
    if (Q < 0).any():
        return None
    return Q


def run_cell(P, n, reps, B, rng):
    counts = np.stack([rng.multinomial(n, P[k], size=reps) for k in range(4)], axis=1)
    est_f = cbd.delta_c(counts, SIGNS)
    est_m = cbd.delta_c(counts)
    _, sig_hat = cbd.system_moments(counts)
    qf = cbd.bootstrap_bounds(counts, rng, B, [ALPHA_K8, ALPHA, 1 - ALPHA], SIGNS)
    qm = cbd.bootstrap_bounds(counts, rng, B, [ALPHA], None)
    qs = cbd.bootstrap_bounds(counts, rng, B, [ALPHA, 1 - ALPHA], SIGNS, shrink=1.0)
    est_s = cbd.delta_c(counts, SIGNS, shrink=1.0)
    wl, wu = cbd.wald_bounds(counts, Z, SIGNS)
    return {
        "est_fixed_mean": float(est_f.mean()), "est_fixed_sd": float(est_f.std()),
        "est_max_mean": float(est_m.mean()),
        "est_shrink_mean": float(est_s.mean()),
        "signal_hat_mean": float(sig_hat.mean()),
        "detect_boot_fixed": float((qf[1] > 0).mean()),
        "detect_boot_fixed_k8": float((qf[0] > 0).mean()),
        "detect_boot_max": float((qm[0] > 0).mean()),
        "detect_wald_fixed": float((wl > 0).mean()),
        "detect_boot_shrink": float((qs[0] > 0).mean()),
        "absent_boot_fixed": float((qf[2] < 0).mean()),
        "absent_boot_shrink": float((qs[1] < 0).mean()),
        "absent_wald_fixed": float((wu < 0).mean()),
    }


def grid(quick=False):
    ns = [100, 400, 1000, 1600, 2500, 4000]
    dcs = [-0.3, -0.15, 0.0, 0.1, 0.19, 0.3]
    sigs = [0.0, 0.1, 0.3, 0.6]
    if quick:
        ns, dcs, sigs = [400], [0.0, 0.19], [0.0, 0.3]
    for sig in sigs:
        for n in ns:
            yield {"model": "lo", "dc": None, "signal": sig, "base": 0.0, "n": n}
    for dc in dcs:
        for sig in sigs:
            for n in ns:
                yield {"model": "symmetric", "dc": dc, "signal": sig, "base": 0.0, "n": n}
    if not quick:
        for dc in (0.0, 0.19):
            for sig in sigs:
                for n in (1000, 2500):
                    yield {"model": "symmetric", "dc": dc, "signal": sig, "base": 0.15, "n": n}


def key(c):
    return f"{c['model']}|{c['dc']}|{c['signal']}|{c['base']}|{c['n']}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--reps", type=int, default=800)
    ap.add_argument("--boot", type=int, default=799)
    ap.add_argument("--out", default=os.path.join(HERE, "results.jsonl"))
    a = ap.parse_args()
    done = set()
    if os.path.exists(a.out):
        with open(a.out) as f:
            done = {key(json.loads(l)) for l in f if l.strip()}
    for i, c in enumerate(grid(a.quick)):
        if key(c) in done:
            continue
        if c["model"] == "lo":
            P = lo_with_signalling(c["signal"])
        else:
            P = cbd.true_system(c["dc"], c["signal"], c["base"])
        if P is None:
            rec = dict(c, feasible=False)
        else:
            true_dc = float(cbd.delta_c(P, SIGNS))
            seed = i * 7919 + 12345
            rng = np.random.default_rng(seed)
            t0 = time.time()
            rec = dict(c, feasible=True, true_dc=true_dc, reps=a.reps, boot=a.boot, seed=seed,
                       **run_cell(P, c["n"], a.reps, a.boot, rng))
            rec["seconds"] = round(time.time() - t0, 2)
        with open(a.out, "a") as f:
            f.write(json.dumps(rec) + "\n")
        print(json.dumps(rec), flush=True)


if __name__ == "__main__":
    main()
