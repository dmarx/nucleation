# scratch/formal/orbit_descent_check.py
# Check of CLAIM-tmpqvtgm (needs numpy and scipy; run with python3 -I).
# Net f(x) = sum_j v_j relu(u_j x) with two hidden units; demands are squared
# errors on three data points. Two function-preserving symmetries act on
# theta = (u1, u2, v1, v2) as diffeomorphisms: per-unit ReLU rescaling
# (u_j, v_j) -> (a u_j, v_j / a), a > 0, whose derivative is not orthogonal,
# and swapping the hidden units, whose derivative is a permutation matrix.
# Checks, on random parameters:
#  1. chain rule g_i(theta) = D sigma^T g_i(sigma theta);
#  2. common descent, 0 not in conv{g_i}, decided by LP, agrees at theta and
#     sigma theta (expected: always, for both symmetries);
#  3. CLAIM-365's Euclidean residual Phi_r, via its dual over the simplex,
#     agrees at theta and sigma theta (expected: always for the swap, not in
#     general for rescaling).
import numpy as np
from scipy.optimize import linprog, minimize
rng = np.random.default_rng(1)
X = np.array([0.7, 1.3, 2.1]); Y = np.array([1.0, -0.5, 2.0])
def f(th, x):
    u1, u2, v1, v2 = th
    return v1 * max(u1 * x, 0) + v2 * max(u2 * x, 0)
def grads(th):
    u1, u2, v1, v2 = th; G = []
    for x, y in zip(X, Y):
        r = f(th, x) - y
        h1, h2 = max(u1 * x, 0), max(u2 * x, 0)
        G.append(2 * r * np.array([v1 * x * (u1 * x > 0), v2 * x * (u2 * x > 0), h1, h2]))
    return np.array(G)
def zero_in_hull(G):
    k = len(G)
    res = linprog(np.zeros(k), A_eq=np.vstack([G.T, np.ones(k)]),
                  b_eq=np.r_[np.zeros(G.shape[1]), 1], bounds=[(0, None)] * k, method="highs")
    return res.status == 0
def phi(G, eps, r, m=120):
    # the dual over the simplex, max of sum lam eps - r |sum lam g|, is concave:
    # evaluate on a fine barycentric grid, then polish with SLSQP from the best
    # grid point, both deterministic
    k = len(G); best = None
    for i in range(m + 1):
        for j in range(m + 1 - i):
            lam = np.array([i, j, m - i - j]) / m
            val = lam @ eps - r * np.linalg.norm(lam @ G)
            if best is None or val > best[0]: best = (val, lam)
    cons = ({"type": "eq", "fun": lambda l: l.sum() - 1},)
    o = minimize(lambda l: -(l @ eps - r * np.linalg.norm(l @ G)), best[1], method="SLSQP",
                 bounds=[(0, 1)] * k, constraints=cons, options={"ftol": 1e-13, "maxiter": 500})
    return max(best[0], -o.fun)
eps = np.array([0.05, 0.02, 0.03]); r = 0.1
n = 300; cd_mis = {"rescale": 0, "swap": 0}; phi_diff = {"rescale": 0, "swap": 0}; chain_ok = True
for _ in range(n):
    th = np.r_[rng.uniform(0.2, 2, 2), rng.uniform(-2, 2, 2)]
    a = rng.uniform(0.3, 3)
    for name, (sig, D) in {
        "rescale": (np.array([a * th[0], th[1], th[2] / a, th[3]]), np.diag([a, 1, 1 / a, 1])),
        "swap": (th[[1, 0, 3, 2]], np.eye(4)[[1, 0, 3, 2]]),
    }.items():
        G, Gs = grads(th), grads(sig)
        chain_ok &= np.allclose(G, Gs @ D)
        cd_mis[name] += zero_in_hull(G) != zero_in_hull(Gs)
        phi_diff[name] += abs(phi(G, eps, r) - phi(Gs, eps, r)) > 1e-6
print("chain rule holds:", chain_ok)
print("common-descent mismatches on", n, "orbit pairs:", cd_mis)
print("Phi_r differs (>1e-6) on", n, "orbit pairs:", phi_diff)
# the one-demand example: f = v relu(u x), x = 1, y = 1, theta = (4, 1), a = 1/2
g = lambda u, v: 2 * (v * max(u, 0) - 1) * np.array([v * (u > 0), max(u, 0)])
print("|g|^2 at (4,1):", g(4, 1) @ g(4, 1), " at (2,2):", g(2, 2) @ g(2, 2))
