# scratch/manuscripts/governance-of-possibility/analysis/study.py
"""Runs the sweep and writes results.json and results.md.

Run from this directory:  python3 -I study.py [out_dir]
Seeds are fixed (numpy default_rng([20261123, seed, stream])).
"""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as m  # noqa: E402

T = 4000                      # periods per long run
SEEDS = range(8)
PS = (0.005, 0.01, 0.02, 0.05)
THETAS = (1.0, 1.5, 2.0, 2.5)
TAUS = (2, 3, 4, 6, 8, 12, 20)
LS = (5.0, 20.0, 50.0, 100.0, 200.0, 500.0)
CS = (0.05, 0.1, 0.2)
REF = dict(p=0.02, theta=2.0, L=50.0, c=0.1)
REPS = 2000                   # imposed contingencies per regime
G = 0.1                       # chance a period that outside money arrives
ORDER = ("I", "II", "III-a", "III-b", "IV", "V", "II-rev", "III-b-rev",
         "IV-drill2")


def all_regimes(theta: float) -> dict[str, m.Regime]:
    r = m.regimes(theta)
    rv = m.regimes(theta, revoke=0.005)
    r["II-rev"] = m.replace(rv["II"], name="II, reserve lapses at 0.005/period")
    r["III-b-rev"] = m.replace(rv["III-b"], name="III-b, reserve lapses at 0.005/period")
    r["IV-drill2"] = m.replace(r["IV"], name="IV, drill every 2nd period (control)",
                               drill_every=2)
    return r


def long_runs() -> dict:
    out: dict = {}
    for theta in THETAS:
        regs = all_regimes(theta)
        for p in PS:
            for k, reg in regs.items():
                if not reg.redesigned and theta != REF["theta"]:
                    continue          # does not depend on theta'
                caps, resp, n_c, outs, first_out = [], [], 0, [], []
                for sd in SEEDS:
                    x = m.run(reg, p, T, sd, G)
                    caps.append(x["cap"].mean())
                    resp.append(x["resp"])
                    n_c += len(x["resp"])
                    outs.append(x["output"].mean())
                    f = int(x["first"][0]) if x["first"][0] >= 0 else T
                    first_out.append(float(x["output"][:f].mean()) if f else 1.0)
                rt = np.concatenate(resp)
                late = {str(t): float((rt > t).sum()) / (T * len(SEEDS))
                        for t in TAUS}
                out[f"{k}|{p}|{theta}"] = dict(
                    regime=k, p=p, theta=theta, cap=float(np.mean(caps)),
                    contingencies=n_c, late_rate=late,
                    mean_resp=float(rt.mean()), output=float(np.mean(outs)),
                    output_before_first=float(np.mean(first_out)))
    return out


def lr(runs: dict, k: str, p: float, theta: float) -> dict:
    reg_theta = theta if f"{k}|{p}|{theta}" in runs else REF["theta"]
    return runs[f"{k}|{p}|{reg_theta}"]


def cost(row: dict, tau: int, L: float, c: float) -> float:
    return c * row["cap"] + L * row["late_rate"][str(tau)]


def imposed(theta: float) -> dict:
    ts = np.arange(0, 41)
    res = {}
    for k, reg in all_regimes(theta).items():
        times = m.impose(reg, REPS, g=G, seed=1)
        res[k] = m.readiness(times, ts).tolist()
    return dict(ts=ts.tolist(), R=res)


def dominance_table(imp: dict, keys: tuple[str, ...]) -> dict:
    R = {k: np.array(imp["R"][k]) for k in keys}
    tab = {}
    for i in keys:
        for j in keys:
            if i < j:
                d = m.dominance(R[i], R[j], tol=0.02)
                cross = [t for t in imp["ts"][1:]
                         if (R[i][t] - R[j][t]) * (R[i][t - 1] - R[j][t - 1]) < 0]
                tab[f"{i} vs {j}"] = dict(relation=d, sign_changes_at=cross)
    return tab


def rankings(runs: dict, imp: dict, p: float, L: float, c: float,
             keys: tuple[str, ...]) -> dict:
    out = {}
    for tau in TAUS:
        by_R = sorted(keys, key=lambda k: -imp["R"][k][tau])
        by_cost = sorted(keys, key=lambda k: cost(lr(runs, k, p, REF["theta"]),
                                                   tau, L, c))
        out[str(tau)] = dict(by_readiness=by_R, by_cost=by_cost,
                             cost={k: round(cost(lr(runs, k, p, REF["theta"]),
                                                 tau, L, c), 4) for k in keys})
    return out


def break_even(runs: dict, imp: dict, hi: str, lo: str, theta: float) -> list:
    """pL at which holding `hi`'s reserve costs the same as `lo`'s lateness."""
    rows = []
    for p in PS:
        a, b = lr(runs, hi, p, theta), lr(runs, lo, p, theta)
        for tau in TAUS:
            dlate = b["late_rate"][str(tau)] - a["late_rate"][str(tau)]
            dR = imp["R"][hi][tau] - imp["R"][lo][tau]
            for c in CS:
                dcap = a["cap"] - b["cap"]
                Lstar = c * dcap / dlate if dlate > 0 else float("inf")
                rows.append(dict(p=p, tau=tau, c=c, dcap=dcap,
                                 pL_star_sim=p * Lstar,
                                 pL_star_imposed=(c * dcap / dR if dR > 0
                                                  else float("inf"))))
    return rows


def reserve_sweep() -> list:
    rows = []
    floors = np.round(np.arange(1.0, 3.01, 0.25), 2)
    for arch, paths in (("original", (m.ORIGINAL,)),
                        ("redesigned", (m.ORIGINAL, m.staged(2.0)))):
        for F in floors:
            reg = m.Regime(f"floor {F}", paths, "floor", floor=float(F))
            times = m.impose(reg, 1000, g=G, seed=2)
            R = m.readiness(times, np.array(TAUS))
            rows.append(dict(arch=arch, floor=float(F), reserve=float(F - 1),
                             R={str(t): float(v) for t, v in zip(TAUS, R)}))
    return rows


def novel() -> list:
    rows = []
    regs = m.regimes(2.0)
    for g, rc in ((G, 0.0), (G, 0.5), (0.0, 0.5)):
        for k in ("I", "II", "III-a", "III-b", "IV", "V"):
            for pol in ("excise", "revise"):
                if g == 0.0 and pol == "excise":
                    continue
                r = m.novel_demand(regs[k], pol, 400, review_cost=rc, g=g,
                                   seed=4)
                rows.append(dict(regime=k, policy=pol, review_cost=rc, g=g, **r))
    return rows


def fmt(x: float) -> str:
    return "inf" if x == float("inf") else f"{x:.3g}"


def write_md(res: dict, path: str) -> None:
    L = ["# Results: regulation as the governance of possibility",
         "", f"Generated by study.py in {res['runtime_s']:.0f} s. "
         f"Long runs: {len(SEEDS)} seeds x {T} periods; imposed contingencies: "
         f"{REPS} per regime after 50 quiet periods; outside money arrives with "
         f"chance {G} a period. Reference: p = {REF['p']}, theta' = "
         f"{REF['theta']}, L = {REF['L']}, c = {REF['c']}.", "",
         "## Present output (before the first contingency, and overall)", "",
         "| Regime | output before first contingency | output overall | "
         "capacity above holding | mean response |", "|---|---|---|---|---|"]
    for k in ORDER:
        r = lr(res["runs"], k, REF["p"], REF["theta"])
        L.append(f"| {k} | {r['output_before_first']:.4f} | {r['output']:.4f} | "
                 f"{r['cap']:.3f} | {r['mean_resp']:.2f} |")
    imp = res["imposed"]
    L += ["", "## Readiness R(t) under an imposed contingency (theta' = 2)", "",
          "| Regime | " + " | ".join(f"t={t}" for t in TAUS) + " |",
          "|---|" + "---|" * len(TAUS)]
    for k in ORDER:
        L.append(f"| {k} | " + " | ".join(f"{imp['R'][k][t]:.3f}" for t in TAUS)
                 + " |")
    L += ["", "## First-order dominance of readiness curves (t = 0..40, tol 0.02)",
          "", "| Pair | relation | sign changes at t |", "|---|---|---|"]
    for pair, d in res["dominance"].items():
        L.append(f"| {pair} | {d['relation']} | {d['sign_changes_at']} |")
    L += ["", "## Ranking by deadline at the reference costs", "",
          "| tau | by readiness | by long-run cost (c*reserve + L*late rate) |",
          "|---|---|---|"]
    for tau, d in res["rankings"].items():
        L.append(f"| {tau} | {' > '.join(d['by_readiness'])} | "
                 f"{' < '.join(d['by_cost'])} |")
    L += ["", "## Break-even p*L for the reserve (II against I)", "",
          "pL* is where c x (extra capacity) equals L x (fewer late "
          "contingencies a period); a reserve pays when pL > pL*.", "",
          "| p | tau | c=0.05 | c=0.1 | c=0.2 | imposed-readiness formula c=0.1 |",
          "|---|---|---|---|---|---|"]
    be = res["break_even"]["II vs I"]
    for p in PS:
        for tau in (3, 6, 12):
            rs = {r["c"]: r for r in be if r["p"] == p and r["tau"] == tau}
            L.append(f"| {p} | {tau} | " + " | ".join(
                fmt(rs[c]["pL_star_sim"]) for c in CS)
                + f" | {fmt(rs[0.1]['pL_star_imposed'])} |")
    L += ["", "## Redesign: reserve needed, and III-b against II", "",
          "| theta' | kept under peak rule (III-a ready at t=40 without outside "
          "money) | III-b capacity | II capacity | R_IIIb(6) | R_II(6) |",
          "|---|---|---|---|---|---|"]
    for row in res["redesign"]:
        L.append(f"| {row['theta']} | {row['kept_peak']} | {row['cap_IIIb']:.3f} "
                 f"| {row['cap_II']:.3f} | {row['R_IIIb_6']:.3f} | "
                 f"{row['R_II_6']:.3f} |")
    L += ["", "## Reserve sweep (imposed readiness at t)", "",
          "| arch | reserve | " + " | ".join(f"t={t}" for t in TAUS) + " |",
          "|---|---|" + "---|" * len(TAUS)]
    for r in res["reserve_sweep"]:
        L.append(f"| {r['arch']} | {r['reserve']:.2f} | "
                 + " | ".join(f"{r['R'][str(t)]:.3f}" for t in TAUS) + " |")
    L += ["", "## Novel demand absent from the specification (CLAIM-361)", "",
          "Harm begins after 50 quiet periods; reaching C needs threshold 2.5. "
          "Horizon 120 periods, 400 reps.", "",
          "| regime | policy | review cost | outside money g | revised | reached C | harm periods"
          " | own-spec violations | D0 violations | review blocked | B_end |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in res["novel"]:
        L.append(f"| {r['regime']} | {r['policy']} | {r['review_cost']} | "
                 f"{r['g']} | {r['revised']:.2f} | {r['reached_C']:.2f} | "
                 f"{r['harm_periods']:.1f} | {r['own_spec_violations']:.1f} | "
                 f"{r['d0_violations']:.1f} | {r['review_blocked_periods']:.1f} | "
                 f"{r['B_end']:.2f} |")
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")


def main(out_dir: str) -> dict:
    t0 = time.time()
    runs = long_runs()
    imp = imposed(REF["theta"])
    keys = ("I", "II", "III-a", "III-b", "IV", "V")
    redesign = []
    for th in THETAS:
        ip = imposed_small(th)
        redesign.append(dict(
            theta=th, kept_peak=bool(ip["III-a-nomoney"] > 0.99),
            cap_IIIb=lr(runs, "III-b", REF["p"], th)["cap"],
            cap_II=lr(runs, "II", REF["p"], th)["cap"],
            R_IIIb_6=ip["III-b"], R_II_6=ip["II"]))
    res = dict(
        params=dict(T=T, seeds=list(SEEDS), ps=PS, thetas=THETAS, taus=TAUS,
                    Ls=LS, cs=CS, ref=REF, reps=REPS, g=G),
        runs=runs, imposed=imp, dominance=dominance_table(imp, keys),
        rankings=rankings(runs, imp, REF["p"], REF["L"], REF["c"], keys),
        break_even={"II vs I": break_even(runs, imp, "II", "I", REF["theta"]),
                    "III-b vs I": break_even(runs, imp, "III-b", "I", REF["theta"]),
                    "II vs III-b": break_even(runs, imp, "II", "III-b", REF["theta"])},
        redesign=redesign, reserve_sweep=reserve_sweep(), novel=novel())
    res["runtime_s"] = time.time() - t0
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "results.json"), "w") as f:
        json.dump(res, f, indent=1)
    write_md(res, os.path.join(out_dir, "results.md"))
    return res


def imposed_small(theta: float) -> dict[str, float]:
    """R(6) for II and III-b, and III-a's readiness with no outside money."""
    r = all_regimes(theta)
    out = {k: float(m.readiness(m.impose(r[k], 1000, g=G, seed=3),
                                np.array([6]))[0]) for k in ("II", "III-b")}
    out["III-a-nomoney"] = float(m.readiness(
        m.impose(r["III-a"], 300, g=0.0, seed=3), np.array([40]))[0])
    return out


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    main(sys.argv[1] if len(sys.argv) > 1 else here)
