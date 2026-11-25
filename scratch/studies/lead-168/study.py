"""LEAD-168 study: where arrangements I and C first differ, under each reading.

Run:  OPENBLAS_NUM_THREADS=1 python3 -I study.py   (from this directory, or
      pass the directory; writes results.json and results.md beside it)
"""
import json
import os
import sys
from collections import Counter
from itertools import product

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as m  # noqa: E402


def part_a():
    """Fixed-policy reading: enumerate every probe, find where traces part."""
    rows, counts = [], Counter()
    for p in m.all_probes(caps=(True, False)):
        ti, tc = m.trace("I", p), m.trace("C", p)
        d = m.first_divergence(ti, tc)
        counts[d] += 1
        rows.append({"probe": p.__dict__, "I": ti, "C": tc, "first": d,
                     "routine": m.routine(p)})
    separating = [r for r in rows if r["first"] is not None]
    cond = {
        "all_separating_are_x_challenged_adverse_withhold_capable": all(
            r["probe"]["act"] == "x" and r["probe"]["challenged"]
            and r["probe"]["adverse"] and r["probe"]["disposition"] == "withhold"
            and r["probe"]["cap"] for r in separating),
        "every_such_probe_separates": all(
            r["first"] is not None for r in rows
            if r["probe"]["act"] == "x" and r["probe"]["challenged"]
            and r["probe"]["adverse"] and r["probe"]["disposition"] == "withhold"
            and r["probe"]["cap"]),
        "no_routine_probe_separates": all(r["first"] is None
                                          for r in rows if r["routine"]),
        "no_acquiescent_probe_separates": all(
            r["first"] is None for r in rows
            if r["probe"]["disposition"] == "acquiesce"),
        "first_stage_of_separation": sorted({r["first"] for r in separating}),
    }
    return {"n_probes": len(rows), "first_counts": {str(k): v for k, v in
                                                    counts.items()},
            "conditions": cond,
            "separating": separating}


def part_b(deadline=10):
    """Delay variant: E conditions by holding an adverse order d steps."""
    out = []
    for d in range(0, 13):
        p = m.Probe("x", True, True, "withhold", True, d, 1, deadline)
        ti, tc = m.trace("I", p), m.trace("C", p)
        out.append({"delay": d, "I": ti, "C": tc,
                    "first": m.first_divergence(ti, tc),
                    "outcome_differs": ti[4] != tc[4]})
    return {"deadline": deadline, "t_order": 1, "rows": out}


def part_c(n=41):
    """Anticipation reading over a grid of payoffs, for each depth."""
    grid = np.linspace(0.05, 2.0, n)
    ps = np.linspace(0.05, 0.95, 19)
    res = {}
    for depth in ("myopic", "reviewer", "full"):
        cnt = Counter()
        alike_and_part = 0
        total = 0
        for g, kw, c, p, u, l in product(grid[::4], grid[::4], (0.5, 1.0),
                                         ps[::3], (0.5, 1.5), (1.0,)):
            pay = m.Payoffs(g, c, kw, p, u, l)
            d = m.first_divergence_game(pay, depth)
            cnt[str(d)] += 1
            total += 1
            if d in ("ruling", "enforcement"):
                alike_and_part += 1
        res[depth] = {"total": total,
                      "first_counts": dict(cnt),
                      "share_alike_in_routine_and_parting": alike_and_part / total}
    # the analytic boundary for 'full': with E disposed to withhold (g > kw),
    # the first difference is the action iff (1-p) g <= p c.
    check = []
    for g, kw, c, p in product(grid[::5], grid[::5], (0.5, 1.0), ps[::2]):
        pay = m.Payoffs(g, c, kw, p, 0.5, 1.0)
        d = m.first_divergence_game(pay, "full")
        predicted = ("action" if g > kw and (1 - p) * g - p * c <= 0 else
                     None if g <= kw else "ruling")
        check.append(d == predicted)
    res["full_boundary_matches_analytic"] = bool(all(check))
    res["full_boundary_cases"] = len(check)
    return res


def part_d():
    """What a non-execution shows: P(E withheld | not executed) in C."""
    rows = []
    for q in (0.5, 0.8, 0.95, 0.99):
        for w in (0.05, 0.2, 0.5):
            rows.append({"q_cap": q, "w": w,
                         "P_withheld_given_not_executed":
                         round(m.p_withheld_given_not_executed(q, w), 4)})
    return rows


def part_e():
    """Structural reading: does F's act depend on E's signal?"""
    return {"I": m.f_depends_on_signal("I"), "C": m.f_depends_on_signal("C")}


def main():
    res = {"A_fixed_policy": part_a(), "B_delay": part_b(),
           "C_anticipation": part_c(), "D_nonexecution": part_d(),
           "E_structural": part_e()}
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(res, f, indent=1, default=str)
    a, b, c = res["A_fixed_policy"], res["B_delay"], res["C_anticipation"]
    lines = ["# LEAD-168 results", "",
             "## A. Fixed policies, every probe enumerated", "",
             f"- probes: {a['n_probes']}; first divergence counts: "
             f"{a['first_counts']}"]
    lines += [f"- {k}: {v}" for k, v in a["conditions"].items()]
    lines += ["", "Separating probes (I trace / C trace):", ""]
    for r in a["separating"]:
        lines.append(f"- {r['I']} / {r['C']}")
    lines += ["", f"## B. Delay variant (order at t=1, deadline {b['deadline']})",
              "", "| delay | first divergence | outcome differs |", "|---|---|---|"]
    for r in b["rows"]:
        lines.append(f"| {r['delay']} | {r['first']} | {r['outcome_differs']} |")
    lines += ["", "## C. Anticipation (backward induction on a payoff grid)", ""]
    for depth in ("myopic", "reviewer", "full"):
        lines.append(f"- {depth}: {c[depth]}")
    lines.append(f"- full-anticipation boundary matches (1-p)g <= pc with g > kw: "
                 f"{c['full_boundary_matches_analytic']} over "
                 f"{c['full_boundary_cases']} cases")
    lines += ["", "## D. P(E withheld | not executed) in C (0 in I)", "",
              "| q_cap | w | P |", "|---|---|---|"]
    for r in res["D_nonexecution"]:
        lines.append(f"| {r['q_cap']} | {r['w']} | "
                     f"{r['P_withheld_given_not_executed']} |")
    lines += ["", "## E. Structural: F's act depends on E's signal", "",
              f"- I: {res['E_structural']['I']}; C: {res['E_structural']['C']}"]
    with open(os.path.join(HERE, "results.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
