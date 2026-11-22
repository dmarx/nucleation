"""Where does an erased anchored wall go? Counts walls over all bonds
(boundary layers included) after the uniform state is written at t = T_IN.
Usage: OPENBLAS_NUM_THREADS=1 python3 -I check_erasure.py > erasure.txt"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import partitions as Pt  # noqa: E402
import z2rnn as Z  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
for sid in [f"trained-d4-s{s}" for s in range(4)] + [f"trained-d8-s{s}" for s in range(2)]:
    P = dict(np.load(os.path.join(HERE, "params", sid + ".npz")))
    rng = np.random.default_rng(3)
    S = np.ones((20, Z.N))
    S[:, 16:] = -1
    x = Z.make_inputs(S, rng, t_free=200)
    hp = Z.forward(P, Z.make_inputs(np.ones((20, Z.N)), rng))
    hr = Z.forward(P, x, hook=lambda t, h: hp[Z.T_IN].copy() if t == Z.T_IN else h)
    w12 = Pt.wall_positions(hr[Z.T_IN + Z.T_FREE])
    w200 = Pt.wall_positions(hr[-1])
    at_edge = np.mean([w == [Z.N - 1] for w in w200])
    print(f"{sid}: walls after 12 steps {w12[0]}, after 200 steps {w200[0]}; "
          f"single wall at the clamped end after 200 steps in {at_edge:.2f} of runs")
