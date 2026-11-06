# scratch/formal/case212_check.py: the twenty-seventh status review's second check of CASE-212 and CLAIM-564 (run: python3 -I scratch/formal/case212_check.py)
# Four configurations with costs and the demands they meet; checks the budgeted complex K(b) at every
# budget, the table of implications S -> j (j not in S) in CLAIM-564, antitonicity of valid implications
# in the budget on random costed contexts, and a control that the inverse inclusion fails.
from itertools import combinations
import random

Q = {'q1': (1, {1}), 'q23': (1, {2, 3}), 'q12': (2, {1, 2}), 'q13': (3, {1, 3})}
D = [1, 2, 3]
SUBS = [frozenset(c) for r in range(4) for c in combinations(D, r)]

def aff(b): return [q for q, (c, _) in Q.items() if c <= b]
def psi(S, b): return [q for q in aff(b) if S <= Q[q][1]]
def K(b): return {tuple(sorted(S)) for S in SUBS if S and psi(S, b)}
def imps(b):
    return {(tuple(sorted(S)), j, not psi(S, b)) for S in SUBS for j in D
            if j not in S and all(j in Q[q][1] for q in psi(S, b))}

verts = {(1,), (2,), (3,)}
assert K(0.5) == set()
assert K(1) == K(1.5) == verts | {(2, 3)}
assert K(2) == K(2.5) == verts | {(2, 3), (1, 2)}
assert K(3) == K(10) == verts | {(2, 3), (1, 2), (1, 3)}
assert all((1, 2, 3) not in K(b) for b in [0.5, 1, 2, 3, 10])
assert imps(1) == imps(1.5) == {((2,), 3, False), ((3,), 2, False), ((1, 2), 3, True), ((1, 3), 2, True)}
assert imps(2) == imps(2.5) == {((3,), 2, False), ((1, 3), 2, True)}
assert imps(3) == imps(10) == set()
print('CASE-212 complexes and CLAIM-564 table: as stated')

random.seed(0)
def valid(QQ, subs, b):
    ext = lambda S: {q for q, (c, a) in QQ.items() if c <= b and S <= a}
    return {(S, T) for S in subs for T in subs if ext(S) <= ext(T)}
bad = ctl = 0
for t in range(2000):
    n, m = random.randint(1, 5), random.randint(1, 4)
    QQ = {i: (random.randint(0, 5), {d for d in range(m) if random.random() < .5}) for i in range(n)}
    subs = [frozenset(c) for r in range(m + 1) for c in combinations(range(m), r)]
    V = [valid(QQ, subs, b) for b in range(6)]
    bad += sum(1 for b in range(6) for b2 in range(b) if not V[b] <= V[b2])
    ctl += not V[0] <= V[5]
assert bad == 0 and ctl > 0
print('antitone violations:', bad, '; control (inverse inclusion fails) in', ctl, 'of 2000 contexts')
