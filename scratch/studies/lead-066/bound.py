"""LEAD-066: the commutator bound for level-wise acquisition, and its checks.

Pure numpy/scipy. See README.md for the statements being checked.
"""
import numpy as np
from scipy.optimize import brentq


# ---------------------------------------------------------------- tree and data

def haar(depth):
    """Orthonormal Haar basis of R^(2^depth), columns grouped by level.

    Returns (H, level) with level[j] the level of column j: 0 for the
    constant vector, l = 1..depth for the 2^(l-1) vectors that split the
    two children of a node at depth l-1.
    """
    n = 2 ** depth
    cols, lev = [np.ones(n) / np.sqrt(n)], [0]
    for l in range(1, depth + 1):
        block = n // 2 ** (l - 1)          # size of a depth-(l-1) subtree
        for k in range(2 ** (l - 1)):
            v = np.zeros(n)
            v[k * block: k * block + block // 2] = 1.0
            v[k * block + block // 2: (k + 1) * block] = -1.0
            cols.append(v / np.linalg.norm(v))
            lev.append(l)
    return np.array(cols).T, np.array(lev)


def projectors(H, level):
    return [H[:, level == l] @ H[:, level == l].T for l in range(level.max() + 1)]


def tree_inputs(H, level, c, d, rng):
    """X0 = sqrt(n) H diag(c_level) R, R with orthonormal rows (n x d), d >= n."""
    n = H.shape[0]
    R = np.linalg.qr(rng.standard_normal((d, n)))[0].T
    return np.sqrt(n) * H @ np.diag(np.asarray(c)[level]) @ R


def tree_target(H, level, g, rng):
    """Scalar target with norm sqrt(n) g_l in level l, random direction in it."""
    n = H.shape[0]
    y = np.zeros(n)
    for l in range(level.max() + 1):
        if g[l] == 0:
            continue
        cols = H[:, level == l]
        z = rng.standard_normal(cols.shape[1])
        y += np.sqrt(n) * g[l] * cols @ (z / np.linalg.norm(z))
    return y


def perturb(X0, sigma, rng):
    """X0 + Delta with ||Delta||_F = sigma ||X0||_F, Gaussian direction."""
    Z = rng.standard_normal(X0.shape)
    return X0 + sigma * np.linalg.norm(X0) / np.linalg.norm(Z) * Z


# ---------------------------------------------------------------- kernels

def gram(X):
    return X @ X.T / X.shape[1]


def k_linear(X):
    return gram(X)


def k_relu_ntk(X):
    """Infinite-width NTK of a two-layer ReLU network (both layers trained)."""
    G = gram(X)
    nrm = np.sqrt(np.diag(G))
    cos = np.clip(G / np.outer(nrm, nrm), -1.0, 1.0)
    th = np.arccos(cos)
    k0 = (np.pi - th) / (2 * np.pi)
    k1 = np.outer(nrm, nrm) * (np.sin(th) + (np.pi - th) * cos) / (2 * np.pi)
    return G * k0 + k1


def k_rbf(X, s=1.0):
    G = gram(X)
    q = np.diag(G)
    return np.exp(-(q[:, None] + q[None, :] - 2 * G) / (2 * s ** 2))


KERNELS = {"linear": k_linear, "relu_ntk": k_relu_ntk, "rbf": k_rbf}


# ---------------------------------------------------------------- operator quantities

def commutator_norms(A, Ps):
    return np.array([np.linalg.norm(A @ P - P @ A, 2) for P in Ps])


def pinch(A, Ps):
    return sum(P @ A @ P for P in Ps)


def block_extremes(A, H, level):
    """(lambda_l, Lambda_l): extreme eigenvalues of A compressed to level l."""
    lo, hi = [], []
    for l in range(level.max() + 1):
        B = H[:, level == l]
        w = np.linalg.eigvalsh(B.T @ A @ B)
        lo.append(w[0]); hi.append(w[-1])
    return np.array(lo), np.array(hi)


class Flow:
    """e(t) = exp(-A t) e0 by eigendecomposition, vectorised over times."""

    def __init__(self, A, e0):
        w, V = np.linalg.eigh((A + A.T) / 2)
        self.w, self.V, self.c = np.clip(w, 0, None), V, V.T @ e0

    def __call__(self, t):
        t = np.atleast_1d(t)
        return self.V @ (np.exp(-np.outer(self.w, t)) * self.c[:, None])   # n x len(t)


def phi(t, lam, a):
    t = np.asarray(t, float)
    if abs(lam - a) < 1e-12 * max(lam, 1e-300):
        return t * np.exp(-lam * t)
    return (np.exp(-a * t) - np.exp(-lam * t)) / (lam - a)


def theorem1_bound(t, eta, lam, a, e0norm):
    """Absolute bound on ||P_l (e(t) - e^D(t))||."""
    return eta * e0norm * phi(t, lam, a)


def acquisition_time(flow, P, delta, tmax, ngrid=4000):
    """First t with ||P e(t)||^2 / ||P e(0)||^2 <= delta (np.inf if none by tmax)."""
    e0 = flow(0.0)[:, 0]
    base = np.linalg.norm(P @ e0) ** 2
    ts = np.concatenate([[0.0], np.geomspace(tmax * 1e-7, tmax, ngrid)])
    r = np.linalg.norm(P @ flow(ts), axis=0) ** 2 / base
    idx = np.nonzero(r <= delta)[0]
    if len(idx) == 0:
        return np.inf
    j = idx[0]
    if j == 0:
        return 0.0
    f = lambda t: np.linalg.norm(P @ flow(t)[:, 0]) ** 2 / base - delta
    return brentq(f, ts[j - 1], ts[j], xtol=1e-14 * ts[j], rtol=1e-12)


def time_interval(delta, eps, lam, Lam):
    """Corollary 2: (lower, upper) for T_l(delta); upper is inf if eps >= sqrt(delta)."""
    sd = np.sqrt(delta)
    lower = 0.0 if sd + eps >= 1 else np.log(1 / (sd + eps)) / Lam
    upper = np.inf if eps >= sd else np.log(1 / (sd - eps)) / lam
    return lower, upper


def davis_kahan_check(A, P, lam, Lam, eta):
    """Davis-Kahan sin-theta, residual form: for every gamma > 0, the part of
    ran P lying in A's eigenvectors at distance >= gamma from [lam, Lam] has
    norm <= eta / gamma. Returns the largest ratio (observed / bound) over the
    gammas given by A's own eigenvalue distances (<= 1 if the theorem holds)."""
    w, V = np.linalg.eigh(A)
    dist = np.maximum(0.0, np.maximum(lam - w, w - Lam))
    worst = 0.0
    for g in np.unique(dist[dist > 1e-12]):
        W = V[:, dist >= g]
        obs = np.linalg.norm(W.T @ P, 2)
        if eta > 0:
            worst = max(worst, obs / (eta / g))
        elif obs > 1e-9:
            worst = np.inf
    return worst


# ---------------------------------------------------------------- moving operator: a small ReLU net

class TwoLayerReLU:
    """f(x) = a . relu(W x / sqrt(d)) / sqrt(m), scalar output, zero at init by
    antisymmetric pairing (units j and j + m/2 share w, opposite a)."""

    def __init__(self, d, m, scale, rng):
        half = m // 2
        W = rng.standard_normal((half, d)) * scale
        a = rng.standard_normal(half) * scale
        self.W = np.vstack([W, W])
        self.a = np.concatenate([a, -a])
        self.m, self.d = m, d

    def forward(self, X):
        Z = X @ self.W.T / np.sqrt(self.d)
        return np.maximum(Z, 0) @ self.a / np.sqrt(self.m)

    def jacobian(self, X):
        """n x (m + m d): derivative of outputs in (a, W)."""
        Z = X @ self.W.T / np.sqrt(self.d)
        Ja = np.maximum(Z, 0) / np.sqrt(self.m)
        mask = (Z > 0).astype(float) * self.a[None, :] / np.sqrt(self.m)
        JW = (mask[:, :, None] * X[:, None, :] / np.sqrt(self.d)).reshape(X.shape[0], -1)
        return np.hstack([Ja, JW])

    def step(self, X, y, h):
        n = X.shape[0]
        e = self.forward(X) - y
        J = self.jacobian(X)
        grad = J.T @ e / n
        self.a -= h * grad[: self.m]
        self.W -= h * grad[self.m:].reshape(self.m, self.d)
        return e, J
