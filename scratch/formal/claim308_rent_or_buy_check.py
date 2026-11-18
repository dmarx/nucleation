"""Second check of CLAIM-308's bound (status review of 2026-11-18).

Setting (CLAIM-308): filing costs F once; each use costs c_r if the argument
is reconstructed, a = c_a + u once it is filed; d = c_r - a > 0 is the
overpayment per use. A deterministic rule without foresight is a filing use
m >= 1: reconstruct uses 1..m-1, file at use m (paying F + a there). Reuse
stops after n uses, unknown in advance. Hindsight pays min(n*c_r, F + n*a).

Checks, each exact over rationals:
  1. Upper bound. The break-even rule, k = floor(F/d), m = k + 1, is within
     2 - a/c_r of hindsight for every n.
  2. Lower bound. For every m, the adversary stopping at n = m forces a ratio
     of at least (2 - a/c_r) - 1/K, K = floor(F/d) (K >= 1); so no
     deterministic rule guarantees materially better once F/d is large.
  3. Tightness. The break-even rule reaches 2 - a/c_r - O(1/K) at n = k + 1.
Controls (each must FAIL the bound it is set against, or the checks above
would pass vacuously):
  C1. The "reached" rounding, m = ceil(F/d) + 1, exceeds 2 on some instance
      with a = 0 and F not a multiple of d (CLAIM-308's rounding remark).
  C2. Filing at once, m = 1, exceeds 2 - a/c_r when F is many overpayments.
"""
from fractions import Fraction as Q
from math import floor, ceil
import random


def cost(m, n, F, cr, a):
    if n < m:
        return n * cr
    return (m - 1) * cr + F + (n - m + 1) * a


def opt(n, F, cr, a):
    return min(n * cr, F + n * a)


def ratio(m, n, F, cr, a):
    return Q(cost(m, n, F, cr, a)) / Q(opt(n, F, cr, a))


def rand_instance(rng):
    cr = Q(rng.randint(2, 40))
    a = Q(rng.randint(0, int(cr) - 1)) * Q(rng.randint(1, 9), 10)
    d = cr - a
    F = Q(rng.randint(1, 4000), rng.randint(1, 20))
    return F, cr, a, d


def main():
    rng = random.Random(20261118)
    worst_excess = None
    lb_fail = 0
    tight_gap = []
    N = 20000
    for _ in range(N):
        F, cr, a, d = rand_instance(rng)
        bound = 2 - a / cr
        k = floor(F / d)
        m = k + 1
        # 1. upper bound over n up to well past the filing use
        for n in range(1, m + 30):
            r = ratio(m, n, F, cr, a)
            ex = r - bound
            worst_excess = ex if worst_excess is None or ex > worst_excess else worst_excess
        # 2. lower bound over all m up to 3K+3 (larger m only raises the ratio)
        K = k
        if K >= 1:
            for mm in range(1, 3 * K + 4):
                r = ratio(mm, mm, F, cr, a)
                if r < bound - Q(1, K):
                    lb_fail += 1
            # 3. tightness of break-even at n = k + 1
            tight_gap.append(float(bound - ratio(m, m, F, cr, a)) * K)
    print(f"1. break-even rule, {N} instances: max(ratio - (2 - a/c_r)) = {float(worst_excess):.3g}"
          f"  -> {'PASS' if worst_excess <= 0 else 'FAIL'}")
    print(f"2. adversary lower bound (2 - a/c_r) - 1/K violated {lb_fail} times"
          f"  -> {'PASS' if lb_fail == 0 else 'FAIL'}")
    print(f"3. tightness: max K*(bound - ratio at n=k+1) = {max(tight_gap):.3g} (bounded, so gap is O(1/K))")

    # C1: reached-rounding exceeds 2
    c1 = Q(0)
    for _ in range(5000):
        cr = Q(rng.randint(2, 40)); a = Q(0); d = cr
        F = Q(rng.randint(1, 400), rng.randint(2, 7))
        if (F / d).denominator == 1:
            continue
        m = ceil(F / d) + 1
        c1 = max(c1, max(ratio(m, n, F, cr, a) for n in range(1, m + 3)))
    print(f"C1. 'reached' rounding, a = 0: max ratio = {float(c1):.3f}  -> {'control fires' if c1 > 2 else 'CONTROL DID NOT FIRE'}")
    # C2: filing at once with F = 50 overpayments
    cr, a = Q(10), Q(2); F = 50 * (cr - a)
    r = ratio(1, 1, F, cr, a)
    print(f"C2. filing at once, F = 50d: ratio at n = 1 = {float(r):.1f} vs bound {float(2 - a/cr):.2f}"
          f"  -> {'control fires' if r > 2 - a / cr else 'CONTROL DID NOT FIRE'}")


if __name__ == "__main__":
    main()
