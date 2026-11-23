"""Summarize results/probes.jsonl into results/summary.json and print tables.

python3 -I analyze.py
"""
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
MEASURES = ["peak_forget", "A_at_B", "tB", "cos0", "seg_end"]
STATES = ["permuted", "rescaled", "ablate_selective", "ablate_random", "continued"]
PROBES = ["sgd", "heavy", "adam", "sign"]
T975 = {11: 2.201, 10: 2.228, 9: 2.262, 8: 2.306, 7: 2.365}


def load():
    rows = [json.loads(l) for l in open(os.path.join(RES, "probes.jsonl"))]
    table = {}
    for r in rows:
        table[(r["trainer"], r["seed"], r["state"], r["probe"])] = r
    return rows, table


def paired(table, tr, seeds, cell, base, m):
    d = []
    for s in seeds:
        x, y = table.get((tr, s) + cell), table.get((tr, s) + base)
        if x is None or y is None:
            continue
        a, b = x[m], y[m]
        if m == "tB" and (a < 0 or b < 0):
            continue
        if np.isnan(a) or np.isnan(b):
            continue
        d.append(a - b)
    d = np.array(d)
    n = len(d)
    if n < 2:
        return {"n": n}
    se = d.std(ddof=1) / np.sqrt(n)
    t = T975.get(n - 1, 2.2)
    return {"n": n, "mean": float(d.mean()), "lo": float(d.mean() - t * se),
            "hi": float(d.mean() + t * se)}


def cell_mean(table, tr, seeds, state, probe, m):
    v = [table[(tr, s, state, probe)][m] for s in seeds if (tr, s, state, probe) in table]
    v = [x for x in v if not (isinstance(x, float) and np.isnan(x)) and not (m == "tB" and x < 0)]
    return float(np.mean(v)) if v else float("nan"), (float(np.std(v, ddof=1)) if len(v) > 1 else float("nan"))


def decomposition(table, tr, seeds, m):
    """Two-way split of the seed-averaged cell means over (state, probe),
    states intact + four disruptions (permuted is identical to intact),
    probes the four reset optimizers."""
    sts = ["intact", "rescaled", "ablate_selective", "ablate_random", "continued"]
    M = np.array([[cell_mean(table, tr, seeds, s, o, m)[0] for o in PROBES] for s in sts])
    g = M.mean()
    rs, cs = M.mean(1) - g, M.mean(0) - g
    ss_state = M.shape[1] * np.sum(rs ** 2)
    ss_opt = M.shape[0] * np.sum(cs ** 2)
    ss_tot = np.sum((M - g) ** 2)
    return {"state": float(ss_state / ss_tot), "optimizer": float(ss_opt / ss_tot),
            "interaction": float((ss_tot - ss_state - ss_opt) / ss_tot),
            "cells": M.round(4).tolist(), "states": sts, "probes": PROBES}


def main():
    rows, table = load()
    cal = json.load(open(os.path.join(RES, "calibration.json")))
    out = {"calibration": cal, "trainers": {}}
    for tr in ["heavy", "adam"]:
        seeds = sorted({r["seed"] for r in rows if r["trainer"] == tr})
        base = ("intact", tr)
        o = {"seeds": len(seeds), "baseline": {}, "optimizer_arm": {}, "state_arm": {},
             "state_arm_by_probe": {}, "decomposition": {}}
        for m in MEASURES:
            o["baseline"][m] = cell_mean(table, tr, seeds, "intact", tr, m)
            o["optimizer_arm"][m] = {p: paired(table, tr, seeds, ("intact", p), base, m)
                                     for p in PROBES + [tr + "_carried"] if p != tr}
            o["state_arm"][m] = {s: paired(table, tr, seeds, (s, tr), base, m) for s in STATES}
            o["state_arm_by_probe"][m] = {
                p: {s: paired(table, tr, seeds, (s, p), ("intact", p), m) for s in STATES}
                for p in PROBES}
            o["decomposition"][m] = decomposition(table, tr, seeds, m)
        o["train_levels"] = {
            s: [float(np.mean([table[(tr, sd, s, tr)]["sA_train"] for sd in seeds])),
                float(np.mean([table[(tr, sd, s, tr)]["sB_train"] for sd in seeds]))]
            for s in ["intact"] + STATES}
        o["segregation_before_probe"] = {
            s: float(np.mean([table[(tr, sd, s, tr)]["seg"] for sd in seeds]))
            for s in ["intact"] + STATES}
        out["trainers"][tr] = o
    json.dump(out, open(os.path.join(RES, "summary.json"), "w"), indent=1)

    def fmt(r):
        if "mean" not in r:
            return "n/a"
        star = "*" if r["lo"] > 0 or r["hi"] < 0 else " "
        return f"{r['mean']:+.4f} [{r['lo']:+.4f},{r['hi']:+.4f}]{star}"

    for tr, o in out["trainers"].items():
        print(f"\n=== trained by {tr}, {o['seeds']} seeds ===")
        print("train levels", {k: [round(x, 4) for x in v] for k, v in o["train_levels"].items()})
        print("segregation", {k: round(v, 3) for k, v in o["segregation_before_probe"].items()})
        for m in MEASURES:
            b = o["baseline"][m]
            print(f"\n{m}: baseline (intact, {tr}) {b[0]:.4f} sd {b[1]:.4f}")
            for p, r in o["optimizer_arm"][m].items():
                print(f"  optimizer -> {p:14s} {fmt(r)}")
            for s, r in o["state_arm"][m].items():
                print(f"  state     -> {s:16s} {fmt(r)}")
            d = o["decomposition"][m]
            print(f"  shares: state {d['state']:.2f} optimizer {d['optimizer']:.2f} "
                  f"interaction {d['interaction']:.2f}")
        print("\nstate effects on peak_forget under each probe optimizer:")
        for p in PROBES:
            print("  ", p, {s: fmt(r) for s, r in o["state_arm_by_probe"]["peak_forget"][p].items()})


if __name__ == "__main__":
    main()
