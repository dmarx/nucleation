"""LEAD-057: three partitions of one dynamical model, and their counterfactual predictions.

Model: four units, linear Gaussian VAR(1), x_{t+1} = M x_t + e_t, e_t ~ N(0, I).
Intrinsic coupling pairs the units {0,1} and {2,3} (strength c) with a weak
background eps between all other units. An apparatus, a beam-like probe,
couples {0,2} and {1,3} with gain g; in the probe variant it has states of
its own.

Three accounts each assign a partition in every scenario:
  F   fixed, preexisting: {0,1}|{2,3} always.
  R   recovered from the measured dynamics in force: the pairing whose
      block-local prediction loses least (see block_loss).
  Arr arrangement-dependent: the apparatus's pairing {0,2}|{1,3} whenever
      the apparatus is in place; silent when it is not.

A partition is tested by what it licenses: that each block can be predicted
from its own past alone. block_loss is the excess one-step prediction error of
the best block-local linear predictors over the best full predictor, as a
fraction of the full error (0 means the blocks are exactly decoupled for
prediction). It is computed exactly from the stationary covariance and checked
by simulation.

Run: python3 -I three_partitions.py  (writes results.json beside this file)
"""
import itertools
import json
import os

import numpy as np

PAIRINGS = {
    "01|23": [[0, 1], [2, 3]],
    "02|13": [[0, 2], [1, 3]],
    "03|12": [[0, 3], [1, 2]],
}
FIXED = "01|23"
APPARATUS = "02|13"

A_SELF, C_PAIR, EPS, G = 0.3, 0.25, 0.02, 0.35


def coupling_matrix(n, pairs, strength, self_coupling=0.0, background=0.0):
    """Symmetric coupling: `strength` within each pair, `background` elsewhere."""
    M = np.full((n, n), background, dtype=float)
    np.fill_diagonal(M, self_coupling)
    for block in pairs:
        for i, j in itertools.permutations(block, 2):
            M[i, j] = strength
    return M


def stationary_cov(M, Sigma):
    """Solve Gamma = M Gamma M^T + Sigma for a stable M."""
    n = M.shape[0]
    if np.max(np.abs(np.linalg.eigvals(M))) >= 1:
        raise ValueError("unstable M")
    vec = np.linalg.solve(np.eye(n * n) - np.kron(M, M), Sigma.reshape(-1))
    return vec.reshape(n, n)


def block_loss(M, partition, Sigma=None):
    """Excess one-step error of block-local prediction, relative to full prediction."""
    n = M.shape[0]
    Sigma = np.eye(n) if Sigma is None else Sigma
    G_ = stationary_cov(M, Sigma)
    C = M @ G_  # cov(x_{t+1}, x_t)
    err = 0.0
    for B in partition:
        B = list(B)
        GBB = G_[np.ix_(B, B)]
        CBB = C[np.ix_(B, B)]
        resid = GBB - CBB @ np.linalg.solve(GBB, CBB.T)
        err += np.trace(resid)
    return err / np.trace(Sigma) - 1.0


def containment(M, unit, block, steps=30):
    """Share of the squared impulse response to `unit` that stays in `block`."""
    x = np.zeros(M.shape[0])
    x[unit] = 1.0
    inside = total = 0.0
    for _ in range(steps):
        x = M @ x
        inside += np.sum(x[list(block)] ** 2)
        total += np.sum(x ** 2)
    return inside / total


def recovered(M, candidates=PAIRINGS):
    """The candidate partition with least block loss, and all the losses."""
    losses = {k: block_loss(M, P) for k, P in candidates.items()}
    return min(losses, key=losses.get), losses


def simulated_block_loss(M, partition, T=200_000, seed=0):
    """Monte Carlo check of block_loss by least-squares fits on simulated data."""
    rng = np.random.default_rng(seed)
    n = M.shape[0]
    X = np.zeros((T, n))
    x = np.zeros(n)
    for t in range(T + 500):
        x = M @ x + rng.standard_normal(n)
        if t >= 500:
            X[t - 500] = x
    past, fut = X[:-1], X[1:]

    def mse(cols):
        P = past[:, cols]
        F = fut[:, cols]
        coef, *_ = np.linalg.lstsq(P, F, rcond=None)
        return np.sum((F - P @ coef) ** 2) / len(F)

    full = mse(list(range(n)))
    return sum(mse(list(B)) for B in partition) / full - 1.0


# --- scenarios --------------------------------------------------------------

def intrinsic(pairs=PAIRINGS[FIXED], c=C_PAIR):
    return coupling_matrix(4, pairs, c, A_SELF, EPS)


def apparatus_coupling(g):
    """The probe's contribution: gain g between the units it pairs."""
    return coupling_matrix(4, PAIRINGS[APPARATUS], g)


def scenarios():
    """Each: the M in force, and whether the apparatus is in place."""
    base = intrinsic()
    return {
        "S0 no apparatus": (base, False),
        "S1 apparatus in place, gain g": (base + apparatus_coupling(G), True),
        "S2 apparatus in place, gain 0": (base, True),
        "S3 apparatus removed, its coupling persists": (base + apparatus_coupling(G), False),
        "S4 no apparatus, internal rewiring to 03|12": (intrinsic(PAIRINGS["03|12"]), False),
    }


def assign(present, M):
    r, losses = recovered(M)
    return {"F": FIXED, "R": r, "Arr": APPARATUS if present else None}, losses


def probe_variant(g=G, d=0.3):
    """The apparatus with states of its own: units 4 (probe on 0,2) and 5 (on 1,3).

    Each probe is driven by the sum of its two units and feeds back into both
    with gain h, chosen so that the two-step path through the probe has gain
    about g. Returns the best balanced 3|3 bipartition of the six variables.
    """
    h = np.sqrt(g)
    M = np.zeros((6, 6))
    M[:4, :4] = intrinsic()
    for p, (i, j) in zip((4, 5), PAIRINGS[APPARATUS]):
        M[p, p] = d
        M[p, i] = M[p, j] = h / 2
        M[i, p] = M[j, p] = h / 2
    cands = {}
    for A in itertools.combinations(range(6), 3):
        if 0 not in A:
            continue
        B = tuple(sorted(set(range(6)) - set(A)))
        cands["".join(map(str, A)) + "|" + "".join(map(str, B))] = [list(A), list(B)]
    best, losses = recovered(M, cands)
    return best, losses, float(np.max(np.abs(np.linalg.eigvals(M))))


def gain_sweep(gains=np.round(np.linspace(0, 0.4, 9), 3)):
    out = []
    for g in gains:
        M = intrinsic() + apparatus_coupling(g)
        r, losses = recovered(M)
        out.append({"g": float(g), "R": r, "Arr": APPARATUS,
                    "loss_F": losses[FIXED], "loss_Arr": losses[APPARATUS]})
    return out


def main():
    res = {"parameters": {"a_self": A_SELF, "c_pair": C_PAIR, "eps": EPS, "g": G},
           "scenarios": {}}
    for name, (M, present) in scenarios().items():
        parts, losses = assign(present, M)
        res["scenarios"][name] = {
            "apparatus_in_place": present,
            "spectral_radius": float(np.max(np.abs(np.linalg.eigvals(M)))),
            "partitions": parts,
            "block_loss": losses,
            "loss_of_each_account": {k: (losses[v] if v else None) for k, v in parts.items()},
            "containment_of_impulse_to_unit0": {
                k: (containment(M, 0, next(B for B in PAIRINGS[v] if 0 in B)) if v else None)
                for k, v in parts.items()},
            "simulated_loss_check": {k: simulated_block_loss(M, P, T=100_000, seed=1)
                                     for k, P in PAIRINGS.items()},
        }
    res["gain_sweep"] = gain_sweep()
    best, losses, rho = probe_variant()
    res["probe_variant"] = {"best_3|3": best, "spectral_radius": rho,
                            "losses_top5": dict(sorted(losses.items(), key=lambda kv: kv[1])[:5])}
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json")
    with open(path, "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
