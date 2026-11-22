"""LEAD-015 experiments. python3 -I run.py [e1 e2 ...]; each writes results/<name>.json."""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as M  # noqa: E402
from test_model import random_Q  # noqa: E402

RES = os.path.join(HERE, "results")
os.makedirs(RES, exist_ok=True)


def save(name, obj):
    with open(os.path.join(RES, name + ".json"), "w") as f:
        json.dump(obj, f, indent=1, default=float)
    print(name, "written")


def settle(Q, x0, T=20000, fn=M.step):
    x = np.asarray(x0, float)
    for t in range(T):
        x2 = fn(x, Q)
        if np.max(np.abs(x2 - x)) < 1e-13:
            return x2
        x = x2
    return x


def escapes(Q, rng, T=40000):
    """Iterate from a small random perturbation; True if it leaves symmetry."""
    x = rng.choice([-1.0, 1.0], 4) * rng.uniform(0.5, 1.0, 4) * 1e-5
    for t in range(T):
        x = M.step(x, Q)
        n = np.max(np.abs(x))
        if n > 1e-2:
            return True
        if n < 1e-10:
            return False
    return None


def e1():
    """Condition vs the nonlinear map on random parameter sets."""
    rng = np.random.default_rng(101)
    agree = total = undecided = skipped = 0
    n_unstable = 0
    for _ in range(2000):
        Q = random_Q(rng)
        lam = M.spectral_radius(M.jacobian(Q))
        if abs(lam - 1) < 0.01:
            skipped += 1
            continue
        esc = escapes(Q, rng)
        if esc is None:
            undecided += 1
            continue
        total += 1
        n_unstable += M.condition(Q)
        agree += (esc == M.condition(Q))
    # fixed points independent of rho and delta (one unstable example)
    base = M.params(dict(g=4.0), dict(g=4.0), theta=0.6, psi=1.0)
    fps = []
    for rho in (0.05, 0.2, 0.8):
        for d in (0.0, 0.5, 0.9):
            Q = M.params(dict(g=4.0, rho=rho, delta=d), dict(g=4.0, rho=rho, delta=d),
                         theta=0.6, psi=1.0)
            fps.append(settle(Q, [1e-3, 0, 1e-3, 0], T=200000).tolist())
    fps = np.array(fps)
    save("e1", dict(sets_tested=total, agree=agree, unstable=n_unstable,
                    skipped_near_threshold=skipped, undecided=undecided,
                    base_lambda=M.spectral_radius(M.jacobian(base)),
                    fixed_points_over_rho_delta=fps.tolist(),
                    fixed_point_spread=float(np.max(fps.max(0) - fps.min(0)))))


def scenario(name, Q):
    J = M.jacobian(Q)
    ev, V = np.linalg.eig(J)
    i = int(np.argmax(ev.real))
    v = np.real(V[:, i])
    v = v / v[np.argmax(np.abs(v))]
    LE, LP = M.loop_gains(Q)
    fp_plus = settle(Q, [1e-3, 0, 1e-3, 0], T=400000)
    fp_minus = settle(Q, [-1e-3, 0, -1e-3, 0], T=400000)
    # a start in which the two institutions lean opposite ways
    fp_cross = settle(Q, [1e-3, 0, -2e-3, 0], T=400000)
    return dict(name=name, theta=Q["theta"], omega=Q["omega"], chi=Q["chi"], psi=Q["psi"],
                g_E=Q["E"]["g"], g_P=Q["P"]["g"],
                Delta_E=M.margin(Q["E"]), Delta_P=M.margin(Q["P"]),
                L_E=LE, L_P=LP, round_trip=LE * LP, condition=bool(M.condition(Q)),
                spectral_radius=M.spectral_radius(J), leading_eigenvalue=float(ev[i].real),
                leading_vector_mE_aE_mP_aP=v.tolist(),
                fixed_point_from_plus=fp_plus.tolist(),
                fixed_point_from_minus=fp_minus.tolist(),
                fixed_point_from_opposite_leans=fp_cross.tolist())


def e2():
    """CLAIM-404's cases, each institution stable alone."""
    out = []
    # (a) A21's chain: evidence P->E and standing E->P, both institutions with
    # their own (sub-threshold) loop. Delta = 0.44 each; threshold theta*sigma*psi > 0.1936.
    out.append(scenario("a21_chain_below", M.params(dict(g=4.0), dict(g=4.0), theta=0.4, psi=1.0)))
    out.append(scenario("a21_chain_above", M.params(dict(g=4.0), dict(g=4.0), theta=0.6, psi=1.0)))
    # (b) neither institution has an internal loop (both g = 0, Regime B in each)
    out.append(scenario("no_internal_loops", M.params(dict(g=0.0), dict(g=0.0), theta=1.0, psi=1.6)))
    # (c) evaluator formally independent (Regime B, g_E = 0), party with its loop
    out.append(scenario("evaluator_regime_B", M.params(dict(g=0.0), dict(g=4.0), theta=1.0, psi=1.0)))
    # (d) informational independence (theta = 0), resources P->E (omega)
    out.append(scenario("info_independent_resources", M.params(dict(g=4.0), dict(g=4.0), omega=1.5, psi=1.0)))
    # (e) the return channel cut (psi = chi = 0): stable whatever theta, omega
    out.append(scenario("return_cut", M.params(dict(g=4.0), dict(g=4.0), theta=3.0, omega=3.0)))
    # (f) both institutions close to their own thresholds: a weak cross loop suffices
    out.append(scenario("near_own_thresholds", M.params(dict(g=9.0), dict(g=9.0), theta=0.1, psi=0.3)))
    save("e2", out)


def e3():
    """Linear response below threshold: a standing bias of the party's corpus
    (b0_P = 0.02) and the evaluator's reading."""
    rows = []
    for psi in np.linspace(0, 0.95, 20):
        Q = M.params(dict(g=4.0), dict(g=4.0, b0=0.02), theta=0.4, psi=float(psi) * 1.21)
        LE, LP = M.loop_gains(Q)
        fp = settle(Q, [0, 0, 0, 0], T=400000)
        dE, dP = M.response(Q)
        rows.append(dict(psi=Q["psi"], round_trip=LE * LP, mE_star=fp[0], mP_star=fp[2],
                         mE_linear=0.02 * dE, mP_linear=0.02 * dP,
                         mP_without_loop=0.02 / M.margin(Q["P"])))
    save("e3", rows)


def e4():
    """Agent-level: A21's chain below and above the two-institution threshold,
    each institution below its own (phi = 0.2, so Delta = 0.52 each and the
    threshold is theta * sigma * psi > 0.2704); from exact symmetry. Captured:
    |mean m_E| over the last 200 rounds above half the reduced captured m_E of
    the 'above' case."""
    out = {}
    T, seeds = 800, 200
    cases = (("below", 0.4, 1.0), ("near_below", 0.6, 1.0), ("above", 0.6, 1.6),
             ("well_above", 0.8, 2.0), ("return_cut", 0.8, 0.0))
    mk = lambda th, ps: M.params(dict(g=4.0, phi=0.2), dict(g=4.0, phi=0.2),
                                 theta=th, psi=ps, k=50)
    thr = 0.5 * abs(settle(mk(0.6, 1.6), [1e-3, 0, 1e-3, 0], T=400000)[0])
    for name, theta, psi in cases:
        Q = mk(theta, psi)
        LE, LP = M.loop_gains(Q)
        fp = settle(Q, [1e-3, 0, 1e-3, 0], T=400000)
        mE, mP, same = [], [], []
        t0 = time.time()
        for s in range(seeds):
            X = M.simulate_agents(Q, T, seed=s)
            last = X[-200:].mean(0)
            mE.append(last[0]); mP.append(last[2])
            same.append(bool(np.sign(last[0]) == np.sign(last[2])))
        mE, mP = np.abs(mE), np.abs(mP)
        out[name] = dict(theta=theta, psi=psi, round_trip=LE * LP,
                         condition=bool(M.condition(Q)),
                         reduced_fixed_point=fp.tolist(),
                         mean_abs_mE=float(mE.mean()), mean_abs_mP=float(mP.mean()),
                         max_abs_mE=float(mE.max()),
                         captured_share=float(np.mean(mE > thr)), capture_threshold=float(thr),
                         same_sign_share=float(np.mean(same)), seconds=time.time() - t0)
        print(name, out[name])
    save("e4", out)


def e5():
    """Alternatives: resources as capacity (multiplicative), and a corrective
    (negative) return channel."""
    res = {}
    # (i) multiplicative resources: linear threshold unchanged by omega
    lam = []
    for om in (0.0, 0.5, 1.0, 2.0):
        Q = M.params(dict(g=4.0), dict(g=4.0), theta=0.6, psi=1.0, omega=om,
                     resource_form="multiplicative")
        lam.append(dict(omega=om, spectral_radius=M.spectral_radius(M.jacobian_numeric(Q)),
                        fixed_point=settle(Q, [1e-3, 0, 1e-3, 0], T=400000).tolist()))
    # and below threshold, multiplicative resources cannot start it from symmetry
    Qb = M.params(dict(g=4.0), dict(g=4.0), theta=0.4, psi=1.0, omega=2.0,
                  resource_form="multiplicative")
    rng = np.random.default_rng(5)
    # bistability below the linear threshold: start far from symmetry, either way
    far = []
    for form, om in (("additive", 0.0), ("multiplicative", 2.0), ("multiplicative", 5.0)):
        for th, ps in ((0.3, 0.8), (0.4, 1.0), (0.6, 1.0)):
            Q = M.params(dict(g=4.0), dict(g=4.0), theta=th, psi=ps, omega=om,
                         resource_form=form)
            far.append(dict(form=form, omega=om, theta=th, psi=ps,
                            spectral_radius=M.spectral_radius(M.jacobian_numeric(Q)),
                            from_plus_0_9=settle(Q, [0.9] * 4, T=400000).tolist(),
                            from_minus_0_9=settle(Q, [-0.9] * 4, T=400000).tolist()))
    # informational independence (theta = 0) with resources as capacity only
    info0 = []
    for om in (2.0, 5.0, 10.0):
        for ps in (1.0, 2.0):
            Q = M.params(dict(g=4.0), dict(g=4.0), theta=0.0, psi=ps, omega=om,
                         resource_form="multiplicative")
            info0.append(dict(omega=om, psi=ps,
                              spectral_radius=M.spectral_radius(M.jacobian_numeric(Q)),
                              from_plus_0_9=settle(Q, [0.9] * 4, T=400000).tolist(),
                              from_minus_0_9=settle(Q, [-0.9] * 4, T=400000).tolist()))
    res["multiplicative"] = dict(above=lam, theta0_capacity_only=info0,
                                 below_omega2_spectral_radius=M.spectral_radius(M.jacobian_numeric(Qb)),
                                 below_omega2_escapes=escapes(Qb, rng),
                                 far_starts=far)
    # (ii) corrective return channel: random sign-mixed channels, each
    # institution stable alone; how often is the symmetric state unstable,
    # and how (real eigenvalue > 1, < -1, or complex pair)?
    rng = np.random.default_rng(55)
    counts = dict(tested=0, unstable=0, real_above_1=0, real_below_minus1=0, complex_pair=0)
    example = None
    for _ in range(20000):
        Q = random_Q(rng)
        Q["psi"] = -abs(Q["psi"]) * 3
        Q["chi"] = -abs(Q["chi"]) * 3
        J = M.jacobian(Q)
        ev = np.linalg.eigvals(J)
        counts["tested"] += 1
        j = int(np.argmax(np.abs(ev)))
        if abs(ev[j]) > 1 + 1e-9:
            counts["unstable"] += 1
            if abs(ev[j].imag) > 1e-9:
                counts["complex_pair"] += 1
                if example is None:
                    example = dict(Q={k: Q[k] for k in ("theta", "omega", "chi", "psi")},
                                   E=Q["E"], P=Q["P"], eigenvalue=[ev[j].real, ev[j].imag],
                                   modulus=abs(ev[j]))
            elif ev[j].real > 0:
                counts["real_above_1"] += 1
            else:
                counts["real_below_minus1"] += 1
    res["corrective_return"] = dict(counts=counts, example=example)
    save("e5", res)


EXPS = dict(e1=e1, e2=e2, e3=e3, e4=e4, e5=e5)

if __name__ == "__main__":
    names = sys.argv[1:] or list(EXPS)
    for n in names:
        t = time.time()
        EXPS[n]()
        print(n, "%.1fs" % (time.time() - t))
