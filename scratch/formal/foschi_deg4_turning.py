# scratch/formal/foschi_deg4_turning.py: for Example 1 of Foschi, Hull & Ku perturbed into an elliptic vertex, locate where the two rho1-branches of Eq. (6) join (turning points in rho4) and list the folding angles there; and where along each torus loop a folding angle passes +-pi.
"""Run: python3 -I foschi_deg4_turning.py
Control: for the developable Example 1 the join must be the double root at rho4 = 0
with all four folding angles 0 (the crossing at the flat state)."""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import foschi_deg4_check as F
import foschi_deg4_monodromy as Mo
PI = math.pi
ex1 = [PI/3, PI/2, 3*PI/4, 5*PI/12]
for name, al in (("developable Example 1 (CONTROL)", ex1),
                 ("elliptic, each alpha -0.05/(2pi)", [a - 0.05/(2*PI) for a in ex1]),
                 ("elliptic, each alpha -0.05", [a - 0.05 for a in ex1]),
                 ("hyperbolic, each alpha +0.05/(2pi)", [a + 0.05/(2*PI) for a in ex1])):
    M = 40000
    prev = None; joins = []
    for k in range(M + 1):
        r4 = -PI + 2*PI*k/M
        q, b = Mo.roots(al, r4)
        ok = abs(q) <= 1
        if prev is not None and ok != prev:
            joins.append(r4)
        prev = ok
    # double roots: |q| closest to 1
    best = min(((1 - abs(Mo.roots(al, -PI + 2*PI*k/20000)[0]), -PI + 2*PI*k/20000) for k in range(20001)))
    print(name)
    if joins:
        for r4 in joins:
            q, b = Mo.roots(al, r4)
            r1 = b + math.acos(max(-1, min(1, q)))
            rho = F.measure(F.build(al, r1, r4))
            print("   branches join at rho4=%+.4f: rho=(%s)" % (r4, ", ".join("%+.4f" % r for r in rho)))
    else:
        print("   no turning point; closest approach of the two roots 1-|q|=%.3g at rho4=%+.4f" % best)
    # where do folding angles pass +-pi along the curve(s)?
    crossings = []
    for sgn in (1, -1):
        last = None
        for k in range(M + 1):
            r4 = -PI + 2*PI*k/M
            q, b = Mo.roots(al, r4)
            if abs(q) > 1:
                last = None; continue
            r1 = b + sgn*math.acos(q)
            rho = F.measure(F.build(al, r1, r4))
            if last is not None:
                for i in range(4):
                    if abs(rho[i] - last[i]) > PI:  # jumped across +-pi
                        crossings.append((sgn, i + 1, r4))
            last = rho
    print("   crease angle passes +-pi (branch, crease, rho4): %s" % ", ".join("(%+d, e%d, %+.3f)" % c for c in crossings))
