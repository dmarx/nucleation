# scratch/formal/fca_basic_theorem_check.py: the twenty-seventh status review's check of the Basic Theorem re-derivation in NOTE-1593 (run: python3 -I scratch/formal/fca_basic_theorem_check.py)
# Galois property, intersection-closed extents and Theorem 1's meet and join on random contexts; L isomorphic to B(L, L, <=) on four lattices; CLAIM-564's table on CASE-212
"""Checks for the Ignatov reading: Basic Theorem on random contexts and on small lattices;
CLAIM-564's enumeration on CASE-212 (reader's own code)."""
import random
from itertools import combinations, product

def derive_G(A, M, I):  # A' : attributes shared by all objects in A
    return frozenset(m for m in M if all((g, m) in I for g in A))
def derive_M(B, G, I):  # B' : objects having all attributes in B
    return frozenset(g for g in G if all((g, m) in I for m in B))

def concepts(G, M, I):
    out = set()
    for r in range(len(G) + 1):
        for A in combinations(G, r):
            B = derive_G(A, M, I); E = derive_M(B, G, I)
            out.add((E, B))
    return out

def check_complete_lattice(G, M, I):
    C = concepts(G, M, I)
    ext = {e for e, b in C}
    # (1) Galois: A ⊆ B' <=> B ⊆ A' <=> A×B ⊆ I, on all pairs of subsets (small sizes)
    for r in range(len(G) + 1):
        for A in combinations(G, r):
            for s in range(len(M) + 1):
                for B in combinations(M, s):
                    a = set(A) <= derive_M(B, G, I); b = set(B) <= derive_G(A, M, I)
                    c = all((g, m) in I for g in A for m in B)
                    assert a == b == c
    # (2) extents closed under arbitrary intersection (incl. empty family = G): complete lattice
    assert frozenset(G) in ext
    for X in ext:
        for Y in ext:
            assert (X & Y) in ext
    # (3) meet formula of Theorem 1: (∩A_j, (∪B_j)'')
    Cl = list(C)
    for (A1, B1), (A2, B2) in combinations(Cl, 2):
        meetE = A1 & A2
        meetB = derive_G(derive_M(B1 | B2, G, I), M, I)
        assert (meetE, meetB) in C and derive_G(meetE, M, I) == meetB
        joinB = B1 & B2
        joinE = derive_M(derive_G(A1 | A2, M, I), G, I)
        assert (joinE, joinB) in C
    return len(C)

random.seed(1)
tot = 0
for trial in range(300):
    G = list(range(random.randint(1, 6))); M = list('abcdef'[:random.randint(1, 6)])
    I = {(g, m) for g in G for m in M if random.random() < 0.5}
    tot += check_complete_lattice(G, M, I)
print('random contexts checked: 300, concepts total', tot)

# second half: L ≅ B(L, L, ≤) via x -> (↓x, ↑x), for several finite lattices
def lattice_check(L, leq, name):
    I = {(x, y) for x in L for y in L if leq(x, y)}
    C = concepts(L, L, I)
    phi = {x: (frozenset(y for y in L if leq(y, x)), frozenset(y for y in L if leq(x, y))) for x in L}
    assert set(phi.values()) == C, name
    for x in L:
        for y in L:
            assert leq(x, y) == (phi[x][0] <= phi[y][0])
    print(f'{name}: |L|={len(L)}, |B(L,L,<=)|={len(C)}, x->(down x, up x) is an order-isomorphism')

divs = [d for d in range(1, 61) if 60 % d == 0]
lattice_check(divs, lambda a, b: b % a == 0, 'divisors of 60')
M3 = ['0', 'a', 'b', 'c', '1']
lattice_check(M3, lambda x, y: x == y or x == '0' or y == '1', 'M3')
N5 = ['0', 'a', 'b', 'c', '1']  # a < b, c incomparable
N5le = {('0', z) for z in N5} | {(z, '1') for z in N5} | {(z, z) for z in N5} | {('a', 'b')}
lattice_check(N5, lambda x, y: (x, y) in N5le, 'N5')
B3 = [frozenset(s) for r in range(4) for s in combinations('xyz', r)]
lattice_check(B3, lambda x, y: x <= y, 'Boolean lattice 2^3')

# CLAIM-564 on CASE-212: configurations with cost and demand sets
cfg = {'q1': (1, {1}), 'q23': (1, {2, 3}), 'q12': (2, {1, 2}), 'q13': (3, {1, 3})}
D = [1, 2, 3]
def implications(b):
    Q = [q for q, (c, s) in cfg.items() if c <= b]
    ext = lambda S: {q for q in Q if set(S) <= cfg[q][1]}
    out = []
    for r in range(1, 3):
        for S in combinations(D, r):
            for j in D:
                if j in S: continue
                if ext(S) <= ext([j]): out.append((S, j, 'vacuous' if not ext(S) else ''))
    return Q, out
for b in [1, 2, 3, None]:
    if b is None:
        Q = list(cfg); ext = lambda S: {q for q in Q if set(S) <= cfg[q][1]}
        imps = [(S, j) for r in range(1, 3) for S in combinations(D, r) for j in D if j not in S and ext(S) <= ext([j])]
        print('no budget:', imps)
    else:
        print('b =', b, *implications(b))
