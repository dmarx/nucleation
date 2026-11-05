# scratch/formal/supplied_maintenance_toys.py: reproduces and asserts the numbers of two toy models filed with the
# aid-and-development reading that follows CLAIM-597: (a) self-sustaining uptake with an ignition threshold, set
# against CLAIM-597's supplied repair, and (b) capacity learned by doing, against aid that substitutes for the work
# or comes after domestic capacity, covering only what it cannot (capacity-first; Azam et al. 1999 use
# "gap-filling aid" for the harmful case, so that name is avoided here). Run: python3 -I scratch/formal/supplied_maintenance_toys.py
# The parameters are invented to show mechanisms; none is a measurement of any organization or state.
import math


def close(x, y, tol=5e-4):
    assert abs(x - y) <= tol, (x, y)


def rk4(f, y, t1, dt=1e-3):
    t = 0.0
    while t < t1 - 1e-12:
        h = min(dt, t1 - t)
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h / 2 * k1)
        k3 = f(t + h / 2, y + h / 2 * k2)
        k4 = f(t + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
    return y


# ---- (a) flame-like uptake dI/dt = -d I + k s I^2 (1 - I) against supplied repair dI/dt = -d I + r s (1 - I) -------
D, KS = 0.2, 2.0
disc = math.sqrt(1 - 4 * D / KS)
I_LOW, I_HIGH = (1 - disc) / 2, (1 + disc) / 2          # ignition threshold (unstable) and kept state (stable)
close(I_LOW, 0.1127)
close(I_HIGH, 0.8873)
RS = D * I_HIGH / (1 - I_HIGH)                            # supplied repair matched to hold the same share
close(RS, 1.5746)
flame = lambda f: (lambda t, i: -D * i + KS * f * i * i * (1 - i))
supplied = lambda f: (lambda t, i: -D * i + RS * f * (1 - i))

# Below the threshold the flame goes out with the supply on; supplied repair recovers from any start.
for i0 in (0.05, 0.10):
    assert rk4(flame(1), i0, 50) < 1e-3
    close(rk4(supplied(1), i0, 50), I_HIGH)
for i0 in (0.12, 0.30):
    close(rk4(flame(1), i0, 50), I_HIGH)

# A partial cut: the flame holds while k s f >= 4 d, that is f >= 0.4, and then collapses; supplied repair degrades
# smoothly to r s f / (r s f + d).
F_CRIT = 4 * D / KS
close(F_CRIT, 0.4)
for f, kept in ((0.5, 0.7236), (0.45, 0.6667)):
    close(rk4(flame(f), I_HIGH, 200), kept)
for f in (0.39, 0.35):
    assert rk4(flame(f), I_HIGH, 200) < 1e-3
    close(rk4(supplied(f), I_HIGH, 200), RS * f / (RS * f + D))
close(RS * 0.39 / (RS * 0.39 + D), 0.7543)

# Withdrawal: both decay as e^(-d t). Hysteresis: the flame relights on restored supply only if it is still above
# the threshold, so a short outage is survived and a long one is not.
close(rk4(flame(0), I_HIGH, 5), I_HIGH * math.exp(-D * 5))
T_LOST = math.log(I_HIGH / I_LOW) / D                     # outage after which the flame cannot relight
close(T_LOST, 10.317, tol=5e-3)
close(rk4(flame(1), rk4(flame(0), I_HIGH, 5), 100), I_HIGH)
assert rk4(flame(1), rk4(flame(0), I_HIGH, 30), 100) < 1e-6

# ---- (b) capacity learned by doing: dC/dt = lam * P * (1 - C) - mu * C, demand 1, domestic output tau * C --------
LAM, MU, TAU = 1.0, 0.3, 1.5
practice_sub = lambda c, a: min(TAU * c, max(0.0, 1 - a))  # aid A does the work first; domestic does the rest
cap_sub = lambda a: (lambda t, c: LAM * practice_sub(c, a) * (1 - c) - MU * c)
cap_first = lambda t, c: LAM * min(TAU * c, 1.0) * (1 - c) - MU * c  # aid only covers what domestic cannot
c_star = lambda a: LAM * (1 - a) / (LAM * (1 - a) + MU)

C0 = c_star(0)
close(C0, 0.7692)
for a, c in ((0.5, 0.625), (0.9, 0.25)):
    close(c_star(a), c)
    close(rk4(cap_sub(a), 0.5, 300), c)
assert rk4(cap_sub(1.0), 0.5, 300) < 1e-9                  # full substitution: capacity decays at mu to nothing


def after_exit(c, horizon=60.0, dt=0.01):
    """Service shortfall integrated after aid stops, and the time until domestic output meets demand."""
    t, gap, t_full = 0.0, 0.0, None
    while t < horizon:
        s = min(TAU * c, 1.0)
        gap += (1 - s) * dt
        if t_full is None and s >= 1 - 1e-9:
            t_full = t
        c = rk4(cap_sub(0.0), c, dt)
        t += dt
    return gap, t_full


rows = {}
for a, dur in ((0.5, 50), (0.9, 50), (1.0, 10), (1.0, 20), (1.0, 40)):
    c_exit = rk4(cap_sub(a), C0, dur)
    rows[(a, dur)] = (c_exit,) + after_exit(c_exit)
close(rows[(0.5, 50)][0], 0.625)
close(rows[(0.9, 50)][0], 0.25)
close(rows[(0.9, 50)][2], 2.00, tol=0.02)
close(rows[(1.0, 10)][0], C0 * math.exp(-MU * 10))
for dur, t_full in ((10, 3.84), (20, 6.38), (40, 11.38)):
    close(rows[(1.0, dur)][2], t_full, tol=0.02)
# Under full substitution each further unit of aid's duration adds mu / (lam * tau - mu) = 0.25 to the time to
# recover, because capacity shrinks as e^(-mu t) and regrows from a small seed at rate lam * tau - mu.
close((rows[(1.0, 40)][2] - rows[(1.0, 20)][2]) / 20, MU / (LAM * TAU - MU), tol=5e-3)

# Capacity-first aid leaves the learning untouched: from a seed of 0.05 capacity regrows as if there were no aid, and
# service is met throughout because aid covers 1 - tau * C while C is short.
close(rk4(cap_first, 0.05, 20), C0)
assert TAU * rk4(cap_first, 0.05, 5) >= 1

print("all supplied-maintenance toy numbers reproduce")
