# scratch/formal/larson_odoni_hypercube_check.py: re-derive Larson and Odoni's three-server hypercube example (Sec. 5.4.3-5.4.4)
# Pass 30 (status review), cluster H: check for THEORY-1394 / NOTE-1620.
# Inputs are read off the book's own images (MIT online edition): Fig. 5.11 (atom rates), Table 5-4
# (dispatch preferences), Table 5-6 (travel times), the location matrix L of Sec. 5.4.4.
# The script builds the generator on the 2^3 binary states plus the M/M/3 infinite tail, solves for the
# steady state, and recomputes the book's printed numbers: (5.21)-(5.25), the eight state probabilities,
# workloads (5.30), Table 5-5 (f_nj by (5.32)-(5.35)), f_I (5.36), (5.37), (5.38), T_Q (5.40),
# T (5.41), Table 5-7 (5.42)-(5.44).
# Controls that should FAIL: (a) giving atom 4 unit 2 as first backup instead of unit 3;
# (b) reading the online edition's image for (5.28), which duplicates (5.26), as the balance about 011.
# Usage: python3 -I scratch/formal/larson_odoni_hypercube_check.py
import numpy as np, math, itertools

lam_atom = np.array([0.25, 0.25, 0.10, 0.25, 0.15, 0.10, 0.10, 0.10, 0.10, 0.10])  # Fig. 5.11
prefs = {1: (1, 2, 3), 2: (1, 2, 3), 3: (2, 1, 3), 4: (1, 3, 2), 5: (2, 1, 3),
         6: (2, 1, 3), 7: (3, 1, 2), 8: (3, 1, 2), 9: (3, 1, 2), 10: (3, 1, 2)}       # Table 5-4
tau = np.array([  # Table 5-6, origin row i, destination column j
    [0, 3, 5, 2, 5, 7, 5, 5, 7, 7], [3, 0, 2, 5, 2, 4, 8, 6, 10, 8], [5, 2, 0, 7, 4, 2, 10, 8, 12, 10],
    [2, 5, 7, 0, 3, 5, 3, 3, 5, 5], [5, 2, 4, 3, 0, 2, 6, 4, 8, 6], [7, 4, 2, 5, 2, 0, 8, 6, 10, 8],
    [5, 8, 10, 3, 6, 8, 0, 2, 2, 4], [5, 6, 8, 3, 4, 6, 2, 0, 4, 2], [7, 10, 12, 5, 8, 10, 2, 4, 0, 2],
    [7, 8, 10, 5, 6, 8, 4, 2, 2, 0]], dtype=float)
L = np.zeros((3, 10)); L[0, 3] = 1; L[1, 4] = 1; L[2, 6] = L[2, 7] = 0.5   # l14 = l25 = 1, l37 = l38 = 1/2
N, mu = 3, 1.0
lam = lam_atom.sum()
PRA = {n: [j for j in prefs if prefs[j][0] == n] for n in (1, 2, 3)}

def busy(state, n):  # state index v(B) = b3*4 + b2*2 + b1; unit n is bit n-1
    return (state >> (n - 1)) & 1

def solve(prefs):
    # Unsaturated states 0..6 plus 7 (all busy, no queue); tail handled by M/M/3 closed form.
    Q = np.zeros((8, 8))
    for s in range(8):
        for j, p in prefs.items():
            free = [n for n in p if not busy(s, n)]
            if free:
                Q[s, s | (1 << (free[0] - 1))] += lam_atom[j - 1]
        for n in (1, 2, 3):
            if busy(s, n):
                Q[s, s & ~(1 << (n - 1))] += mu
    # Tail: state 7 also leaves to queue states at rate lam and is re-entered at rate 3mu; in balance
    # these flows cancel, so the 8-state chain's relative probabilities are exact; scale to P{S0..S3}.
    np.fill_diagonal(Q, -Q.sum(axis=1))
    A = np.vstack([Q.T, np.ones(8)]); b = np.zeros(9); b[-1] = 1
    p8 = np.linalg.lstsq(A, b, rcond=None)[0]
    # M/M/3 with lam=1.5, mu=1 (eq. 4.44 as used in 5.21)
    a = lam / mu; terms = [a**k / math.factorial(k) for k in range(N)]
    pN = a**N / math.factorial(N); P0 = 1 / (sum(terms) + pN / (1 - a / N))
    PS = [P0 * t for t in terms] + [P0 * pN]; PQ = P0 * pN * (a / N) / (1 - a / N)
    P = p8 / p8.sum() * (1 - PQ)
    return P, PS, PQ

def measures(P, PQ, prefs):
    PQp = PQ + P[7]
    f1 = np.zeros((3, 10))
    for s in range(7):
        for j, p in prefs.items():
            n = [u for u in p if not busy(s, u)][0]
            f1[n - 1, j - 1] += lam_atom[j - 1] / lam * P[s]
    f = f1 + lam_atom / lam * PQp / N
    rho = [sum(P[s] for s in range(8) if busy(s, n)) + PQ for n in (1, 2, 3)]
    inter = sum(f[n - 1, j - 1] for n in (1, 2, 3) for j in range(1, 11) if j not in PRA[n])
    fIn1 = sum(f[0, j - 1] for j in range(1, 11) if j not in PRA[1]) / f[0].sum()
    fI1 = sum(f[m - 1, j - 1] for m in (2, 3) for j in PRA[1]) / sum(f[m - 1, j - 1] for m in (1, 2, 3) for j in PRA[1])
    t = L @ tau                                       # (5.39)
    w = lam_atom / lam
    TQ = w @ tau @ w                                  # (5.40)
    T = (f1 * t).sum() + PQp * TQ                     # (5.41)
    Tj = (f1 * t).sum(0) / f1.sum(0) * (1 - PQp) + (w @ tau) * PQp   # (5.42)
    TRA = []
    for n in (1, 2, 3):
        js = [j - 1 for j in PRA[n]]
        num = (f1[:, js] * t[:, js]).sum() / f1[:, js].sum()
        q = sum(lam_atom[j] * lam_atom[k] * tau[k, j] for k in js for j in range(10)) / lam**2 / sum(w[k] for k in js)
        TRA.append(num * (1 - PQp) + q * PQp)          # (5.43), queued term as printed: k in area n
    TU = [((f1[n] * t[n]).sum() + TQ * PQp / N) / (f1[n].sum() + PQp / N) for n in range(3)]  # (5.44)
    return dict(rho=rho, f1=f1, f=f, inter=inter, fIn1=fIn1, fI1=fI1, TQ=TQ, T=T, Tj=Tj, TRA=TRA, TU=TU, PQp=PQp)

book_P = dict(zip([0, 1, 2, 4, 6, 5, 3, 7], [0.21053, 0.13669, 0.08863, 0.09047, 0.05301, 0.08894, 0.09489, 0.11842]))
book = dict(rho=[0.5574, 0.4734, 0.4693], inter=0.43529, fIn1=0.2982, fI1=0.4784, TQ=4.34, T=3.258,
            Tj=[3.37, 4.29, 5.26, 1.75, 1.77, 3.64, 2.64, 2.31, 4.55, 4.19], TRA=[3.13, 3.30, 3.42], TU=[3.14, 3.18, 3.45])
book_f = np.array([  # Table 5-5 lower figures f_nj, rows j=1..10, columns n=1..3
    [0.08692, 0.05076, 0.02897], [0.08692, 0.05076, 0.02897], [0.01470, 0.04037, 0.01159],
    [0.08692, 0.02798, 0.05176], [0.02205, 0.06056, 0.01738], [0.01470, 0.04037, 0.01159],
    [0.01483, 0.01119, 0.04064], [0.01483, 0.01119, 0.04064], [0.01483, 0.01119, 0.04064],
    [0.01483, 0.01119, 0.04064]])

def report(label, prefs, verbose=True):
    P, PS, PQ = solve(prefs)
    m = measures(P, PQ, prefs)
    errs = {}
    errs['P'] = max(abs(P[s] - v) for s, v in book_P.items())
    errs['PS'] = max(abs(a - b) for a, b in zip(PS + [PQ], [4/19, 0.31579, 0.23684, 0.11842, 0.11842]))
    errs['rho'] = max(abs(a - b) for a, b in zip(m['rho'], book['rho']))
    errs['f_nj'] = np.abs(m['f'].T - book_f).max()
    for k in ('inter', 'fIn1', 'fI1', 'TQ', 'T'):
        errs[k] = abs(m[k] - book[k])
    for k in ('Tj', 'TRA', 'TU'):
        errs[k] = max(abs(a - b) for a, b in zip(m[k], book[k]))
    # Probabilities, workloads and dispatch fractions: to the book's printed rounding (the book sums rounded
    # values, hence 2e-5 and 5e-5). Travel times: to 0.05 min, because two printed values are off by more than
    # rounding: T_Q = 196/45 = 4.356 exactly from Table 5-6 (book 4.34) and T_7 = 2.68 (book 2.64).
    tol = dict(P=6e-6, PS=6e-6, rho=6e-5, f_nj=2e-5, inter=5e-5, fIn1=6e-5, fI1=6e-5, TQ=2e-2, T=5e-3, Tj=5e-2, TRA=1.5e-2, TU=1e-2)
    ok = all(errs[k] <= tol[k] for k in errs)
    print(f"--- {label}: {'MATCHES the book' if ok else 'DOES NOT match the book'}")
    if verbose:
        print("  P (B0..B7):", np.round(P, 5))
        print("  rho:", np.round(m['rho'], 4), " f_I:", round(m['inter'], 5), " P'_Q:", round(m['PQp'], 5))
        print("  T_Q:", round(m['TQ'], 3), " T:", round(m['T'], 3))
        print("  T_j:", np.round(m['Tj'], 2)); print("  TRA:", np.round(m['TRA'], 2), " TU:", np.round(m['TU'], 2))
    for k, e in errs.items():
        print(f"  max |err| {k:5s} = {e:.2e} {'ok' if e <= tol[k] else 'FAIL'}")
    return ok, P

ok_main, P = report("book's inputs", prefs)

# Hand-check of the book's balance equations (5.26), (5.27), (5.29) and the correct (5.28) on the solution.
p = lambda s: P[int(s, 2)]
r526 = p('001') * (1.5 + 1) - (p('000') * 0.75 + 1 * (p('101') + p('011')))
r527 = p('100') * (1.5 + 1) - (p('000') * 0.40 + 1 * (p('110') + p('101')))
r529 = p('101') * (1.5 + 2) - (1 * p('111') + p('001') * (0.4 + 0.25) + p('100') * (0.75 + 0.40))
r528 = p('011') * (1.5 + 2) - (1 * p('111') + p('001') * 0.85 + p('010') * 1.10)  # rates of Fig. 5.17
print("residuals (5.26) (5.27) (5.29) and reconstructed (5.28):", [f"{x:.1e}" for x in (r526, r527, r529, r528)])

# Control (a): atom 4's first backup changed from unit 3 to unit 2. Should NOT match.
alt = dict(prefs); alt[4] = (1, 2, 3)
ok_a, _ = report("control (a), atom 4 backed up by unit 2", alt, verbose=False)

# Control (b): the online image printed as (5.28) is (5.26) again. Replace the 011 balance by it and
# solve the book's elimination system (5.22)-(5.29): the system is then singular or off the book's values.
names = ['000', '001', '010', '011', '100', '101', '110', '111']
idx = {s: i for i, s in enumerate(names)}
def row(coefs):
    r = np.zeros(8)
    for s, c in coefs.items(): r[idx[s]] += c
    return r
rows = [row({'000': 1}), row({'111': 1}), row({'001': 1, '010': 1, '100': 1}), row({'110': 1, '101': 1, '011': 1}),
        row({'001': 2.5, '000': -0.75, '101': -1, '011': -1}), row({'100': 2.5, '000': -0.40, '110': -1, '101': -1}),
        row({'001': 2.5, '000': -0.75, '101': -1, '011': -1}),   # the duplicated image used as (5.28)
        row({'101': 3.5, '111': -1, '001': -0.65, '100': -1.15})]
rhs = np.array([4/19, 9/76, 6/19, 9/38, 0, 0, 0, 0])
rank = np.linalg.matrix_rank(np.array(rows))
print(f"--- control (b), duplicated (5.28): coefficient rank {rank} of 8 -> "
      f"{'DOES NOT determine the book values' if rank < 8 else 'determines a solution'}")
rows[6] = row({'011': 3.5, '111': -1, '001': -0.85, '010': -1.10})
sol = np.linalg.solve(np.array(rows), rhs)
print("  with (5.28) rebuilt from Fig. 5.17:", dict(zip(names, np.round(sol, 5))))
print("SUMMARY: book's inputs match:", ok_main, "| control (a) fails as it should:", not ok_a,
      "| control (b) fails as it should:", rank < 8)
