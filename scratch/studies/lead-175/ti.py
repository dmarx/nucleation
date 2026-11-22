"""Helpers for analyze_posterior.py: thermodynamic integration, crossings, and
Chen et al.'s free-energy formula (tested in test_tms.py)."""
from math import log
import numpy as np


def ti_logZ(ladder, EL, EL0, P0):
    """log Z_α(n) = log P0 - ∫_0^n E_{α,n'}[L] dn' on the ladder: [0, n_1] by the
    trapezoid in n from the prior mean EL0, then segment by segment."""
    ladder = np.asarray(ladder, float); EL = np.asarray(EL, float)
    I = np.zeros(len(ladder))
    I[0] = 0.5 * (EL0 + EL[0]) * ladder[0]
    # on each segment, E[L] = a + c/n through the two end values (exact for the
    # asymptotic form L_α + λ/n)
    n1, n2, E1, E2 = ladder[:-1], ladder[1:], EL[:-1], EL[1:]
    c = (E1 - E2) / (1 / n1 - 1 / n2)
    a = E1 - c / n1
    I[1:] = I[0] + np.cumsum(a * (n2 - n1) + c * np.log(n2 / n1))
    return np.log(P0) - I


def crossing(x, y):
    """First upward zero crossing of y over increasing x, interpolated in log x."""
    for i in range(len(x) - 1):
        if np.isfinite(y[i]) and np.isfinite(y[i + 1]) and y[i] < 0 <= y[i + 1]:
            t = -y[i] / (y[i + 1] - y[i])
            return float(np.exp(np.log(x[i]) + t * (np.log(x[i + 1]) - np.log(x[i]))))
    return None


def formula_ncr(dL, dlam, dc):
    """Zero crossings (+ to -) of n dL + dlam log n + dc on n in [2, 1e6] (Eq. 12)."""
    ns = np.geomspace(2, 1e6, 200000)
    v = ns * dL + dlam * np.log(ns) + dc
    i = np.where((v[:-1] > 0) & (v[1:] <= 0))[0]
    return [round(float(ns[j]), 1) for j in i]
