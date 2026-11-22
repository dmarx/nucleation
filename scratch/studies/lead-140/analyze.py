"""Tables for LEAD-140 from results/*.jsonl. Writes results/tables.md.

    python3 -I analyze.py
"""
import json
import os
import sys
from collections import defaultdict

import numpy as np
from scipy.stats import wilcoxon

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rsi  # noqa: E402
from study import done, DAMAGE  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DMG = ("dmg:generate", "dmg:admit", "dmg:score")


def m(b):
    """Battery metrics: held-out score (mean U over the six kinds), public
    score (ordinary U), damage cases recovered (of 72), out-of-family
    recognized (of 24)."""
    return {"heldout": float(np.mean([b[k]["U"] for k in rsi.BATTERY])),
            "public": b["ordinary"]["U"],
            "dmg_ok": sum(b[k]["ok"] for k in DMG),
            "oof_ok": b["oof"]["ok"]}


def fmt(x, d=3):
    return f"{x:.{d}f}"


def paired(a, b):
    a, b = np.asarray(a), np.asarray(b)
    d = b - a
    try:
        p = wilcoxon(d).pvalue if np.any(d != 0) else 1.0
    except ValueError:
        p = 1.0
    return d.mean(), int((d > 0).sum()), int((d < 0).sum()), p


def main():
    out = []
    lins = done("lineages")
    tr = done("transplant")
    dm = done("damage")
    by_arm = defaultdict(list)
    for L in lins.values():
        by_arm[L["arm"]].append(L)
    base = m(tr["theta0"]["battery"]) if "theta0" in tr else None

    out.append("# LEAD-140 tables\n")
    if base:
        out.append(f"Starting artifact theta0 on the held-out battery: held-out "
                   f"{fmt(base['heldout'])}, public {fmt(base['public'])}, "
                   f"damage recovered {base['dmg_ok']}/72, out-of-family "
                   f"{base['oof_ok']}/24.\n")

    out.append("## Phase 1: the lineages' own products after 60 generations\n")
    out.append("Means over lineages of the evolved artifact on the frozen "
               "held-out battery; the improver each ended with.\n")
    out.append("| arm | n | held-out | public | damage /72 | oof /24 | "
               "self-check off | d_dmg=0 | d_oof=0 | canary off | archive on "
               "| n_cand | phi changes | inner eps | outer eps |")
    out.append("|" + "---|" * 15)
    for arm in rsi.ARMS:
        Ls = by_arm.get(arm, [])
        if not Ls:
            continue
        ms = [m(L["battery"]) for L in Ls]
        pv = [rsi.phi_values(L["phi"]) for L in Ls]
        tv = [rsi.theta_values(L["theta"]) for L in Ls]
        nch = [sum(1 for h in L["history"] if h.get("meta") and h["took"])
               for L in Ls]
        out.append(
            f"| {arm} | {len(Ls)} | {fmt(np.mean([x['heldout'] for x in ms]))} "
            f"| {fmt(np.mean([x['public'] for x in ms]))} "
            f"| {np.mean([x['dmg_ok'] for x in ms]):.1f} "
            f"| {np.mean([x['oof_ok'] for x in ms]):.1f} "
            f"| {sum(t['SELF_CHECK_EVERY'] == 0 for t in tv)} "
            f"| {sum(p['d_dmg'] == 0 for p in pv)} "
            f"| {sum(p['d_oof'] == 0 for p in pv)} "
            f"| {sum(p['canary'] == 0 for p in pv)} "
            f"| {sum(p['archive'] == 1 for p in pv)} "
            f"| {np.mean([p['n_cand'] for p in pv]):.2f} "
            f"| {np.mean(nch):.1f} "
            f"| {np.mean([L['inner_eps'] for L in Ls]):.0f} "
            f"| {np.mean([L['outer_eps'] for L in Ls]):.0f} |")
    out.append("")
    out.append("Evolved procedures (theta) per arm, counts of lineages per value:\n")
    for arm in rsi.ARMS:
        Ls = by_arm.get(arm, [])
        if not Ls:
            continue
        parts = []
        for f in rsi.FIELDS:
            c = defaultdict(int)
            for L in Ls:
                c[rsi.theta_values(L["theta"])[f]] += 1
            parts.append(f + " " + ", ".join(f"{k}:{v}" for k, v in sorted(c.items())))
        out.append(f"- {arm}: " + "; ".join(parts))
    out.append("")

    if tr:
        out.append("## Phase 2: earlier and later improvers from the same start\n")
        out.append("Each improver applied for 10 generations at 32 episodes each "
                   "(equal budget; the layered arm's outside veto counted "
                   "separately), on the same seeds, then scored on the held-out "
                   "battery. Means over lineages (replicates averaged first). "
                   "'orig' is the fresh starting artifact theta0; 'improved' the "
                   "lineage's evolved artifact. early = the arm's starting "
                   "improver with an empty record; late = the evolved improver "
                   "with its record; knowledge = starting settings with the "
                   "evolved record; organization = evolved settings, empty record.\n")
        cells = [("orig", "early"), ("orig", "late"), ("orig", "knowledge"),
                 ("orig", "organization"), ("improved", "early"),
                 ("improved", "late")]
        out.append("| arm | " + " | ".join(f"{a}/{i}" for a, i in cells) + " |")
        out.append("|" + "---|" * (len(cells) + 1))
        per = defaultdict(lambda: defaultdict(list))
        for r in tr.values():
            if r["key"] == "theta0":
                continue
            per[(r["arm"], r["lineage"])][(r["artifact"], r["improver"])].append(r)
        agg = defaultdict(dict)  # arm -> cell -> list over lineages of metrics
        for (arm, lin), d in per.items():
            for c, rs in d.items():
                ms = [m(r["battery"]) for r in rs]
                agg[arm].setdefault(c, []).append(
                    {k: float(np.mean([x[k] for x in ms])) for k in ms[0]})
        for metric, label in (("heldout", "held-out score"),
                              ("public", "public score"),
                              ("dmg_ok", "damage recovered /72"),
                              ("oof_ok", "out-of-family /24")):
            out.append(f"| **{label}** |" + " |" * len(cells))
            for arm in rsi.ARMS:
                if arm not in agg:
                    continue
                row = []
                for c in cells:
                    v = agg[arm].get(c, [])
                    row.append(fmt(np.mean([x[metric] for x in v]),
                                   1 if metric.endswith("ok") else 3) if v else "")
                out.append(f"| {arm} | " + " | ".join(row) + " |")
        out.append("")
        out.append("Paired contrasts on the held-out score (mean difference; "
                   "lineages better / worse; Wilcoxon p):\n")
        out.append("| arm | late - early, from theta0 | knowledge - early | "
                   "organization - early | improved artifact - orig, early improver "
                   "| late - early, from improved |")
        out.append("|---|---|---|---|---|---|")
        for arm in rsi.ARMS:
            if arm not in agg:
                continue
            a = agg[arm]
            lin_keys = sorted({lin for (ar, lin) in per if ar == arm})

            def col(c, metric="heldout"):
                return [float(np.mean([m(r["battery"])[metric]
                                       for r in per[(arm, lin)][c]]))
                        for lin in lin_keys if c in per[(arm, lin)]]
            cols = []
            for x, y in ((("orig", "early"), ("orig", "late")),
                         (("orig", "early"), ("orig", "knowledge")),
                         (("orig", "early"), ("orig", "organization")),
                         (("orig", "early"), ("improved", "early")),
                         (("improved", "early"), ("improved", "late"))):
                cx, cy = col(x), col(y)
                if len(cx) == len(cy) and cx:
                    d, up, dn, p = paired(cx, cy)
                    cols.append(f"{d:+.4f}; {up}/{dn}; {p:.3g}")
                else:
                    cols.append("")
            out.append(f"| {arm} | " + " | ".join(cols) + " |")
        out.append("")

    if dm:
        out.append("## Phase 3: damage to the improver's diagnostic machinery\n")
        out.append("The later improver applied to the lineage's evolved artifact "
                   "for 10 generations with its suite lesioned from the start: "
                   "generate (damage and out-of-family cases silently replaced "
                   "by ordinary ones), admit (failed damage and out-of-family "
                   "episodes dropped from the score), score (a bonus to the "
                   "incumbent), obsolete (the successor inherits the starting "
                   "settings and an empty record); _nocanary removes the "
                   "suite's self-test. Means over lineages.\n")
        out.append("| arm | damage | flagged | flagged at gen 0 | held-out | "
                   "public | damage /72 | oof /24 | self-check off |")
        out.append("|" + "---|" * 9)
        g = defaultdict(list)
        for r in dm.values():
            g[(r["arm"], r["damage"])].append(r)
        for arm in rsi.ARMS:
            for d in DAMAGE:
                rs = g.get((arm, d))
                if not rs:
                    continue
                ms = [m(r["battery"]) for r in rs]
                fl = [r["flagged_at"] for r in rs]
                out.append(
                    f"| {arm} | {d} | {sum(f is not None for f in fl)}/{len(rs)} "
                    f"| {sum(f == 0 for f in fl)} "
                    f"| {fmt(np.mean([x['heldout'] for x in ms]))} "
                    f"| {fmt(np.mean([x['public'] for x in ms]))} "
                    f"| {np.mean([x['dmg_ok'] for x in ms]):.1f} "
                    f"| {np.mean([x['oof_ok'] for x in ms]):.1f} "
                    f"| {sum(rsi.theta_values(r['theta'])['SELF_CHECK_EVERY'] == 0 for r in rs)} |")
        out.append("")
    txt = "\n".join(out)
    with open(os.path.join(HERE, "results", "tables.md"), "w") as f:
        f.write(txt + "\n")
    print(txt)


if __name__ == "__main__":
    main()
