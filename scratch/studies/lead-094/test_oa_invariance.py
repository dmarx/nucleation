import numpy as np

from oa_invariance import invariance_defect


def test_first_harmonic_family_is_invariant():
    for alpha in (0.0 + 0j, 0.3 + 0.2j, -0.7j, 0.95 + 0j):
        assert invariance_defect(alpha, 0.8, 1.1 - 0.4j, 0j) < 1e-12


def test_second_harmonic_breaks_invariance_inside_disc():
    assert invariance_defect(0.5 + 0.1j, 0.8, 1.1 - 0.4j, 0.2 + 0.1j) > 1e-3


def test_second_harmonic_defect_vanishes_on_unit_circle():
    assert invariance_defect(np.exp(1.3j), 0.8, 1.1 - 0.4j, 0.2 + 0.1j) < 1e-12
