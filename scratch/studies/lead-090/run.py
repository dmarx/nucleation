"""LEAD-090 experiments. Each writes results/<name>.json as it finishes.

python3 -I run.py [name ...]   (OMP_NUM_THREADS=1); about a minute in all.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(OUT, exist_ok=True)


def save(name, obj):
    with open(os.path.join(OUT, name + ".json"), "w") as f:
        json.dump(obj, f, indent=1, default=float)
    print(name, json.dumps(obj, default=float)[:600])


def rand_params(rng, **kw):
    sigma = rng.uniform(0.05, 0.6)
    phi = rng.uniform(0, 1 - sigma - 0.05)
    P = M.default_params(rho=rng.uniform(0.05, 0.9), sigma=sigma, phi=phi,
                         eps=rng.uniform(0, 1), g=rng.uniform(0, 40),
                         delta=rng.uniform(0, 0.98))
    P.update(kw)
    return P


def settle(fn, m0, a0, P, T=4000):
    return M.run_map(fn, m0, a0, P, T)[-1]


def e1_threshold():
    """Linear threshold against the nonlinear map, and the timescales' role."""
    rng = np.random.default_rng(10)
    agree = n = 0
    mism = []
    for _ in range(2000):
        P = rand_params(rng)
        J = M.jacobian_analytic(P)
        lam = max(abs(np.linalg.eigvals(J)))
        if abs(lam - 1) < 0.01:  # too slow to settle near the threshold
            continue
        m, a = settle(M.mean_field, 0.01, 0.0, P)
        captured = abs(a) > 0.02
        n += 1
        agree += captured == M.threshold_holds(P)
        if captured != M.threshold_holds(P):
            mism.append(dict(lam=lam, a=a))
    # fixed points do not depend on rho or delta
    base = dict(sigma=0.4, phi=0.3, eps=0.2, g=10.0)
    fps = []
    for rho in (0.05, 0.2, 0.8):
        for delta in (0.0, 0.5, 0.9, 0.98):
            P = M.default_params(rho=rho, delta=delta, **base)
            m, a = settle(M.mean_field, 0.01, 0.0, P, T=20000)
            lam = max(abs(np.linalg.eigvals(M.jacobian_analytic(P))))
            fps.append(dict(rho=rho, delta=delta, m=m, a=a, lam_plus=lam,
                            relax_time=-1 / np.log(lam) if lam < 1 else None))
    spread = max(f["a"] for f in fps) - min(f["a"] for f in fps)
    # Curie-Weiss form: a = tanh(J a), J = g sigma^2 / (2 (1 - phi'))
    P = M.default_params(**base)
    Jcw = P["g"] * P["sigma"] ** 2 / (2 * (1 - P["phi"] * (1 - P["eps"])))
    a = 0.5
    for _ in range(10000):
        a = np.tanh(Jcw * a)
    save("e1_threshold", dict(n=n, agree=agree, mismatches=mism[:10],
                              fixed_points=fps, a_spread_over_rho_delta=spread,
                              curie_weiss_J=Jcw, curie_weiss_a=a))


def e2_content_selected_capture():
    """Symmetric structure, a0 = 0: which specialist gains authority is set by
    the initial meaning bias. Mean field and agent-level."""
    P = M.default_params(g=10.0)
    mf = []
    for m0 in (-0.05, -0.01, -0.001, 0.001, 0.01, 0.05):
        for a0 in (-0.02, 0.0, 0.02):
            m, a = settle(M.mean_field, m0, a0, P)
            mf.append(dict(m0=m0, a0=a0, m_inf=m, a_inf=a))
    # agent-level, from the symmetric state: the direction is set by early noise
    T, seeds = 600, 200
    rows = []
    for s in range(seeds):
        tr = M.simulate_stochastic(0.5, 0.5, P, T, seed=s)
        m, a = (2 * tr - 1).T
        early = m[1:21].mean()
        rows.append(dict(seed=s, early_m=early, a_final=a[-1], m_final_mean=m[-100:].mean()))
    early = np.array([r["early_m"] for r in rows])
    af = np.array([r["a_final"] for r in rows])
    captured = np.abs(af) > 0.5
    agree_sign = np.mean(np.sign(early[captured]) == np.sign(af[captured]))
    # below threshold
    Pb = M.default_params(g=3.0)
    below = [abs(2 * M.simulate_stochastic(0.5, 0.5, Pb, T, seed=s)[-1, 1] - 1) for s in range(50)]
    # regime B
    PB = M.default_params(g=10.0, regime="B")
    regB = [abs(2 * M.simulate_stochastic(0.5, 0.5, PB, T, seed=s)[-1, 1] - 1) for s in range(50)]
    save("e2_capture", dict(params=P, mean_field=mf, seeds=seeds,
                            share_captured=captured.mean(),
                            share_A=float(np.mean(af > 0.5)), share_B=float(np.mean(af < -0.5)),
                            early_sign_agrees_with_winner=agree_sign,
                            mean_abs_m_final_captured=float(np.mean([abs(r["m_final_mean"]) for r, c in zip(rows, captured) if c])),
                            below_threshold_g3_max_abs_a=max(below),
                            regimeB_max_abs_a=max(regB)))


def e3_hysteresis():
    """Sweep the corpus imbalance b up then down, continuing from the last state."""
    P = M.default_params(g=10.0, delta=0.5)
    bs = np.round(np.linspace(-0.2, 0.2, 41), 4)
    path = list(bs) + list(bs[::-1])
    out = {}
    for label in ("case092", "bc_agreement", "bc_gaussian", "degroot_fixed"):
        m, a = -0.5, -0.9
        rec = []
        for b in path:
            Pb = dict(P, b=float(b))
            Q = M.to_bc_params(Pb)
            for _ in range(3000):
                if label == "case092":
                    m, a = M.mean_field(m, a, Pb)
                elif label == "bc_agreement":
                    m, a = M.adaptive_bc_step(m, a, Q, "agreement")
                elif label == "bc_gaussian":
                    m, a = M.adaptive_bc_step(m, a, Q, "gaussian")
                else:
                    a = 0.0
                    m = M.degroot_stubborn_step(m, a, Q)
            rec.append((float(b), float(m), float(a)))
        up = {b: (m, a) for b, m, a in rec[:len(bs)]}
        down = {b: (m, a) for b, m, a in rec[len(bs):]}
        gap = max(abs(up[b][0] - down[b][0]) for b in up)
        width = sum(abs(up[b][1] - down[b][1]) > 0.5 for b in up) * (bs[1] - bs[0])
        out[label] = dict(max_m_gap=gap, loop_width_in_b=float(width),
                          at_b0_up=up[0.0], at_b0_down=down[0.0])
    save("e3_hysteresis", dict(params=P, b_grid=[float(bs[0]), float(bs[-1]), len(bs)], results=out))


def e4_predecessors():
    """Reflected appraisal (DeGroot-Friedkin; Friedkin 2011) on the three-member
    system at symmetric structure: power never separates the specialists, and
    opinions do not enter the power map."""
    P = M.default_params()
    C = M.network_from_case(P, 0.0)
    res = {}
    for name, step in (("degroot_friedkin", M.degroot_friedkin_step),
                       ("friedkin2011", M.friedkin2011_step)):
        runs = []
        for x0 in ([1 / 3] * 3, [0.2, 0.4, 0.4], [0.6, 0.2, 0.2]):
            x = np.array(x0)
            for _ in range(500):
                x = step(x, C)
            runs.append(dict(x0=x0, x_final=x.tolist(), specialist_gap=abs(x[1] - x[2])))
        res[name] = runs
    # an asymmetric start: whom power favours is set by x0 and C, whatever the opinions
    x = np.array([0.2, 0.45, 0.35])
    xs = {}
    for name, step in (("degroot_friedkin", M.degroot_friedkin_step),
                       ("friedkin2011", M.friedkin2011_step)):
        y = x.copy()
        for _ in range(500):
            y = step(y, C)
        xs[name] = y.tolist()
    # CASE-092 regime B: authority trajectory identical for opposite meaning starts
    PB = M.default_params(regime="B", r=(0.75, 0.7))
    t1 = M.run_map(M.mean_field, 0.3, 0.0, PB, 500)[:, 1]
    t2 = M.run_map(M.mean_field, -0.3, 0.0, PB, 500)[:, 1]
    # CASE-092 regime A: opposite meaning starts give opposite winners
    PA = M.default_params(g=10.0)
    s1 = M.run_map(M.mean_field, 0.01, 0.0, PA, 4000)[-1]
    s2 = M.run_map(M.mean_field, -0.01, 0.0, PA, 4000)[-1]
    save("e4_predecessors", dict(symmetric_C=res, asymmetric_x0=xs,
                                 regimeB_authority_max_diff_opposite_m0=float(np.max(np.abs(t1 - t2))),
                                 regimeA_opposite_m0=[s1.tolist(), s2.tolist()]))


def e5_identifiability():
    """Different CASE-092 parameters with the same (lam, o, kappa, delta) give
    the same trajectories: the reduced form has four identifiable parameters."""
    P1 = M.default_params(rho=0.2, sigma=0.4, phi=0.3, eps=0.2, g=10.0)
    ph1 = P1["phi"] * (1 - P1["eps"])
    lam, o = P1["rho"] * (1 - ph1), P1["sigma"] / (1 - ph1)
    kap = P1["g"] * (1 - ph1) / 2
    # choose phi'=0.5 with eps=0: then rho, sigma, g follow
    ph2 = 0.5
    P2 = M.default_params(rho=lam / (1 - ph2), sigma=o * (1 - ph2), phi=ph2, eps=0.0,
                          g=2 * kap / (1 - ph2))
    t1 = M.run_map(M.mean_field, 0.05, -0.1, P1, 2000)
    t2 = M.run_map(M.mean_field, 0.05, -0.1, P2, 2000)
    save("e5_identifiability", dict(P1={k: P1[k] for k in ("rho", "sigma", "phi", "eps", "g")},
                                    P2={k: P2[k] for k in ("rho", "sigma", "phi", "eps", "g")},
                                    bc=dict(lam=lam, o=o, kappa=kap),
                                    max_traj_diff=float(np.max(np.abs(t1 - t2)))))


def e6_replicator():
    """The replicator reading of conferral: authority neutral alone, so any
    positive loop destabilizes symmetry."""
    rows = []
    for eta in (0.05, 0.2, 1.0):
        P = M.default_params(conferral="replicator", eta=eta)
        J = M.jacobian_analytic(P)
        lam = max(abs(np.linalg.eigvals(J)))
        m, a = settle(M.mean_field, 0.001, 0.0, P, T=40000)
        rows.append(dict(eta=eta, lam_plus=lam, m_inf=m, a_inf=a))
    save("e6_replicator", dict(rows=rows))


ALL = dict(e1_threshold=e1_threshold, e2=e2_content_selected_capture, e3=e3_hysteresis,
           e4=e4_predecessors, e5=e5_identifiability, e6=e6_replicator)

if __name__ == "__main__":
    for name in (sys.argv[1:] or ALL):
        ALL[name]()
