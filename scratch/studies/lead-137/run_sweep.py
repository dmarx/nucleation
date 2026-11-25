"""Run the LEAD-137 sweep, writing one JSON line per item (append-only,
resumable: items already in results.jsonl are skipped). Deterministic.

Usage: python3 -I run_sweep.py
"""
import json
import os
import sys
import itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import study as S

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.jsonl")

GRID = dict(
    mode=["symmetric", "asymmetric"],
    rho=[0.5, 0.8, 0.95],
    w_cross=[0.1, 0.5],              # 0.1 strongly modular, 0.5 weakly modular
    buffer_width=[1, 2],
    homogeneous_border=[False, True],  # generic graph vs lattice-like slab edge
    seed=list(range(20)),
)
FIXED = dict(K=4, n=8, p_in=0.5, w_in=1.0)


def item_key(cfg):
    return (cfg["mode"], cfg["rho"], cfg["w_cross"], cfg["buffer_width"],
            cfg["homogeneous_border"], cfg["seed"])


def load_done(path):
    done = set()
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                d = json.loads(line)
                done.add((d["mode"], d["rho"], d["w_cross"], d["buffer_width"],
                          d["homogeneous_border"], d["seed"]))
    return done


def main():
    keys = list(GRID.keys())
    done = load_done(OUT)
    n_new = 0
    with open(OUT, "a") as f:
        for combo in itertools.product(*(GRID[k] for k in keys)):
            cfg = dict(FIXED)
            cfg.update(dict(zip(keys, combo)))
            if item_key(cfg) in done:
                continue
            out = S.run_item(cfg)
            f.write(json.dumps(out) + "\n")
            f.flush()
            n_new += 1
    total = len(done) + n_new
    print(f"wrote {n_new} new items, {total} total -> {OUT}")


if __name__ == "__main__":
    main()
