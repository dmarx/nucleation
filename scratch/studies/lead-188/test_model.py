import numpy as np
import pytest

import model as M


@pytest.fixture(scope="module")
def small():
    rng = np.random.default_rng(0)
    return [M.world(400, 60, 5, rng) for _ in range(3)]


def test_graph_simple():
    rng = np.random.default_rng(1)
    e = M.make_graph(500, 2.5, 2, 50, rng)
    assert (e[:, 0] != e[:, 1]).all()
    assert len(np.unique(e, axis=0)) == len(e)
    assert (e[:, 0] < e[:, 1]).all()


def test_cascade_extremes():
    rng = np.random.default_rng(2)
    e = M.make_graph(300, 2.5, 2, 30, rng)
    assert M.cascade(e, 300, 0.0, 5, rng).sum() == 1
    full = M.cascade(e, 300, 1.0, 5, rng)
    # T = 1: the seed's whole connected component
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import connected_components
    a = coo_matrix((np.ones(len(e)), (e[:, 0], e[:, 1])), shape=(300, 300))
    _, lab = connected_components(a, directed=False)
    assert full.sum() == (lab == lab[5]).sum()


def test_top_mask_size():
    s = np.array([5, 5, 5, 1, 2, 9, 9, 3, 4, 0.0])
    for q in (0.001, 0.1, 0.25, 1.0):
        assert M.top_mask(s, q).sum() == max(1, int(np.ceil(q * len(s))))
    assert M.top_mask(s, 0.2)[[5, 6]].all()


def test_m0_without_ascertainment_is_q():
    s = np.arange(1, 101, dtype=float)
    assert M.p_obs(np.ones(100), s, 0.05, 0.0) == pytest.approx(0.05)


def test_mc_reduces_to_m0_at_alpha_zero(small):
    for s, h in small:
        assert M.p_obs(M.w_mc(s, h, 0.0), s, 0.05, 0.0) == pytest.approx(
            M.p_obs(M.w_m0(s, h), s, 0.05, 0.0))


def test_mc_monotone_in_alpha(small):
    s, h = small[0]
    ps = [M.p_obs(M.w_mc(s, h, a), s, 0.05, 0.0) for a in (0, 0.5, 1, 2)]
    assert all(x <= y + 1e-12 for x, y in zip(ps, ps[1:]))


def test_bf_of_null_against_itself_is_one(small):
    r = M.likelihoods(small, 0.05, 0.0)
    # alpha grid starts at 0, so the MC curve's first point is M0
    assert r["curve_MC"][0] == pytest.approx(r["L_M0"], abs=1e-5)


def test_ascertainment_raises_null_likelihood(small):
    a = M.likelihoods(small, 0.05, 0.0)["L_M0"]
    b = M.likelihoods(small, 0.05, 1.0)["L_M0"]
    assert b > a
