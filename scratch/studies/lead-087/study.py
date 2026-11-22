"""LEAD-087 study: run every arm for each seed, append one JSON line per
(seed, arm) to results.jsonl, skipping lines already written.

    OMP_NUM_THREADS=1 python3 -I study.py [n_seeds]
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as M  # noqa: E402

OUT = os.path.join(HERE, "results.jsonl")


def done_keys():
    if not os.path.exists(OUT):
        return set()
    with open(OUT) as f:
        return {(r["seed"], r["arm"]) for r in map(json.loads, f) if r}


def diff_schema_concordance(rng):
    """Members each trained on their own randomly drawn teacher."""
    P = rng.normal(0, 1.0, (M.N, M.K, M.D))
    Ws = np.stack([M.teacher(rng) for _ in range(M.N)])
    idx = np.arange(M.N)
    for _ in range(M.T_TRAIN):
        c = rng.integers(M.K, size=M.N)
        X = Ws[idx, c] + rng.normal(0, M.NOISE, (M.N, M.D))
        P[idx, c] += M.LR_TRAIN * (X - P[idx, c])
    return M.concordance(P)


def agreement(P, W, rng, n=200):
    c = rng.integers(M.K, size=n)
    X = W[c] + rng.normal(0, M.NOISE, (n, M.D))
    L = np.stack([M.nearest(np.repeat(P[k][None], n, 0), X) for k in range(M.N)])
    iu = np.triu_indices(M.N, 1)
    return float((L[iu[0]] == L[iu[1]]).mean())


def proj(Pa, Pb, S, a, u, delta, rec_lo, rec_hi):
    """Mean over the window and over members S of the displacement of
    prototype a from the twin, along u, as a fraction of delta."""
    d = (Pa[rec_lo:rec_hi][:, S, a] - Pb[rec_lo:rec_hi][:, S, a]) @ u
    return float(d.mean() / delta)


def one_seed(seed, keys):
    rng = np.random.default_rng(seed)
    W = M.teacher(rng)
    P0 = M.train(rng, W, social=False)
    P0s = M.train(rng, W, social=True)
    c_diff = diff_schema_concordance(rng)
    R = M.draws(rng)
    S = rng.choice(M.N, int(M.F_S * M.N), replace=False)
    U = np.setdiff1d(np.arange(M.N), S)
    a = int(rng.integers(M.K))
    u = rng.normal(size=M.D)
    u /= np.linalg.norm(u)
    nn = np.sort(np.linalg.norm(W - W[a], axis=1))[1]
    delta = 0.5 * nn
    vec = delta * u
    probe = np.random.default_rng(10_000 + seed)

    # match world-label events across arms to the evidential arm's checks
    ev = M.run(P0, W, R, "evidential", M.Q_BASE)
    e_rate = ev["check_rate"]
    rec = 5
    lo, hi = M.T_PERT // rec + 1, (M.T_PERT + M.WINDOW) // rec + 1
    for arm in M.ARMS:
        if (seed, arm) in keys:
            continue
        start = P0s if arm == "learned-cut" else P0
        q = M.Q_BASE if arm == "evidential" else M.Q_BASE + e_rate
        tu = ev if arm == "evidential" else M.run(start, W, R, arm, q)
        pu = M.run(start, W, R, arm, q, pert=(S, a, vec))
        tw = M.run(start, W, R, arm, q, shift=(a, vec))
        pw = M.run(start, W, R, arm, q, pert=(S, a, vec), shift=(a, vec))
        Tu, Pu, Tw, Pw = tu["traj"], pu["traj"], tw["traj"], pw["traj"]
        k0 = M.T_PERT // rec            # recorded before the perturbation
        row = dict(
            seed=seed, arm=arm, q=q, e_rate=e_rate, delta=delta,
            concordance=M.concordance(Tu[k0]),
            concordance_diff=c_diff,
            agreement=agreement(Tu[k0], W, probe),
            s_u=proj(Pu, Tu, U, a, u, delta, lo, hi),
            s_w=proj(Pw, Tw, U, a, u, delta, lo, hi),
            g_u=1 - proj(Pu, Tu, S, a, u, delta, lo, hi),
            g_w=1 - proj(Pw, Tw, S, a, u, delta, lo, hi),
            agency_vote=M.agency(tu["match_vote"]),
            agency_none=M.agency(tu["match_none"]),
            check_rate=tu["check_rate"],
        )
        with open(OUT, "a") as f:
            f.write(json.dumps(row) + "\n")
        print(seed, arm, {k: round(v, 3) for k, v in row.items()
                          if isinstance(v, float)}, flush=True)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    keys = done_keys()
    for seed in range(n):
        if all((seed, arm) in keys for arm in M.ARMS):
            continue
        one_seed(seed, keys)
