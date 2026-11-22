"""LEAD-081: CASE-099 extended with declared demands and a feasible-update oracle.

The organization has a state theta in R^p and k components, one per declared
demand. Demand i is met when L_i(theta) = 1/2 (theta - c_i)^T H (theta - c_i)
<= tau_i. Each step it declares the local requirement eps_i + g_i^T d <= 0 of an
update d (CLAIM-365's form), with g_i = grad L_i and

    eps_i = min(L_i - tau_i, eta)

so an unmet demand asks for progress eta (or to be met, if closer) and a met
demand asks only not to be broken (eps_i <= 0 is its slack).

Admissible updates: U_r = {d : ||d||_2 <= r}.
Oracle: Phi_r = min_{d in U_r} max_i (eps_i + g_i^T d), with its dual
    Phi_r = max_{lambda in simplex} lambda.eps - r ||G^T lambda||_2.

Governance: influence weights w on the simplex. The actual update is the
weighted-gradient step (A34's rule with unit curvature, clipped to U_r):
    d(w) = -g_w * min(1, r/||g_w||),  g_w = sum_j w_j g_j.
This map (the "search") and the gradients (the "information") are the same
under every allocation rule; only the rule that updates w differs.

Allocation rules (conferral, with memory delta and sharpness gamma):
    w <- delta w + (1 - delta) softmax(gamma * s)
  'A'      : s_j = cos(-g_j, d_actual), agreement of component j's own
             proposal with the update actually made (scored through the
             interpretation whose authority is being evaluated; CASE-092
             Regime A, the gamma arrow of CASE-099).
  'B'      : s_j = (eps_j + g_j^T d_actual) / eta, demand j's own residual
             under the update made: evidence of how demand j fared that does
             not pass through agreement with the update (CASE-092 Regime B).
  'fixed'  : w never changes (a fixed weighting rule).
  'oracle' : w = the allocation that minimizes the worst residual of d(w)
             over the simplex (an allocation oracle: the best the same search
             and information can do by changing only the allocation).
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import minimize


# ---------------------------------------------------------------- oracle
def worst_residual(eps, G, d):
    return float(np.max(eps + G @ d))


def oracle_primal(eps, G, r, d0=None):
    """min_{||d||<=r} max_i eps_i + g_i.d, by SLSQP on (d, t). Returns (Phi, d*)."""
    k, p = G.shape
    if d0 is None:
        d0 = np.zeros(p)
    x0 = np.concatenate([d0, [worst_residual(eps, G, d0)]])
    cons = [
        {"type": "ineq", "fun": lambda x: x[-1] - eps - G @ x[:-1],
         "jac": lambda x: np.hstack([-G, np.ones((k, 1))])},
        {"type": "ineq", "fun": lambda x: r * r - x[:-1] @ x[:-1],
         "jac": lambda x: np.concatenate([-2 * x[:-1], [0.0]])},
    ]
    e_last = np.eye(p + 1)[-1]
    res = minimize(lambda x: x[-1], x0, jac=lambda x: e_last,
                   constraints=cons, method="SLSQP",
                   options={"ftol": 1e-12, "maxiter": 200})
    d = res.x[:-1]
    n = np.linalg.norm(d)
    if n > r:
        d = d * (r / n)
    # never report worse than the warm start (also admissible)
    if worst_residual(eps, G, d0) < worst_residual(eps, G, d):
        d = d0
    return worst_residual(eps, G, d), d


def oracle_dual(eps, G, r):
    """max_{lambda in simplex} lambda.eps - r||G^T lambda||. Returns (value, lambda)."""
    k = len(eps)
    best = (-np.inf, None)
    starts = [np.full(k, 1.0 / k)] + [np.eye(k)[i] * 0.9 + 0.1 / k for i in range(k)]

    def f(l):
        return -(l @ eps - r * np.linalg.norm(G.T @ l))

    def jac(l):
        v = G.T @ l
        nv = np.linalg.norm(v)
        gv = (G @ v) / nv if nv > 1e-15 else np.zeros(k)
        return -(eps - r * gv)

    cons = [{"type": "eq", "fun": lambda l: l.sum() - 1, "jac": lambda l: np.ones(k)}]
    for l0 in starts:
        res = minimize(f, l0, jac=jac, method="SLSQP", bounds=[(0, 1)] * k,
                       constraints=cons, options={"ftol": 1e-12, "maxiter": 200})
        l = np.clip(res.x, 0, None)
        l = l / l.sum()
        val = l @ eps - r * np.linalg.norm(G.T @ l)
        if val > best[0]:
            best = (val, l)
    return best


def oracle_exact2d(eps, G, r):
    """Exact Phi_r for p = 2 by enumerating the vertices of the arrangement.

    m(d) is convex piecewise-affine, so its minimum over the disk is attained
    at a point where it is not locally affine-in-a-descent-direction: a point
    inside the disk where three pieces are equal, a point on the circle where
    two pieces are equal, or the minimizer of one piece on the circle (d = 0
    is added for the degenerate g = 0 case). Returns (Phi, d*).
    """
    k = len(eps)
    cand = [np.zeros(2)]
    for i in range(k):
        n = np.linalg.norm(G[i])
        if n > 0:
            cand.append(-r * G[i] / n)
    for i in range(k):
        for j in range(i + 1, k):
            a = G[i] - G[j]; b = eps[j] - eps[i]      # line a.d = b
            na = a @ a
            if na < 1e-24:
                continue
            p0 = a * b / na; dist2 = p0 @ p0
            if dist2 <= r * r:
                t = np.array([-a[1], a[0]]) / np.sqrt(na)
                h = np.sqrt(r * r - dist2)
                cand += [p0 + h * t, p0 - h * t]
            for l in range(j + 1, k):
                A = np.array([G[i] - G[j], G[i] - G[l]])
                if abs(np.linalg.det(A)) < 1e-14:
                    continue
                d = np.linalg.solve(A, [eps[j] - eps[i], eps[l] - eps[i]])
                if d @ d <= r * r:
                    cand.append(d)
    C = np.array(cand)
    vals = np.max(eps[None, :] + C @ G.T, axis=1)
    i = int(np.argmin(vals))
    return float(vals[i]), C[i]


_GRID = {}


def simplex_grid(k, n):
    key = (k, n)
    if key not in _GRID:
        if k == 3:
            pts = [(a, b, n - a - b) for a in range(n + 1) for b in range(n + 1 - a)]
        else:
            import itertools
            pts = [c for c in itertools.product(range(n + 1), repeat=k) if sum(c) == n]
        _GRID[key] = np.array(pts, float) / n
    return _GRID[key]


def updates_of(W, G, r):
    """d(w) for each row of W (vectorized update_of)."""
    GW = W @ G
    n = np.linalg.norm(GW, axis=1, keepdims=True)
    scale = np.where(n > 0, np.minimum(1.0, r / np.where(n > 0, n, 1.0)), 0.0)
    return -GW * scale


def alloc_oracle(eps, G, r, n=60):
    """Best worst residual reachable by changing only the allocation w, with the
    same gradients and the same update map: min over a simplex grid of
    m(d(w)). An upper bound on the exact minimum (grid step 1/n). Returns
    (Phi_alloc, w_best)."""
    W = simplex_grid(len(eps), n)
    D = updates_of(W, G, r)
    vals = np.max(eps[None, :] + D @ G.T, axis=1)
    i = int(np.argmin(vals))
    return float(vals[i]), W[i]


def oracle(eps, G, r):
    """Phi_r, a minimizer, the multipliers, and the duality gap (primal - dual >= 0)."""
    phi_d, lam = oracle_dual(eps, G, r)
    v = G.T @ lam
    nv = np.linalg.norm(v)
    d0 = -r * v / nv if nv > 1e-12 else np.zeros(G.shape[1])
    phi_p, d = oracle_primal(eps, G, r, d0=d0)
    return phi_p, d, lam, phi_p - phi_d


# ---------------------------------------------------------------- demands
class Demands:
    def __init__(self, centers, taus, H=None, eta=0.05):
        self.c = np.asarray(centers, float)
        self.tau = np.asarray(taus, float)
        p = self.c.shape[1]
        self.H = np.eye(p) if H is None else np.asarray(H, float)
        self.eta = eta

    def losses(self, theta):
        D = theta[None, :] - self.c
        return 0.5 * np.einsum("ij,jk,ik->i", D, self.H, D)

    def grads(self, theta):
        return (theta[None, :] - self.c) @ self.H.T

    def requirement(self, theta):
        return np.minimum(self.losses(theta) - self.tau, self.eta)

    def met(self, theta):
        return self.losses(theta) <= self.tau


def update_of(w, G, r):
    gw = w @ G
    n = np.linalg.norm(gw)
    return -gw * (min(1.0, r / n) if n > 0 else 0.0)


def softmax(x):
    z = np.exp(x - x.max())
    return z / z.sum()


def scores(rule, G, d, eps, eta):
    if rule == "A":
        nd = np.linalg.norm(d)
        if nd == 0:
            return np.zeros(len(G))
        ng = np.linalg.norm(G, axis=1)
        return (-G @ d) / (np.maximum(ng, 1e-12) * nd)
    if rule == "B":
        return (eps + G @ d) / eta
    raise ValueError(rule)


# ---------------------------------------------------------------- run
def run(dem, theta0, w0, rule, T=150, r=0.1, gamma=8.0, delta=0.9, noise=0.0,
        rng=None, burn=None):
    """Simulate one organization; return per-step records and a summary.

    noise: std of Gaussian noise on every gradient the organization sees (the
    same information for the update and the scores, under every rule); the
    oracle and the measures use exact gradients.
    """
    rng = np.random.default_rng(0) if rng is None else rng
    theta = np.array(theta0, float)
    w = np.array(w0, float)
    burn = T // 2 if burn is None else burn
    rec = {"phi": [], "phi_alloc": [], "m": [], "unmet": [], "wmax": []}
    for _ in range(T):
        G = dem.grads(theta)
        eps = dem.requirement(theta)
        Gs = G + noise * rng.standard_normal(G.shape) if noise > 0 else G
        phi, _ = oracle_exact2d(eps, G, r)
        phi_a, w_best = alloc_oracle(eps, G, r)
        if rule == "oracle":
            w = w_best
        d = update_of(w, Gs, r)
        rec["phi"].append(phi)
        rec["phi_alloc"].append(phi_a)
        rec["m"].append(worst_residual(eps, G, d))
        rec["unmet"].append(int((~dem.met(theta)).sum()))
        rec["wmax"].append(float(w.max()))
        if rule in ("A", "B"):
            s = scores(rule, Gs, d, eps, dem.eta)
            w = delta * w + (1 - delta) * softmax(gamma * s)
        theta = theta + d
    rec = {k_: np.array(v) for k_, v in rec.items()}
    tail = slice(burn, None)
    phi, pa, m = rec["phi"][tail], rec["phi_alloc"][tail], rec["m"][tail]
    tol = 1e-7
    summ = {
        # a requirement violated by the actual update
        "violation": float(np.mean(m > tol)),
        # violated while an admissible update meeting every requirement existed
        "realized_violation": float(np.mean((phi <= tol) & (m > tol))),
        # violated while some allocation, with the same search and the same
        # information, would have met every requirement
        "gov_frustration": float(np.mean((pa <= tol) & (m > tol))),
        # an admissible satisfactory update existed but no allocation reached it
        "unreachable": float(np.mean((phi <= tol) & (pa > tol))),
        "structural": float(np.mean(phi > tol)),
        "regret": float(np.mean(m - phi)),
        "final_unmet": int((~dem.met(theta)).sum()),
        "final_wmax": float(rec["wmax"][-1]),
        "final_leader": int(np.argmax(w)),
    }
    return rec, summ


def random_instance(rng, k=3, p=2, overlap=True, cond=1.0, eta=0.05):
    """k demand regions (ellipsoids under H) around centers spread on a circle.

    overlap=True puts a point z inside every region, so the demands are jointly
    satisfiable somewhere; overlap=False shrinks the regions so that (checked by
    the caller with common_region_nonempty) no point meets all of them.
    """
    H = np.diag(np.linspace(1.0, cond, p))
    ang = rng.uniform(0, 2 * np.pi) + 2 * np.pi * np.arange(k) / k + rng.normal(0, 0.3, k)
    c = np.zeros((k, p))
    c[:, 0], c[:, 1] = np.cos(ang), np.sin(ang)
    c *= rng.uniform(0.8, 1.2, (k, 1))
    z = rng.normal(0, 0.2, p)
    Lz = 0.5 * np.einsum("ij,jk,ik->i", z - c, H, z - c)
    taus = Lz * (rng.uniform(1.05, 1.3, k) if overlap else rng.uniform(0.15, 0.3, k))
    return Demands(c, taus, H, eta=eta)


def common_region_nonempty(dem, grid=241, lim=2.5):
    xs = np.linspace(-lim, lim, grid)
    X, Y = np.meshgrid(xs, xs)
    P = np.stack([X.ravel(), Y.ravel()], 1)
    ok = np.ones(len(P), bool)
    for i in range(len(dem.c)):
        D = P - dem.c[i]
        ok &= 0.5 * np.einsum("ij,jk,ik->i", D, dem.H, D) <= dem.tau[i]
    return bool(ok.any())
