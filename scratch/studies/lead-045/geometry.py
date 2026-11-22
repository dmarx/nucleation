"""LEAD-045, part 1: the Geometry model of independent skills (Liu, Liu,
Michaud, Gore and Tegmark 2025; THEORY-253) under gradient descent, sign
descent and Adam, set against the mean-field ODE derived in the README.

Loss: l(theta) = sum_i p_i (1 - s_i)^2, s_i = theta . t_i, theta_0 = 0,
t_i orthonormal and random in R^d. Residual u_i = 1 - s_i.

Derived (README, "Derivation"): for random t_i and large d, sign descent
with step eta follows, per step,
    du_i/dt = -c p_i u_i / ||p o u||_2,     c = eta * sqrt(2 d / pi).
That is gradient flow on the same loss with its clock divided by the
gradient norm: the path in u-space is gradient descent's, only the timing
differs.
"""
import numpy as np
from scipy.integrate import quad


def task_vectors(n_task, d, seed=0):
    rng = np.random.default_rng(seed)
    q, _ = np.linalg.qr(rng.standard_normal((d, n_task)))
    return q.T  # (n_task, d), orthonormal rows


def simulate(p, T, optimizer, eta, steps, record_every=1,
             betas=(0.9, 0.999), adam_eps=1e-8):
    """Full-batch deterministic training from theta = 0. Returns
    (step_axis, s) with s of shape (n_records, n_task)."""
    p = np.asarray(p, float)
    d = T.shape[1]
    theta = np.zeros(d)
    m = np.zeros(d)
    v = np.zeros(d)
    out_t, out_s = [], []
    for k in range(steps + 1):
        s = T @ theta
        if k % record_every == 0:
            out_t.append(k)
            out_s.append(s.copy())
        if k == steps:
            break
        g = -2.0 * T.T @ (p * (1.0 - s))
        if optimizer == "gd":
            theta -= eta * g
        elif optimizer == "sign":
            theta -= eta * np.sign(g)
        elif optimizer == "adam":
            b1, b2 = betas
            m = b1 * m + (1 - b1) * g
            v = b2 * v + (1 - b2) * g * g
            mh = m / (1 - b1 ** (k + 1))
            vh = v / (1 - b2 ** (k + 1))
            theta -= eta * mh / (np.sqrt(vh) + adam_eps)
        else:
            raise ValueError(optimizer)
    return np.array(out_t), np.array(out_s)


def first_crossing(t, s, level):
    """First time each column of s reaches `level`, linearly interpolated;
    nan if never."""
    s = np.atleast_2d(np.asarray(s, float).T).T
    out = np.full(s.shape[1], np.nan)
    for j in range(s.shape[1]):
        idx = np.nonzero(s[:, j] >= level)[0]
        if len(idx) == 0:
            continue
        i = idx[0]
        if i == 0:
            out[j] = t[0]
        else:
            a, b = s[i - 1, j], s[i, j]
            out[j] = t[i - 1] + (level - a) / (b - a) * (t[i] - t[i - 1])
    return out


# ---------- the derived ODE and its closed forms ----------

def ode_clock(p, eps, norm="l2"):
    """Times, in units of 1/c, at which each skill reaches s = 1 - eps under
    du_i/dt = -c p_i u_i / N(p o u), with N the l2 norm (derived) or the l1
    norm (the Resource model of the paper with N0 = 0). Both follow the
    gradient-flow path u_i = exp(-p_i tau), so
    t(tau) = int_0^tau N(p_i exp(-p_i tau')) dtau'."""
    p = np.asarray(p, float)

    def integrand(tau):
        w = p * np.exp(-p * tau)
        return np.sqrt(np.sum(w * w)) if norm == "l2" else np.sum(w)

    taus = np.log(1.0 / eps) / p
    # piecewise, on a grid fine at every scale 1/p_i, so quad sees each term
    lo = 0.01 / p.max()
    knots = np.concatenate([[0.0], np.geomspace(lo, taus.max(), 400)])

    def clock(tau):
        ks = np.concatenate([knots[knots < tau], [tau]])
        return sum(quad(integrand, a, b)[0] for a, b in zip(ks[:-1], ks[1:]))

    return np.array([clock(tau) for tau in taus])


def ode_curves(p, t_grid, norm="l2", n_tau=200001):
    """s_i(t) under the same ODE, on t_grid (units of 1/c)."""
    p = np.asarray(p, float)
    tau = np.linspace(0, 40.0 / p.min(), n_tau)
    w = p[None, :] * np.exp(-p[None, :] * tau[:, None])
    N = np.sqrt((w * w).sum(1)) if norm == "l2" else w.sum(1)
    clock = np.concatenate([[0], np.cumsum(0.5 * (N[1:] + N[:-1]) * np.diff(tau))])
    tau_of_t = np.interp(t_grid, clock, tau)
    return 1.0 - np.exp(-p[None, :] * tau_of_t[:, None])


def domino_limit_ratio(n, eps):
    """t_n / t_1 in the limit p_1 >> p_2 >> ... : (n - eps) / (1 - eps)."""
    return (n - eps) / (1.0 - eps)


def gd_times(p, eps, eta=1.0):
    """Gradient descent in continuous time with step eta:
    u_i = exp(-2 eta p_i t)."""
    return np.log(1.0 / eps) / (2.0 * eta * np.asarray(p, float))


def acceleration_sign(p, u, j):
    """Sign of d/dt log(ds_j/dt) under the derived ODE,
    sign( sum_i p_i^2 u_i^2 (p_i - p_j) ): positive while stronger skills
    remain unlearned (skill j accelerating), negative for the strongest."""
    p = np.asarray(p, float)
    u = np.asarray(u, float)
    return np.sign(np.sum(p * p * u * u * (p - p[j])))


# ---------- the rotated quadratic of the paper's Fig. 12 ----------

def hadamard4():
    h2 = np.array([[1, 1], [1, -1]], float)
    return np.kron(h2, h2) / 2.0


def rotated_quadratic(R, lam, optimizer, eta, steps):
    """l = sum_i lam_i x_i^2, x = R theta, x(0) = 1. Returns x per step."""
    lam = np.asarray(lam, float)
    theta = R.T @ np.ones(len(lam))
    xs = []
    for _ in range(steps + 1):
        x = R @ theta
        xs.append(x.copy())
        g = R.T @ (2 * lam * x)
        theta -= eta * (g if optimizer == "gd" else np.sign(g))
    return np.array(xs)


def hadamard_phase1_end(lam):
    """Exact for R = H4 (|R_ik| = 1/2) and x > 0: while
    lam_1 x_1 > sum_{j>1} lam_j x_j every coordinate of the gradient has the
    sign of row 1, so x_1 falls by 2 eta per step and x_2..x_4 do not move.
    Returns the x_1 at which that regime ends, x(0) = 1."""
    lam = np.asarray(lam, float)
    return np.sum(lam[1:]) / lam[0]
