"""Prior mass of each region label under N(0, I_18), and the prior mean of L in
each region: the n = 0 anchor for the thermodynamic integration in
analyze_posterior.py. Appends one JSON line per chunk of draws (resumable).
Usage: python3 -I prior_regions.py OUT.jsonl [--chunks 20] [--size 50000]"""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import tms
import posterior as P

ap = argparse.ArgumentParser()
ap.add_argument("out"); ap.add_argument("--chunks", type=int, default=20)
ap.add_argument("--size", type=int, default=50000)
a = ap.parse_args()
done = sum(1 for _ in open(a.out)) if os.path.exists(a.out) else 0
for ch in range(done, a.chunks):
    rng = np.random.default_rng([23, ch])
    th = rng.normal(size=(a.size, 18))
    lab = P.labels_of(th)
    _, _, L = P.U_and_grad(th, np.zeros(a.size))
    rec = {"chunk": ch, "size": a.size, "count": {}, "sumL": {}}
    for u in np.unique(lab):
        m = lab == u
        key = P.code_to_label(int(u))
        rec["count"][key] = int(m.sum()); rec["sumL"][key] = float(L[m].sum())
    with open(a.out, "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(ch, flush=True)
