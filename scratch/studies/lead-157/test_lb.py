import numpy as np
import pytest

import lb


@pytest.fixture(scope="module")
def setup():
    task = lb.make_task(0)
    X, y = lb.sample(task, 1500, "both", 1)
    p = lb.train(lb.init(16, 0), X, y, epochs=8)
    return task, X, y, p


def test_grad_matches_finite_difference():
    task = lb.make_task(0)
    X, y = lb.sample(task, 50, "both", 2)
    p = lb.init(5, 3)
    p = [a + 0.1 for a in p]  # nonzero biases
    g = lb.flat(lb.grad(p, X, y))
    th = lb.flat(p)
    r = np.random.default_rng(0)
    for i in r.choice(th.size, 12, replace=False):
        e = np.zeros_like(th)
        e[i] = 1e-5
        fd = (lb.ce(lb.forward(lb.unflat(th + e, p), X), y)
              - lb.ce(lb.forward(lb.unflat(th - e, p), X), y)) / 2e-5
        assert abs(fd - g[i]) < 1e-5 + 1e-4 * abs(fd)


def test_permute_and_rescale_preserve_function(setup):
    _, X, _, p = setup
    r = np.random.default_rng(1)
    h = len(p[1])
    q = lb.rescale(lb.permute(p, r.permutation(h), r.permutation(h)),
                   np.exp(r.uniform(-1, 1, h)), np.exp(r.uniform(-1, 1, h)))
    assert np.allclose(lb.forward(p, X), lb.forward(q, X), atol=1e-9)
    assert np.allclose(lb.forward(lb.canonical(p), X), lb.forward(p, X), atol=1e-9)


def test_canonical_is_scale_invariant(setup):
    _, _, _, p = setup
    r = np.random.default_rng(2)
    h = len(p[1])
    q = lb.rescale(p, np.exp(r.uniform(-1, 1, h)), np.exp(r.uniform(-1, 1, h)))
    for a, b in zip(lb.canonical(p), lb.canonical(q)):
        assert np.allclose(a, b, atol=1e-9)


@pytest.mark.parametrize("method", ["wm", "am"])
def test_matching_recovers_a_hidden_permutation(setup, method):
    _, X, _, p = setup
    r = np.random.default_rng(3)
    h = len(p[1])
    q = lb.permute(p, r.permutation(h), r.permutation(h))
    _, back = lb.align(method, p, q, X)
    for a, b in zip(p, back):
        assert np.allclose(a, b)


def test_swm_recovers_permutation_and_rescaling(setup):
    _, X, y, p = setup
    r = np.random.default_rng(4)
    h = len(p[1])
    q = lb.rescale(lb.permute(p, r.permutation(h), r.permutation(h)),
                   np.exp(r.uniform(-1.4, 1.4, h)), np.exp(r.uniform(-1.4, 1.4, h)))
    a, b = lb.align("swm", p, q, X)
    res = lb.barrier("linear", a, b, None, X, y)
    assert abs(res["loss_barrier"]) < 1e-9
    # permutation alone leaves a barrier between these functionally identical nets
    a, b = lb.align("am", p, q, X)
    assert lb.barrier("linear", a, b, None, X, y)["loss_barrier"] > 1e-3


def test_brute_force_finds_hidden_permutation():
    task = lb.make_task(0)
    X, y = lb.sample(task, 400, "both", 5)
    p = lb.train(lb.init(4, 1), X, y, epochs=5)
    r = np.random.default_rng(5)
    q = lb.permute(p, r.permutation(4), r.permutation(4))
    back = lb.brute_force_match(p, q, X, y)
    assert lb.barrier("linear", p, back, None, X, y)["loss_barrier"] < 1e-9


def test_barrier_zero_for_identical_endpoints_and_paths_hit_endpoints(setup):
    _, X, y, p = setup
    pm = [a + 1.0 for a in p]
    for fam in ("linear", "bezier", "polychain"):
        for t, want in ((0.0, p), (1.0, p)):
            for a, b in zip(lb.point(fam, p, p, pm, t), want):
                assert np.allclose(a, b)
    assert lb.barrier("linear", p, p, None, X, y)["loss_barrier"] == pytest.approx(0, abs=1e-12)


def test_curve_fit_lowers_midpoint_loss(setup):
    task, X, y, p = setup
    q = lb.train(lb.init(16, 7), X, y, epochs=8)
    mid0 = lb.ce(lb.forward(lb.point("bezier", p, q, [(a + b) / 2 for a, b in zip(p, q)], 0.5), X), y)
    pm = lb.fit_curve("bezier", p, q, X, y, steps=300)
    mid1 = lb.ce(lb.forward(lb.point("bezier", p, q, pm, 0.5), X), y)
    assert mid1 < mid0


def test_hessian_eig_on_quadratic_like_check(setup):
    _, X, y, p = setup
    lam = lb.top_hessian_eig(p, X[:500], y[:500], iters=20)
    assert lam > 0


def test_cue_reliance_separates_training_cues():
    task = lb.make_task(0)
    XA, yA = lb.sample(task, 2000, "A", 10)
    p = lb.train(lb.init(16, 0), XA, yA, epochs=10)
    r = lb.cue_reliance(p, task)
    assert r["acc_A_only"] > 0.8 and r["acc_B_only"] < 0.4


def test_full_group_search_removes_rescaled_twin_barrier():
    task = lb.make_task(0)
    X, y = lb.sample(task, 400, "both", 5)
    p = lb.train(lb.init(4, 1), X, y, epochs=5)
    r = np.random.default_rng(6)
    q = lb.rescale(lb.permute(p, r.permutation(4), r.permutation(4)),
                   np.exp(r.uniform(-1, 1, 4)), np.exp(r.uniform(-1, 1, 4)))
    a, b = lb.full_group_search(p, q, X, y)
    assert lb.barrier("linear", a, b, None, X, y)["loss_barrier"] < 1e-4


def test_llfc_is_one_for_identical_nets(setup):
    _, X, _, p = setup
    assert np.allclose(lb.llfc_cos(p, p, X), 1.0)
