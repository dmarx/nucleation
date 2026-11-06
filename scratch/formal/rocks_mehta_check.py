# scratch/formal/rocks_mehta_check.py: the twenty-eighth status review's check of Rocks and Mehta's index theorem, Theorem 1, Corollary 1, and the identity f = (T + lam I) u for the force exciting a linear zero mode (run: python3 -I scratch/formal/rocks_mehta_check.py)
"""Check of Rocks & Mehta (arXiv 2208.07419 v2): the generalized index theorem
(Sec. IV, eq. 20), Theorem 1 (App. B1), Corollary 1, and the reader's identity
f = (T + lam I) u for the LZEF that couples to an LZM u, on two networks that are
not the paper's: (A) a perturbed free 2x5 strip with braced end cells, prestress
on one braced cell; (B) a 3x6 grid with pinned left/right columns, a straight
middle row carrying prestress, random node perturbations off that row, a few
random diagonals, heterogeneous stiffness. Controls: zero prestress with K=I and
with heterogeneous K. Run: python3 -I scratch/formal/rocks_mehta_check.py"""
import numpy as np
from scipy.linalg import null_space, orth
rng = np.random.default_rng(7)
RC = 1e-7  # relative kernel tolerance (inverse is ill-conditioned as lam -> 0)

def compat(P, B, free):
    """C restricted to free dof; free = list of node indices with dof."""
    col = {v: k for k, v in enumerate(free)}
    C = np.zeros((len(B), 2 * len(free))); L = []
    for a, (i, j) in enumerate(B):
        d = P[j] - P[i]; l = np.linalg.norm(d); b = d / l; L.append(l)
        if j in col: C[a, 2*col[j]:2*col[j]+2] = b
        if i in col: C[a, 2*col[i]:2*col[i]+2] = -b
    return C, np.array(L)

def tmat(P, B, free, t, L):
    col = {v: k for k, v in enumerate(free)}; n = len(free)
    T = np.zeros((2*n, 2*n))
    for a, (i, j) in enumerate(B):
        if t[a] == 0: continue
        d = (P[j] - P[i]) / L[a]; M = (np.eye(2) - np.outer(d, d)) / L[a] * t[a]
        for p, q, s in ((i, i, 1), (j, j, 1), (i, j, -1), (j, i, -1)):
            if p in col and q in col:
                T[2*col[p]:2*col[p]+2, 2*col[q]:2*col[q]+2] += s * M
    return T

def same(A, Bm):
    return A.shape[1] == Bm.shape[1] and np.linalg.matrix_rank(np.hstack([A, Bm]), 1e-6) == A.shape[1]

def run(name, P, B, free, t, K, lam):
    C, L = compat(P, B, free); Nc, Ndof = C.shape
    LZM = null_space(C); SSS = null_space(C.T)
    assert np.allclose(C.T @ t, 0), "prestress must be a self-stress"
    T = tmat(P, B, free, t, L); H = C.T @ np.diag(K) @ C + T
    mineig = np.linalg.eigvalsh(H).min()
    G = np.linalg.inv(H + lam*np.eye(Ndof)); dldf = C @ G; dudt = G @ C.T
    LZEF = null_space(dldf, rcond=RC); ZDT = null_space(dudt, rcond=RC)
    res = dict(classical=(Ndof-Nc == LZM.shape[1]-SSS.shape[1]),
               generalized=(Ndof-Nc == LZEF.shape[1]-ZDT.shape[1]),
               th1_i=same(ZDT, SSS), th1_ii=same(orth(G @ LZEF), LZM))
    F = (H + lam*np.eye(Ndof)) @ LZM            # the LZEFs coupling to the LZM basis
    res["f=(T+lam)u"] = np.allclose(F, (T + lam*np.eye(Ndof)) @ LZM)
    res["LZEF span = (T+lam)ker C"] = same(orth(F), LZEF)
    cos = [abs(F[:, k] @ LZM[:, k]) / np.linalg.norm(F[:, k]) for k in range(F.shape[1])]
    col = {v: k for k, v in enumerate(free)}
    pn = {v for a, (i, j) in enumerate(B) if t[a] != 0 for v in (i, j) if v in col}
    m = np.zeros(Ndof, bool)
    for v in pn: m[2*col[v]:2*col[v]+2] = True
    off = [np.linalg.norm(F[~m, k]) / np.linalg.norm(F[:, k]) for k in range(F.shape[1])]
    # Corollary 1: LZM parallel to its LZEF iff it is a Hessian eigenvector
    eig = [np.linalg.norm(H @ LZM[:, k] - (LZM[:, k] @ H @ LZM[:, k]) * LZM[:, k]) < 1e-8 for k in range(LZM.shape[1])]
    cor1 = all((c > 1 - 1e-9) == e for c, e in zip(cos, eig))
    print(f"{name}  lam={lam:g}  Ndof={Ndof} Nc={Nc} #LZM={LZM.shape[1]} #SSS={SSS.shape[1]} "
          f"#LZEF={LZEF.shape[1]} #ZDT={ZDT.shape[1]} min eig H={mineig:.2e}")
    print("   ", res, "Cor1 consistent:", cor1)
    print("    |cos(LZM_k, LZEF_k)|:", np.round(cos, 3))
    print("    share of LZEF norm off prestressed-bond nodes:", np.round(off, 4))

# ---- network A: free strip, braced end cells, prestress on braced cell 0
PA = np.array([[x, y] for y in range(2) for x in range(5)], float) + 0.05*rng.standard_normal((10, 2))
ix = lambda x, y: y*5 + x
BA = [(ix(x, y), ix(x+1, y)) for y in range(2) for x in range(4)] + [(ix(x, 0), ix(x, 1)) for x in range(5)]
for c in (0, 3): BA += [(ix(c, 0), ix(c+1, 1)), (ix(c+1, 0), ix(c, 1))]
freeA = list(range(10)); CA, _ = compat(PA, BA, freeA)
sel = np.array([set(b) <= {0, 1, 5, 6} for b in BA])
s = null_space(CA[sel].T)[:, 0]; tA = np.zeros(len(BA)); tA[sel] = 0.8 * s / np.abs(s).max()
KA = rng.uniform(0.5, 2.0, len(BA))

# ---- network B: 3 rows x 6 cols, columns 0 and 5 pinned, middle row straight and prestressed
W, Hh = 6, 3
iy = lambda x, y: y*W + x
PB = np.array([[x, y] for y in range(Hh) for x in range(W)], float)
for y in (0, 2):
    for x in range(1, W-1): PB[iy(x, y)] += 0.08*rng.standard_normal(2)
for x in range(1, W-1): PB[iy(x, 1), 0] += 0.08*rng.standard_normal()   # stays on the line y=1
BB = [(iy(x, y), iy(x+1, y)) for y in range(Hh) for x in range(W-1)] + \
     [(iy(x, y), iy(x, y+1)) for y in range(Hh-1) for x in range(1, W-1)]
BB += [(iy(1, 0), iy(2, 1))]                                             # one diagonal
freeB = [v for v in range(W*Hh) if v % W not in (0, W-1)]
row = np.array([b[0] // W == 1 and b[1] // W == 1 for b in BB])
CB, _ = compat(PB, BB, freeB)
tB = np.zeros(len(BB)); tB[row] = 0.8                                     # tension along the straight row
assert np.allclose(CB.T @ tB, 0)
KB = rng.uniform(0.5, 2.0, len(BB))

for lam in (1e-3, 1e-6):
    for nm, P, B, fr, t, K in (("A", PA, BA, freeA, tA, KA), ("B", PB, BB, freeB, tB, KB)):
        run(nm + " control t=0,K=I ", P, B, fr, 0*t, np.ones(len(B)), lam)
        run(nm + " control t=0,K het", P, B, fr, 0*t, K, lam)
        run(nm + " prestress, K het ", P, B, fr, t, K, lam)
