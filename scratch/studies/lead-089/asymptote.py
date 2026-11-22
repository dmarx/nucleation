"""Do the control-only gates close the gap on unseen arrangements with
unlimited data? Fits C2, C3, C4 and WO to the exact expected counts of the
governed and interacting worlds (10^6 episodes per training arrangement, no
sampling noise), five seeds of the true parameters, and reports the regret
on the unseen arrangements in nats per episode.

    python3 -I asymptote.py
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def expected_counts(P, arrangements, n_per):
    n = np.zeros_like(P)
    px = M.context_probs()
    for a in arrangements:
        n[:, a, :] = n_per * px[:, None] * P[:, a, :]
    return n


def main():
    out = []
    for world in ("governed", "interacting"):
        for seed in range(5):
            rng = np.random.default_rng([89, 99, seed])
            P, meta = M.world_table(world, rng)
            n = expected_counts(P, M.TRAIN_A, 1e6)
            t = expected_counts(P, M.TEST_A, 1.0)
            row = {"world": world, "seed": seed, **meta}
            for k in ("C2", "C3", "C4"):
                _, pred, _ = M.gate_fit(n, M.features(k)[0], ndraw=50)
                row[k] = float((t * (np.log(P) - np.log(pred))).sum() / t.sum())
            _, pred = M.wo_posterior(n, G=16)
            row["WO"] = float((t * (np.log(P) - np.log(pred))).sum() / t.sum())
            out.append(row)
            print(json.dumps(row), flush=True)
    with open(os.path.join(HERE, "results", "asymptote.json"), "w") as fh:
        json.dump(out, fh, indent=1)


if __name__ == "__main__":
    main()
