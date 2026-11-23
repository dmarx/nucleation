"""LEAD-007: equal present function, different later learning, in Lippl and
Lindsey's diagonal-linear-network PT+FT setup.

A two-layer diagonal linear network beta = v+ * w+ - v- * w- is pretrained by
gradient descent from small initialization on a sparse auxiliary teacher.
For a factor c > 0 the network P_c has first-layer weights c * w and
auxiliary readout v / c: its function is exactly that of P_1. Each P_c is
then fine-tuned by the same procedure (Lippl and Lindsey, section 3.3:
pathway weights set to their sum, readout re-initialized to gamma, gradient
descent on the main task to near-zero training error), on two main tasks:

- nested: the main teacher uses 2 of the 10 auxiliary dimensions;
- dense: the main teacher uses all 10 auxiliary dimensions with random
  coefficients.

The script also fine-tunes the readout alone (linear probing), where the
theory says P_c and P_1 reach the same function.

Results are appended, one JSON line per item, to results/runs.jsonl; items
already written are skipped on rerun.

Run:  OPENBLAS_NUM_THREADS=1 python3 -I diag_rescale.py
"""
import json
import os
import sys

import numpy as np

D = 100
K_AUX = 10
N_AUX = 80
N_MAIN = {"nested": 8, "dense": 14}
CS = [2.0, 1.0, 0.3, 0.1]
SEEDS = list(range(10))
GAMMA = 0.01
ALPHA = 1e-3
TOL = 1e-9
MAX_STEPS = 400_000

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results", "runs.jsonl")


def beta_of(wp, wm, vp, vm):
    return vp * wp - vm * wm


def train(X, y, wp, wm, vp, vm, train_first=True, tol=TOL, max_steps=MAX_STEPS):
    """Full-batch gradient descent on 1/(2n)||X beta - y||^2.

    Returns the trained parameters and the number of steps. The step size
    is recomputed every 500 steps from the current weight scale so that the
    effective step on beta stays below the stability limit.
    """
    wp, wm, vp, vm = (a.copy() for a in (wp, wm, vp, vm))
    n = X.shape[0]
    L = np.linalg.eigvalsh(X.T @ X / n).max()
    lr = None
    for step in range(max_steps):
        scale = max((wp ** 2 + vp ** 2).max(), (wm ** 2 + vm ** 2).max(), 1e-2)
        lr = 0.4 / (L * scale)
        b = beta_of(wp, wm, vp, vm)
        r = X @ b - y
        loss = 0.5 * float(r @ r) / n
        if loss < tol:
            return (wp, wm, vp, vm), step
        g = X.T @ r / n
        gvp, gvm = g * wp, -g * wm
        if train_first:
            gwp, gwm = g * vp, -g * vm
            wp -= lr * gwp
            wm -= lr * gwm
        vp -= lr * gvp
        vm -= lr * gvm
    return (wp, wm, vp, vm), max_steps


def make_teacher(rng, support, coefs):
    b = np.zeros(D)
    b[support] = coefs
    return b


def pretrain(seed):
    rng = np.random.default_rng(seed)
    supp = rng.choice(D, K_AUX, replace=False)
    b_aux = make_teacher(rng, supp, np.ones(K_AUX))
    X = rng.standard_normal((N_AUX, D))
    y = X @ b_aux
    init = [np.full(D, ALPHA) for _ in range(4)]
    params, steps = train(X, y, *init)
    return rng, supp, b_aux, params, steps


def rescale(params, c):
    """First layer times c, auxiliary readout divided by c: same function."""
    wp, wm, vp, vm = params
    return (c * wp, c * wm, vp / c, vm / c)


def finetune_start(params, gamma=GAMMA):
    """Lippl and Lindsey's step: pathway weights set to their sum, readout
    re-initialized to gamma, so the starting function is zero."""
    wp, wm, _, _ = params
    s = wp + wm
    return (s.copy(), s.copy(), np.full(D, gamma), np.full(D, gamma))


def main_task(rng, supp, kind):
    if kind == "nested":
        coefs = np.zeros(K_AUX)
        coefs[:2] = 1.0
    else:
        coefs = rng.uniform(0.5, 1.5, K_AUX) * rng.choice([-1, 1], K_AUX)
    b = make_teacher(rng, supp, coefs)
    X = rng.standard_normal((N_MAIN[kind], D))
    return b, X, X @ b


def done_keys():
    keys = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            for line in f:
                r = json.loads(line)
                keys.add((r["seed"], r["task"], r["c"], r["mode"]))
    return keys


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    have = done_keys()
    for seed in SEEDS:
        todo = [(t, c, m) for t in N_MAIN for c in CS for m in ("full", "probe")
                if (seed, t, c, m) not in have]
        if not todo:
            continue
        rng, supp, b_aux, params, ptsteps = pretrain(seed)
        pre_err = float(np.sum((beta_of(*params) - b_aux) ** 2))
        tasks = {}
        for kind in N_MAIN:
            tasks[kind] = main_task(np.random.default_rng(1000 + seed), supp, kind)
        for kind, c, mode in todo:
            pc = rescale(params, c)
            same_fn = float(np.max(np.abs(beta_of(*pc) - beta_of(*params))))
            b_main, X, y = tasks[kind]
            start = finetune_start(pc)
            out, steps = train(X, y, *start, train_first=(mode == "full"))
            b = beta_of(*out)
            rec = {
                "seed": seed, "task": kind, "c": c, "mode": mode,
                "pretrain_err": pre_err, "pretrain_steps": ptsteps,
                "aux_fn_maxdiff_after_rescale": same_fn,
                "ft_steps": steps,
                "train_loss": float(0.5 * np.mean((X @ b - y) ** 2)),
                "gen_err": float(np.sum((b - b_main) ** 2)),
                "beta": [round(float(x), 6) for x in b],
            }
            with open(OUT, "a") as f:
                f.write(json.dumps(rec) + "\n")
            print(seed, kind, c, mode, rec["gen_err"], steps, flush=True)


if __name__ == "__main__":
    sys.exit(main())
