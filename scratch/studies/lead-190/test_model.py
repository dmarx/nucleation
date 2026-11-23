import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402

one = M.one


def three(r=(0.7, 0.7, 0.7)):
    """Reader 0 and two sources, A (s=+1) and B (s=-1)."""
    return dict(N=3, s=np.array([1.0, 1.0, -1.0]), pref=np.array([0.5, 0.8, -0.8]),
                r=np.array(r))


@pytest.mark.parametrize("regime", ["A", "B"])
@pytest.mark.parametrize("m0,w0", [(0.0, 0.5), (0.3, 0.6), (-0.5, 0.2)])
def test_reader_is_lead090_institution(regime, m0, w0):
    """One reader with sources A and B and phi_s = 0 is LEAD-090's mean field."""
    P1 = one.default_params(g=12.0, regime=regime, r=(0.8, 0.6))
    P = M.params(g=12.0, zeta=1.0 if regime == "A" else 0.0, phi_s=0.0)
    pop = three(r=(0.7, 0.8, 0.6))
    m = np.array([m0, 0.1, -0.2])
    W = M.full_W(3)
    W[0] = [0.0, w0, 1 - w0]
    mask = np.ones((3, 3), bool)
    mask[0, 0] = False  # LEAD-090's collective does not retrieve
    m_new, Wt = M.meaning_mean_field(m, W, pop, P, mask)
    W_new = P["delta"] * W + (1 - P["delta"]) * Wt
    m1, a1 = one.mean_field(m0, 2 * w0 - 1, P1)
    assert m_new[0] == pytest.approx(m1, abs=1e-12)
    assert 2 * W_new[0, 1] - 1 == pytest.approx(a1, abs=1e-12)


def test_stochastic_mean_matches_mean_field():
    pop = M.population(N=6, seed=1)
    P = M.params(phi_s=0.2, zeta=0.5, k=400)
    rng = np.random.default_rng(0)
    m = np.linspace(-0.5, 0.5, 6)
    W = M.full_W(6)
    mf, _ = M.meaning_mean_field(m, W, pop, P)
    draws = np.array([M.meaning_stochastic(m, W, pop, P, rng)[0] for _ in range(3000)])
    assert np.allclose(draws.mean(axis=0), mf, atol=3e-3)


def test_population_jacobian_numeric():
    N = 8
    pop = M.population(N=N, seed=2)
    pop["r"] = np.full(N, 0.7)
    P = M.params(phi_s=0.25, zeta=0.6, g=9.0)
    J = M.population_jacobian(pop, P)
    s = pop["s"]

    def F(x):
        m, a = x[:N], x[N:]
        # the uniform row tilted along s so that sum_j W_ij s_j = a_i
        W = M.full_W(N) + np.outer(a, s - s.mean()) / ((s - s.mean()) @ s)
        m_new, Wt = M.meaning_mean_field(m, W, pop, P)
        W_new = P["delta"] * W + (1 - P["delta"]) * Wt
        return np.concatenate([m_new, W_new @ s])

    x0 = np.zeros(2 * N)
    assert np.allclose(F(x0), x0, atol=1e-14)  # the symmetric state is fixed
    h = 1e-6
    Jn = np.empty((2 * N, 2 * N))
    for k in range(2 * N):
        e = np.zeros(2 * N)
        e[k] = h
        Jn[:, k] = (F(x0 + e) - F(x0 - e)) / (2 * h)
    assert np.allclose(Jn, J, atol=1e-7)


def test_threshold_closed_form_matches_eigenvalues():
    N = 10
    pop = M.population(N=N, seed=3)
    rng = np.random.default_rng(4)
    n = 0
    for _ in range(300):
        P = M.params(phi_s=rng.uniform(0, 0.3), zeta=rng.uniform(0, 1),
                     g=rng.uniform(0, 30), rho=rng.uniform(0.05, 0.9),
                     delta=rng.uniform(0, 0.95))
        J = M.population_jacobian(pop, P)
        lhs, uni, diff = M.meaning_threshold(P)
        ev = np.linalg.eigvals(J)
        lam = max(abs(ev))
        if abs(lam - 1) < 1e-6:
            continue
        n += 1
        assert (lam > 1) == (lhs > uni)
        # count of unstable eigenvalues: 1 (uniform mode) or N (all modes)
        k = int((abs(ev) > 1 + 1e-9).sum())
        assert k == (0 if lhs <= uni else (N if lhs > diff else 1))
    assert n > 250


@pytest.mark.parametrize("agg", ["one-hop", "recursive", "loo"])
@pytest.mark.parametrize("obj", ["policy", "authority"])
def test_grad_matches_finite_differences(agg, obj):
    pop = M.population(N=7, seed=5)
    P = M.params(agg=agg, objective=obj, eta=0.6, lam=0.01)
    rng = np.random.default_rng(6)
    E = rng.uniform(0, 1, (7, 7))
    np.fill_diagonal(E, 0)
    E /= E.sum(axis=1, keepdims=True) * 1.3
    G = M.grad(E, pop["pref"], P)
    h = 1e-6
    for i in range(7):
        for j in range(7):
            if i == j:
                continue
            Ep, Em = E.copy(), E.copy()
            Ep[i, j] += h
            Em[i, j] -= h
            d = (M.objective(Ep, pop["pref"], P)[i] - M.objective(Em, pop["pref"], P)[i]) / (2 * h)
            assert G[i, j] == pytest.approx(d, abs=1e-6)


@pytest.mark.parametrize("agg", ["one-hop", "loo"])
def test_own_authority_insensitive_to_own_row(agg):
    pop = M.population(N=9, seed=7)
    P = M.params(agg=agg, eta=0.7)
    rng = np.random.default_rng(8)
    E = M.project_rows(rng.uniform(0, 0.3, (9, 9)))
    g = M.authority(E, P)
    for i in range(9):
        E2 = E.copy()
        E2[i] = M.project_rows(rng.uniform(0, 0.4, (9, 9)))[i]
        assert M.authority(E2, P)[i] == pytest.approx(g[i], abs=1e-12)
    P["agg"] = "recursive"
    E2 = E.copy()
    E2[0] = M.project_rows(rng.uniform(0, 0.4, (9, 9)))[0]
    assert abs(M.authority(E2, P)[0] - M.authority(E, P)[0]) > 1e-6


def test_projection():
    rng = np.random.default_rng(9)
    X = rng.normal(0, 1, (6, 6))
    Y = M.project_rows(X)
    assert np.all(Y >= 0) and np.all(np.diag(Y) == 0)
    assert np.all(Y.sum(axis=1) <= 1 + 1e-12)
    # a feasible row is unchanged
    Z = M.project_rows(np.abs(X) * 0.01)
    assert np.allclose(M.project_rows(Z), Z)


def test_reach_matches_budget_derivative():
    pop = M.population(N=6, seed=10)
    rng = np.random.default_rng(11)
    E = M.project_rows(rng.uniform(0, 0.5, (6, 6)))
    for agg in ("one-hop", "recursive", "loo"):
        P = M.params(agg=agg, eta=0.6)
        R = M.reach(E, P)
        h = 1e-6
        for i in range(6):
            bp, bm = np.ones(6), np.ones(6)
            bp[i] += h
            bm[i] -= h
            d = (M.authority(E, P, bp) - M.authority(E, P, bm)) / (2 * h)
            assert np.allclose(R[i], d, atol=1e-7)


def test_one_hop_policy_gradient_sign_is_claim375():
    """Under one hop, raising a grant to j moves p* toward p_j: the gradient
    is positive exactly when p_j lies on i's side of p* (CLAIM-375)."""
    pop = M.population(N=8, seed=12)
    P = M.params(lam=0.0)
    E = 0.3 * M.uniform_W(8)
    g = M.authority(E, P)
    pstar = g @ pop["pref"] / g.sum()
    G = M.grad(E, pop["pref"], P)
    for i in range(8):
        for j in range(8):
            if i != j:
                expect = np.sign((pop["pref"][i] - pstar) * (pop["pref"][j] - pstar))
                assert np.sign(G[i, j]) == expect
