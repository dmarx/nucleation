import numpy as np
import pytest

from phi import (Phi, analyse, bipartitions, block_bipartitions, exclusion_winner,
                 group, group_levels, mind_levels, modular_mind, phi_split,
                 self_info, stationary_cov)


def test_stationary_cov_solves_lyapunov():
    rng = np.random.default_rng(0)
    A = rng.normal(size=(5, 5)) * 0.15
    S = stationary_cov(A)
    assert np.allclose(S, A @ S @ A.T + np.eye(5))


def test_unstable_rejected():
    with pytest.raises(ValueError):
        stationary_cov(np.eye(3) * 1.01)


def test_self_info_scalar_ar1():
    # x_t = a x_{t-1} + e: I = -0.5 log(1 - a^2)
    a = 0.6
    A = np.array([[a]])
    S = stationary_cov(A)
    assert np.isclose(self_info(S, A @ S, [0]), -0.5 * np.log(1 - a * a))


def test_self_info_matches_sampled_regression():
    rng = np.random.default_rng(1)
    A = rng.normal(size=(4, 4)) * 0.2
    S = stationary_cov(A)
    T = 200_000
    X = np.zeros((T, 4))
    for t in range(1, T):
        X[t] = A @ X[t - 1] + rng.normal(size=4)
    X = X[1000:]
    Y, Z = X[1:], X[:-1]
    B, *_ = np.linalg.lstsq(Z, Y, rcond=None)
    E = np.cov((Y - Z @ B).T)
    emp = 0.5 * (np.linalg.slogdet(np.cov(Y.T))[1] - np.linalg.slogdet(E)[1])
    assert abs(emp - self_info(S, A @ S, range(4))) < 0.01


def test_phi_zero_for_disconnected_parts():
    A = np.zeros((4, 4))
    A[:2, :2] = 0.3
    A[2:, 2:] = 0.3
    S = stationary_cov(A)
    assert abs(phi_split(S, A @ S, [[0, 1], [2, 3]])) < 1e-12
    val, mib = Phi(S, A @ S, [0, 1, 2, 3])
    assert abs(val) < 1e-12
    assert sorted(map(sorted, mib)) == [[0, 1], [2, 3]]


def test_bipartitions_count():
    assert len(list(bipartitions(range(5)))) == 2 ** 4 - 1
    blocks = [[0, 1], [2], [3, 4]]
    bb = list(block_bipartitions(blocks))
    assert len(bb) == 3
    for a, b in bb:
        assert sorted(a + b) == [0, 1, 2, 3, 4]


def test_models_shapes_and_symmetry():
    A, mods = modular_mind(m=3, n=3)
    assert A.shape == (9, 9) and np.allclose(A, A.T)
    G, members, gmods = group(k=3, m=3, n=3)
    assert G.shape == (27, 27) and np.allclose(G, G.T)
    assert len(members) == 3 and len(gmods) == 9
    # each member block is the mind
    assert np.allclose(G[:9, :9], A)


def test_uncoupled_mind_splits_into_modules():
    A, mods = modular_mind(c=0.0)
    r = analyse(A, mind_levels(A, mods))
    assert exclusion_winner(r) == "module"


def test_uncoupled_group_splits_into_members():
    A, members, mods = group(c=0.15, width_c=3, g=0.0)
    r = analyse(A, group_levels(members, mods))
    assert abs(max(r["group"])) < 1e-12
    assert exclusion_winner(r) == "member"


def test_main_complex_disconnected_is_a_module():
    from phi import main_complex
    A, mods = modular_mind(m=2, n=3, c=0.0)
    val, sub = main_complex(A)
    assert sub in mods


def test_main_complex_tight_mind_is_whole():
    from phi import main_complex
    A, mods = modular_mind(c=0.1, width=3)
    val, sub = main_complex(A)
    assert sub == list(range(9))


@pytest.mark.parametrize("normalize", [True, False])
@pytest.mark.parametrize("g,width", [(0.1, 3), (0.2, 1)])
def test_large_mib_is_not_beaten_by_random_cuts(normalize, g, width):
    """The group's MIB is searched along module seams and single-unit cuts;
    random cuts should not score lower."""
    from phi import large_splits
    A, members, mods = group(c=0.15, width_c=3, g=g, width_g=width)
    S = stationary_cov(A)
    Gm = A @ S
    whole = list(range(27))
    score = (lambda a, b: phi_split(S, Gm, [a, b]) / min(len(a), len(b))) if normalize \
        else (lambda a, b: phi_split(S, Gm, [a, b]))
    _, (a, b) = Phi(S, Gm, whole, large_splits(whole, mods), normalize=normalize)
    best = score(a, b)
    rng = np.random.default_rng(2)
    for _ in range(200):
        mask = rng.random(27) < rng.uniform(0.1, 0.5)
        if mask.all() or not mask.any():
            continue
        a2 = [u for u in whole if mask[u]]
        b2 = [u for u in whole if not mask[u]]
        assert score(a2, b2) >= best - 1e-12
