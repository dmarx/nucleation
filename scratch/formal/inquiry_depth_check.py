"""scratch/formal/inquiry_depth_check.py

Rebuilds the checks of CLAIM-1008 (the first-order condition for the best
depth of inquiry before execution) and CLAIM-1203 (how the best depth moves
with the deadline), from the entries' text alone. The filer's scripts were
not kept. Written at the reruns of 2026-11-25 by a session other than the
claims' filer. Run: python3 -I this file. Standard library only.

Model (CLAIM-1008, A52 section 3): P(k) = p(k) F(H - t(k)), with
p(k) = 1 - exp(-k), t(k) = k, grid search over k in steps of 0.01.
"""
import math

STEP = 0.01   # CLAIM-1203's grid; CLAIM-1008's k* = 1.900 implies 0.001


def Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def phi(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def F_normal(h):
    return Phi((h - 3.0) / 0.7)


def f_normal(h):
    return phi((h - 3.0) / 0.7) / 0.7


def F_mix(h):
    return 0.5 * Phi((h - 1.0) / 0.3) + 0.5 * Phi((h - 6.0) / 0.3)


p = lambda k: 1.0 - math.exp(-k)
dp = lambda k: math.exp(-k)
t = lambda k: k
dt = lambda k: 1.0


def P(k, H, F):
    return p(k) * F(H - t(k))


def argmax(H, F, step=STEP):
    n = int(round(H / step))
    best = max(range(1, n + 1), key=lambda i: P(i * step, H, F))
    k = best * step
    return round(k, 3), P(k, H, F)


def foc_sides(k, H):
    """Left p'/p and right t' F'/F of CLAIM-1008's condition."""
    h = H - t(k)
    return dp(k) / p(k), dt(k) * f_normal(h) / F_normal(h)


def golden_max(H, lo, hi):
    """A refinement of the grid optimum, to test the condition at the true
    interior maximizer (the grid point is within STEP of it)."""
    g = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    for _ in range(200):
        c, d = b - g * (b - a), a + g * (b - a)
        if P(c, H, F_normal) > P(d, H, F_normal):
            b = d
        else:
            a = c
    return (a + b) / 2


def check_table():
    # A52 section 2: ten days, five to carry out.
    rows = {"Rapid": 2, "Extended": 6, "Exhaustive": 9}
    left = {r: 10 - d for r, d in rows.items()}
    assert left == {"Rapid": 8, "Extended": 4, "Exhaustive": 1}
    assert [r for r, l in left.items() if l >= 5] == ["Rapid"]
    print("1008 table: days left 8, 4, 1; only the rapid inquiry leaves the five days")


def check_derivative():
    # P'(k) = p' F(H - t) - p F'(H - t) t', against a central difference.
    for H in (4, 6, 10):
        for k in (0.5, 1.3, 2.7):
            h = H - t(k)
            ana = dp(k) * F_normal(h) - p(k) * f_normal(h) * dt(k)
            e = 1e-6
            num = (P(k + e, H, F_normal) - P(k - e, H, F_normal)) / (2 * e)
            assert abs(ana - num) < 1e-7, (H, k, ana, num)
    print("1008 derivative: analytic P' agrees with a central difference to 1e-7")


def check_condition():
    print("1008 condition at the grid maximizer (sides p'/p and t'F'/F):")
    for H in (4, 5, 6, 8, 10, 14):
        k, _ = argmax(H, F_normal, step=0.001)
        ks = golden_max(H, max(STEP, k - 0.05), k + 0.05)
        l, r = foc_sides(ks, H)
        assert abs(l - r) < 5e-5, (H, ks, l, r)
        lg, rg = foc_sides(k, H)
        assert abs(lg - rg) < 1e-3, (H, k, lg, rg)
        print(f"  H = {H:>2}: grid k* = {k:.3f} (refined {ks:.4f}); "
              f"sides at refined {l:.4f} {r:.4f}; at grid point {lg:.4f} {rg:.4f}")
    k6, _ = argmax(6, F_normal, step=0.001)
    l, r = foc_sides(k6, 6)
    assert k6 == 1.900 and round(l, 3) == 0.176 and round(r, 3) == 0.176, (k6, l, r)


def control_condition():
    """Negative control: away from the optimum the two sides differ."""
    for H, k in ((6, 1.0), (6, 3.0), (10, 2.0)):
        l, r = foc_sides(k, H)
        assert abs(l - r) > 0.05, (H, k, l, r)
    print("1008 control: at k = 1.0 and 3.0 (H = 6) and 2.0 (H = 10) the sides differ by > 0.05")


def logF_second(F, h, e=1e-3):
    return (math.log(F(h + e)) - 2 * math.log(F(h)) + math.log(F(h - e))) / (e * e)


def check_1203_normal():
    want = {4: 0.77, 5: 1.27, 6: 1.90, 8: 3.35, 10: 4.93, 14: 8.25}
    got = {H: argmax(H, F_normal)[0] for H in want}
    assert got == want, got
    print("1203 normal F: k* =", ", ".join(f"{got[H]:.2f}" for H in want),
          "at H = 4, 5, 6, 8, 10, 14")
    # log-concavity of the normal F, hence a nonnegative cross-partial
    # analytic (log F)'' = (f' F - f^2) / F^2, with f' = -(h - 3)/0.7^2 f
    def logF2(h):
        F, f = F_normal(h), f_normal(h)
        return (-(h - 3.0) / 0.49 * f * F - f * f) / (F * F)
    assert all(logF2(h / 10) < 0 for h in range(0, 140))
    # Topkis: the maximizer never falls as H rises, on a fine H grid
    ks = [argmax(H / 20, F_normal)[0] for H in range(40, 281)]
    assert all(b >= a for a, b in zip(ks, ks[1:])), "k* fell with H under a log-concave F"
    print("1203 normal F: (log F)'' < 0 on h in [0, 14); k* nondecreasing over H = 2.00..14.00 in steps of 0.05")


def check_1203_mixture():
    k70, P70 = argmax(7.0, F_mix)
    k705, P705 = argmax(7.05, F_mix)
    k75, _ = argmax(7.5, F_mix)
    k8, _ = argmax(8.0, F_mix)
    print(f"1203 mixture F: H = 7.0 k* = {k70:.2f} (P = {P70:.3f}); H = 7.05 k* = {k705:.2f} "
          f"(P = {P705:.3f}); H = 7.5 k* = {k75:.2f}; H = 8 k* = {k8:.2f}")
    assert (k70, round(P70, 3)) == (5.02, 0.496), (k70, P70)
    assert (k705, round(P705, 3)) == (0.90, 0.502), (k705, P705)
    assert (k75, k8) == (1.20, 1.58), (k75, k8)
    # the cross-partial changes sign: log F convex somewhere after the plateau
    assert any(logF_second(F_mix, h / 100) > 0 for h in range(200, 700))
    # rises to 7.0 first
    ks = [argmax(H / 100, F_mix)[0] for H in range(600, 701, 5)]
    assert all(b >= a for a, b in zip(ks, ks[1:])), ks
    Hs = [7.0 + i / 1000 for i in range(51)]
    kj = [argmax(H, F_mix)[0] for H in Hs]
    jump = next(H for H, a, b in zip(Hs[1:], kj, kj[1:]) if b < a - 2)
    assert abs(jump - 7.04) < 0.006, jump
    print(f"1203 mixture F: k* first drops below 2 at H = {jump:.3f}")
    print("1203 mixture F: k* rises over H = 6.00..7.00; (log F)'' > 0 on part of h in (2, 7); "
          "the drop at about 7.04 reproduces")


def main():
    check_table()
    check_derivative()
    check_condition()
    control_condition()
    check_1203_normal()
    check_1203_mixture()
    print("checks pass")


if __name__ == "__main__":
    main()
