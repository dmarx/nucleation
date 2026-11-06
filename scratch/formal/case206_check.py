# scratch/formal/case206_check.py
"""Independent re-check of CASE-206 (degree-4 vertex under a footprint budget).

Run: python3 -I scratch/formal/case206_check.py
Checks, with controls:
 1. closure R1 R2 R3 R4 = I for modes A and B (this vertex, and random
    flat-foldable vertices); control: a wrong coefficient fails.
 2. completeness: at fixed rho1, the closure has at most two solutions
    (spherical two-circle argument, verified by exhaustive root search);
    control: the search finds both modes.
 3. footprints of A, B, flat; shallow states; crossing of 1.5.
 4. max of footprint on each half-branch is at flat.
 5. acting classes and observing classes, and the agreement window,
    for both probe-cost orders.
"""
import itertools
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import brentq

D = np.pi / 180


def rot(axis, ang):
    a = axis / np.linalg.norm(axis)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


def creases(alpha, beta):
    th = np.cumsum([0, alpha, beta, np.pi - alpha])  # crease directions
    return [np.array([np.cos(t), np.sin(t), 0.0]) for t in th]


def modeA(r1, alpha, beta):
    k = np.sin((alpha + beta) / 2) / np.sin((alpha - beta) / 2)
    r2 = 2 * np.arctan(k * np.tan(r1 / 2))
    return np.array([r1, r2, -r1, r2])


def modeB(r1, alpha, beta):
    k = -np.cos((alpha + beta) / 2) / np.cos((alpha - beta) / 2)
    r2 = 2 * np.arctan(k * np.tan(r1 / 2))
    return np.array([r1, r2, r1, -r2])


def closure(rho, E):
    M = np.eye(3)
    for e, r in zip(E, rho):
        M = M @ rot(e, r)
    return np.abs(M - np.eye(3)).max()


def points(rho, E):
    R1 = rot(E[0], rho[0]); R2 = rot(E[1], rho[1])
    return np.array([[0, 0, 0], E[0], R1 @ E[1], R1 @ R2 @ E[2], E[3]])


def footprint(rho, E):
    P = points(rho, E)[:, :2]
    return ConvexHull(P).volume


al, be = 60 * D, 90 * D
E = creases(al, be)

# 1. closure
print("1. closure")
worst = 0
rng = np.random.default_rng(0)
for _ in range(2000):
    a = rng.uniform(0.05, np.pi - 0.05); b = rng.uniform(0.05, np.pi - 0.05)
    if abs(a - b) < 1e-3:
        continue
    Ee = creases(a, b)
    r1 = rng.uniform(-np.pi + 0.05, np.pi - 0.05)
    worst = max(worst, closure(modeA(r1, a, b), Ee), closure(modeB(r1, a, b), Ee))
print("  worst closure error, 2000 random vertices, both modes:", worst)
bad = modeA(0.7, al, be); bad[1] *= 1.1
print("  control (perturbed coefficient) closure error:", closure(bad, E))
A = np.array([-90, 150, 90, 150]) * D
B = np.array([150, -90, 150, 90]) * D
print("  A on mode A:", np.allclose(modeA(-90 * D, al, be), A), " closure", closure(A, E))
print("  B on mode B:", np.allclose(modeB(150 * D, al, be), B), " closure", closure(B, E))

# 2. completeness: solve closure for (r2, r3, r4) at fixed r1 from many starts
from scipy.optimize import least_squares
print("2. completeness at fixed rho1")
maxsol = 0
for r1 in np.linspace(-170, 170, 35) * D:
    sols = []
    for s in itertools.product(np.linspace(-160, 160, 5) * D, repeat=3):
        f = lambda x: (np.eye(3) - rot(E[0], r1) @ rot(E[1], x[0]) @ rot(E[2], x[1]) @ rot(E[3], x[2]))[np.triu_indices(3)]
        res = least_squares(f, s, bounds=(-np.pi, np.pi))
        if np.abs(res.fun).max() < 1e-9:
            x = (res.x + np.pi) % (2 * np.pi) - np.pi
            if not any(np.allclose(x, y, atol=1e-5) for y in sols):
                sols.append(x)
    known = [modeA(r1, al, be)[1:], modeB(r1, al, be)[1:]]
    for x in sols:
        assert any(np.allclose(x, k, atol=1e-5) for k in known), (r1 / D, x / D)
    maxsol = max(maxsol, len(sols))
    if abs(r1) > 1e-9:
        assert len(sols) == 2, (r1 / D, len(sols))
print("  every solution found is on mode A or B; max distinct per rho1:", maxsol)

# 3. footprints
print("3. footprints")
F = np.zeros(4)
print("  flat", footprint(F, E), " 1+sqrt3/2 =", 1 + np.sqrt(3) / 2)
print("  A", footprint(A, E), " B", footprint(B, E))
print("  A projected points", np.round(points(A, E)[:, :2], 6).tolist())
shA = np.array([-30, 90, 30, 90]) * D; shB = np.array([90, -30, 90, 30]) * D
print("  shallow A", footprint(shA, E), "closure", closure(shA, E))
print("  shallow B", footprint(shB, E), "closure", closure(shB, E))


def branch(mode, sign, t):
    """half-branch parametrised by its largest |fold| = t (deg), sign of largest fold."""
    # find r1 such that max fold angle magnitude = t, with sign
    f = modeA if mode == "A" else modeB
    def g(r1):
        rho = f(r1, al, be)
        return np.max(np.abs(rho)) - t * D
    # largest fold monotone in |r1|; search r1 in (0, pi) or (-pi,0)
    for s1 in (1, -1):
        try:
            r1 = brentq(g, s1 * 1e-9, s1 * (np.pi - 1e-9))
        except ValueError:
            continue
        rho = f(r1, al, be)
        if np.sign(rho[np.argmax(np.abs(rho))]) == sign:
            return rho
    raise RuntimeError


for mode in "AB":
    for sign in (1, -1):
        ts = np.linspace(0.01, 179.0, 4000)
        r = np.array([footprint(branch(mode, sign, t), E) for t in ts])
        x = brentq(lambda t: footprint(branch(mode, sign, t), E) - 1.5, 1, 179)
        rises = ts[1:][np.diff(r) > 1e-12]
        seg = (ts >= 90) & (ts <= 150)
        print(f"  mode {mode} side {sign:+d}: max r off flat {r.max():.6f} (< flat), "
              f"crosses 1.5 at {x:.3f} deg, first rise at {rises.min():.2f} deg, "
              f"r at 179 deg {r[-1]:.4f}, max r on [90, 150] {r[seg].max():.6f} "
              f"vs r(90) {footprint(branch(mode, sign, 90), E):.6f}")

# 5. acting and observing partitions on the nine states
print("5. frontiers")
states = {"F": F}
for mode in "AB":
    for sign in (1, -1):
        states[f"{mode}{sign:+d}s"] = branch(mode, sign, 90)
        states[f"{mode}{sign:+d}d"] = branch(mode, sign, 150)
names = list(states)
fp = {n: footprint(states[n], E) for n in names}
print("  footprints", {n: round(v, 4) for n, v in fp.items()})


def acting(a):
    # classes: same half-branch with shallow footprint <= a joins s,d; any to flat needs fp(F)
    cls = {n: n for n in names}
    for n in names:
        if n.endswith("d") and fp[n[:-1] + "s"] <= a + 1e-12:
            cls[n] = n[:-1] + "s"
    if fp["F"] <= a + 1e-12:
        cls = {n: "all" for n in names}
    return frozenset(frozenset(m for m in names if cls[m] == c) for c in set(cls.values()))


def probe(n, which):
    if which == "flat":
        return n == "F"
    if n == "F":
        return "F"
    if which == "mode":
        return n[0]
    if which == "side":
        return n[1:3]
    if which == "deep":
        return n[-1]


def observing(o, costs):
    bought = [p for p, c in costs.items() if c <= o]
    key = {n: tuple(probe(n, p) for p in bought) for n in names}
    return frozenset(frozenset(m for m in names if key[m] == key[n]) for n in names)


for costs in ({"flat": 1, "mode": 2, "side": 3, "deep": 4},
              {"flat": 1, "mode": 2, "deep": 3, "side": 4}):
    agree = []
    for o in [0, 1, 2, 3, 4]:
        for a in [0, 0.8, 1.0, 1.125, 1.5, 1.866026]:
            if observing(o, costs) == acting(a):
                agree.append((o, a, len(acting(a))))
    print("  costs", costs, "agree at (o, a, #classes):", agree)
print("  acting class counts:", [(a, len(acting(a))) for a in [0, 1.0, 1.125, 1.866026]])

# 6. self-intersection
print("6. self-intersection")
def faces(rho):
    R1=rot(E[0],rho[0]);R2=rot(E[1],rho[1]);R3=rot(E[2],rho[2])
    O=np.zeros(3);c1,c4=E[0],E[3];c2=R1@E[1];c3=R1@R2@E[2]
    return [(O,c1,c2),(O,c2,c3),(O,c3,c4),(O,c4,c1)]
def seg_tri(p,q,tri,eps=1e-9):
    a,b,c=tri; n=np.cross(b-a,c-a); dp=np.dot(p-a,n); dq=np.dot(q-a,n)
    if dp*dq>0 or abs(dp-dq)<1e-15: return False
    t=dp/(dp-dq); x=p+t*(q-p)
    if t<eps or t>1-eps: return False
    # barycentric
    v0,v1,v2=c-a,b-a,x-a
    d00,d01,d11,d20,d21=v0@v0,v0@v1,v1@v1,v2@v0,v2@v1
    den=d00*d11-d01*d01; v=(d11*d20-d01*d21)/den; w=(d00*d21-d01*d20)/den
    return v>eps and w>eps and v+w<1-eps
def hits(rho):
    F=faces(rho)
    for i,j in [(0,2),(1,3)]:
        for X,Y in [(F[i],F[j]),(F[j],F[i])]:
            O,p,q=X
            for s,t in [(O+1e-6*(p-O),p),(O+1e-6*(q-O),q),(p,q)]:
                if seg_tri(s,t,Y): return True
    return False
for mode in "AB":
    for sign in (1,-1):
        n=sum(hits(branch(mode,sign,t)) for t in np.linspace(0.5,179.5,1500))
        print("  mode",mode,"side",sign,"self-intersecting samples of 1500:",n)
# control: a non-closing 'state' far from a mode should be rejected by closure, and a known intersecting arrangement:
print("control hits on a deliberately crossed arrangement:", hits(np.array([170,-170,170,170])*D))
