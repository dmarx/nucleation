# scratch/studies/lead-tmpuszbx/would_prevail.py
"""Compute the would-prevail relation of a will-organization state on small cases.

A will-organization state W (LEAD-tmpuszbx's sketch) is:
  base[k][r]   baseline influence I0 of perspective k in region r
  budget[i]    grant budget b_i
  E[i][j][r]   region-indexed grant matrix, rows stochastic per region, E_ii = 0
  gate[k][c]   suspension: 1 if k's influence is in force in context c, else 0
Influence is one-hop (CLAIM-282): I_j(r) = I0_j(r) + sum_{i!=j} b_i E_ij(r),
times the gate. Settlement of a pair (s, t) in region r and context c is a
weighted vote of the perspectives' rankings by influence. The would-prevail
relation is the set of winning moves over every pair the rankings disagree
on (contestable), whether or not the contest has occurred (CLAIM-tmphyvh3).
"""
from itertools import combinations


def influence(W, k, r, c):
    I = W["base"][k][r] + sum(
        W["budget"][i] * W["E"][i][k][r] for i in W["base"] if i != k
    )
    return I * W.get("gate", {}).get(k, {}).get(c, 1)


def prevails(W, ranks, s, t, r, c):
    """Return the state that prevails between s and t, or None on a tie."""
    vs = vt = 0.0
    for k, order in ranks.items():
        w = influence(W, k, r, c)
        if order.index(s) < order.index(t):
            vs += w
        elif order.index(t) < order.index(s):
            vt += w
    return s if vs > vt else t if vt > vs else None


def relation(W, ranks, states, region, c="calm"):
    """Winning moves (loser -> winner) over contestable pairs."""
    moves = []
    for s, t in combinations(states, 2):
        orders = [o.index(s) < o.index(t) for o in ranks.values()]
        if all(orders) or not any(orders):
            continue  # uncontestable: every perspective ranks the pair alike
        win = prevails(W, ranks, s, t, region(s, t), c)
        if win is not None:
            moves.append(((t if win == s else s), win))
    return moves


def potential(moves, states):
    """A topological order of the winning moves (best first), or None if cyclic."""
    succ = {s: {w for l, w in moves if l == s} for s in states}
    indeg = {s: 0 for s in states}
    for l, w in moves:
        indeg[l] += 1  # count edges into the loser side when reversing
    order, ready = [], [s for s in states if indeg[s] == 0]
    while ready:
        s = ready.pop()
        order.append(s)
        for l, w in moves:
            if w == s:
                indeg[l] -= 1
                if indeg[l] == 0:
                    ready.append(l)
    return order if len(order) == len(states) else None


def describe(name, W, ranks, states, region=lambda s, t: "x", c="calm"):
    mv = relation(W, ranks, states, region, c)
    pot = potential(mv, states)
    match = [k for k, o in ranks.items() if pot == o]
    if not mv:
        verdict = "no contestable pair: valence undefined even dispositionally"
    elif pot is None:
        verdict = "cyclic: no potential, no valence"
    else:
        verdict = f"potential {pot}" + (f" = {match[0]}'s ranking" if match else " (nobody's ranking)")
    print(f"{name}: {len(mv)} contestable moves; {verdict}")
    return pot


S = ["a", "b", "c"]
zero = lambda ks: {i: {j: {"x": 0.0, "y": 0.0} for j in ks} for i in ks}


def state(base, grants=None, budget=None, gate=None):
    ks = list(base)
    E = zero(ks)
    for (i, j, r), v in (grants or {}).items():
        E[i][j][r] = v
    return {"base": base, "budget": budget or {k: 0.0 for k in ks}, "E": E, "gate": gate or {}}


R2 = {"P1": ["a", "b", "c"], "P2": ["c", "b", "a"]}
R2_alt = {"P1": ["b", "a", "c"], "P2": ["c", "b", "a"]}

# 1-2. Same rankings, two will-organizations: an arbiter A grants to P1, or to P2.
base3 = {"P1": {"x": 1, "y": 1}, "P2": {"x": 1, "y": 1}, "A": {"x": 0, "y": 0}}
RA = dict(R2)  # the arbiter holds no ranking of its own
W_to1 = state({k: v for k, v in base3.items()}, {("A", "P1", "x"): 1.0}, {"P1": 0, "P2": 0, "A": 5})
W_to2 = state({k: v for k, v in base3.items()}, {("A", "P2", "x"): 1.0}, {"P1": 0, "P2": 0, "A": 5})
p1 = describe("1 arbiter grants P1", W_to1, RA, S)
p2 = describe("2 arbiter grants P2", W_to2, RA, S)
# 3. Same will-organization as 1, different rankings.
p3 = describe("3 W as in 1, rankings changed", W_to1, R2_alt, S)
print("   W changes valence with rankings fixed:", p1 != p2, "| rankings change it with W fixed:", p1 != p3)

# 4. Majority among three with Condorcet rankings and equal influence.
R3 = {"P1": ["a", "b", "c"], "P2": ["b", "c", "a"], "P3": ["c", "a", "b"]}
eq = state({k: {"x": 1, "y": 1} for k in R3})
describe("4 equal influence, Condorcet rankings", eq, R3, S)

# 5. Agreement on every pair.
describe("5 agreement everywhere", state({k: {"x": 1, "y": 1} for k in R2}), {"P1": S, "P2": list(S)}, S)

# 6. Jurisdiction: P1 governs region x, P2 region y; regions share states.
jur = state({"P1": {"x": 1, "y": 0}, "P2": {"x": 0, "y": 1}})
Rj = {"P1": ["b", "a", "c"], "P2": ["c", "a", "b"]}  # every pair contested
region = lambda s, t: "y" if {s, t} == {"b", "c"} else "x"
describe("6 jurisdiction split, shared states", jur, Rj, S, region)
describe("6a as 6, but P2 agrees with P1 on (a, b)", jur, {"P1": ["b", "a", "c"], "P2": ["c", "b", "a"]}, S, region)
describe("6' jurisdiction split, P1 also holds (b,c)", jur, Rj, S, lambda s, t: "x")

# 7. Suspension: P1 dominates when calm; under threat its influence is gated off.
sus = state({"P1": {"x": 2, "y": 2}, "P2": {"x": 1, "y": 1}}, gate={"P1": {"threat": 0}})
describe("7 calm", sus, R2, S, c="calm")
describe("7 threat (P1 suspended)", sus, R2, S, c="threat")
