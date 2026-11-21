"""Check of CLAIM-759 (status review of 2026-11-20).

Step 2: the orbit partition of a group of automorphisms of a weighted directed
graph is balanced (each unit of a cell gets the same total input weight from
each cell). Step 4: for n >= 5, every homomorphism from S_n to S_m, m < n, has
image of order at most 2.

Checks:
  1. 300 random weighted digraphs made invariant under a random permutation
     group (weights averaged over the group): the orbit partition is balanced.
  2. Every homomorphism S_5 -> S_4 and S_5 -> S_3 (enumerated on the
     generators (0 1), (0 1 2 3 4) and verified on all 120 elements) has
     image of order 1 or 2, and some has order 2 (the sign).
Controls (each must fire):
  C1. The same graphs without the averaging: the orbit partition of the
      group is then usually not balanced.
  C2. S_4 -> S_3 (n = 4 < 5) has a homomorphism with image of order 6, so
      the bound needs n >= 5.
  C3. S_5 -> S_5 has the identity, image of order 120: the enumerator finds
      large images when they exist.
Run: python3 -I scratch/formal/claim759_orbit_balance_check.py
"""
import itertools
import random

random.seed(759)


def compose(a, b):  # (a o b)(i) = a[b[i]]
    return tuple(a[i] for i in b)


def closure(gens, n):
    e = tuple(range(n)); G = {e}; frontier = [e]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = compose(s, g)
                if h not in G:
                    G.add(h); nxt.append(h)
        frontier = nxt
    return G


def orbits(G, n):
    seen, parts = set(), []
    for i in range(n):
        if i not in seen:
            o = {g[i] for g in G}; seen |= o; parts.append(o)
    return parts


def balanced(W, parts, tol=1e-9):
    for P in parts:
        for O in parts:
            vals = [sum(W[k][i] for k in O) for i in P]
            if max(vals) - min(vals) > tol:
                return False
    return True


bal_ok = True; c1_fired = 0; nontrivial = 0
for _ in range(300):
    n = random.randint(4, 9)
    gens = []
    for _ in range(random.randint(1, 2)):
        perm = list(range(n))
        k = random.randint(2, n)
        idx = random.sample(range(n), k)
        cyc = idx[:]
        random.shuffle(cyc)
        for a, b in zip(idx, cyc):
            perm[a] = b
        gens.append(tuple(perm))
    G = closure(gens, n); parts = orbits(G, n)
    nontrivial += len(parts) < n
    W0 = [[random.uniform(-1, 1) for _ in range(n)] for _ in range(n)]
    W = [[sum(W0[g[i]][g[j]] for g in G) / len(G) for j in range(n)] for i in range(n)]
    # W is fixed: W[g i][g j] = W[i][j]
    assert all(abs(W[g[i]][g[j]] - W[i][j]) < 1e-12 for g in G for i in range(n) for j in range(n))
    bal_ok &= balanced(W, parts)
    if len(parts) < n:
        c1_fired += not balanced(W0, parts)
print("graphs with a nontrivial orbit partition:", nontrivial, "all balanced:", bal_ok,
      "C1 unbalanced without averaging:", c1_fired)
assert nontrivial > 100 and bal_ok, "check 1 failed"
assert c1_fired > 0, "control C1 did not fire"


def homs(n, m):
    """All homomorphisms S_n -> S_m, as their image sizes."""
    s = tuple([1, 0] + list(range(2, n))); t = tuple(list(range(1, n)) + [0])
    # BFS words over the generators to every element of S_n
    e = tuple(range(n)); word = {e: ()}; frontier = [e]
    while frontier:
        nxt = []
        for g in frontier:
            for gi, gen in enumerate((s, t)):
                h = compose(g, gen)
                if h not in word:
                    word[h] = word[g] + (gi,); nxt.append(h)
        frontier = nxt
    assert len(word) == len(list(itertools.permutations(range(n))))
    Sm = list(itertools.permutations(range(m))); em = tuple(range(m)); sizes = []
    for a in Sm:
        for b in Sm:
            phi = {}
            for g, w in word.items():
                x = em
                for gi in w:
                    x = compose(x, (a, b)[gi])
                phi[g] = x
            if all(phi[compose(g, gen)] == compose(phi[g], img)
                   for g in word for gen, img in ((s, a), (t, b))):
                sizes.append(len(set(phi.values())))
    return sizes


h54, h53 = homs(5, 4), homs(5, 3)
print("S5->S4 image sizes:", sorted(set(h54)), " S5->S3:", sorted(set(h53)))
assert max(h54) == 2 and max(h53) == 2 and 2 in h54, "check 2 failed"
h43 = homs(4, 3)
print("C2 S4->S3 image sizes:", sorted(set(h43)))
assert 6 in h43, "control C2 did not fire"
h55 = homs(5, 5)
print("C3 S5->S5 image sizes:", sorted(set(h55)))
assert 120 in h55, "control C3 did not fire"
print("claim759 orbit-balance check: all passed, controls C1-C3 fired")
