import numpy as np

import diag_rescale as d


def _params(rng):
    return tuple(rng.uniform(0.1, 1.0, d.D) for _ in range(4))


def test_rescale_preserves_function():
    rng = np.random.default_rng(0)
    p = _params(rng)
    for c in (0.1, 0.3, 2.0):
        assert np.allclose(d.beta_of(*d.rescale(p, c)), d.beta_of(*p), atol=1e-12)


def test_finetune_start_is_zero_function():
    rng = np.random.default_rng(1)
    p = _params(rng)
    assert np.allclose(d.beta_of(*d.finetune_start(p)), 0.0)


def test_train_interpolates_small_problem():
    rng = np.random.default_rng(2)
    X = rng.standard_normal((5, d.D))
    y = rng.standard_normal(5)
    init = [np.full(d.D, 0.1) for _ in range(4)]
    out, steps = d.train(X, y, *init, max_steps=200_000)
    r = X @ d.beta_of(*out) - y
    assert 0.5 * np.mean(r ** 2) < 1e-8


def test_probe_reaches_same_function_for_any_rescale():
    """Readout-only training from P_c and P_1 reaches the same beta."""
    rng = np.random.default_rng(3)
    p = _params(rng)
    X = rng.standard_normal((6, d.D))
    y = rng.standard_normal(6)
    outs = []
    for c in (1.0, 0.3):
        start = d.finetune_start(d.rescale(p, c), gamma=0.0)
        o, _ = d.train(X, y, *start, train_first=False, tol=1e-14, max_steps=400_000)
        outs.append(d.beta_of(*o))
    assert np.allclose(outs[0], outs[1], atol=1e-4)
