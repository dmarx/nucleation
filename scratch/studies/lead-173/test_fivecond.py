import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import pytest

from fivecond import Model, TOL
from witnesses import A389, S389, var1_witnesses, var2_witnesses, leaky_witnesses, pad
from run import random_model, forbidden, allowed_configs


def finite_lag_te(m, K=60):
    """Transfer entropy by regression on K lags of Y (exact covariances)."""
    mY = m.m
    blocks = [[m.L @ np.linalg.matrix_power(m.Ac, abs(i - j)) @ m.Pi @ m.L.T if i >= j
               else (m.L @ np.linalg.matrix_power(m.Ac, abs(i - j)) @ m.Pi @ m.L.T).T
               for j in range(K + 1)] for i in range(K + 1)]
    C = np.block(blocks)  # (Y_{t+1}, Y_t, ..., Y_{t-K+1})
    a = C[:mY, :mY]; b = C[:mY, mY:]; c = C[mY:, mY:]
    own = a - b @ np.linalg.solve(c, b.T)
    full = m.L @ m.Sc @ m.L.T
    return 0.5 * (np.linalg.slogdet(own)[1] - np.linalg.slogdet(full)[1])


def test_claim389_numbers():
    m = Model([A389], S389, [[1, 0]], [[0, 1]])
    assert abs(m.te() - 0.5 * np.log(0.75 / 0.59)) < 1e-9
    assert m.memory_cov_defect() < TOL
    assert max(m.memory_kernels()) < TOL


def test_ar2_memory_matches_question():
    m = var2_witnesses()["1100"]
    k = m.memory_kernels(3)
    assert abs(k[0] - 0.147) < 1e-3 and abs(k[1] - 0.0315) < 1e-3
    assert m.te() < TOL


@pytest.mark.parametrize("seed", range(20))
def test_riccati_te_matches_finite_lag(seed):
    rng = np.random.default_rng(seed)
    m = random_model(rng, p=1 + seed % 2)
    assert abs(m.te() - finite_lag_te(m)) < 1e-6


@pytest.mark.parametrize("seed", range(40))
def test_memory_criteria_agree(seed):
    rng = np.random.default_rng(100 + seed)
    m = random_model(rng, p=1 + seed % 2)
    cov_zero = m.memory_cov_defect() < 1e-9
    ker_zero = max(m.memory_kernels(40)) < 1e-9
    assert cov_zero == ker_zero


def test_witnesses_land_in_their_cells():
    for W, eps in [(var1_witnesses(), 0.0), (var2_witnesses(), 0.0), (leaky_witnesses(), 0.01)]:
        for key, m in W.items():
            h = m.evaluate(h=2, eps=eps, b=2)["holds"]
            assert "".join("1" if h[c] else "0" for c in "PDMA") == key, m.name
            assert h["C"]
            hp = pad(m, 3 - m.m).evaluate(h=2, eps=eps, b=2)["holds"]
            assert all(hp[c] == h[c] for c in "PDMA") and not hp["C"]


def test_allowed_sets():
    assert len(allowed_configs(var=1, eps=0)) == 16
    assert len(allowed_configs(var=2, eps=0)) == 22
    assert len(allowed_configs(var=1, eps=0.01)) == 22
    assert len(allowed_configs(var=2, eps=0.01)) == 30


@pytest.mark.parametrize("seed", range(30))
def test_target_y_collapses_p_into_d_and_m(seed):
    rng = np.random.default_rng(500 + seed)
    m = random_model(rng, p=1 + seed % 2, m=1)
    my = Model(m.A_list, m.Sigma, m.L[:, :m.n], m.L[:, :m.n])
    d = my.evaluate(h=3)
    h = d["holds"]
    assert h["P"] == (h["D"] and h["M"])
    assert h["A"] == (h["D"] and h["M"])
