import numpy as np
import pytest

from chesson_overlap import (
    random_model, chesson_measures, feature_form, reduced_lv,
    invasion_vs_lone_resident, chesson_invasion, full_model_invasion,
)


@pytest.mark.parametrize("seed", range(20))
def test_feature_form_and_measures(seed):
    rng = np.random.default_rng(seed)
    c, v, K, r, mu = random_model(rng, S=4, M=7)
    s, kappa, rho = chesson_measures(c, v, K, r, mu)
    U, b, cost = feature_form(c, v, K, r, mu)
    A, g = reduced_lv(c, v, K, r, mu)
    norms = np.linalg.norm(U, axis=0)
    assert np.allclose(A, U.T @ U)
    assert np.allclose(g, U.T @ b - cost)
    assert np.allclose(s, norms)
    assert np.allclose(rho, (U.T @ U) / np.outer(norms, norms))
    assert np.allclose(kappa, g / norms)
    assert np.all(rho <= 1 + 1e-12) and np.all(rho >= 0)


@pytest.mark.parametrize("seed", range(20))
def test_chesson_eq1_and_invasion(seed):
    rng = np.random.default_rng(100 + seed)
    c, v, K, r, mu = random_model(rng, S=2, M=5)
    s, kappa, rho = chesson_measures(c, v, K, r, mu)
    A, g = reduced_lv(c, v, K, r, mu)
    alpha = A / g[:, None]
    for i, j in [(0, 1), (1, 0)]:
        assert np.isclose(kappa[j] / kappa[i] * rho[i, j], alpha[i, j] / alpha[j, j])
        assert np.isclose(invasion_vs_lone_resident(c, v, K, r, mu, i, j),
                          chesson_invasion(c, v, K, r, mu, i, j))


def test_full_model_matches_while_resources_positive():
    checked = 0
    for seed in range(30):
        rng = np.random.default_rng(500 + seed)
        c, v, K, r, mu = random_model(rng, S=2, M=5)
        mu = mu + 1.5  # higher maintenance keeps the resident from exhausting a resource
        A, g = reduced_lv(c, v, K, r, mu)
        if g[1] <= 0:  # the resident cannot persist alone
            continue
        gfull, Rmin = full_model_invasion(c, v, K, r, mu, 0, 1)
        if Rmin > 1e-3:  # the reduction holds only while every resource is positive
            assert np.isclose(gfull, chesson_invasion(c, v, K, r, mu, 0, 1), atol=1e-6)
            checked += 1
    assert checked >= 10
