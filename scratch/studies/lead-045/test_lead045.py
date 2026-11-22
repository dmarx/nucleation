import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geometry import (task_vectors, simulate, first_crossing, ode_clock,
                      ode_curves, domino_limit_ratio, gd_times, acceleration_sign,
                      hadamard4, rotated_quadratic, hadamard_phase1_end)
from network import (make_data, init_params, forward, numeric_grad_check,
                     train, peak_rate_times)


def test_task_vectors_orthonormal():
    T = task_vectors(5, 200, seed=3)
    assert np.allclose(T @ T.T, np.eye(5), atol=1e-12)


def test_first_crossing_interpolates():
    t = np.array([0, 1, 2, 3])
    s = np.array([[0.0, 0.0], [0.4, 0.1], [0.8, 0.2], [1.0, 0.3]])
    out = first_crossing(t, s, 0.6)
    assert out[0] == pytest.approx(1.5)
    assert np.isnan(out[1])


def test_gd_simulation_matches_closed_form():
    p = [0.8, 0.2]
    T = task_vectors(2, 50)
    eta = 1e-3
    ts, s = simulate(p, T, "gd", eta, 20000, record_every=10)
    tt = first_crossing(ts, s, 0.9)
    # discrete steps: u <- (1 - 2 eta p) u; closed form is continuous time
    assert np.allclose(tt, gd_times(p, 0.1, eta), rtol=2e-3)


def test_equal_frequencies_give_ratio_one():
    assert ode_clock([0.5, 0.5], 0.1)[1] == pytest.approx(ode_clock([0.5, 0.5], 0.1)[0])


def test_ode_ratio_tends_to_domino_limit():
    eps = 0.1
    t = ode_clock([1.0, 1e-5], eps)
    assert t[1] / t[0] == pytest.approx(domino_limit_ratio(2, eps), rel=2e-3)
    t3 = ode_clock([1.0, 1e-4, 1e-8], eps)
    assert t3[2] / t3[0] == pytest.approx(domino_limit_ratio(3, eps), rel=5e-3)


def test_total_skill_bounds():
    # d(sum s)/dt = c ||p o u||_1 / ||p o u||_2, between c and c sqrt(n)
    p = np.array([0.6, 0.3, 0.1])
    grid = np.linspace(0, 3, 301)
    s = ode_curves(p, grid)
    tot = s.sum(1)
    assert np.all(tot >= grid - 1e-3)
    assert np.all(tot <= np.sqrt(3) * grid + 1e-3)


def test_acceleration_sign():
    p = [0.7, 0.2, 0.1]
    u = [0.5, 0.9, 0.95]
    assert acceleration_sign(p, u, 0) < 0      # strongest decelerates
    assert acceleration_sign(p, u, 2) > 0      # weakest accelerates


def test_sign_descent_follows_derived_ode():
    d, eta = 1000, 1e-4
    c = eta * np.sqrt(2 * d / np.pi)
    for p1 in [0.7, 0.95]:
        p = [p1, 1 - p1]
        ts, s = simulate(p, task_vectors(2, d), "sign", eta, 3000)
        tt = first_crossing(ts, s, 0.9)
        pred = ode_clock(p, 0.1) / c
        assert np.allclose(tt, pred, rtol=0.03)


def test_sign_descent_aligned_tasks_learn_together():
    # tasks on disjoint coordinates: every coordinate moves at eta, whatever p
    d = 40
    T = np.zeros((2, d))
    T[0, :20] = 1 / np.sqrt(20)
    T[1, 20:] = 1 / np.sqrt(20)
    ts, s = simulate([0.95, 0.05], T, "sign", 1e-3, 2000)
    tt = first_crossing(ts, s, 0.9)
    assert abs(tt[0] - tt[1]) <= 1


def test_hadamard_phase_one_exact():
    lam = [1.0, 0.1, 0.01, 0.001]
    eta = 1e-3
    xs = rotated_quadratic(hadamard4(), lam, "sign", eta, 600)
    k_end = int((1 - hadamard_phase1_end(lam)) / (2 * eta))
    assert np.allclose(xs[:k_end, 1:], 1.0, atol=1e-12)
    assert np.allclose(xs[:k_end, 0], 1 - 2 * eta * np.arange(k_end), atol=1e-9)
    xi = rotated_quadratic(np.eye(4), lam, "sign", eta, 600)
    assert np.allclose(xi[300], xi[300][0])  # aligned: all four together


def test_network_init_output_zero_and_grads():
    data = make_data(3, 4, 300, 50, 1.0, seed=0)
    for scale in [1.0, 0.01]:
        params = init_params(data["Z"].shape[1], 16, scale, seed=1)
        f, _ = forward(params, data["Z"])
        assert np.allclose(f, 0.0)
    params = init_params(data["Z"].shape[1], 16, 1.0, seed=1)
    params[1] = params[1] + 0.1 * np.random.default_rng(0).standard_normal(16)
    assert numeric_grad_check(params, data["Z"], data["Y"]) < 1e-5


def test_network_learns_and_peaks():
    data = make_data(2, 4, 800, 100, 1.0, seed=0)
    ts, tr, te, _ = train(data, 16, 1.0, "gd", 0.2, 600, record_every=5)
    assert tr[-1].min() > 0.9
    pk = peak_rate_times(ts, tr)
    assert pk.shape == (2,)
