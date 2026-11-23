"""Summarize results/runs.jsonl into results/summary.json and a printed table.

Run:  python3 -I analyze.py
"""
import json
import os
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, "results", "runs.jsonl"))]

by = defaultdict(list)
for r in rows:
    by[(r["task"], r["mode"], r["c"])].append(r)

summary = {"n_rows": len(rows),
           "max_aux_fn_diff_after_rescale": max(r["aux_fn_maxdiff_after_rescale"] for r in rows),
           "max_pretrain_err": max(r["pretrain_err"] for r in rows),
           "max_train_loss": max(r["train_loss"] for r in rows),
           "cells": []}
for (task, mode, c), rs in sorted(by.items()):
    g = np.array([r["gen_err"] for r in rs])
    summary["cells"].append({"task": task, "mode": mode, "c": c, "n": len(rs),
                             "gen_err_mean": float(g.mean()),
                             "gen_err_median": float(np.median(g)),
                             "gen_err_sd": float(g.std(ddof=1)) if len(g) > 1 else None})

# Paired comparison: per seed, which c gives the lowest error under full FT.
best = defaultdict(lambda: defaultdict(int))
seeds = sorted({r["seed"] for r in rows})
for task in ("nested", "dense"):
    for s in seeds:
        rs = [r for r in rows if r["task"] == task and r["mode"] == "full" and r["seed"] == s]
        if rs:
            best[task][min(rs, key=lambda r: r["gen_err"])["c"]] += 1
summary["best_c_count_full"] = {t: dict(v) for t, v in best.items()}

# Paired comparisons under full fine-tuning, with an exact two-sided sign test.
from math import comb


def sign_p(k, n):
    tail = sum(comb(n, i) for i in range(0, min(k, n - k) + 1)) / 2 ** n
    return min(1.0, 2 * tail)


full = {(r["seed"], r["task"], r["c"]): r["gen_err"] for r in rows if r["mode"] == "full"}
pairs = []
for task in ("nested", "dense"):
    for a, b in ((0.3, 2.0), (0.3, 1.0), (1.0, 2.0)):
        ss = [s for s in seeds if (s, task, a) in full and (s, task, b) in full]
        k = sum(full[(s, task, a)] < full[(s, task, b)] for s in ss)
        pairs.append({"task": task, "a": a, "b": b, "a_wins": k, "n": len(ss),
                      "sign_test_p": sign_p(k, len(ss))})
summary["paired_full"] = pairs

# Linear probing: largest difference in the learned beta across c, per seed and task.
probe_diff = 0.0
for task in ("nested", "dense"):
    for s in seeds:
        bs = [np.array(r["beta"]) for r in rows
              if r["task"] == task and r["mode"] == "probe" and r["seed"] == s]
        for b in bs[1:]:
            probe_diff = max(probe_diff, float(np.max(np.abs(b - bs[0]))))
summary["probe_max_beta_diff_across_c"] = probe_diff

json.dump(summary, open(os.path.join(HERE, "results", "summary.json"), "w"), indent=1)
for k in ("n_rows", "max_aux_fn_diff_after_rescale", "max_pretrain_err", "max_train_loss",
          "probe_max_beta_diff_across_c", "best_c_count_full", "paired_full"):
    print(k, summary[k])
for cell in summary["cells"]:
    print(cell)
