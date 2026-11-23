"""LEAD-188 sensitivity sweep: how the Bayes factors of model.py move with
the number of identifiable distributors H, the transmissibility prior,
network size and seed. Observation fixed at q = 0.01; ascertainment
gamma in {0, 1}. Appends one JSON line per setting to sensitivity.jsonl
and skips settings already written.

Run:  python3 -I sensitivity.py
"""
import json
import sys
from itertools import product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # -I drops the script's directory
import model as M  # noqa: E402
OUT = HERE / "sensitivity.jsonl"


def key(d):
    return (d["n"], d["H"], d["t_b"], d["seed"])


def main():
    done = set()
    if OUT.exists():
        for ln in OUT.read_text().splitlines():
            done.add(key(json.loads(ln)))
    grid = product((1500, 3000), (3, 10, 30), (6.0, 12.0), (188, 189, 190))
    for n, H, t_b, seed in grid:
        d = {"n": n, "H": H, "t_b": t_b, "seed": seed}
        if key(d) in done:
            continue
        rng = np.random.default_rng(seed)
        worlds = [M.world(n, 300, H, rng, t_b=t_b) for _ in range(12)]
        for g in (0.0, 1.0):
            r = M.likelihoods(worlds, 0.01, g)
            d[f"g{int(g)}"] = {k: round(r[k], 3) for k in
                               ("L_M0", "BF_MC_vs_M0", "BF_MH_vs_M0",
                                "BF_MC_vs_MH")}
        s_all = np.concatenate([w[0] for w in worlds])
        d["frac_reaching_10pct"] = round(float((s_all >= 0.1 * n).mean()), 3)
        with OUT.open("a") as f:
            f.write(json.dumps(d) + "\n")
        print(json.dumps(d))


if __name__ == "__main__":
    main()
