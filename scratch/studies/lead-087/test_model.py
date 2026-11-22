import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402


def test_nearest():
    P = np.zeros((1, M.K, M.D))
    P[0, 3] = 5.0
    assert M.nearest(P, np.full((1, M.D), 4.9))[0] == 3


def test_structure_invariant_under_rotation():
    rng = np.random.default_rng(0)
    P = rng.normal(size=(1, M.K, M.D))
    Q, _ = np.linalg.qr(rng.normal(size=(M.D, M.D)))
    assert np.allclose(M.structure(P), M.structure(P @ Q.T + 3.0))


def test_concordance_identical_members_is_one():
    rng = np.random.default_rng(1)
    P = np.repeat(rng.normal(size=(1, M.K, M.D)), M.N, 0)
    P += rng.normal(0, 1e-6, P.shape)
    assert M.concordance(P) > 0.999


def test_twin_is_deterministic():
    rng = np.random.default_rng(2)
    W = M.teacher(rng)
    P0 = rng.normal(size=(M.N, M.K, M.D))
    R = M.draws(rng)
    for arm in M.ARMS:
        a = M.run(P0, W, R, arm, 0.05)
        b = M.run(P0, W, R, arm, 0.05)
        assert np.array_equal(a["traj"], b["traj"])


def test_independent_has_no_spillover():
    rng = np.random.default_rng(3)
    W = M.teacher(rng)
    P0 = M.train(rng, W, social=False)
    R = M.draws(rng)
    S = np.arange(6)
    vec = np.ones(M.D)
    a = M.run(P0, W, R, "independent", 0.05)
    b = M.run(P0, W, R, "independent", 0.05, pert=(S, 0, vec))
    assert np.array_equal(a["traj"][:, 6:], b["traj"][:, 6:])
    assert not np.array_equal(a["traj"][-1, :6], b["traj"][-1, :6])


def test_agency_index():
    m = np.ones(M.T_TEST)
    m[M.T_FLIP:M.T_FLIP + 50] = 0
    assert abs(M.agency(m) - 1.0) < 1e-9     # perfect before and after
    m2 = np.concatenate([np.ones(M.T_FLIP), np.zeros(M.T_TEST - M.T_FLIP)])
    assert abs(M.agency(m2)) < 1e-9           # never adapts
