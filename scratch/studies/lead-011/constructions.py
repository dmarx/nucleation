"""LEAD-011: when does an optimal learning policy exist as a scalar optimum?

Three small constructions, each a check of one step of the argument filed
with the lead's run. Nothing here is evidence beyond the arithmetic: the
claims are demonstrated by the argument in their bodies, and these checks
guard the numbers.

1. Endogenous tasks (positive case). The learner's acquisitions change the
   distribution of tasks it later faces. With that dependence declared as a
   kernel, the learner's organization is part of the state, backward
   induction gives a value, and enumerating every Markov policy confirms
   that some policy attains it.

2. Valuation that moves with learning (negative case). Each policy produces
   a learner whose valuation differs. Evaluated by the self each policy
   produces, the ranking of policies is not invariant under the rescalings
   each valuation admits, and the set of self-ratifying policies can be
   empty (a cycle) or hold two policies.

3. Learnability that grows faster than discounting (negative case). Each
   period of investment multiplies the later payoff rate by g. With
   discount gamma and gamma * g > 1, "invest n periods, then exploit"
   is beaten by n + 1 for every n, and never exploiting is worth 0, so no
   policy is optimal; a bounded version shows the supremum need not be
   attained even when the value is finite.

Run: python3 -I -m pytest -q scratch/studies/lead-011 (from the repo root),
or python3 -I scratch/studies/lead-011/constructions.py for a printout.
"""

from __future__ import annotations

import itertools
from fractions import Fraction

import numpy as np

# ---------------------------------------------------------------------------
# 1. Endogenous tasks: a declared kernel restores the optimum.
# ---------------------------------------------------------------------------

# Learner organizations: 0 novice, 1 holds a procedure P, 2 holds P and Q.
N_STATES = 3
# Probability that the period's task is hard, by organization: learning
# changes which tasks the learner meets (more ambitious work comes to it).
P_HARD = np.array([0.1, 0.5, 0.8])
# Reward for working on an easy or hard task, by organization.
R_EASY = np.array([1.0, 1.0, 1.0])
R_HARD = np.array([-1.0, 2.0, 5.0])
# Cost of the next acquisition, by organization (none from state 2).
LEARN_COST = np.array([1.5, 3.0, np.inf])

WORK, LEARN = 0, 1


def expected_work_reward(s: int) -> float:
    """Expected one-period reward of working in organization s."""
    return float((1 - P_HARD[s]) * R_EASY[s] + P_HARD[s] * R_HARD[s])


def backward_induction(T: int, gamma: float = 1.0):
    """Optimal value and a Markov policy for horizon T.

    The task is drawn after the action is chosen, so the decision depends on
    (t, s) only. Returns (V, policy) with V[t, s] the optimal value from
    period t in organization s and policy[t, s] in {WORK, LEARN}.
    """
    V = np.zeros((T + 1, N_STATES))
    policy = np.zeros((T, N_STATES), dtype=int)
    for t in range(T - 1, -1, -1):
        for s in range(N_STATES):
            work = expected_work_reward(s) + gamma * V[t + 1, s]
            if s + 1 < N_STATES:
                learn = -LEARN_COST[s] + gamma * V[t + 1, s + 1]
            else:
                learn = -np.inf
            policy[t, s] = LEARN if learn > work else WORK
            V[t, s] = max(work, learn)
    return V, policy


def evaluate_markov_policy(policy: np.ndarray, T: int, gamma: float = 1.0,
                           s0: int = 0) -> float:
    """Exact expected discounted return of a Markov policy from s0."""
    total = 0.0
    s = s0  # the organization path is deterministic given the policy
    for t in range(T):
        a = policy[t, s]
        if a == LEARN and s + 1 < N_STATES:
            total += gamma ** t * (-LEARN_COST[s])
            s += 1
        else:
            total += gamma ** t * expected_work_reward(s)
    return total


def brute_force_optimum(T: int, gamma: float = 1.0, s0: int = 0):
    """Best value over every deterministic Markov policy, by enumeration."""
    best, best_policy = -np.inf, None
    free = [(t, s) for t in range(T) for s in range(N_STATES - 1)]
    for choice in itertools.product((WORK, LEARN), repeat=len(free)):
        policy = np.zeros((T, N_STATES), dtype=int)
        for (t, s), a in zip(free, choice):
            policy[t, s] = a
        v = evaluate_markov_policy(policy, T, gamma, s0)
        if v > best + 1e-12:
            best, best_policy = v, policy
    return best, best_policy


# ---------------------------------------------------------------------------
# 2. Valuation that moves with learning.
# ---------------------------------------------------------------------------

def ex_post_values(utilities: dict, produces: dict, transforms: dict | None = None):
    """Value of each policy by the valuation of the self it produces.

    utilities[self][policy] is that self's utility for a policy's outcome;
    produces[policy] is the self the policy produces; transforms[self] is a
    positive affine map (a, b) applied to that self's utility, which leaves
    the self's own preferences unchanged.
    """
    transforms = transforms or {}
    out = {}
    for pi, self_ in produces.items():
        a, b = transforms.get(self_, (1, 0))
        assert a > 0
        out[pi] = a * utilities[self_][pi] + b
    return out


def ranking(values: dict) -> list:
    """Policies from best to worst (ties broken by name)."""
    return sorted(values, key=lambda k: (-values[k], k))


def self_ratifying(utilities: dict, produces: dict) -> set:
    """Policies the self they produce would choose again over every other."""
    out = set()
    for pi, self_ in produces.items():
        u = utilities[self_]
        if all(u[pi] >= u[other] for other in produces):
            out.add(pi)
    return out


def ex_ante_optimum(utilities: dict, initial_self: str, policies) -> set:
    """Policies best by the initial self's valuation."""
    u = utilities[initial_self]
    best = max(u[p] for p in policies)
    return {p for p in policies if u[p] == best}


# Two policies, each endorsed by the self it produces.
TWO_SELVES_U = {
    "s0": {"A": 0, "B": 1},  # the learner as it is: prefers not to learn L
    "sL": {"A": 1, "B": 0},  # the learner that learned L: prefers having learned it
}
TWO_SELVES_PRODUCES = {"A": "sL", "B": "s0"}

# Three policies, each regretted by the self it produces (a cycle).
CYCLE_U = {
    "a": {"A": 0, "B": 1, "C": 0},
    "b": {"A": 0, "B": 0, "C": 1},
    "c": {"A": 1, "B": 0, "C": 0},
}
CYCLE_PRODUCES = {"A": "a", "B": "b", "C": "c"}


# ---------------------------------------------------------------------------
# 3. Learnability growing faster than discounting.
# ---------------------------------------------------------------------------

def invest_then_exploit_value(n: int, g, gamma, r=1, horizon=None):
    """Value of investing n periods (payoff 0) and then exploiting.

    Each investment multiplies the per-period payoff rate by g. With no
    horizon the value is (gamma * g)^n * r / (1 - gamma). Exact arithmetic
    when the arguments are Fractions.
    """
    if horizon is None:
        return (gamma * g) ** n * r / (1 - gamma)
    return sum(gamma ** t * g ** n * r for t in range(n, horizon))


def bounded_invest_value(n: int):
    """A bounded version: investing n periods then exploiting is worth
    1 - 2**-n; never exploiting is worth 0. The supremum, 1, is never
    attained."""
    return 1 - Fraction(1, 2 ** n)


def best_n(g, gamma, horizon, r=1):
    """Optimal number of investment periods for a finite horizon."""
    values = [invest_then_exploit_value(n, g, gamma, r, horizon)
              for n in range(horizon + 1)]
    m = max(values)
    return values.index(m), m


if __name__ == "__main__":
    T = 6
    V, pol = backward_induction(T)
    bf, _ = brute_force_optimum(T)
    print("1. endogenous tasks, T=6: backward induction", V[0, 0],
          "enumeration over", 2 ** (T * 2), "Markov policies", bf)
    print("   optimal policy (rows t, cols s; 1 = learn):\n", pol)
    print("2. two selves, ex post:", ex_post_values(TWO_SELVES_U, TWO_SELVES_PRODUCES))
    for tr in ({"sL": (2, 0)}, {"sL": (Fraction(1, 2), 0)}):
        v = ex_post_values(TWO_SELVES_U, TWO_SELVES_PRODUCES, tr)
        print("   rescaled", tr, "->", ranking(v))
    print("   self-ratifying:", self_ratifying(TWO_SELVES_U, TWO_SELVES_PRODUCES))
    print("   cycle self-ratifying:", self_ratifying(CYCLE_U, CYCLE_PRODUCES))
    g, gamma = Fraction(3, 2), Fraction(9, 10)
    print("3. gamma*g =", gamma * g, "values n=0..5:",
          [float(invest_then_exploit_value(n, g, gamma)) for n in range(6)])
    print("   finite horizon 20: best n, value", best_n(g, gamma, 20))
