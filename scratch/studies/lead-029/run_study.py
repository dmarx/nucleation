"""Run LEAD-029's comparison.  Usage:
    python3 -I run_study.py [n_seeds] [out.json]
"""
import json
import os
import sys
import time
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
import jointpred as jp  # noqa: E402

RHO, KAPPA, DELTA, SIGMA = 0.3, 0.1, 1.5, 0.03
GENERATORS = {  # name: (eta, score)
    "amplifying": (3.0, "sq"),
    "damped": (0.5, "sq"),
    "null": (0.0, "sq"),
    "amplifying-abs": (1.0, "abs"),
}
DESIGNS = ("D1", "D2")
T_SWITCH, T_INT = 12, 4


def models():
    return [jp.Cut(), jp.Joint("sq"), jp.CutFlex(), jp.Additive()]  # cut first: the joint starts from its fit


def run_one(args):
    gen, design, seed = args
    eta, score = GENERATORS[gen]
    rng = np.random.default_rng(1000 * seed + 7)
    a = jp.true_operators(rng)
    ctx, E = jp.training_data(rng, design)
    x = jp.simulate_operator(a, RHO, eta, KAPPA, DELTA, ctx, E, score)
    y = x + rng.normal(0, SIGMA, x.shape)
    tctx, tE, labels = jp.test_episodes(t_int=T_INT, t_switch=T_SWITCH)
    tx = jp.simulate_operator(a, RHO, eta, KAPPA, DELTA, tctx, tE, score)
    true_eff = tx[0::2] - tx[1::2]
    held = np.array([(j, c) in jp.HELDOUT for j, s, c, c2 in labels])
    agree = np.array([c == 0 for j, s, c, c2 in labels])
    out = {"gen": gen, "design": design, "seed": seed,
           "true_effect_rms_post": float(np.sqrt((true_eff[:, T_SWITCH:] ** 2).mean())),
           "true_abs_effect_end_by_ctx": [float(np.abs(true_eff[[c == q for _, _, c, _ in labels], -1]).mean()) for q in range(jp.C)],
           "models": {}}
    sp = lambda v: jp.inv_softplus(max(v, 1e-3))
    truth_start = {
        "joint": np.concatenate([jp.logit(a.ravel()), [jp.logit(RHO), sp(eta), jp.logit(KAPPA), sp(DELTA)]]),
        "cut": np.concatenate([jp.logit(a.ravel()), [jp.logit(RHO), jp.logit(KAPPA), sp(DELTA)]]),
        "cutflex": np.concatenate([jp.logit(a.ravel()), [jp.logit(RHO)], [jp.logit(KAPPA)] * jp.K, [sp(DELTA)] * jp.K]),
    }
    fitted = {}
    for m in models():
        t0 = time.time()
        extra = []
        if m.name == "joint":  # staged starts: the cut model's fit, with the loop switched on
            thc = fitted["cut"]["blind"][0]
            extra = [np.concatenate([thc[:13], [sp(e)], thc[13:]]) for e in (0.3, 1.0, 3.0)]
        th_b, sse_b, _ = jp.fit(m, ctx, E, y, rng, extra_starts=extra)
        th_i, sse_i = th_b, sse_b
        if m.name in truth_start:  # informed protocol: one more start, at the generating values
            th_t, sse_t, _ = jp.fit(m, ctx, E, y, rng, restarts=0, extra_starts=[truth_start[m.name]])
            if sse_t < sse_b:
                th_i, sse_i = th_t, sse_t
        fitted[m.name] = {"blind": (th_b, sse_b), "informed": (th_i, sse_i)}
        r = {"k": m.n_params, "seconds": time.time() - t0}
        for proto, (th, sse) in fitted[m.name].items():
            pred = m.predict(th, tctx, tE)
            eff = pred[0::2] - pred[1::2]
            aic, bic = jp.aic_bic(sse, y.size, m.n_params)
            rr = {
                "train_mse": sse / y.size, "aic": aic, "bic": bic,
                "traj_rmse_post": float(np.sqrt(((pred - tx)[:, T_SWITCH:] ** 2).mean())),
                "effect_rmse_pre": float(np.sqrt(((eff - true_eff)[:, T_INT:T_SWITCH] ** 2).mean())),
                "effect_rmse_post": float(np.sqrt(((eff - true_eff)[:, T_SWITCH:] ** 2).mean())),
                "effect_rmse_post_heldout": float(np.sqrt(((eff - true_eff)[held, T_SWITCH:] ** 2).mean())),
                "effect_rmse_post_agree": float(np.sqrt(((eff - true_eff)[agree, T_SWITCH:] ** 2).mean())),
                "effect_rmse_post_dissent": float(np.sqrt(((eff - true_eff)[~agree, T_SWITCH:] ** 2).mean())),
                "abs_effect_end_by_ctx": [float(np.abs(eff[[c == q for _, _, c, _ in labels], -1]).mean()) for q in range(jp.C)],
            }
            if m.name == "joint":
                rr["eta_hat"] = float(m.unpack(th)[2])
                rr["kappa_hat"] = float(m.unpack(th)[3])
            r[proto] = rr
        out["models"][m.name] = r
    print(gen, design, seed, {k: (round(v["blind"]["effect_rmse_post"], 4), round(v["informed"]["effect_rmse_post"], 4)) for k, v in out["models"].items()}, flush=True)
    return out


def summarize(runs):
    summ = {}
    for gen in GENERATORS:
        for d in DESIGNS:
            rs = [r for r in runs if r["gen"] == gen and r["design"] == d]
            if not rs:
                continue
            s = {"n_seeds": len(rs),
                 "true_effect_rms_post": float(np.mean([r["true_effect_rms_post"] for r in rs])),
                 "true_abs_effect_end_by_ctx": np.mean([r["true_abs_effect_end_by_ctx"] for r in rs], axis=0).round(4).tolist()}
            for name in rs[0]["models"]:
                for proto in ("blind", "informed"):
                    ms = [r["models"][name][proto] for r in rs]
                    js = [r["models"]["joint"][proto] for r in rs]
                    e = {key: float(np.mean([m[key] for m in ms])) for key in ms[0] if key != "abs_effect_end_by_ctx"}
                    e["abs_effect_end_by_ctx"] = np.mean([m["abs_effect_end_by_ctx"] for m in ms], axis=0).round(4).tolist()
                    e["beats_joint_effect_post"] = int(sum(m["effect_rmse_post"] < j["effect_rmse_post"] for m, j in zip(ms, js)))
                    e["lower_bic_than_joint"] = int(sum(m["bic"] < j["bic"] for m, j in zip(ms, js)))
                    s[f"{name}/{proto}"] = e
            summ[f"{gen}/{d}"] = s
    return summ


if __name__ == "__main__":
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    n_seeds = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json")
    # Resumable: each finished run is appended to runs.jsonl at once, and
    # runs already there are skipped (each run's random stream depends only
    # on its seed, so a resumed study gives the same results).
    jsonl = os.path.join(os.path.dirname(os.path.abspath(out)), "runs.jsonl")
    done = []
    if os.path.exists(jsonl):
        with open(jsonl) as f:
            done = [json.loads(line) for line in f if line.strip()]
    have = {(r["gen"], r["design"], r["seed"]) for r in done}
    jobs = [(g, d, s) for g in GENERATORS for d in DESIGNS for s in range(n_seeds)
            if (g, d, s) not in have]
    with Pool(4) as p, open(jsonl, "a") as f:
        for r in p.imap_unordered(run_one, jobs, chunksize=1):
            f.write(json.dumps(r) + "\n"); f.flush()
            done.append(r)
    order = {(g, d, s): i for i, (g, d, s) in enumerate(
        (g, d, s) for g in GENERATORS for d in DESIGNS for s in range(n_seeds))}
    runs = sorted((r for r in done if (r["gen"], r["design"], r["seed"]) in order),
                  key=lambda r: order[(r["gen"], r["design"], r["seed"])])
    res = {"settings": {"rho": RHO, "kappa": KAPPA, "delta": DELTA, "sigma": SIGMA,
                        "generators": GENERATORS, "designs": DESIGNS, "K": jp.K, "C": jp.C,
                        "T": 24, "t_intervention": T_INT, "t_switch": T_SWITCH,
                        "n_train_episodes": 240, "heldout": sorted(jp.HELDOUT)},
           "summary": summarize(runs), "runs": runs}
    with open(out, "w") as f:
        json.dump(res, f, indent=1)
