"""LEAD-098 study runner. Each item's result is appended to results.jsonl as soon as it is
computed; a rerun skips items already written. Usage: python3 -I run.py [results.jsonl]"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sim import (connection_laplacian, cycle_holonomies, drive_frame_phase, edges,
                 fit_linear_response, frustrate, gauge_maps, incompatibility, kron_reduce,
                 null_space, observed_offsets, order_parameter, pairwise_expressible, plv,
                 response_matrix, ring_with_chords, sheaf_laplacian, simulate)

N = 8
A = ring_with_chords(N)
RNG = np.random.default_rng(98)
OMEGA_J = 1.0 + 0.05 * RNG.standard_normal(N)          # heterogeneous natural frequencies
PHI_APP = RNG.uniform(0, 2 * np.pi, N)                  # the apparatus's section
PHI_OTHER = RNG.uniform(0, 2 * np.pi, N)                # what "other" coupling enforces
TH_APP = gauge_maps(PHI_APP, A)
TH_OTHER = gauge_maps(PHI_OTHER, A)
Z0 = 0.7 * np.exp(1j * RNG.uniform(0, 2 * np.pi, (4, N)))  # four initial conditions
DT = 0.01


def f(x):
    return float(np.round(x, 6))


def tail(a, frac=0.2):
    return a[int(len(a) * (1 - frac)):]


def inst_freq_spread(out):
    ph = np.unwrap(np.angle(out["z"]), axis=0)
    t = out["t"]
    h = len(t) // 2
    fr = (ph[-1] - ph[h]) / (t[-1] - t[h])  # (B, N)
    return float(np.mean(fr.std(1)))


def kick(j, d, batch):
    def fn(st):
        st["z"][batch, j] *= np.exp(1j * d)
    return fn


# ------------------------------------------------------------------ items

def regime(name, *, K, theta, ctype="diss", F=0.0, psi=None, th_app=TH_APP, mu=0.5):
    """CASE-179's regime table. Batch: 4 initial conditions, plus a paired copy of the
    first with unit 0 kicked by 1 rad at t=150 (localized intervention)."""
    T = 200.0
    z0 = np.vstack([Z0, Z0[:1]])
    out = simulate(N, A, T, DT, K=K, theta=theta, ctype=ctype, mu=mu, omega=OMEGA_J, F=F,
                   psi=psi, sigma=0.002, z0=z0, B=5, seed=1, every=20,
                   schedule=[(150.0, kick(0, 1.0, 4))])
    z = out["z"]
    t = out["t"]
    inc_app = np.array([incompatibility(z[i], A, th_app) for i in range(len(t))])  # (T,B)
    inc_cpl = np.array([incompatibility(z[i], A, theta) for i in range(len(t))])
    pre = t < 150
    L_app = connection_laplacian(A, th_app, 1.0)
    ev = np.linalg.eigvalsh(L_app)
    # localized intervention: does the kicked copy return to its control?
    dphi = np.abs(np.angle(z[:, 4] * np.conj(z[:, 0])))  # (T,N)
    i150 = np.searchsorted(t, 150.0)
    # decay rate of the kick's non-collective part (linear regime), t in (150.2, 165)
    dd = np.angle(z[:, 4] * np.conj(z[:, 0]))
    dd = dd - np.angle(np.exp(1j * dd).mean(1, keepdims=True))
    wk = (t > 150.1) & (t < 165)
    nrm = np.sqrt((dd[wk] ** 2).sum(1)) + 1e-300
    rate = -np.polyfit(t[wk], np.log(nrm), 1)[0]
    return {
        "regime": name, "K": K, "ctype": ctype, "F": F,
        "max_hol_app": f(np.abs(cycle_holonomies(A, th_app)).max()),
        "max_hol_cpl": f(np.abs(cycle_holonomies(A, theta)).max()),
        "lam_min_app_K1": f(ev[0]), "gap_app_K1": f(ev[1]),
        "lam_min_cpl_K1": f(np.linalg.eigvalsh(connection_laplacian(A, theta, 1.0))[0]),
        "incompat_app_final": f(tail(inc_app[pre][:, :4]).mean()),
        "incompat_cpl_final": f(tail(inc_cpl[pre][:, :4]).mean()),
        "incompat_cpl_spread_over_ics": f(tail(inc_cpl[pre][:, :4]).mean(0).std()),
        "kick_noncollective_decay_rate": f(rate),
        "plv_late": f(np.mean([plv(z[(t > 100) & pre, b]) for b in range(4)])),
        "freq_spread_late": f(inst_freq_spread({"t": t[pre], "z": z[pre][:, :4]})),
        "mean_amp": f(np.abs(z[pre][-10:, :4]).mean()),
        "kick_dev_first_sample_after": f(dphi[i150 + 1].max()),
        "kick_dev_final_unit0": f(dphi[-1, 0]),
        "kick_collective_shift_final": f(abs(np.angle(np.exp(1j * np.angle(z[-1, 4] * np.conj(z[-1, 0]))).mean()))),
        "kick_dev_final_others": f(dphi[-1, 1:].max()),
        "kick_dev_others_peak": f(dphi[i150:, 1:].max()),
    }


def withdrawal(name, *, K, mu, u=0.0, t_w=150.0, withdraw_u=False, T=300.0):
    """A12's forcing-withdrawal and suppression arms on the network."""
    sched = []

    def wd(st):
        st["F"][:] = 0.0
        if withdraw_u:
            st["u"][:] = 0.0
    sched.append((t_w, wd))
    out = simulate(N, A, T, DT, K=K, theta=TH_APP, mu=mu, u=u, omega=OMEGA_J, F=0.2,
                   psi=PHI_APP, sigma=0.002, z0=Z0, B=4, seed=2, every=20, schedule=sched)
    z, t = out["z"], out["t"]
    zr = z * np.exp(-1j * PHI_APP)  # in the apparatus's gauge: a section is in-phase
    pre = (t > 100) & (t < t_w)
    post = t > T - 50
    ph_drive = drive_frame_phase(zr, t, 1.0)  # (T,B,N)
    coll = np.angle(np.exp(1j * ph_drive).mean(2))  # collective phase vs drive clock
    drift = np.abs(np.unwrap(coll[post], axis=0)[-1] - np.unwrap(coll[post], axis=0)[0]).mean()
    return {
        "arm": name, "K": K, "mu": mu, "u": u, "withdraw_u": withdraw_u,
        "amp_driven": f(np.abs(z[pre]).mean()),
        "R_driven": f(np.mean([order_parameter(zr[i]) for i in np.where(pre)[0]])),
        "incompat_driven": f(np.mean([incompatibility(z[i], A, TH_APP) for i in np.where(pre)[0]])),
        "amp_after": f(np.abs(z[post]).mean()),
        "R_after": f(np.mean([order_parameter(zr[i]) for i in np.where(post)[0]])),
        "incompat_after": f(np.mean([incompatibility(z[i], A, TH_APP) for i in np.where(post)[0]])),
        "collective_phase_drift_vs_drive_last50": f(drift),
        "collective_phase_spread_over_ics_after": f(np.abs(np.exp(1j * coll[-1]).mean())),
    }


def adaptive(name, *, schedule_kind, T=800.0):
    """A12's adaptive-capacity arm: mu_j maintained by neighbours' activity."""
    ad = dict(eps=0.02, mumax=1.5, a0=0.2, c=0.2)
    sched = []
    if schedule_kind == "short_suppression":
        sched = [(200.0, lambda st: st["u"].__setitem__(slice(None), 2.0)),
                 (220.0, lambda st: st["u"].__setitem__(slice(None), 0.0))]
    elif schedule_kind == "long_suppression":
        sched = [(200.0, lambda st: st["u"].__setitem__(slice(None), 2.0)),
                 (500.0, lambda st: st["u"].__setitem__(slice(None), 0.0))]
    elif schedule_kind == "knockout_all":
        sched = [(200.0, lambda st: st["produce"].__setitem__(slice(None), 0.0))]
    elif schedule_kind == "knockout_unit0":
        def ko(st):
            st["produce"][:, 0] = 0.0
        sched = [(200.0, ko)]
    elif schedule_kind == "knockout_unit0_then_decouple":
        def ko(st):
            st["produce"][:, 0] = 0.0
        sched = [(200.0, ko), (600.0, lambda st: st["K"].__setitem__(slice(None), 0.0))]
    out = simulate(N, A, T, DT, K=0.3, theta=TH_APP, mu=1.0, omega=OMEGA_J, F=0.0,
                   sigma=0.002, z0=Z0[:2], B=2, seed=3, every=50, schedule=sched, adapt=ad)
    z, t, mu = out["z"], out["t"], out["mu"]

    def at(tt):
        i = min(np.searchsorted(t, tt), len(t) - 1)
        return f(np.abs(z[i]).mean()), f(mu[i].mean()), f(mu[i][:, 0].mean()), f(np.abs(z[i][:, 0]).mean())
    keys = [190, 215, 495, 590, 790]
    r = {"arm": name, "schedule": schedule_kind}
    for k in keys:
        a, m, m0, a0 = at(k)
        r[f"t{k}"] = {"amp": a, "mu": m, "mu_unit0": m0, "amp_unit0": a0}
    return r


def drive_systems():
    return {
        "common_drive_uncoupled": dict(K=0.0, F=0.2, psi=PHI_APP),
        "drive_plus_coupling_K0.3": dict(K=0.3, F=0.2, psi=PHI_APP),
        "drive_plus_coupling_K1": dict(K=1.0, F=0.2, psi=PHI_APP),
        "coupled_no_drive_K1": dict(K=1.0, F=0.0, psi=PHI_APP),
    }


def displacement(sysname):
    """QUESTION-063: displace the shared drive for member 0 only (its drive phase is shifted
    by pi/2 at t=100), paired with an undisplaced control under the same noise."""
    p = drive_systems()[sysname]
    if p["F"] == 0:
        return {"system": sysname, "skipped": "no drive to displace"}

    def disp(st):
        st["psi"][1, 0] += np.pi / 2
    out = simulate(N, A, 220.0, DT, theta=TH_APP, mu=0.5, omega=OMEGA_J, sigma=0.002,
                   z0=Z0[:1], B=2, seed=4, every=20, schedule=[(100.0, disp)], **p)
    z = out["z"]
    d = np.angle(z[-1, 1] * np.conj(z[-1, 0]))  # steady phase shift per unit
    dist = shortest_dist(0)
    return {"system": sysname, "shift_unit0": f(d[0]),
            "shift_by_distance": {str(k): f(np.mean(d[dist == k])) for k in sorted(set(dist)) if k > 0},
            "mean_abs_shift_others": f(np.abs(d[1:]).mean()),
            "follow_fraction": f(np.abs(d[1:]).mean() / max(abs(d[0]), 1e-9))}


def shortest_dist(src):
    dist = np.full(N, -1)
    dist[src] = 0
    q = [src]
    for v in q:
        for w in range(N):
            if A[v, w] and dist[w] < 0:
                dist[w] = dist[v] + 1
                q.append(w)
    return dist


def perturbation(sysname):
    """QUESTION-063: kick member 0 by 1 rad at t=100; measure the others."""
    p = drive_systems()[sysname]
    out = simulate(N, A, 160.0, DT, theta=TH_APP, mu=0.5, omega=OMEGA_J, sigma=0.002,
                   z0=Z0[:1], B=2, seed=5, every=5, schedule=[(100.0, kick(0, 1.0, 1))], **p)
    z, t = out["z"], out["t"]
    d = np.angle(z[:, 1] * np.conj(z[:, 0]))
    w = t >= 100
    dw = d[w]
    tt = t[w] - 100
    # recovery time of unit 0 to 1/e
    rec = tt[np.argmax(np.abs(dw[:, 0]) < np.exp(-1))] if np.any(np.abs(dw[1:, 0]) < np.exp(-1)) else None
    return {"system": sysname, "peak_response_others": f(np.abs(dw[:, 1:]).max()),
            "neighbour_peak": f(np.abs(dw[:, [1, 7, 4]]).max()),
            "final_dev_unit0": f(abs(dw[-1, 0])), "final_dev_others": f(np.abs(dw[-1, 1:]).max()),
            "unit0_recovery_time": None if rec is None else f(rec),
            "collective_shift_final": f(np.angle(np.exp(1j * dw[-1]).mean()))}


def observational_tests(sysname):
    """QUESTION-035's passive tests: timing (PLV), gluing (holonomy of observed offsets),
    and coupling gains fitted from noise-driven fluctuations, with the drive unrecorded
    (no pinning term) and recorded (pinning to the drive clock allowed)."""
    p = drive_systems()[sysname]
    out = simulate(N, A, 1000.0, DT, theta=TH_APP, mu=0.5, omega=OMEGA_J, sigma=0.03,
                   z0=Z0[:1], B=1, seed=6, every=10, **p)
    z, t = out["z"][100:, 0], out["t"][100:]
    th_obs = observed_offsets(z, A)
    hol = np.abs(cycle_holonomies(A, th_obs)).max()
    # deviations around mean offsets, in the drive clock frame
    ph = np.unwrap(np.angle(z * np.exp(-1j * 1.0 * t)[:, None]), axis=0)
    if p["F"] == 0:
        ph = ph - ph.mean(1, keepdims=True)  # no clock: take the collective frame
    dev = ph - ph.mean(0)
    dts = t[1] - t[0]
    g_un, _ = fit_linear_response([dev], dts, A, pin=False, ridge=1e-6)
    res = {"system": sysname, "plv": f(plv(z)), "observed_offsets_max_holonomy": f(hol),
           "fit_gain_mean_drive_unrecorded": f(np.mean(list(g_un.values())))}
    if p["F"] > 0:
        g_pin, pin = fit_linear_response([dev], dts, A, pin=True, ridge=1e-6)
        res["fit_gain_mean_drive_recorded"] = f(np.mean(list(g_pin.values())))
        res["fit_pin_mean_drive_recorded"] = f(np.mean(pin))
    return res


def revision(sysname):
    """CASE-179's third manipulation. The apparatus predicts the phase response of every
    unit to a kick on one unit. Initial model: maps 0, unit gains on all edges, no pinning.
    - none: initial model.
    - consistency: maps revised to the observed offsets (coherence reached); gains kept,
      since a coherent network is read as a coupled one.
    - checked: gains and pinning fitted from kicks the apparatus chooses (units 0-3); the
      revision is kept only if it improves prediction on held-out kicks (units 4-7) that
      the experimenter chooses."""
    p = drive_systems()[sysname]
    B = 1 + N
    sched = [(100.0, kick(j, 0.3, 1 + j)) for j in range(N)]
    out = simulate(N, A, 130.0, DT, theta=TH_APP, mu=0.5, omega=OMEGA_J, sigma=0.002,
                   z0=Z0[:1], B=B, seed=7, every=5, schedule=sched, **p)
    z, t = out["z"], out["t"]
    w = t >= 100
    trajs = [np.angle(z[w, 1 + j] * np.conj(z[w, 0])) for j in range(N)]  # (T,N) each
    dts = t[1] - t[0]
    obs_th = observed_offsets(z[(t > 50) & (t < 100), 0], A)
    inc_before = float(incompatibility(z[t < 100][-1, 0], A, np.zeros((N, N)))[0])
    inc_after = float(incompatibility(z[t < 100][-1, 0], A, obs_th)[0])
    horizons = [2.0, 5.0, 10.0]
    idx = [int(round(h / dts)) for h in horizons]

    def err(g, pn, units):
        num = den = 0.0
        for j in units:
            for h, i in zip(horizons, idx):
                pred = response_matrix(g, pn, N, h)[:, j] * 0.3
                obs = trajs[j][i]
                num += ((pred - obs) ** 2).sum()
                den += (obs ** 2).sum()
        return float(np.sqrt(num / den))
    g0 = {e: 1.0 for e in edges(A)}
    p0 = np.zeros(N)
    train, held = range(4), range(4, 8)
    e_none = err(g0, p0, held)
    e_cons = err(g0, p0, held)  # revised maps do not change the linearized phase model
    gf, pf = fit_linear_response([trajs[j] for j in train], dts, A, pin=True, ridge=1e-4)
    e_fit = err(gf, pf, held)
    accepted = e_fit < e_none
    return {"system": sysname, "incompat_initial_maps": f(inc_before),
            "incompat_consistency_maps": f(inc_after),
            "heldout_err_none": f(e_none), "heldout_err_consistency": f(e_cons),
            "heldout_err_checked_candidate": f(e_fit), "checked_accepted": bool(accepted),
            "heldout_err_checked": f(e_fit if accepted else e_none),
            "fitted_gain_mean": f(np.mean(list(gf.values()))), "fitted_pin_mean": f(np.mean(pf))}


def holonomy_item(h, ctype="diss", K=1.0, gauge="G1", eta=0.0, T=300.0):
    """QUESTION-319: one coupling, maps with holonomy h on the cycle through edge (0,1),
    in several dynamics. Response to kicks on each unit (paired) gives a response matrix."""
    base = TH_APP if gauge == "G1" else TH_OTHER
    th = frustrate(base, 0, 1, h)
    B = 1 + N
    sched = [(T - 50.0, kick(j, 0.3, 1 + j)) for j in range(N)]
    out = simulate(N, A, T, DT, K=K, theta=th, ctype=ctype, mu=0.5,
                   omega=np.ones(N) if ctype == "diss" else OMEGA_J, sigma=0.0005,
                   z0=Z0[:1], B=B, seed=8, every=20, schedule=sched,
                   plastic=dict(eta=eta) if eta else None)
    z, t = out["z"], out["t"]
    i_k = np.searchsorted(t, T - 50.0)
    i_r = np.searchsorted(t, T - 45.0)
    Rm = np.array([np.angle(z[i_r, 1 + j] * np.conj(z[i_r, 0])) for j in range(N)]).T / 0.3
    th_final = out["theta"][i_k - 1, 0] if eta else th
    r = {"h": f(h), "ctype": ctype, "K": K, "gauge": gauge, "eta": eta,
         "hol_initial": [f(x) for x in cycle_holonomies(A, th)],
         "hol_final": [f(x) for x in cycle_holonomies(A, th_final)],
         "lam_min": f(np.linalg.eigvalsh(connection_laplacian(A, th_final, 1.0))[0]),
         "residual_incompat": f(incompatibility(z[i_k - 1, 0], A, th_final)[0]),
         "plv": f(plv(z[(t > T - 100) & (t < T - 50), 0])),
         "response_matrix_t5": [[f(x) for x in row] for row in Rm]}
    return r


def sheaf_item(d_int, trial):
    """QUESTION-283: a star of one interior vertex (stalk R^d) and three scalar boundary
    vertices, plus one boundary-boundary edge, random restriction maps. After Kron
    reduction of the interior, is the boundary section space expressible pairwise?"""
    rng = np.random.default_rng(1000 * d_int + trial)
    maps = [(0, k, rng.standard_normal((1, d_int)), rng.standard_normal((1, 1))) for k in (1, 2, 3)]
    maps.append((1, 2, rng.standard_normal((1, 1)), rng.standard_normal((1, 1))))
    L, off = sheaf_laplacian([d_int, 1, 1, 1], maps)
    keep = np.arange(d_int, d_int + 3)
    S = null_space(kron_reduce(L, keep))
    # also the star alone (no boundary edge)
    L2, _ = sheaf_laplacian([d_int, 1, 1, 1], maps[:3])
    S2 = null_space(kron_reduce(L2, keep))
    blocks = [np.array([0]), np.array([1]), np.array([2])]
    dS, dP = pairwise_expressible(S, blocks)
    dS2, dP2 = pairwise_expressible(S2, blocks)
    return {"d_int": d_int, "trial": trial, "dimS": dS, "dimP": dP, "star_dimS": dS2, "star_dimP": dP2}


def items():
    yield "regime:compat_weak_diss", lambda: regime("compatible, weak dissipative", K=0.005, theta=TH_APP)
    yield "regime:compat_strong_enforcing", lambda: regime("compatible, strong dissipative enforcing the maps", K=1.0, theta=TH_APP)
    yield "regime:compat_strong_other", lambda: regime("compatible, strong dissipative enforcing other relations", K=1.0, theta=TH_OTHER)
    yield "regime:compat_conservative", lambda: regime("compatible, conservative", K=1.0, theta=TH_APP, ctype="cons")
    yield "regime:frustrated_strong", lambda: regime("frustrated (holonomy 0.8 pi), strong dissipative", K=1.0, theta=frustrate(TH_APP, 0, 1, 0.8 * np.pi), th_app=frustrate(TH_APP, 0, 1, 0.8 * np.pi))
    yield "regime:common_drive_uncoupled", lambda: regime("common drive, no reciprocal coupling", K=0.0, theta=TH_APP, F=0.2, psi=PHI_APP)
    yield "regime:drive_plus_coupling", lambda: regime("common drive with coupling K=0.3", K=0.3, theta=TH_APP, F=0.2, psi=PHI_APP)
    for s in drive_systems():
        yield f"displace:{s}", (lambda s=s: displacement(s))
        yield f"perturb:{s}", (lambda s=s: perturbation(s))
        yield f"revision:{s}", (lambda s=s: revision(s))
    for name, kw in [("coupled self-sustained", dict(K=0.3, mu=0.5)),
                     ("coupled damped", dict(K=0.3, mu=-0.2)),
                     ("uncoupled self-sustained", dict(K=0.0, mu=0.5)),
                     ("uncoupled damped", dict(K=0.0, mu=-0.2)),
                     ("coupled suppressed, withdraw drive only", dict(K=0.3, mu=0.5, u=1.0)),
                     ("coupled suppressed, withdraw drive and control", dict(K=0.3, mu=0.5, u=1.0, withdraw_u=True))]:
        yield f"withdraw:{name}", (lambda name=name, kw=kw: withdrawal(name, **kw))
    for kind in ["none", "short_suppression", "long_suppression", "knockout_all",
                 "knockout_unit0", "knockout_unit0_then_decouple"]:
        yield f"adaptive:{kind}", (lambda kind=kind: adaptive(kind, schedule_kind=kind))
    for s in drive_systems():
        yield f"observe:{s}", (lambda s=s: observational_tests(s))
    for h in [0.0, 0.25 * np.pi, 0.5 * np.pi, 0.8 * np.pi]:
        yield f"holonomy:diss:{h:.3f}", (lambda h=h: holonomy_item(h))
    yield "holonomy:diss:0.000:G2", lambda: holonomy_item(0.0, gauge="G2")
    yield "holonomy:diss:2.513:G2", lambda: holonomy_item(0.8 * np.pi, gauge="G2")
    yield "holonomy:weak:2.513", lambda: holonomy_item(0.8 * np.pi, K=0.005)
    yield "holonomy:plastic:2.513", lambda: holonomy_item(0.8 * np.pi, eta=0.05, T=600.0)
    for d in (1, 2, 3):
        for tr in range(100):
            yield f"sheaf:{d}:{tr}", (lambda d=d, tr=tr: sheaf_item(d, tr))


def main(path):
    done = set()
    if os.path.exists(path):
        with open(path) as fh:
            for line in fh:
                try:
                    done.add(json.loads(line)["item"])
                except Exception:
                    pass
    with open(path, "a") as fh:
        for key, fn in items():
            if key in done:
                continue
            t0 = time.time()
            r = fn()
            r = {"item": key, "secs": round(time.time() - t0, 2), **r}
            fh.write(json.dumps(r) + "\n")
            fh.flush()
            print(key, r["secs"], flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.jsonl"))
