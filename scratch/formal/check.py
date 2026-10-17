# scratch/formal/check.py: verifies the committed-prediction coupling in CASE-099's linearization
import sympy as sp
import numpy as np

s, kA, kB, kp, m, e, eta = sp.symbols("s kappa_A kappa_B kappa_p m e eta", real=True)
# committed predictions: specialist A leans +s, B leans -s, both bent by the shared meaning m
pA = s + kA * m
pB = -s + kB * m
# evidence as read: raw evidence e, bent by the shared meaning with weight kappa' (kp)
r = e + kp * m
score_diff = -((pA - r) ** 2 - (pB - r) ** 2)   # A's score minus B's, squared-error scoring
gamma = sp.simplify(eta * sp.diff(score_diff, m).subs({m: 0, e: 0}))
drive = sp.simplify(eta * sp.diff(score_diff, e).subs({m: 0, e: 0}))
print("gamma =", sp.factor(gamma))
print("evidence drive =", sp.factor(drive))
# Regime A as the limit: score against the dominant interpretation itself (r = m scaled)
# prediction revised after evidence: pA = pB = r  -> no score difference
print("revised-after-evidence score diff:", sp.simplify((-((r + 0 - r) ** 2 - (r - r) ** 2))))

# stability of J = [[a, b], [g, d]] with b>0, g<0: Jury conditions
a_, d_, b_, g_ = sp.symbols("alpha delta beta gamma", real=True)
J = sp.Matrix([[a_, b_], [g_, d_]])
print("det =", J.det(), " trace =", J.trace())

rng = np.random.default_rng(0)
def max_abs_eig(a, d, b, g):
    return max(abs(np.linalg.eigvals(np.array([[a, b], [g, d]]))))
bad = 0
for _ in range(200000):
    a, d = rng.uniform(0, 0.999, 2)
    b = rng.uniform(0, 3)
    g = rng.uniform(-3, 3)
    stable = max_abs_eig(a, d, b, g) < 1
    if b * g >= 0:
        pred = b * g < (1 - a) * (1 - d)          # CASE-099's condition
    else:
        pred = -b * g < 1 - a * d                 # oscillatory bound for negative coupling
    if stable != pred and abs(max_abs_eig(a, d, b, g) - 1) > 1e-9:
        bad += 1
print("mismatches over 200000 random draws:", bad)
# with b*g < 0, unstable only through complex eigenvalues?
real_unstable = 0
for _ in range(200000):
    a, d = rng.uniform(0, 0.999, 2); b = rng.uniform(0, 3); g = -rng.uniform(0, 3)
    ev = np.linalg.eigvals(np.array([[a, b], [g, d]]))
    if max(abs(ev)) > 1 and np.all(np.abs(ev.imag) < 1e-12):
        real_unstable += 1
print("negative coupling, unstable with real eigenvalues:", real_unstable)
