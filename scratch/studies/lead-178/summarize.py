"""Summarize results.jsonl into results.md."""
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R = [json.loads(x) for x in open(os.path.join(HERE, "results.jsonl"))]
out = []


def p(s=""):
    out.append(s)


def part(name):
    return [r for r in R if r["part"] == name and "T" in r]


def fmt(x):
    return "%.3g" % x


sand = [r for r in R if "lower" in r]
viol = [r for r in sand
        if not (r["lower"] - 1e-10 <= r["T"] <= r["upper"] + 1e-10)]
skipped = [r for r in R if r["part"] != "normbound" and "T" not in r]
p("# LEAD-178 results")
p()
p(f"Sandwich lower <= T <= upper checked on {len(sand)} items: "
  f"{len(viol)} violations. Items skipped as near-unstable: {len(skipped)}.")
p()
EPS = [0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625]
for name, lab in (("closed", "sum, equal column sums"),
                  ("leftvec", "left-Perron-weighted aggregate of the "
                   "unequal-column-sum block")):
    rs = part(name)
    T0 = max(abs(r["T"]) for r in rs if r["eps"] == 0)
    p(f"## {name}: {lab} (20 systems)")
    p()
    p(f"max |T| at eps = 0: {T0:.1e}")
    p()
    p("| eps | T/eps^2 min | max | lower/eps^2 min | upper/eps^2 max |")
    p("|---|---|---|---|---|")
    for e in EPS:
        x = [r for r in rs if r["eps"] == e]
        t = np.array([r["T"] for r in x]) / e ** 2
        lo = np.array([r["lower"] for r in x]) / e ** 2
        up = np.array([r["upper"] for r in x]) / e ** 2
        p(f"| {e} | {fmt(t.min())} | {fmt(t.max())} | {fmt(lo.min())} "
          f"| {fmt(up.max())} |")
    p()
rs = part("unclosed")
p("## unclosed: sum over a block with unequal column sums (20 systems)")
p()
p("| eps | T min | T max | lower min | max over systems of |T - T(0)|/eps |")
p("|---|---|---|---|---|")
T0 = {r["seed"]: r["T"] for r in rs if r["eps"] == 0}
for e in [0.0] + EPS:
    x = [r for r in rs if r["eps"] == e]
    t = [r["T"] for r in x]
    lo = [r["lower"] for r in x]
    d = "" if e == 0 else fmt(max(abs(r["T"] - T0[r["seed"]]) / e
                                  for r in x))
    p(f"| {e} | {fmt(min(t))} | {fmt(max(t))} | {fmt(min(lo))} | {d} |")
p()
rs = part("slowgap")
p("## slowgap: closed, every block's leading eigenvalue 1 - gamma "
  "(10 systems)")
p()
p("| gamma | eps | T/eps^2 median | min | max | lower/eps^2 median "
  "| upper/eps^2 median |")
p("|---|---|---|---|---|---|---|")
for g in [0.3, 0.1, 0.03, 0.01]:
    for e in [0.004, 0.002]:
        x = [r for r in rs if r["gamma"] == g and r["eps"] == e]
        t = np.array([r["T"] for r in x]) / e ** 2
        lo = np.array([r["lower"] for r in x]) / e ** 2
        up = np.array([r["upper"] for r in x]) / e ** 2
        p(f"| {g} | {e} | {fmt(np.median(t))} | {fmt(t.min())} "
          f"| {fmt(t.max())} | {fmt(np.median(lo))} "
          f"| {fmt(np.median(up))} |")
p()
rs = part("fastgap")
p("## fastgap: unclosed, eps = 0, fast eigenvalues of the block shrunk "
  "towards 0 (10 systems)")
p()
p("| spread | largest fast |eigenvalue| | T min | T max | lower min |")
p("|---|---|---|---|---|")
for sp in [0.6, 0.3, 0.1, 0.03, 0.0]:
    x = [r for r in rs if r["spread"] == sp]
    p(f"| {sp} | {fmt(max(r['fast'] for r in x))} "
      f"| {fmt(min(r['T'] for r in x))} | {fmt(max(r['T'] for r in x))} "
      f"| {fmt(min(r['lower'] for r in x))} |")
p()
rs = part("simon")
p("## simon: closed, gamma = 2 eps (10 systems)")
p()
p("| eps | T/eps median | min | max | T/eps^2 median |")
p("|---|---|---|---|---|")
for e in [0.04, 0.02, 0.01, 0.005, 0.0025]:
    t = np.array([r["T"] for r in rs if r["eps"] == e])
    p(f"| {e} | {fmt(np.median(t / e))} | {fmt((t / e).min())} "
      f"| {fmt((t / e).max())} | {fmt(np.median(t / e ** 2))} |")
p()
rs = [r for r in R if r["part"] == "normbound"]
ratio = np.array([r["T"] / r["scalar_bound"] for r in rs])
p(f"## normbound: scalar bound eps^2 ||LC||^2 kappa(V)^2 ||S|| "
  f"/ (2 G (1 - rho^2)) on {len(rs)} items")
p()
p(f"T / bound: max {fmt(ratio.max())}, median {fmt(np.median(ratio))}; "
  f"kappa(V) from {fmt(min(r['kappaV'] for r in rs))} to "
  f"{fmt(max(r['kappaV'] for r in rs))}.")
p()
open(os.path.join(HERE, "results.md"), "w").write("\n".join(out))
print("\n".join(out))
