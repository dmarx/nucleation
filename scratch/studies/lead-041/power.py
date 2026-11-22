"""How many contested decisions a window needs before the procedure can
show a lead (p_lead < 0.05) or show ambivalence (p_ambivalence < 0.05),
with the departure profile of the FOMC record's uncontested quarters
(spec A, nominal: 0.39 of them took the common first choice, 0.42 the
second, 0.19 the third). Synthetic; prints a small table.

Usage: python3 -I power.py
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import procedure as P  # noqa: E402
from fomc import NAMED, TIGHTEN, EASE  # noqa: E402

OPTS = ("cut", "hike", "hold")


def window(n, rng, p_top, alternate=False):
    eps = []
    for t in range(n):
        if alternate:
            d = "hike" if t % 2 == 0 else "cut"
        else:
            u = rng.random()
            d = "hike" if u < p_top else ("hold" if u < p_top + (1 - p_top) / 2 else "cut")
        eps.append(P.Episode(t, "w", OPTS, {"inflation": TIGHTEN, "employment": EASE}, d))
    return eps


def main(reps=30, eps_rate=(0.39, 0.42, 0.19)):
    rng = np.random.default_rng(0)
    print("n  p_top  share_prevails  share_ambivalent(alternating)")
    for n in (4, 8, 16, 24, 40):
        for p_top in (0.6, 0.75, 0.9):
            prev = 0
            for _ in range(reps):
                r = P.analyse_window("w", window(n, rng, p_top), NAMED, eps_rate, rng, n_sim=300)
                prev += r.verdict == "prevails" and r.leading == "inflation"
            amb = 0
            for _ in range(10):
                r = P.analyse_window("w", window(n, rng, 0, True), NAMED, eps_rate, rng, n_sim=300)
                amb += r.verdict == "ambivalent"
            print(n, p_top, round(prev / reps, 2), round(amb / 10, 2))


if __name__ == "__main__":
    main()
