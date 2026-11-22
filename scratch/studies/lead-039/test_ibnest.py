import numpy as np

import ibnest as ib

LN2 = np.log(2)
# CLAIM-387's source reduced to its three causal states: {0,1}, {2}, {3}.
P3 = np.array([0.5, 0.25, 0.25])
K3 = np.array([[1.0, 0.0], [7 / 8, 1 / 8], [5 / 8, 3 / 8]])


def test_claim392_values_reproduced():
    g = ib.simplex_grid(3, 240)
    for beta, ix, iy in [(8, 0.546, 0.097), (12, 0.952, 0.139)]:
        pts, w = ib.envelope_decomp(P3, K3, beta, g)
        IX, IY = ib.lagrangian_values(P3, K3, pts, w)
        assert abs(IX / LN2 - ix) < 0.01 and abs(IY / LN2 - iy) < 0.003


def test_claim392_hull_test_fails():
    g = ib.simplex_grid(3, 240)
    c, _ = ib.envelope_decomp(P3, K3, 8, g)
    f, _ = ib.envelope_decomp(P3, K3, 12, g)
    assert ib.hull_distance(c, f) > 3e-3
    assert ib.hull_distance(f, f) < 1e-9


def test_hull_distance_simple():
    hull = np.array([[1, 0, 0], [0, 1, 0]], float)
    assert ib.hull_distance([[0.5, 0.5, 0]], hull) < 1e-9
    assert abs(ib.hull_distance([[0.5, 0.25, 0.25]], hull) - 0.5) < 1e-7


def test_F_second_derivative_matches_phi():
    rng = np.random.default_rng(0)
    for _ in range(20):
        a, b = rng.dirichlet(np.ones(4)), rng.dirichlet(np.ones(4))
        K = np.vstack([a, b])
        beta = rng.uniform(1.5, 20)
        r, h = rng.uniform(0.1, 0.9), 1e-4
        R = np.array([[1 - r + h, r - h], [1 - r, r], [1 - r - h, r + h]])
        f = ib.F(R, K, beta)
        num = (f[0] - 2 * f[1] + f[2]) / h**2
        ana = (1 - beta * ib.phi(r, a, b)) / (beta * r * (1 - r))
        assert abs(num - ana) < 1e-4 * max(1, abs(ana))


def test_phi_concave():
    rng = np.random.default_rng(1)
    r = np.linspace(1e-3, 1 - 1e-3, 2001)
    for _ in range(200):
        n = rng.integers(2, 7)
        a, b = rng.dirichlet(np.ones(n) * 0.5), rng.dirichlet(np.ones(n) * 0.5)
        if rng.random() < 0.3:  # zero entries
            a[rng.integers(n)] = 0
            a /= a.sum()
        y = ib.phi(r, a, b)
        assert np.diff(y, 2).max() < 1e-9


def test_1d_decomp_binary():
    # Binary symmetric channel, uniform X: the optimum is symmetric.
    K = np.array([[0.9, 0.1], [0.1, 0.9]])
    g = ib.simplex_grid(2, 4000)
    pts, w = ib.envelope_decomp(np.array([0.5, 0.5]), K, 5, g)
    assert len(pts) == 2 and abs(pts[0, 1] + pts[1, 1] - 1) < 1e-3
