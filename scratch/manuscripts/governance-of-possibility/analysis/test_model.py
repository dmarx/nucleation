# scratch/manuscripts/governance-of-possibility/analysis/test_model.py
"""Tests: python3 -I -m pytest -q -p no:cacheprovider test_model.py"""
from __future__ import annotations

import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as m  # noqa: E402

THETAS = (1.0, 1.25, 1.5, 2.0, 2.5, 3.0)


def reached(reg: m.Regime, quiet: int = 5, reps: int = 50, g: float = 0.0) -> float:
    """Share of imposed contingencies met within 60 periods."""
    t = m.impose(reg, reps, quiet=quiet, horizon=60, g=g)
    return float((t <= 60).mean())


def test_budget_rules():
    reg = m.regimes()
    assert m.next_budget(reg["I"], 3.0, 1.0, True) == 1.0
    assert m.next_budget(reg["II"], 3.0, 1.0, True) == 3.0
    assert m.next_budget(reg["II"], 3.0, 1.0, False) == 1.0   # lapsed
    assert m.next_budget(reg["V"], 3.0, 3.0, True) == pytest.approx(1.5)
    assert m.next_budget(reg["V"], 1.5, 1.0, True) == pytest.approx(2.0)
    assert m.next_budget(reg["V"], 3.0, 1.0, True) == pytest.approx(3.0)  # cap


def test_thresholds_are_least_peak():
    """CLAIM-571: a path's threshold is its peak, an architecture's the least."""
    assert m.ORIGINAL.threshold == 3.0
    assert m.staged(2.0).threshold == 2.0
    assert m.staged(0.5).threshold == 1.0          # never below the endpoints
    assert m.regimes(2.0)["III-a"].threshold == 2.0


def test_claim_577_budget_never_rises():
    """Step 1: under the peak rule with no outside money B_{t+1} <= B_t,
    on random contingency histories."""
    for sd in range(6):
        for k in ("I", "III-a"):
            x = m.run(m.regimes(2.0)[k], 0.05 * (sd + 1), 600, sd, g=0.0)
            assert np.all(np.diff(x["B"]) <= 1e-12)


def test_claim_577_one_holding_period_forecloses():
    """Step 3: a transition with threshold above r(A) is lost after one
    holding period, for good, unless money comes from outside (step 4)."""
    I = m.regimes()["I"]
    org = m.Org(I, [1], g=0.0)
    org.step()
    assert org.B == m.HOLD
    for _ in range(200):
        org.step()
    assert org.B == m.HOLD
    assert reached(I, quiet=1) == 0.0          # negative control: it fails
    assert reached(I, quiet=1, g=0.2) == 1.0   # outside money restores it


@pytest.mark.parametrize("theta", THETAS)
def test_claim_tmpg8yl2_kept_exactly_when_threshold_at_most_holding(theta):
    """Under the peak rule a redesigned route is kept after holding exactly
    when its threshold is <= r(A); otherwise it needs a reserve theta - r(A)."""
    IIIa = m.regimes(theta)["III-a"]
    assert (reached(IIIa) == 1.0) == (theta <= m.HOLD)
    assert (reached(IIIa) == 0.0) == (theta > m.HOLD)
    for F in np.arange(1.0, 3.01, 0.25):
        reg = m.Regime("floor", IIIa.paths, "floor", floor=float(F))
        assert (reached(reg, reps=20) == 1.0) == (F >= theta - 1e-9), (theta, F)


def test_claim_tmpg8yl2_original_needs_full_reserve():
    for F in np.arange(1.0, 3.01, 0.25):
        reg = m.Regime("floor", (m.ORIGINAL,), "floor", floor=float(F))
        assert (reached(reg, reps=20) == 1.0) == (F >= 3.0)


def test_present_output_matched():
    """Output is 1 every period with no contingency, in every regime, and
    identical across regimes before the first contingency on a shared seed."""
    regs = m.regimes(2.0)
    for reg in regs.values():
        assert np.all(m.run(reg, 0.0, 300, 0)["output"] == 1.0)
    runs = [m.run(reg, 0.02, 2000, 3) for reg in regs.values()]
    first = int(runs[0]["first"][0])
    assert first > 0 and all(int(r["first"][0]) == first for r in runs)
    for r in runs:
        assert np.all(r["output"][:first] == 1.0)


def test_drill_holds_budget_at_staged_threshold():
    """IV: drilling each period keeps the peak at theta', so the rule itself
    funds the route; its capacity cost equals III-b's reserve."""
    regs = m.regimes(2.0)
    x = m.run(regs["IV"], 0.0, 200, 0)
    assert np.all(x["B"][1:] == 2.0)
    y = m.run(regs["III-b"], 0.0, 200, 0)
    assert x["cap"][1:].mean() == pytest.approx(y["cap"][1:].mean())
    assert reached(regs["IV"]) == 1.0


def test_negative_control_sparse_drill_fails():
    """A drill every second period cannot hold the peak rule: the first
    undrilled period drops the budget to holding, and the drill with it."""
    IV2 = m.replace(m.regimes(2.0)["IV"], drill_every=2)
    x = m.run(IV2, 0.0, 50, 0)
    assert np.all(x["B"][2:] == m.HOLD)
    assert reached(IV2) == 0.0


def test_lapsing_reserve_becomes_peak_rule():
    II = m.replace(m.regimes()["II"], revoke=1.0)
    assert reached(II, quiet=3) == 0.0


def test_carry_over_rebuilds_after_use():
    """CASE-200's rule with Bbar = 1.5: spent at the peak it falls to 1.5,
    then rebuilds 0.5 a held period to the cap."""
    V = m.regimes()["V"]
    seq = [3.0]
    for s in (3.0, 1.0, 1.0, 1.0, 1.0):
        seq.append(m.next_budget(V, seq[-1], s, True))
    assert seq[1:] == pytest.approx([1.5, 2.0, 2.5, 3.0, 3.0])


def test_imposed_readiness_matches_exact():
    """II's imposed readiness is the negative binomial of the original path."""
    ts = np.arange(1, 15)
    t = m.impose(m.regimes()["II"], 3000, quiet=5, g=0.0)
    R = m.readiness(t, ts)
    E = m.exact_readiness(m.ORIGINAL, ts)
    se = np.sqrt(E * (1 - E) / 3000) + 1e-3
    assert np.all(np.abs(R - E) < 4 * se)


def test_reserve_between_thresholds_buys_nothing():
    """CLAIM-679 in the readiness curve: a reserve below the threshold gives
    exactly the readiness of no reserve (common random numbers)."""
    ts = np.arange(0, 30)
    base = m.readiness(m.impose(m.Regime("f", (m.ORIGINAL,), "floor", floor=1.0),
                                300, g=0.1), ts)
    for F in (1.5, 2.0, 2.99):
        R = m.readiness(m.impose(m.Regime("f", (m.ORIGINAL,), "floor", floor=F),
                                 300, g=0.1), ts)
        assert np.array_equal(R, base)


def test_break_even_monotone_in_pL():
    """At fixed p, tau and c the reserve (II) is preferred to the peak rule
    (I) on an upward-closed set of L, so on an upward-closed set of p*L, and
    the switch is at pL* = c * dcap / dlate * p."""
    regs = m.regimes()
    for p in (0.01, 0.05):
        a = [m.run(regs["II"], p, 3000, sd) for sd in range(2)]
        b = [m.run(regs["I"], p, 3000, sd) for sd in range(2)]
        cap_a = np.mean([x["cap"].mean() for x in a])
        cap_b = np.mean([x["cap"].mean() for x in b])
        for tau in (3, 6, 12):
            la = sum((x["resp"] > tau).sum() for x in a) / 6000
            lb = sum((x["resp"] > tau).sum() for x in b) / 6000
            assert lb > la
            for c in (0.05, 0.2):
                Ls = np.linspace(0, 400, 81)
                pref = [c * cap_a + L * la <= c * cap_b + L * lb for L in Ls]
                k = pref.index(True)
                assert all(pref[k:]) and not any(pref[:k])
                Lstar = c * (cap_a - cap_b) / (lb - la)
                assert Ls[k - 1] < Lstar <= Ls[k] + 1e-9


def test_dominance_classifier():
    a, b = np.array([0, .5, 1.]), np.array([0, .4, 1.])
    assert m.dominance(a, b) == "dominates"
    assert m.dominance(b, a) == "dominated"
    assert m.dominance(a, a) == "equal"
    assert m.dominance(np.array([.2, .4]), np.array([.1, .6])) == "cross"


def test_novel_demand_scoring():
    """CLAIM-361: excision scores perfectly on D0 and on the organization's
    own specification while the harm runs on; revision shows violations on
    both, and only the true demand set ranks them correctly. Under the peak
    rule a review that needs capacity cannot start, so the demand is excised
    by default."""
    regs = m.regimes(2.0)
    ex = m.novel_demand(regs["II"], "excise", 20)
    rv = m.novel_demand(regs["II"], "revise", 20)
    assert ex["d0_violations"] == 0 and ex["own_spec_violations"] == 0
    assert ex["harm_periods"] == 120 and ex["reached_C"] == 0
    assert rv["reached_C"] == 1 and rv["harm_periods"] < 20
    assert rv["d0_violations"] > 0
    pk = m.novel_demand(regs["I"], "revise", 20, review_cost=0.5)
    assert pk["revised"] == 0 and pk["harm_periods"] == 120
    free = m.novel_demand(regs["I"], "revise", 20, review_cost=0.0)
    assert free["revised"] == 1
    # without outside money the review crowds out IV's drill, and the route
    nm = m.novel_demand(regs["IV"], "revise", 20, review_cost=0.5, g=0.0)
    assert nm["B_end"] == m.HOLD and nm["reached_C"] == 0
