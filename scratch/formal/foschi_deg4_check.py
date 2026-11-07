# scratch/formal/foschi_deg4_check.py: numerical check of Foschi, Hull & Ku (2022, arXiv 2206.12691v2) Theorems 1-3, Eqs. (4)-(6), (A6), (3), (10), and the two-mode / disconnection claims, against an independent spherical-linkage construction of degree-4 vertices.
"""
Independent construction.  Crease directions c1..c4 are unit vectors; sector
alpha_i lies between c_i and c_{i+1} (indices mod 4), so crease e_i lies between
sectors alpha_{i-1} and alpha_i, as in the paper.  The sector alpha_4 (c4-c1) is
held in the xy-plane; c2 is c1's neighbour rotated about c1 by r1; c3 is c4's
neighbour rotated about c4 by r4.  A state is rigid iff angle(c2, c3) = alpha_2.

Folding angles are then MEASURED from the four vectors alone, by one uniform
signed-dihedral rule at every crease (rho = 0 when the two sectors at a crease are
coplanar and on opposite sides).  The paper's equations are never used to build
states; they are only evaluated on the measured angles.  A global sign flip of all
rho (mirror image) leaves every equation tested invariant, so the valley/mountain
sign convention cannot matter, but a per-crease inconsistency would.

Run:  python3 -I foschi_deg4_check.py
"""
import math, random
import numpy as np

rng = random.Random(20261106)

def rot(axis, ang):
    a = axis / np.linalg.norm(axis)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + math.sin(ang) * K + (1 - math.cos(ang)) * K @ K

def plane(phi):
    return np.array([math.cos(phi), math.sin(phi), 0.0])

def build(al, r1, r4):
    a1, a2, a3, a4 = al
    c1 = plane(0.0)
    c4 = plane(-a4)
    c2 = rot(c1, r1) @ plane(a1)
    c3 = rot(c4, -r4) @ plane(-a4 - a3)
    return [c1, c2, c3, c4]

def gap(al, r1, r4):
    c = build(al, r1, r4)
    return float(c[1] @ c[2]) - math.cos(al[1])

def measure(c):
    """signed folding angle at each crease, uniform rule"""
    rho = []
    for i in range(4):
        ci, p, n = c[i], c[i - 1], c[(i + 1) % 4]
        u = p - (p @ ci) * ci
        w = n - (n @ ci) * ci
        phi = math.atan2(float(ci @ np.cross(u, w)), float(u @ w))
        r = phi - math.pi
        r = (r + math.pi) % (2 * math.pi) - math.pi
        rho.append(r)
    return rho

def states(al, r4):
    """all rigid states with r4 given: solve a*cos r1 + b*sin r1 + d = cos a2"""
    a1, a2, a3, a4 = al
    c1 = plane(0.0)
    c4 = plane(-a4)
    c3 = rot(c4, -r4) @ plane(-a4 - a3)
    e = plane(a1)
    # rot(c1,r1) e = e_par + cos r1 e_perp + sin r1 (c1 x e)
    epar = (e @ c1) * c1
    eperp = e - epar
    ex = np.cross(c1, e)
    A, B, D = float(eperp @ c3), float(ex @ c3), float(epar @ c3)
    R = math.hypot(A, B)
    rhs = math.cos(a2) - D
    if R < 1e-14 or abs(rhs) > R:
        return []
    base = math.atan2(B, A)
    d = math.acos(max(-1.0, min(1.0, rhs / R)))
    out = []
    for r1 in (base + d, base - d):
        c = build(al, r1, r4)
        assert abs(float(c[1] @ c[2]) - math.cos(a2)) < 1e-9
        out.append(c)
    return out

T = lambda r: math.tan(r / 2)
C, S = math.cos, math.sin

def eq4_resid(al, rho, i):
    """Theorem 2, Eq. (4), opposite angles, cross-multiplied"""
    a = lambda k: al[k % 4]
    t2 = T(rho[(i + 2) % 4]) ** 2
    num = (1 + t2) * C(a(i - 1) + a(i)) + t2 * C(a(i + 1) - a(i + 2)) + C(a(i + 1) + a(i + 2))
    den = (1 + t2) * C(a(i - 1) - a(i)) - t2 * C(a(i + 1) - a(i + 2)) - C(a(i + 1) + a(i + 2))
    return T(rho[i]) ** 2 * den + num

def eq5_resid(al, rho, i, variant="printed"):
    """Theorem 2, Eq. (5), adjacent angles rho_i, rho_{i+1}"""
    a = lambda k: al[k % 4]
    x, y = T(rho[i]), T(rho[(i + 1) % 4])
    X, Y = x * x, y * y
    lhs = C(a(i + 2)) * (1 + X) * (1 + Y)
    if variant == "printed":
        rhs = (C(a(i + 1) - a(i) - a(i - 1)) * Y + C(a(i + 1) + a(i) - a(i - 1)) * X
               + C(a(i + 1) - a(i) + a(i - 1)) * X * Y + C(a(i + 1) + a(i) + a(i - 1))
               + 4 * S(a(i + 1)) * S(a(i - 1)) * x * y)
    elif variant == "control_sign":  # CONTROL: flip the sign of the cross term
        rhs = (C(a(i + 1) - a(i) - a(i - 1)) * Y + C(a(i + 1) + a(i) - a(i - 1)) * X
               + C(a(i + 1) - a(i) + a(i - 1)) * X * Y + C(a(i + 1) + a(i) + a(i - 1))
               - 4 * S(a(i + 1)) * S(a(i - 1)) * x * y)
    elif variant == "control_swapXY":  # CONTROL: swap the X and Y coefficients
        rhs = (C(a(i + 1) - a(i) - a(i - 1)) * X + C(a(i + 1) + a(i) - a(i - 1)) * Y
               + C(a(i + 1) - a(i) + a(i - 1)) * X * Y + C(a(i + 1) + a(i) + a(i - 1))
               + 4 * S(a(i + 1)) * S(a(i - 1)) * x * y)
    return lhs - rhs

def a6_resid(al, rho):
    """Appendix Eq. (A6) as printed: x = tan(rho4/2), y = tan(rho1/2)"""
    a1, a2, a3, a4 = al
    x, y = T(rho[3]), T(rho[0])
    return (C(a1 + a3 + a4) + x * x * C(a1 - a3 - a4) + x * x * y * y * C(a1 + a3 - a4)
            + y * y * C(a1 - a3 + a4) + 4 * x * y * S(a1) * S(a3) - (1 + x * x) * (1 + y * y) * C(a2))

def eq6_both(al, rho):
    """Eq. (6): tan(rho1/2) from tan(rho4/2), both signs; return min |error| in atan form"""
    a1, a2, a3, a4 = al
    x = T(rho[3])
    D = C(a2) - C(a1 - a3 - a4) + (C(a2) - C(a1 + a3 - a4)) * x * x
    E = C(a2) - C(a1 + a3 + a4) + (C(a2) - C(a1 - a3 + a4)) * x * x
    disc = 4 * S(a1) ** 2 * S(a3) ** 2 * x * x - D * E
    if disc < 0 or abs(D) < 1e-12:
        return None
    cands = [(2 * S(a1) * S(a3) * x + s * math.sqrt(disc)) / D for s in (1, -1)]
    y = T(rho[0])
    # compare as angles to be safe near infinity
    return min(abs(math.atan(cv) - math.atan(y)) for cv in cands)

def huffman3(al, rho, i):
    a = lambda k: al[k % 4]
    return S(rho[i] / 2) ** 2 * S(a(i)) * S(a(i + 3)) - S(a(i + 1)) * S(a(i + 2)) * S(rho[(i + 2) % 4] / 2) ** 2

def thm3(al, rho, i):
    a = lambda k: al[k % 4]
    r1 = S(a(i + 1)) * S(a(i + 2)) / T(rho[i]) ** 2 + C(a(i + 1) - a(i + 2)) / 2 \
        - S(a(i - 1)) * S(a(i)) / T(rho[(i + 2) % 4]) ** 2 - C(a(i - 1) - a(i)) / 2
    r2 = S(a(i + 1) + a(i + 2)) / T(rho[i]) - S(a(i)) / T(rho[(i - 1) % 4]) - S(a(i - 1)) / T(rho[(i + 1) % 4])
    return r1, r2

def rand_alpha(kind):
    while True:
        al = [rng.uniform(0.15, math.pi - 0.15) for _ in range(4)]
        s = sum(al)
        if kind == "dev":
            al = [a * 2 * math.pi / s for a in al]
            if all(0.05 < a < math.pi - 0.05 for a in al):
                return al
        elif kind == "ell" and s < 2 * math.pi - 0.1:
            return al
        elif kind == "hyp" and s > 2 * math.pi + 0.1:
            return al

def sample(al, n=60):
    out = []
    for _ in range(n):
        r4 = rng.uniform(-math.pi, math.pi)
        for c in states(al, r4):
            rho = measure(c)
            if min(abs(abs(r) - math.pi) for r in rho) > 1e-3 and min(abs(r) for r in rho) > 1e-3:
                out.append(rho)
    return out

def scale(al):
    return 1.0

def main():
    print("== 0. the measured rho1, rho4 agree with the construction's r1, r4 (orientation check)")
    al = rand_alpha("dev")
    for _ in range(5):
        r4 = rng.uniform(-3, 3)
        for c in states(al, r4):
            m = measure(c)
            print("   r4=%+.4f  measured rho4=%+.4f" % (r4, m[3]))

    def run(kind, nvert=40):
        worst = {"eq4": 0, "eq5": 0, "A6": 0, "eq6": 0, "huff": 0, "thm3a": 0, "thm3b": 0,
                 "ctl_sign": float("inf"), "ctl_swap": float("inf"), "ctl_perturb": float("inf")}
        nst = 0
        for _ in range(nvert):
            al = rand_alpha(kind)
            sts = sample(al)
            ctl_sign = ctl_swap = ctl_pert = 0.0
            alp = [al[0] + 0.02] + al[1:]
            for rho in sts:
                nst += 1
                worst["eq4"] = max(worst["eq4"], max(abs(eq4_resid(al, rho, i)) / (1 + T(rho[i]) ** 2) / (1 + T(rho[(i + 2) % 4]) ** 2) for i in range(4)))
                worst["eq5"] = max(worst["eq5"], max(abs(eq5_resid(al, rho, i)) / (1 + T(rho[i]) ** 2) / (1 + T(rho[(i + 1) % 4]) ** 2) for i in range(4)))
                worst["A6"] = max(worst["A6"], abs(a6_resid(al, rho)) / (1 + T(rho[3]) ** 2) / (1 + T(rho[0]) ** 2))
                e6 = eq6_both(al, rho)
                if e6 is not None:
                    worst["eq6"] = max(worst["eq6"], e6)
                ctl_sign = max(ctl_sign, max(abs(eq5_resid(al, rho, i, "control_sign")) / (1 + T(rho[i]) ** 2) / (1 + T(rho[(i + 1) % 4]) ** 2) for i in range(4)))
                ctl_swap = max(ctl_swap, max(abs(eq5_resid(al, rho, i, "control_swapXY")) / (1 + T(rho[i]) ** 2) / (1 + T(rho[(i + 1) % 4]) ** 2) for i in range(4)))
                ctl_pert = max(ctl_pert, max(abs(eq4_resid(alp, rho, i)) / (1 + T(rho[i]) ** 2) / (1 + T(rho[(i + 2) % 4]) ** 2) for i in range(4)))
                if kind == "dev":
                    worst["huff"] = max(worst["huff"], max(abs(huffman3(al, rho, i)) for i in range(4)))
                    for i in range(4):
                        a, b = thm3(al, rho, i)
                        sc = 1 + max(1 / T(r) ** 2 for r in rho)
                        worst["thm3a"] = max(worst["thm3a"], abs(a) / sc)
                        worst["thm3b"] = max(worst["thm3b"], abs(b) / math.sqrt(sc))
            if sts:
                worst["ctl_sign"] = min(worst["ctl_sign"], ctl_sign)
                worst["ctl_swap"] = min(worst["ctl_swap"], ctl_swap)
                worst["ctl_perturb"] = min(worst["ctl_perturb"], ctl_pert)
        print("== %s: %d vertices, %d states" % (kind, nvert, nst))
        for k, v in worst.items():
            tag = "(CONTROL: per-vertex max should be >> 0; min over vertices shown)" if k.startswith("ctl") else "(max residual, should be ~0)"
            print("   %-12s %.3e  %s" % (k, v, tag))

    for kind in ("dev", "ell", "hyp"):
        run(kind)

    print("== 1. Theorem 1 (flat-foldable), and the table and pouch examples")
    # flat-foldable: a1 - a2 + a3 - a4 = 0, labelled a1 <= a2 < a3, a4 ; a3 = pi - a1, a4 = pi - a2
    a1, a2 = 0.7, 1.1
    al = [a1, a2, math.pi - a1, math.pi - a2]
    w1 = w2 = 0
    for rho in sample(al, 200):
        m1 = abs(rho[0] - rho[2]) < 1e-6 and abs(rho[1] + rho[3]) < 1e-6
        m2 = abs(rho[0] + rho[2]) < 1e-6 and abs(rho[1] - rho[3]) < 1e-6
        assert m1 or m2, rho
        if m1:
            w1 = max(w1, abs(T(rho[1]) + C((a1 + a2) / 2) / C((a1 - a2) / 2) * T(rho[0])) / (1 + abs(T(rho[1]))))
        if m2:
            w2 = max(w2, abs(T(rho[0]) - S((a1 - a2) / 2) / S((a1 + a2) / 2) * T(rho[1])) / (1 + abs(T(rho[0]))))
    print("   Thm 1 mode (1) max resid %.2e ; mode (2) max resid %.2e" % (w1, w2))

    al = [5 * math.pi / 8, 5 * math.pi / 8, math.pi / 2, 3 * math.pi / 4]
    w = 0
    for rho in sample(al, 200):
        w = max(w, abs(T(rho[1]) ** 2 - 2 * math.sqrt(2) / (2 + math.sqrt(2) * C(rho[3])) * S(rho[3] / 2) ** 2))
    print("   table Eq. (10) max resid %.2e" % w)

    for th_deg in (50, 60, 70, 80):
        th = math.radians(th_deg)
        al = [th, math.pi / 2 - (th - math.pi / 4), 3 * math.pi / 4, math.pi / 2]
        # find states with rho1 = rho4 by scanning rho4
        hits = []
        for k in range(20001):
            r4 = -math.pi + 2 * math.pi * k / 20000
            for c in states(al, r4):
                rho = measure(c)
                hits.append((abs(rho[0] - rho[3]), rho[3]))
        hits.sort()
        # cluster distinct roots
        roots = []
        for d, r in hits:
            if d < 2e-3 and all(abs(r - q) > 0.05 for q in roots):
                roots.append(r)
        pred = math.pi - math.acos(1 / math.tan(th))
        print("   pouch theta=%d deg: rho1=rho4 at rho4 = %s ; paper: 0, +-%.4f" % (th_deg, ", ".join("%+.4f" % r for r in sorted(roots)), pred))

    print("== 2. topology of the configuration space on the torus (rho1, rho4)")

    def components(al, N=900):
        g = np.empty((N, N))
        ang = [-math.pi + 2 * math.pi * k / N for k in range(N)]
        for i, r1 in enumerate(ang):
            for j, r4 in enumerate(ang):
                g[i, j] = gap(al, r1, r4)
        # cell (i,j) is on the curve if g changes sign on its 4 corners (periodic)
        on = np.zeros((N, N), bool)
        for i in range(N):
            for j in range(N):
                v = [g[i, j], g[(i + 1) % N, j], g[i, (j + 1) % N], g[(i + 1) % N, (j + 1) % N]]
                on[i, j] = min(v) <= 0 <= max(v)
        lab = -np.ones((N, N), int)
        n = 0
        for i in range(N):
            for j in range(N):
                if on[i, j] and lab[i, j] < 0:
                    stack = [(i, j)]
                    lab[i, j] = n
                    while stack:
                        a, b = stack.pop()
                        for da in (-1, 0, 1):
                            for db in (-1, 0, 1):
                                p, q = (a + da) % N, (b + db) % N
                                if on[p, q] and lab[p, q] < 0:
                                    lab[p, q] = n
                                    stack.append((p, q))
                    n += 1
        # does a component contain the unfolded point?
        z = N // 2
        return n, lab[z, z] >= 0

    for name, al in [
        ("paper Ex.1 developable (pi/3, pi/2, 3pi/4, 5pi/12)", [math.pi / 3, math.pi / 2, 3 * math.pi / 4, 5 * math.pi / 12]),
        ("Ex.1 perturbed elliptic, each alpha -0.05", [math.pi / 3 - .05, math.pi / 2 - .05, 3 * math.pi / 4 - .05, 5 * math.pi / 12 - .05]),
        ("Ex.1 perturbed hyperbolic, each alpha +0.05", [math.pi / 3 + .05, math.pi / 2 + .05, 3 * math.pi / 4 + .05, 5 * math.pi / 12 + .05]),
        ("table vertex (5pi/8, 5pi/8, pi/2, 3pi/4), hyperbolic", [5 * math.pi / 8, 5 * math.pi / 8, math.pi / 2, 3 * math.pi / 4]),
    ]:
        n, z = components(al, 600)
        print("   %-55s components on torus: %d ; curve through (0,0): %s" % (name, n, z))

    print("   random vertices (N=400 grid):")
    tally = {}
    for kind in ("dev", "ell", "hyp"):
        for _ in range(12):
            al = rand_alpha(kind)
            n, z = components(al, 400)
            tally.setdefault(kind, []).append(n)
        print("   %s: component counts %s" % (kind, tally[kind]))


if __name__ == "__main__":
    main()
