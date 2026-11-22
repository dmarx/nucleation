"""Run the study item by item, appending one JSON line per network to
results.jsonl and skipping items already written. Usage:
    OPENBLAS_NUM_THREADS=1 python3 -I run.py [--smoke]
(run from this directory; -I is safe because the modules are found via sys.path below)."""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np  # noqa: E402

import experiments as E  # noqa: E402

SPECS = (
    [{"id": f"trained-d4-s{s}", "kind": "trained", "d": 4, "seed": s} for s in range(4)]
    + [{"id": f"trained-d8-s{s}", "kind": "trained", "d": 8, "seed": s} for s in range(2)]
    + [{"id": f"frozen-d4-scale{sc}-s{s}", "kind": "frozen", "d": 4, "seed": s, "scale": sc}
       for sc in (0.5, 1.5) for s in range(2)]
)


def main():
    smoke = "--smoke" in sys.argv
    out = os.path.join(HERE, "results_smoke.jsonl" if smoke else "results.jsonl")
    done = set()
    if os.path.exists(out):
        with open(out) as f:
            done = {json.loads(line)["id"] for line in f if line.strip()}
    specs = SPECS[:1] if smoke else SPECS
    os.makedirs(os.path.join(HERE, "params"), exist_ok=True)
    for spec in specs:
        if spec["id"] in done:
            print("skip", spec["id"], flush=True)
            continue
        if smoke:
            spec = dict(spec, steps=200)
        t = time.time()
        res, P = E.run_item(spec, n_eval=300 if smoke else 1000, n_flip=100 if smoke else 300,
                            log=lambda s: print(s, flush=True))
        res["seconds"] = round(time.time() - t, 1)
        with open(out, "a") as f:
            f.write(json.dumps(res) + "\n")
        if not smoke:
            np.savez(os.path.join(HERE, "params", spec["id"] + ".npz"), **P)
        print("done", spec["id"], res["seconds"], "s", flush=True)


if __name__ == "__main__":
    main()
