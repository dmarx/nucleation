import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402


def world(**kw):
    P = M.default_params(**kw)
    return P, M.make_world(P, np.random.default_rng(0))


def test_proposals_by_type():
    P, W = world(sigma_g=0.0, attack="overt", t_farm=5)
    theta = np.full(W["d"], 0.2)
    G = M.proposals(theta, 0, W, P, np.random.default_rng(1))
    ts, blk, ty = W["theta_star"], W["blk"], W["types"]
    coop = np.where(blk == 0, ts - theta, -P["beta"] * theta)
    assert np.allclose(G[ty == 0], coop)
    assert np.allclose(G[ty == 1], ts - theta)
    assert np.allclose(G[ty == 2], coop)          # farming: looks cooperative
    G2 = M.proposals(theta, 5, W, P, np.random.default_rng(1))
    adv = np.where(blk == 0, P["b_A"] * (W["theta_adv"] - theta), coop)
    assert np.allclose(G2[ty == 2], adv)


def test_attack_direction_in_block():
    P, W = world(attack="mimic")
    assert np.allclose(W["u"][W["blk"] == 0], 0)
    assert np.isclose(np.linalg.norm(W["u"]), 1)
    P, W = world(attack="overt")
    assert np.allclose(W["u"][W["blk"] == 1], 0)


def test_improvement_formula_matches_loss_difference():
    P, W = world()
    rng = np.random.default_rng(2)
    theta = rng.normal(size=W["d"])
    G = rng.normal(size=(W["N"], W["d"]))
    votes = M.evaluator_block_verdicts(theta, G, W, P, [0], oracle=True)
    for i in range(W["N"]):
        for b in (0, 1):
            m = W["blk"] == b
            L0 = np.sum((W["theta_star"] - theta)[m] ** 2)
            L1 = np.sum((W["theta_star"] - theta - P["lr"] * G[i])[m] ** 2)
            assert votes[0, i, b] == np.sign(L0 - L1)


def test_jurisdiction_and_compromise():
    P, W = world(n_Em=1)
    W["comp"][:] = False
    W["comp"][6] = True
    rng = np.random.default_rng(3)
    theta = rng.normal(size=W["d"])
    G = rng.normal(size=(W["N"], W["d"]))
    v = M.evaluator_block_verdicts(theta, G, W, P, [0, 3, 6])
    assert np.all(v[1, :, 1] == 0)                # M-only evaluator abstains on m
    assert np.all(v[0, :, 1] != 0)
    ty = W["types"]
    assert np.all(v[2][ty == 2] == 1) and np.all(v[2][ty == 1] == -1)


def test_clipped_mean():
    Gb = np.array([[1.0, 0], [0, 2.0], [30.0, 0], [5, 5]])
    ok = np.array([True, True, True, False])
    out = M.clipped_mean(Gb, ok)
    # median norm of approved rows is 2: rows clipped to norm <= 2
    assert np.allclose(out, (np.array([1, 0]) + np.array([0, 2]) + np.array([2, 0])) / 3)
    assert np.allclose(M.clipped_mean(Gb, np.zeros(4, bool)), 0)


def test_unrestricted_fixed_point_without_noise():
    P = M.default_params(sigma_g=0.0, attack="none", T=2000, tail=10)
    out = M.run("unrestricted", P, 0)
    W = M.make_world(P, np.random.default_rng(0))
    nD, nCA = P["n_D"], P["n_C"] + P["n_A"]
    frac = nD / (nD + nCA * P["beta"])
    # theta_m -> frac * theta*_m, so MC_m = 1 - (1 - frac)^2
    assert out["MC_m"] == pytest.approx(1 - (1 - frac) ** 2, abs=1e-6)
    assert out["MC_M"] == pytest.approx(1.0, abs=1e-6)


def test_oracle_learns_minority_without_noise():
    P = M.default_params(sigma_g=0.0, attack="mimic", T=600)
    out = M.run("oracle", P, 0)
    assert out["MC_m"] > 0.99 and abs(out["AS"]) < 0.01


@pytest.mark.parametrize("arch", ["unrestricted", "rel-agree", "rel-val", "role", "adaptive"])
def test_no_independent_evidence_symmetry(arch):
    """With nobody holding evidence on m, the observable updates are the same
    in the world and in its relabelling (dissenters' and mimics' targets
    swapped), so attack success in the two worlds sums to 1."""
    kw = dict(sigma_g=0.0, attack="mimic", b_A=1.0, t_farm=0, n_Em=0,
              monitor_covers_m=False, T=300)
    a = M.run(arch, M.default_params(**kw), 4)
    b = M.run(arch, M.default_params(swap_targets=True, **kw), 4)
    assert a["AS"] + b["AS"] == pytest.approx(1.0, abs=1e-9)


@pytest.mark.parametrize("arch", M.ARCHS)
def test_runs_finite(arch):
    out = M.run(arch, M.default_params(T=60, tail=10, t_farm=20, n_comp=2), 1)
    for k in ("MC_M", "MC_m", "AS", "evals_per_round"):
        assert np.isfinite(out[k])


def test_central_evaluator_compromised_admits_attack():
    hon = M.run("role", M.default_params(central=True, attack="mimic"), 0)
    com = M.run("role", M.default_params(central=True, n_comp=1, attack="mimic"), 0)
    assert com["AS"] > hon["AS"] + 0.05
    assert com["dshare"] < 0.01 < hon["dshare"]
