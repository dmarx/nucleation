"""LEAD-049 numerical study. Three parts; results go to results/.

  part1  theorem B with fixed traits: random nonnegative U, exact -i communities
  part2  theorems A and C: Gaussian niches, k operators started almost identical
  part3  the two-resource trade-off: when re-adaptation closes a vacated niche

Run:  python3 -I study.py [part1|part2|part3|all]
"""
import json
import os
import sys
import time
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np

import model as M

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")
EPS, DT = 0.1, 0.02


def dump(name, obj):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w") as fh:
        json.dump(obj, fh, indent=1)


# ------------------------------------------------------------------ part 1

def lv_simulate(A, r, n0, T=400.0, dt=0.01):
    logn = np.log(np.maximum(n0, 1e-300))
    for _ in range(int(T / dt)):
        def f(lg):
            return r - A @ np.exp(lg)
        k1 = f(logn); k2 = f(logn + 0.5 * dt * k1); k3 = f(logn + 0.5 * dt * k2); k4 = f(logn + dt * k3)
        logn = logn + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return np.exp(logn)


def part1(n_inst=2000, n_sim=30):
    rng = np.random.default_rng(49)
    rows = []
    for t in range(n_inst):
        k = int(rng.integers(2, 7))
        U = rng.uniform(0, 1, (7, k)) ** 2  # sparse-ish nonnegative niches
        A = U.T @ U
        nstar = rng.uniform(0.02, 1.0, k)
        r = A @ nstar
        lmin = float(np.linalg.eigvalsh(A)[0])
        for i in range(k):
            lam, bound, sec, nt = M.invasion_frozen(A, r, nstar, i)
            rows.append(dict(inst=t, k=k, i=i, lam=lam, bound=bound, secondary=sec,
                             spectral=float(nstar[i] * lmin)))
    # dynamic confirmation on a subset: simulate the -i community, then reinvasion from 1e-6
    sims = []
    for t in range(n_sim):
        k = int(rng.integers(2, 6))
        U = rng.uniform(0, 1, (7, k)) ** 2
        A = U.T @ U
        nstar = rng.uniform(0.1, 1.0, k)
        r = A @ nstar
        i = int(rng.integers(k))
        Am, rm = np.delete(np.delete(A, i, 0), i, 1), np.delete(r, i)
        nres = lv_simulate(Am, rm, np.full(k - 1, 0.5))
        lam_sim = float(r[i] - np.delete(A[i], i) @ nres)
        lam, bound, sec, _ = M.invasion_frozen(A, r, nstar, i)
        n0 = np.insert(nres, i, 1e-6)
        nback = lv_simulate(A, r, n0, T=2000.0, dt=0.02)
        sims.append(dict(k=k, i=i, lam_exact=lam, lam_sim=lam_sim,
                         recovered=float(nback[i] / nstar[i]),
                         dist_to_nstar=float(np.max(np.abs(nback - nstar)))))
    lam = np.array([r_["lam"] for r_ in rows]); bd = np.array([r_["bound"] for r_ in rows])
    sec = np.array([r_["secondary"] for r_ in rows]); sp = np.array([r_["spectral"] for r_ in rows])
    summary = dict(
        n_instances=n_inst, n_pairs=len(rows),
        all_positive=bool(np.all(lam > 0)),
        all_above_bound=bool(np.all(lam >= bd - 1e-9)),
        all_above_spectral=bool(np.all(lam >= sp - 1e-9)),
        n_secondary=int(sec.sum()),
        max_abs_gap_without_secondary=float(np.max(np.abs(lam - bd)[~sec])),
        min_ratio_with_secondary=float(np.min((lam / bd)[sec])) if sec.any() else None,
        median_ratio_with_secondary=float(np.median((lam / bd)[sec])) if sec.any() else None,
        median_bound_over_spectral=float(np.median(bd / sp)),
        sims=dict(n=n_sim,
                  max_abs_lam_error=float(max(abs(s["lam_sim"] - s["lam_exact"]) for s in sims)),
                  min_recovered_fraction=float(min(s["recovered"] for s in sims)),
                  max_dist_to_nstar=float(max(s["dist_to_nstar"] for s in sims))))
    dump("part1_summary.json", summary)
    dump("part1_sims.json", sims)
    return summary


# ------------------------------------------------------------------ part 2

# Seeds differ only by the 1e-3 starting noise, and at k = 2 all three gave
# identical endpoints, so k >= 4 runs one seed (the CPU is shared).
PART2_JOBS = ([(k, w, s) for k in (2, 3) for w in (0.08, 0.12, 0.2) for s in range(3)]
              + [(k, w, 0) for k in (4, 5, 6) for w in (0.08, 0.12, 0.2)])


def part2_one(args):
    k, w, seed = args
    nic = M.GaussianNiche(m=12, w=w)
    b = np.ones(12)
    rng = np.random.default_rng(1000 * k + seed + int(100 * w))
    c = np.full(k, 0.2)
    n, th = M.simulate(nic, b, c, np.full(k, 0.3), 0.5 + 1e-3 * rng.normal(size=k), EPS, T=400, dt=DT)
    alive = n > 1e-6
    rec = dict(k=k, w=w, seed=seed, n_survivors=int(alive.sum()))
    n, th, c = n[alive], th[alive], c[alive]
    kk = len(n)
    g = np.concatenate(M.grad(nic, b, c, n, th))
    free = M.free_coordinates(nic, b, n, th)
    rec["grad_norm_free"] = float(np.linalg.norm(g[free]))
    rec["min_trait_gap"] = float(np.min(np.diff(np.sort(th)))) if kk > 1 else None
    rec["theorem_A"] = M.theorem_A_check(nic, b, c, n, th, EPS)
    U = nic.u(th)
    A, r = U.T @ U, U.T @ b - c
    rec["gram_min_eig"] = float(np.linalg.eigvalsh(A)[0])
    Lstar = M.potential(nic, b, c, n, th)
    rem = []
    for i in range(kk):
        lam_f, bound, sec, nt = M.invasion_frozen(A, r, n, i)
        keep = np.ones(kk, bool); keep[i] = False
        # residents re-adapt in i's absence
        n_ad, th_ad = M.simulate(nic, b, c, n, th, EPS, T=400, dt=DT, alive=keep)
        th_probe = th_ad.copy(); th_probe[i] = th[i]
        lam_ad = float(M.growth(nic, b, c, n_ad, th_probe)[i])
        # cond C: the frozen -i community meets theorem A for the -i system
        cC = M.theorem_A_check(nic, b, c[keep], nt[keep], th[keep], EPS)
        # reinvasion from 1e-6 with full adaptive dynamics
        n0 = n_ad.copy(); n0[i] = 1e-6
        n_back, th_back = M.simulate(nic, b, c, n0, th_probe, EPS, T=800, dt=DT)
        rem.append(dict(i=i, lam_frozen=lam_f, bound=bound, secondary=sec, lam_adapted=lam_ad,
                        trait_shift=float(np.max(np.abs(th_ad[keep] - th[keep]))),
                        condC=cC["holds"],
                        recovered_fraction=float(n_back[i] / n[i]),
                        L_return_gap=float(M.potential(nic, b, c, n_back, th_back) - Lstar)))
    rec["removals"] = rem
    return rec


def part2():
    jobs = PART2_JOBS
    # append-only, resumable: one JSON line per finished run
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "part2_runs.jsonl")
    done = {}
    if os.path.exists(path):
        with open(path) as fh:
            for line in fh:
                if line.strip():
                    rec = json.loads(line)
                    done[(rec["k"], rec["w"], rec["seed"])] = rec
    todo = [j for j in jobs if j not in done]
    with Pool(4) as p, open(path, "a") as fh:
        for rec in p.imap_unordered(part2_one, todo):
            fh.write(json.dumps(rec) + "\n")
            fh.flush()
            done[(rec["k"], rec["w"], rec["seed"])] = rec
            print("part2 done", rec["k"], rec["w"], rec["seed"], flush=True)
    recs = [done[j] for j in jobs]
    rems = [r_ for rec in recs for r_ in rec["removals"]]
    summary = dict(
        n_runs=len(recs),
        survivors_by_k_w={f"k={rec['k']},w={rec['w']},s={rec['seed']}": rec["n_survivors"] for rec in recs},
        all_converged=bool(all(rec["grad_norm_free"] < 1e-6 for rec in recs)),
        all_theorem_A_holds=bool(all(rec["theorem_A"]["holds"] for rec in recs)),
        all_jacobian_stable=bool(all(rec["theorem_A"]["jac_max_re"] < 0 for rec in recs)),
        max_jac_pred_gap=float(max(abs(rec["theorem_A"]["jac_max_re"] - rec["theorem_A"]["pred_max_re"]) for rec in recs)),
        min_trait_gap=float(min(rec["min_trait_gap"] for rec in recs if rec["min_trait_gap"] is not None)),
        n_removals=len(rems),
        all_frozen_positive=bool(all(x["lam_frozen"] > 0 for x in rems)),
        all_frozen_above_bound=bool(all(x["lam_frozen"] >= x["bound"] - 1e-9 for x in rems)),
        n_adapted_positive=int(sum(x["lam_adapted"] > 0 for x in rems)),
        min_lam_adapted=float(min(x["lam_adapted"] for x in rems)),
        median_adapted_over_frozen=float(np.median([x["lam_adapted"] / x["lam_frozen"] for x in rems])),
        n_condC=int(sum(x["condC"] for x in rems)),
        n_recovered_half=int(sum(x["recovered_fraction"] > 0.5 for x in rems)),
        max_abs_L_return_gap=float(max(abs(x["L_return_gap"]) for x in rems)),
    )
    dump("part2_summary.json", summary)
    return summary


# ------------------------------------------------------------------ part 3

SHAPES = {"weak generalist (gamma=0)": (0.0, -0.5, 0.0),
          "middling (gamma=1.5)": (0.0, -0.5, 1.5),
          "strong generalist (gamma=3)": (0.0, -0.5, 3.0),
          "strong generalist, alpha=0.2": (0.2, -1.0, 4.0)}


def part3_one(args):
    name, cB = args
    al, be, ga = SHAPES[name]
    nic = M.TradeoffNiche(al, be, ga)
    B = 1.0
    b, c = np.array([B, B]), np.array([cB, cB])
    n0, th0 = np.full(2, B - cB), np.array([1.0, 0.0])
    chkA = M.theorem_A_check(nic, b, c, n0, th0, 0.2)
    takeover_pred = bool(nic.da(0.0) * B > nic.da(1.0) * cB)
    n_ad, th_ad = M.simulate(nic, b, c, n0, th0, 0.2, T=300, dt=DT, alive=np.array([True, False]))
    probe = np.array([th_ad[0], 0.0])
    lam_ad = float(M.growth(nic, b, c, n_ad, probe)[1])
    g = nic.a(0.5)
    n_back, th_back = M.simulate(nic, b, c, np.array([n_ad[0], 1e-6]), probe, 0.2, T=400, dt=DT)
    return dict(shape=name, a_half=float(g), da0=float(nic.da(0.0)), da1=float(nic.da(1.0)), c_over_B=cB,
                theorem_A=chkA, lam_frozen=B - cB, takeover_predicted=takeover_pred,
                lone_trait=float(th_ad[0]), lam_adapted=lam_ad,
                lam_generalist_formula=float(cB * (1 / (2 * g) - 1)),
                reinvader_grew=bool(n_back[1] > 1e-5), reinvaded=bool(n_back[1] > 0.5 * (B - cB)), final_traits=[float(x) for x in th_back],
                final_n=[float(x) for x in n_back])


def part3():
    jobs = [(nm, cB) for nm in SHAPES for cB in np.round(np.arange(0.1, 1.0, 0.1), 2)]
    with Pool(4) as p:
        rows = p.map(part3_one, jobs)
    dump("part3_runs.json", rows)
    return rows


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    t0 = time.time()
    if which in ("part1", "all"):
        print(json.dumps(part1(), indent=1), flush=True)
    if which in ("part3", "all"):
        for r_ in part3():
            print(r_["shape"], r_["c_over_B"], "A:", r_["theorem_A"]["holds"], "takeover:", r_["takeover_predicted"],
                  "lone th=%.3f lam_ad=%+.4f formula=%+.4f grew=%s reinv=%s" % (r_["lone_trait"], r_["lam_adapted"],
                                                                     r_["lam_generalist_formula"], r_["reinvader_grew"], r_["reinvaded"]), flush=True)
    if which in ("part2", "all"):
        print(json.dumps(part2(), indent=1), flush=True)
    print("elapsed", time.time() - t0)
