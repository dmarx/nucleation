"""LEAD-178: dynamical dependence of a block's aggregate in a linear
Gaussian VAR(1), and its two-sided bound.

Class: X_t = A X_{t-1} + e_t, A stable, e_t ~ N(0, S) iid, S > 0.
Coarse variable Y = L X (m x n, full row rank), observed without noise.
Dynamical dependence (Barnett-Seth, THEORY-257; THEORY-733):

    T(X -> Y) = 1/2 log det Var(Y_t | Y^-) / det Var(Y_t | X^-),
    Var(Y_t | X^-) = G := L S L^T.

Exact identity used: with P = Cov(X_{t-1} | Y_{t-1}, Y_{t-2}, ...),
    Var(Y_t | Y^-) = G + L A P A^T L^T,
and Sigma_|L <= P <= Pi_|L, where Pi_|L = Cov(X | L X) under the
stationary law and Sigma_|L = Cov(e | L e). Hence

    lower = 1/2 log det(I + G^-1 L A S_|L A^T L^T)
    <= T <= upper = 1/2 log det(I + G^-1 L A Pi_|L A^T L^T).

Everything is computed from exact stationary covariances; no simulation.
"""
import numpy as np


def lyap(A, Q):
    """Solve P = A P A^T + Q (A stable) by vectorisation."""
    n = A.shape[0]
    M = np.eye(n * n) - np.kron(A, A)
    P = np.linalg.solve(M, Q.reshape(-1)).reshape(n, n)
    return (P + P.T) / 2


def cond_cov(P, L):
    """Cov(X | L X) for X ~ N(0, P)."""
    G = L @ P @ L.T
    out = P - P @ L.T @ np.linalg.solve(G, L @ P)
    return (out + out.T) / 2


def filter_cov(A, L, S, tol=1e-15, maxit=200000):
    """P = Cov(X_{t-1} | Y_{<= t-1}) in the stationary regime: iterate
    predict (M = A P A^T + S) and noise-free update (P = cond_cov(M, L))
    from P = Pi_|L. Returns (P, iterations)."""
    Pi = lyap(A, S)
    P = cond_cov(Pi, L)
    for k in range(maxit):
        M = A @ P @ A.T + S
        Pn = cond_cov(M, L)
        d = np.max(np.abs(Pn - P)) / max(1.0, np.max(np.abs(P)))
        P = Pn
        if d < tol:
            return P, k + 1
    raise RuntimeError("filter did not converge (step %.1e)" % d)


def _half_logdet_ratio(G, extra):
    m = G.shape[0]
    sign, ld = np.linalg.slogdet(np.eye(m) + np.linalg.solve(G, extra))
    assert sign > 0
    return 0.5 * ld


def dd(A, L, S):
    """Exact dynamical dependence T(X -> LX) in nats."""
    P, _ = filter_cov(A, L, S)
    G = L @ S @ L.T
    return _half_logdet_ratio(G, L @ A @ P @ A.T @ L.T)


def bounds(A, L, S):
    """(lower, upper) of the sandwich, in nats."""
    G = L @ S @ L.T
    Pi = lyap(A, S)
    LA = L @ A
    lo = _half_logdet_ratio(G, LA @ cond_cov(S, L) @ LA.T)
    up = _half_logdet_ratio(G, LA @ cond_cov(Pi, L) @ LA.T)
    return lo, up


def dd_lags(A, L, S, p):
    """Cross-check from autocovariances alone: 1/2 log det
    Var(Y_t | Y_{t-1..t-p}) / det G, by Gaussian conditioning on the
    stacked lag vector. Converges to dd() as p grows."""
    Pi = lyap(A, S)
    m = L.shape[0]
    # Gamma_k = Cov(Y_{t+k}, Y_t) = L A^k Pi L^T
    Ak = [np.eye(A.shape[0])]
    for _ in range(p):
        Ak.append(A @ Ak[-1])
    Gam = [L @ Ak[k] @ Pi @ L.T for k in range(p + 1)]

    def cov(i, j):  # Cov(Y_{t-i}, Y_{t-j})
        k = j - i
        return Gam[k] if k >= 0 else Gam[-k].T
    # target Y_t (index 0), regressors Y_{t-1}..Y_{t-p}
    R = np.block([[cov(i, j) for j in range(1, p + 1)]
                  for i in range(1, p + 1)])
    c = np.hstack([cov(0, j) for j in range(1, p + 1)])
    V = Gam[0] - c @ np.linalg.solve(R, c.T)
    G = L @ S @ L.T
    return 0.5 * (np.linalg.slogdet(V)[1] - np.linalg.slogdet(G)[1])


def block_sum(sizes, I):
    """Row vector summing block I of a partition with the given sizes."""
    n = sum(sizes)
    L = np.zeros((1, n))
    s = sum(sizes[:I])
    L[0, s:s + sizes[I]] = 1.0
    return L


def block_diag(*Bs):
    n = sum(B.shape[0] for B in Bs)
    out = np.zeros((n, n))
    s = 0
    for B in Bs:
        k = B.shape[0]
        out[s:s + k, s:s + k] = B
        s += k
    return out


def equal_colsum_block(k, lam, rng, spread=0.6):
    """k x k block with every column summing to lam: lam times a random
    column-stochastic matrix, mixed towards uniform by (1 - spread).
    The leading eigenvalue is lam; the others are at most lam*spread
    in modulus."""
    W = rng.random((k, k))
    W /= W.sum(axis=0, keepdims=True)
    U = np.full((k, k), 1.0 / k)
    return lam * (spread * W + (1 - spread) * U)


def unequal_colsum_block(k, lam, rng, spread=0.6, tilt=0.3):
    """Same, then column j rescaled by (1 + tilt * z_j), z_j in [-1, 1],
    then the whole rescaled so the spectral radius is lam."""
    B = equal_colsum_block(k, 1.0, rng, spread)
    z = rng.uniform(-1, 1, k)
    B = B * (1 + tilt * z)[None, :]
    B *= lam / max(abs(np.linalg.eigvals(B)))
    return B


def random_spd(n, rng, cond=5.0):
    Qm, _ = np.linalg.qr(rng.standard_normal((n, n)))
    ev = np.exp(rng.uniform(0, np.log(cond), n))
    S = Qm @ np.diag(ev) @ Qm.T
    return (S + S.T) / 2
