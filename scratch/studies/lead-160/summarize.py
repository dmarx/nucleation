"""Summarize results.jsonl into summary.md (means and ranges over seeds)."""
from __future__ import annotations

import json
import math
import os
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
AG = ("M", "P", "D")


def fmt(xs, p=3):
    xs = [x for x in xs if x is not None and not (isinstance(x, float) and math.isnan(x))]
    if not xs:
        return "n/a"
    a = np.array(xs, float)
    if a.min() == a.max():
        return f"{a.mean():.{p}f}"
    return f"{a.mean():.{p}f} [{a.min():.{p}f}, {a.max():.{p}f}]"


def main():
    rows = [json.loads(l) for l in open(os.path.join(HERE, "results.jsonl"))]
    seeds = sorted({r["seed"] for r in rows})
    out = [f"# LEAD-160 results ({len(seeds)} mazes, 8x8, seeds {seeds[0]}-{seeds[-1]})", "",
           "Mean over mazes, [min, max] where they differ.", ""]

    lev = defaultdict(list)
    for r in rows:
        if r["item"].startswith("level:"):
            lev[r["item"][6:]].append(r)
    out += ["## Test 1: competence at matched levels (same training stream for all three)", "",
            "| level | transitions | success M / P / D | path excess M / P / D | action agreement M-P / M-D |",
            "|---|---|---|---|---|"]
    for name, rs in lev.items():
        out.append("| {} | {} | {} | {} | {} |".format(
            name, fmt([r["n_transitions"] for r in rs], 0),
            " / ".join(fmt([r["competence"][a]["success"] for r in rs]) for a in AG),
            " / ".join(fmt([r["competence"][a]["excess"] for r in rs]) for a in AG),
            fmt([r["agreement"]["M_P"] for r in rs]) + " / " + fmt([r["agreement"]["M_D"] for r in rs])))
    r0 = next(iter(lev.values()))[0]
    out += ["", "Resources at full coverage (first maze): "
            + "; ".join(f"{a}: memory {r0['competence'][a]['memory']} numbers" for a in AG)
            + ". Training updates (unit writes to convergence, full coverage): "
            + "; ".join(f"{a} {fmt([r['competence'][a]['train_updates'] for r in lev['full_coverage']], 0)}" for a in AG), ""]

    out += ["## Test 2: on-demand queries (accuracy against the true maze)", ""]
    c = r0["costs"]
    fams = ("Q1_next", "Q2_dist", "Q3_occ", "Q4_dist_do", "Q4_occ_do")
    for name, rs in lev.items():
        out += [f"### {name}", "", "| query | M | P | D | P without extraction |", "|---|---|---|---|---|"]
        for q in fams:
            cells = [fmt([r["queries"][q][a] for r in rs]) for a in AG]
            own = fmt([r["queries"][q]["P_own"] for r in rs]) if q == "Q4_dist_do" else ""
            out.append(f"| {q} | " + " | ".join(cells) + f" | {own} |")
        if "changed_frac" in rs[0]["queries"]["Q4_dist_do"]:
            out.append("")
            out.append("Fraction of pairs whose distance the intervention changes: "
                       + fmt([r["queries"]["Q4_dist_do"]["changed_frac"] for r in rs]))
        out.append("")
    out += ["### Cost of each agent's procedure (elementary operations, S = 64)", "",
            "| query | M | P | D |", "|---|---|---|---|"]
    for q in fams:
        out.append(f"| {q} | " + " | ".join(f"{c[q][a]:,}" for a in AG) + " |")
    out.append("| per-decision budget | " + " | ".join(f"{c['budget_own'][a]:,}" for a in AG) + " |")
    out += ["", "Available within the agent's own per-decision budget:", ""]
    for q in fams:
        out.append(f"- {q}: " + (", ".join(a for a in AG if c[q][a] <= c["budget_own"][a]) or "none"))
    out += ["", f"Available within a common budget of {c['budget_common']:,} (the planner's):", ""]
    for q in fams:
        out.append(f"- {q}: " + (", ".join(a for a in AG if c[q][a] <= c["budget_common"]) or "none"))
    out.append("")

    out += ["## Test 3: targeted intervention on the unit carrying a passage (block it)", "",
            "Success in the blocked maze before and after the edit; 'repaired' is the share of the pairs "
            "the unedited agent failed that the edited one solves.", "",
            "| agent | success before | success after | repaired | path excess after | numbers written |",
            "|---|---|---|---|---|---|"]
    ed = [row for r in rows if r["item"] == "edit" for row in r["rows"]]
    for a in AG + ("D_global",):
        out.append(f"| {a} | {fmt([x[a]['pre_success'] for x in ed])} | {fmt([x[a]['post_success'] for x in ed])} | "
                   f"{fmt([x[a]['repaired'] for x in ed])} | {fmt([x[a]['post_excess'] for x in ed])} | "
                   f"{ed[0][a]['units_written']} |")
    out.append("")

    def curves(prefix):
        rs = [r for r in rows if r["item"].startswith(prefix)]
        cps = [p[0] for p in rs[0]["curves"]["M"]]
        lines = ["| steps | " + " | ".join(f"{a} success" for a in AG) + " | "
                 + " | ".join(f"{a} excess" for a in AG) + " |",
                 "|---" * (1 + 2 * len(AG)) + "|"]
        for i, cp in enumerate(cps):
            lines.append(f"| {cp} | " + " | ".join(fmt([r["curves"][a][i][1] for r in rs]) for a in AG) + " | "
                         + " | ".join(fmt([r["curves"][a][i][2] for r in rs]) for a in AG) + " |")
        return lines, len(rs)

    for kind in ("block", "shortcut"):
        ls, n = curves(f"change:{kind}")
        out += [f"## Test 4a: environmental change ({kind}), recovery by online learning from a random walk ({n} runs)", ""] + ls + [""]
    for f in ("0.1", "0.3"):
        ls, n = curves(f"damage:{f}")
        dm = [r for r in rows if r["item"].startswith(f"damage:{f}")]
        out += [f"## Test 4b: damage to {f} of the units, recovery by online learning ({n} runs)", ""] + ls + [""]
        out += ["Detection by the agent's own error signal at the first revisit of each unit:", "",
                "| agent | damaged units changed | hit rate | false alarm rate |", "|---|---|---|---|"]
        for a in AG:
            out.append(f"| {a} | {fmt([r['detection'][a]['n_effective'] for r in dm], 0)} | "
                       f"{fmt([r['detection'][a]['hit_rate'] for r in dm])} | "
                       f"{fmt([r['detection'][a]['false_alarm_rate'] for r in dm])} |")
        out.append("")
    with open(os.path.join(HERE, "summary.md"), "w") as fh:
        fh.write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
