"""LEAD-172 analysis: the prospective test.

The early checkpoint t_e is a fixed step, 250 or 500, the same for every arm
and before every arm's generalization; training accuracy is already 1 by
step 100-150 in these runs, so the memorization step does not separate arms.
Each measure's value at t_e is a single-feature linear forecast of
log10 T_gen (first step with test acc >= 0.95), fitted by least squares on
the fit arms (weight decay 1.0) and scored on the held-out-intervention arms
(weight decay 0.5 and 2.0, never seen in fitting). Every forecast has the
same two parameters, so complexity is matched.

The null at equal edge budget: the same coupling fraction computed on 20
random sets of p - 1 off-rule cells (hidden layer) or triads (logits).
Writes analysis_te250.json and analysis_te500.json.
"""
import glob
import gzip
import json
import os

import numpy as np

STUDY = os.path.dirname(os.path.abspath(__file__))


def load(path):
    meta, rows, done = None, {}, None
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if not line.strip():
                continue
            r = json.loads(line)
            if r.get("meta"):
                meta = r
            elif r.get("done"):
                done = r
            else:
                rows[r["step"]] = r          # keep the last row per step
    return meta, [rows[k] for k in sorted(rows)], done


def first(rows, key, thr):
    for r in rows:
        if r[key] >= thr:
            return r["step"]
    return None


def at(rows, step, need=None):
    cand = [r for r in rows if r["step"] <= step and (need is None or r.get(need) is not None)]
    return cand[-1] if cand else None


def features(rows, t_e):
    r = at(rows, t_e)
    rk = at(rows, t_e, need="KA")
    rot = [x["K_rot"] for x in rows if x.get("K_rot") is not None and x["step"] <= t_e]
    f = {
        "train_loss": np.log10(r["train_loss"]),
        "test_acc": r["test_acc"],
        "test_loss": r["test_loss"],
        "fourier_energy": r["fourier_energy"],
        "C1sel": np.log10(r["C1sel"]),
        "C2": np.log10(r["C2"]),
        "KA": rk["KA"],
        "K_rot": rot[-1] if rot else np.nan,
    }
    for j, v in enumerate(r["C1null"]):
        f["C1null_%d" % j] = np.log10(v + 1e-12)
    for j, v in enumerate(r["C2null"]):
        f["C2null_%d" % j] = np.log10(v + 1e-12)
    return f


def fit_predict(x_fit, y_fit, x_ho):
    A = np.c_[np.ones_like(x_fit), x_fit]
    coef, *_ = np.linalg.lstsq(A, y_fit, rcond=None)
    return coef[0] + coef[1] * x_ho, coef


def loo_rmse(x, y):
    err = []
    for i in range(len(x)):
        m = np.arange(len(x)) != i
        pred, _ = fit_predict(x[m], y[m], x[i:i + 1])
        err.append(pred[0] - y[i])
    return float(np.sqrt(np.mean(np.square(err))))


def spearman(x, y):
    rx = np.argsort(np.argsort(x))
    ry = np.argsort(np.argsort(y))
    return float(np.corrcoef(rx, ry)[0, 1])


def main(t_e):
    arms = []
    for path in sorted(glob.glob(os.path.join(STUDY, "results", "*.jsonl.gz"))):
        meta, rows, done = load(path)
        if done is None or done["t_gen"] is None:
            arms.append({"name": meta["name"], "complete": done is not None, "t_gen": None})
            continue
        t_mem = first(rows, "train_acc", 0.99)
        f = features(rows, t_e)
        t_c2 = first(rows, "C2", 0.5)
        t_ka = first([r for r in rows if r.get("KA") is not None], "KA", 0.5)
        arms.append({"name": meta["name"], "frac": meta["frac"], "wd": meta["wd"],
                     "seed": meta["seed"], "complete": True, "t_gen": done["t_gen"],
                     "t_mem": t_mem, "t_C2_half": t_c2, "t_KA_half": t_ka,
                     "C2_final": rows[-1]["C2"], "KA_final": [r for r in rows if r.get("KA") is not None][-1]["KA"],
                     "features": f})
    ok = [a for a in arms if a["t_gen"] is not None]
    fit = [a for a in ok if a["wd"] == 1.0]
    ho = [a for a in ok if a["wd"] != 1.0]
    y_fit = np.log10([a["t_gen"] for a in fit])
    y_ho = np.log10([a["t_gen"] for a in ho])
    names = list(fit[0]["features"]) if fit else []
    scores = {}
    const = float(np.sqrt(np.mean((y_ho - y_fit.mean()) ** 2))) if len(ho) else None
    for k in names:
        x_fit = np.array([a["features"][k] for a in fit])
        x_ho = np.array([a["features"][k] for a in ho])
        if not np.all(np.isfinite(np.r_[x_fit, x_ho])):
            continue
        pred, coef = fit_predict(x_fit, y_fit, x_ho)
        x_all = np.r_[x_fit, x_ho]
        scores[k] = {"heldout_rmse": float(np.sqrt(np.mean((pred - y_ho) ** 2))),
                     "fit_loo_rmse": loo_rmse(x_fit, y_fit),
                     "slope": float(coef[1]),
                     "spearman_all": spearman(x_all, np.r_[y_fit, y_ho])}
    real = [k for k in scores if "null" not in k]

    def null_summary(prefix):
        v = [scores[k]["heldout_rmse"] for k in scores if k.startswith(prefix)]
        lo = [scores[k]["fit_loo_rmse"] for k in scores if k.startswith(prefix)]
        return {"heldout_rmse_median": float(np.median(v)), "heldout_rmse_min": float(np.min(v)),
                "fit_loo_rmse_median": float(np.median(lo)), "n": len(v)}

    out = {
        "n_arms": len(arms), "n_grokked": len(ok), "n_fit": len(fit), "n_heldout": len(ho),
        "constant_heldout_rmse": const,
        "scores": {k: scores[k] for k in real},
        "null_C1": null_summary("C1null"), "null_C2": null_summary("C2null"),
        "rank_C2_among_nulls": int(sum(scores[k]["heldout_rmse"] < scores["C2"]["heldout_rmse"]
                                       for k in scores if k.startswith("C2null"))),
        "rank_C1sel_among_nulls": int(sum(scores[k]["heldout_rmse"] < scores["C1sel"]["heldout_rmse"]
                                          for k in scores if k.startswith("C1null"))),
        "arms": [{k: v for k, v in a.items() if k != "features"}
                 | ({"at_t_mem": {k: a["features"][k] for k in real}} if "features" in a else {})
                 for a in arms],
    }
    out["t_e"] = t_e
    with open(os.path.join(STUDY, "analysis_te%d.json" % t_e), "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    print("== early checkpoint t_e =", t_e, "; min T_gen", min(a["t_gen"] for a in ok))
    print("arms", len(arms), "grokked", len(ok), "fit", len(fit), "heldout", len(ho))
    print("constant heldout rmse", const)
    for k in sorted(real, key=lambda k: scores[k]["heldout_rmse"]):
        s = scores[k]
        print("%-15s heldout %.3f  loo %.3f  rho %.2f" % (k, s["heldout_rmse"], s["fit_loo_rmse"], s["spearman_all"]))
    print("null C1", out["null_C1"], "C1sel beaten by", out["rank_C1sel_among_nulls"])
    print("null C2", out["null_C2"], "C2 beaten by", out["rank_C2_among_nulls"])
    for a in ok:
        print(a["name"], "T_mem", a["t_mem"], "T_C2half", a["t_C2_half"], "T_KAhalf", a["t_KA_half"], "T_gen", a["t_gen"])


if __name__ == "__main__":
    for t_e in (250, 500):
        main(t_e)
