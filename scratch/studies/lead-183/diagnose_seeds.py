"""Post hoc (not pre-registered): per candidate seed, its mean effect when added
to the evaluated sets, against simple architecture features of the seed.
Run: python3 -I diagnose_seeds.py   (writes diagnosis.json)"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nucleus_predictor as npred  # noqa: E402

import numpy as np  # noqa: E402


def main():
    recs = {}
    with open(os.path.join(HERE, "results.jsonl")) as f:
        for line in f:
            r = json.loads(line)
            recs.setdefault((r["arch"], r["p_rigid"]), []).append(r)
    rows = []
    for (s, pr), rs in sorted(recs.items()):
        arch = npred.lattice_architecture(8, 4, pr, 2, random.Random(s))
        pairs = npred.addition_pairs(rs, 300)
        added = {}
        for x in pairs:
            c = (set(x["Sc"]) - set(x["S"])).pop()
            added.setdefault(c, []).append(x["dV"])
        for c, dvs in added.items():
            strong = sum(arch.strength[(c, w)] == 2 for w in arch.nbrs[c])
            rows.append({"arch": s, "p_rigid": pr, "seed": c, "mean_dV": round(float(np.mean(dvs)), 4),
                         "island": len(npred.island(arch, [c])), "degree": len(arch.nbrs[c]),
                         "strong_edges": strong})
    with open(os.path.join(HERE, "diagnosis.json"), "w") as f:
        json.dump(rows, f, indent=0)
    harm = [r for r in rows if r["mean_dV"] < -0.02]
    rest = [r for r in rows if r["mean_dV"] >= -0.02]
    for name, grp in [("harmful (mean dV < -0.02)", harm), ("others", rest)]:
        print(name, len(grp), "island==1:", sum(r["island"] == 1 for r in grp),
              "no strong edge:", sum(r["strong_edges"] == 0 for r in grp),
              "mean island:", round(float(np.mean([r["island"] for r in grp])), 1) if grp else None)
    for r in harm:
        print(r)


if __name__ == "__main__":
    main()
