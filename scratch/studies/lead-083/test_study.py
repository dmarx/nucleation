import numpy as np

import study


def test_block_test_finds_a_block():
    n = 6
    W = np.full((n, n), 0.01)
    W[:3, :3] = 1.0
    W[3:, 3:] = 1.0
    np.fill_diagonal(W, 0)
    gen = W - np.diag(W.sum(1))
    r = study.block_test(W, [0, 1, 2], gen)
    assert r["rho"] > 50 and r["entrywise"] > 50
    r2 = study.block_test(W, [0, 1, 3], gen)
    assert r2["rho"] < 2


def test_uniform_coupling_has_entrywise_ratio_one():
    n = 8
    W = np.full((n, n), 0.3)
    np.fill_diagonal(W, 0)
    gen = W - np.diag(W.sum(1))
    r = study.block_test(W, [0, 1, 2, 3], gen)
    assert abs(r["entrywise"] - 1) < 1e-12


def test_kappa():
    assert study.kappa(1.0, 1.0, 0.0) == 1.0
    assert study.kappa(1.0, 0.0, 0.0) == 0.0


def test_kink_energy_and_zero_mode():
    k = study.Kink(0.25)
    phi = k.ground()
    E, g = k.energy_grad(phi)
    assert abs(E - 2 * np.sqrt(2) / 3) < 1e-2
    ev = np.linalg.eigvalsh(k.hessian(phi))
    assert abs(ev[0]) < 1e-2 and abs(ev[1] - 1.5) < 0.05


def test_kink_gradient_matches_finite_difference():
    k = study.Kink(0.5)
    rng = np.random.default_rng(0)
    phi = np.tanh(k.x) + 0.1 * rng.standard_normal(k.n)
    E, g = k.energy_grad(phi)
    e = np.zeros(k.n); e[7] = 1e-6
    fd = (k.energy_grad(phi + e)[0] - k.energy_grad(phi - e)[0]) / 2e-6
    assert abs(fd - g[7]) < 1e-5


def test_kuramoto_conserves_phase_sum_with_identical_frequencies():
    N = 10
    omega = np.zeros(N)
    K = np.full((N, N), 1.0 / N); np.fill_diagonal(K, 0)
    th0 = np.random.default_rng(0).uniform(0, 6, N)
    rec = study.kuramoto_run(omega, K, 5.0, 0.01, th0, rec_every=1)
    assert abs(rec[-1].sum() - th0.sum()) < 1e-8
