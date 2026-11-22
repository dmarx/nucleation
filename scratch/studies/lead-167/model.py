"""A minimal ecological-scaffolding model, exact over its 256 states.

Six cells (binary trait x_i) in two patches, A = cells 0-2 and B = cells 3-5,
and one binary scaffold variable per patch, r_A (variable 6) and r_B
(variable 7). A full state is an integer whose bit k is variable k.

One synchronous step:

* Scaffold. Each r_p is an external two-state Markov chain, independent of
  the cells: present (1) stays present with prob 1 - q_off, absent (0) turns
  present with prob q_on.
* Collective reproduction (imposed by the scaffold's dispersal regime). With
  prob d/2 patch A is recolonised from B, with prob d/2 B from A, otherwise
  neither: every cell of the recolonised patch copies one uniformly chosen
  cell of the other patch (a one-cell propagule).
* Otherwise each cell i in patch p independently: with prob eps its next
  trait is a fair coin; else with prob a it keeps its own trait (cell-level
  heredity); else with prob g_p it copies a uniformly chosen cell of its own
  patch (itself included), and with prob 1 - g_p a uniformly chosen cell of
  the whole population (no collective structure).
  g_p = r_p + (1 - r_p) * lam: the patch holds together when the scaffold is
  present, and when it is absent only to the degree lam that the cells hold it
  together themselves. lam is the endogenisation parameter: the path through
  the transition runs from lam = 0 (collectives exist only where the
  scaffold is) to lam = 1 (the cells keep them whatever the scaffold does).

`common_input_kernel` is a control with no interaction at all: each cell keeps
its trait with prob a and otherwise copies its patch's environment r_p (a
"reconstructed entity", Bourrat 2024's Fig. 2 situation, at patch level).
"""
from itertools import product

import numpy as np

N_CELLS = 6
PATCH = (0, 0, 0, 1, 1, 1)          # patch of each cell
PATCH_CELLS = ((0, 1, 2), (3, 4, 5))
R_VAR = (6, 7)                      # scaffold variable of each patch
N_VARS = 8
N_STATES = 2 ** N_VARS


def bits(s, n=N_VARS):
    return [(s >> k) & 1 for k in range(n)]


def _cells_kernel(x, r, p_one):
    """Distribution over the 64 next cell configurations when cell i is 1
    with prob p_one[i] independently."""
    out = np.ones(2 ** N_CELLS)
    for c in range(2 ** N_CELLS):
        for i in range(N_CELLS):
            b = (c >> i) & 1
            out[c] *= p_one[i] if b else 1.0 - p_one[i]
    return out


def _recolonised(src_cells):
    """Distribution over a patch's next 3-cell config when it is refounded by
    one uniformly chosen cell of the other patch."""
    out = np.zeros(8)
    for v in src_cells:
        out[7 if v else 0] += 1.0 / len(src_cells)
    return out


def _patch_marginal_normal(p_one, cells):
    out = np.ones(8)
    for c in range(8):
        for j, i in enumerate(cells):
            b = (c >> j) & 1
            out[c] *= p_one[i] if b else 1.0 - p_one[i]
    return out


def scaffold_kernel(lam, a=0.3, eps=0.05, d=0.05, q_on=0.2, q_off=0.2):
    P = np.zeros((N_STATES, N_STATES))
    for s in range(N_STATES):
        v = bits(s)
        x, r = v[:N_CELLS], [v[6], v[7]]
        m = [np.mean([x[i] for i in PATCH_CELLS[p]]) for p in (0, 1)]
        M = np.mean(x)
        p_one = []
        for i in range(N_CELLS):
            p = PATCH[i]
            g = r[p] + (1 - r[p]) * lam
            inner = a * x[i] + (1 - a) * (g * m[p] + (1 - g) * M)
            p_one.append(eps / 2 + (1 - eps) * inner)
        # per-patch next distributions (cells within a patch are conditionally
        # independent in the normal branch; patches are independent too)
        normA = _patch_marginal_normal(p_one, PATCH_CELLS[0])
        normB = _patch_marginal_normal(p_one, PATCH_CELLS[1])
        recA = _recolonised([x[i] for i in PATCH_CELLS[1]])
        recB = _recolonised([x[i] for i in PATCH_CELLS[0]])
        cells = ((1 - d) * np.outer(normA, normB)
                 + d / 2 * np.outer(recA, normB)
                 + d / 2 * np.outer(normA, recB))   # [cA, cB]
        cells = cells.reshape(-1, order="F")        # index cA + 8*cB
        rnext = []
        for p in (0, 1):
            p1 = 1 - q_off if r[p] else q_on
            rnext.append(np.array([1 - p1, p1]))
        rr = np.outer(rnext[0], rnext[1]).reshape(-1, order="F")  # rA + 2*rB
        P[s] = np.outer(cells, rr).reshape(-1, order="F")         # c + 64*rr
    return P


def common_input_kernel(a=0.3, eps=0.05, q_on=0.2, q_off=0.2,
                        asymmetric=False):
    """asymmetric=True: a present environment drives the cell to 1, an absent
    one leaves it a fair coin (the environment's effect is not a relabelling
    of itself across its two states)."""
    P = np.zeros((N_STATES, N_STATES))
    for s in range(N_STATES):
        v = bits(s)
        x, r = v[:N_CELLS], [v[6], v[7]]
        drive = [(1.0 if r[p] else 0.5) if asymmetric else float(r[p])
                 for p in (0, 1)]
        p_one = [eps / 2 + (1 - eps) * (a * x[i] + (1 - a) * drive[PATCH[i]])
                 for i in range(N_CELLS)]
        cells = _cells_kernel(x, r, p_one)
        rnext = []
        for p in (0, 1):
            p1 = 1 - q_off if r[p] else q_on
            rnext.append(np.array([1 - p1, p1]))
        rr = np.outer(rnext[0], rnext[1]).reshape(-1, order="F")
        P[s] = np.outer(cells, rr).reshape(-1, order="F")
    return P


def stationary(P):
    w, V = np.linalg.eig(P.T)
    k = np.argmin(np.abs(w - 1))
    pi = np.real(V[:, k])
    pi = pi / pi.sum()
    pi[pi < 0] = 0
    return pi / pi.sum()
