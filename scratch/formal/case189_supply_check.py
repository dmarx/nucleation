"""scratch/formal/case189_supply_check.py

An independent check of CLAIM-tmpv6tw7 (CASE-189's Construction 2 with a
supply s), written from the claim's and CASE-189's stated model, not from
the filer's script (scratch/manuscripts/governance-of-becoming/analysis/
case189_supply_parameter.py). Written at the recomputation pass of
2026-11-25 by a session other than the filer's. Run: python3 -I this
file. numpy and scipy.

Model (after the encounter, h = 0):
    q'  = 12 s_q q c1 c2/(1 + c1 c2) (1 - q) - q
    ci' = 4 s q cj^2/(1 + cj^2) - (1 + d) ci
Arm A: s_q = s; arm B: s_q = 1. Control: q' = s Kq (1 - q) - q,
ci' = s Kc - (1 + d) ci, matched to arm A's kept state at s = 1, d = 0.
The folds are found from the symmetric equilibrium curves s(c) by bounded
minimization, the outage limits by bisection on the outage length, the
coupling gap as q c (L = q B^T diag(c, c) B on a three-unit chain has
spectrum {0, qc, 3qc}).
"""
import math

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize_scalar


def rhs(s, sq, d):
    def f(t, y):
        q, c1, c2 = y
        return [12 * sq * q * c1 * c2 / (1 + c1 * c2) * (1 - q) - q,
                4 * s * q * c2 ** 2 / (1 + c2 ** 2) - (1 + d) * c1,
                4 * s * q * c1 ** 2 / (1 + c1 ** 2) - (1 + d) * c2]
    return f


def settle(y0, s, arm, d=0.0, T=150.0):
    sq = s if arm == "A" else 1.0
    r = solve_ivp(rhs(s, sq, d), (0, T), y0, rtol=1e-10, atol=1e-13, method="LSODA")
    return r.y[:, -1]


# symmetric equilibria at s = 1, d = 0: q = 1 - (1 + c^2)/(12 c^2) and q = (1 + c^2)/(4 c)
g = lambda c: 1 - (1 + c * c) / (12 * c * c) - (1 + c * c) / (4 * c)
c_lo, c_hi = brentq(g, 0.3, 1.0), brentq(g, 2.0, 5.0)
q_of = lambda c: (1 + c * c) / (4 * c)
kept = np.array([q_of(c_hi), c_hi, c_hi])
saddle = np.array([q_of(c_lo), c_lo, c_lo])
assert abs(c_hi - 3.3371) < 5e-4 and abs(c_lo - 0.5212) < 5e-4, (c_lo, c_hi)
print(f"s = 1: kept c = {c_hi:.4f}, saddle c = {c_lo:.4f}")

# (1) ignition, both arms
for arm in "AB":
    assert settle(0.9 * saddle, 1.0, arm).max() < 1e-3
    assert abs(settle(1.1 * saddle, 1.0, arm)[1] - c_hi) < 1e-3

# (2) folds. Arm A: q = 1 - (1+c^2)/(12 s c^2) and q = (1+d)(1+c^2)/(4 s c) give s(c)
sA = lambda c, d: (1 + c * c) / (12 * c * c) + (1 + d) * (1 + c * c) / (4 * c)
# Arm B: q = 11/12 - 1/(12 c^2), s = (1+d)(1+c^2)/(4 q c)
qB = lambda c: 11 / 12 - 1 / (12 * c * c)
sB = lambda c, d: (1 + d) * (1 + c * c) / (4 * qB(c) * c)
res = {}
for arm, sf in (("A", sA), ("B", sB)):
    for d in (0.0, 0.4):
        m = minimize_scalar(lambda c: sf(c, d), bounds=(0.4, 5), method="bounded", options={"xatol": 1e-10})
        c = m.x
        if arm == "A":
            q = (1 + d) * (1 + c * c) / (4 * m.fun * c)
        else:
            q = qB(c)
        res[(arm, d)] = (m.fun, c, q, q * c)
dstar = 0.6908
want = {("A", 0.0): 0.6491, ("A", 0.4): 0.8528, ("B", 0.0): 0.5914, ("B", 0.4): 0.8280}
for k, v in want.items():
    assert abs(res[k][0] - v) < 5e-4, (k, res[k])
assert abs(res[("B", 0.0)][0] - 1 / (1 + dstar)) < 2e-4
assert abs(res[("A", 0.0)][3] - 0.977) < 1e-3 and abs(res[("B", 0.0)][3] - 0.989) < 1e-3
for k, v in res.items():
    print(f"arm {k[0]}, d = {k[1]}: s* = {v[0]:.4f} at c = {v[1]:.4f}, q = {v[2]:.4f}; gap qc = {v[3]:.4f}")

# collapse rather than decline: kept from the s = 1 state just above s*, out just below
sa = res[("A", 0.0)][0]
above = settle(kept, sa + 0.01, "A")[1]
below = settle(kept, sa - 0.01, "A").max()
assert abs(above - 1.47) < 0.01 and below < 1e-3, (above, below)
print(f"arm A at s* + 0.01: c = {above:.3f}; at s* - 0.01: out")


# (3) outage: s = 0 for T, then s = 1; relights iff T < T_lost
def relights(T, arm):
    y = settle(kept, 0.0, arm, T=T)
    return settle(y, 1.0, arm)[1] > 0.5


lim = {}
for arm in "AB":
    assert relights(0.5, arm) and not relights(5.0, arm)
    lo, hi = 0.5, 5.0
    while hi - lo > 1e-3:
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if relights(mid, arm) else (lo, mid)
    lim[arm] = (lo + hi) / 2
assert abs(lim["A"] - 1.51) < 0.01 and abs(lim["B"] - 1.92) < 0.01, lim
print(f"outage limits: arm A {lim['A']:.3f}, arm B {lim['B']:.3f}")

# control: supplied repair matched to arm A's kept state
Kc = c_hi
Kq = kept[0] / (1 - kept[0])
ctrl = lambda s: (lambda t, y: [s * Kq * (1 - y[0]) - y[0], s * Kc - y[1], s * Kc - y[2]])
from_zero = solve_ivp(ctrl(1.0), (0, 150), [0, 0, 0], rtol=1e-10, atol=1e-13).y[:, -1]
assert abs(from_zero[1] - 3.337) < 1e-3
assert abs(0.639 * Kc - 2.13) < 0.01
after = solve_ivp(ctrl(1.0), (0, 150), solve_ivp(ctrl(0.0), (0, 30), list(kept)).y[:, -1]).y[:, -1]
assert abs(after[1] - Kc) < 1e-3
print("control: reaches c = 3.337 from zero, c = s Kc (2.13 at s = 0.639), full return after a 30-unit outage")

# negative control: a wrong fold value is caught
assert abs(res[("A", 0.0)][0] - 0.5914) > 0.01
print("checks pass")
