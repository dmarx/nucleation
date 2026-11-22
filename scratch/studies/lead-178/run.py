"""LEAD-178 study. Writes results.jsonl (one line per item, append-only,
resumable) and results.md (summary).

Family: A = A* + eps*C, A* = diag(B_1, B_2, B_3) with block sizes 3, 4, 3,
C zero on the diagonal blocks (coupling between blocks only), ||C||_2 = 1,
S a random SPD noise covariance. The aggregate is the sum over block 0.

Parts:
  closed    B_1 has equal column sums (aggregate closed at eps = 0):
            T, lower, upper against eps; T/eps^2.
  unclosed  B_1 has unequal column sums: T against eps, and the floor.
  slowgap   closed, every block's leading eigenvalue 1 - gamma, eps fixed:
            T/eps^2 against gamma.
  fastgap   unclosed, the fast eigenvalues of B_1 shrunk towards 0
            (spread -> 0): the floor against spread.
  simon     closed, gamma = kappa * eps (the slow rate set by the
            coupling, Simon-Ando's scaling): T against eps.
  leftvec   the unclosed systems again, aggregated with block 0's left
            Perron vector instead of the plain sum: T against eps.
  normbound for closed, slowgap and simon items, the scalar bound
            eps^2 ||LC||^2 kappa(V)^2 ||S|| / (2 G (1 - rho^2)),
            V the eigenvectors of A, checked to dominate T.
"""
import json
import os

import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dd as D  # noqa: E402

OUT = os.path.join(HERE, "results.jsonl")
SIZES = [3, 4, 3]
N = sum(SIZES)
L = D.block_sum(SIZES, 0)
EPS = [0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625]


def done_keys():
    keys = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            for line in f:
                keys.add(json.loads(line)["key"])
    return keys


def emit(rec):
    with open(OUT, "a") as f:
        f.write(json.dumps(rec) + "\n")


def coupling(rng):
    C = rng.standard_normal((N, N))
    s = 0
    for k in SIZES:
        C[s:s + k, s:s + k] = 0
        s += k
    return C / np.linalg.norm(C, 2)


def system(seed, closed, lam=(0.9, 0.85, 0.8), spread=0.6):
    rng = np.random.default_rng(seed)
    if closed:
        B0 = D.equal_colsum_block(SIZES[0], lam[0], rng, spread)
    else:
        B0 = D.unequal_colsum_block(SIZES[0], lam[0], rng, spread)
    B1 = D.equal_colsum_block(SIZES[1], lam[1], rng)
    B2 = D.equal_colsum_block(SIZES[2], lam[2], rng)
    Astar = D.block_diag(B0, B1, B2)
    C = coupling(rng)
    S = D.random_spd(N, rng)
    return Astar, C, S


def measure(A, S, Lm=None):
    Lm = L if Lm is None else Lm
    rho = max(abs(np.linalg.eigvals(A)))
    if rho >= 0.9995:
        return None
    lo, up = D.bounds(A, Lm, S)
    t = D.dd(A, Lm, S)
    return dict(rho=float(rho), T=float(t), lower=float(lo), upper=float(up))


def main():
    have = done_keys()
    seeds = range(20)
    for part, closed in (("closed", True), ("unclosed", False)):
        for sd in seeds:
            Astar, C, S = system(sd, closed)
            for e in [0.0] + EPS:
                key = f"{part}/{sd}/{e}"
                if key in have:
                    continue
                m = measure(Astar + e * C, S)
                emit(dict(key=key, part=part, seed=sd, eps=e, **(m or {})))
    for sd in range(10):
        for g in [0.3, 0.1, 0.03, 0.01]:
            lam = (1 - g,) * 3
            Astar, C, S = system(1000 + sd, True, lam=lam)
            for e in [0.004, 0.002]:
                key = f"slowgap/{sd}/{g}/{e}"
                if key in have:
                    continue
                m = measure(Astar + e * C, S)
                emit(dict(key=key, part="slowgap", seed=sd, gamma=g, eps=e,
                          **(m or {})))
    for sd in range(10):
        for sp in [0.6, 0.3, 0.1, 0.03, 0.0]:
            Astar, C, S = system(2000 + sd, False, spread=sp)
            key = f"fastgap/{sd}/{sp}"
            if key in have:
                continue
            ev = sorted(abs(np.linalg.eigvals(Astar[:3, :3])))
            m = measure(Astar, S)
            emit(dict(key=key, part="fastgap", seed=sd, spread=sp,
                      fast=float(ev[-2]), **(m or {})))
    for sd in range(10):
        for e in [0.04, 0.02, 0.01, 0.005, 0.0025]:
            kappa = 2.0
            lam = (1 - kappa * e,) * 3
            Astar, C, S = system(3000 + sd, True, lam=lam)
            key = f"simon/{sd}/{e}"
            if key in have:
                continue
            m = measure(Astar + e * C, S)
            emit(dict(key=key, part="simon", seed=sd, eps=e, kappa=kappa,
                      **(m or {})))

    for sd in seeds:
        Astar, C, S = system(sd, False)
        w, Vl = np.linalg.eig(Astar[:3, :3].T)
        v = np.real(Vl[:, np.argmax(abs(w))])
        v = v / v.sum()
        Lw = np.zeros((1, N))
        Lw[0, :3] = v
        for e in [0.0] + EPS:
            key = f"leftvec/{sd}/{e}"
            if key in have:
                continue
            m = measure(Astar + e * C, S, Lw)
            emit(dict(key=key, part="leftvec", seed=sd, eps=e,
                      weights=[float(x) for x in v], **(m or {})))
    for sd in range(20):
        Astar, C, S = system(sd, True)
        for e in EPS:
            key = f"normbound/closed/{sd}/{e}"
            if key in have:
                continue
            emit(dict(key=key, part="normbound", family="closed", seed=sd,
                      eps=e, **normbound(Astar, C, S, e)))
    for sd in range(10):
        for g in [0.3, 0.1, 0.03, 0.01]:
            Astar, C, S = system(1000 + sd, True, lam=(1 - g,) * 3)
            for e in [0.004, 0.002]:
                key = f"normbound/slowgap/{sd}/{g}/{e}"
                if key in have:
                    continue
                emit(dict(key=key, part="normbound", family="slowgap",
                          seed=sd, gamma=g, eps=e,
                          **normbound(Astar, C, S, e)))
    for sd in range(10):
        for e in [0.04, 0.02, 0.01, 0.005, 0.0025]:
            Astar, C, S = system(3000 + sd, True, lam=(1 - 2.0 * e,) * 3)
            key = f"normbound/simon/{sd}/{e}"
            if key in have:
                continue
            emit(dict(key=key, part="normbound", family="simon", seed=sd,
                      eps=e, **normbound(Astar, C, S, e)))


def normbound(Astar, C, S, e):
    A = Astar + e * C
    w, V = np.linalg.eig(A)
    rho = max(abs(w))
    kap = np.linalg.cond(V)
    G = float((L @ S @ L.T)[0, 0])
    LC = L @ C
    b = e ** 2 * float((LC @ LC.T)[0, 0]) * kap ** 2 * np.linalg.norm(S, 2) / (
        2 * G * (1 - rho ** 2))
    return dict(T=float(D.dd(A, L, S)), scalar_bound=float(b),
                kappaV=float(kap), rho=float(rho))


if __name__ == "__main__":
    main()
