import numpy as np

from twisted import descend, energy_and_winding, twisted_stable


def test_twisted_state_is_fixed_point_with_positive_energy():
    l = 6
    th = 2 * np.pi * np.arange(l) / l
    alpha = np.zeros(l)
    th2 = descend(th + 1e-3 * np.sin(np.arange(l)), alpha, steps=4000)
    e, w = energy_and_winding(th2, alpha)
    assert w == 1
    assert abs(e - l * (1 - np.cos(2 * np.pi / l))) < 1e-6


def test_stability_threshold_is_five():
    assert not twisted_stable(4, 1)
    assert twisted_stable(5, 1)


def test_triangle_and_square_relax_to_zero():
    rng = np.random.default_rng(1)
    for l in (3, 4):
        for _ in range(10):
            th = descend(rng.uniform(0, 2 * np.pi, l), np.zeros(l))
            e, _ = energy_and_winding(th, np.zeros(l))
            assert e < 1e-6
