# scratch/formal/hua_hypercube_convergence_check.py
# Pass 29 (status review), cluster E: re-check for THEORY-1426, NOTE-1618 and the hypercube-convergence QUESTION.
# Part 1: exact-rational check of the homogeneous-case Phi_N (Hua et al., Corollary 1).
# Part 2: re-implementation of Algorithm 1 against the exact stationary distribution from the full
# generator (the control), with Assumption 3.1 evaluated per instance. Seeds default to 0 and 7.
# Usage: python3 -I scratch/formal/hua_hypercube_convergence_check.py [seed ...]

# ---------- Part 1 ----------
# Exact-rational check of Hua et al.'s homogeneous-case Phi_N (Sec. 3.2):
# claim: Phi_N = [prod(lam+j nu) - prod(j nu)] / prod(lam+j nu) < 1.
# Control: compare the paper's general definition of Phi_n (Assumption 3.1, gamma=1, mu_n=n nu)
# against the closed form, exactly.
from fractions import Fraction as F
from math import prod
def phi(n, lam, nu):
    mu = lambda j: j*nu
    if n == 1: return lam/(lam+mu(1))
    s = sum(prod(mu(j)/(lam+mu(j-1)) for j in range(q, n+1)) for q in range(2, n+1))
    return lam/(lam+mu(n))*(s+1)
def closed(N, lam, nu):
    a = prod(lam+j*nu for j in range(1, N+1)); b = prod(j*nu for j in range(1, N+1))
    return (a-b)/a
bad = 0
for lam in [F(1,10), F(1), F(5), F(20)]:
    for nu in [F(1,10), F(1)]:
        for N in range(1, 26):
            p, c = phi(N, lam, nu), closed(N, lam, nu)
            if p != c or not p < 1: bad += 1; print("mismatch/fail", lam, nu, N, float(p), float(c))
print("mismatches or Phi>=1:", bad)
for lam, N in [(F(5),20),(F(10),20),(F(15),25)]:
    print(f"lam/nu={lam}, N={N}: 1-Phi_N = {float(1-phi(N,lam,F(1))):.3e}")


# ---------- Part 2 ----------
# Re-implementation of Hua, Luo, Swersey and Wen's CPU algorithm (Algorithm 1, Eq. 12-14, Prop. 1)
# for the zero-buffer hypercube with server-specific rates, checked against the exact
# stationary distribution from the full generator (control). Also reports the observed
# contraction ratio M_{k+1}/M_k and the paper's bound Phi_N (Assumption 3.1).
import numpy as np, itertools, math, sys
rng = None
def instance(N, J, lam, nu):
    f = rng.dirichlet(np.ones(J)); pref = [rng.permutation(N) for _ in range(J)]
    return dict(N=N, J=J, lam=lam, nu=np.array(nu, float), f=f, pref=pref)
def first_free(state, order):
    for u in order:
        if not (state >> u) & 1: return u
    return None
def rates(I):
    N, lam = I['N'], I['lam']; up = {}  # up[(l,m)] = lambda_lm
    for l in range(2**N):
        for j in range(I['J']):
            u = first_free(l, I['pref'][j])
            if u is not None: up[(l, l | (1 << u))] = up.get((l, l | (1 << u)), 0) + lam*I['f'][j]
    return up
def exact(I, up):
    N = I['N']; S = 2**N; Q = np.zeros((S, S))
    for (l, m), r in up.items(): Q[l, m] += r
    for m in range(S):
        for i in range(N):
            if (m >> i) & 1: Q[m, m & ~(1 << i)] += I['nu'][i]
    Q -= np.diag(Q.sum(1)); A = np.vstack([Q.T, np.ones(S)]); b = np.zeros(S+1); b[-1] = 1
    return np.linalg.lstsq(A, b, rcond=None)[0]
def cpu(I, up, eps=1e-13, delta=1e-14, kmax=200000):
    N, lam, nu = I['N'], I['lam'], I['nu']
    layers = [[m for m in range(2**N) if bin(m).count('1') == n] for n in range(N+1)]
    mu_m = np.array([sum(nu[i] for i in range(N) if (m >> i) & 1) for m in range(2**N)])
    lam_m = np.array([lam if m != 2**N-1 else 0.0 for m in range(2**N)])
    p = np.zeros(2**N)
    for n in range(N+1):
        for m in layers[n]: p[m] = 1/math.comb(N, n)
    lamn = lambda pp, n: sum(pp[m]*lam_m[m] for m in layers[n])
    mun = lambda pp, n: sum(pp[m]*mu_m[m] for m in layers[n])
    diffs = []
    for k in range(kmax):
        old = p.copy()
        for n in range(1, N):
            mu_prev = mun(old, n)  # mu^{k,0}(n)
            pin = p.copy()
            while True:
                new = p.copy()
                for m in layers[n]:
                    a = sum(p[l]*mu_prev/lamn(p, n-1)*up.get((l, m), 0)/(lam_m[m]+mu_m[m]) for l in layers[n-1])
                    b = sum(old[l]*lamn(old, n)/mun(old, n+1)*nu[i]/(lam_m[m]+mu_m[m])
                            for i in range(N) if not (m >> i) & 1 for l in [m | (1 << i)])
                    new[m] = a + b
                d = max(abs(new[m]-p[m]) for m in layers[n]); p = new; mu_prev = mun(p, n)
                if d < delta: break
        M = max(sum(abs(p[m]-old[m]) for m in layers[n]) for n in range(N+1)); diffs.append(M)
        if M < eps: break
    ln = [lamn(p, n) for n in range(N+1)]; mn = [mun(p, n) for n in range(N+1)]
    G = [1.0]
    for n in range(1, N+1): G.append(G[-1]*ln[n-1]/mn[n])
    pn = np.array(G)/sum(G)
    P = np.array([pn[bin(m).count('1')]*p[m] for m in range(2**N)])
    return P, diffs
def PhiN(I):
    N, lam, nu = I['N'], I['lam'], I['nu']
    sums = {n: [sum(nu[list(c)]) for c in itertools.combinations(range(N), n)] for n in range(1, N+1)}
    mx = {n: max(v) for n, v in sums.items()}; mn = {n: min(v) for n, v in sums.items()}
    mx[N+1] = mn[N+1] = 1.0  # gamma_{N+1} undefined in the paper; set to 1
    g = lambda n: mx[n]/mn[n]
    out = []
    for n in range(1, N+1):
        if n == 1: out.append(lam/(lam+mn[1])*g(2)); continue
        s = sum(g(q)*np.prod([mx[j]/(lam+mn[j-1]) for j in range(q, n+1)]) for q in range(2, n+1))
        out.append(lam/(lam+mn[n])*(s+g(n+1)))
    return out

def run_instances():
    for trial, (N, lam, nu) in enumerate([(4, 2.0, [1, 1, 1, 1]), (5, 3.0, [1, 1, 1, 1, 1]),
                                           (5, 3.0, [0.8, 1, 1.1, 1.2, 0.9]), (6, 4.0, [0.5, 1, 1.5, 2, 1, 0.7]),
                                           (5, 8.0, [0.2, 3, 1, 0.5, 2])]):
        I = instance(N, 8, lam, nu); up = rates(I)
        Pex = exact(I, up); P, d = cpu(I, up)
        ratios = [d[i+1]/d[i] for i in range(len(d)-1) if d[i] > 1e-11]
        ph = PhiN(I)
        print(f"N={N} lam={lam} nu={nu}: iters={len(d)} max|P-Pexact|={np.abs(P-Pex).max():.2e} "
              f"sum={P.sum():.12f} observed max ratio={max(ratios) if ratios else float('nan'):.3f} "
              f"Phi_1..N-1 max={max(ph[:-1]):.3f} Assumption3.1 holds={max(ph[:-1])<1}")

seeds = [int(s) for s in sys.argv[1:]] or [0, 7]
for seed in seeds:
    rng = np.random.default_rng(seed)
    print('seed', seed)
    run_instances()
