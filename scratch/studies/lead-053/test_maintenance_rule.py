import math

import maintenance_rule as m


def test_kernel_simple_line():
    # states 0..5, move left or stay; K = {x >= 2}: every state of K can stay.
    states = list(range(6))
    succ = lambda x: [max(x - 1, 0), x]
    assert m.viability_kernel(states, lambda x: x >= 2, succ) == {2, 3, 4, 5}
    # forced drift left: nothing in K is viable.
    succ2 = lambda x: [max(x - 1, 0)]
    assert m.viability_kernel(states, lambda x: x >= 2, succ2) == set()


def test_northstar_dependence_rule_detects_loss():
    rows = m.northstar_report(True)
    # the operative regime and its governance hold throughout
    assert all(r["emergency"] and r["criteria_met"] for r in rows)
    # the stipulated standard sees nothing
    assert all(r["in_kernel_stip"] for r in rows)
    # the dependence rule's kernel is left, and never re-entered
    flags = [r["in_kernel_dep"] for r in rows]
    assert flags[0] and not flags[-1]
    first_out = flags.index(False)
    assert not any(flags[first_out:])


def test_northstar_control_keeps_capacity():
    rows = m.northstar_report(False)
    assert all(r["in_kernel_dep"] for r in rows)
    assert not rows[-1]["emergency"]


def test_kernel_inside_K():
    states = m.northstar_states()
    kern = m.viability_kernel(states, m.K_dependence, m.northstar_successors(True))
    assert all(m.K_dependence(x) for x in kern)
    # In this toy K equals its kernel: from every state of K the lift is
    # permitted, so the capacity is exercisable wherever it is held. What
    # the operative policy loses is K itself, not a margin inside it.
    K = {x for x in states if m.K_dependence(x)}
    assert kern == K


def test_case111_branches_match_case():
    bm, bp = m.case111_branches(-0.2, 1.0)
    assert abs(bp - 0.724) < 1e-3 and abs(bm - 0.276) < 1e-3
    bm, bp = m.case111_branches(-0.15, 1.0)
    assert abs(bp - 0.816) < 1e-3 and abs(bm - 0.184) < 1e-3


def test_case111_kernel_edge_by_simulation():
    mu, kappa, b_f = -0.2, 1.0, 0.1
    edge = m.case111_kernel_lower_edge(mu, kappa, b_f)
    assert m.case111_simulate(edge + 0.01, mu, kappa) > 0.7
    assert m.case111_simulate(edge - 0.01, mu, kappa) < b_f


def test_case112_mu_c_inverts_hc():
    for h in (0.05, 0.1, 0.3):
        assert abs(m.case112_hc(m.case112_mu_c(h)) - h) < 1e-12


def test_case227_levels_and_crossing():
    cm, cp = m.case227_levels()
    assert abs(cm - 0.64174) < 1e-5 and abs(cp - 1.55826) < 1e-5
    assert m.case227_rate(0.6) < 0
    assert abs(m.case227_time_to_half() - 2.88) < 0.01
    # an outside supply of 0.02 reverses the sign at 0.6
    assert m.case227_rate(0.6, u=0.02) > 0
