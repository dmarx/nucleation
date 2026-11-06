"""scratch/formal/claim582_witness.py: checks CLAIM-582's capped-disturbance witness.

CLAIM-582's robustness witness: the system dy/dt = u + w, with |u| <= 1, starts
at y = 0, and the task is to keep |y| <= 0.1 on [0, 1] whatever w does.

- With the hard constraint |w| <= 1, the Lipschitz feedback u = -sat(10 y),
  where sat clips to [-1, 1], keeps |y| <= 0.1 for every disturbance.
  This file asserts that bound against a set of disturbance laws.
- Control: against w = 2 (allowed when only |w| <= 2), every |u| <= 1 gives
  dy/dt >= 1, so y(1) >= 1 > 0.1. The file asserts that the bound is
  exceeded, both under the witness feedback and under the best constant
  input u = -1.
- Non-vacuity control: under w = 1, the witness drives y to within 1e-3 of
  0.1, so the bound is nearly attained and the test can fail.

Integration: forward Euler, fixed step DT = 1e-4, horizon T = 1.0.
For DT <= 0.1 the bound is exact in discrete time as well: on the linear
region, |y + DT(-10 y + w)| <= 0.1 (1 - 10 DT) + DT = 0.1. So the assertion
allows only floating-point slack (EPS = 1e-12).

Run: python3 -I scratch/formal/claim582_witness.py
"""
import math
import random

DT = 1e-4
T = 1.0
STEPS = int(round(T / DT))
BOUND = 0.1
EPS = 1e-12


def sat(x):
    return max(-1.0, min(1.0, x))


def witness(y):
    return -sat(10.0 * y)


def run(policy, disturbance, wmax):
    """Integrate dy/dt = u + w from y = 0. Return (max |y|, y(T))."""
    y, peak = 0.0, 0.0
    for k in range(STEPS):
        t = k * DT
        u = policy(y)
        assert abs(u) <= 1.0
        w = disturbance(t, y)
        assert abs(w) <= 1.0
        y += DT * (u + wmax * w)
        peak = max(peak, abs(y))
    return peak, y


rng = random.Random(0)
# disturbance laws, as fractions of the cap wmax
laws = {
    "w = +1": lambda t, y: 1.0,
    "w = -1": lambda t, y: -1.0,
    "w pushes outward": lambda t, y: 1.0 if y >= 0 else -1.0,
    "w pushes inward": lambda t, y: -1.0 if y > 0 else 1.0,
    "w = sin(40 t)": lambda t, y: math.sin(40.0 * t),
    "w switches at t = 0.5": lambda t, y: 1.0 if t < 0.5 else -1.0,
    "w random +-1": lambda t, y: rng.choice((-1.0, 1.0)),
    "w random uniform": lambda t, y: rng.uniform(-1.0, 1.0),
}

# 1. the witness under the cap |w| <= 1
worst = 0.0
for name, law in laws.items():
    peak, _ = run(witness, law, 1.0)
    print(f"|w| <= 1, {name:24s} max |y| = {peak:.6f}")
    assert peak <= BOUND + EPS, name
    worst = max(worst, peak)

# 2. non-vacuity: the bound is nearly attained, so the test could fail
assert worst >= BOUND - 1e-3, worst

# 3. control: without the cap, w = 2 defeats every policy
peak_w, yT_w = run(witness, lambda t, y: 1.0, 2.0)
peak_c, yT_c = run(lambda y: -1.0, lambda t, y: 1.0, 2.0)
print(f"w = 2, witness feedback:  max |y| = {peak_w:.6f}, y(1) = {yT_w:.6f}")
print(f"w = 2, u = -1 throughout: max |y| = {peak_c:.6f}, y(1) = {yT_c:.6f}")
assert yT_c >= 1.0 - 1e-9 and peak_c > BOUND
assert yT_w >= 1.0 - 1e-9 and peak_w > BOUND

print("OK: |y| <= 0.1 under |w| <= 1; the bound is exceeded under w = 2")
