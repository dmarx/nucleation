"""Receiver-restricted order on experiments: finite computations.

Conventions (row-stochastic matrices):
  P   experiment, |Theta| x |X|, P[t, x] = P(x | t)
  G   garbling on the medium X, |X| x |X|; the garbled experiment is P @ G
  d   decision rule, |X| x |A|, d[x, a] = P(a | x)
  L   loss, |Theta| x |A|
  pi  prior on Theta
A receiver class R (for one action set A) is given by a finite list of
rule matrices, the vertices of its closed convex hull. Its usable risk is
  V_R(P; L, pi) = min_{d in R} sum_t pi_t sum_a (P d)[t, a] L[t, a],
a linear functional minimised over the hull, so the vertices suffice.
"""
import itertools

import numpy as np
from scipy.optimize import linprog


def deterministic_rules(n_in, n_act):
    """All deterministic rules from n_in inputs to n_act actions."""
    out = []
    for f in itertools.product(range(n_act), repeat=n_in):
        d = np.zeros((n_in, n_act))
        d[np.arange(n_in), f] = 1.0
        out.append(d)
    return out


def factoring_class(T, n_act):
    """Rules that read the medium only through the kernel T (|X| x |Y|):
    {T @ D : D any rule on Y}. Vertices: T @ D for deterministic D."""
    return [T @ D for D in deterministic_rules(T.shape[1], n_act)]


def unrestricted_class(n_x, n_act):
    return deterministic_rules(n_x, n_act)


def usable_risk(P, R, L, pi):
    return min(float(np.sum(pi[:, None] * (P @ d) * L)) for d in R)


def in_hull(point, vertices):
    """Is `point` (flattened) in the convex hull of `vertices`? (LP)"""
    V = np.array([v.ravel() for v in vertices]).T  # dim x k
    k = V.shape[1]
    A_eq = np.vstack([V, np.ones((1, k))])
    b_eq = np.concatenate([point.ravel(), [1.0]])
    res = linprog(np.zeros(k), A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * k,
                  method="highs")
    return res.status == 0


def separating_loss(point, vertices):
    """max t s.t. t <= <v_k - point, L> for all k, |L| <= 1.
    Returns (t, L). t > 1e-9 means point is outside the hull and L is a
    loss (under the uniform-weighted pairing) on which `point` beats
    every vertex."""
    shape = point.shape
    n = point.size
    # variables: L (n), t (1); minimise -t
    c = np.zeros(n + 1)
    c[-1] = -1.0
    A_ub, b_ub = [], []
    for v in vertices:
        row = np.zeros(n + 1)
        row[:n] = -(v - point).ravel()
        row[-1] = 1.0
        A_ub.append(row)
        b_ub.append(0.0)
    bounds = [(-1, 1)] * n + [(None, None)]
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=bounds,
                  method="highs")
    return -res.fun, res.x[:n].reshape(shape)


def achievable(P, R):
    """Vertices of Ach_R(P) = conv{P d : d in R}."""
    return [P @ d for d in R]


def r_dominates(P, Pp, R, Rp=None):
    """Ach criterion: P >=_R P' for every loss on A iff
    Ach_R(P') is contained in Ach_R(P). Returns (bool, witness loss or None).
    The witness is in 'joint' form W[t,a]; for a prior pi with full
    support the loss L = W / pi[:, None] separates under pi."""
    Rp = R if Rp is None else Rp
    verts = achievable(P, R)
    for dp in Rp:
        q = Pp @ dp
        if not in_hull(q, verts):
            t, W = separating_loss(q, verts)
            return False, W
    return True, None


def respects(G, R):
    """G is in Mon(R) iff every d in R has G @ d in the hull of R."""
    return all(in_hull(G @ d, R) for d in R)


def factors_through(G, T):
    """Does G @ T = T @ H for some stochastic H? (LP on H)."""
    nx, ny = T.shape
    # unknown H (ny x ny), constraints T H = G T, rows of H sum to 1
    n = ny * ny
    A, b = [], []
    GT = G @ T
    for x in range(nx):
        for j in range(ny):
            row = np.zeros(n)
            for y in range(ny):
                row[y * ny + j] = T[x, y]
            A.append(row)
            b.append(GT[x, j])
    for y in range(ny):
        row = np.zeros(n)
        row[y * ny:(y + 1) * ny] = 1.0
        A.append(row)
        b.append(1.0)
    res = linprog(np.zeros(n), A_eq=np.array(A), b_eq=np.array(b),
                  bounds=[(0, None)] * n, method="highs")
    return res.status == 0


def random_stochastic(rng, n, m, sparsity=0.0):
    M = rng.random((n, m)) * (rng.random((n, m)) >= sparsity)
    M[np.arange(n), rng.integers(0, m, n)] += 0.05
    return M / M.sum(axis=1, keepdims=True)


def deterministic_map(f, m):
    T = np.zeros((len(f), m))
    T[np.arange(len(f)), f] = 1.0
    return T


def compatible_garbling(rng, f, m):
    """A garbling G with G T = T H, built from H on Y and a distribution on
    each fibre of the deterministic map f."""
    n = len(f)
    H = random_stochastic(rng, m, m)
    fib = [np.flatnonzero(np.array(f) == y) for y in range(m)]
    q = np.zeros((m, n))
    for y in range(m):
        w = rng.random(len(fib[y]))
        q[y, fib[y]] = w / w.sum()
    return np.array([H[f[x]] @ q for x in range(n)])
