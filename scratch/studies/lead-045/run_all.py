"""Run every LEAD-045 study and write results/. About five minutes on four
CPU cores: `python3 -I run_all.py` from this directory, or
`python3 -I run_all.py geometry` / `network` for one part."""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import json
import sys
import time
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from geometry import (task_vectors, simulate, first_crossing, ode_clock,
                      domino_limit_ratio, gd_times, hadamard4,
                      rotated_quadratic, hadamard_phase1_end)
from network import make_data, train, peak_rate_times

OUT = os.path.join(HERE, "results")
EPS = 0.1  # a skill counts as learned at s >= 1 - EPS


def geometry_part():
    res = {}
    d, eta = 1000, 1e-4
    c = eta * np.sqrt(2 * d / np.pi)
    T2 = task_vectors(2, d, seed=0)
    rows = []
    for p1 in [0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]:
        p = [p1, 1 - p1]
        ts, s = simulate(p, T2, "sign", eta, 3000)
        tt = first_crossing(ts, s, 1 - EPS)
        l2 = ode_clock(p, EPS) / c
        l1 = ode_clock(p, EPS, "l1") / c
        ts_a, s_a = simulate(p, T2, "adam", eta, 8000)
        ta = first_crossing(ts_a, s_a, 1 - EPS)
        ts_g, s_g = simulate(p, T2, "gd", 0.05, int(1.3 * gd_times(p, EPS, 0.05).max()))
        tg = first_crossing(ts_g, s_g, 1 - EPS)
        # peak-rate step of skill 2 under sign descent, simulated and derived
        ds = np.diff(s[:, 1])
        sim_peak2 = float(ts[int(np.argmax(ds[:int(tt[1])]))])
        rows.append(dict(
            p1=p1, sign_sim_steps=tt.tolist(), sign_sim_ratio=tt[1] / tt[0],
            ode_l2_steps=l2.tolist(), ode_l2_ratio=l2[1] / l2[0],
            ode_l1_ratio=l1[1] / l1[0],
            adam_default_sim_ratio=ta[1] / ta[0],
            gd_sim_ratio=tg[1] / tg[0], gd_theory_ratio=p1 / (1 - p1),
            s2_when_s1_learned_sign=float(np.interp(tt[0], ts, s[:, 1])),
            s2_when_s1_learned_gd=float(np.interp(tg[0], ts_g, s_g[:, 1])),
            s2_when_s1_learned_theory=1 - EPS ** ((1 - p1) / p1),
            sign_sim_peak_step_skill2=sim_peak2,
            skill2_level_at_half_own_time_sign=float(np.interp(tt[1] / 2, ts, s[:, 1]) / (1 - EPS)),
            skill2_level_at_half_own_time_gd=float(np.interp(tg[1] / 2, ts_g, s_g[:, 1]) / (1 - EPS))))
    res["two_tasks"] = dict(d=d, eta_sign=eta, c_per_step=c, eps=EPS,
                            domino_limit_ratio=domino_limit_ratio(2, EPS),
                            rows=rows)
    many = []
    for alpha in [1.0, 2.0, 3.0]:
        n = 5
        p = np.arange(1, n + 1, dtype=float) ** (-alpha)
        p /= p.sum()
        T = task_vectors(n, d, seed=1)
        ts, s = simulate(p, T, "sign", eta, 6000)
        tt = first_crossing(ts, s, 1 - EPS)
        l2 = ode_clock(p, EPS) / c
        many.append(dict(alpha=alpha, p=p.tolist(),
                         sign_sim_ratios=(tt / tt[0]).tolist(),
                         ode_l2_ratios=(l2 / l2[0]).tolist(),
                         domino_limit_ratios=[domino_limit_ratio(k, EPS) for k in range(1, n + 1)],
                         gd_ratios=(p[0] / p).tolist()))
    res["many_tasks"] = many
    lam = [1.0, 0.1, 0.01, 0.001]
    quad = {}
    for R, name in [(np.eye(4), "identity"), (hadamard4(), "hadamard")]:
        for opt in ["sign", "gd"]:
            xs = rotated_quadratic(R, lam, opt, 1e-3, 20000)
            half = []
            for j in range(4):
                idx = np.nonzero(xs[:, j] <= 0.5)[0]
                half.append(int(idx[0]) if len(idx) else None)
            quad[f"{name}_{opt}_half_steps"] = half
    xs = rotated_quadratic(hadamard4(), lam, "sign", 1e-3, 600)
    x1_end = hadamard_phase1_end(lam)
    k_end = int((1 - x1_end) / 2e-3)
    quad["hadamard_phase1_x1_end"] = x1_end
    quad["hadamard_phase1_last_step"] = k_end
    quad["hadamard_max_move_x2_x4_before_it"] = float(np.abs(xs[:k_end, 1:] - 1).max())
    res["rotated_quadratic"] = quad
    return res


RECORD_EVERY = 3
NET = dict(K=4, D=8, n_train=4096, n_test_per_skill=500, alpha=2.0, width=64)
OPT = {"gd": (0.2, 6000), "sign": (1e-3, 3000), "adam": (1e-3, 3000)}


def one_network_run(args):
    opt, scale, seed, lr, steps = args
    data = make_data(NET["K"], NET["D"], NET["n_train"], NET["n_test_per_skill"],
                     NET["alpha"], seed=seed)
    t0 = time.time()
    ts, tr, te, _ = train(data, NET["width"], scale, opt, lr, steps,
                          record_every=RECORD_EVERY, seed=seed)
    t_half = first_crossing(ts, tr, 0.5)
    t_learn = first_crossing(ts, tr, 1 - EPS)
    peaks = peak_rate_times(ts, tr, smooth=3)
    # level reached at half of each skill's own learning time, over 1 - EPS:
    # above 0.5 the curve rose fastest early (concave, no delay), below 0.5
    # it was held back and rose late (delayed onset)
    half_level = [float(np.interp(t_learn[j] / 2, ts, tr[:, j]) / (1 - EPS))
                  for j in range(NET["K"])]
    at_t1 = [float(np.interp(t_learn[0], ts, tr[:, j])) for j in range(NET["K"])]
    return dict(optimizer=opt, init_scale=scale, seed=seed, lr=lr, steps=steps,
                p=data["p"].tolist(), counts=data["counts"].tolist(),
                t_half=t_half.tolist(), t_learned=t_learn.tolist(),
                ratio_learned=(t_learn / t_learn[0]).tolist(),
                peak_rate_step=peaks.tolist(),
                peak_over_t1=(peaks / t_learn[0]).tolist(),
                peak_over_own_t_learned=(peaks / t_learn).tolist(),
                level_at_half_own_time=half_level,
                curve_steps=ts.tolist(), curve_train=tr.astype(np.float32),
                level_when_skill1_learned=at_t1,
                final_train=tr[-1].tolist(), final_test=te[-1].tolist(),
                seconds=time.time() - t0)


def ode_prediction_for_network():
    p = np.arange(1, NET["K"] + 1, dtype=float) ** (-NET["alpha"])
    p /= p.sum()
    t = ode_clock(p, EPS)
    return dict(p=p.tolist(), sign_ode_ratios=(t / t[0]).tolist(),
                gd_decoupled_ratios=(p[0] / p).tolist())


def network_part():
    jobs = [(opt, scale, seed, *OPT[opt])
            for opt in ["gd", "sign", "adam"] for scale in [1.0, 0.01]
            for seed in [0, 1, 2]]
    jobs.append(("sign", 1.0, 0, 3e-4, 9000))  # learning-rate check
    with Pool(4) as pool:
        runs = pool.map(one_network_run, jobs)
    curves = {}
    for i, r in enumerate(runs):
        curves[f"run{i}_level"] = r.pop("curve_train")
        curves[f"run{i}_steps"] = np.array(r.pop("curve_steps"))
        r["curve_key"] = f"run{i}"
    np.savez_compressed(os.path.join(OUT, "network_curves.npz"), **curves)
    return dict(config=NET, record_every=RECORD_EVERY, eps=EPS,
                geometry_model_prediction=ode_prediction_for_network(), runs=runs)


def fmt(xs, nd=1):
    return " ".join("nan" if (x is None or (isinstance(x, float) and np.isnan(x)))
                    else f"{x:.{nd}f}" for x in xs)


def write_tsv(net):
    lines = ["optimizer\tinit_scale\tseed\tlr\tt_half\tt_learned\tratio_learned\t"
             "peak_rate_step\tpeak_over_own_t_learned\tlevel_at_half_own_time\t"
             "level_when_skill1_learned\tfinal_test"]
    for r in net["runs"]:
        lines.append("\t".join([r["optimizer"], str(r["init_scale"]), str(r["seed"]),
                                str(r["lr"]), fmt(r["t_half"]), fmt(r["t_learned"]),
                                fmt(r["ratio_learned"], 2), fmt(r["peak_rate_step"]),
                                fmt(r["peak_over_own_t_learned"], 2),
                                fmt(r["level_at_half_own_time"], 2),
                                fmt(r["level_when_skill1_learned"], 2),
                                fmt(r["final_test"], 3)]))
    with open(os.path.join(OUT, "network.tsv"), "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    parts = sys.argv[1:] or ["geometry", "network"]
    if "geometry" in parts:
        g = geometry_part()
        with open(os.path.join(OUT, "geometry.json"), "w") as f:
            json.dump(g, f, indent=1)
        print(json.dumps(g["two_tasks"]["rows"], indent=0)[:3000])
    if "network" in parts:
        n = network_part()
        with open(os.path.join(OUT, "network.json"), "w") as f:
            json.dump(n, f, indent=1)
        write_tsv(n)
        print(open(os.path.join(OUT, "network.tsv")).read())
