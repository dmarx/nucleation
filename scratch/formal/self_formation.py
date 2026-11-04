# scratch/formal/self_formation.py
"""A construction for CLAIM-tmpbeh2e: self-formation as a maintained new capacity.

Extends CASE-189 (a transient encounter forms a maintained connector) and
CASE-115 (one shared parameter cannot meet two opposed demands; splitting it
can). An agent acts in two contexts, A and B, with targets a and b. Its output
is y_k = x + s_k * u * z, with s_A = +1, s_B = -1, a shared level x and a
differentiating command z in [-1, 1]. How far it can differentiate is
u = sigma(S) * sigma(G), sigma(c) = c / (1 + c), where S is its capacity to
tell A from B (a sensor) and G its capacity to act differently on them (a
channel). With fast adaptation of x and z, its residual frustration is

    F(u, D) = max(0, D/2 - u)**2,    D = |a - b|.

The capacities are slow:

    dS/dt = alpha * F + beta * P(G) + e_S(t) - (1 + dmg) * S
    dG/dt = alpha * F + beta * P(S) + e_G(t) - (1 + dmg) * G
    P(c)  = 3 c**2 / (1 + c**2)

alpha * F is production driven by the agent's own frustration, beta * P the
mutual production by which sensor and channel maintain each other (CASE-189's
Construction 1), and e(t) any outside supply. Everything is stipulated; the
point is what the tests can and cannot tell apart.

Run: python3 scratch/formal/self_formation.py
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


def sigma(c: float) -> float:
    return c / (1.0 + c)


def P(c: float) -> float:
    return 3.0 * c * c / (1.0 + c * c)


def frustration(S: float, G: float, D: float) -> float:
    u = sigma(max(S, 0.0)) * sigma(max(G, 0.0))
    return max(0.0, D / 2.0 - u) ** 2


def simulate(schedule, alpha=1.0, beta=1.0, ext=None, dmg=0.0, y0=(0.0, 0.0),
             t_end=100.0, knock=None):
    """schedule(t) -> D; ext(t, S, G) -> (e_S, e_G); knock(t) -> dict of overrides."""
    def rhs(t, y):
        S, G = y
        a, b, d = alpha, beta, dmg
        e = ext(t, S, G) if ext else (0.0, 0.0)
        if knock:
            k = knock(t)
            a = k.get("alpha", a); b = k.get("beta", b)
            if k.get("no_ext"):
                e = (0.0, 0.0)
        F = frustration(S, G, schedule(t))
        return [a * F + b * P(G) + e[0] - (1 + d) * S,
                a * F + b * P(S) + e[1] - (1 + d) * G]
    ts = np.linspace(0, t_end, int(t_end * 20) + 1)
    sol = solve_ivp(rhs, (0, t_end), list(y0), t_eval=ts, rtol=1e-9, atol=1e-11, max_step=0.05)
    S, G = sol.y
    F = np.array([frustration(s, g, schedule(t)) for t, s, g in zip(ts, S, G)])
    return ts, S, G, F


def integral(ts, F, t0, t1):
    m = (ts >= t0) & (ts <= t1)
    return float(np.trapezoid(F[m], ts[m]))


def main() -> None:
    root_lo = (3 - 5 ** 0.5) / 2
    root_hi = (3 + 5 ** 0.5) / 2
    u_hi = sigma(root_hi) ** 2
    print(f"maintained state with no frustration: S = G = {root_hi:.4f} (saddle {root_lo:.4f}); "
          f"u = {u_hi:.4f}, resolves any D <= {2 * u_hi:.4f}")

    # 1. formation, persistence, transfer
    def sched(t):  # discrepancy D=1 on [0,20), none on [20,60), new same-class D=0.8 on [60,80), none after
        return 1.0 if t < 20 else (0.8 if 60 <= t < 80 else 0.0)

    runs = {
        "self-forming (alpha=1, beta=1)": dict(alpha=1.0, beta=1.0),
        "no maintenance cycle (beta=0)": dict(alpha=1.0, beta=0.0),
        "naive, never exposed": None,
    }
    print("\n1. Formation (D = 1 on t < 20), persistence (no conflict, 20-60), transfer (D = 0.8, 60-80)")
    for name, kw in runs.items():
        if kw is None:
            ts, S, G, F = simulate(lambda t: 0.8 if 60 <= t < 80 else 0.0, t_end=100)
        else:
            ts, S, G, F = simulate(sched, t_end=100, **kw)
        i = lambda t: int(round(t * 20))
        print(f"  {name:34s} S(20)={S[i(20)]:.3f} S(59)={S[i(59)]:.3f} "
              f"intF[0,20]={integral(ts, F, 0, 20):.4f} intF[60,80]={integral(ts, F, 60, 80):.4f}")

    # 2. thresholds: least alpha that forms the capacity for D = 1; least D that forms it for alpha = 1
    def formed(alpha, D):
        ts, S, G, F = simulate(lambda t: D if t < 40 else 0.0, alpha=alpha, t_end=80)
        return S[-1] > 1.0
    lo, hi = 0.01, 50.0
    for _ in range(40):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if formed(mid, 1.0) else (mid, hi)
    print(f"\n2. least alpha forming the capacity at D = 1: {hi:.4f}")
    lo, hi = 0.0, 2.0
    for _ in range(40):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if formed(1.0, mid) else (mid, hi)
    print(f"   least D forming it at alpha = 1: {hi:.4f}  (smaller discrepancies are tolerated, not formed)")

    # 3. a larger same-class discrepancy extends the capacity
    ts, S, G, F = simulate(lambda t: 1.0 if t < 20 else (1.6 if 40 <= t < 70 else 0.0), t_end=100)
    i = lambda t: int(round(t * 20))
    print(f"\n3. D = 1.6 after formation: S(39)={S[i(39)]:.3f} -> S(69)={S[i(69)]:.3f}, "
          f"F(69)={F[i(69)]:.5f}; after it ends S(99)={S[i(99)]:.3f}")

    # 4. provenance
    print("\n4. Provenance (knockouts at t = 30, after the conflict ended at t = 20)")
    sched2 = lambda t: 1.0 if t < 20 else 0.0
    own = simulate(sched2, t_end=60)
    pulse = simulate(sched2, alpha=0.0, ext=lambda t, S, G: (3.0, 3.0) if t < 2 else (0.0, 0.0), t_end=60)
    upheld = simulate(sched2, beta=0.0, ext=lambda t, S, G: (P(G), P(S)), t_end=60)
    print(f"  own formation        S(29)={own[1][i(29)]:.4f}")
    print(f"  outside pulse, then own maintenance  S(29)={pulse[1][i(29)]:.4f}")
    print(f"  upheld from outside (supply = P as feedback) S(29)={upheld[1][i(29)]:.4f}, "
          f"max |S_own - S_upheld| = {np.max(np.abs(own[1] - upheld[1])):.2e}")
    for name, kw in [("own formation", dict()),
                     ("outside pulse", dict(alpha=0.0, ext=lambda t, S, G: (3.0, 3.0) if t < 2 else (0.0, 0.0))),
                     ("upheld from outside", dict(beta=0.0, ext=lambda t, S, G: (P(G), P(S))))]:
        k1 = simulate(sched2, t_end=60, knock=lambda t: {"beta": 0.0} if t >= 30 else {}, **kw)
        k2 = simulate(sched2, t_end=60, knock=lambda t: {"no_ext": True} if t >= 30 else {}, **kw)
        k0 = simulate(sched2, t_end=60, knock=lambda t: {"alpha": 0.0}, **kw)
        print(f"  {name:20s} internal-maintenance KO -> S(59)={k1[1][-21]:.4f}; "
              f"outside-supply KO -> S(59)={k2[1][-21]:.4f}; "
              f"frustration-production KO from t=0 -> S(29)={k0[1][i(29)]:.4f}")

    # 5. damage: the maintained capacity has CASE-189's fold
    print("\n5. Damage on turnover after formation (constant from t = 30):")
    for d in (0.3, 0.45, 0.5, 0.55):
        ts, S, G, F = simulate(sched2, t_end=200, dmg=0.0,
                               knock=None)
        def rhs_d(t, y, d=d):
            S, G = y
            return [P(G) - (1 + d) * S, P(S) - (1 + d) * G]
        sol = solve_ivp(rhs_d, (0, 400), [S[i(30)], G[i(30)]], rtol=1e-9, atol=1e-11)
        print(f"  d = {d:.2f}: S(+400) = {sol.y[0][-1]:.4f}")


if __name__ == "__main__":
    main()
