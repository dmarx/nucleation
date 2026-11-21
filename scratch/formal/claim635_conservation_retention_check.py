"""Check of CLAIM-635's retention bound (status review of 2026-11-20).

Claim: on a finite state space with Markov kernels K_1, K_2, ... (possibly
different at each step), if K_i f = f for every i and g = f - E f(S_0) is
not a.s. zero under the starting law, then for every n

    I(S_0; S_n) >= (E|g(S_0)|)^2 / (2 ||g||_inf^2)   nats,

while a bounded defect ||K f - f||_inf <= p does not prevent forgetting.

Checks:
  1. Martingale step: K_1 ... K_n f = f (so E[g(S_n) | S_0] = g(S_0)).
  2. The identity E_joint[h] - E_product[h] = E|g(S_0)| for
     h(x, y) = sgn(g(x)) g(y).
  3. The total-variation step, |E_P h - E_Q h| <= 2 ||h||_inf TV(P, Q).
  4. Pinsker, TV(joint, product) <= sqrt(I / 2), I in nats.
  5. The bound itself, on random reducible, time-dependent chains with
     transient states, n = 1 .. 40.
  6. The witness: the two-state flip chain with defect p forgets its start.
  7. The worked example: identity kernels, f(x) = x, uniform start gives
     1/2 nat against ln 2.
Controls (each must FAIL, or the checks above would pass vacuously):
  C1. A perturbed, non-harmonic f (kernels mixed toward a common law):
      the martingale check fails, and the bound computed from f is
      violated at some n.
  C2. The bound with its factor 2 dropped, (E|g|)^2 / ||g||^2, is violated
      (the worked example: 1 nat > ln 2), so the check can see a wrong
      constant.
  C3. The bound is in nats and is not slack enough to survive a unit
      error: scaling I down by ln 2 (I_nats * ln 2) violates it on some
      instance.
"""
import math
import random

import numpy as np

TOL = 1e-10


def mutual_information(p0, P):
    """I(S_0; S_n) in nats, start law p0, n-step transition matrix P."""
    joint = p0[:, None] * P
    pn = joint.sum(axis=0)
    prod = p0[:, None] * pn[None, :]
    mask = joint > 0
    return float((joint[mask] * np.log(joint[mask] / prod[mask])).sum())


def harmonic_kernel(f, closed, rng):
    """A random kernel with K f = f exactly.

    States in a closed class move only within it, and f is constant on each
    class. A transient state x moves anywhere, its row a random law mixed
    with a point mass so that the row's f-mean equals f(x).
    """
    n = len(f)
    K = np.zeros((n, n))
    cls = {}
    for c, members in enumerate(closed):
        for x in members:
            cls[x] = members
    for x in range(n):
        if x in cls:
            row = rng.dirichlet(np.ones(len(cls[x])))
            K[x, cls[x]] = row
            continue
        q = rng.dirichlet(np.ones(n))
        mu = q @ f
        if abs(mu - f[x]) < 1e-15:
            K[x] = q
            continue
        # point mass on a state on the other side of f(x) from mu
        side = [z for z in range(n) if (f[z] - f[x]) * (mu - f[x]) < 0]
        z = rng.choice(side)
        lam = (f[z] - f[x]) / (f[z] - mu)  # lam*mu + (1-lam) f(z) = f(x)
        K[x] = lam * q
        K[x, z] += 1 - lam
    return K


def random_instance(rng):
    """Five to seven states, two or three closed classes, the rest transient."""
    n = rng.integers(5, 8)
    k = rng.integers(2, 4)
    states = list(range(n))
    rng.shuffle(states)
    closed, i = [], 0
    for c in range(k):
        size = rng.integers(1, 3)
        closed.append(sorted(states[i:i + size]))
        i += size
    f = np.zeros(n)
    vals = rng.uniform(-1, 1, size=k)
    vals[0], vals[1] = -1.0, 1.0  # so every transient value lies strictly inside
    for c, members in enumerate(closed):
        f[members] = vals[c]
    for x in states[i:]:
        f[x] = rng.uniform(-0.95, 0.95)
    p0 = rng.dirichlet(np.ones(n))
    return f, closed, p0


def bound(f, p0, factor=2.0):
    g = f - p0 @ f
    Eabs = p0 @ np.abs(g)
    return Eabs ** 2 / (factor * np.max(np.abs(g)) ** 2), g, Eabs


def main():
    rng = np.random.default_rng(20261120)
    trials, horizon = 3000, 40
    min_slack, worst_mart = math.inf, 0.0
    for t in range(trials):
        f, closed, p0 = random_instance(rng)
        b, g, Eabs = bound(f, p0)
        assert Eabs > 0
        P = np.eye(len(f))
        for step in range(1, horizon + 1):
            K = harmonic_kernel(f, closed, rng)
            assert np.allclose(K.sum(axis=1), 1) and (K >= -1e-15).all()
            P = P @ K
            # 1. martingale
            worst_mart = max(worst_mart, float(np.max(np.abs(P @ g - g))))
            # 2. identity
            joint = p0[:, None] * P
            pn = joint.sum(axis=0)
            prod = p0[:, None] * pn[None, :]
            h = np.sign(g)[:, None] * g[None, :]
            gap = float((joint * h).sum() - (prod * h).sum())
            assert abs(gap - Eabs) < 1e-9, (t, step, gap, Eabs)
            # 3. TV step
            tv = 0.5 * float(np.abs(joint - prod).sum())
            assert gap <= 2 * np.max(np.abs(h)) * tv + TOL
            # 4. Pinsker
            I = mutual_information(p0, P)
            assert tv <= math.sqrt(I / 2) + TOL
            # 5. the bound
            assert I >= b - TOL, (t, step, I, b)
            min_slack = min(min_slack, I - b)
    assert worst_mart < 1e-9
    print(f"checks 1-5: {trials} chains x {horizon} steps; "
          f"max martingale error {worst_mart:.1e}; min slack {min_slack:.3f} nats")

    # 6. witness: two-state flip with probability p
    for p in (0.01, 0.2, 0.5, 0.9):
        K = np.array([[1 - p, p], [p, 1 - p]])
        f = np.array([0.0, 1.0])
        assert abs(np.max(np.abs(K @ f - f)) - p) < 1e-12
        P = np.linalg.matrix_power(K, 3000)
        I = mutual_information(np.array([0.5, 0.5]), P)
        assert I < 1e-6, (p, I)
    print("check 6: two-state flip, defect p in {0.01, 0.2, 0.5, 0.9}: I -> 0")

    # 7. worked example
    f = np.array([0.0, 1.0]); p0 = np.array([0.5, 0.5])
    b, _, _ = bound(f, p0)
    I = mutual_information(p0, np.eye(2))
    assert abs(b - 0.5) < 1e-12 and abs(I - math.log(2)) < 1e-12
    print(f"check 7: identity example, bound {b} nat, I = ln 2 = {I:.4f}")

    # Controls
    # C1: kernels mixed toward a common law break harmonicity; bound fails.
    fired_mart = fired_bound = False
    for t in range(200):
        f, closed, p0 = random_instance(rng)
        b, g, _ = bound(f, p0)
        nu = rng.dirichlet(np.ones(len(f)))
        P = np.eye(len(f))
        for step in range(1, horizon + 1):
            K = 0.8 * harmonic_kernel(f, closed, rng) + 0.2 * nu[None, :]
            P = P @ K
            if np.max(np.abs(P @ g - g)) > 1e-6:
                fired_mart = True
            if mutual_information(p0, P) < b - 1e-6:
                fired_bound = True
    assert fired_mart and fired_bound, (fired_mart, fired_bound)
    print("control C1 fired: non-harmonic f fails the martingale check and the bound")

    # C2: the bound without its factor 2 is violated.
    f = np.array([0.0, 1.0]); p0 = np.array([0.5, 0.5])
    b1, _, _ = bound(f, p0, factor=1.0)
    assert mutual_information(p0, np.eye(2)) < b1
    print(f"control C2 fired: bound with factor 1 gives {b1} > ln 2")

    # C3: information scaled the wrong way between bits and nats.
    fired = False
    for t in range(500):
        f, closed, p0 = random_instance(rng)
        b, _, _ = bound(f, p0)
        P = np.eye(len(f))
        for step in range(1, 15):
            P = P @ harmonic_kernel(f, closed, rng)
        if mutual_information(p0, P) * math.log(2) < b:
            fired = True
            break
    assert fired
    print("control C3 fired: I scaled by ln 2 violates the bound on some instance")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
