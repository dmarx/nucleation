# scratch/formal/foschi_deg4_topology.py: where the two folding modes of a degree-4 vertex meet, and how many components the configuration space has, for Foschi, Hull & Ku (2022) Example 1 and random vertices; also locates the misprint in Eq. (4) and (A6).
"""
Uses the independent construction of foschi_deg4_check.py (imported from the same
directory).  The configuration space is the zero set of
    G(r1, r4) = c2(r1) . c3(r4) - cos(alpha2)
on the torus of (rho1, rho4), which fixes the whole state (rho2, rho3 follow).
A meeting point of two modes is a singular point of the zero set (G = 0 and
grad G = 0).  Components are counted by marching squares with 4-connectivity on a
periodic grid, and, separately, on the square with the seam rho = +-pi cut (the
paper's R^4 convention, rho_i in [-pi, pi]) where every crease angle rho1..rho4
must stay off +-pi.

Run:  python3 -I foschi_deg4_topology.py
"""
import math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import foschi_deg4_check as F  # noqa: E402

PI = math.pi

def Ggrid(al, N):
    a1, a2, a3, a4 = al
    ang = -PI + 2 * PI * (np.arange(N) + 0.5) / N
    c1 = F.plane(0.0); c4 = F.plane(-a4)
    e = F.plane(a1); epar = (e @ c1) * c1; eperp = e - epar; ex = np.cross(c1, e)
    f = F.plane(-a4 - a3); fpar = (f @ c4) * c4; fperp = f - fpar; fx = np.cross(c4, f)
    c2 = epar[None, :] + np.cos(ang)[:, None] * eperp[None, :] + np.sin(ang)[:, None] * ex[None, :]
    c3 = fpar[None, :] + np.cos(-ang)[:, None] * fperp[None, :] + np.sin(-ang)[:, None] * fx[None, :]
    return ang, c2 @ c3.T - math.cos(a2)

def label(on, wrap):
    N = on.shape[0]
    lab = -np.ones(on.shape, int); n = 0
    for i in range(N):
        for j in range(N):
            if on[i, j] and lab[i, j] < 0:
                st = [(i, j)]; lab[i, j] = n
                while st:
                    a, b = st.pop()
                    for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        p, q = a + da, b + db
                        if wrap:
                            p %= N; q %= N
                        elif not (0 <= p < N and 0 <= q < N):
                            continue
                        if on[p, q] and lab[p, q] < 0:
                            lab[p, q] = n; st.append((p, q))
                n += 1
    return n, lab

def analyse(name, al, N=1200):
    ang, g = Ggrid(al, N)
    s = np.sign(g)
    on = np.zeros_like(g, bool)
    for di in (0, 1):
        for dj in (0, 1):
            on |= (np.roll(np.roll(s, -di, 0), -dj, 1) != s)
    ntor, labt = label(on, True)
    # cut convention: drop cells where any rho is within 0.02 of +-pi
    cut = on.copy()
    idx = np.argwhere(on)
    nearpi = 0
    for (i, j) in idx:
        r1, r4 = ang[i], ang[j]
        c = F.build(al, r1, r4)
        rho = F.measure(c)
        if min(abs(abs(r) - PI) for r in rho) < 0.02:
            cut[i, j] = False; nearpi += 1
    ncut, labc = label(cut, False)
    # singular points: curve cells with smallest |grad G|
    gi = (np.roll(g, -1, 0) - np.roll(g, 1, 0)) / 2
    gj = (np.roll(g, -1, 1) - np.roll(g, 1, 1)) / 2
    gn = np.hypot(gi, gj) * N / (2 * PI)
    cand = sorted(((gn[i, j], ang[i], ang[j]) for (i, j) in idx), key=lambda t: t[0])
    sing = []
    for v, r1, r4 in cand:
        if v > 0.05:
            break
        if all(math.hypot(r1 - a, r4 - b) > 0.2 for _, a, b in sing):
            sing.append((v, r1, r4))
    comp_sizes = sorted(np.bincount(labt[labt >= 0]).tolist(), reverse=True)
    print("%s\n   alpha=%s sum-2pi=%+.4f" % (name, ["%.4f" % a for a in al], sum(al) - 2 * PI))
    print("   torus components: %d (cells %s); with rho=+-pi seam cut: %d" % (ntor, comp_sizes, ncut))
    for v, r1, r4 in sing:
        rho = F.measure(F.build(al, r1, r4))
        print("   near-singular point |grad|=%.3g at rho=(%s)" % (v, ", ".join("%+.3f" % r for r in rho)))
    if not sing:
        print("   no singular point (min |grad G| on curve %.3g)" % (cand[0][0] if cand else float('nan')))
    return ntor

print("\n==== TOPOLOGY ====")
ex1 = [PI / 3, PI / 2, 3 * PI / 4, 5 * PI / 12]
analyse("Example 1 developable", ex1)
for d in (0.05 / (2 * PI), 0.02, 0.05):
    analyse("Example 1, each alpha %+.4f (elliptic)" % -d, [a - d for a in ex1])
    analyse("Example 1, each alpha %+.4f (hyperbolic)" % d, [a + d for a in ex1])
analyse("flat-foldable (0.7, 1.1, pi-0.7, pi-1.1)", [0.7, 1.1, PI - 0.7, PI - 1.1])
analyse("table vertex", [5 * PI / 8, 5 * PI / 8, PI / 2, 3 * PI / 4])
analyse("CONTROL bird's foot elliptic (pi/4,pi/4,pi/3,pi/3)", [PI / 4, PI / 4, PI / 3, PI / 3])

print("\n==== RANDOM ====")
import random
rr = random.Random(7)
counts = {"ell": [], "hyp": [], "dev": []}
for kind in ("dev", "ell", "hyp"):
    for _ in range(10):
        F.rng = rr
        al = F.rand_alpha(kind)
        counts[kind].append(analyse("random %s" % kind, al, N=700))
print("counts:", counts)
