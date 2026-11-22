"""LEAD-063 run: sweep the coupling between parts, for the modular mind
(inter-module coupling c) and for the group (inter-member coupling g, with
each member a unified modular mind), and record Phi at every level and the
exclusion verdict. Appends one JSON line per item to results.jsonl and
skips items already there.

    python3 -I run.py            # from this directory
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from phi import (analyse, exclusion_winner, group, group_levels,  # noqa: E402
                 mind_levels, modular_mind)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results.jsonl")

# Fixed parameters. Modules: 3 units, within-module weight W.
W = 0.12
MIND_C, MIND_WIDTH = 0.15, 3   # the members' own inter-module coupling
COUPLINGS = [round(x, 2) for x in np.arange(0.0, 0.251, 0.01)]
WIDTHS = [1, 2, 3]
NORMS = [True, False]


def done_keys():
    keys = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            for line in f:
                r = json.loads(line)
                keys.add((r["model"], r["coupling"], r["width"], r["normalize"]))
    return keys


def main():
    done = done_keys()
    with open(OUT, "a") as f:
        for norm in NORMS:
            for model in ["mind", "group"]:
                for width in WIDTHS:
                    for x in COUPLINGS:
                        key = (model, x, width, norm)
                        if key in done:
                            continue
                        rec = {"model": model, "coupling": x, "width": width,
                               "normalize": norm, "w": W}
                        try:
                            if model == "mind":
                                A, mods = modular_mind(w=W, c=x, width=width)
                                r = analyse(A, mind_levels(A, mods), norm)
                            else:
                                A, mem, mods = group(w=W, c=MIND_C, width_c=MIND_WIDTH,
                                                     g=x, width_g=width)
                                r = analyse(A, group_levels(mem, mods), norm)
                                rec.update(member_c=MIND_C, member_width=MIND_WIDTH)
                            rec["rho"] = float(np.max(np.abs(np.linalg.eigvals(A))))
                            rec["phi"] = {k: float(max(v)) for k, v in r.items()}
                            rec["winner"] = exclusion_winner(r)
                        except ValueError as e:
                            rec["error"] = str(e)
                        f.write(json.dumps(rec) + "\n")
                        f.flush()
                        print(json.dumps(rec), flush=True)


if __name__ == "__main__":
    main()
