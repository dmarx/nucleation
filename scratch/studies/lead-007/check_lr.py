"""Check that full fine-tuning's outcome does not depend on the step size:
rerun seeds 0-2, both tasks, c in {0.3, 2.0}, with the step-size factor
halved (0.2 against 0.4), and compare with results/runs.jsonl.

Run:  OPENBLAS_NUM_THREADS=1 python3 -I check_lr.py
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import diag_rescale as d  # noqa: E402

base = {}
for line in open(os.path.join(HERE, "results", "runs.jsonl")):
    r = json.loads(line)
    if r["mode"] == "full":
        base[(r["seed"], r["task"], r["c"])] = r["gen_err"]

out = []
for seed in (0, 1, 2):
    _, supp, _, params, _ = d.pretrain(seed)
    for kind in d.N_MAIN:
        b_main, X, y = d.main_task(np.random.default_rng(1000 + seed), supp, kind)
        for c in (0.3, 2.0):
            o, steps = d.train(X, y, *d.finetune_start(d.rescale(params, c)),
                               lr_factor=0.2, max_steps=800_000)
            g = float(np.sum((d.beta_of(*o) - b_main) ** 2))
            rec = {"seed": seed, "task": kind, "c": c, "gen_err_half_lr": g,
                   "gen_err_base": base[(seed, kind, c)], "steps": steps}
            out.append(rec)
            print(rec, flush=True)
with open(os.path.join(HERE, "results", "check_lr.json"), "w") as f:
    json.dump(out, f, indent=1)
