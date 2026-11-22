"""Contextuality-by-Default estimators for a rank-4 cyclic system (LEAD-182).

Contents q0..q3, contexts c_k = (q_k, q_{k+1 mod 4}). In the generalised
Winograd layout of Lo, Sadrzadeh and Mansfield (2023): q0 = (p1, s1),
q1 = (p2, s2), q2 = (p1, a1), q3 = (p2, a2), so c0 = (s1, s2), c1 = (s2, a1),
c2 = (a1, a2), c3 = (a2, s1).

Each respondent sees one context and gives two binary answers, coded +1/-1
by a rule fixed in advance. A context's data are the counts of the four
answer pairs in the order (++, +-, -+, --).

The criterion (Kujala and Dzhafarov's cyclic-system theorem, as used in
LIT-264 and in Lo et al. 2023, eq. 3): the system is contextual iff

    Delta_C = s_odd(E) - (n - 2) - Delta > 0,

with E_k = <R_k R_{k+1}> in context k, s_odd the largest signed sum with an
odd number of minus signs, n = 4, and Delta = sum over contents of
|<R_q in one context> - <R_q in the other>|, the signalling (inconsistent
connectedness) the criterion discounts.
"""
from __future__ import annotations

import itertools

import numpy as np

N_CONTEXTS = 4
# Sign vectors with an odd number of -1 entries (8 of them for n = 4).
ODD_SIGNS = np.array([s for s in itertools.product((1, -1), repeat=4)
                      if np.prod(s) == -1], dtype=float)


def cells_from_moments(m_a: float, m_b: float, e: float) -> np.ndarray:
    """Cell probabilities (++, +-, -+, --) from two +/-1 means and their product mean."""
    p = np.array([1 + m_a + m_b + e,
                  1 + m_a - m_b - e,
                  1 - m_a + m_b - e,
                  1 - m_a - m_b + e]) / 4.0
    return p


def moments(counts: np.ndarray):
    """Means of first answer, second answer and product, from counts or probabilities.

    `counts` has last axis of length 4 (++, +-, -+, --); any leading axes are kept.
    """
    c = np.asarray(counts, dtype=float)
    tot = c.sum(axis=-1)
    pp, pm, mp, mm = (c[..., i] / tot for i in range(4))
    m_a = pp + pm - mp - mm
    m_b = pp - pm + mp - mm
    e = pp + mm - pm - mp
    return m_a, m_b, e


def system_moments(counts: np.ndarray, shrink: float = 0.0):
    """For a system (leading axes ..., 4 contexts, 4 cells) return E (...,4) and signalling Delta (...).

    Context k measures (q_k, q_{k+1}); so content q appears as the first
    variable of context q and the second variable of context q-1.

    shrink > 0 soft-thresholds each content's |difference| by shrink times
    its estimated standard error (needs counts, not probabilities). It
    trades the plug-in's upward bias at zero signalling for a downward one
    at small signalling; the simulation measures what that costs in size.
    """
    m_a, m_b, e = moments(counts)          # each (..., 4)
    first = m_a                            # <R_q> in context q
    second = np.roll(m_b, 1, axis=-1)      # <R_q> in context q-1
    d = np.abs(first - second)
    if shrink:
        n = np.asarray(counts, dtype=float).sum(axis=-1)
        se = np.sqrt(np.clip(1 - first ** 2, 0, None) / n
                     + np.clip(1 - second ** 2, 0, None) / np.roll(n, 1, axis=-1))
        d = np.clip(d - shrink * se, 0, None)
    delta = d.sum(axis=-1)
    return e, delta


def delta_c(counts: np.ndarray, signs: np.ndarray | None = None,
            shrink: float = 0.0) -> np.ndarray:
    """Delta_C for one or many systems.

    signs=None takes s_odd, the maximum over odd sign vectors (the criterion
    as stated). A fixed odd sign vector gives the preregistered statistic,
    which does not pay the upward bias of the maximum.
    """
    e, delta = system_moments(counts, shrink)
    if signs is None:
        s = (e[..., None, :] * ODD_SIGNS).sum(axis=-1).max(axis=-1)
    else:
        signs = np.asarray(signs, dtype=float)
        if np.prod(signs) != -1:
            raise ValueError("a fixed sign vector must have an odd number of minus signs")
        s = (e * signs).sum(axis=-1)
    return s - 2.0 - delta


def true_system(dc: float, signal: float, base: float = 0.0,
                signs=(1, 1, 1, -1)) -> np.ndarray | None:
    """A true model (4 contexts x 4 cells) with given Delta_C and signalling Delta.

    All |E_k| equal e = (2 + Delta + Delta_C)/4 with the given odd sign
    pattern; every content's marginal is base + Delta/8 in one of its two
    contexts and base - Delta/8 in the other, so the signalling sums to
    Delta. Returns None if the cells would be infeasible.
    """
    signs = np.asarray(signs, dtype=float)
    e = (2.0 + signal + dc) / 4.0
    if not 0 <= e <= 1:
        return None
    h = signal / 8.0
    P = np.empty((4, 4))
    for k in range(4):
        # content k as first variable of context k gets +h; content k+1 as
        # second variable of context k gets -h (it gets +h in its own context).
        P[k] = cells_from_moments(base + h, base - h, signs[k] * e)
    if (P < -1e-12).any():
        return None
    P = np.clip(P, 0, None)
    return P / P.sum(axis=1, keepdims=True)


def bootstrap_bounds(counts: np.ndarray, rng: np.random.Generator, B: int,
                     alphas, signs=None, shrink: float = 0.0) -> np.ndarray:
    """Percentile bootstrap quantiles of Delta_C, resampling respondents within each context.

    counts: (reps, 4, 4). Returns an array (len(alphas), reps) of quantiles.
    """
    counts = np.asarray(counts)
    n = counts.sum(axis=-1)                        # (reps, 4)
    phat = counts / n[..., None]
    reps = counts.shape[0]
    boot = np.empty((B, reps, 4, 4))
    for k in range(4):
        # Generator.multinomial broadcasts n and pvals over the leading axes.
        boot[:, :, k, :] = rng.multinomial(n[:, k], phat[:, k, :], size=(B, reps))
    stats = delta_c(boot, signs, shrink)           # (B, reps)
    return np.quantile(stats, np.asarray(alphas), axis=0)


def wald_bounds(counts: np.ndarray, z: float, signs) -> tuple[np.ndarray, np.ndarray]:
    """Delta-method one-sided bounds for the fixed-sign statistic.

    Per respondent in context k the statistic's influence is
    g = s_k x_a x_b - t_a x_a - t_b x_b, with t the sign of the content's
    marginal difference (taken as estimated; this is where the delta method
    fails near zero signalling, and the simulation measures how much).
    """
    counts = np.asarray(counts, dtype=float)
    signs = np.asarray(signs, dtype=float)
    n = counts.sum(axis=-1)
    m_a, m_b, e = moments(counts)
    first, second = m_a, np.roll(m_b, 1, axis=-1)
    t = np.sign(first - second)                    # for content q: + in context q, - in q-1
    t_first = t                                    # coefficient on x_a in context k (content k)
    t_second = -np.roll(t, -1, axis=-1)            # coefficient on x_b in context k (content k+1)
    # outcomes (x_a, x_b) per cell
    xa = np.array([1, 1, -1, -1.0])
    xb = np.array([1, -1, 1, -1.0])
    g = (signs[..., :, None] * (xa * xb)[None, :]
         - t_first[..., None] * xa - t_second[..., None] * xb)   # (..., 4, 4)
    p = counts / n[..., None]
    mean_g = (p * g).sum(-1)
    var_g = (p * g * g).sum(-1) - mean_g ** 2
    se = np.sqrt((var_g / n).sum(-1))
    est = delta_c(counts, signs)
    return est - z * se, est + z * se


def mixture(P1: np.ndarray, P2: np.ndarray, w: float = 0.5) -> np.ndarray:
    """The system observed when two subsystems (say, two label orders) are pooled."""
    return w * P1 + (1 - w) * P2


def absence_upper_bound(counts: np.ndarray, signs, alpha: float = 0.05) -> np.ndarray:
    """A conservative upper confidence bound for Delta_C, valid by construction.

    Bonferroni over two parts: an upper bound for sigma . E at alpha/2
    (normal approximation, the E_k independent across contexts), and a
    lower bound for the signalling, each content's |d| at least
    max(0, |d_hat| - z se) at alpha/8 apiece (since ||d_hat| - |d|| <= |d_hat - d|).
    With probability about 1 - alpha the true Delta_C is below the result,
    whatever the true signalling; the plug-in and soft-thresholded bounds
    have no such guarantee (summary.md). Absence is shown when it is below 0.
    """
    from statistics import NormalDist
    counts = np.asarray(counts, dtype=float)
    signs = np.asarray(signs, dtype=float)
    n = counts.sum(axis=-1)
    m_a, m_b, e = moments(counts)
    z1 = NormalDist().inv_cdf(1 - alpha / 2)
    z2 = NormalDist().inv_cdf(1 - alpha / 8)
    se_e = np.sqrt((np.clip(1 - e ** 2, 0, None) / n).sum(axis=-1))
    upper_s = (signs * e).sum(axis=-1) + z1 * se_e
    first, second = m_a, np.roll(m_b, 1, axis=-1)
    se_d = np.sqrt(np.clip(1 - first ** 2, 0, None) / n
                   + np.clip(1 - second ** 2, 0, None) / np.roll(n, 1, axis=-1))
    lower_delta = np.clip(np.abs(first - second) - z2 * se_d, 0, None).sum(axis=-1)
    return upper_s - 2.0 - lower_delta
