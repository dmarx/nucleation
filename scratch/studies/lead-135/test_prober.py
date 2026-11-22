"""Tests for LEAD-135's individuation-by-probing prober.

Run:  python3 -I -m pytest -q
"""
import pytest

import prober as P


def test_seed_static_family_agrees():
    """At budget 0 (the static probe family) the seed pair is indistinguishable
    (CASE-202: 'agree under a restricted set of observable interactions')."""
    a, b = P.seed_pair()
    assert a.demand_reachability(0) == b.demand_reachability(0)


def test_seed_same_compatibility_complex():
    """Same complex {∅,{D1},{D2}} (CLAIM-347, CLAIM-583): each demand met
    singly, never jointly."""
    a, b = P.seed_pair()
    assert a.compatibility_complex() == b.compatibility_complex()
    names = {frozenset(), frozenset({"D1"}), frozenset({"D2"})}
    assert a.compatibility_complex() == names


def test_seed_distinguishing_budget_is_one():
    """CLAIM-583's core: a probe allowed one admissible move tells the pair
    apart; the verdict stabilizes at budget 1 and they diverge."""
    a, b = P.seed_pair()
    res = P.probe_pair(a, b, 4)
    assert res["same_complex"] is True
    assert res["distinguishing_budget"] == 1
    assert res["stabilizes_at"] == 1
    assert res["final_verdict"] == "distinguishable"
    assert res["ever_diverge"] is True


def test_seed_B_reaches_A_does_not_at_budget_one():
    """The mechanism of the difference: in B the D1-config reaches a D2-config
    in one move; in A it does not."""
    a, b = P.seed_pair()
    assert b.demands["D2"] in b.reachable_within(b.demands["D1"], 1)
    assert a.demands["D2"] not in a.reachable_within(a.demands["D1"], 3)


def test_reachable_within_is_monotone():
    """Reachable sets only grow with budget (needed for CLAIM-574)."""
    _, b = P.seed_pair()
    s = b.demands["D1"]
    prev = set()
    for budget in range(0, 5):
        cur = b.reachable_within(s, budget)
        assert prev <= cur
        prev = cur


@pytest.mark.parametrize("L", [2, 3, 4, 5, 6])
def test_path_family_threshold_equals_L(L):
    """A constructed family where the stabilization budget is exactly the path
    length L: the budget at which the pair parts is a measured quantity, not
    fixed at 1 (CASE-202: 'a measurement and not a design choice')."""
    a, b = P.path_pair(L)
    res = P.probe_pair(a, b, L + 2)
    assert res["same_complex"] is True
    assert res["distinguishing_budget"] == L
    assert res["stabilizes_at"] == L
    assert res["distinction_monotone_in_budget"] is True
    # below threshold: indistinguishable; at and above: distinguishable
    below = [v["distinguishable"] for v in res["verdicts"] if v["budget"] < L]
    atabove = [v["distinguishable"] for v in res["verdicts"] if v["budget"] >= L]
    assert not any(below)
    assert all(atabove)


def test_path_family_rejects_degenerate_L1():
    with pytest.raises(ValueError):
        P.path_pair(1)


def test_control_reset_equals_acted():
    """The non-destructive probe gives the same readout on a reset copy and on
    an acted-on copy: the difference is discovered, not created (CASE-202)."""
    a, b = P.seed_pair()
    res = P.probe_pair(a, b, 4)
    assert res["control_reset_equals_acted"] is True


def test_identical_pair_never_distinguished():
    """A pair of identical mechanisms is indistinguishable at every budget: a
    difference the prober reports is never an artefact of probing."""
    _, b = P.seed_pair()
    res = P.probe_pair(b, b, 4)
    assert res["final_verdict"] == "indistinguishable"
    assert res["distinguishing_budget"] is None
    assert res["ever_diverge"] is False


def test_distinction_monotone_on_seed():
    a, b = P.seed_pair()
    res = P.probe_pair(a, b, 4)
    assert res["distinction_monotone_in_budget"] is True
