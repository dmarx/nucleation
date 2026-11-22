"""Run the laboratory: worlds x arms x seeds, one JSON line per run,
appended as each finishes; reruns skip runs already written.

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run.py results.jsonl WORLD SEED [SEED ...]
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lab  # noqa: E402


def main():
    out, world, seeds = sys.argv[1], sys.argv[2], [int(s) for s in sys.argv[3:]]
    done = set()
    if os.path.exists(out):
        for line in open(out):
            r = json.loads(line)
            done.add((r["world"], r["arm"], r["seed"]))
    for seed in seeds:
        for arm in lab.ARMS:
            if (world, arm, seed) in done:
                continue
            t = time.time()
            rec = lab.run(world, arm, seed)
            rec["seconds"] = round(time.time() - t, 1)
            with open(out, "a") as f:
                f.write(json.dumps(rec) + "\n")
            print(world, arm, seed, rec["seconds"], flush=True)


if __name__ == "__main__":
    main()
