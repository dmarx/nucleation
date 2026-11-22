"""Check the level-restricted verdict for the modular mind against an
exhaustive search over all 502 subsets of >= 2 units (the full exclusion
rule), for couplings up to the within-module weight. Appends to
complex_check.jsonl, skipping items already there.

    python3 -I check_mind.py
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from phi import analyse, exclusion_winner, main_complex, mind_levels, modular_mind  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "complex_check.jsonl")
W = 0.12

done = set()
if os.path.exists(OUT):
    for l in open(OUT):
        r = json.loads(l)
        done.add((r["coupling"], r["width"]))

with open(OUT, "a") as f:
    for width in [1, 2, 3]:
        for x in [round(v, 2) for v in np.arange(0.0, W + 0.001, 0.01)]:
            if (x, width) in done:
                continue
            A, mods = modular_mind(w=W, c=x, width=width)
            lvl = exclusion_winner(analyse(A, mind_levels(A, mods)))
            val, sub = main_complex(A)
            kind = ("mind" if len(sub) == 9 else
                    "module" if sub in mods else "other")
            rec = {"coupling": x, "width": width, "level_verdict": lvl,
                   "main_complex": sub, "main_complex_kind": kind,
                   "phi": val, "agree": kind == lvl}
            f.write(json.dumps(rec) + "\n")
            f.flush()
            print(json.dumps(rec), flush=True)
