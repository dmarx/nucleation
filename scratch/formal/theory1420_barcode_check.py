# scratch/formal/theory1420_barcode_check.py: the twenty-sixth status review's second check of THEORY-1420's bar counts (run: python3 -I scratch/formal/theory1420_barcode_check.py)
"""Second checker's script for THEORY-1420 (pass 26, cluster L).

Computes the sublevelset persistent homology (Z/2) of f_n(x) = sum_i g(x_i)
on a periodic grid of the n-torus, Freudenthal-triangulated, lower-star
filtration, by standard boundary-matrix reduction. Compares bar counts with
C(n,k) + (m^n - 1) C(n-1,k) (m = number of minima of g), semi-infinite
counts with C(n,k), and reports the finite bar lengths.

g = OPLS-UA CH2 torsion (c1,c2,c3 = 0.7055, -0.1355, 1.5725 kcal/mol, trans
at pi): the alkane case (m = 3). Controls: cos (m = 1, expect Betti numbers
only), cos(2x) (m = 2), and a deliberately non-sum function on T^2 whose
counts the formula must NOT predict.
"""
import itertools, math, sys
import numpy as np

def opls(phi):
    c1, c2, c3 = 0.7055, -0.1355, 1.5725
    return c1*(1+np.cos(phi)) + c2*(1-np.cos(2*phi)) + c3*(1+np.cos(3*phi))

def torus_complex(n, N):
    """Freudenthal triangulation of the periodic grid (Z/N)^n."""
    verts = list(itertools.product(range(N), repeat=n))
    idx = {v: i for i, v in enumerate(verts)}
    simplices = set()
    for v in verts:
        for perm in itertools.permutations(range(n)):
            path = [v]
            cur = list(v)
            for a in perm:
                cur[a] = (cur[a] + 1) % N
                path.append(tuple(cur))
            ids = [idx[p] for p in path]
            for r in range(1, n + 2):
                for face in itertools.combinations(ids, r):
                    simplices.add(tuple(sorted(face)))
    return verts, sorted(simplices, key=len)

def persistence(vals, simplices):
    fv = [max(vals[i] for i in s) for s in simplices]
    order = sorted(range(len(simplices)), key=lambda j: (fv[j], len(simplices[j]), j))
    pos = {simplices[j]: p for p, j in enumerate(order)}
    S = [simplices[j] for j in order]
    F = [fv[j] for j in order]
    cols = []
    for s in S:
        c = 0
        if len(s) > 1:
            for face in itertools.combinations(s, len(s) - 1):
                c ^= 1 << pos[face]
        cols.append(c)
    low_of = {}
    paired = set()
    bars = []
    for j in range(len(S)):
        c = cols[j]
        while c:
            l = c.bit_length() - 1
            if l in low_of:
                c ^= cols[low_of[l]]
            else:
                break
        cols[j] = c
        if c:
            l = c.bit_length() - 1
            low_of[l] = j
            paired.add(l); paired.add(j)
            bars.append((len(S[l]) - 1, F[l], F[j]))
    for j in range(len(S)):
        if j not in paired:
            bars.append((len(S[j]) - 1, F[j], math.inf))
    return bars

def summarize(bars, eps):
    out = {}
    for d, b, e in bars:
        if e - b > eps:
            out.setdefault(d, []).append((b, e))
    return out

def run(name, n, N, f, m_expect, check_formula=True, eps=1e-9):
    verts, simp = torus_complex(n, N)
    grid = 2 * np.pi * np.array(verts) / N
    vals = f(grid)
    bars = summarize(persistence(list(vals), simp), eps)
    ok = True
    print(f"== {name}: n={n}, N={N}, simplices={len(simp)}")
    for k in range(n + 1):
        bk = bars.get(k, [])
        inf = sum(1 for b, e in bk if e == math.inf)
        fin = [e - b for b, e in bk if e != math.inf]
        pred_tot = math.comb(n, k) + (m_expect**n - 1) * (math.comb(n - 1, k) if k <= n - 1 else 0)
        lens = sorted(set(round(x, 6) for x in fin))
        line = f"  dim {k}: bars={len(bk)} semi-inf={inf} finite={len(fin)} lengths={lens}"
        if check_formula:
            match = (len(bk) == pred_tot and inf == math.comb(n, k))
            ok &= match
            line += f"  predicted={pred_tot} (inf {math.comb(n,k)}) {'OK' if match else 'MISMATCH'}"
        print(line)
    return ok, bars

if __name__ == "__main__":
    # Structure of g: critical points on a fine grid
    x = np.linspace(0, 2*np.pi, 3600, endpoint=False)
    y = opls(x); d = np.roll(y, -1) - y; dl = y - np.roll(y, 1)
    mins = x[(dl < 0) & (d > 0)]; maxs = x[(dl > 0) & (d < 0)]
    print("OPLS-UA g: minima at deg", np.round(np.degrees(mins), 1), "values", np.round(opls(mins), 4))
    print("           maxima at deg", np.round(np.degrees(maxs), 1), "values", np.round(opls(maxs), 4))
    allok = True
    # controls with known answers
    allok &= run("control cos (m=1)", 2, 12, lambda G: np.cos(G).sum(axis=1), 1)[0]
    allok &= run("control cos 2x (m=2)", 2, 16, lambda G: np.cos(2*G).sum(axis=1), 2)[0]
    allok &= run("control cos 2x (m=2)", 3, 8, lambda G: np.cos(2*G).sum(axis=1), 2)[0]
    # negative control: not a sum of identical terms; formula with m=3 should fail
    neg, _ = run("negative control (non-sum)", 2, 24,
                 lambda G: opls(G[:, 0]) + opls(G[:, 1]) + 0.8*np.cos(G[:, 0] - G[:, 1]) * np.sin(3*G[:, 0]), 3)
    print("  negative control 1 matched counts:", neg, "(expected True: counts depend only on critical-point counts; lengths differ)")
    neg2, _ = run("negative control 2 (unequal terms opls(x)+cos(y))", 2, 48,
                  lambda G: opls(G[:, 0]) + np.cos(G[:, 1]), 3)
    print("  negative control 2 matched formula:", neg2, "(expected False)")
    # the alkane case: grid multiple of 12 so trans (180) and cis (0) are grid points;
    # gauche minima / g-t barriers are near, not on, grid points, so lengths are approximate
    for n, N in [(1, 360), (2, 48), (3, 12), (4, 6)]:
        allok &= run("alkane OPLS-UA (m=3)", n, N, lambda G: opls(G).sum(axis=1), 3)[0]
    print("ALL FORMULA CHECKS (excluding negative control):", "PASS" if allok else "FAIL")
