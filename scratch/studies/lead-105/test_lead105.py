import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import crossed as c  # noqa: E402


def small_setup(seed=0, steps=200):
    a, b, b2 = c.make_tasks(seed)
    X, ids = c.make_data(seed)
    y = c.targets(X, ids, a, b)
    yn = c.targets(X, ids, a, b2)
    p = c.init_params(seed)
    c.train(p, X, y, c.Optimizer("adam", 3e-3), steps)
    return p, X, ids, y, yn


def test_probe_target_conflicts_with_task_a():
    a, b, b2 = c.make_tasks(3)
    assert abs(np.linalg.norm(b2) - 1) < 1e-12
    assert abs(a @ b) < 1e-12
    assert abs(a @ b2 + np.sqrt(3) / 2) < 1e-12


def test_gradient_matches_finite_differences():
    p, X, ids, y, _ = small_setup(steps=50)
    _, g = c.loss_and_grad(p, X, y)
    rng = np.random.default_rng(0)
    for k in p:
        for _ in range(3):
            idx = tuple(rng.integers(0, n) for n in p[k].shape)
            h = 1e-6
            q1, q2 = c.copy(p), c.copy(p)
            q1[k][idx] += h
            q2[k][idx] -= h
            num = (c.loss_and_grad(q1, X, y)[0] - c.loss_and_grad(q2, X, y)[0]) / (2 * h)
            assert abs(num - g[k][idx]) < 1e-6 * max(1, abs(num))


def test_permutation_preserves_function_and_probe():
    p, X, ids, _, yn = small_setup()
    q, _ = c.permute_units(p, np.random.default_rng(1))
    assert np.allclose(c.forward(p, X)[0], c.forward(q, X)[0])
    for po in ["sgd", "adam", "sign"]:
        r1 = c.probe(p, X, ids, yn, c.Optimizer(po, c.PROBE_LR[po]))
        r2 = c.probe(q, X, ids, yn, c.Optimizer(po, c.PROBE_LR[po]))
        assert abs(r1["peak_forget"] - r2["peak_forget"]) < 1e-9
        assert r1["tB"] == r2["tB"]


def test_rescaling_preserves_function_not_gradient_cosine():
    p, X, ids, _, yn = small_setup()
    q, _ = c.rescale_units(p, np.random.default_rng(2))
    assert np.allclose(c.forward(p, X)[0], c.forward(q, X)[0])
    r1 = c.probe(p, X, ids, yn, c.Optimizer("sgd", 1e-9))
    r2 = c.probe(q, X, ids, yn, c.Optimizer("sgd", 1e-9))
    assert abs(r1["sA0"] - r2["sA0"]) < 1e-9
    assert abs(r1["cos0"] - r2["cos0"]) > 1e-3


def test_sgd_on_rescaled_equals_preconditioned_sgd_on_original():
    p, X, ids, _, yn = small_setup()
    q, cvec = c.rescale_units(p, np.random.default_rng(4))
    lr = 0.01
    q_run = c.copy(q)
    c.train(q_run, X, yn, c.Optimizer("sgd", lr), 100)
    p_run = c.preconditioned_sgd_on_original(p, cvec, X, yn, lr, 100)
    assert np.allclose(c.forward(q_run, X)[0], c.forward(p_run, X)[0], atol=1e-9)


def test_sign_descent_and_adam_updates():
    p = {"W1": np.zeros((2, 2)), "b1": np.zeros(2), "w2": np.zeros(2), "b2": np.zeros(1)}
    g = {"W1": np.array([[1.0, -2.0], [0.0, 3.0]]), "b1": np.array([-1.0, 1.0]),
         "w2": np.array([5.0, -5.0]), "b2": np.array([0.5])}
    q = c.copy(p)
    c.Optimizer("sign", 0.1).step(q, g)
    assert np.allclose(q["W1"], -0.1 * np.sign(g["W1"]))
    q = c.copy(p)
    c.Optimizer("adam", 0.1).step(q, g)
    # first Adam step is lr * sign(g) up to eps
    assert np.allclose(q["w2"], -0.1 * np.sign(g["w2"]), atol=1e-6)


def test_segregation_bounds():
    p, X, ids, _, _ = small_setup()
    s = c.segregation(p, X, ids)
    assert 0.0 <= s <= 1.0
    sel = c.selectivity(p, X, ids)
    assert np.all((sel >= 0) & (sel <= 1 + 1e-9))


def test_ablation_zeroes_output_contribution():
    p, X, ids, _, _ = small_setup()
    units = np.array([0, 3, 5])
    q = c.ablate_units(p, units, np.random.default_rng(0))
    assert np.all(q["w2"][units] == 0)
    other = np.setdiff1d(np.arange(c.WIDTH), units)
    assert np.allclose(q["W1"][other], p["W1"][other])
