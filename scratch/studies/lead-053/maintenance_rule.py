"""LEAD-053: the dependence rule for a regulatory capacity's constraint set K,
applied to the record's cases.

The rule (the assistant's wording, filed as a CLAIM):
  - membership: K constrains every constraint that the constraints realizing
    the named capacity depend on, directly or through others (production
    dependence, TERM-070's "depends on");
  - threshold: each such constraint must stand at the least level at which
    what depends on it is still produced; at the top, the least level at
    which the capacity can be exercised;
  - alternatives: where a capacity has substitutable routes, K is the union,
    over routes, of the states in which every constraint of that route stands.
K is then fixed independently of the dynamics of the constraints themselves,
and the viability kernel (THEORY-134) is computed from those dynamics.

Run:  python3 -I maintenance_rule.py      (prints the results)
Test: python3 -I -m pytest -q test_maintenance_rule.py
"""

from __future__ import annotations

import itertools
import math

# ---------------------------------------------------------------------------
# A finite viability kernel (discrete time, finite states, set-valued controls)
# ---------------------------------------------------------------------------


def viability_kernel(states, K, successors):
    """Largest subset of K from each state of which SOME control keeps the
    state in the subset: the discrete viability kernel (Aubin; THEORY-134).
    `successors(x)` returns a list of the possible next states, one per
    control. Iterates Viab_{n+1} = {x in Viab_n : some successor in Viab_n}."""
    viab = {x for x in states if K(x)}
    while True:
        nxt = {x for x in viab if any(y in viab for y in successors(x))}
        if nxt == viab:
            return viab
        viab = nxt


# ---------------------------------------------------------------------------
# CASE-036, Northstar, as a finite toy (stipulated for this test)
# ---------------------------------------------------------------------------
# State (e, P, L): e = 1 emergency regime on; P = maintenance practice 0..4
# (deployments, fixes, the skill of making them); L = legibility 0..4 (how
# readable the system is, the evidence on which lifting is judged).
#   - Under the emergency (e = 1) maintenance is deferred: P falls by 1.
#     Off it (e = 0), P recovers by 1.
#   - L is produced by maintenance: it rises by 1 when P >= 2, falls by 1
#     when P < 2.
#   - Deferred maintenance emits anomalies: anomaly iff P <= 2 or L <= 1.
#   - Governance (the emergency criteria, applied correctly): while an
#     anomaly shows, the emergency must stay. Lifting is permitted only with
#     no anomaly showing and L >= 2 (enough evidence to judge the lift).
#   - Controls: keep, or lift (when permitted). `defer_maintenance=False` is
#     the control variant in which the emergency does not touch P.

PMAX = LMAX = 4


def northstar_states():
    return list(itertools.product((0, 1), range(PMAX + 1), range(LMAX + 1)))


def anomaly(P, L):
    return P <= 2 or L <= 1


def lift_permitted(P, L):
    return (not anomaly(P, L)) and L >= 2


def northstar_step(x, lift, defer_maintenance=True):
    e, P, L = x
    if e == 1 and lift and lift_permitted(P, L):
        e = 0
    if e == 1 and defer_maintenance:
        P2 = max(P - 1, 0)
    elif e == 1:
        P2 = P
    else:
        P2 = min(P + 1, PMAX)
    L2 = min(L + 1, LMAX) if P >= 2 else max(L - 1, 0)
    return (e, P2, L2)


def northstar_successors(defer_maintenance=True):
    def succ(x):
        return list({northstar_step(x, lift, defer_maintenance) for lift in (False, True)})
    return succ


def K_dependence(x):
    """The dependence rule for the capacity to leave the emergency regime by
    the organization's own means. Realizing constraint: the lifting
    decision, exercisable iff permitted, which needs L >= 2 and no anomaly.
    L depends on P (L is sustained iff P >= 2); the anomaly test depends on
    P and L. Least levels: L >= 2 (the lift's evidence), P >= 3 (no anomaly
    from deferred maintenance; this also sustains L). So K = {P >= 3, L >= 2}.
    The regime e is not constrained: K is about the capacity, not the
    operative regime."""
    _, P, L = x
    return P >= 3 and L >= 2


def K_stipulated(x):
    """The organization's own declared standard (CLAIM-195's route carried to
    an agent): the emergency criteria are met, that is, no anomaly is showing
    while the emergency is off. Under the emergency every state meets it."""
    e, P, L = x
    return e == 1 or not anomaly(P, L)


def operative_trajectory(x0, steps, defer_maintenance=True):
    """The organization's operative policy: keep the emergency while the
    criteria require it, and also while they merely permit keeping it (a
    cautious governance that lifts only once evidence is overwhelming,
    here L == LMAX and P == PMAX); otherwise lift."""
    xs = [x0]
    x = x0
    for _ in range(steps):
        e, P, L = x
        lift = e == 1 and lift_permitted(P, L) and P == PMAX and L == LMAX
        x = northstar_step(x, lift, defer_maintenance)
        xs.append(x)
    return xs


def northstar_report(defer_maintenance=True, x0=(1, 4, 3), steps=8):
    states = northstar_states()
    succ = northstar_successors(defer_maintenance)
    kern_dep = viability_kernel(states, K_dependence, succ)
    kern_sti = viability_kernel(states, K_stipulated, succ)
    traj = operative_trajectory(x0, steps, defer_maintenance)
    rows = []
    for t, x in enumerate(traj):
        rows.append({
            "t": t, "state": x, "emergency": x[0] == 1,
            "criteria_met": K_stipulated(x),
            "in_K_dep": K_dependence(x), "in_kernel_dep": x in kern_dep,
            "in_kernel_stip": x in kern_sti,
        })
    return rows


# ---------------------------------------------------------------------------
# CASE-111: fold in boundary maintenance, b' = mu b + kappa b^2 - b^3
# ---------------------------------------------------------------------------


def case111_branches(mu, kappa):
    disc = kappa * kappa + 4 * mu
    if disc < 0:
        return None
    r = math.sqrt(disc)
    return (kappa - r) / 2, (kappa + r) / 2  # (b_minus, b_plus)


def case111_kernel_lower_edge(mu, kappa, b_f):
    """K = {b >= b_f}, b_f the functional level set by what b maintains.
    For a one-dimensional autonomous flow the kernel of [b_f, inf) is
    [max(b_f, b_minus), inf) when b_plus >= b_f (states at or above b_minus
    go to b_plus), and empty when b_plus < b_f or there is no b_plus.
    Valid for mu < 0 (bistable range); for mu >= 0, b = 0 is unstable and
    every b > 0 goes to b_plus."""
    br = case111_branches(mu, kappa)
    if br is None:
        return None
    bm, bp = br
    if bp < b_f:
        return None
    if mu >= 0:
        return b_f
    return max(b_f, bm)


def case111_simulate(b0, mu, kappa, T=400.0, dt=0.01):
    b = b0
    for _ in range(int(T / dt)):
        b += dt * (mu * b + kappa * b * b - b ** 3)
    return b


# ---------------------------------------------------------------------------
# CASE-112: tilted bistability, w' = mu w - w^3 + h
# ---------------------------------------------------------------------------


def case112_hc(mu):
    return 2 * (mu / 3) ** 1.5 if mu > 0 else 0.0


def case112_mu_c(h_max):
    """The structural level past which an agent whose higher-order volition
    is bounded by |h| <= h_max can no longer switch regime: h_c(mu) = h_max."""
    return 3 * (h_max / 2) ** (2 / 3)


# ---------------------------------------------------------------------------
# CASE-227: anti-phase mode kept by a decaying capacity c
# ---------------------------------------------------------------------------


def case227_rate(c, alpha=2.2, delta=1.0, u=0.0):
    return alpha * c * c / (1 + c * c) - delta * c + u


def case227_levels(alpha=2.2, delta=1.0):
    # alpha c/(1+c^2) = delta  ->  delta c^2 - alpha c + delta = 0
    disc = alpha * alpha - 4 * delta * delta
    r = math.sqrt(disc)
    return (alpha - r) / (2 * delta), (alpha + r) / (2 * delta)


def case227_time_to_half(c0=0.6, eps=1.0, dt=1e-4, alpha=2.2, delta=1.0):
    c, t = c0, 0.0
    while c > 0.5:
        c += dt * eps * case227_rate(c, alpha, delta)
        t += dt
        if t > 1e4:
            return math.inf
    return t


def main():
    print("== CASE-036 (Northstar toy), emergency defers maintenance ==")
    for r in northstar_report(True):
        print(r)
    print("== control: emergency does not defer maintenance ==")
    for r in northstar_report(False):
        print(r)
    print("== CASE-111, kappa = 1 ==")
    for mu in (-0.2, -0.15, -0.05, 0.05):
        bm, bp = case111_branches(mu, 1.0)
        print(f"mu={mu}: b-={bm:.4f} b+={bp:.4f} "
              f"kernel lower edge (b_f=0.1)={case111_kernel_lower_edge(mu, 1.0, 0.1)}")
    print("== CASE-112 ==")
    for h_max in (0.1, 0.2, 0.385):
        print(f"h_max={h_max}: mu_c={case112_mu_c(h_max):.4f}, "
              f"check h_c(mu_c)={case112_hc(case112_mu_c(h_max)):.4f}")
    print("== CASE-227 ==")
    cm, cp = case227_levels()
    print(f"c- = {cm:.5f}, c+ = {cp:.5f}; K = (1/2, inf); kernel = [{cm:.5f}, inf)")
    print(f"c(0)=0.6 in K, not in kernel; reaches 1/2 at t = {case227_time_to_half():.3f}/eps")
    print(f"with outside supply u=0.02: rate at 0.6 = {case227_rate(0.6, u=0.02):+.4f}")


if __name__ == "__main__":
    main()
