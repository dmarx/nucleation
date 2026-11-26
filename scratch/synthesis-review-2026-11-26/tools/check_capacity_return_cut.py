"""Check for NEW-CLAIM-capacity-capture-without-return: with the return
channel cut (chi = psi = 0) and resources as capacity, g_E (1 + omega m_P),
the evaluator E is captured iff (1 + omega m_P*) g_E sigma_E^2 > 2 (1 - phi'_E),
where m_P* is the party's own fixed point; and the side is E's, not P's.
Usage: python3 -I check_capacity_return_cut.py <dir holding LEAD-015's model.py> [theta]
With no second argument theta = 0 (E's evidence independent of P);
with one, theta is drawn from [0, 1]. Captured = E bistable, two stable
readings reached from +0.9 and -0.9, rather than one (tilted) fixed point."""
import sys
import numpy as np
sys.path.insert(0, sys.argv[1])
import model as M  # noqa: E402

def settle(Q, x0, T=400000):
    x = np.asarray(x0, float)
    for _ in range(T):
        x2 = M.step(x, Q)
        if np.max(np.abs(x2 - x)) < 1e-13:
            return x2
        x = x2
    return x

THETA0 = len(sys.argv) < 3
agree = total = 0
rng = np.random.default_rng(7)
rows = []
for _ in range(400):
    gE, gP = rng.uniform(1, 6, 2)
    bP = rng.uniform(-0.3, 0.3)
    om = rng.uniform(0, 10)
    th = 0.0 if THETA0 else rng.uniform(0, 1)
    Q = M.params(dict(g=gE), dict(g=gP, b0=bP), theta=th, omega=om, chi=0.0, psi=0.0,
                 resource_form="multiplicative")
    if M.margin(Q["E"]) <= 0 or M.margin(Q["P"]) <= 0:
        continue  # each stable alone
    xp = settle(Q, [0.0, 0.0, 0.0, 0.0])
    mP = xp[2]
    E = Q["E"]
    lhs = (1 + om * mP) * E["g"] * E["sigma"] ** 2
    rhs = 2 * (1 - M.phi_eff(E))
    if abs(lhs - rhs) < 0.02 * rhs:
        continue
    pred = lhs > rhs
    a = settle(Q, [0.9, 0.9, mP, xp[3]])[0]
    b = settle(Q, [-0.9, -0.9, mP, xp[3]])[0]
    # with theta > 0 and mP != 0 E's evidence is tilted; capture = two distinct
    # stable readings (bistability) rather than one tilted fixed point
    obs = abs(a - b) > 1e-3
    total += 1
    agree += (pred == obs)
    if obs:
        rows.append((round(om, 2), round(mP, 3), round(a, 3), round(b, 3)))
print("agree", agree, "of", total)
print("captured examples (omega, m_P*, from +, from -):", rows[:8])
