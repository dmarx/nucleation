"""Tests for LEAD-011's constructions."""

import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import constructions as c  # noqa: E402


# 1. Endogenous tasks --------------------------------------------------------

@pytest.mark.parametrize("T", [1, 3, 5, 6])
@pytest.mark.parametrize("gamma", [1.0, 0.9])
def test_backward_induction_value_is_attained_by_some_markov_policy(T, gamma):
    V, policy = c.backward_induction(T, gamma)
    attained = c.evaluate_markov_policy(policy, T, gamma)
    best, _ = c.brute_force_optimum(T, gamma)
    assert attained == pytest.approx(V[0, 0])
    assert best == pytest.approx(V[0, 0])


def test_the_task_distribution_does_depend_on_what_was_learned():
    # The construction is a genuine case of endogenous tasks.
    assert len(set(c.P_HARD.tolist())) == c.N_STATES


def test_optimal_policy_learns_when_horizon_allows():
    # Long enough horizon: the optimum invests in both acquisitions first,
    # though each acquisition period is a loss on its own.
    V, policy = c.backward_induction(6)
    assert policy[0, 0] == c.LEARN and policy[1, 1] == c.LEARN
    assert c.expected_work_reward(0) > -c.LEARN_COST[0]
    # Short horizon: it does not.
    V1, policy1 = c.backward_induction(1)
    assert policy1[0, 0] == c.WORK


# 2. Valuation that moves with learning --------------------------------------

def test_ex_post_ranking_is_not_invariant_to_admissible_rescaling():
    up = c.ex_post_values(c.TWO_SELVES_U, c.TWO_SELVES_PRODUCES, {"sL": (2, 0)})
    down = c.ex_post_values(c.TWO_SELVES_U, c.TWO_SELVES_PRODUCES,
                            {"sL": (Fraction(1, 2), 0)})
    assert c.ranking(up)[0] == "A"
    assert c.ranking(down)[0] == "B"


def test_rescaling_leaves_each_selfs_own_preferences_unchanged():
    for self_, u in c.TWO_SELVES_U.items():
        for a, b in [(2, 0), (Fraction(1, 2), 3)]:
            v = {p: a * x + b for p, x in u.items()}
            assert c.ranking(v) == c.ranking(u)


def test_two_policies_both_self_ratifying():
    assert c.self_ratifying(c.TWO_SELVES_U, c.TWO_SELVES_PRODUCES) == {"A", "B"}


def test_cycle_has_no_self_ratifying_policy():
    assert c.self_ratifying(c.CYCLE_U, c.CYCLE_PRODUCES) == set()


def test_ex_ante_valuation_gives_an_optimum_that_ignores_the_later_valuation():
    best = c.ex_ante_optimum(c.TWO_SELVES_U, "s0", ["A", "B"])
    assert best == {"B"}
    # Whatever the learned self values, the ex ante optimum is unchanged.
    for uA in range(-5, 6):
        u = {"s0": c.TWO_SELVES_U["s0"], "sL": {"A": uA, "B": 0}}
        assert c.ex_ante_optimum(u, "s0", ["A", "B"]) == {"B"}


# 3. Learnability growing faster than discounting -----------------------------

def test_each_investment_policy_is_beaten_by_investing_once_more():
    g, gamma = Fraction(3, 2), Fraction(9, 10)
    assert gamma * g > 1
    vals = [c.invest_then_exploit_value(n, g, gamma) for n in range(50)]
    assert all(b > a for a, b in zip(vals, vals[1:]))
    # Never exploiting is worth 0, below every finite n.
    assert min(vals) > 0


def test_discount_dominating_growth_restores_an_optimum_at_zero():
    g, gamma = Fraction(11, 10), Fraction(8, 10)
    assert gamma * g < 1
    vals = [c.invest_then_exploit_value(n, g, gamma) for n in range(50)]
    assert vals.index(max(vals)) == 0


def test_bounded_values_supremum_not_attained():
    vals = [c.bounded_invest_value(n) for n in range(60)]
    assert all(v < 1 for v in vals)
    assert all(b > a for a, b in zip(vals, vals[1:]))
    assert 1 - vals[-1] < Fraction(1, 10 ** 17)


@pytest.mark.parametrize("horizon", [5, 20, 60])
def test_finite_horizon_attains_an_optimum_even_with_fast_growth(horizon):
    g, gamma = Fraction(3, 2), Fraction(9, 10)
    n, v = c.best_n(g, gamma, horizon)
    assert 0 <= n < horizon
    assert v == max(c.invest_then_exploit_value(k, g, gamma, 1, horizon)
                    for k in range(horizon + 1))
