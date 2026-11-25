"""scratch/formal/reserve_redesign_scope_check.py

Checks CLAIM-1180 (a reserve keeps every transition whose threshold is at most
the budget; a redesign lowers only the thresholds whose least-peak path can use
the redesigned route; so trading the reserve theta - h for theta' - h loses
exactly the other transitions with threshold in (theta', theta] whose
least-peak path does not use the redesign), as narrowed at the status pass of
2026-11-24. Written by a session other than the claim's filer, from the
derivation and the check in the entry; the entry's own check was not kept.

One capacity usable at every configuration. A configuration has a holding cost;
a path's peak is the largest holding cost along it, endpoints included; a
transition's threshold is the least peak over paths (CLAIM-571), a bottleneck
shortest path. Run: python3 -I this file.
"""
import heapq
import random

INF = float("inf")


def thresholds(cost, edges, src):
    """Least peak from src to every node (minimax path), by Dijkstra."""
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    best = {n: INF for n in cost}
    best[src] = cost[src]
    heap = [(cost[src], src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > best[u]:
            continue
        for v in adj.get(u, []):
            nd = max(d, cost[v])
            if nd < best[v]:
                best[v] = nd
                heapq.heappush(heap, (nd, v))
    return best


def kept(thr, budget):
    return {x for x, t in thr.items() if t <= budget}


# The configurations of the manuscript's section 9, as the entry gives them.
COST = {"A": 1, "B": 1, "C": 1, "C2": 1, "M": 3, "N": 2.5, "D": 1, "P": 3.5}
EDGES = [("A", "M"), ("M", "B"), ("A", "N"), ("N", "C"), ("N", "C2"),
         # control: D is reached only through P, above theta = 3
         ("A", "P"), ("P", "D")]
REDESIGN_COST = {"S1": 2, "S2": 2}
REDESIGN_EDGES = [("A", "S1"), ("S1", "S2"), ("S2", "B"), ("S2", "C2")]


def peak_rule_budget(h, periods, held_at=None):
    """Budget after holding A for `periods` periods under CLAIM-577's rule,
    with an optional reserve (floor or drill) held at `held_at`."""
    b = 3
    for _ in range(periods):
        use = h if held_at is None else max(h, held_at)
        b = use
    return b


def manuscript_case():
    before = thresholds(COST, EDGES, "A")
    after = thresholds({**COST, **REDESIGN_COST}, EDGES + REDESIGN_EDGES, "A")
    assert before["B"] == 3 and after["B"] == 2
    assert before["C"] == 2.5 and after["C"] == 2.5
    assert before["C2"] == 2.5 and after["C2"] == 2   # redesign serves C2 too
    assert before["D"] == after["D"] == 3.5          # control above theta
    theta, theta2, h = before["B"], after["B"], 1
    full = kept(before, theta)          # reserve theta - h, no redesign
    small = kept(after, theta2)         # redesign, reserve theta' - h
    lost = full - small
    assert lost == {"C", "M", "N"}, lost   # thresholds in (2, 3], redesign unused
    assert "D" not in full and "D" not in small   # never kept: the narrowing
    assert "B" in small and "C2" in small
    # Under the peak rule with no reserve the budget falls to h at once.
    assert peak_rule_budget(h, 1) == 1
    assert peak_rule_budget(h, 5, held_at=2) == 2   # drill or floor at 2
    assert "C" not in kept(after, peak_rule_budget(h, 5, held_at=2))
    assert "C" in kept(before, peak_rule_budget(h, 5, held_at=3))
    return before, after


def random_case(rng, n=12, extra=3):
    cost = {"n%d" % i: rng.choice([1, 1.5, 2, 2.5, 3, 3.5, 4]) for i in range(n)}
    cost["n0"] = 1
    nd = lambda i: "n%d" % i
    edges = [(nd(rng.randrange(i)), nd(i)) for i in range(1, n)]
    edges += [(nd(rng.randrange(n)), nd(rng.randrange(n))) for _ in range(n // 2)]
    new = {"r%d" % j: rng.choice([1, 1.5, 2, 2.5]) for j in range(extra)}
    new_edges = [(rng.choice(list(cost) + list(new)), k) for k in new]
    new_edges += [(k, nd(rng.randrange(n))) for k in new for _ in range(2)]
    before = thresholds(cost, edges, "n0")
    after_all = thresholds({**cost, **new}, edges + new_edges, "n0")
    after = {x: after_all[x] for x in cost}
    for x in cost:
        # step 2: a redesign can only lower a threshold ...
        assert after[x] <= before[x]
    target = max([nd(i) for i in range(1, n)], key=lambda x: before[x] - after[x])
    theta, theta2 = before[target], after[target]
    if not theta2 < theta < INF:
        return 0
    lost = kept(before, theta) - kept(after, theta2)
    unused = {x for x in cost if after[x] == before[x]}
    # step 3: among transitions the redesign does not serve, the lost ones
    # are exactly those with threshold in (theta', theta]
    assert lost & unused == {x for x in unused if theta2 < before[x] <= theta}
    # the narrowing: nothing above theta was kept before, so none is "lost"
    assert not {x for x in lost if before[x] > theta}
    return 1


def negative_control():
    """The unnarrowed reading counts every threshold above theta' as lost;
    the control D (3.5 > theta) shows that reading names a transition the
    full reserve never kept."""
    before = thresholds(COST, EDGES, "A")
    after = thresholds({**COST, **REDESIGN_COST}, EDGES + REDESIGN_EDGES, "A")
    unnarrowed = {x for x in COST if after[x] > 2 and after[x] == before[x]}
    assert "D" in unnarrowed and "D" not in kept(before, 3)


def main():
    before, after = manuscript_case()
    print("least peaks before:", {k: before[k] for k in sorted(COST)})
    print("least peaks after: ", {k: after[k] for k in sorted(COST)})
    negative_control()
    rng = random.Random(20261124)
    used = sum(random_case(rng) for _ in range(5000))
    print("random architectures with a lowered threshold checked:", used)
    print("checks pass")


if __name__ == "__main__":
    main()
