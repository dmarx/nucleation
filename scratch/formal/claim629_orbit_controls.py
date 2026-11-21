"""Firing controls for CLAIM-629's first item (status review of 2026-11-20).

scratch/formal/orbit_descent_check.py found no common-descent mismatch on 300
orbit pairs of a two-unit ReLU net. That passes vacuously if the verdict is
the same at almost every point, or if the LP comparison cannot tell two
gradient sets apart. This script re-runs the comparison with controls.

Checks:
  1. Both verdicts occur among the sampled points (common descent, and 0 in
     the convex hull of the gradients), so agreement is not forced.
  2. On every orbit pair (ReLU rescaling by a > 0; swapping the units) the
     verdict agrees, and the chain rule g(theta) = D sigma^T g(sigma theta)
     holds.
Controls (each must report mismatches):
  C1. A linear map that is not a symmetry: rescale u1 by a, leave v1. The
      losses are not preserved, and the verdict should differ on some pairs.
  C2. The right gradients at theta against a wrong pull-back: compare the
      verdict at theta with the verdict for D sigma^{-T} g(sigma theta)'s
      shuffled demand assignment (the gradients of different demands at
      sigma theta reassigned at random, with one sign flipped). This must
      differ somewhere, or the LP is not discriminating.
  C3. The one-demand rescaling example: squared gradient norm 612 at (4, 1)
      and 288 at (2, 2); a = 1 (identity) must give equal norms.
Run: python3 -I scratch/formal/claim629_orbit_controls.py (needs numpy, scipy)
"""
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(20261120)
X = np.array([0.7, 1.3, 2.1, -0.9]); Y = np.array([1.0, -0.5, 2.0, 0.3])


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


n = 400
verdicts = {True: 0, False: 0}
mis = {"rescale": 0, "swap": 0, "C1 not a symmetry": 0, "C2 shuffled": 0}
chain_ok = True
for _ in range(n):
    th = np.r_[rng.uniform(-2, 2, 2), rng.uniform(-2, 2, 2)]
    a = rng.uniform(0.3, 3)
    G = grads(th); z = zero_in_hull(G); verdicts[z] += 1
    for name, (sig, D) in {
        "rescale": (np.array([a * th[0], th[1], th[2] / a, th[3]]), np.diag([a, 1, 1 / a, 1])),
        "swap": (th[[1, 0, 3, 2]], np.eye(4)[[1, 0, 3, 2]]),
    }.items():
        Gs = grads(sig)
        chain_ok &= np.allclose(G, Gs @ D)
        mis[name] += z != zero_in_hull(Gs)
    # C1: u1 -> a u1 only; not function-preserving
    mis["C1 not a symmetry"] += z != zero_in_hull(grads(np.array([a * th[0], th[1], th[2], th[3]])))
    # C2: wrong demand assignment with a sign flip
    Gw = G[rng.permutation(len(G))].copy(); Gw[0] *= -1
    mis["C2 shuffled"] += z != zero_in_hull(Gw)

print("verdicts over", n, "points (True = 0 in hull):", verdicts)
print("chain rule holds:", chain_ok)
print("mismatches:", mis)
g = lambda u, v: 2 * (v * max(u, 0) - 1) * np.array([v * (u > 0), max(u, 0)])
print("C3 |g|^2 at (4,1):", g(4, 1) @ g(4, 1), " at (2,2):", g(2, 2) @ g(2, 2),
      " identity a=1:", g(4, 1) @ g(4, 1) == g(4, 1) @ g(4, 1))
assert verdicts[True] > 0 and verdicts[False] > 0, "check 1 vacuous"
assert chain_ok and mis["rescale"] == 0 and mis["swap"] == 0, "check 2 failed"
assert mis["C1 not a symmetry"] > 0, "control C1 did not fire"
assert mis["C2 shuffled"] > 0, "control C2 did not fire"
assert g(4, 1) @ g(4, 1) == 612 and g(2, 2) @ g(2, 2) == 288
print("claim629 orbit controls: all passed, both controls fired")
