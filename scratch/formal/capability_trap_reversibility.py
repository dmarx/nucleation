# scratch/formal/capability_trap_reversibility.py: what CLAIM-605's model says about a reversibility principle
# (CLAIM-tmpsmg1c) read as "go gradually". Same model and parameters as capability_trap_toy.py:
#   dC/dt = lam * P * C * (1 - C) - mu * C, substitutive support A gives P = min(tau*C, 1 - A).
# Three checks, each asserted:
#   1. Partial substitution at a constant share a leaves no deadline when a < a* = 1 - mu / (1 - C_LOW) = 0.585;
#      above it, capacity is lost however long the evaluation runs before withdrawal.
#   2. A pilot of full substitution stays reversible by an abrupt cut until 3.10, and the longest safe exit taper
#      shrinks as the pilot runs: 13.9 after no pilot, 9.7 after 1 unit, 5.2 after 2, 2.8 after 2.5, 0.5 after 3.
#   3. A gradual phase-in to full substitution is reversible by an abrupt cut at its end only if it lasts < 8.5.
# Run: python3 -I scratch/formal/capability_trap_reversibility.py
# The parameters are invented to show a mechanism; none is a measurement of any organization or person.
import math

LAM, MU, TAU = 1.0, 0.3, 1.5
C_LOW = (1 - math.sqrt(1 - 4 * MU / (LAM * TAU))) / 2
C_HIGH = 1 - MU / LAM


def close(x, y, tol):
    assert abs(x - y) <= tol, (x, y)


def sim(c, a_of_t, horizon, dt=1e-3):
    t = 0.0
    while t < horizon:
        p = min(TAU * c, max(0.0, 1 - a_of_t(t)))
        c += dt * (LAM * p * c * (1 - c) - MU * c)
        t += dt
    return c


def recovers(c):
    return sim(c, lambda t: 0.0, 300) > 0.69


def bisect(ok, lo, hi, n=30):
    for _ in range(n):
        mid = (lo + hi) / 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo


# 1. Constant partial substitution. On the branch P = 1 - a the kept state is C = 1 - mu / (1 - a); it stays above
#    the threshold, and withdrawal restores C_HIGH, exactly when a < a*.
A_STAR = 1 - MU / (1 - C_LOW)
close(A_STAR, 0.585, 1e-3)
for a, ok in ((0.30, True), (0.50, True), (0.58, True), (0.59, False), (0.70, False)):
    c = sim(C_HIGH, lambda t: a, 400)
    assert recovers(c) == ok, (a, c)

# 2. A pilot of full substitution for D units, then a linear exit taper from full support over T units.
T_TRAP = math.log(C_HIGH / C_LOW) / MU
close(T_TRAP, 3.098, 1e-3)
safe = {}
for d in (0.0, 1.0, 2.0, 2.5, 3.0):
    c0 = sim(C_HIGH, lambda t: 1.0, d)
    assert recovers(c0)  # every pilot shorter than T_TRAP is reversible by an abrupt cut
    safe[d] = bisect(lambda T: recovers(sim(c0, lambda t: max(0.0, 1 - t / T), 60)), 0.01, 60.0)
for d, expect in ((0.0, 13.92), (1.0, 9.67), (2.0, 5.17), (2.5, 2.84), (3.0, 0.46)):
    close(safe[d], expect, 0.05)
assert not recovers(sim(C_HIGH, lambda t: 1.0, 3.5))  # past the deadline, an abrupt cut fails too

# 3. A gradual phase-in: support ramps from none to full over L units, then is cut abruptly.
L_SAFE = bisect(lambda L: recovers(sim(C_HIGH, lambda t: min(1.0, t / L), L)), 3.0, 30.0)
close(L_SAFE, 8.52, 0.05)

print("reversibility checks reproduce: a* =", round(A_STAR, 3), "; safe taper after pilot", {k: round(v, 2) for k, v in safe.items()},
      "; longest reversible phase-in", round(L_SAFE, 2))
