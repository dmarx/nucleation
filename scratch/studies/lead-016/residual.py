"""QUESTION-135 check: the R specialist's residual direction at the snapshot.

d² is the squared distance of the specialist's normalized parameter vector
from the span of the other operators' normalized vectors (operators with
negligible norm are dropped). Printed beside the recovery exponent of the
rare_frozen_e3 arm. Writes results/residual.json.
"""
import json
import os
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
R = 3

rows = []
for rule in ("moe", "moe_aux", "moe_bias", "rep"):
    diff, lam = {}, {}
    with open(os.path.join(RES, f"runs_{rule}.jsonl")) as f:
        for line in f:
            r = json.loads(line)
            if r["arm"] == "diff":
                diff[(r["K"], r["seed"])] = r
            elif r["arm"] == "rare_frozen_e3":
                lam[(r["K"], r["seed"])] = r["lam_cond"]
    for key, r in sorted(diff.items()):
        th = np.array(r["theta"])
        P = np.array(r["P"])
        i = int(P[R].argmax())
        n = np.linalg.norm(th, axis=1)
        U = th / n[:, None]
        others = [j for j in range(len(th)) if j != i and n[j] > 0.3]
        Q, _ = np.linalg.qr(U[others].T)
        res = U[i] - Q @ (Q.T @ U[i])
        # nearest other operator by cosine, and its norm
        cos = [float(U[i] @ U[j]) for j in range(len(th)) if j != i]
        rows.append({"rule": rule, "K": key[0], "seed": key[1], "d2": float(res @ res),
                     "max_cos_other": max(cos), "lam_e3": lam.get(key)})

agg = defaultdict(list)
for x in rows:
    agg[(x["rule"], x["K"])].append(x)
for k, xs in agg.items():
    print(k, "d2 median", round(float(np.median([x["d2"] for x in xs])), 3),
          "max cos", round(float(np.median([x["max_cos_other"] for x in xs])), 3),
          "lam median", float(np.median([x["lam_e3"] for x in xs])))
with open(os.path.join(RES, "residual.json"), "w") as f:
    json.dump(rows, f, indent=1)
