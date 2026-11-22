"""pytest for tms.py (run: python3 -I -m pytest scratch/studies/lead-175 -q)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pytest
import tms


def test_table1_losses():
    # Chen et al. Table 1, as checked by scratch/formal/tms_critical_sizes_check.py
    assert tms.pop_loss(*tms.CRIT["6"]) == pytest.approx(0.04819, abs=2e-5)
    assert tms.pop_loss(*tms.CRIT["5"]) == pytest.approx(0.06874, abs=2e-5)
    assert tms.pop_loss(*tms.CRIT["5+"]) == pytest.approx(0.06180, abs=2e-5)


@pytest.mark.parametrize("seed", range(5))
def test_closed_form_matches_quadrature(seed):
    rng = np.random.default_rng(seed)
    W = rng.normal(size=(2, 6)); b = rng.normal(scale=0.5, size=6)
    assert tms.pop_loss(W, b) == pytest.approx(tms.pop_loss_quad(W, b, M=400001), rel=1e-6, abs=1e-9)


@pytest.mark.parametrize("seed", range(5))
def test_pop_gradient_finite_difference(seed):
    rng = np.random.default_rng(10 + seed)
    W = rng.normal(size=(2, 6)); b = rng.normal(scale=0.5, size=6)
    _, gW, gb = tms.pop_loss(W, b, grad=True)
    h = 1e-6
    for (r, c) in [(0, 0), (1, 3), (0, 5)]:
        E = np.zeros_like(W); E[r, c] = h
        fd = (tms.pop_loss(W + E, b) - tms.pop_loss(W - E, b)) / (2 * h)
        assert gW[r, c] == pytest.approx(fd, rel=1e-5, abs=1e-8)
    for j in (0, 4):
        e = np.zeros(6); e[j] = h
        fd = (tms.pop_loss(W, b + e) - tms.pop_loss(W, b - e)) / (2 * h)
        assert gb[j] == pytest.approx(fd, rel=1e-5, abs=1e-8)


def test_pop_gradient_vanishes_at_critical_points():
    for name in ("6", "5", "4"):
        _, gW, gb = tms.pop_loss(*tms.CRIT[name], grad=True)
        assert np.abs(gW).max() < 1e-3 and np.abs(gb).max() < 1e-3, name


def test_batch_gradient_finite_difference_and_mean():
    rng = np.random.default_rng(3)
    W = rng.normal(size=(2, 2, 6)); b = rng.normal(scale=0.3, size=(2, 6))
    idx = rng.integers(0, 6, size=(2, 7)); mu = rng.random((2, 7))
    loss, gW, gb = tms.batch_loss_grad(W, b, idx, mu)
    h = 1e-6
    E = np.zeros_like(W); E[1, 0, 2] = h
    fd = (tms.batch_loss_grad(W + E, b, idx, mu)[0] - tms.batch_loss_grad(W - E, b, idx, mu)[0]) / (2 * h)
    assert gW[1, 0, 2] == pytest.approx(fd[1], rel=1e-5)
    assert fd[0] == pytest.approx(0, abs=1e-8)          # runs do not interact
    e = np.zeros_like(b); e[0, 3] = h
    fd = (tms.batch_loss_grad(W, b + e, idx, mu)[0] - tms.batch_loss_grad(W, b - e, idx, mu)[0]) / (2 * h)
    assert gb[0, 3] == pytest.approx(fd[0], rel=1e-5, abs=1e-9)
    # a huge batch approximates the population loss
    n = 400000
    idx = rng.integers(0, 6, size=(1, n)); mu = rng.random((1, n))
    W6, b6 = tms.CRIT["6"]
    l, _, _ = tms.batch_loss_grad(W6[None], b6[None], idx, mu)
    assert l[0] == pytest.approx(0.04819, rel=0.02)


def test_classifier_on_critical_points():
    for name, (W, b) in tms.CRIT.items():
        k, s, m = tms.classify(W[None], b[None])
        assert tms.label(k[0], s[0], m[0]) == name
    # invariant under rotation of the hidden plane and permutation of features
    rng = np.random.default_rng(0)
    th = 0.37; Q = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    p = rng.permutation(6)
    W, b = tms.CRIT["5+"]
    k, s, m = tms.classify((Q @ W)[:, p][None], b[p][None])
    assert tms.label(k[0], s[0], m[0]) == "5+"
