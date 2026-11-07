# scratch/formal/vipond_checks.py: checks Vipond (JMLR 2020) Example 3 / Figure 2 numbers against Definition 25, tests Proposition 28's printed identity against its w <-> 1/w swap, and tests Proposition 24 / 36 recovery of the rank invariant, including pairs equal in one coordinate
from fractions import Fraction as F
import itertools, random

# A module is a list of boxes (a, b, closed_top). closed_top=True: closed box [a,b] (the paper's Example 3 notation);
# False: half-open [a,b), the support of a finitely presented rectangle module (generators at a, relations at b).
def rank(M, p, q):
    """rank of M(p <= q) for a direct sum of box modules = number of boxes containing both p and q"""
    def inside(box, x):
        a, b, closed = box
        return all(a[i] <= x[i] and (x[i] <= b[i] if closed else x[i] < b[i]) for i in range(len(x)))
    return sum(1 for box in M if inside(box, p) and inside(box, q))

def landscape_brute(M, k, x, w, eps_grid=2000, emax=10):
    """Definition 25 by brute force: sup eps >= 0 such that beta^{x-h,x+h} >= k for all h >= 0 with max_i w_i h_i <= eps.
    For box modules x-h and x+h leave a box only as h grows, so the corner h_i = eps / w_i is the worst case and is the one tested."""
    best = F(0)
    for j in range(1, eps_grid + 1):
        e = F(emax) * j / eps_grid
        h = tuple(e / wi for wi in w)
        if rank(M, tuple(x[i] - h[i] for i in range(2)), tuple(x[i] + h[i] for i in range(2))) >= k:
            best = e
        else:
            break
    return best

def landscape_exact(M, k, x, w):
    """closed form for a sum of boxes: k-th largest of min_i w_i * min(x_i - a_i, b_i - x_i) over boxes containing x"""
    vals = sorted((min(w[i] * min(x[i] - a[i], b[i] - x[i]) for i in range(2)) for (a, b, cl) in M
                   if rank([(a, b, cl)], x, x) == 1), reverse=True)
    return vals[k - 1] if len(vals) >= k else F(0)

def pullback(M, c):
    """M o phi_c where phi_c(z) = (c_i z_i): box [a,b] becomes [a/c, b/c]"""
    return [(tuple(a[i] / c[i] for i in range(2)), tuple(b[i] / c[i] for i in range(2)), cl) for (a, b, cl) in M]

one = (F(1), F(1))
Mex = [((F(0),F(1)),(F(10),F(2)),True), ((F(4),F(1)),(F(6),F(2)),True)]
Nex = [((F(0),F(1)),(F(6),F(2)),True), ((F(4),F(1)),(F(10),F(2)),True)]
w = (F(1,10), F(1)); x = (F(5), F(3,2))
lM = landscape_brute(Mex, 1, x, w); lN = landscape_brute(Nex, 1, x, w)
print("Def 25 at (5,1.5), w=(1/10,1): lambda_w(M)=%s lambda_w(N)=%s (paper: 0.5 and 0.1)" % (lM, lN))
assert (lM, lN) == (F(1,2), F(1,10))

winv = tuple(1 / wi for wi in w)
# Printed Prop 28 last line: lambda_w(M)(k,x) = lambda_1(M o phi_w)(k, w^{-1} x)
printed = lambda M: landscape_brute(pullback(M, w), 1, tuple(winv[i] * x[i] for i in range(2)), one)
# Swapped version: lambda_w(M)(k,x) = lambda_1(M o phi_{w^{-1}})(k, w x)
swapped = lambda M: landscape_brute(pullback(M, winv), 1, tuple(w[i] * x[i] for i in range(2)), one)
print("printed Prop 28 gives M:%s N:%s ; swapped gives M:%s N:%s" % (printed(Mex), printed(Nex), swapped(Mex), swapped(Nex)))
assert swapped(Mex) == lM and swapped(Nex) == lN
# CONTROL (expected to fail to match): the printed identity does not reproduce the paper's own value for N
assert printed(Nex) != lN

# Random check of the swapped identity, and of the brute force against the closed form, on random half-open box modules
random.seed(1)
def rbox():
    a = (F(random.randint(0, 8)), F(random.randint(0, 8)))
    b = (a[0] + random.randint(1, 8), a[1] + random.randint(1, 8))
    return (a, b, False)
bad_printed = 0
for t in range(60):
    M = [rbox() for _ in range(3)]
    ww = (F(random.randint(1, 10), 10), F(1)) if random.random() < .5 else (F(1), F(random.randint(1, 10), 10))
    xx = (F(random.randint(0, 16), 2), F(random.randint(0, 16), 2))
    for k in (1, 2):
        d = landscape_brute(M, k, xx, ww, eps_grid=400, emax=8)
        s = landscape_brute(pullback(M, tuple(1/v for v in ww)), k, tuple(ww[i]*xx[i] for i in range(2)), one, eps_grid=400, emax=8)
        p = landscape_brute(pullback(M, ww), k, tuple(xx[i]/ww[i] for i in range(2)), one, eps_grid=400, emax=8)
        assert d == s, (M, ww, xx, k, d, s)
        e = landscape_exact(M, k, xx, ww)
        assert abs(d - e) <= F(8, 400), (M, ww, xx, k, d, e)  # brute force agrees with the closed form to grid resolution
        bad_printed += (d != p)
print("random trials: swapped identity always agrees; printed identity disagreed in", bad_printed, "of 120")

# Proposition 24 / 36: recover beta^{a,b} from weighted landscapes of a finitely presented (half-open box) module.
def recover(M, a, b, delta=F(1, 1000)):
    """rescale so (a, b) lies on a slope-1 line, then use Prop 24's formula with a small delta.
    For a pair equal in some coordinate, first replace b by b + delta*1 (right-continuity of f.p. modules)."""
    if any(a[i] == b[i] for i in range(2)):
        b = tuple(b[i] + delta for i in range(2))
    d = tuple(b[i] - a[i] for i in range(2)); m = max(d)
    ww = tuple(m / d[i] / max(m / d[j] for j in range(2)) for i in range(2))  # unit weight, w_i proportional to 1/d_i
    r = ww[0] * d[0]  # = ww[1]*d[1]: the rescaled pair is (w a, w a + r 1)
    assert ww[0] * d[0] == ww[1] * d[1]
    delta = r / 1000  # Prop 24's delta is taken small in the rescaled coordinates
    c = tuple(a[i] + (r + delta) / 2 / ww[i] for i in range(2))  # point whose rescaled image is w a + ((r+delta)/2) 1
    k = 0
    while landscape_exact(M, k + 1, c, ww) >= (r + delta) / 2:
        k += 1
        if k > 10: break
    return k
M = [((F(0),F(0)),(F(4),F(3)),False), ((F(1),F(1)),(F(3),F(5)),False), ((F(2),F(0)),(F(6),F(2)),False)]
tests = [((F(1),F(1)),(F(2),F(2))), ((F(2),F(1)),(F(2),F(2))), ((F(1),F(1)),(F(2),F(4))), ((F(2),F(0)),(F(5),F(1))), ((F(0),F(0)),(F(3),F(0)))]
for a, b in tests:
    print("beta^{%s,%s}: true %d, recovered %d" % (tuple(map(str,a)), tuple(map(str,b)), rank(M, a, b), recover(M, a, b)))
    assert rank(M, a, b) == recover(M, a, b)
# CONTROL (expected to fail): without the right-continuity step, a pair equal in one coordinate gives no unit weight
a, b = (F(2),F(1)), (F(2),F(2))
try:
    d = tuple(b[i]-a[i] for i in range(2)); _ = tuple(max(d)/d[i] for i in range(2))
    raise SystemExit("control did not fail")
except ZeroDivisionError:
    print("control: pair (2,1)<=(2,2) admits no rescaling onto a slope-1 line (division by zero), as expected")
print("ALL OK")
