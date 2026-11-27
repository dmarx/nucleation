# scratch/studies/lead-tmpuszbx/indecision.py
"""Indecision as a terminal strongly connected component of the would-prevail relation.

The relation of winning moves (loser -> winner) need not be acyclic, but its
condensation, with each strongly connected component (SCC) collapsed to one
node, always is, so it always has a potential over components. A winning-move
dynamics (from the current state, take any move that beats it) ends in a
terminal component. A terminal component of one state is a decision; of more
than one, the dynamics cycles there forever: indecision. The owner's
"valence toward indecision" is read here as the probability, over the
situations the organization starts from, of ending in a non-singleton
terminal component.
"""
import random
from itertools import combinations



def sccs(states, moves):
    """Tarjan's algorithm; returns a list of components (sets)."""
    succ = {s: [w for l, w in moves if l == s] for s in states}
    index, low, stack, on, out, n = {}, {}, [], set(), [], [0]

    def visit(v):
        index[v] = low[v] = n[0]; n[0] += 1; stack.append(v); on.add(v)
        for w in succ[v]:
            if w not in index:
                visit(w); low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = set()
            while True:
                w = stack.pop(); on.discard(w); comp.add(w)
                if w == v:
                    break
            out.append(comp)

    for v in states:
        if v not in index:
            visit(v)
    return out


def condensation_acyclic(states, moves):
    comps = sccs(states, moves)
    cid = {s: i for i, c in enumerate(comps) for s in c}
    edges = {(cid[l], cid[w]) for l, w in moves if cid[l] != cid[w]}
    # acyclic iff the component graph has an SCC decomposition into singletons
    return all(len(c) == 1 for c in sccs(list(range(len(comps))), list(edges))), comps, cid, edges


def terminal(comps, cid, edges):
    has_out = {a for a, b in edges}
    return [c for i, c in enumerate(comps) if i not in has_out]


def p_indecision(states, moves, start_weights, trials=20000, steps=60, seed=0):
    rng = random.Random(seed)
    comps = sccs(states, moves)
    cid = {s: i for i, c in enumerate(comps) for s in c}
    succ = {s: [w for l, w in moves if l == s] for s in states}
    starts, weights = zip(*start_weights.items())
    hit = 0
    for _ in range(trials):
        s = rng.choices(starts, weights)[0]
        for _ in range(steps):
            if not succ[s]:
                break
            s = rng.choice(succ[s])
        hit += len(comps[cid[s]]) > 1 and not succ[s] == []
    return hit / trials


def report(name, states, moves, starts):
    ok, comps, cid, edges = condensation_acyclic(states, moves)
    term = terminal(comps, cid, edges)
    p = p_indecision(states, moves, starts)
    print(f"{name}: condensation acyclic={ok}; terminal components={[sorted(c) for c in term]}; "
          f"P(indecision)={p:.3f}")


S3 = ["a", "b", "c"]
# would_prevail.py case 4: P1 a>b>c, P2 b>c>a, P3 c>a>b, equal influence, majority.
case4 = [("b", "a"), ("c", "b"), ("a", "c")]
report("majority cycle (case 4)", S3, case4, {s: 1 for s in S3})

# Four states: a cycle among a, b, c, and a fourth state d that beats one of them.
S4 = ["a", "b", "c", "d"]
mv = [("a", "b"), ("b", "c"), ("c", "a"), ("c", "d")]
report("d escapes the cycle from c", S4, mv, {s: 1 for s in S4})
mv2 = [("a", "b"), ("b", "c"), ("c", "a"), ("d", "a")]
report("d feeds the cycle", S4, mv2, {s: 1 for s in S4})
# Sparse record: two separate sinks, one a cycle, one a winner; starts decide.
S6 = ["a", "b", "c", "d", "e", "f"]
mv3 = [("a", "b"), ("b", "c"), ("c", "a"), ("d", "e"), ("f", "e")]
report("two basins, uniform starts", S6, mv3, {s: 1 for s in S6})
report("two basins, starts mostly in the cycle's basin", S6, mv3, {"a": 4, "b": 4, "c": 4, "d": 1, "e": 1, "f": 1})

# Every relation's condensation is acyclic: check on random relations.
rng = random.Random(1)
bad = 0
for _ in range(2000):
    n = rng.randint(2, 7)
    st = list(range(n))
    m = [(i, j) if rng.random() < 0.5 else (j, i) for i, j in combinations(st, 2) if rng.random() < 0.7]
    bad += not condensation_acyclic(st, m)[0]
print("random relations with a cyclic condensation:", bad, "of 2000")
