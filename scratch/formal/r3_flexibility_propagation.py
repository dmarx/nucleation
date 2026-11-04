# scratch/formal/r3_flexibility_propagation.py
# CASE for the second reading of U19's slash: psychological flexibility and
# organizational flexibility as one property at two scales, joined by
# propagation, not aggregation (Guida, Minutola and Presti's P4, LIT-1218),
# with leverage as conferral (TERM-tmplu4ih) over the consequences others meet.
import numpy as np

N, steps, eta = 8, 60, 0.15
base = 0.3
def run(leverage_high: bool, culture: int):
    f = np.full(N, base); f[0] = 1.0            # member 0 is trained
    L = np.full((N, N), 0.02); np.fill_diagonal(L, 0)
    L[0, 1:] = 0.4 if leverage_high else 0.02   # what member 0 confers on the others' consequences
    mean0 = f.mean()
    for _ in range(steps):
        # flexible action is retained when the consequences a member meets reward it
        # (culture=+1) and extinguished when they penalize it (-1); colleagues take it up
        # in proportion to what the flexible member confers on their consequences
        uptake = eta * (L.T @ (f - base)) * (culture > 0)
        f = f + uptake * (1 - f) - (0.01 if culture > 0 else 0.15) * (f - base)
        f = np.clip(f, 0, 1)
    retained = f[0]; spread = f[1:].mean()
    return mean0, retained, spread
print(f"{'leverage':9s} {'culture':10s} mean_at_start retained(trained) spread(untrained mean)")
for lev in (True, False):
    for cul in (+1, -1):
        m0, r, s = run(lev, cul)
        print(f"{'high' if lev else 'low':9s} {'reinforcing' if cul>0 else 'penalizing':10s} {m0:13.3f} {r:17.3f} {s:22.3f}")
