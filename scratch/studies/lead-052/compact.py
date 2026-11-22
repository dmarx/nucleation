"""Round the floats in results/runs.jsonl to five significant figures, so
the committed file stays under about 1 MB. Run once, after run_all.py."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "results", "runs.jsonl")


def rnd(x):
    if isinstance(x, float):
        return float(f"{x:.5g}") if x == x and abs(x) != float("inf") else x
    if isinstance(x, list):
        return [rnd(v) for v in x]
    if isinstance(x, dict):
        return {k: (v if k == "key" else rnd(v)) for k, v in x.items()}
    return x


recs = [json.loads(line) for line in open(PATH)]
for r in recs:
    r.pop("seconds", None)
with open(PATH + ".tmp", "w") as f:
    for r in recs:
        f.write(json.dumps(rnd(r), separators=(",", ":")) + "\n")
os.replace(PATH + ".tmp", PATH)
print(len(recs), os.path.getsize(PATH))
