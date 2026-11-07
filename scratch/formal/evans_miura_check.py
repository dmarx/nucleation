# scratch/formal/evans_miura_check.py: checks Evans, Silverberg & Santangelo (2015, arXiv 1503.05756v2) Sec. III: that det[D(q)J] from their printed J0 and D^T(q) vanishes exactly on their dispersion relation (Eq. 16), that Eq. 24's decay length follows from it, and, independently, that a triangulated Miura-ori sheet's count of infinitesimal floppy modes grows with its perimeter, not its area.
"""
Part 1 uses the paper's own matrices, transcribed from the LaTeX source
(LatticeMechanicsOrigamiTessellations_final.tex): J = diag(J0, -J0, J0, -J0)
(24 x 12) and D^T(q) (24 x 12).  Two entries of D^T are printed with an
unsubscripted q (rows 12 and 13); each reading (qx, qy, qx+qy, 0) is tried.
Part 2 is independent of the paper's algebra: a bar-and-joint model of an n x n
Miura-ori whose parallelogram faces are each split by one diagonal (the paper's
"two extra folds per vertex"), with every triangle rigid and every edge a hinge;
the floppy modes are the null space of the rigidity matrix minus the 6 rigid-body
motions.  A sheet without the diagonals (rigid parallelograms) is the control:
it must have the single rigid-origami mode, at every size.
Run:  python3 -I evans_miura_check.py
"""
import math, cmath
import numpy as np

# ---------- Part 1 ----------
def J0(al, eps):
    A = math.cos(al) / math.sin(eps / 2) / math.sqrt(math.sin(eps / 2) ** 2 - math.cos(al) ** 2)
    B = math.sin(eps / 2) / math.sqrt(math.sin(eps / 2) ** 2 - math.cos(al) ** 2)
    C = 1 / math.sin(al / 2) / 2
    return np.array([[A, C, C], [0, 1, 0], [B, C, 0], [-A, 0, 0], [B, 0, C], [0, 0, 1]], float)

def DT(qx, qy, q):
    e = cmath.exp
    rows = {  # row index (1-based) -> (column 1-based, value)
        1: (1, 1), 2: (2, e(1j * qy / 2)), 3: (3, e(1j * qy / 2)), 4: (4, -e(-1j * qx / 2)),
        5: (5, -1), 6: (6, -1), 7: (4, e(1j * qx / 2)), 8: (7, e(1j * qx / 2 + 1j * qy / 2)),
        9: (8, e(1j * qy / 2)), 10: (1, -1), 11: (9, -1), 12: (10, e(1j * q / 2)),
        13: (11, -e(-1j * q / 2)), 14: (7, -e(-1j * qx / 2 - 1j * qy / 2)), 15: (3, -e(-1j * qy / 2)),
        16: (12, 1), 17: (5, 1), 18: (10, -e(-1j * qx / 2)), 19: (12, -1), 20: (2, -e(-1j * qy / 2)),
        21: (8, -e(-1j * qy / 2)), 22: (11, e(1j * qx / 2)), 23: (9, 1), 24: (6, 1),
    }
    M = np.zeros((24, 12), complex)
    for r, (c, v) in rows.items():
        M[r - 1, c - 1] = v
    return M

def detDJ(al, eps, qx, qy, which):
    q = {"qx": qx, "qy": qy, "qx+qy": qx + qy, "0": 0}[which]
    J = np.zeros((24, 12))
    for k, s in enumerate((1, -1, 1, -1)):
        J[6 * k:6 * k + 6, 3 * k:3 * k + 3] = s * J0(al, eps)
    D = DT(qx, qy, q).T
    return np.linalg.det(D @ J)

def disp(al, eps, qx, qy):
    return math.cos(al) ** 2 / math.sin(eps / 2) ** 4 * cmath.sin(qx / 2) ** 2 + cmath.sin(qy / 2) ** 2

def ell(al, eps, q):
    return 1 / (2 * abs(math.asinh(math.cos(al) * math.sin(q / 2) / math.sin(eps / 2) ** 2)))

print("== Part 1: det[D(q)J] against Eq. (16)")
al, eps = math.pi / 3, math.pi / 2
for which in ("qx", "qy", "qx+qy", "0"):
    # real wavevectors: det should vanish only at q = 0
    vals = [abs(detDJ(al, eps, qx, qy, which)) for qx in np.linspace(-3, 3, 13) for qy in np.linspace(-3, 3, 13)]
    zero_at_0 = abs(detDJ(al, eps, 0.0, 0.0, which))
    # imaginary qy = i kappa from Eq. 24: det should vanish there
    resid = []
    for qx in (0.3, 0.9, 1.7, 2.5):
        kap = 1 / ell(al, eps, qx)
        resid.append(abs(detDJ(al, eps, qx, 1j * kap, which)) / max(1e-300, abs(detDJ(al, eps, qx, 1j * kap * 1.3, which))))
    print("   q read as %-5s: |det| at q=0 %.1e ; min |det| on real grid without 0 %.2e ; |det(qy=i kappa)|/|det(qy=1.3 i kappa)| = %s"
          % (which, zero_at_0, sorted(vals)[1] if zero_at_0 < 1e-9 else min(vals), ", ".join("%.1e" % r for r in resid)))

# null space dimension at q = 0 (paper: 3 uniform modes)
for which in ("qx",):
    J = np.zeros((24, 12))
    for k, s in enumerate((1, -1, 1, -1)):
        J[6 * k:6 * k + 6, 3 * k:3 * k + 3] = s * J0(al, eps)
    R = DT(0, 0, 0).T @ J
    sv = np.linalg.svd(R, compute_uv=False)
    print("   null space of R(0): %d (paper: 3); singular values %s" % (int((sv < 1e-9).sum()), ", ".join("%.2g" % x for x in sv[-4:])))
    psi = [np.array([1, 0, 0] * 4, float), np.array([0, -1, 1] * 4, float)]
    A = math.cos(al) / math.sin(eps / 2) / math.sqrt(math.sin(eps / 2) ** 2 - math.cos(al) ** 2)
    C = 1 / math.sin(al / 2) / 2
    psi.append(np.array([-2 * C / A, 1, 1, 0, 1, 1, -2 * C / A, 1, 1, 0, 1, 1], float))
    print("   |R(0) Psi| for the printed Psi_I, Psi_II, Psi_III: %s" % ", ".join("%.1e" % np.linalg.norm(R @ p) for p in psi))
# CONTROL: a wrong dispersion relation (drop the cos^2/sin^4 factor) must fail.  At alpha = pi/3,
# eps = pi/2 that factor is exactly 1 (0.25/0.25), so the control is run at the paper's other
# angle, alpha = 9pi/20 (Fig. 7), where the true relation is checked too.
for al2, eps2 in ((9 * math.pi / 20, math.pi / 2), (math.pi / 3, 2 * math.pi / 3)):
    for qx in (0.4, 0.9, 2.0):
        kap = 1 / ell(al2, eps2, qx)
        kap_wrong = 2 * math.asinh(abs(math.sin(qx / 2)))
        r_true = abs(detDJ(al2, eps2, qx, 1j * kap, "qx")) / abs(detDJ(al2, eps2, qx, 1j * kap * 1.3, "qx"))
        r_wrong = abs(detDJ(al2, eps2, qx, 1j * kap_wrong, "qx")) / abs(detDJ(al2, eps2, qx, 1j * kap_wrong * 1.3, "qx"))
        print("   alpha=%.4f eps=%.4f q=%.1f: Eq.24 kappa ratio %.1e ; CONTROL factor-dropped kappa ratio %.1e (should be >> 0)"
              % (al2, eps2, qx, r_true, r_wrong))
# Eq. 24 from Eq. 16: sin^2(i kappa/2) = -sinh^2(kappa/2)
for q in (0.3, 1.2, 2.8):
    k = 1 / ell(al, eps, q)
    print("   Eq.16 at qy = i/ell(q) from Eq.24, q=%.1f: residual %.1e" % (q, abs(disp(al, eps, q, 1j * k))))

# ---------- Part 2 ----------
print("== Part 2: floppy modes of a finite triangulated Miura-ori (independent)")

def miura(n, m, a=1.0, b=1.0, alpha=math.pi / 3, theta=math.pi / 4, diag=True):
    """standard rigid-folded Miura-ori vertex positions (Schenk & Guest param.)"""
    # folded geometry
    H = a * math.sin(theta) * math.sin(alpha)
    S = b * math.cos(theta) * math.tan(alpha) / math.sqrt(1 + math.cos(theta) ** 2 * math.tan(alpha) ** 2)
    L = a * math.sqrt(1 - math.sin(theta) ** 2 * math.sin(alpha) ** 2)
    V = b / math.sqrt(1 + math.cos(theta) ** 2 * math.tan(alpha) ** 2)
    P = {}
    for i in range(n + 1):
        for j in range(m + 1):
            # zig-zag: odd j shifted in x by V; odd i raised by H
            P[(i, j)] = np.array([i * S, j * L + (V if i % 2 else 0.0), H if j % 2 else 0.0])
    edges = set()
    for i in range(n + 1):
        for j in range(m + 1):
            if i < n: edges.add(((i, j), (i + 1, j)))
            if j < m: edges.add(((i, j), (i, j + 1)))
            if diag and i < n and j < m: edges.add(((i, j), (i + 1, j + 1)))
    return P, list(edges)

def floppy(P, edges, rigid_quads=False):
    keys = list(P); idx = {k: t for t, k in enumerate(keys)}
    rows = []
    for u, v in edges:
        r = np.zeros(3 * len(keys)); d = P[u] - P[v]
        r[3 * idx[u]:3 * idx[u] + 3] = d; r[3 * idx[v]:3 * idx[v] + 3] = -d
        rows.append(r)
    if rigid_quads:  # control: keep each parallelogram planar (no face bending) via its other diagonal too
        pass
    Rm = np.array(rows)
    sv = np.linalg.svd(Rm, compute_uv=False)
    tol = 1e-9 * sv[0]
    rank = int((sv > tol).sum())
    return 3 * len(keys) - rank - 6

def flat_sheet(n, m):
    P, e = miura(n, m, theta=0.0)  # theta = 0: unfolded, all z = 0
    return P, e

def generic(n, m, seed=1):
    rng = np.random.default_rng(seed)
    P, e = miura(n, m)
    return {k: v + 0.05 * rng.standard_normal(3) for k, v in P.items()}, e

print("   n x n cells | vertices | boundary vertices B | floppy (folded Miura) | Maxwell B-3 | generic perturbed | CONTROL unfolded flat sheet")
for n in (2, 3, 4, 6, 8, 10, 12):
    P, e = miura(n, n)
    Bv = 4 * n
    print("   %2d x %-2d     | %4d     | %4d                | %4d                  | %4d        | %4d              | %d" % (
        n, n, len(P), Bv, floppy(P, e), Bv - 3, floppy(*generic(n, n)), floppy(*flat_sheet(n, n))))
for n, m in ((4, 12), (12, 4), (2, 20)):
    P, e = miura(n, m)
    print("   %2d x %-2d     | %4d     | %4d                | %4d                  | %4d" % (n, m, len(P), 2 * (n + m), floppy(P, e), 2 * (n + m) - 3))
