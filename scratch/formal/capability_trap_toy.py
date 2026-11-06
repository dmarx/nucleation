# scratch/formal/capability_trap_toy.py: reproduces and asserts the numbers of the capability-trap and tapering toy.
# Capacity C in [0,1]; demand 1; the organization's output is tau*C. Learning by doing needs existing capacity:
#   dC/dt = lam * P * C * (1 - C) - mu * C,
# where P is the work the organization does. Substitutive support A does the work first: P = min(tau*C, 1 - A).
# Capacity-first support covers only what the organization cannot do: P = min(tau*C, 1).
# Run: python3 -I scratch/formal/capability_trap_toy.py
# The parameters are invented to show a mechanism; none is a measurement of any organization.
import math

LAM, MU, TAU = 1.0, 0.3, 1.5


def close(x, y, tol=5e-3):
    assert abs(x - y) <= tol, (x, y)


def sim(c, a_of_t, horizon, substitutive=True, dt=1e-3):
    """Integrate capacity; return final C and the service shortfall (1 - service) integrated over the horizon."""
    t, gap = 0.0, 0.0
    while t < horizon:
        a = a_of_t(t)
        if substitutive:
            p = min(TAU * c, max(0.0, 1 - a))
            gap += max(0.0, 1 - min(1.0, a + p)) * dt
        else:
            p = min(TAU * c, 1.0)  # support fills 1 - tau*C, so service is whole
        c += dt * (LAM * p * c * (1 - c) - MU * c)
        t += dt
    return c, gap


# Steady states with no support: C = 0 is stable, an unstable threshold on the branch P = tau*C where
# lam*tau*C*(1 - C) = mu, and a kept state on the branch P = 1 at C = 1 - mu/lam.
C_LOW = (1 - math.sqrt(1 - 4 * MU / (LAM * TAU))) / 2
C_HIGH = 1 - MU / LAM
close(C_LOW, 0.2764, 1e-4)
close(C_HIGH, 0.7, 1e-9)

# 1. Full substitution has a deadline: capacity decays as e^(-mu t), crosses the threshold after
#    ln(C_HIGH / C_LOW) / mu = 3.10, and after that withdrawal does not bring it back.
T_TRAP = math.log(C_HIGH / C_LOW) / MU
close(T_TRAP, 3.098, 1e-3)
for dur, recovers in ((2.0, True), (3.0, True), (3.5, False), (5.0, False)):
    c_exit, _ = sim(C_HIGH, lambda t: 1.0, dur)
    c_end, _ = sim(c_exit, lambda t: 0.0, 200)
    assert (c_end > 0.6) == recovers, (dur, c_end)

# 2. Capacity-first support keeps a party above the threshold but cannot lift one below it.
assert sim(0.30, lambda t: 0.0, 200, substitutive=False)[0] > 0.69
assert sim(0.20, lambda t: 0.0, 200, substitutive=False)[0] < 0.01


# 3. Tapering substitutive support: slower is worse. From C = 0.45 under support covering 95 % of the work, an
#    abrupt cut recovers with a service shortfall of 0.97; a linear taper over 5 periods recovers with 2.61; a taper
#    over 10 periods holds practice down long enough to cross the threshold, and capacity is lost.
def taper(a0, length):
    return (lambda t: 0.0) if length == 0 else (lambda t: max(0.0, a0 * (1 - t / length)))


rows = {}
for length in (0, 5, 10):
    c_end, _ = sim(0.45, taper(0.95, length), 300)
    _, gap = sim(0.45, taper(0.95, length), 60)
    rows[length] = (c_end, gap)
assert rows[0][0] > 0.69 and rows[5][0] > 0.69 and rows[10][0] < 0.01
close(rows[0][1], 0.97, 0.01)
close(rows[5][1], 2.61, 0.01)

# The longest safe taper, by bisection: tapers shorter than it recover, longer ones are trapped.
lo, hi = 5.0, 10.0
for _ in range(25):
    mid = (lo + hi) / 2
    if sim(0.45, taper(0.95, mid), 300)[0] > 0.69:
        lo = mid
    else:
        hi = mid
T_SAFE = lo
close(T_SAFE, 9.13, 0.02)

# 4. Capacity-first support needs no taper: from the same start, capacity grows to the kept state and the
#    support it supplies, 1 - tau*C, falls to zero by itself.
c_cf, _ = sim(0.45, lambda t: 0.0, 60, substitutive=False)
close(c_cf, C_HIGH, 0.01)
assert TAU * c_cf >= 1

print("all capability-trap toy numbers reproduce; longest safe taper", round(T_SAFE, 2))
