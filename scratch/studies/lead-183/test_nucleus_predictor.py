import random

import pytest

import nucleus_predictor as npred


def chain(n, rigid_flags, q=3, target=None):
    """A path 0-1-...-(n-1); rigid edges copy the state, ambiguous edges allow
    the target pair plus (t_u, other) for every other state."""
    target = target or [0] * n
    edges = [(i, i + 1) for i in range(n - 1)]
    rel = {}
    for (u, v), rigid in zip(edges, rigid_flags):
        if rigid:
            allowed = {(a, a) for a in range(q)}
        else:
            allowed = {(target[u], b) for b in range(q)} | {(a, target[v]) for a in range(q)}
        rel[(u, v)] = allowed
        rel[(v, u)] = {(b, a) for a, b in allowed}
    return npred.Architecture(n, edges, q, rel, target)


def test_island_is_rigid_cluster():
    arch = chain(6, [True, True, False, True, True])
    assert npred.island(arch, [0]) == {0, 1, 2}
    assert npred.island(arch, [4]) == {3, 4, 5}
    assert npred.island(arch, [0, 5]) == set(range(6))


def test_vic_can_decrease_and_monotone_baselines_cannot():
    # rigid 0..4 (island of 0), then ambiguous edges 4-5, 5-6, 6-7
    arch = chain(8, [True, True, True, True, False, False, False])
    p = npred.Predictors(arch)
    assert p.vic([0]) == pytest.approx(5 / 8)
    # a seed inside 0's island changes nothing
    assert p.vic([0, 3]) == pytest.approx(5 / 8)
    # seed 6 (island {6}): 0,1,2 stay with 0; 3 is a tie (half); 4,5,7 go
    # to 6 and are not in its island; 6 counts -> 4.5/8
    assert p.vic([0, 6]) == pytest.approx(4.5 / 8)
    assert p.vic([0, 6]) < p.vic([0])
    for name in npred.MONOTONE:
        f = getattr(p, name)
        assert f([0, 6]) >= f([0])


def test_vic_decrease_inside_and_outside():
    # rigid 0..6, ambiguous 6-7, 7-8
    arch = chain(9, [True] * 6 + [False, False])
    p = npred.Predictors(arch)
    assert p.vic([0]) == pytest.approx(7 / 9)
    # a second large-island seed at 6 shares the island: no change
    assert p.vic([0, 6]) == pytest.approx(7 / 9)
    # a small-island seed at 8 takes 5, 6, 7 and a half of 4
    assert p.vic([0, 8]) == pytest.approx(5.5 / 9)
    # adding 6 to {0, 8} restores 4..6 to a large island
    assert p.vic([0, 6, 8]) > p.vic([0, 8])


def test_icn_counts_components():
    arch = chain(6, [True, False, False, False, True])
    p = npred.Predictors(arch)
    assert p.icn([0]) == pytest.approx((2 / 6) / 1)
    assert p.icn([0, 5]) == pytest.approx((4 / 6) / 2)


def test_simulation_rigid_chain_always_succeeds():
    arch = chain(6, [True] * 5)
    rng = random.Random(1)
    assert npred.estimate_V(arch, [0], 0.0, 50, rng) == 1.0


def test_simulation_ambiguous_edge_half():
    # 0 - 1 ambiguous with q=2: from 0 at target, 1 has two compatible states
    arch = chain(2, [False], q=2)
    rng = random.Random(2)
    v = npred.estimate_V(arch, [0], 0.0, 4000, rng)
    assert abs(v - 0.5) < 0.04


def test_simulation_context_resolves_ambiguity():
    # triangle-free check: component 1 between two seeds 0 and 2, each edge
    # ambiguous but with different distractors -> only target compatible
    target = [0, 0, 0]
    edges = [(0, 1), (1, 2)]
    rel = {}
    r01 = {(0, 0), (0, 1)}
    r12 = {(0, 0), (2, 0)}  # (v1, v2): v1 in {0, 2} given v2 = 0
    for (u, v), al in zip(edges, [r01, r12]):
        rel[(u, v)] = al
        rel[(v, u)] = {(b, a) for a, b in al}
    arch = npred.Architecture(3, edges, 3, rel, target)
    rng = random.Random(3)
    assert npred.estimate_V(arch, [0, 2], 0.0, 200, rng) == 1.0
    assert npred.island(arch, [0, 2]) == {0, 1, 2}
    # arc consistency is static: 1's relation with the unset 2 already rules
    # out state 1, so under the pre-registered island seed 0 alone forces
    # everything ...
    assert npred.island_ac(arch, [0]) == {0, 1, 2}
    # ... the amended forward island does not ...
    assert npred.island_forward(arch, [0]) == {0}
    # ... and the myopic growth, seeing only set neighbours, errs half the
    # time: a known gap between the island and the dynamics
    v = npred.estimate_V(arch, [0], 0.0, 4000, random.Random(4))
    assert abs(v - 0.5) < 0.04


def test_lattice_target_satisfies_relations():
    arch = npred.lattice_architecture(5, 4, 0.5, 2, random.Random(0))
    for u, v in arch.edges:
        assert (arch.target[u], arch.target[v]) in arch.allowed(u, v)
        assert (arch.target[v], arch.target[u]) in arch.allowed(v, u)
    # the whole target is the island of all components
    assert npred.island(arch, list(range(arch.n))) == set(range(arch.n))


def test_metrics():
    assert npred.spearman([1, 2, 3], [2, 4, 9]) == pytest.approx(1.0)
    assert npred.auc([2, 3], [0, 1]) == 1.0
    assert npred.auc([0], [0]) == 0.5


def test_two_sided_ambiguity_never_forces_from_target():
    import random as r
    arch = npred.lattice_architecture(6, 4, 0.0, 2, r.Random(5))
    for s in range(arch.n):
        assert npred.island_forward(arch, [s]) == {s}
