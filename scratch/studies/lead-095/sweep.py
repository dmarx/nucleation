"""LEAD-095: how far the default run's D(s) profiles hold across parameters.

Draws random parameter sets (seed fixed) and, for nucleus-present states
(1, n), n = 0..M-1, reports how often D(1, n) is monotone in n under each
mechanism, and how often it falls by the end.

Run:  python3 -I scratch/studies/lead-095/sweep.py [out.json]
"""
import json
import sys
from dataclasses import replace

import numpy as np

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))

from committor_model import Params, D_table

TOL = 1e-12


def draw(rng) -> Params:
    return Params(M=int(rng.integers(4, 13)), b=float(rng.uniform(0.3, 3)),
                  g=float(rng.uniform(1.5, 6)), kappa=float(10 ** rng.uniform(-2.5, -1)),
                  a0=float(10 ** rng.uniform(-1.5, 0)), aS=float(10 ** rng.uniform(0.3, 1.3)),
                  d0=float(10 ** rng.uniform(-0.7, 0.7)), theta=1.0)


def profile(D):
    d = np.diff(D)
    return dict(rising=bool(np.all(d >= -TOL)), falling=bool(np.all(d <= TOL)),
                ends_lower=bool(D[-1] < D[0]))


def sweep(n_draws=2000, seed=20261122) -> dict:
    rng = np.random.default_rng(seed)
    counts: dict = {}
    for _ in range(n_draws):
        p = draw(rng)
        theta = float(rng.uniform(0.2, 0.8))
        M = p.M
        for name, q in {"neither": replace(p, rate_effect=False),
                        "rate only": replace(p, rate_effect=True),
                        "feedback only": replace(p, theta=theta, rate_effect=False),
                        "feedback+rate": replace(p, theta=theta, rate_effect=True)}.items():
            pr = profile(D_table(q)[1, :M])
            c = counts.setdefault(name, dict(rising=0, falling=0, ends_lower=0))
            for k, v in pr.items():
                c[k] += v
    return dict(n_draws=n_draws, seed=seed,
                share={k: {kk: round(vv / n_draws, 4) for kk, vv in v.items()} for k, v in counts.items()})


if __name__ == "__main__":
    res = sweep()
    for k, v in res["share"].items():
        print(f"{k:14s} rising {v['rising']:.3f}  falling {v['falling']:.3f}  ends lower {v['ends_lower']:.3f}")
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as fh:
            json.dump(res, fh, indent=1)
