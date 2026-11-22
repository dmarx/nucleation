"""Matched comparison restricted to claims whose first inbound edge came >= 1 day
after filing (so the filing-day burst is out of both arms); bootstrap 300."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import analyze as A

def run(cs, ev):
    keep = [c for c in cs if A.first_edge[c] is not None and A.first_edge[c] - A.t0[c] >= A.DAY]
    return A.matched(keep, ev)

for m in ("strict", "title", "status"):
    ev = A.EV[m]
    pt = run(A.claims, ev)
    bs = [run(list(A.rng.choice(A.claims, size=len(A.claims))), ev)["ratio"] for _ in range(300)]
    print(m, {k: round(v, 3) if isinstance(v, float) else v for k, v in pt.items()},
          "95%", np.round(np.nanpercentile(bs, [2.5, 97.5]), 2))
