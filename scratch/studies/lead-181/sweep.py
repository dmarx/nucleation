"""LEAD-181 robustness sweep: the optimal inquiry under the penalty (pen)
and with newly recognized violations unpenalized (amnesty, grace g = L), as
the cost of being found out (sigma) and the remediation lag (L) vary, with
surfacing s = 0.03 and costly inquiry (alpha = 0.1). Optimum only, by Monte
Carlo over the policy grid with common random numbers. Writes sweep.md.
Run: OPENBLAS_NUM_THREADS=1 python3 -I sweep.py   (about a minute)
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as m  # noqa: E402

REPS, SEED = 1000, 20261124
ARMS = m.arms()


def optimum(regime, kw):
    vals = []
    for ai, bi in ARMS:
        rng = np.random.default_rng(SEED)
        vals.append(m.simulate(np.full(REPS, ai), np.full(REPS, bi), regime,
                               rng, **kw)["reward"].mean())
    return ARMS[int(np.argmax(vals))]


def main():
    rows = ["| L | sigma | pen optimum (a, b) | amnesty optimum (a, b) |",
            "|---|---|---|---|"]
    for L in (1, 3):
        for sigma in (0.0, 3.0, 10.0, 30.0):
            kw = dict(alpha=0.1, s=0.03, sigma=sigma, L=L, g=L)
            rows.append(f"| {L} | {sigma:g} | {optimum('pen', kw)} | "
                        f"{optimum('amnesty', kw)} |")
            print(rows[-1], flush=True)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "sweep.md"), "w") as f:
        f.write("# LEAD-181 sweep\n\nOptimal stationary policy (a inquiry "
                "units of B = 10, b remediation cap), s = 0.03, "
                "alpha = 0.1, lam = 1, T = 20.\n\n")
        f.write("\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
