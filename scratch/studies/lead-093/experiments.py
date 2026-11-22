"""LEAD-093 experiments. Each writes one JSON line per item to
results/<name>.jsonl as it is produced, and skips items already written.

    OMP_NUM_THREADS=1 python3 -I experiments.py e1 e2 ...
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from closing import (params, produce_steady_states, stable, maintained_state,
                     closes, sigma_needed, run, y0_empty, critical, founding,
                     min_founding_time, persists_after_withdrawal,
                     run_generations, gillespie_extinction, background_N)

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
os.makedirs(RES, exist_ok=True)


def done_keys(name):
    path = os.path.join(RES, name + ".jsonl")
    keys = set()
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                keys.add(json.loads(line)["key"])
    return keys


def emit(name, rec):
    with open(os.path.join(RES, name + ".jsonl"), "a") as f:
        f.write(json.dumps(rec, default=float) + "\n")


def fl(x):
    return None if x is None or (isinstance(x, float) and not np.isfinite(x)) else float(x)


def classify(p):
    """'self-igniting': the only stable state is maintained (forms from
    nothing); 'bistable': a stable empty state and a stable maintained state
    (founding needed, the loop closes once founded); 'open': no maintained
    state without outside supply."""
    sts = produce_steady_states(p, 0.0)
    good = [s for s in sts if stable(p, s, 0.0)[0]]
    thr = 50 * background_N(p)
    maint = [s for s in good if s[2] >= thr]
    empty = [s for s in good if s[2] < thr]
    if maint and empty:
        return "bistable", maint[-1]
    if maint:
        return "self-igniting", maint[-1]
    return "open", None


# E1: phase diagram over constraint turnover kT and teaching rate beta
def e1():
    name = "e1_phase"
    done = done_keys(name)
    for kT in np.geomspace(0.02, 1.0, 25):
        for beta in np.geomspace(0.002, 0.1, 25):
            key = f"{kT:.6g}|{beta:.6g}"
            if key in done:
                continue
            cls, st = classify(params(kT=kT, beta=beta))
            emit(name, dict(key=key, kT=kT, beta=beta, cls=cls,
                            N=fl(st[2]) if st else None, T=fl(st[1]) if st else None))


# E2: the turnover the closed loop survives, against teaching rate, defect
# share and material supply
def e2():
    name = "e2_critical_turnover"
    done = done_keys(name)
    base = params()
    items = ([("beta", b) for b in [0.005, 0.01, 0.02, 0.04, 0.08]]
             + [("eps", e) for e in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]]
             + [("J", j) for j in [0.7, 0.8, 1.0, 1.5, 2.0, 4.0]])
    for key_name, v in items:
        key = f"{key_name}={v}"
        if key in done:
            continue
        q = params(**{key_name: v})
        kc = critical(q, "kT", 0.005, 10.0)
        emit(name, dict(key=key, param=key_name, value=v, kT_crit=fl(kc)))
    for key_name, lo, hi in [("eps", 0.0, 0.99), ("J", 0.01, 1.0), ("beta", 1e-4, 0.02)]:
        key = f"crit_{key_name}_at_base"
        if key in done:
            continue
        emit(name, dict(key=key, param=key_name, crit=fl(critical(base, key_name, lo, hi))))


# E3: outside supply still needed: material J for closure, and the standing
# teacher supply sigma to hold N at a declared level, with and without the loop
def e3():
    name = "e3_supply"
    done = done_keys(name)
    N_target = 2.0
    for kT in [0.02, 0.05, 0.1, 0.15, 0.19, 0.25, 0.4, 0.55, 0.7, 0.85, 1.0, 1.5]:
        key = f"kT={kT}"
        if key in done:
            continue
        p = params(kT=kT)
        Jc = critical(p, "J", 0.05, 20.0)
        s_loop, m1, T1 = sigma_needed(p, N_target)
        s_none, m0, T0 = sigma_needed(params(kT=kT, beta=0.0), N_target)
        st_loop = stable(params(kT=kT, sigma=s_loop), (m1, T1, N_target, 0.0), s_loop)[0]
        st_none = stable(params(kT=kT, beta=0.0, sigma=s_none), (m0, T0, N_target, 0.0), s_none)[0]
        ms = maintained_state(p)
        emit(name, dict(key=key, kT=kT, J_crit=fl(Jc), N_target=N_target,
                        sigma_with_loop=fl(s_loop), sigma_without_loop=fl(s_none),
                        T_with_loop=fl(T1), T_without_loop=fl(T0),
                        stable_with_loop=st_loop, stable_without_loop=st_none,
                        N_maintained_sigma0=fl(ms[2]) if ms else None,
                        self_share=fl(1 - s_loop / (kT * T1)) if T1 and T1 > 0 else None))


# E4: when the loop closes in time: shortest founding by an outside teacher
def e4():
    name = "e4_founding"
    done = done_keys(name)
    base = params()
    ms = maintained_state(base)
    items = [(0.1, s) for s in [0.01, 0.02, 0.05, 0.1, 0.3]] + \
            [(k, 0.05) for k in [0.03, 0.05, 0.08, 0.12, 0.15, 0.18]]
    for kT, sig in items:
        key = f"kT={kT}|sigma={sig}"
        if key in done:
            continue
        p = params(kT=kT)
        cls, st = classify(p)
        tw = min_founding_time(p, sig, t_hi=2000.0, tol=0.01)
        rec = dict(key=key, kT=kT, sigma=sig, cls=cls, t_w=fl(tw),
                   N_maint=fl(st[2]) if st else None)
        if np.isfinite(tw):
            q = params(kT=kT, sigma=sig)
            _, Y = run(q, y0_empty(p), max(tw, 1e-6), n_eval=2)
            m, T, N = Y[0, -1], Y[1, -1], Y[2, -1]
            rec.update(m_at_tw=m, T_at_tw=T, N_at_tw=N,
                       self_share_at_tw=p["beta"] * m * N / (p["beta"] * m * N + sig))
            # after withdrawal at tw (+1% to be on the safe side): time to half
            # of the maintained nucleus count
            tw2 = tw * 1.01 + 0.01
            t, Y2 = run(q, y0_empty(p), tw2, n_eval=2)
            t3, Y3 = run(p, Y2[:, -1], 3000.0, n_eval=30001)
            half = np.argmax(Y3[2] >= 0.5 * st[2]) if np.any(Y3[2] >= 0.5 * st[2]) else None
            rec["t_half_after_withdrawal"] = fl(tw2 + t3[half]) if half is not None else None
            # the same founding kept on: time to half
            t4, Y4 = run(q, y0_empty(p), 3000.0, n_eval=30001)
            h4 = np.argmax(Y4[2] >= 0.5 * st[2]) if np.any(Y4[2] >= 0.5 * st[2]) else None
            rec["t_half_supply_kept"] = fl(t4[h4]) if h4 is not None else None
        # comparator: no founding at all
        t5, Y5 = run(p, y0_empty(p), 3000.0, n_eval=3001)
        if st:
            h5 = np.argmax(Y5[2] >= 0.5 * st[2]) if np.any(Y5[2] >= 0.5 * st[2]) else None
            rec["t_half_no_founding"] = fl(t5[h5]) if h5 is not None else None
        emit(name, rec)


# E5: disturbance the closed loop survives without outside supply
def e5():
    name = "e5_disturbance"
    done = done_keys(name)
    p = params()
    ms = maintained_state(p)
    y_ms = np.array([ms[0], ms[1], ms[2], ms[3], 0.0])

    def survives(y):
        return persists_after_withdrawal(p, y, t_after=1500.0)

    for what in ["T", "N", "both"]:
        key = f"remove_{what}"
        if key in done:
            continue
        lo, hi = 0.0, 1.0
        while hi - lo > 1e-4:
            x = 0.5 * (lo + hi)
            y = y_ms.copy()
            if what in ("T", "both"):
                y[1] *= (1 - x)
            if what in ("N", "both"):
                y[2] *= (1 - x)
            if survives(y):
                lo = x
            else:
                hi = x
        emit(name, dict(key=key, removed=what, x_crit=0.5 * (lo + hi)))
    # a turnover pulse: kT raised to k2 for a time tau
    for k2 in [0.15, 0.2, 0.3, 0.5, 1.0, 3.0]:
        key = f"pulse_kT={k2}"
        if key in done:
            continue
        q = params(kT=k2)

        def ok(tau):
            _, Y = run(q, y_ms, tau, n_eval=2)
            return survives(Y[:, -1])
        if ok(2000.0):
            emit(name, dict(key=key, k2=k2, tau_crit=None, note="survives any duration"))
            continue
        lo, hi = 0.0, 2000.0
        while hi - lo > 0.01:
            mid = 0.5 * (lo + hi)
            if ok(mid):
                lo = mid
            else:
                hi = mid
        emit(name, dict(key=key, k2=k2, tau_crit=0.5 * (lo + hi)))


# E6: the repair arm: nuclei repair damaged teachers but make none
def e6():
    name = "e6_repair"
    done = done_keys(name)
    N_target = 2.0

    def steady(p, sig):
        q = dict(p)
        q["sigma"] = sig
        y = np.array([5.0, 3.0, 3.0, 0.0, 0.5])
        _, Y = run(q, y, 4000.0, n_eval=2)
        _, Y = run(q, Y[:, -1], 4000.0, n_eval=2)
        return Y[:, -1]

    for lam in [0.0, 0.01, 0.05, 0.2]:
        for rho in [0.0, 0.05, 0.2, 1.0, 5.0]:
            key = f"lam={lam}|rho={rho}"
            if key in done:
                continue
            p = params(arm="repair", rho=rho, lam=lam, beta=0.0)
            if lam == 0.0 and rho > 0:
                # no loss of damaged teachers: total teacher mass is conserved
                # with sigma = 0, so whether N persists depends on how much
                # teacher mass there is; report sigma = 0 from a state holding it
                y = steady(p, 0.0)
                emit(name, dict(key=key, lam=lam, rho=rho, sigma_needed=0.0,
                                N_at_sigma0=y[2], teacher_total=y[1] + y[4],
                                note="sigma=0 run from T+D=3.5"))
                continue
            lo, hi = 0.0, 2.0
            if steady(p, hi)[2] < N_target:
                emit(name, dict(key=key, lam=lam, rho=rho, sigma_needed=None))
                continue
            while hi - lo > 1e-5:
                mid = 0.5 * (lo + hi)
                if steady(p, mid)[2] >= N_target:
                    hi = mid
                else:
                    lo = mid
            y = steady(p, hi)
            # lifetime after withdrawal: time for N to fall to half
            t, Y = run(p, y, 5000.0, n_eval=50001)
            h = np.argmax(Y[2] <= 0.5 * y[2]) if np.any(Y[2] <= 0.5 * y[2]) else None
            emit(name, dict(key=key, lam=lam, rho=rho, sigma_needed=hi,
                            T=y[1], D=y[4], lamD=lam * y[4],
                            t_half_after_withdrawal=fl(t[h]) if h is not None else None))


# E7: successors matched on structure, differing in teaching
def e7():
    name = "e7_matched"
    done = done_keys(name)
    X = 3.0   # total nuclei N + B held by each system under supply
    for eps in [0.0, 0.3, 0.5, 0.6, 0.7, 0.9]:
        key = f"eps={eps}"
        if key in done:
            continue
        p = params(eps=eps)
        sig, m, T = sigma_needed(p, (1 - eps) * X)
        q = params(eps=eps, sigma=sig)
        # start from the supplied steady state and withdraw
        Ng, Bd = (1 - eps) * X, eps * X
        y = np.array([m, T, Ng, Bd, 0.0])
        _, Y = run(p, y, 3000.0, n_eval=2)
        emit(name, dict(key=key, eps=eps, total_nuclei=X, sigma_needed=sig,
                        m=m, T=T, good=Ng, defective=Bd,
                        total_after_withdrawal=Y[2, -1] + Y[3, -1],
                        persists=bool(Y[2, -1] + Y[3, -1] > 0.5 * X),
                        closes=closes(p)))


# E8: succession: students become teachers
def e8():
    name = "e8_succession"
    done = done_keys(name)
    p = params()
    for sig, tw in [(0.05, 12.0), (0.05, 100.0)]:
        key = f"sigma={sig}|tw={tw}"
        if key in done:
            continue
        G = 80
        t, m, T, N = run_generations(p, sig, tw, 1200.0, G=G, n_eval=1201)
        Ttot = T.sum(0)
        out_share = np.where(Ttot > 0, T[0] / np.maximum(Ttot, 1e-300), np.nan)
        gens = np.arange(G + 1)
        mean_gen = np.where(Ttot > 0, (gens[:, None] * T).sum(0) / np.maximum(Ttot, 1e-300), np.nan)
        i99 = np.argmax((out_share < 0.01) & (t > tw)) if np.any((out_share < 0.01) & (t > tw)) else None
        sel = (t >= 400) & (t <= 1000)
        rate = np.polyfit(t[sel], mean_gen[sel], 1)[0]
        snap = {str(int(tt)): dict(out_share=fl(out_share[i]), mean_gen=fl(mean_gen[i]),
                                   T=fl(Ttot[i]), N=fl(N.sum(0)[i]))
                for i, tt in enumerate(t) if int(tt) in (0, 5, 12, 25, 50, 100, 200, 400, 800, 1200) and abs(tt - int(tt)) < 1e-9}
        emit(name, dict(key=key, sigma=sig, t_w=tw,
                        t_students_make_99pct=fl(t[i99]) if i99 is not None else None,
                        gen_per_time_400_1000=rate, absorbing_share_end=fl(T[-1, -1] / Ttot[-1]),
                        snapshots=snap))


# E9: finite numbers: time to lose the loop after withdrawal
def e9(n_runs=40, t_max=20000.0):
    name = "e9_stochastic"
    done = done_keys(name)
    for kT in [0.1, 0.15]:
        p = params(kT=kT)
        ms = maintained_state(p)
        for omega in [1, 2, 4, 8, 12]:
            for r in range(n_runs):
                key = f"kT={kT}|omega={omega}|run={r}"
                if key in done:
                    continue
                rng = np.random.default_rng(1000 * omega + r + int(kT * 1e4))
                y = (round(ms[0] * omega), round(ms[1] * omega), round(ms[2] * omega))
                t0 = time.time()
                te = gillespie_extinction(p, omega, y, t_max, rng)
                emit(name, dict(key=key, kT=kT, omega=omega, run=r, start=y,
                                t_ext=te, censored=bool(te >= t_max), wall=time.time() - t0))


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        t0 = time.time()
        globals()[arg]()
        print(arg, "done in", round(time.time() - t0, 1), "s", flush=True)
