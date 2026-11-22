"""Would a fixed weighting rule, chosen in hindsight per instance, do what
Regime B does? For the first N_H satisfiable instances of sweep.py, run every
fixed w on a simplex grid of step 1/10 and keep the best. Writes
results/fixed_hindsight.json."""
import json
import sys
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import numpy as np
import model as M
from sweep import setup, BASE, T

N_H = 60


def job(seed):
    dem, theta0, w0, _ = setup(seed, True, 1.0)
    best = (2.0, None)
    for w in M.simplex_grid(3, 10):
        _, s = M.run(dem, theta0, w, "fixed", T=T, r=BASE["r"])
        if s["gov_frustration"] < best[0]:
            best = (s["gov_frustration"], w.tolist())
    _, sB = M.run(dem, theta0, w0, "B", T=T, r=BASE["r"], gamma=BASE["gamma"],
                  delta=BASE["delta"])
    _, sA = M.run(dem, theta0, w0, "A", T=T, r=BASE["r"], gamma=BASE["gamma"],
                  delta=BASE["delta"])
    return {"seed": seed, "best_fixed": best[0], "best_w": best[1],
            "B": sB["gov_frustration"], "A": sA["gov_frustration"]}


if __name__ == "__main__":
    with Pool(4) as p:
        rows = p.map(job, range(N_H))
    bf = np.array([r["best_fixed"] for r in rows]); B = np.array([r["B"] for r in rows])
    A = np.array([r["A"] for r in rows])
    out = {"n": N_H, "grid": "1/10 (66 weightings)",
           "best_fixed_mean": float(bf.mean()), "B_mean": float(B.mean()), "A_mean": float(A.mean()),
           "best_fixed_le_B": int((bf <= B + 1e-12).sum()),
           "best_fixed_zero": int((bf == 0).sum()), "B_zero": int((B == 0).sum()),
           "rows": rows}
    (HERE / "results" / "fixed_hindsight.json").write_text(json.dumps(out, indent=1))
    print({k: v for k, v in out.items() if k != "rows"})
