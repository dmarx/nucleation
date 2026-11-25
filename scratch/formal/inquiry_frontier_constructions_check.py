"""scratch/formal/inquiry_frontier_constructions_check.py

Reconstructs and checks the four constructions of CLAIM-1115 (the filer's
script of 2026-11-23 was not kept), plus its check on A58's two relations.
Written at the status pass of 2026-11-24 by a session other than the
claim's filer, from the entry's text alone. Run: python3 -I this file.

Notation as in the entry: c_Q(q) the least cost of formulating q; c_A(q, a)
the least cost of producing and evaluating a with q supplied;
Q_ask(B) = {q : c_Q(q) <= B}; A_cond(B) = {(q, a) : c_A(q, a) <= B}.
A system is given by its formulation routes: for each (q, a), a list of
(cost of formulating by this route, cost of answering after it).
"""

SEQ = lambda x, y: x + y      # sequential spending
PAR = lambda x, y: max(x, y)  # in parallel, against a horizon


def least_costs(routes):
    cq = {q: min(f for f, _ in rs) for (q, _), rs in routes.items()}
    ca = {qa: min(g for _, g in rs) for qa, rs in routes.items()}
    return cq, ca


def frontiers(routes, B):
    cq, ca = least_costs(routes)
    return ({q for q, c in cq.items() if c <= B},
            {qa for qa, c in ca.items() if c <= B})


def joint_true(routes, B, rule=SEQ):
    """Pairs attainable together: some route's composed cost within B."""
    return {qa for qa, rs in routes.items() if min(rule(f, g) for f, g in rs) <= B}


def joint_from_families(routes, budgets, B, rule=SEQ):
    """Recover least costs as the least budget at which each item appears in
    the families Q_ask(.) and A_cond(.), then compose them by the rule."""
    fam = {b: frontiers(routes, b) for b in budgets}
    cq = {q: min(b for b in budgets if q in fam[b][0]) for (q, _) in routes}
    ca = {qa: min(b for b in budgets if qa in fam[b][1]) for qa in routes}
    return {(q, a) for (q, a) in routes if rule(cq[q], ca[(q, a)]) <= B}


QA = ("q", "a")
S1 = {QA: [(10, 10)]}
S2 = {QA: [(2, 10)]}


def construction_1():
    B = 12
    assert frontiers(S1, B) == frontiers(S2, B) == ({"q"}, {QA})
    assert joint_true(S1, B) == set() and joint_true(S2, B) == {QA}
    print("1. at B = 12 the frontiers agree; joint pairs:",
          sorted(joint_true(S1, B)), "against", sorted(joint_true(S2, B)))


def construction_2():
    budgets = range(40)
    for s in (S1, S2):
        for B in budgets:
            assert joint_from_families(s, budgets, B) == joint_true(s, B)
    # the families do distinguish S1 and S2 (at B = 2 to 9)
    assert any(frontiers(S1, B) != frontiers(S2, B) for B in budgets)
    print("2. recovered joint sets equal the true ones at every B in 0..39")


def construction_3():
    s = {QA: [(6, 6)]}
    H = 10
    assert joint_true(s, H, SEQ) == set()
    assert joint_true(s, H, PAR) == {QA}
    # same frontiers, different rule: the frontiers do not carry the rule
    print("3. c_Q = c_A = 6, horizon 10: sequential", sorted(joint_true(s, H, SEQ)),
          "parallel", sorted(joint_true(s, H, PAR)))


def construction_4():
    s = {QA: [(2, 9), (6, 3)]}
    cq, ca = least_costs(s)
    assert (cq["q"], ca[QA]) == (2, 3)
    assert min(f + g for f, g in s[QA]) == 9
    for B, least_says, truth in [(5, True, False), (8, True, False),
                                 (9, True, True), (11, True, True)]:
        assert (QA in joint_from_families(s, range(40), B)) == least_says
        assert (QA in joint_true(s, B)) == truth
    print("4. least costs 2 + 3 = 5, true joint cost 9; they disagree at B = 5 and 8,"
          " agree at 9 and 11")


def control_no_coupling():
    """Negative control: where the cost of answering does not depend on the
    route of formulation, least costs give the joint set at every budget."""
    s = {QA: [(2, 3), (6, 3)], ("q", "b"): [(2, 7), (6, 7)]}
    for B in range(40):
        assert joint_from_families(s, range(40), B) == joint_true(s, B)
    print("control: no coupling, least costs exact at every B in 0..39")


def a58_relations():
    F1 = {("q1", "a1"), ("q2", "a2")}
    F2 = {("q1", "a2"), ("q2", "a1")}
    proj = lambda F, i: {p[i] for p in F}
    assert proj(F1, 0) == proj(F2, 0) and proj(F1, 1) == proj(F2, 1)
    indexed = lambda F: {q: {a for (qq, a) in F if qq == q} for q in proj(F, 0)}
    assert indexed(F1) != indexed(F2)
    print("A58: equal projections, indexed answer frontiers differ:",
          indexed(F1), indexed(F2))


def main():
    construction_1()
    construction_2()
    construction_3()
    construction_4()
    control_no_coupling()
    a58_relations()
    print("checks pass")


if __name__ == "__main__":
    main()
