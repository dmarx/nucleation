# scratch/formal/r3_dysregulation_arms.py
# CASE for CLAIM-tmp99a8m: two organizations with the same impairment during an
# emotional episode, one dysregulated in DBT's sense (activation with high gain
# and a slowly decaying baseline captures interpretation), one in A29's
# attentional sense (a fixed budget shared with a competing demand).
import numpy as np

dt, T = 0.01, 80.0
t = np.arange(0, T, dt)
on, off = 10.0, 20.0
event = ((t >= on) & (t < off)).astype(float)   # discrepancy d(t), and competing demand D(t)

# DBT arm: z = b + alpha*d, db/dt = -(b - b0)/tau_b + gamma*d, q = sigma(kappa(z - theta))
alpha, b0, theta, kappa, tau_b, gamma = 2.0, 0.0, 1.0, 8.0, 15.0, 0.2
eps = 0.05
def dbt(lower_at=None):
    b = np.empty_like(t); b[0] = b0
    for k in range(1, len(t)):
        if lower_at is not None and t[k] >= lower_at:
            b[k] = b0; continue          # activation lowered to baseline (a regulation skill)
        b[k] = b[k-1] + dt*(-(b[k-1]-b0)/tau_b + gamma*event[k-1])
    a = alpha*(1.0 if lower_at is None else np.where(t >= lower_at, 0.0, 1.0))
    z = b + a*event
    q = 1/(1+np.exp(-kappa*(z-theta)))   # chance the threat perspective is active
    perf = 1 - 0.6*q                     # while active its interpretation governs the task
    tol = (theta + np.log(eps/(1-eps))/kappa - b)/alpha
    return perf, tol, b

# Attentional arm: budget B shared by the task (needs r) and a competing demand D(t)
B, r, D = 1.0, 1.0, 0.6
def att(remove_demand_at=None):
    Dt = D*event.copy()
    if remove_demand_at is not None: Dt[t >= remove_demand_at] = 0
    return np.minimum(1, (B - Dt)/r)

def report(name, p):
    def m(a, b): return p[(t >= a) & (t < b)].mean()
    after = t[(t >= off) & (p < 0.95)]
    lag = (after.max()-off) if len(after) else 0.0
    print(f"{name:34s} during={m(12,20):.3f}  20-30={m(20,30):.3f}  30-50={m(30,50):.3f}  impaired(<0.95) for {lag:5.1f} after the event")

p_d, tol, b = dbt(); p_a = att()
report("DBT arm", p_d); report("attentional arm", p_a)
report("DBT arm, activation lowered at 15", dbt(lower_at=15)[0])
report("DBT arm, competing demand removed", p_d)  # it has none: unchanged
report("attentional, demand removed at 15", att(remove_demand_at=15))
report("attentional, activation lowered", p_a)     # it has no activation term: unchanged
neg = t[(tol < 0) & (t >= off)]
print(f"DBT arm: tolerance at eps={eps} negative after the event for {(neg.max()-off) if len(neg) else 0:.1f} time units; peak baseline b={b.max():.3f}")
