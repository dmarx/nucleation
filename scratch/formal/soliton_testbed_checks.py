# scratch/formal/soliton_testbed_checks.py: reproduces and asserts the numbers of the constructions filed from the
# exchange "Explain String Theory" (2026-11-15): (a) the phi^4 kink's profile and energy, and that translated kinks
# share charge and energy; (b) the mutual-maintenance model dc/dt = -c + 4 s r c (1 - c), dr/dt = -r + 4 c (1 - r),
# its three equilibria and eigenvalues at s = 1, its joint-state threshold, a constant outside controller that holds
# r at r+, a founding pulse h(t), and withdrawal of the standing supply s.
# Run: python3 -I scratch/formal/soliton_testbed_checks.py
# The parameters are invented to show mechanisms; none is a measurement of any organization.
import math


def close(x, y, tol=5e-4):
    assert abs(x - y) <= tol, (x, y)


def integrate(f, y, t1, dt=1e-3):
    """Classical RK4 for a list-valued state."""
    t = 0.0
    while t < t1 - 1e-12:
        h = min(dt, t1 - t)
        k1 = f(t, y)
        k2 = f(t + h / 2, [a + h / 2 * b for a, b in zip(y, k1)])
        k3 = f(t + h / 2, [a + h / 2 * b for a, b in zip(y, k2)])
        k4 = f(t + h, [a + h * b for a, b in zip(y, k3)])
        y = [a + h / 6 * (p + 2 * q + 2 * r + w) for a, p, q, r, w in zip(y, k1, k2, k3, k4)]
        t += h
    return y


# ---- (a) the kink: E = int [k/2 phi'^2 + l/4 (phi^2 - v^2)^2] dx, phi_K = v tanh((x - X)/ell) ---------------------
K, L, V = 1.3, 0.7, 1.1
ELL = math.sqrt(2 * K / (L * V ** 2))


def kink_energy(x0, a=-40.0, b=40.0, n=200_000):
    h, total = (b - a) / n, 0.0
    for i in range(n + 1):
        x = a + i * h
        u = (x - x0) / ELL
        phi, dphi = V * math.tanh(u), V / ELL / math.cosh(u) ** 2
        w = 0.5 if i in (0, n) else 1.0
        total += w * (K / 2 * dphi ** 2 + L / 4 * (phi ** 2 - V ** 2) ** 2)
    return total * h


E_FORMULA = 2 * math.sqrt(2 * K * L) / 3 * V ** 3
close(kink_energy(0.0), E_FORMULA, 1e-6)
close(kink_energy(7.5), E_FORMULA, 1e-6)  # translated kink: same energy
# Static equation K phi'' = L phi (phi^2 - v^2), checked by finite differences at several points.
for x in (-1.7, -0.3, 0.0, 0.9, 2.4):
    d = 1e-4
    phi = lambda z: V * math.tanh(z / ELL)
    lhs = K * (phi(x + d) - 2 * phi(x) + phi(x - d)) / d ** 2
    close(lhs, L * phi(x) * (phi(x) ** 2 - V ** 2), 1e-5)
# Same boundary charge Q = (phi(+inf) - phi(-inf)) / 2v = 1 for any centre: the charge does not locate the kink.
for x0 in (0.0, 7.5):
    q = (V * math.tanh((40 - x0) / ELL) - V * math.tanh((-40 - x0) / ELL)) / (2 * V)
    close(q, 1.0, 1e-9)

# ---- (b) mutual maintenance ---------------------------------------------------------------------------------------
C_LO, C_HI = (3 - math.sqrt(5)) / 8, (3 + math.sqrt(5)) / 8
R = lambda c: 4 * c / (1 + 4 * c)
close(C_LO, 0.0955), close(R(C_LO), 0.2764), close(C_HI, 0.6545), close(R(C_HI), 0.7236)


def eig(c, r, s=1.0):
    a, b = -1 + 4 * s * r * (1 - 2 * c), 4 * s * c * (1 - c)
    cc, d = 4 * (1 - r), -1 - 4 * c
    tr, det = a + d, a * d - b * cc
    disc = math.sqrt(tr * tr - 4 * det)
    return sorted([(tr - disc) / 2, (tr + disc) / 2])


lo, hi = eig(C_LO, R(C_LO)), eig(C_HI, R(C_HI))
close(lo[0], -1.930, 1e-3), close(lo[1], 0.443, 1e-3)    # saddle
close(hi[0], -4.076, 1e-3), close(hi[1], -1.436, 1e-3)   # stable
assert eig(0.0, 0.0) == [-1.0, -1.0]                     # collapsed state stable


def mutual(s=1.0, h=lambda t: 0.0, r_pathway=True):
    def f(t, y):
        c, r = y
        dr = -r + (4 * c * (1 - r) if r_pathway else 0.0)
        return [-c + 4 * s * r * c * (1 - c) + h(t) * (1 - c), dr]
    return f


# The threshold is a property of the joint state: c = 0.12 > c_lo collapses when r = 0, survives when r = 0.3.
c, r = integrate(mutual(), [0.12, 0.0], 200)
assert c < 1e-6, c
c, r = integrate(mutual(), [0.12, 0.3], 200)
close(c, C_HI), close(r, R(C_HI))

# A constant outside controller holding r at r+ recovers from c = 0.01; the mutual system from (0.01, r+) collapses.
R_HI = R(C_HI)
c_ext = integrate(lambda t, y: [-y[0] + 4 * R_HI * y[0] * (1 - y[0])], [0.01], 200)[0]
close(c_ext, (4 * R_HI - 1) / (4 * R_HI))                # the controlled system's own equilibrium, = c+ here
close(c_ext, C_HI)
c, r = integrate(mutual(), [0.01, R_HI], 200)
assert c < 1e-6, c

# Disabling the c -> r pathway: the mutual system's r decays and c follows; the controlled system is untouched.
c, r = integrate(mutual(r_pathway=False), [C_HI, R_HI], 60)
assert c < 1e-3 and r < 1e-3, (c, r)

# Founding versus feeding: a pulse h on [0, 5) carries the collapsed state into the maintained basin and can be
# withdrawn; withdrawing the standing supply s (s = 0 gives dc/dt = -c) ends it.
c, r = integrate(mutual(h=lambda t: 1.0 if t < 5 else 0.0), [0.0, 0.0], 200)
close(c, C_HI), close(r, R_HI)
c, r = integrate(mutual(s=0.0), [C_HI, R_HI], 60)
assert c < 1e-6, c

print("soliton testbed checks: all passed")
