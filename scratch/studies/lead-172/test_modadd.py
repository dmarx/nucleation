import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modadd as M  # noqa: E402


def test_gradients_match_finite_differences():
    p, n = 7, 6
    rng = np.random.default_rng(0)
    params = M.init_params(p, n, rng)
    params["b1"] += 0.3
    a, b, y = M.all_pairs(p)
    _, g = M.loss_and_grads(params, a, b, y)
    for k in params:
        idx = tuple(rng.integers(0, s) for s in params[k].shape)
        old = params[k][idx]
        params[k][idx] = old + 1e-6
        lp = M.ce(params, a, b, y)
        params[k][idx] = old - 1e-6
        lm = M.ce(params, a, b, y)
        params[k][idx] = old
        assert abs((lp - lm) / 2e-6 - g[k][idx]) < 1e-5, k


def test_rule_triads_hold_all_energy_of_the_task():
    p = 7
    a, b, c = M.all_pairs(p)
    f = np.zeros((p, p, p))
    f[a, b, c] = 1.0
    f = f - f.mean(2, keepdims=True)
    E = np.abs(np.fft.fftn(f)) ** 2
    _, m3 = M.rule_masks(p)
    assert np.isclose(E[m3].sum() / E.sum(), 1.0)
    n2, n3 = M.null_masks(p, 3)
    for m in n3:
        assert m.sum() == m3.sum() and not (m & m3).any()
        assert np.isclose(E[m].sum(), 0.0)


def test_ntk_closed_form_matches_jacobians():
    p, n = 5, 4
    rng = np.random.default_rng(1)
    params = M.init_params(p, n, rng)
    a, b, _ = M.all_pairs(p)
    K = M.ntk(params, p)
    # explicit Jacobian of every logit w.r.t. every parameter
    keys = list(params)
    J = np.zeros((p * p, p, sum(params[k].size for k in keys)))
    off = 0
    for k in keys:
        for j in range(params[k].size):
            idx = np.unravel_index(j, params[k].shape)
            old = params[k][idx]
            params[k][idx] = old + 1e-6
            fp = M.forward(params, a, b)[2]
            params[k][idx] = old - 1e-6
            fm = M.forward(params, a, b)[2]
            params[k][idx] = old
            J[:, :, off + j] = (fp - fm) / 2e-6
        off += params[k].size
    K2 = np.einsum("xcq,ycq->xy", J, J)
    assert np.allclose(K, K2, atol=1e-4)


def test_diag_basis_spans_functions_of_sum():
    p = 5
    Q = M.diag_char_basis(p)
    a, b, c = M.all_pairs(p)
    v = np.cos(2 * np.pi * 2 * c / p)
    assert np.isclose(np.linalg.norm(Q.T @ v), np.linalg.norm(v))
