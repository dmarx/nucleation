"""Abstract finite groups as index sets with a Cayley table, and the
one-hot composition dataset.

The network sees elements ONLY as one-hot indices 0..n-1. No matrix
representation of the group is ever supplied to the model. The permutation
realisation here is a private device to *generate* the multiplication table;
its matrices never touch the network or the blind recovery path.
"""
import itertools
import numpy as np


def _perm_compose(p, q):
    # (p*q)(i) = p(q(i)); permutations as tuples.
    return tuple(p[q[i]] for i in range(len(p)))


def symmetric_group(n):
    """Return (elements, cayley) for S_n.

    elements: list of permutation tuples (index -> element).
    cayley: int array C[g, h] = index of element g*h.
    The indexing is arbitrary (itertools order); nothing downstream may
    assume it.
    """
    elems = sorted(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(elems)}
    m = len(elems)
    cayley = np.zeros((m, m), dtype=np.int64)
    for i, p in enumerate(elems):
        for j, q in enumerate(elems):
            cayley[i, j] = idx[_perm_compose(p, q)]
    return elems, cayley


def cyclic_group(n):
    """Return (elements, cayley) for Z/n (abelian, for a contrast control)."""
    elems = list(range(n))
    cayley = np.array([[(i + j) % n for j in elems] for i in elems],
                      dtype=np.int64)
    return elems, cayley


def is_group_table(cayley):
    """Check a square int table is a group op: closure, identity, inverses,
    associativity. Returns a dict of booleans/fractions. Uses ONLY the table
    (no group supplied)."""
    m = cayley.shape[0]
    assert cayley.shape == (m, m)
    vals = set(cayley.flatten().tolist())
    closure = vals <= set(range(m))
    # identity: a row == 0..m-1 and matching column.
    ident = None
    for e in range(m):
        if np.array_equal(cayley[e], np.arange(m)) and \
           np.array_equal(cayley[:, e], np.arange(m)):
            ident = e
            break
    has_ident = ident is not None
    has_inv = False
    if has_ident:
        has_inv = all(ident in cayley[g].tolist() and
                      ident in cayley[:, g].tolist() for g in range(m))
    # associativity fraction over all triples.
    good = 0
    tot = m * m * m
    for a in range(m):
        ca = cayley[a]
        for b in range(m):
            ab = cayley[a, b]
            # (a*b)*c vs a*(b*c) for all c
            left = cayley[ab]          # (a*b)*c over c
            right = cayley[a, cayley[b]]  # a*(b*c) over c
            good += int(np.sum(left == right))
    assoc_frac = good / tot
    return {
        "closure": bool(closure),
        "identity": ident,
        "has_identity": bool(has_ident),
        "has_inverses": bool(has_inv),
        "assoc_frac": float(assoc_frac),
        "is_group": bool(closure and has_ident and has_inv and
                         assoc_frac == 1.0),
    }


def composition_dataset(cayley):
    """All (g, h) -> g*h as one-hot inputs and integer target.

    Returns X (m*m, 2*m) one-hot [onehot(g) | onehot(h)], y (m*m,) int.
    """
    m = cayley.shape[0]
    rows_x = []
    rows_y = []
    eye = np.eye(m)
    for g in range(m):
        for h in range(m):
            rows_x.append(np.concatenate([eye[g], eye[h]]))
            rows_y.append(int(cayley[g, h]))
    return np.array(rows_x), np.array(rows_y, dtype=np.int64)
