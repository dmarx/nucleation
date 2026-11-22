"""LEAD-052: phase maps and summary numbers from results/runs.jsonl.

    python3 -I analyse.py [delta] [tol]      (defaults 0.1 and 1.25)

Writes results/summary_<delta>_<tol>.json and prints the maps.
Map letters: C coarse-first, F fine-first, S simultaneous, M mixed,
I incomplete; lower case when the seeds disagree (the majority shown).
"""
import json
import os
import sys
from collections import Counter, defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import phases as ph  # noqa: E402

LETTER = {"coarse-first": "C", "fine-first": "F", "simultaneous": "S",
          "mixed": "M", "incomplete": "I"}


def load():
    with open(os.path.join(HERE, "results", "runs.jsonl")) as f:
        return [json.loads(line) for line in f]


def point_key(p):
    return tuple(sorted(p.items()))


def predicted_class(rec, rule, tol):
    c, g = np.array(rec["c"][1:]), np.array(rec["g"][1:])
    if rule == "by_cross_covariance":      # deep linear, eps -> 0: T ~ 1/(c g)
        return ph.classify(1 / (c * g), tol)
    if rule == "by_input_variance":        # linear kernel: T ~ 1/c^2
        return ph.classify(1 / c ** 2, tol)
    if rule == "by_target_strength":       # T ~ 1/g
        return ph.classify(1 / g, tol)
    raise ValueError(rule)


def exponents(recs, delta):
    """Within-point least squares of log T_l on log g_l and log c_l (levels
    1..3), pooling points and seeds: T ~ g^beta_g c^beta_c."""
    rows, ys = [], []
    for r in recs:
        T = np.array(r["T"][str(delta)])
        if not np.all(np.isfinite(T)):
            continue
        lg, lc, lt = (np.log(np.array(r["g"][1:])), np.log(np.array(r["c"][1:])), np.log(T))
        rows.append(np.stack([lg - lg.mean(), lc - lc.mean()], 1))
        ys.append(lt - lt.mean())
    if not rows:
        return None
    A, y = np.vstack(rows), np.concatenate(ys)
    keep = [j for j in range(2) if np.any(np.abs(A[:, j]) > 1e-12)]
    coef = np.full(2, np.nan)
    sol, *_ = np.linalg.lstsq(A[:, keep], y, rcond=None)
    coef[keep] = sol
    resid = y - A[:, keep] @ sol
    r2 = 1 - resid.var() / y.var() if y.var() > 1e-12 else np.nan
    return dict(beta_g=None if np.isnan(coef[0]) else round(float(coef[0]), 3),
                beta_c=None if np.isnan(coef[1]) else round(float(coef[1]), 3),
                r2=None if np.isnan(r2) else round(float(r2), 3))


def main():
    delta = float(sys.argv[1]) if len(sys.argv) > 1 else 0.1
    tol = float(sys.argv[2]) if len(sys.argv) > 2 else 1.25
    recs = load()
    by = defaultdict(list)
    for r in recs:
        by[(r["exp"], r["learner"])].append(r)
    summary = {}
    for exp, axes in (("E1", ("la", "lb")), ("E2", ("log2_rho_in", "log2_rho_out"))):
        learners = sorted({l for (e, l) in by if e == exp})
        for learner in learners:
            rs = by[(exp, learner)]
            cells = defaultdict(list)
            for r in rs:
                cells[point_key(r["point"])].append(r)
            xs = sorted({r["point"][axes[0]] for r in rs})
            ys = sorted({r["point"][axes[1]] for r in rs})
            grid, counts, agree = [], Counter(), Counter()
            n_split = 0
            for x in xs:
                row = ""
                for y in ys:
                    cell = cells.get(point_key({axes[0]: x, axes[1]: y}), [])
                    if not cell:
                        row += "."
                        continue
                    cls = [ph.classify(r["T"][str(delta)], tol) for r in cell]
                    top, n = Counter(cls).most_common(1)[0]
                    split = n < len(cls)
                    n_split += split
                    row += LETTER[top].lower() if split else LETTER[top]
                    counts[top] += 1
                    for rule in ("by_cross_covariance", "by_input_variance",
                                 "by_target_strength"):
                        agree[rule] += predicted_class(cell[0], rule, tol) == top
                grid.append(row)
            n_cells = sum(counts.values())
            summary[f"{exp}/{learner}"] = dict(
                axes=axes, rows=xs, cols=ys, map=grid, counts=dict(counts),
                cells=n_cells, seed_split_cells=n_split,
                agreement={k: round(v / n_cells, 3) for k, v in agree.items()},
                exponents=exponents(rs, delta))
    e3 = defaultdict(dict)
    for (exp, learner), rs in by.items():
        if exp != "E3":
            continue
        for prof in sorted({r["point"]["profile"] for r in rs}):
            sub = [r for r in rs if r["point"]["profile"] == prof]
            cls = [ph.classify(r["T"][str(delta)], tol) for r in sub]
            Ts = np.array([r["T"][str(delta)] for r in sub])
            e3[learner][prof] = dict(classes=[LETTER[c] for c in cls],
                                     T_mean=np.round(Ts.mean(0), 3).tolist())
        e3[learner]["exponents"] = exponents(rs, delta)
    summary["E3"] = e3
    out = os.path.join(HERE, "results", f"summary_{delta:g}_{tol:g}.json")
    with open(out, "w") as f:
        json.dump(summary, f, indent=1)
    for k, v in summary.items():
        if k == "E3":
            continue
        print(f"\n{k}  rows {v['axes'][0]} {v['rows'][0]:g}..{v['rows'][-1]:g}, "
              f"cols {v['axes'][1]}  counts {v['counts']}  seed-split {v['seed_split_cells']}")
        print("  agreement", v["agreement"], " exponents", v["exponents"])
        for row in v["map"]:
            print("   ", row)
    print("\nE3")
    for learner in sorted(e3):
        d = e3[learner]
        print(f"  {learner:24s}", {p: "".join(d[p]["classes"]) for p in d if p != "exponents"},
              d["exponents"])


if __name__ == "__main__":
    main()
