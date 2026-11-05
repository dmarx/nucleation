# scratch/formal/dna_origami_toys.py: reproduces and asserts the numbers of the DNA-origami toy models filed in
# dmarx/nucleation#403: CASE-tmpa6s9d (four-state annealing), CASE-tmpj3cmd (A's branching model and uniform
# scaling), CASE-tmp7oe6s (placement and timing at equal integrated exposure), CASE-tmpli7gt (A's stabilization
# toy), and the deadline qualification of CLAIM-tmpiyvk1. Run: python3 -I scratch/formal/dna_origami_toys.py
# The rates and energies are invented to show mechanisms; none is a DNA-origami measurement.
import numpy as np
from scipy.linalg import expm


def close(x, y, tol=5e-4):
    assert abs(x - y) <= tol, (x, y)


# ---- CASE-tmpa6s9d: four-state annealing toy, G = H - T S (kcal/mol), Arrhenius rates -------------------------
R, NU = 0.001987, 1e6
G = {"U": (0, 0), "N": (-120, -0.36), "F": (-300, -0.88), "M": (-150, -0.46)}
TS = {("U", "N"): (-40, -0.155), ("N", "F"): (-260, -0.84), ("U", "M"): (-60, -0.22)}
S = list(G)
IX = {s: i for i, s in enumerate(S)}
g = lambda x, T: x[0] - T * x[1]


def q_anneal(T, absorbing_F=False):
    q = np.zeros((4, 4))
    for (a, b), ts in TS.items():
        for i, j in ((a, b), (b, a)):
            q[IX[i], IX[j]] = NU * np.exp(-(g(ts, T) - g(G[i], T)) / (R * T))
    np.fill_diagonal(q, -q.sum(1))
    if absorbing_F:
        q[IX["F"], :] = 0
    return q


def anneal(schedule, first_passage=False):
    """schedule: list of (temperature K, seconds). Returns Pr(X_T = F) (occupancy) or Pr(tau_F <= T)."""
    p = np.eye(4)[0]
    for T, t in schedule:
        p = p @ expm(q_anneal(T, first_passage) * t)
    return p[IX["F"]]


temps = np.arange(290, 345, 0.1)
occ_1h = np.array([anneal([(T, 3600)]) for T in temps])
close(occ_1h.max(), 0.9039)
close(temps[occ_1h.argmax()], 318.6, 0.05)
assert (occ_1h >= 0.95).sum() == 0                       # no constant temperature reaches 95 % folded at 1 h
from scipy.optimize import minimize_scalar                 # a numerical optimum: grid, then a bounded refinement
_r = minimize_scalar(lambda T: -anneal([(T, 3600)]), bounds=(310, 330), method="bounded", options={"xatol": 1e-4})
close(_r.x, 318.618, 0.01); close(-_r.fun, 0.90395, 1e-4)
hit_1h = np.array([anneal([(T, 3600)], True) for T in temps])
assert np.max(np.abs(hit_1h - occ_1h)) < 1e-6              # occupancy and first passage agree here: F barely melts
win16 = [T for T in np.arange(290, 345, 0.5) if anneal([(T, 57600)]) >= 0.9]
close(win16[0], 313.0, 0.01); close(win16[-1], 323.5, 0.01)
sched = [(327, 300), (318, 3300)]
close(anneal(sched), 0.9845); close(anneal(sched, True), 0.9845)
print("annealing toy: best constant 1 h %.4f; 16 h window %.1f-%.1f K; schedule %.4f" % (occ_1h.max(), win16[0], win16[-1], anneal(sched)))


# ---- CASE-tmpj3cmd: A's branching model U->N (a), U->K (b), N->F (c), N->K (d); F, K absorbing ----------------
def branch_eventual(a, b, c, d):
    return a / (a + b) * c / (c + d)


close(branch_eventual(1, .5, 2, .25), 0.5926)
close(branch_eventual(3, .5, 2, .25), 0.7619)
close(branch_eventual(1, 2, 2, .25), 0.2963)
lam = 20
close(branch_eventual(lam, lam * .5, 2, .25), 0.5926)            # both exits from U bimolecular: unchanged
close(branch_eventual(lam, lam * .5, 2, lam * .25), 0.1900)      # trap from N bimolecular, completion not: worse
print("branching model: 59.3 / 76.2 / 29.6 %%; uniform x20 with bimolecular trap from N: %.1f %%" % (100 * branch_eventual(lam, lam * .5, 2, lam * .25)))


# ---- CASE-tmp7oe6s: placement at equal cost; timing at equal integrated exposure (int c dt = 4 over [0,4]) ------
close(branch_eventual(2, .5, 2, .25), 0.7111)
close(branch_eventual(1, .5, 4, .25), 0.6275)


def qb(a, b, c, d):
    return np.array([[-(a + b), a, 0, b], [0, -(c + d), c, d], [0, 0, 0, 0], [0, 0, 0, 0]], float)


def timed(cfun, rates, n=400, T=4.0):
    p = np.eye(4)[0]
    dt = T / n
    for k in range(n):
        p = p @ expm(qb(*rates(cfun((k + .5) * dt))) * dt)
    return p[2]


front = lambda t: 2.0 if t < 2 else 0.0
even = lambda t: 1.0
late = lambda t: 0.0 if t < 2 else 2.0
rows = {
    "nucleation uses it": (lambda c: (c, .5, 2, .25), (0.706, 0.588, 0.248)),
    "nucleation and trap from N": (lambda c: (c, .5, 2, .25 * c), (0.641, 0.588, 0.226)),
    "trap from U and completion": (lambda c: (1, .5 * c, 2 * c, .25), (0.454, 0.588, 0.653)),
}
for name, (rates, expect) in rows.items():
    got = [timed(f, rates) for f in (front, even, late)]
    for x, y in zip(got, expect):
        close(x, y, 1e-3)
    print("timing, %s: front %.3f even %.3f late %.3f" % (name, *got))


# ---- CASE-tmpli7gt: A's stabilization toy ----------------------------------------------------------------------
Y = lambda s: s / (1 + s) / (1 + s * s / 4)
close(1.10 / 2.10, 0.524); close(1 / (1 + 1.21 / 4), 0.768); close(Y(1.10), 0.402)
xs = np.linspace(0.01, 5, 200001)
close(xs[Y(xs).argmax()], 1.1134, 1e-3); close(Y(xs).max(), 0.4022)
print("stabilization toy: optimum s = %.4f, yield %.4f" % (xs[Y(xs).argmax()], Y(xs).max()))


# ---- CLAIM-tmpiyvk1: eventual committor versus success by a deadline -------------------------------------------
def by_deadline(a, b, T):
    return a / (a + b) * (1 - np.exp(-(a + b) * T))


close(by_deadline(.08, .02, 10), 0.5057); close(by_deadline(.008, .002, 10), 0.0761)
print("deadline: eventual 0.8 both; by T=10 %.3f against %.3f" % (by_deadline(.08, .02, 10), by_deadline(.008, .002, 10)))
print("all assertions passed")


# ---- CLAIM on QUESTION-tmp4jbc3: equal yields in both arms, different routes --------------------------------------
# Parts: nucleus N and a downstream part B. N forms at rate a; B at b0 without N, b1 with N; any unfinished state traps
# at kappa (absorbing). Success = both formed. Generative nucleus: b1 != b0. State advantage only: b1 == b0.
from scipy.optimize import brentq as _brentq


def two_part(start, a, b0, b1, kap):
    q10 = b1 / (b1 + kap)
    q01 = a / (a + kap)
    q00 = (a * q10 + b0 * q01) / (a + b0 + kap)
    return {"00": q00, "10": q10}[start]


gen = (1.0, 0.5, 2.0, 0.5)
close(two_part("10", *gen), 0.8000); close(two_part("00", *gen), 17 / 30)
a_state = _brentq(lambda a: two_part("00", a, 2.0, 2.0, 0.5) - 17 / 30, 0.1, 5)
close(two_part("10", a_state, 2.0, 2.0, 0.5), 0.8000); close(two_part("00", a_state, 2.0, 2.0, 0.5), 17 / 30)
close(a_state, 0.7991, 1e-3)
print("route: generative (b0 0.5, b1 2.0) and state-only (a %.4f, b0 = b1 = 2.0) both give 0.800 with N, %.4f without" % (a_state, 17 / 30))
print("all assertions passed (route)")


# ---- CLAIM-tmps9wa1: supplied repair. dI/dt = -d I + rho s (1 - I) ---------------------------------------------
d_, rs_ = 0.2, 1.0
I_star = rs_ / (rs_ + d_)
close(I_star, 0.8333)
for t_, v_ in ((1, 0.6823), (5, 0.3066), (10, 0.1128)):
    close(I_star * np.exp(-d_ * t_), v_)                    # after the supply is withdrawn
for th_, need_ in ((0.9, 9.0), (0.99, 99.0)):
    close(th_ / (1 - th_), need_, 1e-6)                     # supply rho*s needed per unit damage rate to hold theta
print("supplied repair: intact %.3f; after withdrawal %.3f at t=10; 9d for 90 %%, 99d for 99 %%" % (I_star, I_star * np.exp(-2)))
print("all assertions passed (repair)")
