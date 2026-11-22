import numpy as np

import partitions as Pt


def test_wall_mask_and_positions():
    phi = np.array([[1.0, 1.0, -1.0, -1.0, 1.0]])
    h = phi[..., None] * np.array([0.6, 0.8])
    assert Pt.wall_mask(h).tolist() == [[False, True, True, True, True]]
    assert Pt.wall_positions(h) == [[2, 4]]
    assert Pt.wall_positions(h, lo=3) == [[4]]


def test_field_follows_a_rotating_direction():
    T, B, n = 6, 3, 5
    sg = np.sign(np.arange(n) - 2.5)
    hs = np.zeros((T, B, n, 2))
    for t in range(T):
        ang = 0.4 * t
        hs[t] = sg[None, :, None] * np.array([np.cos(ang), np.sin(ang)])
    phi = Pt.field(hs)
    assert np.allclose(np.abs(phi), 1.0)
    assert np.all(np.sign(phi[1:]) == np.sign(phi[1]))


def test_near_tolerance():
    a = np.array([[True, False, False, False]])
    b = np.array([[False, True, False, False]])
    assert Pt.near(a, b, 1) == 1.0
    b2 = np.array([[False, False, True, False]])
    assert Pt.near(a, b2, 1) == 0.0


def test_te_copy_process_positive_and_independent_near_zero():
    rng = np.random.default_rng(0)
    T, B, n = 40, 200, 6
    D = rng.choice([0, 2], size=(T + 1, B, n))
    phase = np.zeros(T + 1, dtype=np.int64)
    _, te_ind = Pt.local_te(D, phase)
    assert abs(te_ind.mean()) < 0.05
    C = D.copy()
    for t in range(T):
        C[t + 1, :, 1:] = C[t, :, :-1]  # each site copies its left neighbour
    _, te_copy = Pt.local_te(C, phase)
    # sites 1..n-1 receive one full bit from the left
    assert te_copy[5:, :, 2:].mean() > 0.9


def test_uniform_field_is_all_domain():
    T, B, n = 10, 50, 8
    D = np.full((T + 1, B, n), 2, dtype=np.int64)
    D[:, ::2] = 0
    phase = np.zeros(T + 1, dtype=np.int64)
    ts, structure, info = Pt.causal_state_structure(D, phase)
    # interior sites (away from the ghost-padded ends) are domain
    assert not structure[:, :, 2:-2].any()
    assert info["n_causal_states"] >= 1


def test_static_wall_is_structure():
    T, B, n = 10, 50, 10
    D = np.full((T + 1, B, n), 2, dtype=np.int64)
    D[:, :, 5:] = 0
    phase = np.zeros(T + 1, dtype=np.int64)
    ts, structure, _ = Pt.causal_state_structure(D, phase)
    assert structure[:, :, 3:7].all()
    # a future cone of radius 2 reaches the wall from sites 3..6 only
    assert not structure[:, :, 2].any()
    assert not structure[:, :, 7].any()


def test_temporally_alternating_domain_is_domain():
    T, B, n = 10, 50, 8
    D = np.full((T + 1, B, n), 2, dtype=np.int64)
    D[::2] = 0
    phase = np.zeros(T + 1, dtype=np.int64)
    ts, structure, _ = Pt.causal_state_structure(D, phase)
    assert not structure[:, :, 2:-2].any()
