"""Theorem C's hypothesis in part 2, computed correctly.

study.py's part-2 field `condC` tests only positive definiteness and n > 0
at the frozen -i community. It omits the requirement that the free trait
coordinates be stationary there, so it is not Theorem C's hypothesis. This
script reruns each part-2 growth phase, which is deterministic, and records
for each removal the norm of the gradient on the free coordinates at the
frozen -i community, and whether the full hypothesis holds.
Append-only and resumable: results/condC_check.jsonl.
Run: python3 -I condC_check.py
"""
import json
import os
import sys
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np

import model as M
from study import DT, EPS, OUT


def one(args):
    k, w, seed = args
    nic = M.GaussianNiche(m=12, w=w)
    b = np.ones(12)
    rng = np.random.default_rng(1000 * k + seed + int(100 * w))  # as in study.part2_one
    c = np.full(k, 0.2)
    n, th = M.simulate(nic, b, c, np.full(k, 0.3), 0.5 + 1e-3 * rng.normal(size=k), EPS, T=400, dt=DT)
    alive = n > 1e-6
    n, th, c = n[alive], th[alive], c[alive]
    U = nic.u(th)
    A, r = U.T @ U, U.T @ b - c
    out = []
    for i in range(len(n)):
        _, _, _, nt = M.invasion_frozen(A, r, n, i)
        keep = np.ones(len(n), bool); keep[i] = False
        nk, tk, ck = nt[keep], th[keep], c[keep]
        present = nk > 1e-12
        g = np.concatenate(M.grad(nic, b, ck[present], nk[present], tk[present]))
        free = M.free_coordinates(nic, b, nk[present], tk[present])
        gnorm = float(np.linalg.norm(g[free]))
        chk = M.theorem_A_check(nic, b, ck[present], nk[present], tk[present], EPS)
        out.append(dict(i=i, free_grad_norm=gnorm, secondary=bool((~present).any()),
                        hypothesis_C=bool(chk["holds"] and gnorm < 1e-8 and present.all())))
    return dict(k=k, w=w, seed=seed, removals=out)


if __name__ == "__main__":
    jobs = [(k, w, s) for k in (2, 3, 4, 5, 6) for w in (0.08, 0.12, 0.2) for s in range(3)]
    path = os.path.join(OUT, "condC_check.jsonl")
    done = set()
    if os.path.exists(path):
        for line in open(path):
            if line.strip():
                rec = json.loads(line)
                done.add((rec["k"], rec["w"], rec["seed"]))
    todo = [j for j in jobs if j not in done]
    with Pool(4) as p, open(path, "a") as fh:
        for rec in p.imap_unordered(one, todo):
            fh.write(json.dumps(rec) + "\n")
            fh.flush()
            print("condC", rec["k"], rec["w"], rec["seed"],
                  [x["hypothesis_C"] for x in rec["removals"]], flush=True)
