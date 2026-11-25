# scratch/manuscripts/governance-of-becoming/analysis/case189_supply_parameter.py
"""CASE-189's Construction 2 with a supply parameter s (gap G1.2 of Article 1; LEFT-OUT audit B17).

Run: python3 -I scratch/manuscripts/governance-of-becoming/analysis/case189_supply_parameter.py
Deterministic (fixed-step RK4, no randomness). Fictional by construction, illustrative parameters, as CASE-189 is.

Step 0 reproduces CASE-189's own figures (Construction 1 and Construction 2) before anything is extended.

The extension. CASE-189's Construction 2, with s multiplying the production terms:
    q'  = (20 h + 12 s_q q c1 c2 / (1 + c1 c2)) (1 - q) - q
    ci' = 4 s q cj^2 / (1 + cj^2) - (1 + d) ci
  Arm A: s_q = s (the supply enters all three production terms; the transient encounter term 20h does not).
  Arm B: s_q = 1 (the supply enters only the two capacity terms; the connector's own production is untouched).
  Control: supplied repair, the analogue of CLAIM-597 / CLAIM-604's second case: production set by s alone,
    q' = s Kq (1 - q) - q,  ci' = s Kc - (1 + d) ci,  with Kq, Kc matched so that at s = 1, d = 0 it holds
    arm A's maintained state.
  At s = 1 both arms are CASE-189's Construction 2 exactly.

Parameters, fixed before running: d = 0 for the supply sweeps (d = 0.4, CASE-189's invariance bound, as a second
level for the fold only); full supply s = 1; sweep points s = 0.9, 0.8, 0.7 and s* +/- 0.01; outages of length
0.5 and 5 with s restored to 1; ignition tested at 0.9 and 1.1 times the saddle; RK4 dt = 1e-3 for the reproduction,
2e-3 for the protocol runs; "out" means every variable below 1e-3, "kept" means c1 above 0.5, after 150 time units.

CLAIM-604's three signatures, as tested here: (1) ignition threshold: with the supply on, a start below an
unstable interior state goes out; (2) collapse rather than decline: below a supply level s* the kept state ceases
to exist and the structure goes out, where above it the kept state declines continuously; (3) hysteresis: after a
long enough outage (s = 0), restoring the supply does not relight it.

EXPECTATION (written before the first run, kept whatever the result):
  - Step 0 reproduces CASE-189's figures to its stated digits.
  - Arm A shows all three signatures. The production is drawn through the structure's own state (q times a
    sigmoid of c), so it is CLAIM-604's first case in form: an interior saddle at s = 1 (signature 1); a saddle-
    node in s at some s* < 1, found by minimizing s(c) = (1 + c^2)((1 + d) + 1/(3c)) / (4c) over c (signature 2);
    and, since s = 0 removes all production, decay towards 0 and a finite outage T_lost after which restoring s
    does not relight (signature 3).
  - Arm B shows all three too, but its signature 2 is CASE-189's damage fold relabelled: s and d enter only as
    s / (1 + d), so s*_B(d) = (1 + d) / (1 + d*) exactly, about 0.5914 at d = 0. What the supply adds in arm B is
    only that an outage is now defined.
  - The supplied-repair control shows none of the three: one globally stable equilibrium for each s > 0, smooth
    decline, recovery from any outage.
  - The coupling's spectral gap at the supply fold stays bounded away from zero (q* c*), as CLAIM-521 has it at
    the damage fold, while the slowest maintenance eigenvalue goes to zero.
  - None of this bears on CLAIM-606 / CLAIM-522: the signatures are found in a model whose internality is
    stipulated, and an outside crew supplying the same state-dependent production gives the same equations.
"""
import math

import numpy as np


def close(x, y, tol=5e-4):
    assert abs(x - y) <= tol, (x, y)


def rk4(f, y, t0, t1, dt):
    y = list(y)
    t = t0
    n = len(y)
    while t < t1 - 1e-12:
        h = min(dt, t1 - t)
        k1 = f(t, y)
        k2 = f(t + h / 2, [y[i] + h / 2 * k1[i] for i in range(n)])
        k3 = f(t + h / 2, [y[i] + h / 2 * k2[i] for i in range(n)])
        k4 = f(t + h, [y[i] + h * k3[i] for i in range(n)])
        y = [y[i] + h / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(n)]
        t += h
    return y


def jac(f, y, eps=1e-6):
    n = len(y)
    J = np.zeros((n, n))
    for j in range(n):
        yp, ym = list(y), list(y)
        yp[j] += eps
        ym[j] -= eps
        fp, fm = f(0.0, yp), f(0.0, ym)
        for i in range(n):
            J[i, j] = (fp[i] - fm[i]) / (2 * eps)
    return np.sort(np.linalg.eigvals(J).real)


def golden_min(g, a, b, it=200):
    r = (math.sqrt(5) - 1) / 2
    x1, x2 = b - r * (b - a), a + r * (b - a)
    for _ in range(it):
        if g(x1) < g(x2):
            b, x2 = x2, x1
            x1 = b - r * (b - a)
        else:
            a, x1 = x1, x2
            x2 = a + r * (b - a)
    x = (a + b) / 2
    return x, g(x)


def bisect_root(g, a, b, it=200):
    ga = g(a)
    for _ in range(it):
        m = (a + b) / 2
        gm = g(m)
        if (gm > 0) == (ga > 0):
            a, ga = m, gm
        else:
            b = m
    return (a + b) / 2


print("=== Step 0: CASE-189's own figures ===")
# ---- Construction 1 --------------------------------------------------------------------------------------------
c_lo, c_hi = (3 - math.sqrt(5)) / 2, (3 + math.sqrt(5)) / 2
close(c_lo, 0.382)
close(c_hi, 2.618)
con1 = lambda d1, d2: (lambda t, y: [3 * y[1] ** 2 / (1 + y[1] ** 2) - (1 + d1) * y[0],
                                     3 * y[0] ** 2 / (1 + y[0] ** 2) - (1 + d2) * y[1]])
ev = jac(con1(0, 0), [c_hi, c_hi])
close(ev[0], -1.2546)
close(ev[1], -0.7454)
close(rk4(con1(0, 0), [0.0, c_hi], 0, 60, 1e-3)[0], c_hi)          # reset c1 to 0 recovers
close(rk4(con1(0.4, 0.4), [2.0, 2.0], 0, 60, 1e-3)[0], 1.456, 1e-3)  # constant d = 0.4 settles at 1.456
close(math.sqrt(9) / 2 - 1, 0.5)                                    # fold: 9 - 4(1 + d)^2 = 0 at d = 0.5
assert rk4(con1(0, 0), [0.2, 0.2], 0, 60, 1e-3)[0] < 1e-3            # seed 0.2 collapses
close(rk4(con1(0, 0), [0.5, 0.5], 0, 60, 1e-3)[0], c_hi)             # seed 0.5 grows
print(f"C1: equilibria {c_lo:.3f} (saddle), {c_hi:.3f} (eigenvalues {ev[1]:.4f}, {ev[0]:.4f}); d=0.4 -> 1.456; "
      f"fold d=0.5")


# ---- Construction 2, generalized -------------------------------------------------------------------------------
def chi(z):
    return min(1.0, max(0.0, 10 * z - 5))


def model(s=1.0, sq=None, d=0.0, encounter=True, ko=None):
    """Arm A: sq=None (s_q = s). Arm B: sq=1.0. ko: knock out 'q', 'c1' or 'c2' production."""
    def f(t, y):
        q, c1, c2 = y
        z = math.exp(-t) if encounter else 0.0
        h = chi(z) ** 2
        s_q = s if sq is None else sq
        pq = 0.0 if ko == "q" else 12 * s_q * q * c1 * c2 / (1 + c1 * c2)
        p1 = 0.0 if ko == "c1" else 4 * s * q * c2 ** 2 / (1 + c2 ** 2)
        p2 = 0.0 if ko == "c2" else 4 * s * q * c1 ** 2 / (1 + c1 ** 2)
        return [(20 * h + pq) * (1 - q) - q, p1 - (1 + d) * c1, p2 - (1 + d) * c2]
    return f


Y0 = [0.0, 3.0, 3.0]
close(rk4(model(), Y0, 0, 0.25, 1e-3)[0], 0.967, 1e-3)
assert all(abs(v) < 1e-12 for v in [chi(math.exp(-t)) for t in (math.log(2), 1.0, 5.0)])
y_d4 = rk4(model(d=0.4), Y0, 0, 80, 1e-3)
close(y_d4[0], 0.897, 1e-3)
close(y_d4[1], 2.085, 1e-3)
y_noenc = rk4(model(encounter=False), Y0, 0, 80, 1e-3)
assert y_noenc[0] == 0.0 and max(y_noenc) < 1e-3
for ko in ("q", "c1", "c2"):
    assert max(rk4(model(ko=ko), Y0, 0, 120, 1e-3)) < 1e-3, ko
cs2 = (7 + 2 * math.sqrt(15)) / 11
cst = math.sqrt(cs2)
qst = 11 / 12 - 1 / (12 * cs2)
dst = (11 * cs2 - 1) / (3 * cst * (1 + cs2)) - 1
close(cst, 1.1578)
close(qst, 0.8545)
close(dst, 0.6908)
close(qst * cst, 0.9894)


def coupling_gap(q, c1, c2):
    B = np.array([[1.0, -1.0, 0.0], [0.0, 1.0, -1.0]])   # path 1-2-3
    L = q * B.T @ np.diag([c1, c2]) @ B
    return np.sort(np.linalg.eigvalsh(L))[1]


close(coupling_gap(qst, cst, cst), 0.9894)
print(f"C2: q(1/4)={rk4(model(), Y0, 0, 0.25, 1e-3)[0]:.3f}; d=0.4 long run (q,c)=({y_d4[0]:.3f}, {y_d4[1]:.3f}); "
      f"no encounter -> 0; each knockout -> 0")
print(f"C2 damage fold: c*={cst:.4f}, q*={qst:.4f}, d*={dst:.4f}, lambda2={coupling_gap(qst, cst, cst):.4f}")
print("Step 0 reproduces CASE-189.")


# ---- Symmetric equilibria with supply ---------------------------------------------------------------------------
def q_of(c, s, arm):
    s_q = s if arm == "A" else 1.0
    return 1 - (1 + c * c) / (12 * s_q * c * c)


def s_of_c(c, d, arm):
    """Supply at which (q_of(c), c, c) is an equilibrium."""
    if arm == "A":
        return (1 + c * c) * ((1 + d) + 1 / (3 * c)) / (4 * c)
    return (1 + d) * (1 + c * c) / (4 * q_of(c, 1.0, "B") * c)


def equilibria(s, d, arm):
    """Lower (saddle) and upper (kept) symmetric positive equilibria at supply s, or None."""
    cm, smin = golden_min(lambda c: s_of_c(c, d, arm), 0.4, 10.0)
    if s < smin:
        return None
    lo = bisect_root(lambda c: s_of_c(c, d, arm) - s, 0.35, cm)
    hi = bisect_root(lambda c: s_of_c(c, d, arm) - s, cm, 50.0)
    return [(q_of(c, s, arm), c, c) for c in (lo, hi)]


sq_arm = {"A": None, "B": 1.0}
DT = 2e-3
results = {}
for arm in ("A", "B"):
    print(f"\n=== Arm {arm}: supply in {'all three production terms' if arm == 'A' else 'the capacity terms only'} ===")
    lo, hi = equilibria(1.0, 0.0, arm)
    close(hi[1], rk4(model(), Y0, 0, 80, 1e-3)[1], 1e-4)             # s = 1 is CASE-189's Construction 2
    f1 = model(s=1.0, sq=sq_arm[arm], encounter=False)
    ev_lo, ev_hi = jac(f1, list(lo)), jac(f1, list(hi))
    assert ev_lo[-1] > 0 and ev_lo[-2] < 0 and ev_hi[-1] < 0
    print(f"s=1, d=0: kept (q,c)=({hi[0]:.4f}, {hi[1]:.4f}) eig max {ev_hi[-1]:.4f}; "
          f"saddle (q,c)=({lo[0]:.4f}, {lo[1]:.4f}) eig {ev_lo[-1]:+.4f}")

    # Signature 1: ignition threshold with the supply on.
    below = rk4(f1, [0.9 * v for v in lo], 0, 150, DT)
    above = rk4(f1, [min(0.999, 1.1 * lo[0]), 1.1 * lo[1], 1.1 * lo[2]], 0, 150, DT)
    assert max(below) < 1e-3 and above[1] > 0.5
    close(above[1], hi[1], 1e-3)
    print(f"[1] ignition: from 0.9 x saddle -> out (max {max(below):.1e}); from 1.1 x saddle -> c={above[1]:.4f}")

    # Signature 2: collapse rather than decline.
    for d in (0.0, 0.4):
        cm, smin = golden_min(lambda c: s_of_c(c, d, arm), 0.4, 10.0)
        print(f"[2] d={d}: supply fold s*={smin:.4f} at c*={cm:.4f}, q*={q_of(cm, smin, arm):.4f}, "
              f"coupling gap there {coupling_gap(q_of(cm, smin, arm), cm, cm):.4f}")
        if arm == "B":
            close(smin, (1 + d) / (1 + dst), 1e-6)                 # the damage fold relabelled
        if d == 0.0:
            results[arm] = smin
            sstar, cstar = smin, cm
    ev_near = jac(model(s=sstar + 1e-4, sq=sq_arm[arm], encounter=False), list(equilibria(sstar + 1e-4, 0, arm)[1]))
    assert -0.05 < ev_near[-1] < 0
    print(f"    slowest maintenance eigenvalue at s*+1e-4: {ev_near[-1]:.4f}")
    kept = []
    for s in (0.9, 0.8, 0.7, round(sstar + 0.01, 4)):
        y = rk4(model(s=s, sq=sq_arm[arm], encounter=False), list(hi), 0, 150, DT)
        close(y[1], equilibria(s, 0, arm)[1][1], 2e-3)
        kept.append((s, y[1]))
    yb = rk4(model(s=sstar - 0.01, sq=sq_arm[arm], encounter=False), list(hi), 0, 300, DT)
    assert max(yb) < 1e-3
    print("    kept c from the s=1 state: " + ", ".join(f"s={s}: {c:.4f}" for s, c in kept)
          + f"; s={sstar - 0.01:.4f}: out (max {max(yb):.1e})")
    assert kept[-1][1] > 0.8                                       # it holds a substantial state just above s*

    # Signature 3: hysteresis after an outage.
    def relights(T):
        y = rk4(model(s=0.0, sq=sq_arm[arm], encounter=False), list(hi), 0, T, DT)
        y = rk4(f1, y, 0, 150, DT)
        assert max(y) < 1e-3 or y[1] > 0.5
        return y[1] > 0.5

    assert relights(0.5) and not relights(5.0)
    a, b = 0.5, 5.0
    for _ in range(14):
        m = (a + b) / 2
        a, b = (m, b) if relights(m) else (a, m)
    T_lost = (a + b) / 2
    print(f"[3] outage: 0.5 units off -> relights; 5 units off -> does not; T_lost ~ {T_lost:.3f}")
    results[arm + "T"] = T_lost

# ---- Control: supplied repair -----------------------------------------------------------------------------------
print("\n=== Control: supplied repair (production set by s alone) ===")
_, hiA = equilibria(1.0, 0.0, "A")
KQ, KC = hiA[0] / (1 - hiA[0]), hiA[1]


def supplied(s, d=0.0):
    return lambda t, y: [s * KQ * (1 - y[0]) - y[0], s * KC - (1 + d) * y[1], s * KC - (1 + d) * y[2]]


ctrl_eq = lambda s: (s * KQ / (s * KQ + 1), s * KC)
for y0 in ([0.0, 0.0, 0.0], [0.05, 0.1, 0.1], [0.9 * v for v in equilibria(1.0, 0, "A")[0]]):
    y = rk4(supplied(1.0), y0, 0, 60, DT)
    close(y[1], KC, 1e-4)
print(f"[1] from (0,0,0), a small seed and 0.9 x arm A's saddle: all reach c={KC:.4f}; no threshold")
row = []
for s in (0.9, 0.7, results["A"] - 0.01, 0.1):
    y = rk4(supplied(s), [hiA[0], hiA[1], hiA[2]], 0, 60, DT)
    close(y[1], ctrl_eq(s)[1], 1e-4)
    row.append((s, y[1]))
print("[2] kept c declines linearly in s: " + ", ".join(f"s={s:.4f}: {c:.4f}" for s, c in row))
for T in (5.0, 30.0):
    y = rk4(supplied(0.0), [hiA[0], hiA[1], hiA[2]], 0, T, DT)
    y = rk4(supplied(1.0), y, 0, 60, DT)
    close(y[1], KC, 1e-4)
print("[3] after outages of 5 and 30 units, restoring s returns it to the same state")

print(f"\nSummary: s*_A={results['A']:.4f}, s*_B={results['B']:.4f} (= 1/(1+d*) = {1 / (1 + dst):.4f}), "
      f"T_lost A={results['AT']:.3f}, B={results['BT']:.3f}")
print("checks pass")
