# scratch/studies/contextual-self/triangle.py
"""A contextual self: three role contexts, pairwise consistent, no global presentation.

Each context (work W, family F, friends R) fixes a person's stance on one
shared trait, a bit. Each meeting occasion (an overlap of two contexts)
imposes a constraint the joint presentation there must meet. Check:
(1) every overlap, taken alone, is satisfiable;
(2) every pair of contexts glues (CLAIM-153: two consistent contexts glue);
(3) no assignment satisfies all three overlaps (the obstruction is the cycle);
(4) removing any one overlap (keeping one pair of audiences apart) restores
    a global assignment, with no role changed.
"""
from itertools import product

C = ["W", "F", "R"]
# overlap constraints: same stance at W∩F and F∩R, opposite at R∩W (a parity cycle)
overlaps = {("W", "F"): lambda a, b: a == b,
            ("F", "R"): lambda a, b: a == b,
            ("R", "W"): lambda a, b: a != b}

def ok(assign, ovs):
    return all(f(assign[x], assign[y]) for (x, y), f in ovs.items())

each = {k: any(f(a, b) for a, b in product([0, 1], repeat=2)) for k, f in overlaps.items()}
print("(1) each overlap satisfiable:", all(each.values()))
pairs = all(any(ok(dict(zip(C, v)), {k: f}) for v in product([0, 1], repeat=3)) for k, f in overlaps.items())
print("(2) each pair of contexts glues:", pairs)
glob = [v for v in product([0, 1], repeat=3) if ok(dict(zip(C, v)), overlaps)]
print("(3) global presentations satisfying the whole cycle:", glob)
for cut in overlaps:
    rest = {k: f for k, f in overlaps.items() if k != cut}
    sols = [v for v in product([0, 1], repeat=3) if ok(dict(zip(C, v)), rest)]
    print(f"(4) keep {cut} apart -> {len(sols)} global presentations, e.g. {dict(zip(C, sols[0]))}")
