import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ikmodel as m  # noqa: E402


def naive_step(x, w, a, c, delta):
    """Loop transcription of eqs. (1)-(2) for one run."""
    N = len(x)
    xn = np.empty(N)
    wn = np.empty((N, N))
    for i in range(N):
        h = (1 - c) * x[i] + c * sum(w[i, j] * x[j] for j in range(N))
        xn[i] = a * h * (1 - h)
        num = np.array([(1 + delta * (1 - 2 * abs(x[i] - x[j]))) * w[i, j] for j in range(N)])
        wn[i] = num / num.sum()
    return xn, wn


def test_init_matches_paper():
    x, w = m.init_state(10, 3, np.random.default_rng(0))
    assert x.shape == (3, 10) and w.shape == (3, 10, 10)
    assert np.allclose(np.diagonal(w, axis1=1, axis2=2), 0)
    off = w[:, ~np.eye(10, dtype=bool)]
    assert np.allclose(off, 1 / 9)
    assert ((x > 0) & (x < 1)).all()


def test_step_matches_naive_transcription():
    rng = np.random.default_rng(1)
    x, w = m.init_state(7, 2, rng)
    w = w * rng.uniform(0.5, 1.5, size=w.shape)
    w /= w.sum(axis=2, keepdims=True)
    x1, w1 = m.step(x, w, 3.97, 0.12, 0.1)
    for s in range(2):
        xn, wn = naive_step(x[s], w[s], 3.97, 0.12, 0.1)
        assert np.allclose(x1[s], xn)
        assert np.allclose(w1[s], wn)


def test_step_preserves_normalization_and_zero_diagonal():
    x, w = m.init_state(20, 2, np.random.default_rng(2))
    x, w, wa = m.run(x, w, 3.97, 0.12, 0.1, 500, avg_from=400)
    assert np.allclose(w.sum(axis=2), 1)
    assert np.allclose(np.diagonal(w, axis1=1, axis2=2), 0)
    assert np.allclose(wa.sum(axis=2), 1)
    assert ((x > 0) & (x < 1)).all()


def test_wout_mean_is_one():
    x, w = m.init_state(15, 1, np.random.default_rng(3))
    x, w, _ = m.run(x, w, 3.97, 0.12, 0.1, 300)
    assert np.isclose(m.w_out(w[0]).mean(), 1.0)


def test_out_degree_counts_columns():
    w = np.zeros((4, 4))
    w[1, 0] = w[2, 0] = w[3, 0] = 1.0  # unit 0 sends to 1, 2, 3
    w[0, 1] = 1.0                      # unit 1 sends to 0
    assert list(m.out_degree(w)) == [3, 1, 0, 0]
    assert list(m.w_out(w)) == [3.0, 1.0, 0.0, 0.0]


def test_block_counts():
    w = np.zeros((4, 4))
    core = np.array([True, False, False, False])
    w[1, 0] = w[2, 0] = 1.0  # core -> periphery: 2
    w[0, 1] = 1.0            # periphery -> core: 1
    w[2, 3] = 1.0            # periphery -> periphery: 1
    assert m.block_counts(w, core) == {"CC": 0, "CP": 2, "PC": 1, "PP": 1}


def test_remove_units_renormalizes():
    x, w = m.init_state(6, 1, np.random.default_rng(4))
    x, w, _ = m.run(x, w, 3.97, 0.12, 0.1, 50)
    keep = np.array([True, False, True, True, False, True])
    x2, w2 = m.remove_units(x, w, keep)
    assert x2.shape == (1, 4) and w2.shape == (1, 4, 4)
    assert np.allclose(w2.sum(axis=2), 1)
    # ratios among survivors' weights are unchanged
    sub = w[0][np.ix_(keep, keep)]
    assert np.allclose(w2[0], sub / sub.sum(axis=1, keepdims=True))


def test_suppress_sources():
    x, w = m.init_state(5, 1, np.random.default_rng(5))
    src = np.array([True, False, False, False, False])
    w2 = m.suppress_sources(w, src, 1e-3)
    assert np.allclose(w2.sum(axis=2), 1)
    # row 1 gave 1/4 to each of 0, 2, 3, 4; now unit 0 gets eps-weighted share
    assert np.isclose(w2[0, 1, 0], 1e-3 / (3 + 1e-3))
    assert (w2[0, 1:, 0] > 0).all()
