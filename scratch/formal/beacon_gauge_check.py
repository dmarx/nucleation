"""scratch/formal/beacon_gauge_check.py

Checks the identity behind the claim on the beacon's unidentifiable
miscalibration (filed 2026-11-23): a world whose protected beacon reports
z* + d, and a world whose beacon is correct but whose target, beacon
placements and sensor biases are shifted (z + d, z* + d, b_i - A_i d), give
every sensor report and every beacon report identically.

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


if __name__ == "__main__":
    raise SystemExit(main())
