"""Numerical checks of the receiver-restricted order's results.
Run: OMP_NUM_THREADS=1 python3 -I run_checks.py  (from this directory, or
pass the directory on sys.path as below). Writes results.json beside it."""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rorder import (achievable, compatible_garbling, deterministic_map,  # noqa: E402
                    factoring_class, factors_through, in_hull, r_dominates,
                    random_stochastic, respects, unrestricted_class,
                    usable_risk)

rng = np.random.default_rng(100)
out = {}

# ---------- E1: CLAIM-199's XOR example on a common medium {0,1}^2 -------
# outcome index x = 2*x1 + x2
def idx(x1, x2):
    return 2 * x1 + x2

U = np.zeros((2, 4))
for z in (0, 1):
    for x1 in (0, 1):
        U[z, idx(x1, z ^ x1)] = 0.5
G_xor = np.zeros((4, 4))
for x1 in (0, 1):
    for x2 in (0, 1):
        G_xor[idx(x1, x2), idx(x1 ^ x2, 0)] = 1.0
T1 = deterministic_map([0, 0, 1, 1], 2)  # reads x1
T2 = deterministic_map([0, 1, 0, 1], 2)  # reads x2
R1 = factoring_class(T1, 2) + factoring_class(T2, 2)  # one-coordinate
Rall = unrestricted_class(4, 2)
L01 = 1.0 - np.eye(2)
pi = np.array([0.5, 0.5])
out["E1_xor"] = {
    "V_R1(U)": usable_risk(U, R1, L01, pi),
    "V_R1(UG)": usable_risk(U @ G_xor, R1, L01, pi),
    "V_all(U)": usable_risk(U, Rall, L01, pi),
    "V_all(UG)": usable_risk(U @ G_xor, Rall, L01, pi),
    "G_xor in Mon(R1)": respects(G_xor, R1),
}

# ---------- E2: strict reversal of Blackwell's order --------------------
# P: x1 = z with prob .9, x2 a fair coin independent of z.
P = np.zeros((2, 4))
for z in (0, 1):
    for x1 in (0, 1):
        for x2 in (0, 1):
            P[z, idx(x1, x2)] = (0.9 if x1 == z else 0.1) * 0.5
r_PU, _ = r_dominates(P, U, R1)
r_UP, _ = r_dominates(U, P, R1)
a_UP, _ = r_dominates(U, P, Rall)
a_PU, _ = r_dominates(P, U, Rall)
out["E2_reversal"] = {
    "P >=_R1 U": r_PU, "U >=_R1 P": r_UP,
    "U >=_all P": a_UP, "P >=_all U": a_PU,
    "V_R1(P)": usable_risk(P, R1, L01, pi),
    "V_R1(U)": usable_risk(U, R1, L01, pi),
    "V_all(P)": usable_risk(P, Rall, L01, pi),
    "V_all(U)": usable_risk(U, Rall, L01, pi),
}

# ---------- T1: Ach criterion and prior independence --------------------
n_t, n_x, n_a = 3, 4, 2
agree = 0
viol = 0
trials = 0
incl_count = 0
for k in range(300):
    f = list(rng.permutation([0, 1] + list(rng.integers(0, 2, n_x - 2))))
    T = deterministic_map(f, 2)
    R = factoring_class(T, n_a)
    P = random_stochastic(rng, n_t, n_x)
    if k % 2 == 0:
        Pp = P @ compatible_garbling(rng, f, 2)  # often dominated
    else:
        Pp = random_stochastic(rng, n_t, n_x)
    ok, W = r_dominates(P, Pp, R)
    trials += 1
    if ok:
        incl_count += 1
        bad = 0
        for _ in range(300):
            pr = rng.dirichlet(np.ones(n_t))
            L = rng.normal(size=(n_t, n_a))
            if usable_risk(Pp, R, L, pr) < usable_risk(P, R, L, pr) - 1e-9:
                bad += 1
        viol += bad
        agree += bad == 0
    else:
        sep_all = True
        for _ in range(5):
            pr = rng.dirichlet(np.ones(n_t))
            L = W / pr[:, None]
            if not usable_risk(Pp, R, L, pr) < usable_risk(P, R, L, pr) - 1e-9:
                sep_all = False
        agree += sep_all
out["T1_ach_criterion_prior_free"] = {
    "trials": trials, "inclusions": incl_count,
    "agreeing": agree, "violations_when_included": viol}

# ---------- T2: Mon(R) = garblings the receiver can simulate -----------
res = {"trials": 0, "respects": 0, "hull_eq_factor": 0,
       "mono_violations": 0, "identity_witness_ok": 0, "non_respecting": 0}
for k in range(300):
    f = list(rng.permutation([0, 1] + list(rng.integers(0, 2, n_x - 2))))
    T = deterministic_map(f, 2)
    R = factoring_class(T, n_a)
    G = compatible_garbling(rng, f, 2) if k % 2 == 0 else \
        random_stochastic(rng, n_x, n_x, sparsity=0.5)
    resp = respects(G, R)
    fac = factors_through(G, T)
    res["trials"] += 1
    res["hull_eq_factor"] += resp == fac
    if resp:
        res["respects"] += 1
        for _ in range(50):
            Pq = random_stochastic(rng, n_t, n_x)
            pr = rng.dirichlet(np.ones(n_t))
            L = rng.normal(size=(n_t, n_a))
            if usable_risk(Pq @ G, R, L, pr) < usable_risk(Pq, R, L, pr) - 1e-9:
                res["mono_violations"] += 1
    else:
        res["non_respecting"] += 1
        Id = np.eye(n_x)  # Theta = X, the identity experiment
        ok, W = r_dominates(Id, G, R)
        if not ok:
            pr = np.full(n_x, 1.0 / n_x)
            L = W / pr[:, None]
            if usable_risk(G, R, L, pr) < usable_risk(Id, R, L, pr) - 1e-9:
                res["identity_witness_ok"] += 1
out["T2_monoid_theorem"] = res

# ---------- T3: the ceiling ----------------------------------------------
cviol = 0
for k in range(500):
    f = list(rng.permutation([0, 1] + list(rng.integers(0, 2, n_x - 2))))
    R = factoring_class(deterministic_map(f, 2), n_a)
    Pq = random_stochastic(rng, n_t, n_x)
    G = random_stochastic(rng, n_x, n_x, sparsity=0.5)
    pr = rng.dirichlet(np.ones(n_t))
    L = rng.normal(size=(n_t, n_a))
    if usable_risk(Pq @ G, R, L, pr) < usable_risk(Pq, Rall_ := unrestricted_class(n_x, n_a), L, pr) - 1e-9:
        cviol += 1
out["T3_ceiling"] = {"trials": 500, "violations": cviol}

# ---------- T4: factoring receivers inherit Blackwell's converse --------
# P >=_{R_T} P' iff P'T is a garbling of PT (finite converse applied to PT).
def is_garbling(Q, Qp):
    """exists stochastic K with Qp = Q K ?"""
    from scipy.optimize import linprog
    n, m = Q.shape[1], Qp.shape[1]
    A, b = [], []
    for t in range(Q.shape[0]):
        for j in range(m):
            row = np.zeros(n * m)
            for y in range(n):
                row[y * m + j] = Q[t, y]
            A.append(row); b.append(Qp[t, j])
    for y in range(n):
        row = np.zeros(n * m); row[y * m:(y + 1) * m] = 1.0
        A.append(row); b.append(1.0)
    r = linprog(np.zeros(n * m), A_eq=np.array(A), b_eq=np.array(b),
                bounds=[(0, None)] * (n * m), method="highs")
    return r.status == 0

t4 = {"trials": 0, "agree": 0, "dominated": 0}
for k in range(200):
    f = list(rng.permutation([0, 1, 2] + list(rng.integers(0, 3, 2))))
    T = deterministic_map(f, 3)
    R = factoring_class(T, 3)  # |A| = |Y| = 3 suffices for the converse
    Pq = random_stochastic(rng, 2, 5)
    Pp = Pq @ random_stochastic(rng, 5, 5) if k % 2 == 0 else random_stochastic(rng, 2, 5)
    ok, _ = r_dominates(Pq, Pp, R)
    g = is_garbling(Pq @ T, Pp @ T)
    t4["trials"] += 1
    t4["agree"] += ok == g
    t4["dominated"] += ok
out["T4_factoring_inherits_converse"] = t4

with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(out, fh, indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else float(o))
print(json.dumps(out, indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else float(o)))
