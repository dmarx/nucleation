"""scratch/formal/inquiry_coupling_bounds_check.py

Rebuilds the checks of CLAIM-1157 (boundedness does not make asking and
answering compete; a common budget, bottleneck or sequential dependence
supplies the coupling; a shared deadline is not a shared pool of hours) and
CLAIM-1025 (the joint frontier lies between an inner and an outer bound that
the separate frontiers give, and is not a function of them), from the
entries' text alone. The filers' scripts were not kept. Written at the
reruns of 2026-11-25 by a session other than the claims' filer.
Run: python3 -I this file. Standard library only.

Schedules. A question q is posed by some route r, taking T_Q time and C_Q
cost, and then answered, taking T_A and C_A (which may depend on r). The
answer may start after a lead of s days of posing (0 <= s <= T_Q; s = T_Q
is waiting for the finished question). If one expert does both, the two run
one after the other. Finish = T_Q + T_A with one expert, else
max(T_Q, s + T_A). Cost = C_Q + C_A from one pooled budget.
"""
import itertools
import random


# ---------------------------------------------------------------- CLAIM-1157

def feasible_answer_spends(x_q, arch, B=10, BQ=5, BA=5, grid=range(0, 11)):
    """The answer's feasible spends given the query's spend x_q."""
    if arch == "separate":                    # C_Q <= B_Q and C_A <= B_A
        return {x for x in grid if x_q <= BQ and x <= BA}
    if arch == "shared":                      # C_Q + C_A <= B
        return {x for x in grid if x_q + x <= B}
    if arch == "sequential":                  # T_Q + T_A <= H, separate staff
        return {x for x in grid if x_q + x <= B}
    if arch == "bottleneck":                  # concurrent, one server of rate 1
        return {x for x in grid if max(x_q, x) <= B and x_q + x <= B}
    raise ValueError(arch)


def check_1157():
    # Separate pools, no dependence: the feasible set is a product, so more
    # spending on asking leaves answering's feasible set unchanged.
    sets = [feasible_answer_spends(xq, "separate") for xq in range(0, 6)]
    assert all(s == sets[0] for s in sets)
    prod = {(a, b) for a in range(11) for b in range(11) if a <= 5 and b <= 5}
    assert {(a, b) for a in range(11) for b in feasible_answer_spends(a, "separate")} == prod
    # Each coupling makes it shrink.
    for arch in ("shared", "sequential", "bottleneck"):
        sizes = [len(feasible_answer_spends(xq, arch)) for xq in range(0, 6)]
        assert all(b < a for a, b in zip(sizes, sizes[1:])), (arch, sizes)
    # The deadline: two independent five-minute activities in one interval.
    assert max(5, 5) == 5 and 5 + 5 == 10
    # Shared deadline with separate staff and no precedence: no competition.
    H = 5
    ok = {(a, b) for a in range(11) for b in range(11) if max(a, b) <= H}
    assert all(((a, b) in ok) == (a <= H and b <= H) for a in range(11) for b in range(11))
    print("1157: separate pools give a product (answer's set unchanged as asking spends 0..5);"
          " a shared budget, a sequential dependence and a shared server each shrink it;"
          " two 5-minute activities in parallel take 5 minutes, not 10")


def control_1157():
    """Negative control: the test detects coupling when it is planted into
    'separate' pools by a hidden transfer (asking spends from answering's)."""
    def leaky(x_q):
        return {x for x in range(11) if x_q <= 5 and x <= 5 - max(0, x_q - 3)}
    sets = [leaky(xq) for xq in range(0, 6)]
    assert not all(s == sets[0] for s in sets)
    print("1157 control: a planted transfer between the pools is detected as coupling")


# ---------------------------------------------------------------- CLAIM-1025

def finish(TQ, TA, s, one_expert):
    return TQ + TA if one_expert else max(TQ, s + TA)


def check_examples():
    H = 4
    # posing alone 3 <= 4, answering alone 3 <= 4: same separate frontiers
    assert 3 <= H and 3 <= H
    X = finish(3, 3, 1, False)
    Y = finish(3, 3, 3, False)
    Z = finish(3, 3, 0, True)
    assert (X, Y, Z) == (4, 6, 6)
    assert (X <= H, Y <= H, Z <= H) == (True, False, False)
    # sharing preliminary work, for a set of two questions
    assert 3 + 3 - 2 == 4
    print("1025 examples: H = 4, X finishes at 4 (feasible), Y and Z at 6 (not);"
          " the separate frontiers agree; shared preliminary work: 4, not 6")


def random_org(rng, nq=4):
    org = {}
    for q in range(nq):
        routes = []
        for _ in range(rng.randint(1, 3)):
            TQ, CQ = rng.randint(0, 5), rng.randint(0, 5)
            TA, CA = rng.randint(0, 5), rng.randint(0, 5)
            s = rng.randint(0, TQ)
            routes.append((TQ, CQ, TA, CA, s))
        org[q] = routes
    return org, rng.random() < 0.5


def sets_for(org, one_expert, H, B):
    FQ = {q for q, rs in org.items() if any(TQ <= H and CQ <= B for TQ, CQ, *_ in rs)}
    FA = {q for q, rs in org.items() if any(TA <= H and CA <= B for _, _, TA, CA, _ in rs)}
    J = {q for q, rs in org.items()
         if any(finish(TQ, TA, s, one_expert) <= H and CQ + CA <= B
                for TQ, CQ, TA, CA, s in rs)}
    inner_route = {q for q, rs in org.items()
                   if any(TQ + TA <= H and CQ + CA <= B for TQ, CQ, TA, CA, _ in rs)}
    return FQ, FA, J, inner_route


def check_bounds():
    rng = random.Random(1025)
    n = 0
    for _ in range(4000):
        org, one = random_org(rng)
        for H, B in itertools.product(range(0, 11), range(0, 11)):
            FQ, FA, J, inner = sets_for(org, one, H, B)
            assert J <= FQ & FA, "outer bound broken"
            assert inner <= J, "inner bound broken"
            n += 1
    print(f"1025 bounds: inner (one route run sequentially) <= J <= F_Q & F_A on {n} (organization, H, B) cases")


def check_least_cost_inner():
    """The inner bound read off the frontiers (least posing cost plus least
    answering cost, possibly of different routes) fails where posing changes
    answering's cost: CLAIM-1115's construction 4, least costs 2 + 3 = 5,
    true joint cost 9."""
    routes = [(0, 2, 0, 9, 0), (0, 6, 0, 3, 0)]
    least = min(r[1] for r in routes) + min(r[3] for r in routes)
    true = min(r[1] + r[3] for r in routes)
    assert (least, true) == (5, 9)
    for B in (5, 8):
        assert least <= B < true
    print("1025 qualification: least costs say 5, true joint cost 9; at B = 5 and 8 the frontier-read inner bound is wrong")


def control_least_cost_inner():
    """Negative control: answering's cost independent of the posing route,
    so the frontier-read inner bound is exact."""
    routes = [(0, 2, 0, 3, 0), (0, 6, 0, 3, 0)]
    least = min(r[1] for r in routes) + min(r[3] for r in routes)
    true = min(r[1] + r[3] for r in routes)
    assert least == true == 5
    print("1025 control: route-independent answering cost, frontier-read inner bound exact (5 = 5)")


def control_outer():
    """Negative control: allow the answer to start before posing begins
    (a negative lead), which is not a schedule; the outer-bound test then
    catches a joint 'success' outside F_A."""
    TQ, TA, s, H = 1, 5, -2, 4
    J = finish(TQ, TA, s, False) <= H
    FA = TA <= H
    assert J and not FA
    print("1025 control: with an inadmissible negative lead the outer-bound test fires")


def check_not_function():
    """Same (F_Q, F_A) at every horizon and budget, different J: X and Y."""
    X = {0: [(3, 0, 3, 0, 1)]}
    Y = {0: [(3, 0, 3, 0, 3)]}
    differ = False
    for H, B in itertools.product(range(0, 10), range(0, 3)):
        fx, fy = sets_for(X, False, H, B), sets_for(Y, False, H, B)
        assert fx[:2] == fy[:2]
        differ |= fx[2] != fy[2]
    assert differ
    # downward closure for sets of questions with additive shared costs
    cost = {frozenset(): 0, frozenset("a"): 3, frozenset("b"): 3, frozenset("ab"): 4}
    for S, c in cost.items():
        assert all(cost[T] <= c for T in cost if T <= S)
    print("1025: X and Y share F_Q and F_A at every H in 0..9 and B in 0..2, and differ in J;"
          " the shared-work cost is monotone, so the joint sets are downward closed")


def main():
    check_1157()
    control_1157()
    check_examples()
    check_bounds()
    check_least_cost_inner()
    control_least_cost_inner()
    control_outer()
    check_not_function()
    print("checks pass")


if __name__ == "__main__":
    main()
