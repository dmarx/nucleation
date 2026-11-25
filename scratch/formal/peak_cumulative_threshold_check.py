"""scratch/formal/peak_cumulative_threshold_check.py

Rebuilds the check of CLAIM-646 on its construction CASE-236 from the
entries' text alone: no script of the filer's was kept. Written at the
recomputation pass of 2026-11-25 by a session other than the filer's.
Run: python3 -I this file. Standard library only.

On configurations 0..n, every configuration and every move needs one unit
of held (peak) capacity and every move spends one unit. The chain allows
moves i <-> i+1; the complete graph a move between every pair. Checks:
(1) the peak threshold B*(x, y), the least over paths of the largest peak
along the path, is 1 for every pair in both systems; (2) at a peak budget
below 1 no pair is joined; (3) the least cumulative cost from 0 to n is n
in the chain and 1 in the complete graph; (4) CLAIM-581's non-equivalence
of additive budgets in the chain at budget 1; and a negative control: a
chain whose middle configuration needs two units has threshold 2 across it,
so the check can fail.
"""
import heapq


def systems(n):
    chain = {i: [j for j in (i - 1, i + 1) if 0 <= j <= n] for i in range(n + 1)}
    full = {i: [j for j in range(n + 1) if j != i] for i in range(n + 1)}
    return chain, full


def minimax(adj, hold, move, s):
    """Least, over paths from s, of the largest peak need (configurations and moves)."""
    best = {s: hold[s]}
    pq = [(hold[s], s)]
    while pq:
        b, u = heapq.heappop(pq)
        if b > best[u]:
            continue
        for v in adj[u]:
            nb = max(b, move, hold[v])
            if nb < best.get(v, float("inf")):
                best[v] = nb
                heapq.heappush(pq, (nb, v))
    return best


def least_spend(adj, s):
    dist = {s: 0}
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v in adj[u]:
            if d + 1 < dist.get(v, float("inf")):
                dist[v] = d + 1
                heapq.heappush(pq, (d + 1, v))
    return dist


def check(n):
    chain, full = systems(n)
    hold = {i: 1 for i in range(n + 1)}
    for adj in (chain, full):
        for x in range(n + 1):
            b = minimax(adj, hold, 1, x)
            assert all(b[y] == 1 for y in range(n + 1)), (n, x)
            # below budget 1 nothing can even be held, so no pair is joined
            assert min(b.values()) >= 1
    assert least_spend(chain, 0)[n] == n
    assert least_spend(full, 0)[n] == 1
    return n / 1


for n in (2, 3, 10, 40, 100):
    ratio = check(n)
    print(f"n = {n:>3}: every pair at threshold 1 in both; least spend 0 -> n: chain {n}, complete 1 (ratio {ratio:g})")

# CLAIM-581: additive budgets give no equivalence (chain, cumulative budget 1)
chain, _ = systems(2)
d = {x: least_spend(chain, x) for x in range(3)}
assert d[0][1] <= 1 and d[1][2] <= 1 and d[0][2] > 1

# negative control: raise the middle configuration's need to 2
chain, full = systems(4)
hold = {0: 1, 1: 1, 2: 2, 3: 1, 4: 1}
assert minimax(chain, hold, 1, 0)[4] == 2
assert minimax(full, hold, 1, 0)[4] == 1  # the complete graph routes round it
print("negative control: a chain with a 2-unit middle has threshold 2 across it; the complete graph 1")
print("checks pass")
