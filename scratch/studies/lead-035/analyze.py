"""Summarize results.jsonl into summary.json and a table on stdout.

For each item, over its late window (the last decade of t before the run
ended, t > 0): the log-log slope of each omega_j against t (Han et al.
predict 1/4), the ratio max/min omega at the end (they predict -> 1), the
ratio of the geometric-mean omega to (4t/N)^(1/4) at the end (-> 1, in
their time unit), and, for the trained models, the deviation share
L_perp/L_LS at the end (the central path has it near 0).

    python3 -I analyze.py [directory holding results*.jsonl]
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import snr  # noqa: E402


def late(traj, decades=1.0):
    t = np.array([r["t"] for r in traj])
    keep = t >= t[-1] / 10 ** decades
    keep &= t > 0
    return [r for r, k in zip(traj, keep) if k]


def measurable(traj):
    """Rows where omega is within double precision. Runs stop at the first
    mark past it, and that row (sometimes omega ~ 1e150) is dropped."""
    return [r for r in traj if r["L_LS"] >= 1e-10 and r["sw_cond"] >= 1e-12]


def summarize(row):
    traj = measurable(row["traj"])
    N = row["N"]
    w = late(traj)
    t = np.array([r["t"] for r in w])
    om = np.array([r["omega"] for r in w])
    slopes = [snr.loglog_slope(t, om[:, j]) for j in range(om.shape[1])]
    # exponential rate: slope of log omega on t, per unit t
    exp_rate = [float(np.polyfit(t, np.log(om[:, j]), 1)[0])
                for j in range(om.shape[1])]
    # which of the two describes the window better (residual of each fit)
    def resid(x, y):
        A = np.vstack([x, np.ones_like(x)]).T
        r = np.linalg.lstsq(A, y, rcond=None)[1]
        return float(r[0]) if len(r) else 0.0
    lg = np.log(om.mean(axis=1))
    pw_res, ex_res = resid(np.log(t), lg), resid(t, lg)
    end = traj[-1]
    gm = float(np.exp(np.mean(np.log(end["omega"]))))
    out = {
        "id": row["id"], "model": row["model"], "seed": row["seed"],
        "steps": end["step"], "t_end": end["t"],
        "stopped_early": row["traj"][-1]["step"] < row["cfg"]["steps"],
        "window_t": [float(t[0]), float(t[-1])],
        "loglog_slopes": slopes,
        "exp_rates": exp_rate,
        "power_vs_exp_residual": [pw_res, ex_res],
        "omega_end": end["omega"],
        "ratio_max_min_end": end["omega"][0] / end["omega"][-1],
        "ratio_max_min_start": traj[0]["omega"][0] / traj[0]["omega"][-1],
        "gm_over_han_end": gm / float(snr.han_asymptote(end["t"], N)),
        "L_LS_end": end["L_LS"], "nc1_end": end["nc1"],
    }
    if "L" in end:
        out["L_end"] = end["L"]
        out["perp_share_end"] = (end["L"] - end["L_LS"]) / end["L_LS"]
        # max over the late window, as in Han et al.'s Figure 2 reading
        out["perp_share_max_late"] = max((r["L"] - r["L_LS"]) / r["L_LS"]
                                         for r in w)
    if "acc" in end:
        out["acc_end"] = end["acc"]
    if row["model"].startswith("ufm-renorm"):
        om0 = np.array(traj[0]["omega"])
        exact = [float(snr.han_exact(end["t"], x, N, row["C"])[0]) for x in om0]
        out["omega_exact_end"] = exact
        out["max_rel_err_vs_exact"] = float(np.max(
            np.abs(np.array(end["omega"]) - exact) / np.array(exact)))
    return out


def main():
    import glob
    d = sys.argv[1] if len(sys.argv) > 1 else HERE
    rows = []
    for p in sorted(glob.glob(os.path.join(d, "results*.jsonl"))):
        rows += [json.loads(l) for l in open(p) if l.strip()]
    rows.sort(key=lambda r: r["id"])
    path = os.path.join(d, "x")
    summ = [summarize(r) for r in rows]
    with open(os.path.join(os.path.dirname(path), "summary.json"), "w") as f:
        json.dump(summ, f, indent=1)
    hdr = ("id", "t_end", "slopes", "max/min", "gm/han", "perp", "acc", "early")
    print("%-24s %9s %-22s %8s %9s %9s %5s %s" % hdr)
    for s in summ:
        print("%-24s %9.3g %-22s %8.3g %9.3g %9s %5s %s" % (
            s["id"], s["t_end"],
            " ".join("%.3f" % x for x in s["loglog_slopes"]),
            s["ratio_max_min_end"], s["gm_over_han_end"],
            "%.2g" % s["perp_share_end"] if "perp_share_end" in s else "-",
            "%.2f" % s["acc_end"] if "acc_end" in s else "-",
            "yes" if s["stopped_early"] else ""))


if __name__ == "__main__":
    main()
