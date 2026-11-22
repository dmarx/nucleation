import numpy as np

import measure as m


def test_cooc_counts_symmetric_window():
    ids = np.array([0, 1, 2, 0, 1])
    n = m.cooc(ids, 3, 3, 1)
    # pairs at distance 1: (0,1),(1,2),(2,0),(0,1) both directions
    assert n[0, 1] == 2 and n[1, 0] == 2 and n[1, 2] == 1 and n[2, 0] == 1 and n[0, 0] == 0
    assert (n == n.T).all()


def test_interaction_zero_when_additive():
    rng = np.random.default_rng(0)
    x, xp, y, yp = (rng.normal(size=50) for _ in range(4))
    rel, pair, inter = m.interaction_fraction(x + y, x + yp, xp + y, xp + yp)
    assert np.isclose(inter, 0) and rel > 0 and pair > 0
    Pa, Pb, Pc, Pd = (rng.normal(size=50) for _ in range(4))
    rel, pair, inter = m.interaction_fraction(Pa, Pb, Pc, Pd)
    tot = sum(((P - (Pa + Pb + Pc + Pd) / 4) ** 2).sum() for P in (Pa, Pb, Pc, Pd))
    assert np.isclose(rel + pair + inter, tot)


def test_cv_r2_recovers_additive_signal():
    rng = np.random.default_rng(1)
    X = (rng.random((400, 10)) < 0.3).astype(float)
    Y = X @ rng.normal(size=(10, 30))
    assert m.cv_r2(X, m.double_center(Y) + 0 * Y) > 0.99 or m.cv_r2(X, Y - Y.mean(0)) > 0.99
    assert m.cv_r2(X[rng.permutation(400)], Y - Y.mean(0)) < 0.1
