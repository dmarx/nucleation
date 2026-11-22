"""Tables from results.jsonl (LEAD-182). Run: python3 -I scratch/studies/lead-182/summarize.py > scratch/studies/lead-182/summary.md"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, "results.jsonl")) if l.strip()]
ok = [r for r in rows if r.get("feasible")]


def table(title, sel, cols, fmt="{:.2f}"):
    ns = sorted({r["n"] for r in sel})
    groups = {}
    for r in sel:
        groups.setdefault((r["model"], r["dc"], r["signal"], r["base"]), {})[r["n"]] = r
    print(f"### {title}\n")
    for col, label in cols:
        print(f"{label}\n")
        print("| model | true Δ_C | signalling Δ | base | " + " | ".join(f"n={n}" for n in ns) + " |")
        print("|---|---|---|---|" + "---|" * len(ns))
        for k in sorted(groups, key=lambda k: (k[0], k[3], k[1] if k[1] is not None else 9, k[2])):
            g = groups[k]
            any_r = next(iter(g.values()))
            cells = [fmt.format(g[n][col]) if n in g else "" for n in ns]
            print(f"| {k[0]} | {any_r['true_dc']:.3f} | {k[2]} | {k[3]} | " + " | ".join(cells) + " |")
        print()


print("# LEAD-182 power simulation: summary\n")
print(f"{len(rows)} cells, {len(ok)} feasible; {ok[0]['reps']} replications a cell, "
      f"{ok[0]['boot']} bootstrap resamples. One-sided tests at 0.05 unless stated. "
      "'n' is respondents a context (four contexts an item).\n")
inf = [r for r in rows if not r.get("feasible")]
if inf:
    print("Infeasible (cells would be negative): " + "; ".join(
        f"{r['model']} Δ_C={r['dc']} Δ={r['signal']} base={r['base']}" for r in inf
        if r["n"] == min(x["n"] for x in rows)) + "\n")

pos = [r for r in ok if r["true_dc"] > 1e-9]
zero = [r for r in ok if abs(r["true_dc"]) <= 1e-9]
neg = [r for r in ok if r["true_dc"] < -1e-9]
table("Detection when the system is contextual (power)", pos,
      [("detect_boot_fixed", "Plug-in signalling, fixed signs, bootstrap:"),
       ("detect_boot_max", "Plug-in signalling, maximum over sign patterns, bootstrap:"),
       ("detect_boot_shrink", "Signalling soft-thresholded by one SE, fixed signs, bootstrap:"),
       ("detect_wald_fixed", "Plug-in, fixed signs, delta method:"),
       ("detect_boot_fixed_k8", "Plug-in, fixed signs, bootstrap at 0.05/8 (eight items):")])
table("False detection on the boundary (true Δ_C = 0; size)", zero,
      [("detect_boot_fixed", "Plug-in, fixed signs, bootstrap:"),
       ("detect_boot_shrink", "Soft-thresholded, bootstrap:"),
       ("detect_wald_fixed", "Plug-in, delta method:")], "{:.3f}")
table("False detection below the boundary (true Δ_C < 0)", neg,
      [("detect_boot_shrink", "Soft-thresholded, bootstrap:")], "{:.3f}")
table("Absence verdict (upper bound below 0) when the system is contextual (should be rare)", pos,
      [("absent_boot_fixed", "Plug-in, bootstrap:"),
       ("absent_boot_shrink", "Soft-thresholded, bootstrap:")], "{:.3f}")
table("Absence verdict on the boundary (true Δ_C = 0; size of the absence test)", zero,
      [("absent_boot_fixed", "Plug-in, bootstrap:"),
       ("absent_boot_shrink", "Soft-thresholded, bootstrap:")], "{:.3f}")
table("Absence verdict when the system is noncontextual (power to show absence)", neg,
      [("absent_boot_fixed", "Plug-in, bootstrap:"),
       ("absent_boot_shrink", "Soft-thresholded, bootstrap:")])
table("Bias of the estimates (mean estimate − true value)", [dict(r, bias_f=r["est_fixed_mean"] - r["true_dc"],
                                                               bias_s=r["est_shrink_mean"] - r["true_dc"],
                                                               bias_sig=r["signal_hat_mean"] - r["signal"]) for r in ok
                                                          if r["model"] == "symmetric" and r["dc"] == 0.19],
      [("bias_f", "Δ_C, plug-in:"), ("bias_s", "Δ_C, soft-thresholded:"), ("bias_sig", "Signalling Δ, plug-in:")],
      "{:+.3f}")
