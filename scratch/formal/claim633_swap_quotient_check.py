"""Check of CLAIM-633 (status review of 2026-11-20).

Network f = u1 v1 + u2 v2, weights >= 0; resource R = (u1 + v1 + u2 + v2)/2;
swap s(u1, v1, u2, v2) = (u2, v2, u1, v1); S_B = {f = 1, R <= B}; p = u2 v2.
Checks, for budgets B in [1, sqrt 2):
  1. s preserves f and R exactly (rationals).
  2. Every sampled point of S_B has p in [0, p_B] or [1 - p_B, 1], with
     h(p_B) = B, p_B < 1/2: two pieces separated by the gap (p_B, 1 - p_B),
     exchanged by s (p -> 1 - p).
  3. The claim's retraction joins each sampled point of the lower piece to
     a = (1, 1, 0, 0) inside S_B: f stays 1 and R never rises along it.
  4. B = 1 admits only a and b among balanced points; B < 1 admits none.
Controls (each must fire):
  C1. B = 1.5 >= sqrt 2: the balanced point at p = 1/2 is in S_B, so the gap
      closes (one piece) -- the detector in 2 must report a point in the gap.
  C2. A resource the swap does not preserve, R' = (2 u1 + 2 v1 + u2 + v2)/2:
      check 1 must fail for it.
  C3. A wrong path, the straight segment from the point to a: f must leave 1
      somewhere, so the f-check in 3 is discriminating.
Run: python3 -I scratch/formal/claim633_swap_quotient_check.py
"""
import math
import random
from fractions import Fraction as Q

random.seed(633)
h = lambda p: math.sqrt(1 - p) + math.sqrt(p)
f = lambda w: w[0] * w[1] + w[2] * w[3]
R = lambda w: (w[0] + w[1] + w[2] + w[3]) / 2
Rp = lambda w: (2 * w[0] + 2 * w[1] + w[2] + w[3]) / 2
swap = lambda w: (w[2], w[3], w[0], w[1])


def p_B(B):  # root of h(p) = B on [0, 1/2]
    lo, hi = 0.0, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if h(mid) <= B else (lo, mid)
    return lo


def sample():
    p = random.random() ** random.choice([1, 3, 6])
    if random.random() < 0.5:
        p = 1 - p
    u1 = math.exp(random.uniform(-1.2, 1.2)) * math.sqrt(1 - p)
    u2 = math.exp(random.uniform(-1.2, 1.2)) * math.sqrt(p)
    w = (u1, (1 - p) / u1 if u1 else 0.0, u2, p / u2 if u2 else 0.0)
    return w, p


# 1. exact preservation
ok1 = True; c2_fired = False
for _ in range(2000):
    w = tuple(Q(random.randint(0, 50), random.randint(1, 20)) for _ in range(4))
    ok1 &= f(swap(w)) == f(w) and R(swap(w)) == R(w)
    c2_fired |= Rp(swap(w)) != Rp(w)
assert ok1, "check 1 failed"
assert c2_fired, "control C2 did not fire"


def retraction_ok(w, p, B, steps=200, straight=False):
    """Follow the claim's path (or a straight segment) to a; return
    (f stays 1, R never above B and nonincreasing)."""
    pts = []
    if straight:
        a = (1.0, 1.0, 0.0, 0.0)
        pts = [tuple((1 - t) * x + t * y for x, y in zip(w, a)) for t in (i / steps for i in range(steps + 1))]
    else:
        s1, s2 = math.sqrt(1 - p), math.sqrt(p)
        for i in range(steps + 1):  # stage 1: geometric slide along each hyperbola to its balanced point
            t = i / steps
            u1 = w[0] ** (1 - t) * s1 ** t
            if p > 0:
                u2 = w[2] ** (1 - t) * s2 ** t; v2 = p / u2
            else:  # p = 0: shrink the nonzero one of u2, v2
                u2, v2 = w[2] * (1 - t), w[3] * (1 - t)
            pts.append((u1, (1 - p) / u1, u2, v2))
        for i in range(steps + 1):  # stage 2: along balanced points, p down to 0
            q = p * (1 - i / steps)
            pts.append((math.sqrt(1 - q), math.sqrt(1 - q), math.sqrt(q), math.sqrt(q)))
    f_ok = all(abs(f(x) - 1) < 1e-9 for x in pts)
    Rs = [R(x) for x in pts]
    r_ok = all(r <= B + 1e-9 for r in Rs) and all(b <= a + 1e-9 for a, b in zip(Rs, Rs[1:]))
    end_ok = max(abs(x - y) for x, y in zip(pts[-1], (1.0, 1.0, 0.0, 0.0))) < 1e-9
    return f_ok, r_ok and end_ok


in_set = 0; gap_hits = 0; swap_ok = True; retr_ok = True; c3_fired = False
for B in (1.0001, 1.05, 1.1, 1.2, 1.3, 1.4, 1.414):
    pb = p_B(B); assert pb < 0.5
    for _ in range(4000):
        w, p = sample()
        if R(w) > B:
            continue
        in_set += 1
        gap_hits += pb + 1e-12 < p < 1 - pb - 1e-12
        sw = swap(w)
        swap_ok &= abs(f(sw) - 1) < 1e-12 and R(sw) <= B + 1e-12 and abs(sw[2] * sw[3] - (1 - p)) < 1e-12
        if p <= 0.5:
            fo, ro = retraction_ok(w, p, B)
            retr_ok &= fo and ro
            fs, _ = retraction_ok(w, p, B, straight=True)
            c3_fired |= not fs
print("points of S_B sampled:", in_set, "in the gap:", gap_hits, "swap ok:", swap_ok, "retraction ok:", retr_ok)
assert in_set > 1000 and gap_hits == 0 and swap_ok and retr_ok, "checks 2-3 failed"
assert c3_fired, "control C3 did not fire"

# 4. B = 1 and B < 1 among balanced points (R = h(p) there, the minimum for each p)
ps = [i / 10000 for i in range(10001)]
assert [p for p in ps if h(p) <= 1 + 1e-12] == [0.0, 1.0]
assert not [p for p in ps if h(p) <= 0.999]

# C1: at B = 1.5 >= sqrt 2 the gap closes: points with p near 1/2 enter S_B,
# so the same gap detector (using the gap of B = 1.414) must report hits.
pb = p_B(1.414); c1_hits = 0
for _ in range(20000):
    w, p = sample()
    if R(w) <= 1.5 and pb + 1e-12 < p < 1 - pb - 1e-12:
        c1_hits += 1
print("C1: points of S_1.5 in the gap of B = 1.414:", c1_hits)
assert c1_hits > 0, "control C1 did not fire"
print("claim633 swap-quotient check: all passed, controls C1-C3 fired")
