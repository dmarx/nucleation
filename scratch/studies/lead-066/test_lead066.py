import numpy as np
import pytest

import bound as B


def setup(depth=3, sigma=0.0, kernel="linear", seed=0, c=None, g=None):
    rng = np.random.default_rng(seed)
    H, lev = B.haar(depth)
    n = H.shape[0]
    c = c if c is not None else [1.0] + [0.8 ** (l - 1) for l in range(1, depth + 1)]
    g = g if g is not None else [0.0] + [1.0] * depth
    X0 = B.tree_inputs(H, lev, c, n, rng)
    X = B.perturb(X0, sigma, rng) if sigma > 0 else X0
    A = B.KERNELS[kernel](X) / n
    A0 = B.KERNELS[kernel](X0) / n
    y = B.tree_target(H, lev, g, rng)
    return H, lev, B.projectors(H, lev), A, A0, -y


def test_haar_orthonormal_and_levels():
    H, lev = B.haar(4)
    assert np.allclose(H.T @ H, np.eye(16))
    assert [int((lev == l).sum()) for l in range(5)] == [1, 1, 2, 4, 8]
    Ps = B.projectors(H, lev)
    assert np.allclose(sum(Ps), np.eye(16))


@pytest.mark.parametrize("kernel", ["linear", "relu_ntk", "rbf"])
def test_exact_commutation_on_tree_data(kernel):
    _, _, Ps, A, _, _ = setup(kernel=kernel)
    assert B.commutator_norms(A, Ps).max() < 1e-10


@pytest.mark.parametrize("kernel", ["linear", "relu_ntk", "rbf"])
def test_commutator_equals_offdiagonal_block_and_below_perturbation(kernel):
    _, _, Ps, A, A0, _ = setup(sigma=0.2, kernel=kernel, seed=3)
    n = A.shape[0]
    for P in Ps:
        Q = np.eye(n) - P
        eta = np.linalg.norm(A @ P - P @ A, 2)
        assert eta == pytest.approx(np.linalg.norm(P @ A @ Q, 2), rel=1e-10)
        assert eta <= np.linalg.norm(A - A0, 2) + 1e-12


def test_theorem1_holds_pointwise_in_time():
    for seed in range(5):
        H, lev, Ps, A, _, e0 = setup(depth=4, sigma=0.3, kernel="relu_ntk", seed=seed)
        D = B.pinch(A, Ps)
        f, fD = B.Flow(A, e0), B.Flow(D, e0)
        lam, Lam = B.block_extremes(A, H, lev)
        a = np.linalg.eigvalsh(A)[0]
        eta = B.commutator_norms(A, Ps)
        ts = np.geomspace(1e-3, 1e4, 500) / lam.max()
        diff = f(ts) - fD(ts)
        for l, P in enumerate(Ps):
            obs = np.linalg.norm(P @ diff, axis=0)
            bnd = B.theorem1_bound(ts, eta[l], lam[l], a, np.linalg.norm(e0))
            assert np.all(obs <= bnd * (1 + 1e-9) + 1e-13)
            assert np.all(bnd <= eta[l] * np.linalg.norm(e0) / lam[l] * (1 + 1e-12))


def test_sharpness_two_by_two():
    # start in a slow level, leak into a fast one: sup leakage -> eta/mu1
    mu1, mu2, eta = 1.0, 1e-4, 1e-3
    A = np.array([[mu1, eta], [eta, mu2]])
    f = B.Flow(A, np.array([0.0, 1.0]))
    ts = np.geomspace(1e-2, 1e3, 4000)
    sup = np.abs(f(ts)[0]).max()
    assert sup <= eta / (mu1 - 0) + 1e-15
    assert sup / (eta / mu1) > 0.99


def test_acquisition_time_inside_interval_exact_case():
    H, lev, Ps, A, _, e0 = setup(depth=3)
    lam, Lam = B.block_extremes(A, H, lev)
    f = B.Flow(A, e0)
    for l in range(1, 4):
        T = B.acquisition_time(f, Ps[l], 0.1, 100 / lam[l])
        assert T == pytest.approx(np.log(1 / np.sqrt(0.1)) / lam[l], rel=1e-8)


def test_davis_kahan():
    H, lev, Ps, A, _, _ = setup(depth=4, sigma=0.2, kernel="rbf", seed=1)
    lam, Lam = B.block_extremes(A, H, lev)
    eta = B.commutator_norms(A, Ps)
    for l, P in enumerate(Ps):
        assert B.davis_kahan_check(A, P, lam[l], Lam[l], eta[l]) <= 1 + 1e-9


def test_network_jacobian_and_zero_output():
    rng = np.random.default_rng(0)
    net = B.TwoLayerReLU(8, 32, 1.0, rng)
    X = rng.standard_normal((8, 8))
    assert np.allclose(net.forward(X), 0)
    net.a += 0.1 * rng.standard_normal(32)
    J = net.jacobian(X)
    v = rng.standard_normal(J.shape[1]) * 1e-6
    f0 = net.forward(X)
    net.a += v[:32]; net.W += v[32:].reshape(32, 8)
    assert np.allclose(net.forward(X) - f0, J @ v, atol=1e-9)
