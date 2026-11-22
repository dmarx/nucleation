"""Calibrate each arm's (a, gain, s) so the aggregate statistics match.

Targets: member variance 1, mean pairwise member correlation 0.4, lag-1
autocorrelation of the aggregate mean(x) 0.9. Common random numbers (one
seed) make the simulated moments smooth in the parameters. Writes
calibration.json.
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import aggregate_stats, simulate  # noqa: E402

TARGET = dict(var_member=1.0, rho_members=0.4, ac1_agg=0.9)
START = dict(A=[0.6, 0.15, 0.6], B=[0.5, 0.4, 0.6], C=[0.6, 0.15, 0.6],
             C0=[0.6, 0.15, 0.6])


def moments(arm, theta, R=300, T=1500, burn=600, seed=11):
    a, gain, s = theta
    st = aggregate_stats(simulate(arm, dict(a=a, gain=gain, s=s), R, T, burn, seed))
    return st


def resid(theta, arm):
    st = moments(arm, theta)
    return [st[k] - v for k, v in TARGET.items()]


def calibrate(arm):
    sol = least_squares(resid, START[arm], args=(arm,),
                        bounds=([0.0, 0.0, 0.05], [0.98, 2.0, 2.0]),
                        diff_step=1e-2, xtol=1e-6, ftol=1e-6)
    a, gain, s = sol.x
    return dict(a=float(a), gain=float(gain), s=float(s),
                residual=[float(v) for v in sol.fun])


if __name__ == "__main__":
    out = {}
    here = os.path.dirname(os.path.abspath(__file__))
    for arm in ["A", "B", "C", "C0"]:
        out[arm] = calibrate(arm)
        print(arm, out[arm], flush=True)
    with open(os.path.join(here, "calibration.json"), "w") as f:
        json.dump(out, f, indent=1)
