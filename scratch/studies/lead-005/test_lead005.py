"""Tests for the LEAD-005 study.  Run:  python3 -I -m pytest -q  (from this directory)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from feedback_toy import (decode, describe, env_T, evaluate,  # noqa: E402
                          interventional_partition, predictive_partition)
from still2012 import (Model, entropy, equilibrate_kernel,  # noqa: E402
                       metropolis_kernel, mutual_info, random_model, run_exact,
                       run_paths, sample)

LN2 = np.log(2)


def h(p):
    return entropy([p, 1 - p])


# ------------------------------------------------------------ basics
def test_entropy_and_mi():
    assert entropy([0.5, 0.5]) == pytest.approx(LN2)
    assert mutual_info(np.array([[0.5, 0], [0, 0.5]])) == pytest.approx(LN2)
    assert mutual_info(np.full((2, 2), 0.25)) == pytest.approx(0, abs=1e-15)


@pytest.mark.parametrize("sweeps", [1, 3])
def test_metropolis_keeps_equilibrium(sweeps):
    E = np.array([0.0, 1.3, 2.1, 0.4])
    K = metropolis_kernel(E, sweeps)
    p = np.exp(-E) / np.exp(-E).sum()
    assert np.allclose(K.sum(1), 1)
    assert np.allclose(p @ K, p)


# ------------------------------------------------------------ identities
@pytest.mark.parametrize("feedback", [False, True])
def test_identities_hold_with_and_without_feedback(feedback):
    rng = np.random.default_rng(7)
    for _ in range(20):
        r = run_exact(random_model(rng, feedback=feedback), 6)
        T = r.totals
        for s in r.steps:                                      # Eq. 14
            assert s["Wdiss_switch"] == pytest.approx(s["nostalgia"], abs=1e-12)
        assert T["Wdiss"] == pytest.approx(T["nostalgia"] - T["dF_relax"], abs=1e-12)  # Eq. 17
        assert -T["Q"] == pytest.approx(T["Ie"] + T["Wdiss"], abs=1e-12)               # Eq. 19
        assert T["dE"] == pytest.approx(T["W"] + T["Q"], abs=1e-12)                    # first law
        assert T["dF_relax"] <= 1e-12                                                   # Eq. 16
        assert T["nostalgia"] <= T["Wdiss"] + 1e-12 <= T["Wex"] + 2e-12                 # Eq. 18
        assert -T["Q"] >= T["Ie"] + T["nostalgia"] - 1e-12                              # Eq. 21


def test_no_feedback_nostalgia_nonnegative_each_step():
    rng = np.random.default_rng(11)
    for _ in range(30):
        r = run_exact(random_model(rng), 6)
        assert min(s["nostalgia"] for s in r.steps) >= -1e-12


def test_path_reading_excess_work_matches_and_bound_holds():
    rng = np.random.default_rng(3)
    for _ in range(5):
        m = random_model(rng, n_s=3)
        T = run_exact(m, 4).totals
        P = run_paths(m, 4)
        assert P["Wex"] == pytest.approx(T["Wex"], abs=1e-12)   # reading-independent
        assert P["Wdiss"] <= T["Wdiss"] + 1e-12                  # convexity of KL
        assert P["Wdiss"] >= T["nostalgia"] - 1e-12


def test_monte_carlo_agrees_with_exact():
    for fb in (False, True):
        m = random_model(np.random.default_rng(5), feedback=fb)
        T = run_exact(m, 6).totals
        mc = sample(m, 6, 100_000, np.random.default_rng(6))
        assert abs(mc["W"] - T["W"]) < 4 * mc["W_se"]
        assert abs(mc["Q"] - T["Q"]) < 4 * mc["Q_se"]


def test_feedback_breaks_the_sign_not_the_bound():
    rng = np.random.default_rng(2)
    neg_sum = neg_wex = 0
    for _ in range(200):
        T = run_exact(random_model(rng, feedback=True, concentration=0.3), 6).totals
        assert T["nostalgia"] <= T["Wdiss"] + 1e-12
        neg_sum += T["nostalgia"] < 0
        neg_wex += T["Wex"] < 0
    assert neg_sum > 0 and neg_wex > 0


# ------------------------------------------------------------ the record's example
def test_two_state_markov_copy_memory_nostalgia():
    """A memory that copies a two-state Markov drive with rows (0.9, 0.1),
    (0.2, 0.8) keeps H(X_t|X_{t+1}) ~ 0.38 nats it does not carry over."""
    P = np.array([[0.9, 0.1], [0.2, 0.8]])
    pi = np.array([2 / 3, 1 / 3])
    gap = 40.0
    E = np.array([[0.0, gap], [gap, 0.0]])
    m = Model(E=E, p0x=pi, D=np.repeat(P[:, None, :], 2, axis=1),
              K=np.stack([equilibrate_kernel(E[:, x]) for x in range(2)]))
    r = run_exact(m, 5)
    joint = pi[:, None] * P
    H_cond = entropy(joint) - entropy(joint.sum(0))
    assert H_cond == pytest.approx(0.3835, abs=1e-4)
    for s in r.steps:
        assert s["nostalgia"] == pytest.approx(H_cond, abs=1e-9)
    assert r.totals["nostalgia"] <= r.totals["Wdiss"] + 1e-12


# ------------------------------------------------------------ feedback toy
def test_toy_partitions():
    T = env_T(0.1, 0.05)
    rand = np.full((8, 2), 0.5)
    a0 = np.zeros((8, 2)); a0[:, 0] = 1
    au = np.zeros((8, 2))
    for x in range(8):
        au[x, decode(x)[0]] = 1
    assert describe(predictive_partition(T, rand)) == "{v}"
    assert describe(predictive_partition(T, au)) == "{v}"
    assert describe(predictive_partition(T, a0)) == "{u,v}"
    assert describe(interventional_partition(T, "y")) == "{u}"
    assert describe(interventional_partition(T, "x")) == "{u,v}"


def test_toy_policy_moves_nostalgia_not_heat():
    best = evaluate("interventional {u}", None, eps=0.02, delta=0.0, gap=30.0)
    const = evaluate("interventional {u}", lambda s: 0, eps=0.02, delta=0.0, gap=30.0)
    assert best["success"] == pytest.approx(1.0, abs=1e-9)
    assert const["success"] == pytest.approx(0.5, abs=1e-9)
    assert best["nostalgia"] == pytest.approx(LN2, abs=1e-9)
    assert const["nostalgia"] == pytest.approx(0.0, abs=1e-9)
    assert best["heat_step"] == pytest.approx(const["heat_step"], abs=1e-9)


@pytest.mark.parametrize("eps,delta,gap", [(0.1, 0.05, 6.0), (0.3, 0.1, 4.0), (0.02, 0.0, 10.0)])
def test_toy_interventional_memory_is_cheapest_that_does_the_task(eps, delta, gap):
    rows = {n: evaluate(n, None, eps, delta, gap)
            for n in ("none", "predictive {v}", "interventional {u}", "u and v", "full {u,v,y}")}
    assert rows["predictive {v}"]["success"] == pytest.approx(0.5, abs=1e-9)
    assert rows["none"]["success"] == pytest.approx(0.5, abs=1e-9)
    doers = [n for n, r in rows.items() if r["success"] > 0.8]
    assert set(doers) == {"interventional {u}", "u and v", "full {u,v,y}"}
    for key in ("nostalgia", "heat_step", "H_overwrite"):
        assert min(doers, key=lambda n: rows[n][key]) == "interventional {u}"
