# scratch/formal/foschi_deg4_monodromy.py: robust (grid-free) count of the components of a degree-4 vertex's configuration space on the torus, by following the two rho1-roots once round the rho4-circle; checks the grid counts of foschi_deg4_topology.py.
"""
For each rho4 the rigid states are the roots r1 of a*cos r1 + b*sin r1 + d = cos a2:
two roots (base +- delta), one double root, or none.  If both roots exist for
every rho4, the configuration space is a double cover of the rho4-circle: two
loops if following one root once round returns to the same root, one loop if it
returns to the other (monodromy).  If roots vanish on some rho4 intervals, the two
roots join at the interval ends (turning points) and each maximal interval with
roots carries one loop.  Controls: the developable Example 1 must show the double
root at rho4 = 0 (the crossing at the flat state); the elliptic bird's foot of
Fig. 7 must be reported with its crossing too.
Run:  python3 -I foschi_deg4_monodromy.py
"""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import foschi_deg4_check as F
PI = math.pi

def roots(al, r4):
    a1, a2, a3, a4 = al
    import numpy as np
    c1 = F.plane(0.0); c4 = F.plane(-a4)
    c3 = F.rot(c4, -r4) @ F.plane(-a4 - a3)
    e = F.plane(a1); epar = (e @ c1) * c1; eperp = e - epar; ex = np.cross(c1, e)
    A, B, D = float(eperp @ c3), float(ex @ c3), float(epar @ c3)
    R = math.hypot(A, B); rhs = math.cos(a2) - D
    q = rhs / R  # roots exist iff |q| <= 1
    base = math.atan2(B, A)
    return q, base

def wrap(x):
    return (x + PI) % (2 * PI) - PI

def count(al, M=200000):
    qs = []; bs = []
    for k in range(M):
        r4 = -PI + 2 * PI * k / M
        q, b = roots(al, r4); qs.append(q); bs.append(b)
    ok = [abs(q) <= 1 for q in qs]
    minmargin = min(1 - abs(q) for q in qs)
    if all(ok):
        # follow root base + acos(q) continuously round the circle
        cur = wrap(bs[0] + math.acos(qs[0]))
        start_plus = cur
        for k in range(1, M + 1):
            q, b = qs[k % M], bs[k % M]
            d = math.acos(q)
            c1, c2 = wrap(b + d), wrap(b - d)
            cur = c1 if abs(wrap(c1 - cur)) <= abs(wrap(c2 - cur)) else c2
        same = abs(wrap(cur - start_plus)) < 1e-3
        return (2 if same else 1), "roots for every rho4 (min margin %.3g); monodromy %s" % (minmargin, "trivial" if same else "swaps the roots")
    # count maximal intervals (cyclic) with roots
    n = 0
    for k in range(M):
        if ok[k] and not ok[k - 1]:
            n += 1
    return n, "roots vanish on part of the rho4-circle; %d interval(s) with roots, one loop each" % n

def main():
    cases = [
        ("Example 1 developable", [PI/3, PI/2, 3*PI/4, 5*PI/12]),
    ]
    ex1 = cases[0][1]
    for d in (0.05/(2*PI), 0.02, 0.05, 0.1):
        cases.append(("Example 1, each alpha -%.4f (elliptic)" % d, [a - d for a in ex1]))
        cases.append(("Example 1, each alpha +%.4f (hyperbolic)" % d, [a + d for a in ex1]))
    cases += [
        ("Example 1, alpha_1 only -0.05 (elliptic)", [ex1[0]-0.05] + ex1[1:]),
        ("Example 1, alpha_1 only +0.05 (hyperbolic)", [ex1[0]+0.05] + ex1[1:]),
        ("table vertex (hyperbolic)", [5*PI/8, 5*PI/8, PI/2, 3*PI/4]),
        ("CONTROL elliptic bird's foot (pi/4,pi/4,pi/3,pi/3)", [PI/4, PI/4, PI/3, PI/3]),
        ("CONTROL hyperbolic bird's foot (2pi/3,2pi/3,3pi/4,3pi/4)", [2*PI/3, 2*PI/3, 3*PI/4, 3*PI/4]),
        ("square-twist pouch theta=60deg (developable)", [PI/3, PI/2 - PI/12, 3*PI/4, PI/2]),
    ]
    for name, al in cases:
        n, why = count(al)
        print("%-58s sum-2pi=%+.4f  components on torus: %d  (%s)" % (name, sum(al) - 2*PI, n, why))

    import random
    F.rng = random.Random(11)
    for kind in ("ell", "hyp"):
        res = [count(F.rand_alpha(kind), 40000)[0] for _ in range(40)]
        print("random %s, 40 vertices: components %s -> {0:%d, 1:%d, 2:%d}" % (kind, res, res.count(0), res.count(1), res.count(2)))


if __name__ == "__main__":
    main()
