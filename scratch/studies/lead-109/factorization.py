"""Self-consistent factorizations into agents (LEAD-109).

We model a fixed level of description as a fixed set of n regimes with a
fixed symmetric coupling matrix M (M[i,j] = interaction strength between
regime i and j, >= 0). A factorization is a partition P of the regimes
into blocks ("candidate agents"). We ask whether, at a FIXED level (fixed
M) and target, several partitions can be self-consistent at once, and
whether any two can CROSSCUT (disagree on co-grouping), which is
CLAIM-170's defeated_if.

The admission test (CLAIM-174), test 1 (CLAIM-157/TERM-049, priced by
CLAIM-154):

  A block is "one system" when it is a near-decomposable block: strong
  within-block coupling, weak across-block coupling, with a gap that beats
  the Occam threshold tau.

Operationalised per partition P:
  a(P) = max across-block edge weight (the strongest coupling P cuts)
  b(P) = min over multi-member blocks of that block's maximum-spanning-tree
         bottleneck (the weakest edge in the strongest way to keep the
         block connected = the single-linkage merge level inside the block)
  gap(P) = b(P) / a(P)         (+inf when a(P)==0: nothing is cut)
  P clears test 1 at tau iff gap(P) > tau.
Singleton blocks impose no within-constraint (a lone regime is trivially
one system).

Test 2 (goal-directed beats device by the Occam cost) and test 3
(adaptation) are per-block gates: a block is kept only if it also passes.
We model test 2 by CLAIM-154's rule directly: reify iff d'^2 > Occam.

The structural result we check: the clearing partitions are exactly cuts
of the single-linkage dendrogram of M, hence TOTALLY NESTED (a chain under
refinement). So crosscutting disagreement is impossible; the only
multiplicity is across grain (a unique finest clearing partition, plus
coarser ones). Tests 2-3 only remove members of this chain.
"""
import itertools
import numpy as np


# ---------- partitions ----------
def partitions(n):
    """All set partitions of range(n), each as a tuple of frozensets."""
    if n == 0:
        yield ()
        return
    first = n - 1
    for smaller in partitions(n - 1):
        # add element `first` to each existing block, or as its own block
        for i, block in enumerate(smaller):
            yield smaller[:i] + (block | {first},) + smaller[i + 1:]
        yield smaller + (frozenset({first}),)


def as_partition(blocks):
    return tuple(sorted((frozenset(b) for b in blocks), key=lambda s: min(s)))


def is_refinement(P, Q):
    """True if P refines Q: every P-block sits inside some Q-block."""
    for b in P:
        if not any(b <= c for c in Q):
            return False
    return True


def comparable(P, Q):
    return is_refinement(P, Q) or is_refinement(Q, P)


def crosscut(P, Q):
    return not comparable(P, Q)


# ---------- test 1: near-decomposable gap ----------
def _max_spanning_bottleneck(M, block):
    """Weakest edge on the maximum-bottleneck spanning tree of `block`.
    = the single-linkage threshold at which `block` becomes one component.
    Returns +inf for a singleton, 0 if the block is disconnected (any
    zero edge must be used)."""
    nodes = sorted(block)
    if len(nodes) == 1:
        return np.inf
    # Prim's algorithm maximising the minimum edge (max-bottleneck tree).
    in_tree = {nodes[0]}
    rest = set(nodes[1:])
    bottleneck = np.inf
    while rest:
        best_w, best_v = -1.0, None
        for u in in_tree:
            for v in rest:
                w = M[u, v]
                if w > best_w:
                    best_w, best_v = w, v
        bottleneck = min(bottleneck, best_w)
        in_tree.add(best_v)
        rest.remove(best_v)
    return bottleneck


def across_max(M, P):
    a = 0.0
    for bi in range(len(P)):
        for bj in range(bi + 1, len(P)):
            for u in P[bi]:
                for v in P[bj]:
                    if M[u, v] > a:
                        a = M[u, v]
    return a


def gap(M, P):
    a = across_max(M, P)
    bs = [_max_spanning_bottleneck(M, b) for b in P if len(b) > 1]
    b = min(bs) if bs else np.inf
    if a == 0.0:
        return np.inf
    return b / a


def clears_test1(M, P, tau):
    return gap(M, P) > tau


# ---------- single-linkage dendrogram cuts ----------
def dendrogram_cuts(M, n):
    """All partitions obtained by single-linkage: connected components of
    the graph keeping edges with weight >= theta, for every distinct edge
    weight theta. These are totally nested by construction."""
    weights = sorted({M[i, j] for i in range(n) for j in range(i + 1, n)},
                     reverse=True)
    cuts = []
    thresholds = [np.inf] + weights
    for theta in thresholds:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n):
            for j in range(i + 1, n):
                if M[i, j] >= theta:
                    parent[find(i)] = find(j)
        comp = {}
        for i in range(n):
            comp.setdefault(find(i), set()).add(i)
        cuts.append(as_partition(comp.values()))
    # dedupe preserving order (finest first)
    seen, out = set(), []
    for c in cuts:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out


# ---------- test 2: CLAIM-154 pricing ----------
def reify(d_prime_sq, occam):
    """CLAIM-154: keep (treat the block as an agent, not a device) iff the
    effect-to-noise d'^2 beats the Occam cost ln(s^2/sigma^2)."""
    return d_prime_sq > occam


def self_consistent_family(M, n, tau, test2=None):
    """All self-consistent factorizations at (M, tau).

    With test2 None we apply test 1 only (the near-decomposable "one
    system" geometry, the binding constraint). Then a lone regime is
    trivially one system, so the all-singletons partition always clears
    and is the finest member.

    A factorization *into agents* (CLAIM-170: "each described as an
    agent") requires EVERY block to pass tests 2-3 as well. Pass test2 as
    a dict block(frozenset) -> (d_prime_sq, occam); a partition is kept
    only if every block (singletons included) reifies as an agent
    (CLAIM-154: d'^2 > Occam). A block absent from test2 defaults to a
    device (fails)."""
    fam = []
    for P in partitions(n):
        PP = as_partition(P)
        if not clears_test1(M, PP, tau):
            continue
        if test2 is not None:
            ok = True
            for b in PP:
                d2, oc = test2.get(frozenset(b), (0.0, np.inf))
                if not reify(d2, oc):
                    ok = False
                    break
            if not ok:
                continue
        fam.append(PP)
    return fam


def is_chain(fam):
    """True iff the family is totally ordered by refinement (no crosscut)."""
    return all(comparable(P, Q) for P, Q in itertools.combinations(fam, 2))


def finest(fam):
    """The unique finest member, if one refines all others; else None."""
    cands = [P for P in fam if all(is_refinement(P, Q) for Q in fam)]
    return cands[0] if len(cands) == 1 else None
