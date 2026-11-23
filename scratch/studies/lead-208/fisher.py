"""Fisher metric of the 13 couplings from decimated spins.

For an exponential family p_theta(s) ~ exp(theta . Phi(s)), the Fisher metric
of the data o = (spins kept after k decimations) is

    g^k = Cov( E[Phi | o] )                          (THEORY-777, Eq. 34)

Level 0: E[Phi | o] = Phi.  Level 1: o is the black sublattice and the
conditional mean is exact (rb_given_black).  Level k >= 2: E[Phi | o] =
E[ rb(black) | o ], estimated by two independent compatible chains (SW plus
heat-bath on the free sites, the observed sites frozen), started from the
sampled configuration, which is itself an exact draw from the conditional
law. Using the product of the two chains' means removes the bias that the
square of a single noisy mean would add (Machta et al.'s "products over
distinct replicas"); what remains is the chains' correlation through their
common start, which the burn-in controls (checked in the run).
"""
import numpy as np

from ising import (NPARAM, heat_bath, observables, observed_mask,
                   rb_given_black, swendsen_wang)


def compatible_mean(s0, K, frozen, rng, burn, nmeas):
    """Mean of rb(black) over a compatible chain from s0, observed sites frozen."""
    s = s0.copy()
    acc = np.zeros((s.shape[0], NPARAM))
    for t in range(burn + nmeas):
        swendsen_wang(s, K, rng, frozen=frozen)
        heat_bath(s, K, rng, frozen=frozen)
        if t >= burn:
            acc += rb_given_black(s, K)
    return acc / nmeas


def level_estimates(s, K, levels, rng, burn=3, nmeas=2):
    """For each level k, two estimates (A, B) of E[Phi | o_k], each (B, 13)."""
    L = s.shape[-1]
    out = {}
    for k in levels:
        if k == 0:
            a = observables(s)
            out[k] = (a, a)
        elif k == 1:
            a = rb_given_black(s, K)
            out[k] = (a, a)
        else:
            fz = observed_mask(L, k)
            a = compatible_mean(s, K, fz, rng, burn, nmeas)
            b = compatible_mean(s, K, fz, rng, burn, nmeas)
            out[k] = (a, b)
    return out


def cross_cov(A, B):
    """Symmetrised cross-covariance of two estimates of the same quantity."""
    A = A - A.mean(axis=0)
    B = B - B.mean(axis=0)
    C = A.T @ B / (len(A) - 1)
    return 0.5 * (C + C.T)


def spectrum_with_errors(A, B, nblocks=16):
    """Eigenvalues (descending) of cross_cov(A, B), with jackknife errors.

    Rows of A and B must be ordered so that consecutive blocks are
    independent (whole chains per block)."""
    lam = np.sort(np.linalg.eigvalsh(cross_cov(A, B)))[::-1]
    n = len(A)
    edges = np.linspace(0, n, nblocks + 1).astype(int)
    jk = []
    for i in range(nblocks):
        keep = np.r_[0:edges[i], edges[i + 1]:n]
        jk.append(np.sort(np.linalg.eigvalsh(cross_cov(A[keep], B[keep])))[::-1])
    jk = np.array(jk)
    err = np.sqrt((nblocks - 1) / nblocks * ((jk - jk.mean(axis=0)) ** 2).sum(axis=0))
    return lam, err, jk
