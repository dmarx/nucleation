"""Tests for frustration.py (LEAD-076, part 1). Run: python3 -I -m pytest -q"""
import random

import pytest

from frustration import (Org, frustrated, in_K, minimal_nonfaces, outcome, unmet_acting,
                         but_for_thwarters, thwarted, active, rule_count_max,
                         c1_frustration_quiet, c2_frustration_idle,
                         c3_minimal_conflict, c4_pair_inside_larger,
                         c5_thwarting_without_frustration, c6_sentry_static)


def test_complex_basics():
    org, _ = c1_frustration_quiet()
    assert in_K(org, [1]) and in_K(org, [2]) and frustrated(org, [1, 2])
    assert minimal_nonfaces(org) == [frozenset({1, 2})]


def test_c1_no_thwarting():
    org, rule = c1_frustration_quiet()
    r = outcome(org, rule)
    assert unmet_acting(org, r) == frozenset()
    assert thwarted(org, rule) == {}


def test_c2_idle_frustration():
    org, rule = c2_frustration_idle()
    r = outcome(org, rule)
    assert unmet_acting(org, r) == frozenset({1})
    assert but_for_thwarters(org, rule, 1, max_size=1) == []
    # deleting member 2 altogether leaves member 1 unmet
    solo = Org(R=org.R, A={1: org.A[1]}, Q={1: org.Q[1]})
    assert outcome(solo, rule) not in solo.A[1]


@pytest.mark.parametrize("n", [2, 3, 4, 6])
def test_c3_each_other_member_but_for(n):
    org, rule = c3_minimal_conflict(n)
    assert minimal_nonfaces(org) == [frozenset(range(n))]
    r = outcome(org, rule)
    ua = unmet_acting(org, r)
    assert len(ua) == 1
    (i,) = ua
    assert set(but_for_thwarters(org, rule, i)) == {frozenset({j}) for j in range(n) if j != i}


def test_c4_pairwise_attribution_fails():
    org, rule = c4_pair_inside_larger()
    assert frozenset({"i", "j"}) in minimal_nonfaces(org)
    assert but_for_thwarters(org, rule, "i", max_size=1) == []
    assert frozenset({"j", "k"}) in but_for_thwarters(org, rule, "i", max_size=3)


def test_c5_thwarting_without_frustration():
    org, rule = c5_thwarting_without_frustration()
    assert not frustrated(org, org.members)
    assert but_for_thwarters(org, rule, 1) == [frozenset({2})]
    assert thwarted(org, rule_count_max) == {}


def test_c6_sentry_static():
    org, rule = c6_sentry_static()
    assert not frustrated(org, org.members)
    assert but_for_thwarters(org, rule, "investigator") == [frozenset({"sentry"})]
    assert thwarted(org, rule_count_max) == {}


def random_org(rng, n_members, n_arr, quiet_p=0.0):
    R = tuple(range(n_arr))
    A, Q = {}, {}
    for i in range(n_members):
        A[i] = frozenset(r for r in R if rng.random() < 0.5)
        extra = frozenset(r for r in R if r not in A[i] and rng.random() < quiet_p)
        Q[i] = A[i] | extra
    return Org(R=R, A=A, Q=Q)


def test_random_countmax_unmet_acting_implies_frustrated_read_set():
    """Under the count-maximizing rule, if some member is unmet and acting at
    the outcome, the members whose demands are read there are structurally
    frustrated. Hence no thwarting where they are jointly satisfiable."""
    rng = random.Random(0)
    checked = 0
    for _ in range(4000):
        org = random_org(rng, rng.randint(2, 4), rng.randint(2, 5), quiet_p=0.4)
        try:
            r = outcome(org, rule_count_max)
        except RuntimeError:
            continue
        P = active(org, r)
        if unmet_acting(org, r):
            assert frustrated(org, P)
            checked += 1
        if in_K(org, P):
            assert thwarted(org, rule_count_max, max_size=3) == {}
    assert checked > 100


def test_random_minimal_conflicts():
    """Organizations whose whole member set is a minimal non-face and whose
    members act whenever unmet: under count-max exactly one member is unmet,
    and every other member is separately a but-for thwarter of it."""
    rng = random.Random(1)
    found = 0
    for _ in range(20000):
        n = rng.randint(2, 4)
        org = random_org(rng, n, rng.randint(2, 5))
        if minimal_nonfaces(org) != [frozenset(org.members)]:
            continue
        found += 1
        r = outcome(org, rule_count_max)
        ua = unmet_acting(org, r)
        assert len(ua) == 1
        (i,) = ua
        assert set(but_for_thwarters(org, rule_count_max, i)) == {frozenset({j}) for j in org.members if j != i}
    assert found > 200
