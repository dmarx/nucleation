import numpy as np
from sim import *


def test_holonomy_and_twisted_eig():
    A = ring_with_chords(8)
    th = gauge_maps(np.random.default_rng(1).uniform(0, 6, 8), A)
    assert np.allclose(cycle_holonomies(A, th), 0, atol=1e-9)
    assert abs(min_eig(connection_laplacian(A, th, 1.0))) < 1e-9
    fr = frustrate(th, 0, 1, 1.0)
    h = cycle_holonomies(A, fr)
    assert np.any(np.abs(h) > 0.5)
    assert min_eig(connection_laplacian(A, fr, 1.0)) > 1e-3


def test_single_oscillator_limit_cycle():
    out = simulate(1, np.zeros((1, 1)) + 0, 60, mu=0.5, z0=[0.1])
    assert abs(abs(out["z"][-1, 0, 0]) - np.sqrt(0.5)) < 1e-3


def test_section_has_zero_incompatibility():
    A = ring_with_chords(8)
    phi = np.random.default_rng(2).uniform(0, 6, 8)
    th = gauge_maps(phi, A)
    z = np.exp(1j * phi)
    assert incompatibility(z, A, th)[0] < 1e-12
    assert incompatibility(np.ones(8), A, th)[0] > 0.1


def test_enforcing_coupling_attracts_to_section():
    A = ring_with_chords(8)
    phi = np.random.default_rng(3).uniform(0, 6, 8)
    th = gauge_maps(phi, A)
    out = simulate(8, A, 80, K=1.0, theta=th, mu=0.5)
    assert incompatibility(out["z"][-1], A, th)[0] < 1e-4


def test_conservative_norm_nearly_conserved():
    A = ring_with_chords(8)
    out = simulate(8, A, 20, dt=0.001, K=1.0, ctype="cons", z0=np.exp(1j * np.arange(8)))
    n0 = (np.abs(out["z"][0]) ** 2).sum()
    n1 = (np.abs(out["z"][-1]) ** 2).sum()
    assert abs(n1 / n0 - 1) < 0.05


def test_fit_linear_response_recovers_gains():
    A = ring_with_chords(6, chords=())
    from scipy.linalg import expm
    g = {e: 0.3 + 0.1 * i for i, e in enumerate(edges(A))}
    p = np.full(6, 0.2)
    dt = 0.01
    trajs = []
    for j in range(6):
        x0 = np.zeros(6); x0[j] = 1
        M = np.diag(p.copy())
        for (a, b), w in g.items():
            M[a, a] += w; M[b, b] += w; M[a, b] -= w; M[b, a] -= w
        Ts = np.arange(400) * dt
        trajs.append(np.array([expm(-M * t) @ x0 for t in Ts]))
    gf, pf = fit_linear_response(trajs, dt, A, ridge=1e-8)
    for e in g:
        assert abs(gf[e] - g[e]) < 0.03
    assert np.allclose(pf, p, atol=0.03)


def test_hansen_ghrist_higher_order():
    # interior vertex 0 with stalk R^2; boundary 1,2,3 scalar: v1=a+b, v2=a, v3=b
    I = np.eye(2)
    maps = [(0, 1, np.array([[1.0, 1.0]]), np.eye(1)),
            (0, 2, np.array([[1.0, 0.0]]), np.eye(1)),
            (0, 3, np.array([[0.0, 1.0]]), np.eye(1))]
    L, off = sheaf_laplacian([2, 1, 1, 1], maps)
    keep = np.arange(2, 5)
    Lr = kron_reduce(L, keep)
    S = null_space(Lr)
    assert pairwise_expressible(S, [np.array([0]), np.array([1]), np.array([2])]) == (2, 3)
    # scalar interior: pairwise suffices
    maps1 = [(0, k, np.eye(1), np.eye(1)) for k in (1, 2, 3)]
    L1, _ = sheaf_laplacian([1, 1, 1, 1], maps1)
    S1 = null_space(kron_reduce(L1, np.arange(1, 4)))
    assert pairwise_expressible(S1, [np.array([0]), np.array([1]), np.array([2])]) == (1, 1)
