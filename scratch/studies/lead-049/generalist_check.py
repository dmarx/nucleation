"""Two-resource trade-off: the lone symmetric generalist as a -i community.

For each shape and c/B, evaluates at theta = 1/2 and n = (2 a(1/2) B - c) / (2 a(1/2)^2):
whether it is an equilibrium meeting theorem A for the one-operator system, and the
removed specialist's recovery growth there, c (1 / (2 a(1/2)) - 1).
Run: python3 -I generalist_check.py   (writes results/generalist_check.json)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np

import model as M
from study import SHAPES

rows = []
for name, (al, be, ga) in SHAPES.items():
    nic = M.TradeoffNiche(al, be, ga)
    g = nic.a(0.5)
    for cB in np.round(np.arange(0.1, 1.0, 0.1), 2):
        B = 1.0
        b, c = np.array([B, B]), np.array([cB])
        n = np.array([(2 * g * B - cB) / (2 * g * g)])
        th = np.array([0.5])
        chk = M.theorem_A_check(nic, b, c, n, th, eps=0.2)
        grad = np.concatenate(M.grad(nic, b, c, n, th))
        R = M.residual(nic, b, n, th)
        lam_spec = float(R[1] - cB)  # specialist u(0) = (0, 1)
        rows.append(dict(shape=name, c_over_B=float(cB), a_half=float(g), n=float(n[0]),
                         grad_norm=float(np.linalg.norm(grad)), theorem_A_holds=chk["holds"],
                         hess_min=chk["hess_min"], lam_specialist=lam_spec,
                         lam_formula=float(cB * (1 / (2 * g) - 1))))
        print(name, cB, "A:", chk["holds"], "hess_min=%.4f lam=%+.4f" % (chk["hess_min"], lam_spec))
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results"), exist_ok=True)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "generalist_check.json"), "w") as fh:
    json.dump(rows, fh, indent=1)
