"""scratch/formal/forced_stuart_landau_check.py

Rebuilds the numbers of CASE-225 (a forced Stuart-Landau oscillator with an
inhibitory control) from the case's text; the reader's rerun was not kept.
Written at the recomputation pass of 2026-11-25 by a session other than
the filer's. Run: python3 -I this file. numpy and scipy.

Model: z' = (mu - u + i omega - |z|^2) z + F e^{i Omega t}, with
mu = 0.5, u = 1, omega = 1, F = 0.02, Omega = 1.3 (the case's rerun).
Checks: the driven amplitude under control against F/sqrt((u - mu)^2 +
(Omega - omega)^2) = 0.03430; removing F with u kept, the output decays
to rest; removing F and u, the limit cycle of radius sqrt(mu) returns;
with u = 0, a self-sustained (mu = 0.5) and a damped (mu = -0.5)
oscillator both answer the drive at its frequency, and only the
withdrawal of the drive tells them apart.
"""
import math

import numpy as np
from scipy.integrate import solve_ivp


def sl(mu, u, om, F, Om):
    def f(t, y):
        z = y[0] + 1j * y[1]
        dz = (mu - u + 1j * om - abs(z) ** 2) * z + F * np.exp(1j * Om * t)
        return [dz.real, dz.imag]
    return f


def run(f, y0, T, n=4000):
    r = solve_ivp(f, (0, T), y0, rtol=1e-10, atol=1e-13, dense_output=True)
    ts = np.linspace(T - 50, T, n)
    z = r.sol(ts)
    return np.abs(z[0] + 1j * z[1]), r.y[:, -1], ts, z


mu, u, om, F, Om = 0.5, 1.0, 1.0, 0.02, 1.3
pred = F / math.hypot(u - mu, Om - om)
amp, y, _, _ = run(sl(mu, u, om, F, Om), [0.01, 0.0], 400)
a = amp.mean()
assert abs(pred - 0.03430) < 5e-6 and abs(a - pred) < 2e-4, (a, pred)
print(f"driven amplitude under control {a:.5f} against predicted {pred:.5f} (case: 0.03428, 0.03430)")

amp_rest, _, _, _ = run(sl(mu, u, om, 0.0, Om), y, 400)
assert amp_rest[-1] < 1e-8  # to rest, down to the integrator's tolerance (the case gives 4e-36)
print(f"drive removed, control kept: |z| = {amp_rest[-1]:.1e}")

amp_lc, _, _, _ = run(sl(mu, 0.0, om, 0.0, Om), y, 400)
assert abs(amp_lc[-1] - math.sqrt(mu)) < 1e-3
print(f"drive and control removed: |z| = {amp_lc[-1]:.4f} against sqrt(mu) = {math.sqrt(mu):.4f}")

# without control, self-sustained and damped both lock to the drive (F large enough to lock)
Fl = 0.3
for m in (0.5, -0.5):
    _, _, ts, z = run(sl(m, 0.0, om, Fl, Om), [0.1, 0.0], 600)
    phase = np.unwrap(np.angle(z[0] + 1j * z[1]))
    freq = (phase[-1] - phase[0]) / (ts[-1] - ts[0])
    assert abs(freq - Om) < 1e-3, (m, freq)
    _, yend, _, _ = run(sl(m, 0.0, om, Fl, Om), [0.1, 0.0], 600)
    amp_after, _, _, _ = run(sl(m, 0.0, om, 0.0, Om), yend, 300)
    print(f"mu = {m:+.1f}: locked to the drive (frequency {freq:.4f}); drive removed: |z| -> {amp_after[-1]:.4f}")
    assert (amp_after[-1] > 0.7) if m > 0 else (amp_after[-1] < 1e-6)
print("checks pass")
