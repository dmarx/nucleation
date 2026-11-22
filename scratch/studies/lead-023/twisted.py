"""Local minima of the XY energy on an l-cycle of contexts with zero monodromy.

For LEAD-023's note on CLAIM-153, from Bacic et al. (LIT-2253) and Manik et al.
(LIT-2267): on a cycle of l units with zero offsets, a twisted state of winding
z (every edge difference 2*pi*z/l) is a fixed point; it is stable when every
edge difference is below pi/2, so for z = 1 when l >= 5. Its energy
l*(1 - cos(2*pi*z/l)) is positive although the monodromy is zero, so a local
search for the minimum of CLAIM-153's energy can report an obstruction that is
not there once the cycle has five or more contexts.

Rerun: python3 -I twisted.py   (prints, per l, the end states of gradient
descent from random starts: Counter of (energy, winding)).
Test:  python3 -I -m pytest test_twisted.py
"""
from collections import Counter

import numpy as np


def energy_and_winding(th, alpha):
    d = np.roll(th, -1) - th - alpha
    e = float(np.sum(1 - np.cos(d)))
    w = int(round(float(np.sum(np.angle(np.exp(1j * d)))) / (2 * np.pi)))
    return e, w


def descend(th, alpha, steps=6000, dt=0.05):
    th = th.copy()
    for _ in range(steps):
        s = np.sin(np.roll(th, -1) - th - alpha)
        th -= dt * (-s + np.roll(s, 1))
    return th


def twisted_stable(l, z):
    """Linear stability of the twisted state on an l-ring: all edge cosines > 0."""
    return np.cos(2 * np.pi * z / l) > 1e-12  # l = 4 sits at pi/2, marginal


def survey(l, phi=0.0, starts=60, seed=0):
    rng = np.random.default_rng(seed)
    alpha = np.full(l, phi / l)
    out = Counter()
    for _ in range(starts):
        th = descend(rng.uniform(0, 2 * np.pi, l), alpha)
        e, w = energy_and_winding(th, alpha)
        out[(round(e, 3), w)] += 1
    return out


if __name__ == '__main__':
    for l in (3, 4, 5, 6, 8):
        print(l, dict(survey(l)))
