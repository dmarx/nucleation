"""LEAD-192: numerical check of the projection perturbation bound for the
compressed diffusion-wavelet chain.

The compressed chain is written in ambient coordinates:

    A_0 = T,   A_{i+1} = P_{i+1} A_i^2 P_{i+1},

where P_{i+1} is the orthogonal projector onto the columns kept when A_i is
truncated. For an orthonormal basis Phi_i of Ran P_i this is exactly
Coifman and Maggioni's T_i = Phi_i^T A_i Phi_i, with T_{i+1} = M_i M_i^T
(their (4.16)); for selected, non-orthogonal columns it is the
pseudo-inverse compression Sevi, Rilling and Borgnat restate.

The bound checked (CLAIM filed by the lead run of 2026-11-23):

    f_0 = 0,  f_{i+1} <= (||T^{2^i}|| + ||A_i||) f_i + ||A_i|| (d_i + d'_i)
    ||P_{j+1} - Pi_{j+1}|| <= (d_j + f_j) / sigma_min(R^{2^j})

with f_i = ||T^{2^i} - A_i||, d_i = ||(I - P_{i+1}) A_i|| (column residual),
d'_i = ||A_i (I - P_{i+1})|| (row residual), Pi_{j+1} the orthogonal
projector onto a T-invariant subspace of dimension rank P_{j+1}, and
R = Q^T T Q for an orthonormal basis Q of that subspace. For symmetric T
with ||T|| <= 1: f_j <= sum_i 2^{j-i} d_i and sigma_min = lambda_k^{2^j}.

Run with: python3 -I scratch/studies/lead-192/lead192.py
"""

from __future__ import annotations

import json
import sys

import numpy as np
import scipy.linalg as sla

np.set_printoptions(precision=3, suppress=False)


# ---------------------------------------------------------------- operators

def circle_operator(n: int) -> np.ndarray:
    """Coifman and Maggioni's circle example: T = (T')^2, T' the periodic
    three-point average with 1/2 on the diagonal and 1/4 off it."""
    Tp = 0.5 * np.eye(n)
    for i in range(n):
        Tp[i, (i + 1) % n] += 0.25
        Tp[i, (i - 1) % n] += 0.25
    return Tp @ Tp


def clouds_operator(n_per: int = 60, sep: float = 6.0, sigma: float = 1.0,
                    seed: int = 0) -> np.ndarray:
    """Symmetric normalized heat kernel on three Gaussian clouds in R^3,
    lazy (T = (I + D^-1/2 W D^-1/2)/2) so the spectrum is in [0, 1]."""
    rng = np.random.default_rng(seed)
    centers = np.array([[0, 0, 0], [sep, 0, 0], [0, sep, 0]], float)
    X = np.vstack([c + rng.standard_normal((n_per, 3)) for c in centers])
    D2 = ((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)
    W = np.exp(-D2 / (2 * sigma ** 2))
    d = W.sum(1)
    S = W / np.sqrt(np.outer(d, d))
    return 0.5 * (np.eye(len(X)) + S)


def spectrum_operator(lams: np.ndarray, seed: int = 0) -> np.ndarray:
    """Symmetric operator with a prescribed spectrum and a random eigenbasis."""
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((len(lams), len(lams))))
    return (Q * lams) @ Q.T


def directed_operator(n: int = 120, k: int = 3, beta: float = 0.3,
                      gamma: float = 0.5, seed: int = 0) -> np.ndarray:
    """Lazy random walk on a directed small-world graph, symmetrized by the
    stationary measure as Sevi et al. do: T = Pi^1/2 (g I + (1-g) P) Pi^-1/2.
    ||T||_2 <= 1 for any stationary pi; T is not symmetric."""
    rng = np.random.default_rng(seed)
    A = np.zeros((n, n))
    for i in range(n):
        for s in range(1, k + 1):
            j = (i + s) % n
            if s > 1 and rng.random() < beta:  # keep i -> i+1: strongly connected
                j = int(rng.integers(n))
                while j == i:
                    j = int(rng.integers(n))
            A[i, j] = 1.0
    P = A / A.sum(1, keepdims=True)
    P = gamma * np.eye(n) + (1 - gamma) * P
    w, V = np.linalg.eig(P.T)
    pi = np.real(V[:, np.argmin(np.abs(w - 1))])
    pi = np.abs(pi) / np.abs(pi).sum()
    s = np.sqrt(pi)
    return (s[:, None] * P) / s[None, :]


# -------------------------------------------------------------- truncations

def truncate_pivoted_qr(A: np.ndarray, eps: float) -> np.ndarray:
    """Orthonormal basis of the columns kept by column-pivoted QR, keeping
    while |R_kk| > eps (the rule of Coifman and Maggioni's section 5)."""
    Q, R, _ = sla.qr(A, pivoting=True, mode="economic")
    diag = np.abs(np.diag(R))
    k = int(np.sum(diag > eps))
    return Q[:, :k]


def truncate_svd(A: np.ndarray, eps: float) -> np.ndarray:
    """Exact truncation: left singular vectors with singular value > eps."""
    U, s, _ = np.linalg.svd(A)
    return U[:, : int(np.sum(s > eps))]


def truncate_noisy(A: np.ndarray, eps: float, noise: float, rng) -> np.ndarray:
    """Exact truncation followed by a random tilt of size about `noise`,
    re-projected into Ran A's support so that nesting is kept."""
    U = truncate_svd(A, eps)
    support = truncate_svd(A, 1e-13)  # the current level's space
    G = U + noise * support @ rng.standard_normal((support.shape[1], U.shape[1]))
    Q, _ = np.linalg.qr(G)
    return Q


# ---------------------------------------------------------------- the chain

def matpow_sym(T: np.ndarray, m: int) -> np.ndarray:
    return np.linalg.matrix_power(T, m)


def run_chain(T: np.ndarray, eps: float, levels: int, truncate) -> list[dict]:
    """Run the compressed chain and record every quantity in the bound."""
    n = T.shape[0]
    sym = np.allclose(T, T.T)
    if sym:
        lam, Xi = np.linalg.eigh(T)
        order = np.argsort(lam)[::-1]
        lam, Xi = lam[order], Xi[:, order]
    else:
        # ordered real Schur form: leading k columns span the dominant
        # invariant subspace of dimension k (ordered by |eigenvalue|)
        Tt, Z = sla.schur(T, output="complex")
        w = np.diag(Tt)
        lam = w[np.argsort(-np.abs(w))]
    A = T.copy()
    f = 0.0
    out = []
    Tm = T.copy()  # T^{2^j}
    for j in range(levels):
        Qk = truncate(A)
        k = Qk.shape[1]
        if k == 0:
            break
        P = Qk @ Qk.T
        I = np.eye(n)
        d_col = np.linalg.norm((I - P) @ A, 2)
        d_row = np.linalg.norm(A @ (I - P), 2)
        nA = np.linalg.norm(A, 2)
        nTm = np.linalg.norm(Tm, 2)
        f_true = np.linalg.norm(Tm - A, 2)
        # target invariant subspace of dimension k
        if sym:
            Qt = Xi[:, :k]
            smin = lam[k - 1] ** (2 ** j)
            lam_next = lam[k] ** (2 ** j) if k < n else 0.0
            gap_ratio = lam_next / smin
        else:
            # reorder Schur so the k largest-|lambda| eigenvalues lead
            thr = np.sort(np.abs(np.diag(sla.schur(T, output="complex")[0])))[::-1]
            cut = (thr[k - 1] + thr[k]) / 2 if k < n else 0.0
            Tt, Z, sdim = sla.schur(T, output="complex",
                                    sort=lambda z: abs(z) > cut)
            Qt = Z[:, :sdim]
            if sdim != k:
                Qt = None
            if Qt is not None:
                Rm = Qt.conj().T @ Tm @ Qt
                smin = np.linalg.svd(Rm, compute_uv=False)[-1]
            else:
                smin = np.nan
            gap_ratio = (thr[k] / thr[k - 1]) ** (2 ** j) if k < n else 0.0
        if Qt is not None:
            Pt = Qt @ Qt.conj().T
            s_true = np.linalg.norm(P - Pt, 2)
        else:
            s_true = np.nan
        bound_s = (d_col + f_true) / smin if smin > 0 else np.inf
        rec = dict(j=j, k=k, d_col=d_col, d_row=d_row, normA=nA, normTm=nTm,
                   f_true=f_true, f_bound=f, s_true=s_true, s_bound=bound_s,
                   s_bound_chain=(d_col + f) / smin if smin > 0 else np.inf,
                   smin=smin, gap_ratio=gap_ratio,
                   closure_Tm=np.linalg.norm((I - P) @ Tm @ P, 2),
                   closure_T=np.linalg.norm((I - P) @ T @ P, 2))
        if sym:
            # graded per-vector bound on the kept eigenvectors
            res = np.linalg.norm((I - P) @ Xi[:, :k], axis=0)
            gb = (d_col + f_true) / lam[:k] ** (2 ** j)
            rec["graded_ok"] = bool(np.all(res <= gb * (1 + 1e-9) + 1e-12))
            rec["top_vec_err"] = float(res[0])
        out.append(rec)
        # recursion for the next level
        f = (nTm + nA) * f + nA * (d_col + d_row)
        A = P @ A @ A @ P
        Tm = Tm @ Tm
    return out


def main() -> None:
    rng = np.random.default_rng(1)
    cases = {
        "circle-256-qr": (circle_operator(256), 1e-4, 12,
                          lambda A: truncate_pivoted_qr(A, 1e-4)),
        "clouds-qr": (clouds_operator(), 1e-4, 14,
                      lambda A: truncate_pivoted_qr(A, 1e-4)),
        "gapped-noisy": (spectrum_operator(np.r_[np.ones(1), 0.999, 0.998,
                                                  np.linspace(0.6, 0.0, 117)]),
                         1e-4, 10,
                         lambda A: truncate_noisy(A, 1e-4, 1e-6, rng)),
        "directed-qr": (directed_operator(), 1e-4, 10,
                        lambda A: truncate_pivoted_qr(A, 1e-4)),
    }
    results = {}
    for name, (T, eps, L, tr) in cases.items():
        rows = run_chain(T, eps, L, tr)
        results[name] = rows
        print(f"== {name}")
        print(" j    k   d_col     d_row     f_true    f_bound   s_true    s_bound   chain_bd  ratio^M  clos_T")
        for r in rows:
            print(f"{r['j']:2d} {r['k']:4d}  {r['d_col']:.2e}  {r['d_row']:.2e}  "
                  f"{r['f_true']:.2e}  {r['f_bound']:.2e}  {r['s_true']:.2e}  "
                  f"{r['s_bound']:.2e}  {r['s_bound_chain']:.2e}  {r['gap_ratio']:.2e}  "
                  f"{r['closure_T']:.2e}")
    with open(sys.argv[1] if len(sys.argv) > 1 else "/dev/stdout", "w") as fh:
        json.dump(results, fh, default=float, indent=1)


if __name__ == "__main__":
    main()
