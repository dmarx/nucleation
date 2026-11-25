"""scratch/formal/maintained_nuclei_check.py

Rebuilds the checks of CLAIM-1195 (the standing cost of holding a nucleus
ready in the linear model dc/dt = a u - d c, and the threshold that appears
when building capability needs capability, dc/dt = a u c^2/(c^2 + K^2) - d c),
from the entry's text alone. The filer's script was not kept. Written at the
reruns of 2026-11-25 by a session other than the claim's filer.
Run: python3 -I this file. Standard library only. Euler steps of 0.01.
"""
import math
import random

DT = 0.01
A, D, K = 1.0, 0.1, 1.0


def run(c, u, T, sig=False):
    for _ in range(int(round(T / DT))):
        g = c * c / (c * c + K * K) if sig else 1.0
        c += DT * (A * u * g - D * c)
    return c


def roots(u):
    disc = (A * u) ** 2 - 4 * D * D * K * K
    if disc < 0:
        return None
    r = math.sqrt(disc)
    return (A * u - r) / (2 * D), (A * u + r) / (2 * D)


def check_linear():
    for u, target in ((0.05, 0.5), (0.2, 2.0)):
        for c0 in (0.0, 1.0, 5.0):
            c = run(c0, u, 200)
            assert abs(c - target) < 1e-3, (u, c0, c)
    print("linear: from 0, 1 and 5 the level tends to a u / d (0.5 at u = 0.05, 2.0 at u = 0.2)")


def check_averaging_bound():
    """c(T) <= c(0) + T (a ubar - d cbar) whenever c >= cbar on [0, T]; with
    funding averaging 0.9 of d cbar / a the nucleus cannot be held at cbar."""
    cbar = 2.0
    need = D * cbar / A
    rng = random.Random(1195)
    finals = []
    for _ in range(50):
        T, c, path, us = 100.0, cbar, [], []
        for _ in range(int(T / DT)):
            u = rng.uniform(0, 2 * 0.9 * need)
            us.append(u)
            c += DT * (A * u - D * c)
            path.append(c)
        ubar = sum(us) / len(us)
        # the integral identity behind the bound, exactly for the Euler scheme
        lhs = c - cbar
        rhs = DT * (A * sum(us) - D * (cbar + sum(path[:-1])))
        assert abs(lhs - rhs) < 1e-9
        if min(path) >= cbar:
            assert c <= cbar + T * (A * ubar - D * cbar) + 1e-9
        assert min(path) < cbar
        finals.append(c)
    print(f"linear, funding averaging 0.9 of d cbar / a from cbar = 2: falls below cbar in 50 of 50 random runs;"
          f" final level {min(finals):.2f} to {max(finals):.2f} at T = 100 (mean {sum(finals)/len(finals):.2f},"
          " tending to 1.8)")
    # The entry reports one such run ending at 1.61. It does not give the
    # funding process, the horizon or the seed, and under i.i.d. funding the
    # level concentrates near 1.8, so that figure is not reproduced here.
    print("  the entry's single run ending at 1.61 is not reproduced: its funding process, horizon and seed"
          " are not stated, and i.i.d. funding of this mean gives 1.74 to 1.84")
    return finals


def check_budget_sum():
    nuclei = [(0.1, 2.0, 1.0), (0.5, 1.0, 1.0), (0.02, 3.0, 1.0)]   # (d, cbar, a)
    need = sum(d * cb / a for d, cb, a in nuclei)
    for B, ok in ((need + 0.01, True), (need - 0.01, False)):
        assert (need <= B) == ok
    per_unit = [d / a for d, _, a in nuclei]          # cost of holding one unit of level
    assert per_unit[1] > per_unit[0] > per_unit[2]     # fast decay (0.5) dearer than slow (0.02)
    print(f"budget: holding three nuclei needs sum d cbar / a = {need:.2f}; a fast-decaying one is dearer per unit held")


def check_sigmoid():
    # u = 0.15 < 2 d K / a = 0.2: every start decays
    assert roots(0.15) is None
    for c0 in (0.2, 1.0, 2.0, 5.0):
        assert run(c0, 0.15, 600, sig=True) < 1e-3
    lo, hi = roots(0.25)
    assert (round(lo, 3), round(hi, 3)) == (0.5, 2.0)
    assert run(0.2, 0.25, 600, sig=True) < 1e-3
    for c0 in (1.0, 2.0, 5.0):
        assert abs(run(c0, 0.25, 600, sig=True) - 2.0) < 1e-3, c0
    lo, hi = roots(0.4)
    assert (round(lo, 3), round(hi, 3)) == (0.268, 3.732)
    print("sigmoidal: u = 0.15 all decay; u = 0.25 roots 0.5 and 2.0, start 0.2 decays, 1, 2, 5 reach 2.0;"
          " u = 0.4 roots 0.268 and 3.732")
    return lo, hi


def check_hysteresis(lo, hi):
    out = {}
    for cut in (26, 27):
        c = run(hi, 0.0, cut, sig=True)
        back = run(c, 0.4, 600, sig=True)
        out[cut] = (c, back)
    (c26, b26), (c27, b27) = out[26], out[27]
    assert round(c26, 3) == 0.277 and abs(b26 - hi) < 1e-3, (c26, b26)
    assert round(c27, 3) == 0.250 and b27 < 1e-3, (c27, b27)
    pred = math.log(hi / lo) / D
    assert round(pred, 1) == 26.3
    print(f"hysteresis at u = 0.4: cut 26 leaves {c26:.3f}, restored to {b26:.3f}; cut 27 leaves {c27:.3f},"
          f" restored to {b27:.4f}; predicted cut-off ln(c+/c-)/d = {pred:.2f}")


def control_linear_no_threshold():
    """Negative control: the linear model, cut for the same 27 units, is
    restored by restoring funding: no threshold without the sigmoid."""
    c = run(4.0, 0.0, 27)
    back = run(c, 0.4, 600)
    assert abs(back - 4.0) < 1e-3
    print(f"control: linear model cut 27 leaves {c:.3f} and restoring u = 0.4 returns {back:.3f} = a u / d")


def main():
    check_linear()
    check_averaging_bound()
    check_budget_sum()
    lo, hi = check_sigmoid()
    check_hysteresis(lo, hi)
    control_linear_no_threshold()
    print("checks pass")


if __name__ == "__main__":
    main()
