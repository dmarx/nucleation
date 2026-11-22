"""Tests for LEAD-095's committor model.  Run: python3 -I -m pytest -q scratch/studies/lead-095"""
import os
import sys
from dataclasses import replace

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from committor_model import (Model, Params, committor, simulate_success,  # noqa: E402
                             time_withdrawal, withdrawal_decomposition)


def birth_death(M, up, down):
    Q = np.zeros((M + 1, M + 1))
    for i in range(1, M):
        Q[i, i + 1], Q[i, i - 1] = up, down
    np.fill_diagonal(Q, -Q.sum(1))
    return Q


@pytest.mark.parametrize("up,down", [(1.0, 2.0), (2.0, 1.0), (0.3, 0.7)])
def test_gamblers_ruin(up, down):
    """Known answer: q(i) = (1 - r^i) / (1 - r^M), r = down/up, hitting M before 0."""
    M = 10
    q = committor(birth_death(M, up, down), [M], [0])
    r = down / up
    exact = (1 - r ** np.arange(M + 1)) / (1 - r ** M)
    assert np.allclose(q, exact, atol=1e-12)


def test_gamblers_ruin_symmetric():
    M = 7
    q = committor(birth_death(M, 1.0, 1.0), [M], [0])
    assert np.allclose(q, np.arange(M + 1) / M, atol=1e-12)


def test_claim596_construction():
    """CLAIM-596's two-part model: q(N established) = 0.8, q(neither) = 17/30."""
    a, b0, b1, k = 1.0, 0.5, 2.0, 0.5
    # states: 0 neither, 1 N only, 2 B only, 3 F, 4 K
    Q = np.zeros((5, 5))
    Q[0, 1], Q[0, 2], Q[0, 4] = a, b0, k
    Q[1, 3], Q[1, 4] = b1, k
    Q[2, 3], Q[2, 4] = a, k
    np.fill_diagonal(Q, -Q.sum(1))
    q = committor(Q, [3], [4])
    assert q[1] == pytest.approx(0.8, abs=1e-12)
    assert q[0] == pytest.approx(17 / 30, abs=1e-12)


def test_generator_rows_and_range():
    for sup in (True, False):
        m = Model(Params())
        Q = m.generator(sup)
        assert np.allclose(Q.sum(1), 0)
        assert (Q - np.diag(np.diag(Q)) >= 0).all()
        q = m.q(sup)
        assert (q >= -1e-12).all() and (q <= 1 + 1e-12).all()


@pytest.mark.parametrize("theta,rate,state", [(0.5, True, True), (1.0, False, True), (1.0, True, False)])
def test_decomposition_identity(theta, rate, state):
    p = replace(Params(), theta=theta, rate_effect=rate, state_effect=state)
    m = Model(p)
    D = m.q(True) - m.q(False)
    assert np.allclose(withdrawal_decomposition(p), D, atol=1e-12)


def test_monte_carlo_agrees():
    p = replace(Params(), M=4)
    m = Model(p)
    rng = np.random.default_rng(7)
    for sup in (True, False):
        Q = m.generator(sup)
        q = m.q(sup)
        s = m.idx(1, 1)
        est = simulate_success(Q, s, m.F, m.K, 4000, rng)
        assert abs(est - q[s]) < 4 * np.sqrt(q[s] * (1 - q[s]) / 4000) + 1e-3


def test_time_withdrawal_limits():
    p = Params()
    m = Model(p)
    rows = time_withdrawal(p, [0.0, 2000.0])
    assert rows[0]["Y"] == pytest.approx(m.q(False)[m.idx(0, 0)], abs=1e-10)
    assert rows[1]["Y"] == pytest.approx(m.q(True)[m.idx(0, 0)], abs=1e-6)


def test_switches_off_make_nucleus_inert():
    """With neither effect, the nucleus changes nothing: Delta_N = 0 and D = 0."""
    p = replace(Params(), state_effect=False, rate_effect=False)
    t0, tS = Model(p).table(False), Model(p).table(True)
    assert np.allclose(t0[1], t0[0], atol=1e-12)
    assert np.allclose(tS, t0, atol=1e-12)
