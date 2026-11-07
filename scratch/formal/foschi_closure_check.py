# scratch/formal/foschi_closure_check.py: checks the closure condition Foschi, Hull & Ku state in Sec. II (prod R(e_i, rho_i) = I, cited to belcastro & Hull 2002) on independently built developable states, and that the rotations do not commute; control: a wrong fold angle must break it.
"""Creases e_i are the FLAT directions (angles 0, a1, a1+a2, a1+a2+a3); rho_i are the
angles measured by foschi_deg4_check.measure on a built folded state.  For a
non-developable vertex there are no flat crease directions to rotate about, so
the product in this form is not defined there.  Run: python3 -I foschi_closure_check.py"""
import math, sys, os, random, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import foschi_deg4_check as F
F.rng = random.Random(3)
worst = {}; ctl = 1e9; comm = 1e9
for _ in range(30):
    al = F.rand_alpha("dev")
    phis = [0, al[0], al[0] + al[1], al[0] + al[1] + al[2]]
    e = [F.plane(p) for p in phis]
    for rho in F.sample(al, 20):
        for order, sgn in itertools.product(("1234", "4321"), (1, -1)):
            idx = [int(c) - 1 for c in order]
            P = np.eye(3)
            for i in idx:
                P = P @ F.rot(e[i], sgn * rho[i])
            worst[(order, sgn)] = max(worst.get((order, sgn), 0), np.abs(P - np.eye(3)).max())
        best = min(worst, key=worst.get)
        idx = [int(c) - 1 for c in best[0]]
        P = np.eye(3); bad = list(rho); bad[0] += 0.05
        for i in idx:
            P = P @ F.rot(e[i], best[1] * bad[i])
        ctl = min(ctl, np.abs(P - np.eye(3)).max())
        A, B = F.rot(e[0], rho[0]), F.rot(e[1], rho[1])
        comm = min(comm, np.abs(A @ B - B @ A).max())
for k, v in sorted(worst.items(), key=lambda t: t[1]):
    print("order %s, sign %+d: max |prod - I| = %.2e" % (k[0], k[1], v))
print("CONTROL rho1 + 0.05: min over states of max |prod - I| = %.2e (should be >> 0)" % ctl)
print("min over states of max |R1 R2 - R2 R1| = %.2e (non-commuting)" % comm)
