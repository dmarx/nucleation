"""Drop the per-pair records from results/E1.jsonl (analyse.pairs_of recomputes
them exactly from the stored rates, bounds and times; checked: 0 mismatches of
43,740) so the committed file stays under about 1 MB. Run once after run.py.

    python3 -I compact.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, "results", "E1.jsonl")
with open(p) as f:
    rows = [json.loads(x) for x in f if x.strip()]
for r in rows:
    r.pop("pairs", None)
with open(p, "w") as f:
    for r in rows:
        f.write(json.dumps(r, separators=(",", ":")) + "\n")
