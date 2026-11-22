"""Exhaustive exclusion on a small group, so that no candidate set is
assumed: 2 members, each a mind of 2 modules x 3 units (12 units in all).
For each inter-member coupling g and link width, find the subset of maximal
Phi over all 4083 subsets, and classify it: the whole group, one member,
one module, a set inside one member, or a set crossing members. The same
search on the lone small mind is recorded first. Appends to
small_group.jsonl, skipping items already there.

    python3 -I check_small_group.py
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from phi import group, main_complex, modular_mind  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "small_group.jsonl")
W, C, WC = 0.12, 0.15, 3  # each member: 2 modules of 3, linked by 3 pairs of 0.15

done = set()
if os.path.exists(OUT):
    for l in open(OUT):
        r = json.loads(l)
        done.add((r["model"], r["coupling"], r["width"]))


def classify(sub, members, modules):
    s = set(sub)
    if len(sub) == sum(len(m) for m in members):
        return "whole"
    if any(s == set(m) for m in members):
        return "member"
    if any(s == set(m) for m in modules):
        return "module"
    if any(s <= set(m) for m in members):
        return "inside-one-member"
    return "crosses-members"


with open(OUT, "a") as f:
    if ("mind", C, WC) not in done:
        A, mods = modular_mind(m=2, n=3, w=W, c=C, width=WC)
        val, sub = main_complex(A)
        rec = {"model": "mind", "coupling": C, "width": WC, "phi": val,
               "main_complex": sub,
               "kind": "whole" if len(sub) == 6 else
                       ("module" if sub in mods else "other")}
        f.write(json.dumps(rec) + "\n"); f.flush(); print(json.dumps(rec), flush=True)
    for width in [1, 3, 6]:
        for g in [0.0, 0.05, 0.1, 0.15]:
            if ("group", g, width) in done:
                continue
            A, members, modules = group(k=2, m=2, n=3, w=W, c=C, width_c=WC,
                                        g=g, width_g=width)
            try:
                val, sub = main_complex(A)
            except ValueError as e:
                rec = {"model": "group", "coupling": g, "width": width, "error": str(e)}
            else:
                rec = {"model": "group", "coupling": g, "width": width, "phi": val,
                       "main_complex": sub, "kind": classify(sub, members, modules)}
            f.write(json.dumps(rec) + "\n"); f.flush(); print(json.dumps(rec), flush=True)
