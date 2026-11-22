"""Bourrat 2023's dC (LIT-049, Eqs. 1-2) on partitions of the six cells.

Coarse-graining by averaging the trait within each block (NOTE-064, p. 9).
For a stochastic system the predictions are taken as conditional
expectations of the block means h steps ahead:

  C_T(x)   = E[ c(X_{t+h}) | full state x ]           (evolve fine, then coarse)
  C_P(c)   = E[ c(X_{t+h}) | c(X_t) = c ]             (coarse, then evolve)
  C_P(c,r) = E[ c(X_{t+h}) | c(X_t) = c, R_t = r ]    (the dC|E version)

The coarse model is the best predictor from the coarse state under the
stationary distribution. dC(x) is the maximal block error (the paper's
max-error reading, p. 14), dC its stationary mean. dC|E is the largest, over
the environment's states, of the within-state mean ("below theta in all
states of the environment", weighted by the system's actual probability).

`dist=True` gives an extension that is not Bourrat's: the total-variation
distance between the truthful and projected predictive distributions of the
coarse state, instead of the difference of point predictions.
"""
import functools

import numpy as np


def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for part in set_partitions(rest):
        yield [[first]] + part
        for k in range(len(part)):
            yield part[:k] + [[first] + part[k]] + part[k + 1:]


def coarse_index(partition, n_vars, n_cells):
    return _coarse_index(tuple(tuple(b) for b in partition), n_vars)


@functools.lru_cache(maxsize=None)
def _coarse_index(partition, n_vars):
    """Per full state: the block-means vector and an integer id of the
    coarse cell configuration (block counts)."""
    n = 2 ** n_vars
    means = np.zeros((n, len(partition)))
    ids = np.zeros(n, int)
    for s in range(n):
        counts = [sum((s >> i) & 1 for i in b) for b in partition]
        means[s] = [c / len(b) for c, b in zip(counts, partition)]
        k = 0
        for c, b in zip(counts, partition):
            k = k * (len(b) + 1) + c
        ids[s] = k
    return means, ids


def delta_c(Ph, pi, partition, n_vars, n_cells, r_vars, dist=False):
    means, ids = coarse_index(partition, n_vars, n_cells)
    n = Ph.shape[0]
    ridx = np.zeros(n, int)
    for s in range(n):
        ridx[s] = sum(((s >> v) & 1) << j for j, v in enumerate(r_vars))
    if dist:
        nC = ids.max() + 1
        T = np.zeros((n, nC))
        for x2 in range(n):
            T[:, ids[x2]] += Ph[:, x2]
    else:
        T = Ph @ means                      # truthful predictions

    def projected(groups):
        P = np.zeros_like(T)
        for g in np.unique(groups):
            m = groups == g
            w = pi[m]
            P[m] = (w[:, None] * T[m]).sum(0) / w.sum()
        return P

    def err(Pp):
        if dist:
            return 0.5 * np.abs(T - Pp).sum(1)
        return np.abs(T - Pp).max(1)

    e_unc = err(projected(ids))
    e_cond = err(projected(ids * (ridx.max() + 1) + ridx))
    dC = float((pi * e_unc).sum())
    strata = []
    for r in np.unique(ridx):
        m = ridx == r
        strata.append(float((pi[m] * e_cond[m]).sum() / pi[m].sum()))
    return dict(dC=dC, dC_worst=float(e_unc.max()), dC_E=max(strata),
                dC_E_strata=strata)
