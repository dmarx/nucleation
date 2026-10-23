# scratch/formal/valence.py: synthetic cases behind the valence line's measures (CLAIM-tmp7df5r, TERM-tmp8gbrt)
"""Each case prints what it shows. Run: python3 scratch/formal/valence.py

The measures are kept apart, as the review of PR #327 asked:
- ordinal existence: is the win graph acyclic (a potential exists)?
- ordinal approximation: the least fraction of wins whose reversal
  leaves the graph acyclic (a minimum feedback arc set);
- ordinal alignment: the share of contested wins that agree with a fixed
  ordering;
- cardinal inconsistency: the Hodge cyclic share, meaningful only where
  margins are intensities.
"""
from itertools import combinations, permutations

import numpy as np


def hodge(n: int, flow: list[tuple[int, int, float]]) -> tuple[np.ndarray, float]:
    """Least-squares potential s and cyclic share of a flow (i, j, y): i over j by y."""
    D = np.zeros((len(flow), n))
    Y = np.array([y for _, _, y in flow], dtype=float)
    for k, (i, j, _) in enumerate(flow):
        D[k, i], D[k, j] = 1, -1
    s, *_ = np.linalg.lstsq(D, Y, rcond=None)
    s -= s.mean()
    R = Y - D @ s
    return s, float(R @ R / (Y @ Y)) if Y @ Y > 0 else float("nan")


def wins_graph(wins: list[tuple[int, int]]) -> set[tuple[int, int]]:
    return {(a, b) for a, b in wins}


def acyclic(n: int, edges: set[tuple[int, int]]) -> bool:
    indeg = {v: 0 for v in range(n)}
    for _, b in edges:
        indeg[b] += 1
    queue, seen = [v for v in range(n) if indeg[v] == 0], 0
    while queue:
        v = queue.pop()
        seen += 1
        for a, b in edges:
            if a == v:
                indeg[b] -= 1
                if indeg[b] == 0:
                    queue.append(b)
    return seen == n


def longest_chain_potential(n: int, edges: set[tuple[int, int]]) -> list[int]:
    """CLAIM-tmp7df5r part 1: P(x) = length of the longest chain of wins ending at x."""
    P = [0] * n
    for _ in range(n):
        for a, b in edges:
            P[b] = max(P[b], P[a] + 1)
    return P


def agreement(wins: list[tuple[int, int]], order: list[int]) -> float:
    """Share of wins a -> b ('b won over a' read as a move to b) that climb the ordering.

    Here a win (w, l) means w beat l; it agrees with an ordering that ranks w above l.
    """
    rank = {v: k for k, v in enumerate(order)}  # order lists best first
    return sum(rank[w] < rank[l] for w, l in wins) / len(wins)


def min_reversal_fraction(n: int, wins: list[tuple[int, int]]) -> tuple[float, list[int]]:
    """Ordinal approximation: 1 - best agreement over all orderings (brute force, small n)."""
    best = max(permutations(range(n)), key=lambda o: agreement(wins, list(o)))
    return 1 - agreement(wins, list(best)), list(best)


def circular_triads(n: int, edges: set[tuple[int, int]]) -> int:
    return sum(
        {(a, b), (b, c), (c, a)} <= edges or {(b, a), (c, b), (a, c)} <= edges
        for a, b, c in combinations(range(n), 3)
    )


def case(title: str) -> None:
    print(f"\n== {title}")


# 1. The review's counterexample: an ordinal potential that the Hodge gradient reverses.
case("1. margins A>B by 1, B>C by 10, A>C by 1")
s, cyc = hodge(3, [(0, 1, 1), (1, 2, 10), (0, 2, 1)])
print("Hodge scores (A, B, C):", np.round(s, 3), "-> B above A, reversing the A>B win")
print("cyclic share:", round(cyc, 3), "although the win relation A>B>C is transitive")
moves = {(1, 0), (2, 1), (2, 0)}  # a move from loser to winner
print("ordinal: acyclic =", acyclic(3, moves), "; longest-chain potential (A, B, C):",
      longest_chain_potential(3, moves), "-> keeps A>B>C")

# 2. Complete, equally weighted transitive tournaments: the (n-2)/3n baseline holds.
case("2. complete binary transitive tournaments")
for n in (3, 4, 5, 8, 20):
    _, cyc = hodge(n, [(i, j, 1) for i, j in combinations(range(n), 2)])
    print(f"n={n}: cyclic share {cyc:.4f}, (n-2)/3n = {(n - 2) / (3 * n):.4f}")

# 3. The baseline does not carry to sparse graphs.
case("3. transitive but sparse: 4 options, pair (A, C) never contested")
flow = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 1), (1, 3, 1)]
_, cyc = hodge(4, flow)
print(f"cyclic share {cyc:.3f} vs complete baseline {2 / 12:.3f}")
# null model: the same graph, orientations drawn from uniformly random orderings
rng = np.random.default_rng(0)
pairs = [(0, 1), (1, 2), (2, 3), (0, 3), (1, 3)]
transitive_null = []
for _ in range(2000):
    order = rng.permutation(4)
    rank = {v: k for k, v in enumerate(order)}
    transitive_null.append(hodge(4, [(a, b, 1 if rank[a] < rank[b] else -1) for a, b in pairs])[1])
print("graph-preserving transitive null: cyclic share ranges",
      round(min(transitive_null), 3), "to", round(max(transitive_null), 3),
      "; so a sparse record's baseline depends on its graph and on which ordering produced it")

# 4. Aggregation erases ambivalence.
case("4. alternation on one pair: A, B, A, B, A, B")
history = [(0, 1), (1, 0)] * 3
net = sum(1 if w == 0 else -1 for w, _ in history)
print("net flow A over B:", net, "-> aggregated record shows no conflict at all")
signs = [1 if w == 0 else -1 for w, _ in history]
flips = sum(a != b for a, b in zip(signs, signs[1:]))
print("kept apart: direction", net / len(history), "; contests", len(history),
      "; reversals", flips, "of", len(history) - 1, "-> maximal variability")
print("per-window graphs (window = 1 contest) are each acyclic; the ambivalence is in the sequence")

# 5. Conflict-free systems are vacuously eligible under existence alone.
case("5. no contested pairs")
print("empty win graph acyclic:", acyclic(3, set()), "; every ordering is trivially a potential,",
      "agreement undefined (no wins) -> valence must be undefined, not zero")

# 6. Coherence is not alignment, measured ordinally.
case("6. coherence vs alignment")
# perspectives v: A>B>C and w: C>B>A; a stable compromise settles every conflict as B>A>C
for label, wins in (("compromise B>A>C", [(1, 0), (1, 2), (0, 2)] * 2),
                    ("v decides all", [(0, 1), (0, 2), (1, 2)] * 2)):
    frac, best = min_reversal_fraction(3, wins)
    print(f"{label}: incoherence {frac:.2f}; alignment with v {agreement(wins, [0, 1, 2]):.2f},",
          f"with w {agreement(wins, [2, 1, 0]):.2f}")
print("both records are wholly coherent; only the second is aligned with a perspective")

# 7. Identifiability: the wins need not single out one perspective.
case("7. two perspectives the wins cannot tell apart")
wins = [(0, 1), (2, 3), (0, 3)]  # pairs (1, 2) and others never contested
for name, order in (("v: A>B>C>D", [0, 1, 2, 3]), ("w: C>A>D>B", [2, 0, 3, 1])):
    print(f"alignment with {name}: {agreement(wins, order):.2f}")
print("both are potentials of the record; only an intervention that contests a pair they",
      "rank differently (e.g. B against C) separates them")

# 8. Ambivalence counted ordinally: circular triads.
case("8. circular triads")
cycle = {(0, 1), (1, 2), (2, 0)}
print("3-cycle: acyclic =", acyclic(3, cycle), "; circular triads =", circular_triads(3, cycle),
      "; Hodge cyclic share =", round(hodge(3, [(0, 1, 1), (1, 2, 1), (2, 0, 1)])[1], 3))

# 9. The lexicographic semiorder of CLAIM-tmp85p0g, part 3b, cycles.
case("9. lexicographic semiorder, delta = 1")
d = 1.0
xs = [(0, 0), (d / 2, 1 / 3), (d, 2 / 3), (3 * d / 2, 1)]


def chosen(x: tuple[float, float], y: tuple[float, float]) -> bool:
    return y[0] - x[0] > d or (abs(x[0] - y[0]) <= d and x[1] > y[1])


E = {(i, j) for i in range(4) for j in range(4) if i != j and chosen(xs[i], xs[j])}
print("choices (winner, loser):", sorted(E), "; acyclic =", acyclic(4, E),
      "; circular triads =", circular_triads(4, E))
