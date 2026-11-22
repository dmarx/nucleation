"""LEAD-061: Golub & Jackson (2010) Proposition 2 with several closed groups.

Checks three things.

1. Theorem 3's influence vector: s is the left unit eigenvector on EACH
   minimal closed group, normalized to sum to 1 there, and 0 elsewhere.
   `influence` computes it; `limit_beliefs` iterates DeGroot and the test
   checks Theorem 3 (iv)-(v) against it.
2. The counterexample to Proposition 2's "if" direction under
   Definition 3 (plim of the max over all agents): m groups of size k,
   equal weights inside each, Bernoulli(1/2) signals. s_1 = 1/k, and
   P(max_i |p_i(inf) - 1/2| >= eps) = 1 - (1 - q_k(eps))^m exactly, with
   q_k(eps) the binomial tail of one group's mean.
3. Contrasts in which the max does go to 0: a bounded number of groups,
   and groups whose size grows faster than log m.

Run:  python3 -I gj_closed_groups.py   (prints the tables in README.md)
"""
import math
import sys

import numpy as np


# ---------- Theorem 3 ----------

def _reach(T):
    n = T.shape[0]
    A = (T > 0).astype(int)
    R = np.eye(n, dtype=int) | A
    for _ in range(int(math.ceil(math.log2(max(n, 2)))) + 1):
        R = ((R @ R) > 0).astype(int)
    return R.astype(bool)


def minimal_closed_groups(T):
    """Minimal closed groups: strongly connected classes with no edge out."""
    n = T.shape[0]
    R = _reach(T)
    seen, groups = set(), []
    for i in range(n):
        if i in seen:
            continue
        cls = [j for j in range(n) if R[i, j] and R[j, i]]
        seen.update(cls)
        reach_i = set(np.nonzero(R[i])[0])
        if reach_i == set(cls):
            groups.append(sorted(cls))
    return groups


def influence(T):
    """Theorem 3's s: per minimal closed group B, left eigenvector of T_B
    for eigenvalue 1 with entries summing to 1 on B; 0 off the groups."""
    n = T.shape[0]
    s = np.zeros(n)
    for B in minimal_closed_groups(T):
        TB = T[np.ix_(B, B)]
        w, V = np.linalg.eig(TB.T)
        v = np.real(V[:, np.argmin(np.abs(w - 1))])
        s[B] = v / v.sum()
    return s


def limit_beliefs(T, p, t=4000):
    x = np.array(p, dtype=float)
    for _ in range(t):
        x = T @ x
    return x


# ---------- the counterexample, exactly ----------

def group_miss_prob(k, eps):
    """P(|mean of k Bernoulli(1/2) - 1/2| >= eps): exact for k <= 200,
    scipy's binomial tails beyond."""
    lo = math.floor(k * (0.5 - eps) + 1e-9)   # j <= lo misses low
    hi = math.ceil(k * (0.5 + eps) - 1e-9)    # j >= hi misses high
    if k <= 200:
        tot = sum(math.comb(k, j) for j in range(k + 1) if j <= lo or j >= hi)
        return tot / 2 ** k
    from scipy.stats import binom
    q = (binom.cdf(lo, k, 0.5) if lo >= 0 else 0.0) + binom.sf(hi - 1, k, 0.5)
    return min(1.0, float(q))


def any_group_miss_prob(m, k, eps):
    """P(max over m independent groups of size k misses by >= eps)."""
    q = group_miss_prob(k, eps)
    if q >= 1:
        return 1.0
    # 1 - (1-q)^m, stable for huge m (m may exceed the float range)
    log_rate = math.log10(m) + math.log10(-math.log1p(-q)) if q > 0 else -math.inf
    if log_rate > 300:
        return 1.0
    return -math.expm1(float(m) * math.log1p(-q))


def log10_group_miss_prob(k, eps):
    """log10 q_k(eps), computed in log space so tiny tails do not underflow."""
    if k <= 200:
        q = group_miss_prob(k, eps)
        return math.log10(q) if q > 0 else -math.inf
    from scipy.stats import binom
    from scipy.special import logsumexp
    lo = math.floor(k * (0.5 - eps) + 1e-9)
    hi = math.ceil(k * (0.5 + eps) - 1e-9)
    parts = [binom.logsf(hi - 1, k, 0.5)]
    if lo >= 0:
        parts.append(binom.logcdf(lo, k, 0.5))
    return float(logsumexp(parts)) / math.log(10)


def log10_expected_misses(m, k, eps):
    """log10 of m * q_k(eps): the expected number of groups that miss,
    which bounds P(some group misses) above (union bound)."""
    return math.log10(m) + log10_group_miss_prob(k, eps)


def audit_family(log10_n):
    """n agents, k = ceil(sqrt(ln n)), m = n // k groups (n given by log10)."""
    ln_n = log10_n * math.log(10)
    k = math.ceil(math.sqrt(ln_n))
    m = 10 ** log10_n // k
    return m, k


def hoeffding_bound(m, k, eps):
    """Union bound with Hoeffding: m * 2 exp(-2 eps^2 k), for equal weights."""
    return min(1.0, m * 2 * math.exp(-2 * eps * eps * k))


# ---------- Monte Carlo on an actual T ----------

def several_group_matrix(m, k, n_transient, rng):
    """m closed groups of size k with random positive, aperiodic weights,
    plus transient agents who listen to random members of M and to each other."""
    n = m * k + n_transient
    T = np.zeros((n, n))
    for g in range(m):
        idx = list(range(g * k, (g + 1) * k))
        W = rng.random((k, k)) + 0.05
        T[np.ix_(idx, idx)] = W / W.sum(1, keepdims=True)
    for i in range(m * k, n):
        targets = rng.choice(n, size=min(4, n), replace=False)
        T[i, targets] = rng.random(len(targets)) + 0.05
        if not np.any(T[i, : m * k] > 0):
            T[i, rng.integers(0, m * k)] = 0.5
        T[i] /= T[i].sum()
    return T


def mc_max_dev(m, k, eps, reps, rng):
    """Monte Carlo of P(max_i |p_i(inf) - 1/2| >= eps), equal weights,
    using Theorem 3: group consensus = group mean."""
    hits = 0
    for _ in range(reps):
        p = rng.integers(0, 2, size=(m, k))
        dev = np.abs(p.mean(1) - 0.5).max()
        hits += dev >= eps - 1e-12
    return hits / reps


def main():
    out = sys.stdout
    rng = np.random.default_rng(61)

    out.write("## 1. Theorem 3 on a several-group T (m=3 groups of 4, 3 transient)\n\n")
    T = several_group_matrix(3, 4, 3, rng)
    s = influence(T)
    p = rng.random(T.shape[0])
    lim = limit_beliefs(T, p)
    groups = minimal_closed_groups(T)
    out.write(f"minimal closed groups: {groups}\n")
    out.write(f"sum of s per group: {[round(s[B].sum(), 12) for B in groups]}; total {s.sum():.6f}\n")
    out.write(f"s_1 = {s.max():.4f}\n")
    for B in groups:
        out.write(f"group {B}: s_B p_B = {s[B] @ p[B]:.6f}, limits {np.round(lim[B], 6)}\n")
    out.write(f"transient limits: {np.round(lim[12:], 6)}\n\n")

    out.write("## 2. Audit family: k = ceil(sqrt(ln n)), m = n // k, Bernoulli(1/2)\n\n")
    out.write("| log10 n | k | s_1 = 1/k | log10 E[# groups at 0 or 1] | P(some group at 0 or 1) | P(max dev >= 0.25) |\n")
    out.write("|---|---|---|---|---|---|\n")
    for L in (1, 2, 4, 6, 10, 20, 50, 100, 200, 400, 1000):
        m, k = audit_family(L)
        p_half = any_group_miss_prob(m, k, 0.5)
        p_q = any_group_miss_prob(m, k, 0.25)
        e = log10_expected_misses(m, k, 0.5)
        out.write(f"| {L} | {k} | {1/k:.3f} | {e:.1f} | {p_half:.6f} | {p_q:.6f} |\n")
    out.write("\nk grows like sqrt(ln n) so s_1 -> 0; m * 2^(1-k) -> infinity, so the\n"
              "probability that some group's consensus is 0 or 1 (miss by 1/2) tends to 1.\n\n")

    out.write("## 3. Contrasts in which the max does go to 0 (eps = 0.1)\n\n")
    out.write("| case | log10 n | m | k | s_1 | P(max dev >= 0.1), exact | log10 E[# groups missing] |\n|---|---|---|---|---|---|---|\n")
    for L in (2, 3, 4, 5):
        n = 10 ** L
        m, k = 3, n // 3
        out.write(f"| 3 groups | {L} | {m} | {k} | {1/k:.2e} | {any_group_miss_prob(m, k, 0.1):.3e} | {log10_expected_misses(m, k, 0.1):.1f} |\n")
    for L in (2, 5, 10, 20, 50, 100, 200):
        n = 10 ** L
        # k ~ (ln n)^2: grows faster than ln m
        k = math.ceil(math.log(n) ** 2)
        m = max(1, n // k)
        out.write(f"| k = (ln n)^2 | {L} | 10^{math.log10(m):.1f} | {k} | {1/k:.2e} | {any_group_miss_prob(m, k, 0.1):.3e} | {log10_expected_misses(m, k, 0.1):.1f} |\n")
    out.write("\n")

    out.write("## 4. Monte Carlo check of section 2 (eps = 0.5)\n\n")
    out.write("| m | k | exact | Monte Carlo (2000 reps) |\n|---|---|---|---|\n")
    for m, k in ((20, 3), (200, 4), (2000, 5)):
        out.write(f"| {m} | {k} | {any_group_miss_prob(m, k, 0.5):.4f} | {mc_max_dev(m, k, 0.5, 2000, rng):.4f} |\n")


if __name__ == "__main__":
    main()
