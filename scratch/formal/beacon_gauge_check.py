"""scratch/formal/beacon_gauge_check.py

Checks the identity behind the claim on the beacon's unidentifiable
miscalibration (filed 2026-11-23): a world whose protected beacon reports
z* + d, and a world whose beacon is correct but whose target, beacon
placements and sensor biases are shifted (z + d, z* + d, b_i - A_i d), give
every sensor report and every beacon report identically.

Also checks, for k channels that each read the same placed points with a
fixed offset of their own (r_kt = z_t + d_k), which unknowns the reports
identify: every difference d_i - d_j, and never the common mode, a shift
of all offsets and all points together.

Run: python3 -I scratch/formal/beacon_gauge_check.py
"""
import numpy as np


def main(trials=1000, n=4, seed=1):
    rng = np.random.default_rng(seed)
    bad = 0
    for _ in range(trials):
        A = [rng.normal(size=(2, 2)) for _ in range(n)]
        b = [rng.normal(size=2) for _ in range(n)]
        d, z, zs = rng.normal(size=2), rng.normal(size=2), rng.normal(size=2)
        b2 = [bi - Ai @ d for Ai, bi in zip(A, b)]
        same = (all(np.allclose(Ai @ z + bi, Ai @ (z + d) + ci) for Ai, bi, ci in zip(A, b, b2))
                and all(np.allclose(Ai @ zs + bi, Ai @ (zs + d) + ci) for Ai, bi, ci in zip(A, b, b2)))
        bad += not same
    print(f"trials {trials}, mismatches {bad}")
    return bad


def common_mode(ks=(1, 2, 3, 5), T=10):
    """Unidentified dimensions of (points, offsets) from the reports alone."""
    out = {}
    for k in ks:
        rows = []
        for t in range(T):
            for c in range(k):
                for ax in range(2):
                    row = np.zeros(2 * T + 2 * k)
                    row[2 * t + ax] = 1
                    row[2 * T + 2 * c + ax] = 1
                    rows.append(row)
        M = np.array(rows)
        out[k] = M.shape[1] - np.linalg.matrix_rank(M)
        print(f"k={k} channels: {out[k]} unidentified dimensions (the common mode)")
    return out


if __name__ == "__main__":
    bad = main()
    cm = common_mode()
    raise SystemExit(bad or any(v != 2 for v in cm.values()))
