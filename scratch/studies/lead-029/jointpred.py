"""LEAD-029: a joint prediction of the coupled meaning-influence model, and
A55 section 7's comparison of one model against separate models.

Generator (an instance of CLAIM-297's equations, K operators, C contexts,
two interpretations so that the meaning state x is a scalar in [0, 1]):

    governance:  u <- u + Delta * e_t                      (conferral E_t)
    meaning:     x_{t+1} = (1 - rho) x_t + rho * sum_i w_i a_i(q_t),
                 w = softmax(u)                            (sum_i w_i P_i(q)^T x)
    influence:   u <- (1 - kappa) u + eta * (s - mean(s)),
                 s_i = -(a_i(q_t) - x_{t+1})^2              (scored against the
                                                            dominant reading)
    read-out:    y_t = x_t + noise

P_i(q) = (1 - rho) I + rho 1 [a_i(q), 1 - a_i(q)] is a stochastic matrix, so
the meaning step is exactly sum_i w_i P_i(q)^T x.  `score="abs"` uses
s_i = -|a_i - x_{t+1}| instead (a misspecification check).

Models fitted to the same training data (least squares on y):

  joint  : the generator's family (a, rho, eta, kappa, Delta), 16 parameters.
  cut    : the same, with the loop cut (eta = 0): governance moves authority,
           interpretation never does.  15 parameters.
  cutflex: cut with a decay and an intervention size per operator, 19.
  additive: an interpretation model (context -> level, AR(1)) plus a
           governance model (an intervention's effect in response units, by
           operator and context, decaying geometrically), summed.  18.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import minimize
from scipy.special import expit

K, C = 3, 4  # operators, contexts


def sigmoid(z):
    return expit(z)


def logit(p):
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


def softplus(z):
    return np.logaddexp(0.0, z)


def inv_softplus(y):
    return np.log(np.expm1(y))


# ---------------------------------------------------------------- simulators

def simulate_operator(a, rho, eta, kappa, delta, ctx, E, score="sq"):
    """Run the coupled model.  a: (K, C); kappa, delta scalars or (K,);
    ctx: (N, T) ints; E: (N, T, K) in {-1, 0, 1}.  Returns x: (N, T), the
    meaning state after each step (x_1 .. x_T); x_0 = 0.5, u_0 = 0."""
    N, T = ctx.shape
    x = np.full(N, 0.5)
    u = np.zeros((N, K))
    out = np.empty((N, T))
    kappa = np.broadcast_to(np.asarray(kappa, float), (K,))
    delta = np.broadcast_to(np.asarray(delta, float), (K,))
    for t in range(T):
        u = u + delta * E[:, t, :]
        w = np.exp(u - u.max(axis=1, keepdims=True))
        w /= w.sum(axis=1, keepdims=True)
        at = a[:, ctx[:, t]].T  # (N, K)
        x = (1 - rho) * x + rho * (w * at).sum(axis=1)
        if eta != 0.0:
            d = at - x[:, None]
            s = -(d * d) if score == "sq" else -np.abs(d)
            s = s - s.mean(axis=1, keepdims=True)
            u = (1 - kappa) * u + eta * s
        else:
            u = (1 - kappa) * u
        out[:, t] = x
    return out


def simulate_additive(m, rho, phi, beta, ctx, E):
    """Separate models summed: interpretation level m[q] approached at rate
    rho; governance offset g decaying at phi, kicked by beta[j, q] when
    operator j is intervened on (sign of the intervention) under context q."""
    N, T = ctx.shape
    yI = np.full(N, 0.5)
    g = np.zeros(N)
    out = np.empty((N, T))
    for t in range(T):
        q = ctx[:, t]
        g = phi * g + (E[:, t, :] * beta[:, q].T).sum(axis=1)
        yI = yI + rho * (m[q] - yI)
        out[:, t] = yI + g
    return out


# ---------------------------------------------------------------- models

class Model:
    name = ""
    n_params = 0

    def unpack(self, th):
        raise NotImplementedError

    def predict(self, th, ctx, E):
        raise NotImplementedError

    def random_init(self, rng):
        raise NotImplementedError


class Joint(Model):
    name, n_params = "joint", K * C + 4

    def __init__(self, score="sq"):
        self.score = score

    def unpack(self, th):
        a = sigmoid(th[:K * C]).reshape(K, C)
        rho, eta, kappa, delta = (sigmoid(th[12]), softplus(th[13]),
                                  sigmoid(th[14]), softplus(th[15]))
        return a, rho, eta, kappa, delta

    def predict(self, th, ctx, E):
        a, rho, eta, kappa, delta = self.unpack(th)
        return simulate_operator(a, rho, eta, kappa, delta, ctx, E, self.score)

    def random_init(self, rng):
        return np.concatenate([rng.normal(0, 1, K * C),
                               [logit(rng.uniform(0.1, 0.6)),
                                inv_softplus(rng.uniform(0.05, 4.0)),
                                logit(rng.uniform(0.03, 0.4)),
                                inv_softplus(rng.uniform(0.3, 3.0))]])


class Cut(Model):
    name, n_params = "cut", K * C + 3

    def unpack(self, th):
        a = sigmoid(th[:K * C]).reshape(K, C)
        return a, sigmoid(th[12]), sigmoid(th[13]), softplus(th[14])

    def predict(self, th, ctx, E):
        a, rho, kappa, delta = self.unpack(th)
        return simulate_operator(a, rho, 0.0, kappa, delta, ctx, E)

    def random_init(self, rng):
        return np.concatenate([rng.normal(0, 1, K * C),
                               [logit(rng.uniform(0.1, 0.6)),
                                logit(rng.uniform(0.03, 0.4)),
                                inv_softplus(rng.uniform(0.3, 3.0))]])


class CutFlex(Model):
    name, n_params = "cutflex", K * C + 1 + 2 * K

    def unpack(self, th):
        a = sigmoid(th[:K * C]).reshape(K, C)
        rho = sigmoid(th[12])
        kappa = sigmoid(th[13:13 + K])
        delta = softplus(th[13 + K:13 + 2 * K])
        return a, rho, kappa, delta

    def predict(self, th, ctx, E):
        a, rho, kappa, delta = self.unpack(th)
        return simulate_operator(a, rho, 0.0, kappa, delta, ctx, E)

    def random_init(self, rng):
        return np.concatenate([rng.normal(0, 1, K * C),
                               [logit(rng.uniform(0.1, 0.6))],
                               logit(rng.uniform(0.03, 0.4, K)),
                               inv_softplus(rng.uniform(0.3, 3.0, K))])


class Additive(Model):
    name, n_params = "additive", C + 2 + K * C

    def unpack(self, th):
        m = sigmoid(th[:C])
        rho, phi = sigmoid(th[C]), sigmoid(th[C + 1])
        beta = th[C + 2:].reshape(K, C)
        return m, rho, phi, beta

    def predict(self, th, ctx, E):
        return simulate_additive(*self.unpack(th), ctx, E)

    def random_init(self, rng):
        return np.concatenate([rng.normal(0, 1, C),
                               [logit(rng.uniform(0.1, 0.6)),
                                logit(rng.uniform(0.3, 0.95))],
                               rng.normal(0, 0.1, K * C)])


def fit(model, ctx, E, y, rng, restarts=6, maxiter=300, extra_starts=(),
        schedule=(6, 12, 24)):
    """Least squares by L-BFGS-B.  Each start is fitted on growing prefixes of
    the episodes (continuation over `schedule`; the last entry must be the
    full length), random starts first, then any `extra_starts` (fitted on
    the full length only).  Returns the best parameter vector, its sum of
    squared errors, and the best over the random starts alone."""
    def loss_T(T):
        def loss(th):
            r = model.predict(th, ctx[:, :T], E[:, :T]) - y[:, :T]
            return float((r * r).sum())
        return loss

    full = loss_T(ctx.shape[1])
    best_random = None
    for _ in range(restarts):
        th = model.random_init(rng)
        for T in schedule:
            th = minimize(loss_T(T), th, method="L-BFGS-B",
                          options={"maxiter": maxiter}).x
        f = full(th)
        if best_random is None or f < best_random[1]:
            best_random = (th, f)
    best = best_random
    for th0 in extra_starts:
        res = minimize(full, np.asarray(th0, float), method="L-BFGS-B",
                       options={"maxiter": maxiter})
        if best is None or res.fun < best[1]:
            best = (res.x, res.fun)
    return best[0], best[1], best_random


def aic_bic(sse, n_obs, k):
    """Gaussian AIC and BIC with the noise variance profiled out."""
    ll = -0.5 * n_obs * (np.log(2 * np.pi * sse / n_obs) + 1)
    return 2 * k - 2 * ll, k * np.log(n_obs) - 2 * ll


# ---------------------------------------------------------------- derivation

def linearized_jacobian(rho, eta, kappa, da):
    """Two operators, squared score, linearized at the symmetric allocation
    (v = u1 - u2 = 0, x at its fixed point) under one context with dissent
    da = a1 - a2.  State (dx, dv)."""
    alpha = 1 - rho
    beta = rho * da / 4
    gamma = 2 * eta * da * (1 - rho)
    dlt = (1 - kappa) + eta * rho * da * da / 2
    return np.array([[alpha, beta], [gamma, dlt]])


def unstable(eta, kappa, da):
    """The derived condition: the symmetric allocation is unstable under a
    context iff eta * da^2 / 2 > kappa (det(I - J) = rho (kappa - eta da^2/2))."""
    return eta * da * da / 2 > kappa


def simulate_two(a1, a2, rho, eta, kappa, v0, T):
    """Two operators under one fixed context; returns v_t = u1 - u2."""
    a = np.array([[a1], [a2]])
    x = 0.5 * (a1 + a2)
    u = np.array([v0 / 2, -v0 / 2])
    vs = []
    for _ in range(T):
        w = np.exp(u - u.max()); w /= w.sum()
        x = (1 - rho) * x + rho * (w * a[:, 0]).sum()
        s = -(a[:, 0] - x) ** 2
        u = (1 - kappa) * u + eta * (s - s.mean())
        vs.append(u[0] - u[1])
    return np.array(vs)


# ---------------------------------------------------------------- data

def true_operators(rng, min_spread=0.4):
    """Context 0: all operators agree (a = 0.5).  Contexts 1..C-1: readings
    drawn from U(0.1, 0.9), redrawn until they spread by min_spread."""
    a = np.empty((K, C))
    a[:, 0] = 0.5
    for c in range(1, C):
        while True:
            col = rng.uniform(0.1, 0.9, K)
            if col.max() - col.min() >= min_spread:
                break
        a[:, c] = col
    return a


def piecewise_contexts(rng, T, lo=6, hi=12):
    seq = np.empty(T, int)
    t = 0
    q = rng.integers(C)
    while t < T:
        L = rng.integers(lo, hi + 1)
        seq[t:t + L] = q
        t += L
        q = (q + rng.integers(1, C)) % C
    return seq


HELDOUT = {(0, 1), (1, 2), (2, 3)}  # (operator, context) never intervened on in D2 training


def training_data(rng, design, T=24, n=240):
    ctx = np.empty((n, T), int)
    E = np.zeros((n, T, K))
    for k in range(n):
        if design == "D1":
            if k < n // 2:  # context changes only
                ctx[k] = piecewise_contexts(rng, T)
            else:          # governance only, context held fixed
                ctx[k] = rng.integers(C)
                for _ in range(rng.integers(1, 4)):
                    E[k, rng.integers(T - 2), rng.integers(K)] = rng.choice([-1, 1])
        elif design == "D2":  # compositions, with HELDOUT (j, c) never intervened
            ctx[k] = piecewise_contexts(rng, T)
            placed = 0
            while placed < rng.integers(1, 4):
                t, j = rng.integers(T - 2), rng.integers(K)
                if (j, ctx[k, t]) in HELDOUT:
                    continue
                E[k, t, j] = rng.choice([-1, 1])
                placed += 1
        else:
            raise ValueError(design)
    return ctx, E


def test_episodes(T=24, t_int=4, t_switch=12):
    """Every (operator j, sign, context c at the intervention, later context
    c' != c), each with its untreated twin.  Returns ctx, E, labels; rows
    2i and 2i+1 are treated and untreated."""
    rows, labels = [], []
    for j in range(K):
        for sign in (-1, 1):
            for c in range(C):
                for c2 in range(C):
                    if c2 == c:
                        continue
                    q = np.full(T, c); q[t_switch:] = c2
                    e = np.zeros((T, K)); e[t_int, j] = sign
                    rows.append((q, e)); rows.append((q, np.zeros((T, K))))
                    labels.append((j, sign, c, c2))
    ctx = np.array([r[0] for r in rows])
    E = np.array([r[1] for r in rows])
    return ctx, E, labels
