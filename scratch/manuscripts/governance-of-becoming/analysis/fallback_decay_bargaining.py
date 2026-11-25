# scratch/manuscripts/governance-of-becoming/analysis/fallback_decay_bargaining.py
# The assistant's computation for Article 9 (governance-of-becoming), 2026-11-25: Proposed-grade, illustrative.
# It joins two held models the record keeps apart:
#   - CLAIM-605's capacity learned by doing, dC/dt = lam*P*C*(1 - C) - mu*C, with substitutive support
#     P = min(tau*C, 1 - A) or capacity-first support P = min(tau*C, 1); lam = 1, mu = 0.3, tau = 1.5
#     (scratch/formal/capability_trap_toy.py);
#   - the symmetric Nash split of CASE-264 and CLAIM-tmp2jhc1, u_P = o_P + (S - o_P - o_R)/2, with CASE-264's
#     S = 10 and R's stand-alone o_R = 2.
# P's outside option o_P(t) is the value of P's stand-alone path from its capacity C(t): annuitized at rate r,
# w * r * integral of e^(-r s) min(tau*C_s, 1) ds over a horizon of 80, normalized to the horizon, with C_s following the no-support dynamics from C(t). w = 4 is the
# value per unit time of meeting the whole demand alone. w, r and the horizon are invented; none is a measurement.
# Deterministic (no randomness). Run: python3 -I scratch/manuscripts/governance-of-becoming/analysis/fallback_decay_bargaining.py
import math

LAM, MU, TAU = 1.0, 0.3, 1.5
S, O_R, W = 10.0, 2.0, 4.0
DT, HORIZON = 0.01, 80.0


def close(x, y, tol):
    assert abs(x - y) <= tol, (x, y, tol)


def rate(c, a, model, first=False):
    """dC/dt. model 605: learning needs capacity (threshold); model 602: CLAIM-602's form, no threshold."""
    p = min(TAU * c, 1.0) if first else min(TAU * c, max(0.0, 1.0 - a))
    grow = LAM * p * c * (1 - c) if model == 605 else LAM * p * (1 - c)
    return grow - MU * c


def step(c, a, model, first=False, dt=DT):
    k1 = rate(c, a, model, first)
    k2 = rate(c + dt * k1 / 2, a, model, first)
    k3 = rate(c + dt * k2 / 2, a, model, first)
    k4 = rate(c + dt * k3, a, model, first)
    return min(1.0, max(0.0, c + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6))


def outside_option(c, model, r):
    """Annuitized value of P's stand-alone path from capacity c (no support)."""
    t, v = 0.0, 0.0
    while t < HORIZON - 1e-9:
        v += (math.exp(-r * t) - math.exp(-r * (t + DT))) / r * min(TAU * c, 1.0)
        c = step(c, 0.0, model)
        t += DT
    return W * r * v / (1 - math.exp(-r * HORIZON))


def myopic(c):
    return W * min(TAU * c, 1.0)


def nash(o_p):
    assert S >= o_p + O_R
    return o_p + (S - o_p - O_R) / 2


def path(c0, a, model, first, t_end, every):
    """Capacity under support, sampled every `every` time units."""
    out, c, t, n = [(0.0, c0)], c0, 0.0, int(round(every / DT))
    k = 0
    while t < t_end - 1e-9:
        c = step(c, a, model, first)
        t += DT
        k += 1
        if k % n == 0:
            out.append((round(t, 6), c))
    return out


# ---- 0. The components reproduce. --------------------------------------------------------------------------
C_LOW = (1 - math.sqrt(1 - 4 * MU / (LAM * TAU))) / 2
C_HIGH = 1 - MU / LAM
T_DEAD = math.log(C_HIGH / C_LOW) / MU
close(C_LOW, 0.2764, 1e-4)
close(C_HIGH, 0.7, 1e-9)
close(T_DEAD, 3.098, 1e-3)                                   # CLAIM-605, result 1
for o_b, u_b in ((0, 8), (2, 9), (4, 10)):                   # CLAIM-tmp2jhc1 / A22 sec. 9: V = 20, o_A = 4
    close(o_b + (20 - 4 - o_b) / 2, u_b, 1e-12)
close(nash(0.0), 4.0, 1e-12)                                 # CASE-264, arm A: P's share 4 with a_P = 0
close(S - nash(0.0), 6.0, 1e-12)
C602 = LAM / (LAM + MU)                                      # CLAIM-602's kept capacity 0.769
close(C602, 0.7692, 1e-4)

R = 0.25                                                     # the baseline, fixed before the run; section 4 varies it
print("Fallback decay and the Nash split (illustrative parameters; the assistant's computation)")
print(f"CLAIM-605 threshold {C_LOW:.4f}, kept state {C_HIGH:.2f}, deadline {T_DEAD:.2f}; S = {S:g}, o_R = {O_R:g}, "
      f"w = {W:g}, r = {R:g}")

# ---- 1. Main arm: full substitution (A = 1) in CLAIM-605's model, P's fallback valued by its stand-alone path. -----
main = path(C_HIGH, 1.0, 605, False, 6.0, 0.05)
rows = []
for t, c in main:
    close(c, C_HIGH * math.exp(-MU * t), 2e-6)               # under A = 1, C = 0.7 e^(-mu t) exactly
    o = outside_option(c, 605, R)
    rows.append((t, c, o, nash(o), myopic(c), nash(myopic(c))))
u0 = rows[0][3]
close(rows[0][2], W, 1e-3)                                   # at the kept state P's fallback is the full w
close(u0, 6.0, 1e-3)
print("\n1. Full substitution, CLAIM-605's model. t, C(t), o_P(t), P's Nash share; myopic o_P and share")
for t, c, o, u, om, um in rows:
    if abs(t * 2 - round(t * 2)) < 1e-9:
        print(f"   t = {t:4.1f}  C = {c:.3f}  o_P = {o:.3f}  u_P = {u:.3f}   | myopic o_P = {om:.3f}  u_P = {um:.3f}")

# The share never rises, and every unit of fallback lost moves half a unit to R.
for (t1, _, o1, u1, _, _), (t2, _, o2, u2, _, _) in zip(rows, rows[1:]):
    assert u2 <= u1 + 1e-9
    close(u1 - u2, (o1 - o2) / 2, 1e-9)
# Where the fall is steepest: the largest drop per interval is in the interval that holds the deadline.
drops = [((rows[i][0] + rows[i + 1][0]) / 2, rows[i][3] - rows[i + 1][3]) for i in range(len(rows) - 1)]
t_steep, d_steep = max(drops, key=lambda x: x[1])
assert abs(t_steep - T_DEAD) <= 0.05, t_steep
u_at = {round(t, 2): u for t, _, _, u, _, _ in rows}
before, after = u_at[2.6], u_at[3.6]
end = rows[-1][3]
share_lost_total = u0 - end
share_lost_window = before - after
print(f"   steepest fall per 0.05 at t = {t_steep:.3f} (deadline {T_DEAD:.3f}): {d_steep:.3f}")
print(f"   u_P: {u0:.3f} at t = 0, {before:.3f} at 2.6, {after:.3f} at 3.6, {end:.3f} at 6;"
      f" {100 * share_lost_window / share_lost_total:.0f} % of the fall by t = 6 lies in [2.6, 3.6]")
assert end > nash(0.0)                                        # by t = 6 P is still above CASE-264's arm A (4)
# The forward-looking fallback is worth more than current output before the deadline (recovery is ahead) and less
# after it (decay is ahead); the two cross where C(t) passes the threshold, at the deadline.
cross = [(rows[i][0], rows[i + 1][0]) for i in range(len(rows) - 1)
         if (rows[i][2] - rows[i][4]) > 0 >= (rows[i + 1][2] - rows[i + 1][4])]
assert len(cross) == 1 and cross[0][0] <= T_DEAD <= cross[0][1], cross
print(f"   forward-looking o_P exceeds current-output o_P until t in {cross[0]}, and is below it after")
# The myopic valuation, current output only, sees no deadline: it leaves P less than the forward-looking one before
# the deadline (once tau*C < 1, at t > 0.163) and more after it, and its own fall is steepest at the start.
for t, c, _, u, _, um in rows[1:]:
    if TAU * c >= 1:
        continue
    assert (um < u) if t < T_DEAD - 0.05 else (um > u) if t > T_DEAD + 0.05 else True
m_drops = [((rows[i][0] + rows[i + 1][0]) / 2, rows[i][5] - rows[i + 1][5]) for i in range(len(rows) - 1)]
t_m, d_m = max(m_drops, key=lambda x: x[1])
assert t_m < 1.0, t_m
print(f"   the current-output valuation falls fastest at t = {t_m:.3f} ({d_m:.3f} per 0.05), not at the deadline")

# ---- 2. Ending the supply before or after the deadline. --------------------------------------------------------
print("\n2. Supply ended at T; P's fallback after 20 further units with no support")
for T in (2.0, 3.0, 3.5, 5.0):
    c = C_HIGH * math.exp(-MU * T)
    for _ in range(int(20 / DT)):
        c = step(c, 0.0, 605)
    o = outside_option(c, 605, R)
    print(f"   T = {T:3.1f}: C = {c:.3f}, o_P = {o:.3f}, u_P = {nash(o):.3f}")
    assert (o > 3.9) == (T < T_DEAD)

# ---- 3. Controls. ----------------------------------------------------------------------------------------------
print("\n3. Controls")
# 3a. Negative control: capacity-first support leaves capacity, the fallback and the split where they were.
cf = path(C_HIGH, 1.0, 605, True, 6.0, 1.0)
for t, c in cf:
    close(c, C_HIGH, 1e-6)
    close(nash(outside_option(c, 605, R)), u0, 1e-3)
print(f"   3a capacity-first support: u_P stays {u0:.3f} for t in [0, 6]")
# 3b. Partial substitution below CLAIM-605's a* = 1 - mu/(1 - C_LOW) = 0.585: capacity settles at 1 - mu/(lam a')
#     with a' = 1 - A, above the threshold, so the fallback keeps its recovery and the split settles, with no cliff.
A_STAR = 1 - MU / (1 - C_LOW)
close(A_STAR, 0.585, 1e-3)
part = path(C_HIGH, 0.5, 605, False, 40.0, 0.5)
c_set = part[-1][1]
close(c_set, 1 - MU / (LAM * 0.5), 1e-3)
o_set = outside_option(c_set, 605, R)
pu = [nash(outside_option(c, 605, R)) for _, c in part]
p_drop = max(pu[i] - pu[i + 1] for i in range(len(pu) - 1))
print(f"   3b substitution at A = 0.5 (below a* = {A_STAR:.3f}): C settles at {c_set:.3f}, o_P = {o_set:.3f}, "
      f"u_P = {nash(o_set):.3f}; largest fall per 0.5 = {p_drop:.3f}")
assert nash(o_set) > 5.0
# 3c. A control that can fail: CLAIM-602's model has no threshold, so the same pipeline must show no cliff.
s602 = path(C602, 1.0, 602, False, 6.0, 0.05)
u602 = [nash(outside_option(c, 602, R)) for _, c in s602]
d602 = max(u602[i] - u602[i + 1] for i in range(len(u602) - 1))
print(f"   3c CLAIM-602's model, full substitution: u_P {u602[0]:.3f} -> {u602[-1]:.3f} over [0, 6]; "
      f"largest fall per 0.05 = {d602:.3f} (CLAIM-605's model: {d_steep:.3f})")
assert d602 < d_steep / 3 and u602[-1] > end + 0.5
# 3d. CASE-264's arm B: R sets the terms and P cannot leave. P gets the least that keeps it working, r = 1,
#     whatever its fallback is worth, so the decay moves nothing.
print("   3d CASE-264 arm B (no exit; by construction): u_P = 1 at every t; the fallback's decay changes nothing")
# 3e. Take-it-or-leave-it with exit: R offers P exactly its fallback, so P bears the whole fall, not half of it.
tl = [o for _, _, o, _, _, _ in rows]
print(f"   3e take-it-or-leave-it with exit: u_P = o_P, {tl[0]:.3f} -> {tl[-1]:.3f}; Nash {u0:.3f} -> {end:.3f}")
close(tl[0] - tl[-1], 2 * (u0 - end), 1e-9)

# ---- 4. Sensitivity to the discount rate: the steepest fall stays at the deadline. ------------------------------
print("\n4. Discount rate r: where the fall is steepest, and how much of it lies within 0.5 of the deadline")
fracs = []
i_lo, i_hi = [i for i, (t, _) in enumerate(main) if abs(t - 2.6) < 1e-9 or abs(t - 3.6) < 1e-9]
for r in (0.02, 0.05, 0.1, 0.25, 0.5):
    us = [nash(outside_option(c, 605, r)) for _, c in main]
    ds = [((main[i][0] + main[i + 1][0]) / 2, us[i] - us[i + 1]) for i in range(len(us) - 1)]
    ts, dmax = max(ds, key=lambda x: x[1])
    frac = (us[i_lo] - us[i_hi]) / (us[0] - us[-1])
    fracs.append(frac)
    print(f"   r = {r:4.2f}: u_P {us[0]:.3f} -> {us[-1]:.3f}; steepest at t = {ts:.3f}, {dmax:.3f} per 0.05; "
          f"{100 * frac:.0f} % of the fall by t = 6 in [2.6, 3.6]")
    if r <= 0.25:                                             # for an impatient P (r = 0.5) it moves earlier
        assert abs(ts - T_DEAD) <= 0.05, (r, ts)
assert all(a > b for a, b in zip(fracs, fracs[1:]))           # the more patient P is, the more the fall is a step

print("\nchecks pass")
