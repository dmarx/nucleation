"""Post hoc (not pre-registered): re-estimate V for every significant decrease
found by the primary run, with fresh runs, to see whether it is real.
Run: python3 -I recheck_decreases.py   (writes recheck.json)"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nucleus_predictor as npred  # noqa: E402
RUNS = 3000


def main():
    recs = {}
    with open(os.path.join(HERE, "results.jsonl")) as f:
        for line in f:
            r = json.loads(line)
            recs.setdefault((r["arch"], r["p_rigid"]), []).append(r)
    out = []
    for (s, pr), rs in sorted(recs.items()):
        arch = npred.lattice_architecture(8, 4, pr, 2, random.Random(s))
        pairs = npred.addition_pairs(rs, 300)
        for x in pairs:
            if x["label"] != -1:
                continue
            rng = random.Random(f"{s}-{x['S']}-{x['Sc']}")
            va = npred.estimate_V(arch, list(x["S"]), 1e-4, RUNS, rng)
            vb = npred.estimate_V(arch, list(x["Sc"]), 1e-4, RUNS, rng)
            se = (va * (1 - va) / RUNS + vb * (1 - vb) / RUNS) ** 0.5
            out.append({"arch": s, "p_rigid": pr, "S": list(x["S"]), "Sc": list(x["Sc"]),
                        "dV_300": round(x["dV"], 3), "V_S": va, "V_Sc": vb,
                        "dV_3000": round(vb - va, 4), "z": round((vb - va) / se, 2) if se else None,
                        "d_vic": round(x["d_vic"], 4), "d_icn": round(x["d_icn"], 4)})
    with open(os.path.join(HERE, "recheck.json"), "w") as f:
        json.dump(out, f, indent=1)
    for o in out:
        print(o)


if __name__ == "__main__":
    main()
