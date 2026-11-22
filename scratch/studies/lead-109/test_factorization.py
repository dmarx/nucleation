"""Tests for factorization.py (LEAD-109). Run: python3 -I -m pytest -q."""
import itertools
import numpy as np
import factorization as F


def _ring(n, strong, weak):
    """n regimes on a cycle: nearest-neighbour coupling `strong`, all other
    pairs `weak`."""
    M = np.full((n, n), weak, float)
    for i in range(n):
        M[i, (i + 1) % n] = M[(i + 1) % n, i] = strong
    np.fill_diagonal(M, 0.0)
    return M


def _two_clusters(weak):
    """6 regimes, blocks {0,1,2} and {3,4,5}, within=1.0, across=weak."""
    M = np.full((6, 6), weak, float)
    for b in ([0, 1, 2], [3, 4, 5]):
        for i, j in itertools.combinations(b, 2):
            M[i, j] = M[j, i] = 1.0
    np.fill_diagonal(M, 0.0)
    return M


def test_partitions_count_is_bell():
    # Bell numbers B0..B6
    bell = [1, 1, 2, 5, 15, 52, 203]
    for n in range(7):
        assert len(list(F.partitions(n))) == bell[n]


def test_refinement_and_crosscut():
    P = F.as_partition([{0, 1}, {2, 3}])
    Q = F.as_partition([{0, 1, 2, 3}])
    R = F.as_partition([{0, 2}, {1, 3}])
    assert F.is_refinement(P, Q) and not F.is_refinement(Q, P)
    assert F.comparable(P, Q) and not F.comparable(P, R)
    assert F.crosscut(P, R)


def test_gap_detects_the_block_structure():
    M = _two_clusters(weak=0.05)
    good = F.as_partition([{0, 1, 2}, {3, 4, 5}])
    # within bottleneck 1.0, across 0.05 -> gap 20
    assert abs(F.gap(M, good) - 20.0) < 1e-9
    # a crosscutting split puts a strong edge across -> gap 1.0 (fails)
    bad = F.as_partition([{0, 1, 3}, {2, 4, 5}])
    assert F.gap(M, bad) <= 1.0 + 1e-9


def test_clearing_family_is_always_a_nested_chain():
    """CORE RESULT: over many random M, every pair of test-1-clearing
    partitions is comparable (nested). No crosscutting disagreement."""
    rng = np.random.default_rng(0)
    n = 6
    for _ in range(300):
        A = rng.random((n, n))
        M = np.triu(A, 1)
        M = M + M.T
        for tau in (1.0, 1.5, 2.0, 4.0):
            fam = F.self_consistent_family(M, n, tau)
            assert F.is_chain(fam), "found a crosscutting tie!"
            if fam:
                assert F.finest(fam) is not None


def test_clearing_partitions_are_dendrogram_cuts():
    """Every clearing partition is a single-linkage cut (so they nest)."""
    rng = np.random.default_rng(1)
    n = 6
    for _ in range(200):
        A = rng.random((n, n))
        M = np.triu(A, 1)
        M = M + M.T
        cuts = set(F.dendrogram_cuts(M, n))
        for tau in (1.2, 2.0, 3.0):
            for P in F.self_consistent_family(M, n, tau):
                assert P in cuts


def test_crosscutting_tie_is_impossible_even_under_exact_symmetry():
    """A symmetric '4-cycle' where the two pairings {01,23} and {12,30}
    are related by a rotation. At most one can clear tau>1; they never
    both clear. Demonstrates uniqueness survives exact symmetry."""
    for s, w in [(1.0, 0.3), (1.0, 0.9), (0.8, 0.2)]:
        M = _ring(4, strong=s, weak=w)
        A = F.as_partition([{0, 1}, {2, 3}])
        B = F.as_partition([{1, 2}, {3, 0}])
        for tau in (1.01, 1.5, 2.0):
            cA, cB = F.clears_test1(M, A, tau), F.clears_test1(M, B, tau)
            assert not (cA and cB)  # never a crosscutting tie
        # In fact on the uniform 4-ring neither pairing clears (each pair
        # straddles a strong edge): gap == 1.
        assert abs(F.gap(M, A) - (s / s)) < 1e-9
        assert abs(F.gap(M, B) - (s / s)) < 1e-9


def test_grain_multiplicity_is_real():
    """A two-level (watchmaker) hierarchy has MORE THAN ONE clearing grain:
    the fine partition into sub-blocks AND the coarse partition into the
    two super-blocks both clear. Genuine non-uniqueness across grain."""
    # 4 regimes: tight pairs {0,1},{2,3} (w=1.0) bound into one super-block
    # by a medium bridge (0.3); everything else weak (0.02).
    M = np.full((4, 4), 0.02, float)
    M[0, 1] = M[1, 0] = 1.0
    M[2, 3] = M[3, 2] = 1.0
    M[1, 2] = M[2, 1] = 0.3  # bridge between the pairs
    np.fill_diagonal(M, 0.0)
    fine = F.as_partition([{0, 1}, {2, 3}])
    coarse = F.as_partition([{0, 1, 2, 3}])
    singletons = F.as_partition([{0}, {1}, {2}, {3}])
    tau = 2.0
    assert F.clears_test1(M, fine, tau)     # gap 1.0/0.3 ~ 3.3 > 2
    assert F.clears_test1(M, coarse, tau)   # nothing cut -> inf
    fam = F.self_consistent_family(M, 4, tau)  # test 1 only
    assert fine in fam and coarse in fam    # two self-consistent grains
    assert F.crosscut(fine, coarse) is False  # but nested, not crosscut
    # under test 1 alone a lone regime is trivially one system, so the
    # finest member is all-singletons; the agent tests (test2) decide
    # whether a lone regime earns agenthood.
    assert F.finest(fam) == singletons


def test_test2_only_prunes_the_chain():
    """Adding the CLAIM-154 goal-vs-device gate removes grains but never
    creates a crosscut, and can leave a unique agent factorization."""
    M = np.full((4, 4), 0.02, float)
    M[0, 1] = M[1, 0] = 1.0
    M[2, 3] = M[3, 2] = 1.0
    M[1, 2] = M[2, 1] = 0.3
    np.fill_diagonal(M, 0.0)
    tau = 2.0
    # Lone regimes read as devices (fail test 2); the two tight pairs read
    # as agents; the coarse super-block also reads as a mere device.
    test2 = {
        frozenset({0, 1}): (9.0, 2.0),      # d'^2=9 > Occam=2 -> agent
        frozenset({2, 3}): (9.0, 2.0),      # agent
        frozenset({0, 1, 2, 3}): (1.0, 4.0),  # device, pruned
        # every singleton defaults to a device (absent) -> pruned
    }
    fam = F.self_consistent_family(M, 4, tau, test2=test2)
    assert F.is_chain(fam)
    fine = F.as_partition([{0, 1}, {2, 3}])
    coarse = F.as_partition([{0, 1, 2, 3}])
    singletons = F.as_partition([{0}, {1}, {2}, {3}])
    assert fine in fam
    assert coarse not in fam        # pruned by test 2
    assert singletons not in fam    # lone regimes are devices, not agents
    # with the agent tests gating every block, the unique factorization
    # into agents here is the fine one.
    assert F.finest(fam) == fine
    assert len(fam) == 1


def test_grain_non_uniqueness_with_full_agent_tests():
    """DEMONSTRATION of two distinct self-consistent factorizations INTO
    AGENTS of one fixed level (M) and target. The fine partition (two
    agents) and the coarse partition (one agent) are BOTH valid: every
    block of each is an agent. They disagree on how many agents there are
    and which regimes each governs. They are nested (not crosscut), so the
    only thing choosing between them is the grain, which the level/target
    as stated does not fix (CLAIM-170's two 'levels'; CLAIM-174's Kenton
    actor-critic vs one-agent graph)."""
    M = np.full((4, 4), 0.02, float)
    M[0, 1] = M[1, 0] = 1.0
    M[2, 3] = M[3, 2] = 1.0
    M[1, 2] = M[2, 1] = 0.3
    np.fill_diagonal(M, 0.0)
    tau = 2.0
    test2 = {
        frozenset({0, 1}): (9.0, 2.0),          # agent
        frozenset({2, 3}): (9.0, 2.0),          # agent
        frozenset({0, 1, 2, 3}): (16.0, 3.0),   # ALSO an agent at its grain
    }
    fam = F.self_consistent_family(M, 4, tau, test2=test2)
    fine = F.as_partition([{0, 1}, {2, 3}])
    coarse = F.as_partition([{0, 1, 2, 3}])
    assert fine in fam and coarse in fam
    assert len(fam) == 2                       # two factorizations into agents
    assert F.is_chain(fam)                     # nested, never crosscutting
    assert F.crosscut(fine, coarse) is False


def test_reify_rule():
    assert F.reify(9.0, 2.0) is True
    assert F.reify(1.0, 4.0) is False
