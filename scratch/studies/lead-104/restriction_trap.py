# scratch/studies/lead-104/restriction_trap.py
# LEAD-104: the model of the competence-restriction loop (CLAIM-721), built as
# CLAIM-605's model with *reinstatement made a threshold on capacity*.
#
# CLAIM-605's dynamics, unchanged (lam=1, mu=0.3, tau=1.5):
#     dC/dt = lam * P * C * (1 - C) - mu * C,
# capacity C in [0,1] learned by doing (needs C present), decaying with disuse.
# Free party: P = min(tau*C, 1); steady states C=0 (stable), C_LOW=0.276
# (unstable), C_HIGH=0.7 (stable).
#
# The modification. Instead of outside support doing the work, a RESTRICTION
# removes the doing, and REINSTATEMENT is a threshold C_r on capacity: the
# restriction lifts (one-way) the instant C >= C_r.
#   - while restricted (R=1): the party may exercise only at fraction rho of
#     what it could, and the restricting party may run a training program
#     adding capacity directly at rate g:
#         P = rho * min(tau*C, 1),   dC/dt = lam*P*C*(1-C) - mu*C + g.
#     rho=0, g=0 is the bare restriction: no route to practice or training.
#   - while free (R=0): P = min(tau*C, 1), g=0 (CLAIM-605's free party).
#
# CLAIM-721's three conditions are now switches, each necessary for the loop:
#   (1) competence decays with disuse            -> mu > 0;
#   (2) lifting depends on competence shown      -> reinstatement gated on C_r;
#   (3) the restricting party supplies no route  -> rho = 0 and g = 0.
#
# Run: python3 -I scratch/studies/lead-104/restriction_trap.py
# The parameters are invented to show a mechanism; none is a measurement.
import math

LAM, MU, TAU = 1.0, 0.3, 1.5


def close(x, y, tol=5e-3):
    assert abs(x - y) <= tol, (x, y)


def dcdt(c, restricted, rho, g):
    p = (rho if restricted else 1.0) * min(TAU * c, 1.0)
    return LAM * p * c * (1 - c) - MU * c + (g if restricted else 0.0)


def sim(c0, c_r, rho=0.0, g=0.0, decay=True, horizon=400.0, dt=1e-3,
        gated=True):
    """Integrate a party that starts restricted at c0. The restriction lifts
    (one-way) when C >= c_r if gated, else it never lifts here. Returns
    (final C, reinstated?, reinstatement time or None)."""
    mu = MU if decay else 0.0
    c, t, restricted, t_reinstate = c0, 0.0, True, None
    while t < horizon:
        if restricted and gated and c >= c_r:
            restricted, t_reinstate = False, t
        p = (rho if restricted else 1.0) * min(TAU * c, 1.0)
        c += dt * (LAM * p * c * (1 - c) - mu * c + (g if restricted else 0.0))
        c = min(max(c, 0.0), 1.0)
        t += dt
    if restricted and gated and c >= c_r:
        restricted, t_reinstate = False, horizon
    return c, (not restricted), t_reinstate


# --- The free party's landscape (CLAIM-605, unchanged) -----------------------
C_LOW = (1 - math.sqrt(1 - 4 * MU / (LAM * TAU))) / 2   # unstable threshold
C_HIGH = 1 - MU / LAM                                   # kept state
C_R = 0.6   # reinstatement threshold: the authority lifts the bar at C >= 0.6
C0 = 0.5    # the party is restricted "for lack of competence": C0 < C_R
T_DEAD = math.log(C0 / C_LOW) / MU         # recoverability deadline
RHO_CRIT = 4 * MU / (LAM * TAU)            # practice-route critical fraction
G_CRIT = MU * C_R                          # training-route critical rate


def free_limit(c_start, horizon=400.0, dt=1e-3):
    """Where the FREE party ends from c_start (C_LOW<c -> C_HIGH; else -> 0)."""
    c, t = c_start, 0.0
    while t < horizon:
        c += dt * dcdt(c, False, 0.0, 0.0)
        t += dt
    return c


def main():
    close(C_LOW, 0.2764, 1e-4)
    close(C_HIGH, 0.7, 1e-9)

    # === Result 1: the bare trap is self-perpetuating =======================
    # No route (rho=0, g=0): while restricted dC/dt = -mu*C, so
    # C(t) = C0*exp(-mu t), strictly decreasing. It never reaches any C_r above
    # its limit, so the gate never opens: the restriction causes the very decay
    # that withholds reinstatement.
    c_end, reinstated, _ = sim(C0, C_R, rho=0.0, g=0.0)
    assert not reinstated and c_end < 0.01, (c_end, reinstated)

    # "produces the evidence for its own continuation": competence reviews at a
    # fixed interval each read a lower C than the last and each < C_r, so every
    # review extends the restriction. The decay IS the evidence.
    reviews = [C0 * math.exp(-MU * t) for t in (0.0, 2.0, 4.0, 6.0)]
    assert all(b < a for a, b in zip(reviews, reviews[1:]))    # monotone down
    assert all(r < C_R for r in reviews)                       # always "unfit"
    close(reviews[0], 0.5, 1e-9)
    close(reviews[2], 0.1506, 1e-3)

    # === Result 2: a recoverability deadline (CLAIM-605's twin) =============
    # A party restricted at C_LOW < C0 < C_R is not reinstated (C < C_r,
    # decaying) yet WOULD recover if someone freed it -- but only until C
    # decays past C_LOW. That window closes at t_dead = ln(C0/C_LOW)/mu; after
    # it, even lifting fails.
    close(T_DEAD, 1.976, 1e-3)
    for t_free, recovers in ((1.0, True), (1.5, True),
                             (2.5, False), (4.0, False)):
        c_at_free = C0 * math.exp(-MU * t_free)                # no-route decay
        assert (free_limit(c_at_free) > 0.6) == recovers, (t_free, c_at_free)

    # === Result 3: the route decides -- practice cannot ignite, training can =
    # (a) No route -> trap (Result 1).
    # (b) A practice route restores exercise at fraction rho (multiplicative,
    #     g=0). Positive restricted steady states exist only if rho >= rho_crit;
    #     below it EVERY restricted party decays to 0, however competent, and a
    #     route cannot ignite a party below its shifted threshold.
    close(RHO_CRIT, 0.8, 1e-9)
    assert sim(C0, C_R, rho=0.5, g=0.0)[1] is False      # weak route: trapped
    assert sim(C0, C_R, rho=0.5, g=0.0)[0] < 0.01
    # a route that fully restores exercise (rho=1) reinstates:
    assert sim(C0, C_R, rho=1.0, g=0.0)[1] is True
    # (c) A training route adds capacity directly (rate g, with rho=0: no
    #     exercise at all). Then dC/dt = g - mu*C -> C* = g/mu. It reinstates
    #     once g >= g_crit = mu*C_r, FROM ANY start, even C0 = 0 ("it ignites").
    close(G_CRIT, 0.18, 1e-9)
    assert sim(0.00, C_R, rho=0.0, g=0.20)[1] is True    # ignites from zero
    assert sim(0.00, C_R, rho=0.0, g=0.20)[0] > 0.69     # then free -> 0.7
    assert sim(C0, C_R, rho=0.0, g=0.15)[1] is False     # below g_crit: trap
    close(sim(C0, C_R, rho=0.0, g=0.15, gated=False)[0], 0.15 / MU, 1e-2)

    # === Result 4: each of the three conditions is necessary ================
    # Drop (1) decay: C stays at C0 < C_r forever -- a standing bar, but it
    # makes no new evidence; not the worsening loop.
    c_nodecay, reinst_nodecay, _ = sim(C0, C_R, rho=0.0, g=0.0, decay=False)
    close(c_nodecay, C0, 1e-6)
    assert reinst_nodecay is False
    # Drop (2) competence-gated lifting: a fixed release date frees the party
    # regardless; freed at t=1 (C=0.370 > C_LOW) it recovers, and the loop
    # cannot form because release does not wait on C.
    c_at1 = C0 * math.exp(-MU * 1.0)
    assert c_at1 > C_LOW and free_limit(c_at1) > 0.69
    # Drop (3) no route: Result 3 -- a sufficient route reinstates.

    print("restriction-trap model: all numbers reproduce.")
    print(f"  C_LOW={C_LOW:.4f}  C_HIGH={C_HIGH:.4f}  C_r={C_R}  C0={C0}")
    print(f"  recoverability deadline t_dead={T_DEAD:.3f}")
    print(f"  practice-route critical fraction rho_crit={RHO_CRIT:.3f}")
    print(f"  training-route critical rate g_crit={G_CRIT:.3f} (= mu*C_r)")


if __name__ == "__main__":
    main()
