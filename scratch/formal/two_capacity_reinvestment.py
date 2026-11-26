# scratch/formal/two_capacity_reinvestment.py: reproduces and asserts the numbers of the assistant's gap fill on
# A4 §§8-9 of the exchange "Alignment consequences brainstorm" (2026-11-26): CLAIM-602's model extended to two
# capacities, with the effort a supply frees reinvested in a second task. Run:
#   python3 -I scratch/formal/two_capacity_reinvestment.py
# dC_k/dt = lam * P_k * (1 - C_k) - mu * C_k, task 1 has demand 1 met first by the supply (share A), the party doing
# P1 = min(tau*C1, 1 - A); the freed effort r*A goes to task 2. Parameters are CLAIM-602's (lam=1, mu=0.3, tau=1.5),
# invented to show mechanisms; none is a measurement.
LAM, MU, TAU, DT = 1.0, 0.3, 1.5, 1e-3


def close(x, y, tol=5e-3):
    assert abs(x - y) <= tol, (x, y)


def steady(A, r):
    c1 = LAM * (1 - A) / (LAM * (1 - A) + MU) if A < 1 else 0.0
    c2 = LAM * r * A / (LAM * r * A + MU) if r * A > 0 else 0.0
    return c1, c2


def run(A, r, t_sub, t_after, finite_budget):
    """Supply for t_sub, then none for up to t_after. Returns (C1, C2) at exit, time to meet demand, C2 at the end."""
    c1, c2 = LAM / (LAM + MU), 0.0          # start at the unassisted steady state of task 1
    for _ in range(int(round(t_sub / DT))):
        p1 = min(TAU * c1, 1 - A)
        p2 = min(r * A, 1 - p1) if finite_budget else r * A
        c1 += DT * (LAM * p1 * (1 - c1) - MU * c1)
        c2 += DT * (LAM * p2 * (1 - c2) - MU * c2)
    exit_state, recovery = (c1, c2), None
    for k in range(int(round(t_after / DT))):
        if recovery is None and TAU * c1 >= 1:
            recovery = k * DT
        p1 = min(TAU * c1, 1.0)
        p2 = max(0.0, min(r * A, 1 - p1)) if finite_budget else r * A
        c1 += DT * (LAM * p1 * (1 - c1) - MU * c1)
        c2 += DT * (LAM * p2 * (1 - c2) - MU * c2)
    return exit_state, recovery, c2


# 1. The first capacity's steady state does not depend on what the freed effort builds.
close(LAM / (LAM + MU), 0.769)
for A, c1_expected in ((0.5, 0.625), (0.9, 0.25)):
    for r in (0.0, 0.5, 1.0):
        c1, c2 = steady(A, r)
        close(c1, c1_expected)
close(steady(0.5, 1.0)[1], 0.625)
close(steady(0.9, 1.0)[1], 0.75)
close(sum(steady(0.5, 1.0)), 1.25)       # the sum exceeds the unassisted 0.769, and means nothing (incommensurable)

# 2. Withdrawal after full substitution for 20 units costs the same recovery whatever was reinvested (CLAIM-602: 6.38).
recs = []
for r in (0.0, 0.5, 1.0):
    (c1x, c2x), rec, _ = run(1.0, r, 20, 60, finite_budget=False)
    recs.append(rec)
close(recs[0], 6.38, tol=0.01)
assert max(recs) - min(recs) < 1e-9, recs

# 3. With a finite effort budget the new capacity is held only while the supply lasts.
(c1x, c2x), rec, c2_end = run(1.0, 1.0, 20, 30, finite_budget=True)
close(c2x, 0.769)
close(rec, 6.38, tol=0.01)
assert c2_end < 0.001, c2_end
print("two_capacity_reinvestment: all assertions pass")
