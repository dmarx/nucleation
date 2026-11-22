"""Tests for cbd.py. Run: python3 -I -m pytest -q scratch/studies/lead-182/test_cbd.py
(from the repository root; the test puts its own directory on sys.path)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cbd  # noqa: E402


def lo_table():
    # Lo, Sadrzadeh and Mansfield (2023), Table 1(a), rows in context order
    # (canni,hungry), (canni,alive), (herbi,hungry), (herbi,alive);
    # columns (A,A), (A,B), (B,A), (B,B) -> (++, +-, -+, --).
    return np.array([[0.402, 0.097, 0.097, 0.402],
                     [0.044, 0.455, 0.455, 0.044],
                     [0.345, 0.154, 0.154, 0.345],
                     [0.344, 0.155, 0.155, 0.344]])


def test_lo_violation_reproduces_0192():
    # Contents: q0=(p1,canni) q1=(p2,hungry) q2=(p1,herbi) q3=(p2,alive).
    # Cyclic contexts (q0,q1)=(canni,hungry), (q1,q2)=(herbi,hungry) with
    # answers swapped, (q2,q3)=(herbi,alive), (q3,q0)=(canni,alive) swapped.
    t = lo_table()
    swap = lambda r: r[[0, 2, 1, 3]]  # exchange the roles of the two answers
    sys4 = np.array([t[0], swap(t[2]), t[3], swap(t[1])])
    dc = cbd.delta_c(sys4)
    # Rows sum to 0.998 as printed; renormalised, the violation is 0.196.
    assert dc == pytest.approx(0.192, abs=0.005)
    e, delta = cbd.system_moments(sys4)
    assert delta == pytest.approx(0.0, abs=1e-9)  # symmetric by construction


def test_lo_standard_deviation_about_0176():
    # About 87 valid responses a context (348 / 4); the paper's bootstrap SD is 0.176.
    t = lo_table()
    swap = lambda r: r[[0, 2, 1, 3]]
    sys4 = np.array([t[0], swap(t[2]), t[3], swap(t[1])])
    e, _ = cbd.system_moments(sys4)
    sd = np.sqrt(((1 - e ** 2) / 87).sum())
    assert sd == pytest.approx(0.176, abs=0.005)


@pytest.mark.parametrize("dc,signal,base", [(0.19, 0.0, 0.0), (0.0, 0.3, 0.0),
                                            (-0.15, 0.6, 0.0), (0.1, 0.3, 0.15)])
def test_true_system_hits_targets(dc, signal, base):
    P = cbd.true_system(dc, signal, base)
    assert P is not None
    assert np.allclose(P.sum(axis=1), 1)
    assert cbd.delta_c(P, (1, 1, 1, -1)) == pytest.approx(dc)
    assert cbd.delta_c(P) == pytest.approx(dc)  # the fixed pattern is the maximising one
    _, delta = cbd.system_moments(P)
    assert delta == pytest.approx(signal)


def test_pr_box_is_maximally_contextual_without_signalling():
    pr = cbd.true_system(2.0, 0.0)  # e = 1
    assert cbd.delta_c(pr) == pytest.approx(2.0)


def test_product_of_marginals_is_noncontextual():
    rng = np.random.default_rng(0)
    for _ in range(200):
        m = rng.uniform(-1, 1, size=(4, 2))
        P = np.array([cbd.cells_from_moments(a, b, a * b) for a, b in m])
        assert cbd.delta_c(P) <= 1e-9


def test_fixed_signs_must_be_odd():
    with pytest.raises(ValueError):
        cbd.delta_c(np.full((4, 4), 0.25), (1, 1, 1, 1))


def test_wald_se_matches_simulation_spread_when_signalling_is_clear():
    rng = np.random.default_rng(1)
    P = cbd.true_system(0.19, 0.6)  # signalling 1.0 with this e is infeasible
    n = 1000
    counts = np.stack([rng.multinomial(n, P[k], size=4000) for k in range(4)], axis=1)
    est = cbd.delta_c(counts, (1, 1, 1, -1))
    lo, hi = cbd.wald_bounds(counts, 1.0, (1, 1, 1, -1))
    se = ((hi - lo) / 2).mean()
    assert se == pytest.approx(est.std(), rel=0.1)


def test_bootstrap_bounds_shape_and_order():
    rng = np.random.default_rng(2)
    P = cbd.true_system(0.19, 0.0)
    counts = np.stack([rng.multinomial(200, P[k], size=5) for k in range(4)], axis=1)
    q = cbd.bootstrap_bounds(counts, rng, 199, [0.05, 0.95], (1, 1, 1, -1))
    assert q.shape == (2, 5)
    assert (q[0] <= q[1]).all()


def test_wald_se_overstates_spread_near_zero_signalling():
    # |m - m'| folds the noise when the true difference is near zero, so the
    # statistic is less variable (and biased downward) than the delta method says.
    rng = np.random.default_rng(3)
    P = cbd.true_system(0.19, 0.0)
    counts = np.stack([rng.multinomial(400, P[k], size=4000) for k in range(4)], axis=1)
    est = cbd.delta_c(counts, (1, 1, 1, -1))
    lo, hi = cbd.wald_bounds(counts, 1.0, (1, 1, 1, -1))
    assert ((hi - lo) / 2).mean() > 1.1 * est.std()
    assert est.mean() < 0.19 - 0.05


def test_pooling_label_orders_can_create_contextuality():
    # Two noncontextual systems with the same correlations and opposite
    # direct influences: pooled, the influences cancel and the pooled system
    # is contextual. So counterbalancing cells must be analysed apart.
    e, h = 0.65, 0.075                     # s_odd = 2.6, Delta = 8h = 0.6
    signs = (1, 1, 1, -1)
    P1 = np.array([cbd.cells_from_moments(h, -h, signs[k] * e) for k in range(4)])
    P2 = np.array([cbd.cells_from_moments(-h, h, signs[k] * e) for k in range(4)])
    assert cbd.delta_c(P1) == pytest.approx(0.0)
    assert cbd.delta_c(P2) == pytest.approx(0.0)
    assert cbd.delta_c(cbd.mixture(P1, P2)) == pytest.approx(0.6)


def test_shrink_reduces_signalling_estimate():
    rng = np.random.default_rng(4)
    P = cbd.true_system(0.0, 0.0)
    counts = np.stack([rng.multinomial(400, P[k], size=2000) for k in range(4)], axis=1)
    _, d0 = cbd.system_moments(counts)
    _, d1 = cbd.system_moments(counts, shrink=1.0)
    assert d1.mean() < 0.25 * d0.mean()
    # the plug-in bias at zero signalling is about 4 * sqrt(2/n) * sqrt(2/pi)
    assert d0.mean() == pytest.approx(4 * np.sqrt(2 / 400) * np.sqrt(2 / np.pi), rel=0.05)


def test_absence_bound_is_conservative_on_the_boundary():
    rng = np.random.default_rng(5)
    for sig in (0.0, 0.3, 0.6):
        P = cbd.true_system(0.0, sig)
        counts = np.stack([rng.multinomial(400, P[k], size=3000) for k in range(4)], axis=1)
        assert (cbd.absence_upper_bound(counts, (1, 1, 1, -1)) < 0).mean() < 0.05
