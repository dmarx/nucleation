"""Print the tables the CASE quotes, from results.jsonl."""
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R = {}
for line in open(os.path.join(HERE, "results.jsonl")):
    d = json.loads(line)
    R[d["key"]] = d["result"]

print("== A: spectrum")
for h in (1.0, 0.5, 0.25):
    r = R.get(f"A-spectrum|{h}|None")
    if r:
        print(h, [round(e, 3) for e in r["eig"]], "zero-mode length", round(r["zero_mode_participation_length"], 2))

print("== A: block test, max rho by segment length (containing kink / far vacuum)")
for h in (1.0, 0.5, 0.25):
    r = R.get(f"A-blocktest|{h}|None")
    if r:
        print(h, "eps", r["eps"], {L: (round(v["max_rho_containing_kink"], 3), round(v["max_rho_far_vacuum"], 3), v["entrywise"]) for L, v in r["by_length"].items()})

print("== A: compensation kappa by distance from the kink centre (mean of the two load signs)")
for h in (1.0, 0.5, 0.25):
    for X0 in (0.0, 6.0):
        r = R.get(f"A-compensation|{h}|{X0}")
        if not r:
            continue
        rows = r["rows"]
        Xc = r["X_fit"]
        for T in ("T5", "T50"):
            sites = sorted(set(x["site"] for x in rows))
            km = {s: np.mean([x[T]["kappa"] for x in rows if x["site"] == s]) for s in sites}
            Xs = {s: np.mean([abs(x[T]["X_shift"]) for x in rows if x["site"] == s]) for s in sites}
            comp = [s for s in sites if km[s] > 0.5]
            print(f"h={h} X0={X0} {T} centre {Xc:.2f}; kappa>0.5 on [{min(comp) if comp else None}, {max(comp) if comp else None}] ({len(comp)} sites)")
            print("   ", [(round(s - Xc, 2), round(float(km[s]), 2), round(float(Xs[s]), 2)) for s in sites])

print("== B, C: oscillators")
for arm in ("B", "C"):
    for k in ("baseline", "blocktest", "entrain|form", "entrain|outside", "compensate|form", "compensate|outside"):
        key = f"{arm}|{k}" if "|" in k else f"{arm}|{k}|None"
        r = R.get(key)
        if r is not None:
            print(arm, k, json.dumps(r, default=float)[:700])
