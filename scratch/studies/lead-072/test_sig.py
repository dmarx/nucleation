import itertools
import math
import os
import sys

import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sig  # noqa: E402


def test_u2_unbiased_exactly():
    for n, m, p, q in [(2, 3, 0.3, 0.7), (5, 4, 0.5, 0.5), (10, 7, 0.1, 0.25)]:
        xs, ys = np.arange(n + 1), np.arange(m + 1)
        w = np.outer(stats.binom.pmf(xs, n, p), stats.binom.pmf(ys, m, q))
        v = np.array([[sig.u2(x, n, y, m) for y in ys] for x in xs])
        assert abs((w * v).sum() - (p - q) ** 2) < 1e-12


def test_plug_one_occurrence_values():
    # LIT-851 / CLAIM-235's worked case: one occurrence per context, p = q = 1/2,
    # per content the plug-in is 0 or 2 with mean 1; two contents give mean 2.
    mean, _ = sig.exact_moments(sig.plug, 1, 1, 0.5, 0.5)
    assert abs(mean - 1.0) < 1e-12


def test_abs_diff_range():
    assert sig.abs_diff_range(0.1, 0.3, 0.5, 0.6) == (0.2, 0.5)
    lo, hi = sig.abs_diff_range(0.1, 0.5, 0.4, 0.6)
    assert lo == 0.0 and abs(hi - 0.5) < 1e-12


def test_clopper_pearson_known():
    lo, hi = sig.clopper_pearson(0, 10, 0.05)
    assert lo == 0.0 and abs(hi - (1 - 0.025 ** (1 / 10))) < 1e-9


def test_box_contains_plugin():
    c = [(3, 10, 7, 12), (1, 10, 0, 12)]
    lo, hi = sig.box_interval(c)
    est = sum(sig.plug(*t) for t in c)
    assert lo <= est <= hi
    assert 0 <= lo and hi <= 4


def test_box_one_occurrence_uninformative():
    lo, hi = sig.box_interval([(1, 1, 0, 1), (0, 1, 0, 1)])
    assert lo == 0.0 and hi > 3.9


def test_newcombe_matches_published_example():
    # Newcombe (1998) Table II example: 56/70 vs 48/80, 95% interval 0.0528 to 0.3339
    lo, hi = sig.newcombe(56, 70, 48, 80, 0.05)
    assert abs(lo - 0.0524) < 0.002 and abs(hi - 0.3339) < 0.002


def test_nosig_test_fisher_size_exact_small():
    # exact size of one content's Fisher test is <= alpha on a grid
    n = m = 8
    for p in np.linspace(0.05, 0.95, 7):
        xs = np.arange(n + 1)
        w = np.outer(stats.binom.pmf(xs, n, p), stats.binom.pmf(xs, m, p))
        rej = np.array([[sig.content_pvalue(x, n, y, m) <= 0.05 for y in xs] for x in xs])
        assert (w * rej).sum() <= 0.05 + 1e-12


def test_exact_coverage_cp_at_least_nominal():
    for n, m, p, q in itertools.product([3, 10], [4], [0.2, 0.5], [0.5, 0.9]):
        cov = sig.exact_content_coverage(n, m, p, q, 0.05, "cp", k=1)
        assert cov >= 0.95 - 1e-9
