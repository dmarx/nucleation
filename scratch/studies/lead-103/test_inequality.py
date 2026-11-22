"""Tests for LEAD-103 inequality study. Run: python3 -I -m pytest -q"""
import numpy as np
import inequality as M


def test_nc_bound_is_one_on_every_diamond_face():
    for obj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        r = M.nc_bound_lp(obj)
        assert r.success
        assert abs((-r.fun) - 1.0) < 1e-7, (obj, -r.fun)


def test_qubit_orbit_satisfies_equivalences():
    x = z = 1 / np.sqrt(2)
    exX, exZ, oe2 = M.qubit_orbit(x, z)
    # OE1: equal predictability magnitudes
    assert max(abs(abs(v) - x) for v in exX) < 1e-9
    assert max(abs(abs(v) - z) for v in exZ) < 1e-9
    # OE2: the two equal mixtures coincide exactly (both the maximally mixed)
    assert oe2 < 1e-12


def test_qubit_violates_bound_up_to_sqrt2():
    x = z = 1 / np.sqrt(2)
    assert x + z > 1.0 + 1e-9
    assert abs((x + z) - np.sqrt(2)) < 1e-9


def test_general_search_respects_bound():
    best = M.nc_bound_general(trials=40, K=5, seed=3)
    assert best <= 1.0 + 1e-4


def test_dropping_equivalence_removes_bound():
    r = M.nc_bound_lp_no_oe2()
    assert r.success
    assert (-r.fun) > 1.5  # reaches x=z=1 -> x+z=2 without OE2
