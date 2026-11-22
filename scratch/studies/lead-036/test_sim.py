import json
import os
import sys
from dataclasses import replace

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
import sim  # noqa: E402
from sim import Params  # noqa: E402


def test_commit_prob_ramp():
    q = sim.commit_prob([0.0, 0.4, 0.6, 0.8, 1.0], 0.4, 0.8)
    assert np.allclose(q, [0, 0, 0.5, 1, 1])


def test_k_base_and_k_star():
    p = Params()
    assert p.k_base == pytest.approx(0.25)
    assert sim.k_star(p.Bbar + p.eta_lam, p) == pytest.approx(min(1, 0.1 * 0.72 / 0.08))
    assert sim.k_star(0.5, p) == 0.0


def test_decoupled_converges_to_k_star():
    p = replace(Params(), runs=50, T=200, k0=0.1)
    res = sim.simulate(p, "decoupled_full", seed=1)
    target = float(sim.k_star(p.Bbar + p.eta_lam, p))
    assert np.allclose(res["k_path"][-1], target, atol=1e-5)
    # the budget never moves
    assert np.all(res["B_path"] == p.Bbar + p.eta_lam)


def test_decoupled_does_not_depend_on_occasions():
    p = replace(Params(), runs=20, T=60)
    a = sim.simulate(p, "decoupled_full", seed=1)["k_path"]
    b = sim.simulate(replace(p, lam=4.0), "decoupled_full", seed=7)["k_path"]
    assert np.allclose(a, b)


def test_coupled_budget_rule_W1():
    """B_{t+1} = Bbar + eta * M_t: every budget after the first is Bbar plus
    eta times a whole number of commitments, and those numbers add up to all
    commitments but the last period's."""
    p = replace(Params(), runs=1, T=200, lam=1.0)
    res = sim.simulate(p, "coupled", seed=3)
    M = (res["B_path"][1:, 0] - p.Bbar) / p.eta
    assert np.allclose(M, np.round(M))
    assert M.sum() <= res["committed"][0] + 1e-9
    assert res["committed"][0] - M.sum() <= 12


def test_coupled_budget_rule_window():
    p = replace(Params(), runs=1, T=100, lam=1.0, W=4)
    res = sim.simulate(p, "coupled", seed=5)
    B = res["B_path"][:, 0]
    # every budget is Bbar + eta * (integer sum over 4 quarters) / 4
    s = (B - p.Bbar) / p.eta * 4
    assert np.allclose(s, np.round(s))


def test_absorbing_below_k_lo_when_k_base_below():
    """Once k < k_lo and k_base < k_lo, nothing is committed, B = Bbar, k -> k_base."""
    p = replace(Params(), runs=200, T=80, k0=0.39, lam=4.0, B0=1.2)
    res = sim.simulate(p, "coupled", seed=2)
    assert res["committed"].sum() == 0
    assert np.all(res["B_path"][1:] == p.Bbar)
    assert np.all(res["k_path"] < p.k_lo)
    assert np.allclose(res["k_path"][-1], p.k_base, atol=1e-3)


def test_not_absorbing_when_k_base_above_k_lo():
    p = replace(Params(), Bbar=1.35, runs=200, T=80, k0=0.1, lam=1.0)
    res = sim.simulate(p, "coupled", seed=2)
    assert res["k_path"][-1].min() > p.k_lo


def test_fixed_points_three_and_one():
    fp = sim.fixed_points(Params())
    kinds = [s for _, s in fp]
    assert kinds == ["stable", "unstable", "stable"]
    assert fp[0][0] == pytest.approx(0.25, abs=1e-4)
    assert fp[2][0] == pytest.approx(0.9, abs=1e-4)
    fp2 = sim.fixed_points(replace(Params(), Bbar=1.35))
    assert [s for _, s in fp2] == ["stable"]
    # without coverage feedback the coupled mean field has one fixed point
    fp3 = sim.fixed_points(Params(), coverage=False)
    assert [s for _, s in fp3] == ["stable"]


def test_nocov_mean_budget():
    """With p = 1, E[B] = Bbar + eta * lam = Bbar + eta_lam."""
    p = replace(Params(), runs=4000, T=40, lam=0.25)
    res = sim.simulate(p, "coupled_nocov", seed=4)
    assert res["B_path"][1:].mean() == pytest.approx(p.Bbar + p.eta_lam, rel=0.02)


def test_same_occasions_across_rules():
    p = replace(Params(), runs=300, T=40)
    a = sim.simulate(p, "coupled_nocov", seed=9)
    b = sim.simulate(p, "decoupled_full", seed=9)
    assert np.array_equal(a["occ"], b["occ"])


def test_grid_resumes(tmp_path, monkeypatch):
    monkeypatch.setattr(sim, "LAMS", [1.0])
    monkeypatch.setattr(sim, "WS", [1])
    monkeypatch.setattr(sim, "BBARS", [1.2])
    path = tmp_path / "r.jsonl"
    base = replace(Params(), runs=50, T=20)
    sim.run_grid(str(path), base)
    n1 = len(path.read_text().splitlines())
    sim.run_grid(str(path), base)
    n2 = len(path.read_text().splitlines())
    assert n1 == n2 == 4
    d = [json.loads(x) for x in path.read_text().splitlines()]
    eq = [x for x in d if x["rule"] == "decoupled_equal"][0]
    co = [x for x in d if x["rule"] == "coupled"][0]
    assert eq["B_fixed"] == pytest.approx(co["B_mean"])


def test_n_star():
    p = Params()
    n = sim.n_star(p)
    k = 1.0
    for _ in range(n):
        k = 0.92 * k + 0.1 * 0.2
    assert k < p.k_lo
    k = 1.0
    for _ in range(n - 1):
        k = 0.92 * k + 0.1 * 0.2
    assert k >= p.k_lo


@pytest.mark.parametrize("lam,W", [(0.05, 1), (0.1, 1), (0.1, 4), (0.25, 4)])
def test_loss_bound_holds(lam, W):
    p = replace(Params(), lam=lam, W=W, runs=2000)
    res = sim.simulate(p, "coupled", seed=11)
    lost = sim.summarize(p, res, "coupled")["lost"]
    assert lost >= sim.loss_lower_bound(p) - 3 * np.sqrt(0.25 / p.runs)
