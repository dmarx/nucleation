import numpy as np
from scipy.special import logsumexp

import model as M


def test_wo_table_normalized_and_relations():
    P = M.wo_table(0.3, 0.9, 0.2, 0.0)
    assert np.allclose(P.sum(-1), 1)
    # no signal, no objection: deploy whatever the arrangement
    assert np.allclose(P[0, :, 0], 1)
    # objection, no signal: A verifies, B verifies with prob m
    x = 4  # o=1, r=0, b=0
    assert np.isclose(P[x, 0b100, 1], 1) and np.isclose(P[x, 0b000, 1], 0.2)
    # signal: product team classifies severe at q0, reliability at q1
    x = 2  # r=1
    assert np.isclose(P[x, 0b000, 2], 0.3) and np.isclose(P[x, 0b010, 2], 0.9)
    # override: business-critical release deploys despite severe
    x = 3  # r=1, b=1
    assert np.isclose(P[x, 0b001, 2], 0) and np.isclose(P[x, 0b001, 0], 1)


def test_wo_table_vectorized():
    q = np.array([0.2, 0.5])
    P = M.wo_table(q, 0.9, 0.1, 0.05)
    assert P.shape == (2, 8, 8, 3)
    assert np.allclose(P[1], M.wo_table(0.5, 0.9, 0.1, 0.05))


def test_dirichlet_evidence_brute_force():
    # one cell, counts (2, 1, 0): evidence = 2! 1! 0! * 2! / (3+2)!... exact
    c = np.array([[2.0, 1.0, 0.0]])
    le, _ = M.dirichlet_cells(c)
    # Monte Carlo over the Dirichlet(1,1,1) prior
    rng = np.random.default_rng(1)
    th = rng.dirichlet(np.ones(3), size=400000)
    mc = np.log(np.mean(th[:, 0] ** 2 * th[:, 1]))
    assert abs(le - mc) < 0.02


def test_features_dims():
    assert M.features("C2")[0].shape == (8, 8, 7)
    assert M.features("C3")[0].shape == (8, 8, 19)


def test_laplace_close_to_quadrature_one_feature():
    # gate with a single intercept feature, 2 weights; compare Laplace with
    # a 2-D grid integral of the exact posterior
    Phi = np.ones((8, 8, 1))
    n = np.zeros((8, 8, 3))
    n[0, 0] = [40, 25, 10]
    le, pred, w = M.gate_fit(n, Phi, sigma=2.0)
    g = np.linspace(-8, 8, 801)
    W1, W2 = np.meshgrid(g, g, indexing="ij")
    z = np.stack([np.zeros_like(W1), W1, W2], -1)
    lp = z - logsumexp(z, axis=-1, keepdims=True)
    ll = (n[0, 0] * lp).sum(-1)
    lprior = -0.5 * (W1**2 + W2**2) / 4 - np.log(2 * np.pi * 4)
    exact = logsumexp(ll + lprior) + 2 * np.log(g[1] - g[0])
    assert abs(le - exact) < 0.05
    assert np.allclose(pred[0, 0], (n[0, 0] + 0.0) / 75, atol=0.03)


def test_wo_quadrature_against_monte_carlo():
    rng = np.random.default_rng(2)
    P = M.wo_table(0.3, 0.8, 0.2, 0.05)
    n = M.sample_counts(P, M.TRAIN_A, 15, rng)
    le, pred = M.wo_posterior(n, G=16)
    S = 200000
    th = (rng.uniform(size=S), rng.uniform(size=S), rng.uniform(size=S),
          rng.uniform(0, M.EPS_MAX, size=S))
    ll = np.concatenate([(n * np.log(M.wo_table(*(t[i:i + 20000] for t in th))))
                         .sum(axis=(-3, -2, -1)) for i in range(0, S, 20000)])
    mc = logsumexp(ll) - np.log(S)
    assert abs(le - mc) < 0.1
    assert np.allclose(pred.sum(-1), 1)


def test_gate_recovers_additive_world():
    # data drawn from C2's own family: C2 should beat C1 in evidence
    rng = np.random.default_rng(3)
    Phi, _ = M.features("C2")
    W = rng.normal(0, 1, size=(2, Phi.shape[-1]))
    P = M._gate_probs(W.ravel(), Phi)
    n = M.sample_counts(P, M.TRAIN_A, 300, rng)
    le2, _, _ = M.gate_fit(n, Phi)
    le1, _ = M.c1(n)
    assert le2 > le1
