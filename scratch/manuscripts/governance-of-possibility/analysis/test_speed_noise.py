# scratch/manuscripts/governance-of-possibility/analysis/test_speed_noise.py
"""The speed-noise product of a first-order filter (CLAIM-tmpm9sp7, §4).

For dz = k(d + n - z) dt with n white noise of intensity sigma^2, the time to
come within delta of a unit step is t = ln(1/delta)/k, and the stationary
variance is k sigma^2 / 2, so t * Var = sigma^2 ln(1/delta) / 2 whatever k is.
Run: python3 -I -m pytest -q -p no:cacheprovider test_speed_noise.py
"""
import math

import numpy as np


def step_time(k: float, delta: float, dt: float = 1e-4) -> float:
    """Time for z to come within delta of a unit step, by Euler integration."""
    z, t = 0.0, 0.0
    while 1.0 - z > delta:
        z += k * (1.0 - z) * dt
        t += dt
    return t


def stationary_variance(k: float, sigma: float, steps: int = 800_000,
                        seed: int = 0) -> float:
    """Exact-discretization Ornstein-Uhlenbeck run; sample variance after burn-in.

    The step is scaled to the correlation time 1/k, so every rate gets about
    8,000 correlation times and the estimate's sampling error is about 2%.
    """
    dt = 0.02 / k
    rng = np.random.default_rng(seed)
    a = math.exp(-k * dt)
    s = sigma * math.sqrt(k * (1 - a * a) / 2)
    z = np.empty(steps)
    z[0] = 0.0
    noise = rng.normal(0.0, s, steps)
    for i in range(1, steps):
        z[i] = a * z[i - 1] + noise[i]
    return float(z[steps // 10:].var())


def test_step_time_matches_formula():
    for k in (0.2, 1.0, 5.0):
        assert abs(step_time(k, 0.05) - math.log(20) / k) < 2e-3 / k + 1e-3


def test_product_is_independent_of_rate():
    sigma, delta = 1.0, 0.05
    target = sigma ** 2 * math.log(1 / delta) / 2
    for k in (0.5, 1.0, 4.0):
        prod = (math.log(1 / delta) / k) * stationary_variance(k, sigma)
        assert abs(prod - target) / target < 0.06, (k, prod, target)


def test_negative_control_product_moves_with_sigma():
    """The invariant is in k, not in sigma: doubling sigma quadruples it."""
    k, delta = 1.0, 0.05
    p1 = (math.log(1 / delta) / k) * stationary_variance(k, 1.0)
    p2 = (math.log(1 / delta) / k) * stationary_variance(k, 2.0)
    assert 3.6 < p2 / p1 < 4.4
