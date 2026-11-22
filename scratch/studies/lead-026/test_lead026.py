"""Tests for LEAD-026's model and measures. Run:
    python3 -m pytest -q -p no:cacheprovider test_lead026.py
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import measures as M  # noqa: E402
from model import N, Sim  # noqa: E402


def var_sim(Bs, T=60000, seed=0, noise=1.0):
    """Simulate x_{t+1} = sum_l B_l x_{t+1-l} + noise; one replica."""
    rng = np.random.default_rng(seed)
    p, d = len(Bs), Bs[0].shape[0]
    x = np.zeros((T + p, d))
    for t in range(p, T + p - 1):
        x[t + 1] = sum(Bs[l] @ x[t - l] for l in range(p)) + noise * rng.standard_normal(d)
    return x[p:, None, :]


def test_cmi_known_gaussian():
    s2 = 0.5
    C = np.array([[1.0, 1.0], [1.0, 1.0 + s2]])
    assert M.cmi_cov(C, [0], [1]) == pytest.approx(0.5 * np.log(1 + 1 / s2))


def test_ar1_astar():
    rho = 0.8
    traj = var_sim([np.array([[rho]])], T=200000)
    C = M.lag_pair_cov(traj, 1)
    k = M.krakauer(C, [0], [])
    assert k["Astar"] == pytest.approx(-0.5 * np.log(1 - rho ** 2), rel=0.03)


def test_bipartitions_count():
    for k in range(2, 7):
        assert len(list(M.bipartitions(list(range(k))))) == 2 ** (k - 1) - 1


def test_block_finds_coupled_pair_and_isolate():
    B = np.array([[0.5, 0.3, 0.0], [0.3, 0.5, 0.0], [0.0, 0.0, 0.7]])
    traj = var_sim([B])
    C, n = M.embed_cov(traj, 2)
    V = [0, 1, 2]
    assert M.block_scores(C, n, 3, 1, [0, 1], V)["passes"]
    assert M.block_scores(C, n, 3, 1, [2], V)["passes"]
    assert not M.block_scores(C, n, 3, 1, [0], V)["passes"]
    assert not M.block_scores(C, n, 3, 1, [0, 1, 2], V)["passes"]


def test_lagged_coupling_and_the_window():
    """Coupling only at lag 3. With memoryless units a one-step VAR does
    not see it and a three-step window does. With persistent units the
    one-step VAR sees it anyway, through the source's own persistence,
    though less strongly than the three-step window."""
    d = 2
    B3 = np.array([[0.0, 0.3], [0.3, 0.0]])
    Z = np.zeros((d, d))
    traj = var_sim([Z, Z, B3])
    C, n = M.embed_cov(traj, 4)
    s1 = M.block_scores(C, n, d, 1, [0, 1], [0, 1])
    s3 = M.block_scores(C, n, d, 3, [0, 1], [0, 1])
    assert s1["internal"] < 0 < s3["internal"]
    traj = var_sim([np.diag([0.5, 0.5]), Z, B3])
    C, n = M.embed_cov(traj, 4)
    s1 = M.block_scores(C, n, d, 1, [0, 1], [0, 1])
    s3 = M.block_scores(C, n, d, 3, [0, 1], [0, 1])
    assert 0 < s1["internal"] < s3["internal"]


def test_common_input_observed_and_hidden():
    """Two units driven by u, no coupling between them. With u observed the
    pair fails and the pair plus u passes; with u hidden the pair passes."""
    B = np.array([[0.5, 0.0, 0.4], [0.0, 0.5, 0.4], [0.0, 0.0, 0.95]])
    traj = var_sim([B])
    C, n = M.embed_cov(traj, 3)
    V = [0, 1, 2]
    assert not M.block_scores(C, n, 3, 1, [0, 1], V)["passes"]
    assert M.block_scores(C, n, 3, 1, [0, 1, 2], V)["passes"]
    Ch, nh = M.embed_cov(traj[:, :, :2], 3)
    assert M.block_scores(Ch, nh, 2, 3, [0, 1], [0, 1])["passes"]


def test_turnover_rate_is_shared():
    par = dict(a=0.5, gain=0.3, s=0.6)
    for arm in ("A", "B", "C", "C0"):
        sim = Sim(arm, par, 2000, np.random.default_rng(1))
        rates = []
        for _ in range(50):
            sim.step()
            rates.append(sim.last_rep.mean())
        assert np.mean(rates) == pytest.approx(sim.p["r"], rel=0.05)


def test_arm_b_coupling_is_only_lagged():
    """Perturb member 0 at t (same random numbers): member 1's slot is
    unchanged for L - 1 steps and changes at lag L."""
    par = dict(a=0.5, gain=0.4, s=0.6)
    s1 = Sim("B", par, 500, np.random.default_rng(3))
    for _ in range(50):
        s1.step()
    import copy
    s2 = copy.deepcopy(s1)
    s2.intervene([0], s2.x[:, [0]] + 5.0)
    L = s1.p["L"]
    diffs = []
    for _ in range(L):
        s1.step()
        s2.step()
        diffs.append(np.abs(s1.x[:, 1:N] - s2.x[:, 1:N]).max())
    assert max(diffs[:L - 1]) == 0.0
    assert diffs[L - 1] > 0.0


def test_arm_a_members_do_not_affect_each_other():
    par = dict(a=0.5, gain=0.3, s=0.6)
    s1 = Sim("A", par, 300, np.random.default_rng(4))
    for _ in range(20):
        s1.step()
    import copy
    s2 = copy.deepcopy(s1)
    s2.intervene([0], s2.x[:, [0]] + 5.0)
    for _ in range(30):
        s1.step()
        s2.step()
    assert np.abs(s1.x[:, 1:] - s2.x[:, 1:]).max() == 0.0


def test_arm_c_institution_answers_members_c0_does_not():
    par = dict(a=0.5, gain=0.2, s=0.6)
    import copy
    for arm, expect in (("C", True), ("C0", False)):
        s1 = Sim(arm, par, 300, np.random.default_rng(5))
        for _ in range(20):
            s1.step()
        s2 = copy.deepcopy(s1)
        s2.intervene([0], s2.x[:, [0]] + 5.0)
        s1.step()
        s2.step()
        moved = np.abs(s1.x[:, 6] - s2.x[:, 6]).max() > 0
        assert moved == expect


def test_ahat_of_the_distractor_is_its_ar1_information():
    """z is an AR(1) with rho 0.9 that nothing touches: Ahat(1) of {z} is
    -1/2 ln(1 - rho^2), and a member's Ahat(1) in arm A is below its
    observational A*(1) (the driver's share is cut by the intervention)."""
    from run import ahat_rows
    from model import Z_IDX
    par = dict(a=0.57, gain=0.3, s=0.62)
    base = Sim("A", par, 20000, np.random.default_rng(7))
    for _ in range(200):
        base.step()
    rows = ahat_rows(base, [dict(label="z", S=[Z_IDX]), dict(label="1m", S=[0])],
                     np.random.default_rng(8), [1], 9)
    assert rows[0]["ahat"][1] == pytest.approx(-0.5 * np.log(1 - 0.81), rel=0.05)
    traj = Sim("A", par, 200, np.random.default_rng(10)).run(1000, 300)
    astar = M.krakauer(M.lag_pair_cov(traj, 1), [0], [])["Astar"]
    assert rows[1]["ahat"][1] < astar
