import numpy as np
import pytest

import gridagents as ga


@pytest.fixture(scope="module")
def world():
    rng = np.random.default_rng(0)
    m = ga.make_maze(5, 5, 4, rng)
    trans = ga.random_walk(m.T, 20_000, rng)
    agents = {}
    for cls in ga.AGENTS:
        ag = cls(m.S)
        ag.train(trans)
        agents[cls.name] = ag
    return m, trans, agents, ga.all_pairs_dist(m.T)


def test_maze_connected_and_symmetric():
    m = ga.make_maze(6, 6, 5, np.random.default_rng(1))
    d = ga.all_pairs_dist(m.T)
    assert np.isfinite(d).all()
    for s in range(m.S):
        for a in range(ga.A):
            t = m.T[s, a]
            if t != s:
                assert m.T[t, ga.OPP[a]] == s
    # a perfect maze has S-1 passages; extra walls removed add loops
    assert len(m.passages()) == m.S - 1 + 5


def test_corridor_dist_and_rollout():
    m = ga.Maze(1, 3, np.repeat(np.arange(3)[:, None], 4, axis=1))
    m.open(0, 1)
    m.open(1, 1)
    d = ga.all_pairs_dist(m.T)
    assert d[0, 2] == 2 and d[2, 0] == 2
    pl = ga.Planner(3)
    pl.Th = m.T.copy()
    succ, excess, _ = ga.competence(m.T, pl.values(), d)
    assert succ == 1.0 and excess == 1.0


def test_all_agents_fully_competent_on_full_data(world):
    m, _, agents, d = world
    for name, ag in agents.items():
        succ, excess, _ = ga.competence(m.T, ag.values(), d)
        assert succ == 1.0, name
        if name in ("M", "P"):
            assert excess == pytest.approx(1.0)


def test_policy_and_planner_identical_policies(world):
    m, trans, agents, _ = world
    assert np.array_equal(ga.greedy(agents["M"].values()), ga.greedy(agents["P"].values()))
    # also on partial data
    M, P = ga.Planner(m.S), ga.Policy(m.S)
    M.train(trans[:60]); P.train(trans[:60])
    vm, vp = M.values(), P.values()
    reach = (vm.max(axis=1) > 0) & ~np.eye(m.S, dtype=bool)  # at g itself the agent is done
    assert np.array_equal(ga.greedy(vm)[reach], ga.greedy(vp)[reach])


def test_same_data_gives_same_success(world):
    m, trans, _, d = world
    for n in (40, 120, 400):
        succ = []
        for cls in ga.AGENTS:
            ag = cls(m.S)
            ag.train(trans[:n])
            succ.append(ga.competence(m.T, ag.values(), d)[0])
        assert succ[0] == succ[1] == succ[2], (n, succ)


def test_demons_converge_to_true_occupancy(world):
    m, _, agents, _ = world
    true = ga.occupancy(m.T)
    np.testing.assert_allclose(agents["D"].occupancy(), true, rtol=1e-9)


def test_readouts_exact_at_full_data(world):
    m, _, agents, _ = world
    for name, ag in agents.items():
        assert np.array_equal(ag.model(), m.T), name
    D = agents["D"]
    assert D.readout(3, 1) == m.T[3, 1]


def test_woodbury_matches_recompute(world):
    m, _, agents, _ = world
    s, d = m.passages()[2]
    t = m.T[s, d]
    m2 = m.copy()
    m2.block(s, d)
    np.testing.assert_allclose(agents["D"].occupancy_after_block(s, d, t), ga.occupancy(m2.T),
                               rtol=1e-8, atol=1e-14)


def test_planner_edit_replans(world):
    m, trans, _, _ = world
    # find a passage whose blocking keeps the maze connected
    for s, dd in m.passages():
        m2 = m.copy()
        m2.block(s, dd)
        d2 = ga.all_pairs_dist(m2.T)
        if np.isfinite(d2).all():
            break
    pl = ga.Planner(m.S)
    pl.train(trans)
    t = m.T[s, dd]
    pl.local_edit_block(s, dd)
    pl.local_edit_block(t, ga.OPP[dd])
    succ, excess, _ = ga.competence(m2.T, pl.values(), d2)
    assert succ == 1.0 and excess == pytest.approx(1.0)


def test_policy_value_reads_distance(world):
    m, _, agents, d = world
    Q = agents["P"].Q
    V = Q.max(axis=1)
    x, g = 0, m.S - 1
    assert 1 + np.log(V[x, g]) / np.log(ga.GAMMA_P) == pytest.approx(d[x, g])


def test_error_signals(world):
    m, _, agents, _ = world
    s, a = m.passages()[0]
    for ag in agents.values():
        assert not ag.error(s, a, m.T[s, a])
        assert ag.error(s, a, s)
