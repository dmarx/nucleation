import math

import numpy as np

import gj_closed_groups as g


def test_minimal_closed_groups_and_influence():
    rng = np.random.default_rng(0)
    T = g.several_group_matrix(3, 4, 3, rng)
    groups = g.minimal_closed_groups(T)
    assert groups == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
    s = g.influence(T)
    for B in groups:
        assert abs(s[B].sum() - 1) < 1e-10          # Theorem 3 (i)
        assert np.all(s[B] > 0)                       # (iii)
        assert np.allclose(s[B] @ T[np.ix_(B, B)], s[B])
    assert np.all(s[12:] == 0)                        # (ii)


def test_limits_match_theorem_3():
    rng = np.random.default_rng(1)
    T = g.several_group_matrix(3, 4, 3, rng)
    s = g.influence(T)
    p = rng.random(T.shape[0])
    lim = g.limit_beliefs(T, p)
    cons = []
    for B in g.minimal_closed_groups(T):
        c = s[B] @ p[B]
        cons.append(c)
        assert np.allclose(lim[B], c, atol=1e-9)      # (iv)
    for x in lim[12:]:                                # (v): convex mixtures
        assert min(cons) - 1e-9 <= x <= max(cons) + 1e-9


def test_equal_weights_influence_is_one_over_k():
    k, m = 5, 4
    T = np.kron(np.eye(m), np.full((k, k), 1 / k))
    s = g.influence(T)
    assert np.allclose(s, 1 / k)


def test_group_miss_prob_exact():
    assert g.group_miss_prob(1, 0.5) == 1.0
    assert g.group_miss_prob(3, 0.5) == 2 / 8
    # k=4: |j/4-1/2| >= 0.25 for j in {0,1,3,4}: 1+4+4+1 = 10 of 16
    assert g.group_miss_prob(4, 0.25) == 10 / 16


def test_any_group_miss_prob():
    assert abs(g.any_group_miss_prob(3, 3, 0.5) - (1 - (3 / 4) ** 3)) < 1e-15
    # huge m does not underflow
    assert g.any_group_miss_prob(10 ** 50, 10, 0.5) == 1.0


def test_audit_family_s1_to_zero_but_not_wise():
    m, k = g.audit_family(400)
    assert 1 / k < 0.04
    assert g.any_group_miss_prob(m, k, 0.5) > 0.999999


def test_bounded_groups_wise():
    assert g.any_group_miss_prob(3, 10 ** 5 // 3, 0.1) < 1e-100


def test_log10_group_miss_prob_agrees():
    for k in (50, 150, 200):
        q = g.group_miss_prob(k, 0.1)
        assert abs(g.log10_group_miss_prob(k, 0.1) - math.log10(q)) < 1e-9
    # scipy branch is close to the exact one just past the switch
    import math as _m
    exact = sum(_m.comb(300, j) for j in range(301) if j <= 120 or j >= 180) / 2 ** 300
    assert abs(g.log10_group_miss_prob(300, 0.1) - _m.log10(exact)) < 1e-6
