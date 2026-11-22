"""Run the candidate factorial under each parameter variant; append one JSON
line per (variant, configuration) to results.jsonl and skip lines already
written, so the run resumes.

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run.py
"""

import itertools
import json
import os
import sys
from dataclasses import replace

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from loop import CANDIDATES, Config, Params, simulate  # noqa: E402

OUT = os.path.join(HERE, "results.jsonl")
SEEDS, STEPS, BLOCK = 20, 3000, 300

# one-at-a-time variants around the default
VARIANTS = [("default", {})] + [
    (f"{k}={v}", {k: v}) for k, vs in [
        ("eta", [0.3, 1.0]),
        ("zeta", [0.5]),
        ("kappa1", [0.0, 0.5]),
        ("kappa2", [0.4, 1.2]),
        ("kbar", [0.0, 0.2, 0.8]),
        ("theta", [2.0, 3.0]),
        ("phi", [0.25, 1.0]),
        ("q5", [0.02, 0.2]),
        ("eta_tau", [0.2]),
        ("sigma1", [2.0]),
    ] for v in vs
]


def configs():
    for bits in itertools.product([False, True], repeat=len(CANDIDATES)):
        d = dict(zip(CANDIDATES, bits))
        if d["capture"] and not d["sense"]:
            continue
        yield Config(**d)
    # the other reading of "no commitment": revise after the evidence
    for bits in itertools.product([False, True], repeat=len(CANDIDATES)):
        d = dict(zip(CANDIDATES, bits))
        if d["commit"] or (d["capture"] and not d["sense"]):
            continue
        yield Config(**d, no_commit_mode="posthoc")


def key(variant, cfg):
    return f"{variant}|{cfg.label()}|{cfg.no_commit_mode if not cfg.commit else 'commit'}"


def main():
    done = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            done = {json.loads(line)["key"] for line in f if line.strip()}
    with open(OUT, "a") as f:
        for vname, over in VARIANTS:
            p = replace(Params(), **over)
            for cfg in configs():
                k = key(vname, cfg)
                if k in done:
                    continue
                rs = [simulate(cfg, p, STEPS, BLOCK, s) for s in range(SEEDS)]
                li = [r["lockin"] for r in rs]
                rec = {
                    "key": k, "variant": vname, "config": cfg.label(),
                    "no_commit_mode": cfg.no_commit_mode if not cfg.commit else None,
                    **{c: getattr(cfg, c) for c in CANDIDATES},
                    "lockin_mean": float(np.nanmean(li)) if not all(np.isnan(li)) else None,
                    "lockin_seeds": [None if np.isnan(x) else x for x in li],
                    "first_block_tracked": float(np.mean([r["first_block_tracked"] for r in rs])),
                    "captures_mean": float(np.mean([r["captures"] for r in rs])),
                    "override": over, "seeds": SEEDS, "steps": STEPS, "block": BLOCK,
                }
                f.write(json.dumps(rec) + "\n")
                f.flush()


if __name__ == "__main__":
    main()
