"""Signalling estimators, intervals and a test for binary CbD systems (LEAD-072).

Notation. A binary content q is recorded in two contexts c and c'. In c it
takes value +1 in x of n occurrences, in c' in y of m occurrences, with
true probabilities p and p'. CbD's signalling (LIT-851 Eq. 1) is

    Delta = sum_q |<R_q^c> - <R_q^c'>| = sum_q 2 |p_q - p'_q|.

Everything here is per content and adds up over contents; the interval
and the test combine contents by Bonferroni, which is valid whatever the
dependence between contents that share a context.

Estimators (per content, in Delta units, i.e. 2|p - p'|):
  plug(x,n,y,m)    2 |x/n - y/m|                      (the plug-in)
  root_u2(x,n,y,m) 2 sqrt(max(0, U)), U unbiased for (p - p')^2 (n, m >= 2)

Interval (stated sampling error):
  box_interval     simultaneous Clopper-Pearson intervals for every
                   context marginal at level alpha/(2k), and Delta's range
                   over that box. Coverage >= 1 - alpha for any n, m.
  newcombe_delta   Newcombe hybrid-score interval for p - p' per content
                   at alpha/k, folded and summed. Approximate.

Test of the null "no content signals" (H0: p_q = p'_q for every q):
  nosig_test       per-content Fisher exact (or Boschloo) p-values,
                   Bonferroni over contents. Size <= alpha.
"""
import math

import numpy as np
from scipy import stats


# ---------------------------------------------------------------- estimators

def plug(x, n, y, m):
    return 2.0 * abs(x / n - y / m)


def u2(x, n, y, m):
    """Unbiased estimator of (p - p')^2 from independent Bin(n,p), Bin(m,p')."""
    if n < 2 or m < 2:
        raise ValueError("U2 needs at least two occurrences in each context")
    return (x * (x - 1)) / (n * (n - 1)) - 2.0 * x * y / (n * m) + (y * (y - 1)) / (m * (m - 1))


def root_u2(x, n, y, m):
    return 2.0 * math.sqrt(max(0.0, u2(x, n, y, m)))


# ---------------------------------------------------------------- intervals

def clopper_pearson(x, n, alpha):
    """Two-sided exact interval for a binomial proportion at level 1 - alpha."""
    lo = 0.0 if x == 0 else stats.beta.ppf(alpha / 2, x, n - x + 1)
    hi = 1.0 if x == n else stats.beta.ppf(1 - alpha / 2, x + 1, n - x)
    return float(lo), float(hi)


def abs_diff_range(lp, up, lq, uq):
    """Min and max of |p - q| over p in [lp, up], q in [lq, uq]."""
    lo = max(0.0, lp - uq, lq - up)
    hi = max(up - lq, uq - lp)
    return lo, hi


def box_interval(contents, alpha=0.05):
    """contents: list of (x, n, y, m). Returns (lo, hi) for Delta.

    Each of the 2k context marginals gets a Clopper-Pearson interval at
    alpha/(2k); with probability >= 1 - alpha all hold at once, and then
    Delta lies in [sum of per-content minima, sum of maxima]."""
    k = len(contents)
    a = alpha / (2 * k)
    lo = hi = 0.0
    for x, n, y, m in contents:
        lp, up = clopper_pearson(x, n, a)
        lq, uq = clopper_pearson(y, m, a)
        l, h = abs_diff_range(lp, up, lq, uq)
        lo += 2 * l
        hi += 2 * h
    return lo, hi


def wilson(x, n, alpha):
    z = stats.norm.ppf(1 - alpha / 2)
    ph = x / n
    den = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / den
    w = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return c - w, c + w


def newcombe(x, n, y, m, alpha):
    """Newcombe (1998) method 10 hybrid score interval for p - p'."""
    p1, p2 = x / n, y / m
    l1, u1 = wilson(x, n, alpha)
    l2, u2_ = wilson(y, m, alpha)
    d = p1 - p2
    lo = d - math.sqrt((p1 - l1) ** 2 + (u2_ - p2) ** 2)
    hi = d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return lo, hi


def newcombe_delta(contents, alpha=0.05):
    k = len(contents)
    lo = hi = 0.0
    for x, n, y, m in contents:
        l, h = newcombe(x, n, y, m, alpha / k)
        if l > 0:
            fl, fh = l, h
        elif h < 0:
            fl, fh = -h, -l
        else:
            fl, fh = 0.0, max(-l, h)
        lo += 2 * fl
        hi += 2 * fh
    return lo, hi


# ---------------------------------------------------------------- test

def content_pvalue(x, n, y, m, method="fisher"):
    table = [[x, n - x], [y, m - y]]
    if method == "fisher":
        return float(stats.fisher_exact(table).pvalue)
    if method == "boschloo":
        return float(stats.boschloo_exact(table, n=32).pvalue)
    raise ValueError(method)


def nosig_test(contents, alpha=0.05, method="fisher"):
    """Bonferroni over per-content exact tests. Returns (reject, min p * k)."""
    k = len(contents)
    ps = [content_pvalue(*c, method=method) for c in contents]
    padj = min(1.0, k * min(ps))
    return padj <= alpha, padj


# ---------------------------------------------------------------- exact moments

def exact_moments(est, n, m, p, q):
    """Exact mean and RMSE-about-truth of a per-content estimator."""
    xs = np.arange(n + 1)
    ys = np.arange(m + 1)
    px = stats.binom.pmf(xs, n, p)
    py = stats.binom.pmf(ys, m, q)
    vals = np.array([[est(x, n, y, m) for y in ys] for x in xs])
    w = np.outer(px, py)
    truth = 2 * abs(p - q)
    mean = float((w * vals).sum())
    rmse = float(math.sqrt((w * (vals - truth) ** 2).sum()))
    return mean, rmse


def exact_content_coverage(n, m, p, q, alpha, kind="cp", k=1):
    """Exact coverage of the per-content |p - q| interval used inside the
    Delta interval for k contents (so at level alpha/(2k) per marginal for
    'cp', alpha/k per content for 'newcombe')."""
    xs = np.arange(n + 1)
    ys = np.arange(m + 1)
    px = stats.binom.pmf(xs, n, p)
    py = stats.binom.pmf(ys, m, q)
    t = abs(p - q)
    cov = 0.0
    for x in xs:
        for y in ys:
            if kind == "cp":
                a = alpha / (2 * k)
                l, h = abs_diff_range(*clopper_pearson(x, n, a), *clopper_pearson(y, m, a))
            else:
                l0, h0 = newcombe(x, n, y, m, alpha / k)
                if l0 > 0:
                    l, h = l0, h0
                elif h0 < 0:
                    l, h = -h0, -l0
                else:
                    l, h = 0.0, max(-l0, h0)
            if l - 1e-12 <= t <= h + 1e-12:
                cov += px[x] * py[y]
    return float(cov)
