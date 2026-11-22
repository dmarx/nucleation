import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import (World, fit_operator, denoise, softmax_neg, run_chain,  # noqa: E402
                   Router, Governance, energy_features)
import study  # noqa: E402


def setup():
    rng = np.random.default_rng(0)
    w = World(rng, 3)
    ops = [fit_operator(w.sample(rng, k, 3000), w.m) for k in range(3)]
    return rng, w, ops


def test_own_specialist_denoises_best():
    rng, w, ops = setup()
    X = w.sample(rng, 1, 500)
    Y = X + 0.6 * rng.standard_normal(X.shape)
    errs = [np.mean((denoise(op, Y, 0.6) - X) ** 2) for op in ops]
    assert int(np.argmin(errs)) == 1
    assert errs[1] < np.mean((Y - X) ** 2) / 3


def test_energy_features_identify_type():
    rng, w, ops = setup()
    X = w.sample(rng, 2, 200)
    e = energy_features(ops, X + 0.3 * rng.standard_normal(X.shape))
    assert np.mean(np.argmax(e, 1) == 2) > 0.9


def test_softmax_neg_prefers_low_and_is_scale_free():
    g = softmax_neg(np.array([1.0, 2.0, 3.0]), 0.1)
    assert np.argmax(g) == 0 and abs(g.sum() - 1) < 1e-12
    assert np.allclose(g, softmax_neg(np.array([10.0, 20.0, 30.0]), 0.1))


def test_probe_scores_match_denoise():
    rng, w, ops = setup()
    X = w.sample(rng, 0, 5)
    sg = np.array([1.0, 0.6, 0.35, 0.2, 0.1])
    Y = X + sg[:, None] * rng.standard_normal(X.shape)
    S = study.probe_scores(ops, X, Y, sg)
    for i in range(5):
        for k in range(3):
            assert np.isclose(S[i, k], np.mean((denoise(ops[k], Y[i:i + 1], sg[i]) - X[i]) ** 2))


def test_governance_moves_grants_to_best_and_skips_unobserved():
    gov = Governance(2, 3)
    S = np.array([[0.1, 0.5, 0.5], [0.5, 0.5, 0.1]])
    for _ in range(20):
        gov.update(np.array([0, 1]), S)
    assert np.argmax(gov.g[0]) == 0 and np.argmax(gov.g[1]) == 2
    c = gov.c.copy()
    gov.update(np.array([0]), np.array([[np.nan, np.nan, 9.0]]))
    assert gov.c[0, 0] == c[0, 0] and gov.c[0, 2] > c[0, 2]


def test_router_learns_contextual_scores():
    rng = np.random.default_rng(1)
    r = Router(3, 2, forget=0.9)
    for _ in range(10):
        F = np.hstack([rng.integers(0, 2, (50, 1)), np.ones((50, 1)), np.zeros((50, 1))]).astype(float)
        S = np.stack([0.1 + 0.8 * F[:, 0], 0.9 - 0.8 * F[:, 0]], 1)
        r.update(F, S)
    g = r.gate(np.array([[0.0, 1, 0], [1.0, 1, 0]]))
    assert np.argmax(g[0]) == 0 and np.argmax(g[1]) == 1


def test_chain_with_oracle_beats_uniform():
    rng, w, ops = setup()
    X0 = np.stack([w.sample(rng, r, 20) for r in range(3)], 1)
    ora = run_chain(ops, X0, np.random.default_rng(5), lambda r, Y, s: np.tile(np.eye(3)[r], (len(Y), 1)))
    uni = run_chain(ops, X0, np.random.default_rng(5), lambda r, Y, s: np.full((len(Y), 3), 1 / 3))
    assert np.mean((ora - X0) ** 2) < np.mean((uni - X0) ** 2)


def test_cycles_environment_has_intransitive_duels():
    rng = np.random.default_rng(0)
    w, ops, K, pre, post = study.make_env('cycles', rng)
    X = study.draw(w, rng, pre[0], 6000)
    sg = np.full(len(X), 0.6)
    Y = X + 0.6 * rng.standard_normal(X.shape)
    S = study.probe_scores(ops, X, Y, sg)
    win = lambda a, b: np.mean(S[:, a] < S[:, b])
    # B beats A, C beats B, A beats C in region 0
    assert win(1, 0) > 0.5 and win(2, 1) > 0.5 and win(0, 2) > 0.5


def test_run_item_smoke():
    rec = study.run_item('bandit', 0, 0.1)
    assert rec['oracle']['post'] < rec['fixed']['post']
    assert len(rec['curves']['router']) == study.E
