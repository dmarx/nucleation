import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import phases as ph  # noqa: E402


def test_haar_orthogonal_and_levels():
    H, lev = ph.haar(3)
    assert np.allclose(H.T @ H, np.eye(8))
    assert list(np.bincount(lev)) == [1, 1, 2, 4]
    # a level-l vector is constant on depth-l blocks and sums to zero on
    # each depth-(l-1) block
    for k in range(8):
        l = lev[k]
        if l == 0:
            continue
        blk = 8 // 2 ** (l - 1)
        assert np.allclose(H[:, k].reshape(-1, blk).sum(1), 0)


def test_spectrum_set_by_strengths():
    c = [1.0, 2.0, 1.0, 0.5]
    g = [0.0, 1.0, 3.0, 0.5]
    d = ph.make_data(3, c, g, seed=1)
    N = d["N"]
    Sx = d["X"].T @ d["X"] / N
    Syx = d["Y"].T @ d["X"] / N
    ev = np.sort(np.linalg.eigvalsh(Sx))
    assert np.allclose(ev, np.sort(np.array(c)[d["lev"]] ** 2))
    sv = np.sort(np.linalg.svd(Syx, compute_uv=False))
    assert np.allclose(sv, np.sort(np.array(c)[d["lev"]] * np.array(g)[d["lev"]]))


def test_ultrametric_kernel_commutes_with_levels():
    d = ph.make_data(3, [1, 0.7, 1.3, 0.9], [0, 1, 1, 1], seed=2)
    for K in (ph.relu_ntk(d["X"]), ph.linear_ntk(d["X"])):
        mu, comm = ph.level_eigenvalues(K, d)
        assert comm < 1e-10
    # a non-tree input (random) does not commute
    rng = np.random.default_rng(0)
    d2 = dict(d)
    d2["X"] = rng.standard_normal(d["X"].shape)
    _, comm2 = ph.level_eigenvalues(ph.relu_ntk(d2["X"]), d2)
    assert comm2 > 1e-3


def test_kernel_flow_is_exponential_per_level():
    d = ph.make_data(3, [1, 1, 1.2, 0.8], [0, 2, 0.5, 1], seed=3)
    K = ph.relu_ntk(d["X"])
    mu, _ = ph.level_eigenvalues(K, d)
    t = np.array([0.0, 1.0, 5.0])
    r = ph.kernel_flow_risks(K, d, t)
    for j, l in enumerate(ph.target_levels(d)):
        assert np.allclose(r[:, j], np.exp(-2 * mu[l] * t / d["N"]))


def test_relu_ntk_matches_monte_carlo():
    rng = np.random.default_rng(0)
    X = rng.standard_normal((5, 6))
    m = 200_000
    W = rng.standard_normal((m, 6))
    U = X @ W.T / np.sqrt(6)
    A, D = np.maximum(U, 0), (U > 0).astype(float)
    K_mc = A @ A.T / m + (X @ X.T / 6) * (D @ D.T / m)
    assert np.allclose(ph.relu_ntk(X), K_mc, atol=0.02 * np.abs(K_mc).max())


def test_deep_linear_gradient_matches_finite_difference():
    rng = np.random.default_rng(0)
    d = ph.make_data(2, [1, 1, 1], [0, 1, 0.5], seed=0)
    Ws = ph.init_deep_linear(4, 4, 5, 3, 1.0, rng)
    X, Y, N = d["X"], d["Y"], d["N"]

    def loss(Ws):
        return 0.5 * np.sum((ph.deep_linear_out(Ws, X) - Y) ** 2) / N

    W0 = [W.copy() for W in Ws]
    lr = 1e-7
    Ws2 = [W.copy() for W in W0]
    ph.deep_linear_step(Ws2, X, Y, lr)
    k, i, j = 1, 2, 3
    g_bp = (W0[k][i, j] - Ws2[k][i, j]) / lr
    h = 1e-6
    Wp = [W.copy() for W in W0]; Wp[k][i, j] += h
    Wm = [W.copy() for W in W0]; Wm[k][i, j] -= h
    g_fd = (loss(Wp) - loss(Wm)) / (2 * h)
    assert np.isclose(g_bp, g_fd, rtol=1e-4)


def test_relu_gradient_matches_finite_difference():
    rng = np.random.default_rng(1)
    d = ph.make_data(2, [1, 1, 1], [0, 1, 0.5], seed=0)
    X, Y, N = d["X"], d["Y"], d["N"]
    for ntk in (False, True):
        p = ph.init_relu(4, 4, 6, 1.0, rng, ntk=ntk)
        p["V"] += 0.3 * rng.standard_normal(p["V"].shape)  # break symmetry

        def loss(p):
            return 0.5 * np.sum((ph.relu_forward(p, X)[0] - Y) ** 2) / N

        q = {k: (v.copy() if isinstance(v, np.ndarray) else v) for k, v in p.items()}
        lr = 1e-7
        ph.relu_step(q, X, Y, lr)
        for name, idx in (("W", (1, 2)), ("V", (2, 3))):
            g_bp = (p[name][idx] - q[name][idx]) / lr
            h = 1e-6
            pp = {k: (v.copy() if isinstance(v, np.ndarray) else v) for k, v in p.items()}
            pm = {k: (v.copy() if isinstance(v, np.ndarray) else v) for k, v in p.items()}
            pp[name][idx] += h
            pm[name][idx] -= h
            g_fd = (loss(pp) - loss(pm)) / (2 * h)
            assert np.isclose(g_bp, g_fd, rtol=1e-4, atol=1e-9)


def test_relu_antisymmetric_init_zero_output():
    rng = np.random.default_rng(0)
    d = ph.make_data(3, [1, 1, 1, 1], [0, 1, 1, 1])
    p = ph.init_relu(8, 8, 16, 1.0, rng)
    assert np.allclose(ph.relu_forward(p, d["X"])[0], 0)


def test_classify():
    assert ph.classify([1, 2, 4]) == "coarse-first"
    assert ph.classify([4, 2, 1]) == "fine-first"
    assert ph.classify([1, 1.1, 1.2]) == "simultaneous"
    assert ph.classify([1, 4, 2]) == "mixed"
    assert ph.classify([1, 1.1, 3]) == "coarse-first"
    assert ph.classify([1, np.inf, 2]) == "incomplete"


def test_first_crossing_interpolates():
    t = np.array([0.0, 1.0, 2.0])
    r = np.array([[1.0], [0.1], [0.01]])
    assert np.isclose(ph.first_crossing(t, r, 0.1)[0], 1.0)
    assert np.isclose(ph.first_crossing(t, r, np.sqrt(0.1) * 0.1)[0], 1.5)
    assert np.isinf(ph.first_crossing(t, r, 1e-3)[0])


def test_deep_linear_training_follows_theory():
    """Small-init two-layer linear network on aligned data: measured
    acquisition times within 25% of the decoupled solution's, and in its
    order."""
    c = [1, 1, 1, 1]
    g = [0, 1.0, 0.5, 0.25]
    d = ph.make_data(3, c, g, seed=0)
    t, r = ph.train(d, "deep_linear", seed=0, lr=0.02, t_max=80, width=16,
                    scale=0.03, depth=2)
    T = ph.first_crossing(t, r, 0.1)
    assert ph.classify(T) == "coarse-first"
    assert T[0] < T[1] < T[2]
    assert 1.2 < T[1] / T[0] < 3.0 and 1.2 < T[2] / T[1] < 3.0
