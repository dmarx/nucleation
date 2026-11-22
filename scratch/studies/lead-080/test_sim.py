"""Tests for the LEAD-080 simulator: python3 -I -m pytest -q -p no:cacheprovider ."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sim  # noqa: E402
from sim import Params, simulate, next_budget, draw_calls, MONTH  # noqa: E402


def call(t, need, says, A=5.0, T=10.0, Tma=30.0, work=60.0):
    return dict(t=t, need=need, says=says, A=A, T=T, Tma=Tma, work=work)


def test_budget_rules():
    P = Params()
    assert next_budget("spend-matching", 1.3, 0.7, P) == 0.7
    assert next_budget("peak-carry", 1.3, 0.7, replace_rho(P, 1.0)) == pytest.approx(1.3)
    assert next_budget("peak-carry", 1.3, 0.7, replace_rho(P, 0.6)) == pytest.approx(1.06)
    # CASE-200's numbers: Bbar 1.0, 0.3 unspent, full rollover -> 1.3
    assert next_budget("base-carry", 1.0, 0.7, replace_rho(P, 1.0)) == pytest.approx(1.3)
    assert next_budget("base-carry", 1.0, 0.7, replace_rho(P, 0.6)) == pytest.approx(1.18)


def replace_rho(P, rho):
    from dataclasses import replace
    return replace(P, rho=rho)


def test_quiet_month_forecloses_under_spend_matching():
    """CLAIM-577 step 3: one quiet month and the budget is the holding cost,
    after which no squad can be mobilized, drills included, for good."""
    P = Params(months=24, drill_every=0)
    late = [call(5 * MONTH + 500.0, True, True)]
    r = simulate(P, late)
    assert r["B"][1] == pytest.approx(0.7)
    assert np.all(r["B"][1:] == pytest.approx(0.7))
    assert r["tot"]["blocked"] == 1 and r["tot"]["met"] == 0
    # monthly drills keep the peak observed, so the budget holds
    r2 = simulate(Params(months=24, drill_every=1), late)
    assert np.all(r2["B"] == pytest.approx(1.3))
    assert r2["tot"]["met"] == 1


def test_spend_matching_budget_never_rises():
    """CLAIM-577 step 1, on random histories."""
    for i in range(30):
        P = Params(months=60, lam=3.0, policy=("provisional", "confirm")[i % 2],
                   drill_every=i % 4)
        rng = np.random.default_rng(i)
        B = simulate(P, draw_calls(P, rng))["B"]
        assert np.all(np.diff(B) <= 1e-12)


def test_full_peak_carry_holds_budget():
    P = Params(months=60, regime="peak-carry", rho=1.0, drill_every=0)
    rng = np.random.default_rng(1)
    B = simulate(P, draw_calls(P, rng))["B"]
    assert np.allclose(B, 1.3)


def test_base_carry_after_use_skips_a_month():
    """Under CASE-200's rule a month spent at the peak leaves 1.0 next month."""
    P = Params(months=4, regime="base-carry", rho=1.0, drill_every=1)
    r = simulate(P, [])
    # month 0: B=1.3, drill -> s=1.3 -> B1 = 1.0; month 1: drill blocked ->
    # s=0.7 -> B2 = 1.3; month 2: drill -> B3 = 1.0
    assert list(np.round(r["B"], 6)) == [1.3, 1.0, 1.3, 1.0, 1.3]
    assert r["tot"]["drills"] == 2 and r["tot"]["drills_blocked"] == 2


def test_timing_provisional_vs_confirm():
    """CASE-213: provisional dispatch arrives at max(A, T), confirmation at
    A + T. With A = 5, T = 10, deadline 12: provisional meets, confirm misses."""
    c = [call(100.0, True, True, A=5.0, T=10.0)]
    for pol, met in (("provisional", 1), ("confirm", 0)):
        r = simulate(Params(months=1, policy=pol, deadline=12.0, regime="peak-carry", drill_every=0), c)
        assert r["tot"]["met"] == met
    # A > T: the squad is on scene first and sees the need itself
    c2 = [call(100.0, True, False, A=12.0, T=8.0)]
    r = simulate(Params(months=1, policy="provisional", deadline=10.0, regime="peak-carry", drill_every=0), c2)
    assert r["tot"]["met"] == 1


def test_cancellation_counts_as_peak_spending():
    """A cancelled provisional dispatch occupies the squad and so the peak."""
    c = [call(100.0, False, False, A=5.0, T=10.0)]
    r = simulate(Params(months=2, policy="provisional", drill_every=0), c)
    assert r["tot"]["cancelled"] == 1
    assert r["s"][0] == pytest.approx(1.3) and r["B"][1] == pytest.approx(1.3)
    # under confirmation nothing is sent, and the budget falls
    r = simulate(Params(months=2, policy="confirm", drill_every=0), c)
    assert r["B"][1] == pytest.approx(0.7)


def test_skill_decay_half_life():
    """delta = 0.09 a month: half of skill lost in about 7.4 months."""
    P = Params(months=12, drill_every=0, regime="peak-carry")
    k = simulate(P, [])["k"]
    assert k[7] > 0.5 > k[8]


def test_unqualified_squad_fails():
    P = Params(months=10, drill_every=0, regime="peak-carry")
    r = simulate(P, [call(9 * MONTH + 1.0, True, True, A=5.0, T=10.0)])
    assert r["k"][9] < 0.5 and r["tot"]["met"] == 0 and r["tot"]["needed"] == 1


def test_two_squads_second_needs_more_budget():
    P = Params(months=1, n_squads=2, drill_every=0, regime="spend-matching")
    c = [call(100.0, True, True, work=600.0), call(200.0, True, True, work=600.0)]
    r = simulate(P, c)
    assert r["s"][0] == pytest.approx(1.9) and r["tot"]["needed"] == 2


def test_lost_for_good():
    full = 1.3
    assert sim.lost_for_good(np.array([1.3] * 3 + [0.7] * 20), full) == 3
    assert sim.lost_for_good(np.array([1.3, 1.0] * 20), full) is None
    assert sim.lost_for_good(np.array([1.3] * 20), full) is None


def test_loss_probability_formula():
    """Under spend-matching with provisional dispatch and no drills, every
    call mobilizes the squad, so a month is quiet with chance exp(-lam) and
    the chance of loss for good within the first 12 months of a 24-month run
    is 1 - (1 - exp(-lam))**12."""
    lam, months, seeds = 3.0, 24, 2000
    P = Params(months=months, lam=lam, drill_every=0, policy="provisional")
    lost = 0
    for i in range(seeds):
        rng = np.random.default_rng([7, i])
        B = simulate(P, draw_calls(P, rng))["B"][:months]
        lost += sim.lost_for_good(B, 1.3) is not None
    expect = 1 - (1 - np.exp(-lam)) ** 12
    se = np.sqrt(expect * (1 - expect) / seeds)
    assert abs(lost / seeds - expect) < 3.5 * se


def test_base_carry_multi_period_threshold():
    """CASE-200's recursion from B = 1.0: one period of saving reaches 1.3
    only with rho - alpha = 1, but rho - alpha = 0.6 reaches it in three
    periods, and 0.5 or less never does (fixed point (1 - 0.7r)/(1 - r))."""
    f = sim.base_carry_periods_to_reach
    assert f(1.0, 1.0, 0.7, 1.3, 1.0) == 1
    assert f(1.0, 0.6, 0.7, 1.3, 1.0) == 3
    assert f(1.0, 0.5, 0.7, 1.3, 1.0) is None
    assert f(1.0, 0.4, 0.7, 1.3, 1.0) is None
