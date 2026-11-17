# scratch/formal/pinned_kink_run.py: an executed run of the pinned kink proposed for QUESTION-438 (A5 §7 of the
# exchange "Explain String Theory"). Allen–Cahn gradient flow d(phi)/dt = k phi'' - l phi (phi^2 - v^2) - 2 a g(x) phi
# on [-L, L] with phi(-L) = -v, phi(L) = +v; g is a Gaussian bump at 0, so a > 0 adds the energy term
# a * int g (phi^2 - v^2), which is lowest when the kink's core sits on the bump. The demand "the kink's centre lies
# in [-0.5, 0.5]" is feasible with and without pinning (the centred kink is a static solution either way); the run
# shows it is attracting only with pinning, and that the boundary charge Q = 1 is the same throughout.
# Filed by the assistant at the owner's request (2026-11-15). Run: python3 -I scratch/formal/pinned_kink_run.py
import numpy as np

K, LAM, V, L, N = 1.0, 2.0, 1.0, 20.0, 801
x = np.linspace(-L, L, N)
dx = x[1] - x[0]
ELL = np.sqrt(2 * K / (LAM * V ** 2))
g = np.exp(-x ** 2 / 2.0)


def centre(phi):
    i = np.where(np.diff(np.sign(phi)) > 0)[0][0]
    return x[i] - phi[i] * dx / (phi[i + 1] - phi[i])


def relax(x0, a, t1=200.0, dt=0.2 * dx ** 2):
    phi = V * np.tanh((x - x0) / ELL)
    for _ in range(int(t1 / dt)):
        lap = np.zeros_like(phi)
        lap[1:-1] = (phi[2:] - 2 * phi[1:-1] + phi[:-2]) / dx ** 2
        phi[1:-1] += dt * (K * lap[1:-1] - LAM * phi[1:-1] * (phi[1:-1] ** 2 - V ** 2) - 2 * a * g[1:-1] * phi[1:-1])
    return phi


for a in (0.0, 0.3):
    for x0 in (0.0, 2.0):
        phi = relax(x0, a)
        q = (phi[-1] - phi[0]) / (2 * V)
        print(f"pinning a={a}: start centre {x0:+.1f} -> centre {centre(phi):+.3f}, charge Q={q:.3f}")
        assert abs(q - 1) < 1e-9
        if x0 == 0.0:
            assert abs(centre(phi)) < 1e-3            # the centred kink is a static solution: the demand is feasible
        elif a == 0.0:
            assert abs(centre(phi) - x0) < 0.05       # unpinned: no restoring force, the centre stays put
        else:
            assert abs(centre(phi)) < 0.5             # pinned: it returns into the demanded interval
print("pinned kink run: all passed")
