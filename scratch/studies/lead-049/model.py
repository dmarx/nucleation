"""Symmetric resource competition with bounded, gradient-driven niche adaptation.

Model class (LEAD-049). Operators i = 1..k have abundance (participation
intensity) n_i >= 0 and a scalar niche trait theta_i in the box [lo, hi].
A trait fixes a nonnegative niche (resource-use) vector u(theta) in R^m.
Supply b in R^m, maintenance cost c_i > 0.

    R      = b - sum_j n_j u(theta_j)                    (residual supply)
    dn_i   = n_i (u_i . R - c_i)                         (Lotka-Volterra, A = U^T U)
    dth_i  = eps * kappa_i(n) * Proj[ u'(theta_i) . R ]  (selection gradient of a
                                                          rare mutant, projected
                                                          onto the box)

with kappa_i = n_i (canonical equation of adaptive dynamics: mutation supply
proportional to abundance) or kappa_i = 1. Both are gradient flows of

    L(n, theta) = 1/2 |b - U(theta) n|^2 + c . n

in the metric D^{-1}, D = diag(n_1..n_k, eps kappa_1/n_1 .. eps kappa_k/n_k):
  dn_i = -n_i dL/dn_i  and  dth_i = -(eps kappa_i / n_i) dL/dth_i.
"""
import itertools

import numpy as np


# ---------------------------------------------------------------- niche maps

class GaussianNiche:
    """MacArthur-Levins niche: resources at positions x_alpha on [0, 1],
    u_alpha(theta) = h exp(-(x_alpha - theta)^2 / (2 w^2)). Trait box [0, 1]."""

    lo, hi = 0.0, 1.0

    def __init__(self, m=12, w=0.12, h=1.0):
        self.x = np.linspace(0.0, 1.0, m)
        self.w = w
        self.h = h
        self.m = m

    def u(self, th):
        th = np.atleast_1d(th)
        return self.h * np.exp(-(self.x[:, None] - th[None, :]) ** 2 / (2 * self.w ** 2))

    def du(self, th):
        th = np.atleast_1d(th)
        return self.u(th) * (self.x[:, None] - th[None, :]) / self.w ** 2


class TradeoffNiche:
    """Two resources. u(theta) = (a(theta), a(1 - theta)), theta in [0, 1],
    a(0) = 0, a(1) = 1. theta = 1 is the specialist on resource 1, theta = 0
    on resource 2, theta = 1/2 the symmetric generalist.

    a(t) = t + t(1 - t)(alpha + beta t) + gamma t^2 (1 - t)^2, so
    a'(0) = 1 + alpha, a'(1) = 1 - alpha - beta,
    a(1/2) = 1/2 + (alpha + beta/2)/4 + gamma/16."""

    lo, hi = 0.0, 1.0
    m = 2

    def __init__(self, alpha=0.0, beta=0.0, gamma=0.0):
        self.alpha, self.beta, self.gamma = alpha, beta, gamma

    def a(self, t):
        al, be, ga = self.alpha, self.beta, self.gamma
        return t + t * (1 - t) * (al + be * t) + ga * t ** 2 * (1 - t) ** 2

    def da(self, t):
        al, be, ga = self.alpha, self.beta, self.gamma
        # d/dt [t(1-t)(al + be t)] = (1 - 2t)(al + be t) + be t (1 - t)
        # d/dt [t^2 (1-t)^2]       = 2t(1-t)(1-2t)
        return 1 + (1 - 2 * t) * (al + be * t) + be * t * (1 - t) + ga * 2 * t * (1 - t) * (1 - 2 * t)

    def u(self, th):
        th = np.atleast_1d(th)
        return np.vstack([self.a(th), self.a(1 - th)])

    def du(self, th):
        th = np.atleast_1d(th)
        return np.vstack([self.da(th), -self.da(1 - th)])


# ---------------------------------------------------------------- potential

def residual(niche, b, n, th):
    return b - niche.u(th) @ n


def potential(niche, b, c, n, th):
    R = residual(niche, b, n, th)
    return 0.5 * R @ R + np.dot(c, n)


def grad(niche, b, c, n, th):
    """(dL/dn, dL/dtheta)."""
    R = residual(niche, b, n, th)
    U, J = niche.u(th), niche.du(th)
    return -(U.T @ R) + c, -n * (J.T @ R)


def growth(niche, b, c, n, th):
    """Per-capita growth f_i = u_i . R - c_i = -dL/dn_i."""
    return -grad(niche, b, c, n, th)[0]


def selection_gradient(niche, b, n, th):
    """Rare-mutant selection gradient u'(theta_i) . R."""
    return niche.du(th).T @ residual(niche, b, n, th)


def active_bounds(niche, th, sg, tol=1e-9):
    """Mask of trait coordinates held at a bound with the gradient pointing out."""
    at_lo = (th <= niche.lo + tol) & (sg < 0)
    at_hi = (th >= niche.hi - tol) & (sg > 0)
    return at_lo | at_hi


# ---------------------------------------------------------------- dynamics

def vector_field(niche, b, c, n, th, eps, kappa="n", alive=None):
    f = growth(niche, b, c, n, th)
    sg = selection_gradient(niche, b, n, th)
    kap = n.copy() if kappa == "n" else np.ones_like(n)
    dth = eps * kap * sg
    dth[active_bounds(niche, th, sg)] = 0.0
    if alive is not None:
        dth[~alive] = 0.0
    return f, dth  # f is d log n / dt


def simulate(niche, b, c, n0, th0, eps, T, dt=0.01, kappa="n", alive=None,
             floor=1e-300, record_every=None):
    """RK4 in (log n, theta) with the trait clipped to its box after each step.
    alive: mask; operators not alive are held at n = 0 (removed)."""
    n0 = np.asarray(n0, float)
    alive = np.ones(len(n0), bool) if alive is None else np.asarray(alive, bool)
    logn = np.where(alive, np.log(np.maximum(n0, floor)), -np.inf)
    th = np.asarray(th0, float).copy()
    steps = int(round(T / dt))
    trace = []

    def F(lg, t_):
        n = np.where(alive, np.exp(lg), 0.0)
        f, dth = vector_field(niche, b, c, n, t_, eps, kappa, alive)
        return np.where(alive, f, 0.0), dth

    for s in range(steps):
        k1 = F(logn, th)
        k2 = F(logn + 0.5 * dt * k1[0], np.clip(th + 0.5 * dt * k1[1], niche.lo, niche.hi))
        k3 = F(logn + 0.5 * dt * k2[0], np.clip(th + 0.5 * dt * k2[1], niche.lo, niche.hi))
        k4 = F(logn + dt * k3[0], np.clip(th + dt * k3[1], niche.lo, niche.hi))
        dl = (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        logn = np.where(alive, logn + dt * dl, -np.inf)
        th = np.clip(th + dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6, niche.lo, niche.hi)
        if record_every and s % record_every == 0:
            trace.append((s * dt, np.where(alive, np.exp(logn), 0.0).copy(), th.copy()))
    n = np.where(alive, np.exp(logn), 0.0)
    return (n, th, trace) if record_every else (n, th)


# ---------------------------------------------------------------- theorem A

def free_coordinates(niche, b, n, th, tol=1e-9):
    """Indices into z = (n, theta) of the coordinates the linearization acts on:
    all n_i (assumed > 0) and the theta_i not held at a bound."""
    sg = selection_gradient(niche, b, n, th)
    held = active_bounds(niche, th, sg, tol)
    k = len(n)
    return np.concatenate([np.arange(k), k + np.where(~held)[0]])


def hessian(niche, b, c, n, th, h=1e-6):
    """Hessian of L in z = (n, theta), central differences of the exact gradient."""
    k = len(n)
    z = np.concatenate([n, th])

    def g(zz):
        gn, gt = grad(niche, b, c, zz[:k], zz[k:])
        return np.concatenate([gn, gt])

    H = np.zeros((2 * k, 2 * k))
    for j in range(2 * k):
        e = np.zeros(2 * k)
        e[j] = h
        H[:, j] = (g(z + e) - g(z - e)) / (2 * h)
    return 0.5 * (H + H.T)


def metric_diag(n, eps, kappa="n"):
    kap = n if kappa == "n" else np.ones_like(n)
    return np.concatenate([n, eps * kap / n])


def jacobian_free(niche, b, c, n, th, eps, kappa="n", h=1e-7):
    """Numerical Jacobian of the (n, theta) vector field on the free coordinates."""
    k = len(n)
    idx = free_coordinates(niche, b, n, th)
    z0 = np.concatenate([n, th])

    def V(z):
        nn, tt = z[:k], z[k:]
        f, dth = vector_field(niche, b, c, nn, tt, eps, kappa)
        return np.concatenate([nn * f, dth])

    Jm = np.zeros((len(idx), len(idx)))
    for col, j in enumerate(idx):
        e = np.zeros(2 * k)
        e[j] = h
        Jm[:, col] = (V(z0 + e)[idx] - V(z0 - e)[idx]) / (2 * h)
    return Jm


def theorem_A_check(niche, b, c, n, th, eps, kappa="n"):
    """Return (sufficient condition holds, min eig of free Hessian,
    max real part of numerical Jacobian, max real part of -D H prediction,
    strict-complementarity margin)."""
    k = len(n)
    idx = free_coordinates(niche, b, n, th)
    H = hessian(niche, b, c, n, th)[np.ix_(idx, idx)]
    D = metric_diag(n, eps, kappa)[idx]
    pred = np.linalg.eigvals(-(D[:, None] * H))
    Jm = jacobian_free(niche, b, c, n, th, eps, kappa)
    sg = selection_gradient(niche, b, n, th)
    held = active_bounds(niche, th, sg)
    margin = np.min(np.abs(sg[held])) if held.any() else np.inf
    hmin = np.min(np.linalg.eigvalsh(H))
    return dict(holds=bool(hmin > 0 and n.min() > 0), hess_min=float(hmin),
                jac_max_re=float(np.max(np.linalg.eigvals(Jm).real)),
                pred_max_re=float(np.max(pred.real)), margin=float(margin),
                n_free_traits=int(len(idx) - k))


# ---------------------------------------------------------------- theorem B

def lv_equilibrium(A, r, allowed=None, tol=1e-10):
    """Unique KKT point of min 1/2 n^T A n - r^T n over n >= 0 (A positive
    definite), with n_j = 0 forced off `allowed`. Exact, by support enumeration."""
    k = len(r)
    allowed = np.ones(k, bool) if allowed is None else np.asarray(allowed, bool)
    pool = np.where(allowed)[0]
    for size in range(len(pool), -1, -1):
        for S in itertools.combinations(pool, size):
            S = list(S)
            n = np.zeros(k)
            if S:
                n[S] = np.linalg.solve(A[np.ix_(S, S)], r[S])
                if n[S].min() <= tol:
                    continue
            g = A @ n - r
            out = [j for j in pool if j not in S]
            if all(g[j] >= -tol for j in out):
                return n
    raise RuntimeError("no KKT point found")


def invasion_frozen(A, r, nstar, i):
    """Recovery growth of i into the -i community with traits frozen, and
    theorem B's bound n_i* / (A^{-1})_ii, and whether secondary extinctions occurred."""
    k = len(r)
    allowed = np.ones(k, bool)
    allowed[i] = False
    nt = lv_equilibrium(A, r, allowed)
    lam = r[i] - A[i] @ nt
    bound = nstar[i] / np.linalg.inv(A)[i, i]
    others = [j for j in range(k) if j != i]
    secondary = bool(np.any(nt[others] <= 1e-12))
    return float(lam), float(bound), secondary, nt
