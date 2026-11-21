"""scratch/formal/claim639_632_625_checks.py: re-derivation checks for the status review of 2026-11-20.

Three demonstrated claims, each checked by enumeration with a control that
must fire (DP-4).

CLAIM-639 (merge-tree levels under an error in the requirement).
  Five configurations x, m1, y, m2, z on a path, reversible moves between
  neighbours. Threshold d(u, v) = least, over paths, of the largest
  requirement on the path (endpoints included), identities free. Levels of
  the merge tree are the partitions into classes {d <= a} at each budget a.
  Probes p = {x, m1, y} | {m2, z} and q = {z} | rest; a level agrees under
  some cost order iff it is the common refinement of some set of probes
  (CLAIM-592). Asserted: true r (m1 = 1.0, m2 = 1.1) has a nontrivial
  middle level that is a probe refinement; the estimate (1.1, 1.0) is within
  0.1 everywhere, moves every threshold by at most 0.1, and has no
  nontrivial level that is a probe refinement. Also asserted on random
  ultrametric instances: a level whose bounding merges are more than 2 eps
  apart survives every estimate within eps (the claim's security bound).
  Control: with the merges 0.3 apart (> 2 eps = 0.2), the same eps = 0.1
  error cannot reorder them, and the agreeing level survives.

CLAIM-632 (Frechet bounds on readiness from per-capacity records).
  For random marginals on {0,1}^n (n = 2..4), a linear program over all
  joint distributions gives the least and greatest Pr(all hold); asserted
  equal to max(0, sum P - (n - 1)) and min P. The table's three rows are
  recomputed. The expiry clause is checked: if every marginal only falls,
  the upper bound only falls (a refutation from records outlasts the
  record), while the lower bound can fall below a floor it met (a
  certification need not). The joint-exercise sentence is checked to hold
  under pathwise decay (each success event only shrinks) and to fail under
  marginal-only decay: a control constructs a case in which both marginals
  fall and Pr(all hold) rises.

CLAIM-625 (gluing against continuation), discrete-time analogue.
  Random nondeterministic transition systems on a finite state set with a
  pointwise viable set K. Histories on an interval are admissible paths
  staying in K. Asserted: (i) two viable histories on [a, b] and [b, c]
  that agree at b glue to a viable history on [a, c]; (ii) a viable
  history on [0, t] extends viably to [0, T] iff its endpoint lies in the
  (T - t)-step viability kernel; (iii) some system has a viable history on
  [0, t] with no viable extension (restriction not onto). Control: a
  time-dependent K, under which the kernel test (computed with the
  time-invariant kernel) gives a wrong answer somewhere.

Run: python3 -I scratch/formal/claim639_632_625_checks.py
"""
import itertools
import random

import numpy as np
from scipy.optimize import linprog

rng = random.Random(20261120)

# ---------------------------------------------------------------- CLAIM-639
NODES = ["x", "m1", "y", "m2", "z"]
EDGES = [(0, 1), (1, 2), (2, 3), (3, 4)]


def thresholds(r, nodes=NODES, edges=EDGES):
    n = len(nodes)
    INF = float("inf")
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0.0  # identities free
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    # minimax path: for each source, widest-path style relaxation
    for s in range(n):
        best = [INF] * n
        best[s] = r[s]
        changed = True
        while changed:
            changed = False
            for u in range(n):
                if best[u] == INF:
                    continue
                for v in adj[u]:
                    c = max(best[u], r[v])
                    if c < best[v]:
                        best[v] = c
                        changed = True
        for t in range(n):
            if t != s:
                d[s][t] = best[t]
    return d


def partition_at(d, a):
    n = len(d)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for i in range(n):
        for j in range(i + 1, n):
            if d[i][j] <= a:
                parent[find(i)] = find(j)
    blocks = {}
    for i in range(n):
        blocks.setdefault(find(i), []).append(i)
    return frozenset(frozenset(b) for b in blocks.values())


def levels(d):
    heights = sorted({d[i][j] for i in range(len(d)) for j in range(len(d)) if i != j})
    out = [partition_at(d, -1.0)]
    for h in heights:
        p = partition_at(d, h)
        if p != out[-1]:
            out.append(p)
    return out, heights


def refine(parts, n):
    labels = [tuple(next(k for k, b in enumerate(sorted(map(sorted, P))) if i in b) for P in parts) for i in range(n)]
    blocks = {}
    for i, lab in enumerate(labels):
        blocks.setdefault(lab, []).append(i)
    return frozenset(frozenset(b) for b in blocks.values())


def probe_refinements(probes, n):
    out = set()
    for k in range(len(probes) + 1):
        for sub in itertools.combinations(probes, k):
            out.add(refine(list(sub), n))
    return out


def nontrivial(levs, n):
    return [L for L in levs if 1 < len(L) < n]


def check_639(r_true, r_est, eps):
    n = len(NODES)
    p = frozenset([frozenset([0, 1, 2]), frozenset([3, 4])])
    q = frozenset([frozenset([4]), frozenset([0, 1, 2, 3])])
    cands = probe_refinements([p, q], n)
    dt, de = thresholds(r_true), thresholds(r_est)
    assert all(abs(a - b) <= eps + 1e-12 for a, b in zip(r_true, r_est))
    assert all(abs(dt[i][j] - de[i][j]) <= eps + 1e-12 for i in range(n) for j in range(n))  # CLAIM-580
    lt, _ = levels(dt)
    le, _ = levels(de)
    agree_t = [L for L in nontrivial(lt, n) if L in cands]
    agree_e = [L for L in nontrivial(le, n) if L in cands]
    return agree_t, agree_e, lt, le


agree_t, agree_e, lt, le = check_639([0, 1.0, 0, 1.1, 0], [0, 1.1, 0, 1.0, 0], 0.1)
assert agree_t == [frozenset([frozenset([0, 1, 2]), frozenset([3]), frozenset([4])])], agree_t
assert agree_e == [], agree_e
assert frozenset([frozenset([0]), frozenset([1]), frozenset([2, 3, 4])]) in le
print("CLAIM-639 witness: true middle level agrees, estimated middle level {x}{m1}{y,m2,z} agrees with no probe set: OK")

# control: merges 0.3 apart, same eps = 0.1 error cannot reorder them
agree_t2, agree_e2, _, _ = check_639([0, 1.0, 0, 1.3, 0], [0, 1.1, 0, 1.2, 0], 0.1)
assert agree_t2 == agree_e2 != [], (agree_t2, agree_e2)
print("CLAIM-639 control (gap 0.3 > 2 eps): agreeing level survives: OK (control fires as expected)")


# security bound on random ultrametric instances: a level whose bounding
# merges are > 2 eps apart reappears in the estimate
def random_graph(n):
    edges = [(i, i + 1) for i in range(n - 1)]
    for i in range(n):
        for j in range(i + 2, n):
            if rng.random() < 0.3:
                edges.append((i, j))
    return edges


survived = 0
lost_close = 0
for trial in range(3000):
    n = rng.randint(4, 7)
    edges = random_graph(n)
    nodes = list(range(n))
    r = [round(rng.uniform(0, 2), 2) for _ in range(n)]
    eps = rng.choice([0.05, 0.1, 0.2])
    rh = [x + rng.uniform(-eps, eps) for x in r]
    dt = thresholds(r, nodes, edges)
    de = thresholds(rh, nodes, edges)
    assert all(abs(dt[i][j] - de[i][j]) <= eps + 1e-9 for i in range(n) for j in range(n))
    lt, ht = levels(dt)
    le, _ = levels(de)
    hs = [-1.0] + ht
    # level k of lt holds on [h_k, h_{k+1}); find its bounding merges
    for k in range(1, len(lt)):
        lo = sorted({dt[i][j] for i in range(n) for j in range(n) if i != j and partition_at(dt, dt[i][j]) == lt[k]})
        if not lo:
            continue
        h1 = lo[0]
        higher = [h for h in ht if h > h1 and partition_at(dt, h) != lt[k]]
        if not higher:
            continue
        h2 = higher[0]
        if h2 - h1 > 2 * eps + 1e-9:
            assert lt[k] in le, (r, rh, eps, lt[k])
            survived += 1
        elif lt[k] not in le:
            lost_close += 1
assert lost_close > 0  # control: the survival test can fail, and does when the gap is <= 2 eps
print(f"CLAIM-639 security bound: {survived} levels with gap > 2 eps all survive; "
      f"control: {lost_close} levels with gap <= 2 eps lost: OK")

# ---------------------------------------------------------------- CLAIM-632


def frechet_lp(P):
    n = len(P)
    atoms = list(itertools.product([0, 1], repeat=n))
    A_eq = [[1.0] * len(atoms)]
    b_eq = [1.0]
    for i in range(n):
        A_eq.append([float(a[i]) for a in atoms])
        b_eq.append(P[i])
    c = np.array([1.0 if all(a) else 0.0 for a in atoms])
    lo = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(0, 1), method="highs")
    hi = linprog(-c, A_eq=A_eq, b_eq=b_eq, bounds=(0, 1), method="highs")
    assert lo.status == 0 and hi.status == 0
    return lo.fun, -hi.fun


for trial in range(1500):
    n = rng.randint(2, 4)
    P = [rng.random() for _ in range(n)]
    lo, hi = frechet_lp(P)
    L = max(0.0, sum(P) - (n - 1))
    U = min(P)
    assert abs(lo - L) < 1e-7 and abs(hi - U) < 1e-7, (P, lo, hi, L, U)
print("CLAIM-632 bounds: LP extremes equal Frechet bounds on 1500 marginal vectors: OK")

# control: a wrong lower bound (product of marginals) is not the LP minimum
P = [0.9, 0.9, 0.9, 0.9]
lo, hi = frechet_lp(P)
assert abs(lo - 0.6) < 1e-7 and abs(hi - 0.9) < 1e-7
assert abs(lo - 0.9 ** 4) > 0.05
print("CLAIM-632 control: independence value 0.6561 is not the bound 0.6: OK (control fires)")

rows = [((0.9, 0.9, 0.9, 0.9), (0.6, 0.9)), ((0.97, 0.97, 0.97, 0.95), (0.86, 0.95)), ((0.6, 0.95, 0.95, 0.95), (0.45, 0.6))]
for P, (L, U) in rows:
    lo, hi = frechet_lp(list(P))
    assert abs(lo - L) < 1e-7 and abs(hi - U) < 1e-7
v = lambda R: 3 * R - 2
assert abs(v(0.6) + 0.2) < 1e-9 and abs(v(0.9) - 0.7) < 1e-9 and abs(v(0.86) - 0.58) < 1e-9 and abs(v(0.6) + 0.2) < 1e-9
print("CLAIM-632 table rows recomputed: OK")

# expiry with marginal decay
cert_lost = 0
for trial in range(2000):
    n = rng.randint(2, 5)
    P = [rng.uniform(0.7, 1.0) for _ in range(n)]
    Q = [p - rng.uniform(0, 0.1) for p in P]
    U, Up = min(P), min(Q)
    L, Lp = max(0, sum(P) - (n - 1)), max(0, sum(Q) - (n - 1))
    assert Up <= U + 1e-12 and Lp <= L + 1e-12
    rstar = rng.uniform(0.5, 1.0)
    if U < rstar:
        assert Up < rstar  # refutation outlasts
    if L >= rstar and Lp < rstar:
        cert_lost += 1
assert cert_lost > 0
print(f"CLAIM-632 expiry: refutations always outlast; {cert_lost} certifications lost: OK")

# joint exercise: pathwise decay keeps R from rising; marginal-only decay need not
# two capacities on a 20-point uniform space: CASE-237 run backwards
N = 20
A1 = set(range(0, 17))          # 0.85
A2 = set(range(3, 20))          # 0.85, failing apart: R = 0.7
R0 = len(A1 & A2) / N
assert abs(R0 - 0.7) < 1e-12
B1 = set(range(0, 16))          # 0.8  (pathwise: subset of A1)
B2 = set(range(4, 20))          # 0.8  (pathwise: subset of A2)
assert B1 <= A1 and B2 <= A2
assert len(B1 & B2) / N <= R0
C1 = set(range(0, 16))          # 0.8
C2 = set(range(0, 16))          # 0.8, failing together: R = 0.8 > 0.7
assert len(C1) < len(A1) and len(C2) < len(A2)
assert len(C1 & C2) / N > R0
print("CLAIM-632 joint-exercise sentence: holds under pathwise decay; fails under marginal-only decay "
      f"(R {R0} -> {len(C1 & C2) / N}): control fires")

# ---------------------------------------------------------------- CLAIM-625


def kernel(succ, K, steps):
    """States from which some path of `steps` moves stays in K (start included)."""
    V = set(K)
    for _ in range(steps):
        V = {s for s in K if any(t in V for t in succ[s])}
    return V


def viable_paths(succ, K, start_states, length):
    paths = [[s] for s in start_states if s in K]
    for _ in range(length):
        paths = [p + [t] for p in paths for t in succ[p[-1]] if t in K]
    return paths


terminal_found = False
for trial in range(400):
    S = rng.randint(3, 6)
    succ = {s: [t for t in range(S) if rng.random() < 0.35] for s in range(S)}
    K = {s for s in range(S) if rng.random() < 0.75}
    T = rng.randint(2, 5)
    for t in range(0, T + 1):
        hist = viable_paths(succ, K, range(S), t)
        ker = kernel(succ, K, T - t)
        for h in hist:
            ext = any(True for e in viable_paths(succ, K, [h[-1]], T - t))
            assert ext == (h[-1] in ker), (succ, K, h, T, t)
            if not ext:
                terminal_found = True
    # gluing: histories on [0,b] and [b,c] agreeing at b
    for b in range(0, 3):
        left = viable_paths(succ, K, range(S), b)
        for hl in left[:20]:
            for hr in viable_paths(succ, K, [hl[-1]], 2)[:20]:
                g = hl + hr[1:]
                assert all(s in K for s in g) and all(g[i + 1] in succ[g[i]] for i in range(len(g) - 1))
assert terminal_found
print("CLAIM-625 discrete analogue: gluing holds; extension iff endpoint in finite-horizon kernel; "
      "a terminal viable history exists: OK")

# control: time-dependent K breaks the time-invariant kernel test
succ = {0: [0], 1: [1]}
K_t = lambda k: {0, 1} if k < 2 else {1}  # state 0 leaves the constraint at step 2
hist = [[0, 0]]  # viable on [0, 1]
T = 3
ext = all(K_t(k) >= {0} for k in range(2, T + 1))
inv_ker = kernel(succ, K_t(0), T - 1)
assert (0 in inv_ker) and not ext
print("CLAIM-625 control (time-dependent K): time-invariant kernel test wrongly predicts extension: control fires")
print("all checks passed")
