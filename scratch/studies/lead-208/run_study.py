"""LEAD-208 study driver. Appends one JSON line per item to results/*.jsonl and
skips items already written, so an interrupted run resumes.

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run_study.py [mc|strip|burn|all]
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from clusters import box_counts, largest_cluster_masks  # noqa: E402
from fisher import level_estimates, spectrum_with_errors  # noqa: E402
from ising import K_C, PARAM_NAMES, random_spins, swendsen_wang  # noqa: E402
from strip import column_mi, row_ipred  # noqa: E402

RES = os.path.join(HERE, "results")
os.makedirs(RES, exist_ok=True)

# T / T_c -> K = K_c / (T / T_c)
TEMPS = {"Tc": 1.0, "0.9Tc": 0.9, "1.1Tc": 1.1}
# (L, chains, measurements per chain); every config gets all levels
SIZES = [(16, 64, 128), (32, 64, 64), (64, 32, 48)]
THERM, GAP = 60, 2


def done_keys(path):
    if not os.path.exists(path):
        return set()
    with open(path) as f:
        return {json.loads(line)["key"] for line in f if line.strip()}


def append(path, rec):
    with open(path, "a") as f:
        f.write(json.dumps(rec) + "\n")


def kmax(L):
    return 2 * int(np.log2(L)) - 4  # last level keeps a 4 x 4 sublattice


def mc_item(L, nchain, nmeas, tname, seed, burn=3, nmeas_inner=2, levels=None):
    K = K_C / TEMPS[tname]
    rng = np.random.default_rng(seed)
    levels = list(range(kmax(L) + 1)) if levels is None else levels
    s = random_spins(rng, nchain, L)
    for _ in range(THERM):
        swendsen_wang(s, K, rng)
    A = {k: [] for k in levels}
    Bq = {k: [] for k in levels}
    eps = [e for e in (1, 2, 4, 8, 16, 32) if e <= L // 2]
    logN, mass = [], []
    for t in range(nmeas):
        for _ in range(GAP):
            swendsen_wang(s, K, rng)
        est = level_estimates(s, K, levels, rng, burn=burn, nmeas=nmeas_inner)
        for k in levels:
            A[k].append(est[k][0])
            Bq[k].append(est[k][1])
        lc = largest_cluster_masks(s)
        logN.append(np.log(box_counts(lc, eps)))
        mass.append(lc.sum(axis=(1, 2)))
    out = {"levels": {}}
    for k in levels:
        # rows chain-major so jackknife blocks are whole chains
        a = np.stack(A[k], axis=1).reshape(-1, A[k][0].shape[1])
        b = np.stack(Bq[k], axis=1).reshape(-1, A[k][0].shape[1])
        lam, err, _ = spectrum_with_errors(a, b)
        C = 0.5 * (a - a.mean(0)).T @ (b - b.mean(0)) / (len(a) - 1)
        C = C + C.T
        w, v = np.linalg.eigh(C)
        order = np.argsort(w)[::-1]
        v = v[:, order]
        out["levels"][str(k)] = {
            "lam": lam.tolist(), "err": err.tolist(),
            "vec_top3": v[:, :3].T.round(4).tolist(),
            "diag": np.diag(C).tolist(),
        }
    logN = np.stack(logN, axis=1).reshape(-1, len(eps))  # chain-major
    mass = np.stack(mass, axis=1).ravel()
    out["clusters"] = {"eps": eps, "mean_logN": logN.mean(0).tolist(),
                       "sem_logN": (logN.std(0) / np.sqrt(len(logN))).tolist(),
                       "mean_mass": float(mass.mean()),
                       "sem_mass": float(mass.std() / np.sqrt(len(mass)))}
    return out


def run_mc():
    path = os.path.join(RES, "fisher_clusters.jsonl")
    have = done_keys(path)
    seed = 208
    for L, nchain, nmeas in SIZES:
        for tname in TEMPS:
            seed += 1
            key = "L%d_%s" % (L, tname)
            if key in have:
                continue
            t0 = time.time()
            rec = mc_item(L, nchain, nmeas, tname, seed)
            rec.update({"key": key, "L": L, "T_over_Tc": TEMPS[tname],
                        "K": K_C / TEMPS[tname], "nconf": nchain * nmeas,
                        "nchain": nchain, "seed": seed, "burn": 3,
                        "nmeas_inner": 2, "params": PARAM_NAMES,
                        "seconds": round(time.time() - t0, 1)})
            append(path, rec)
            print(key, rec["seconds"], "s", flush=True)


def run_burn_check():
    """Same lattice, burn-in 1 vs 8 in the compatible chains (L = 32, T_c)."""
    path = os.path.join(RES, "burn_check.jsonl")
    have = done_keys(path)
    for burn in (1, 8):
        key = "L32_Tc_burn%d" % burn
        if key in have:
            continue
        t0 = time.time()
        rec = mc_item(32, 32, 32, "Tc", 9000, burn=burn, levels=[2, 4, 6])
        rec.pop("clusters")
        rec.update({"key": key, "burn": burn, "seconds": round(time.time() - t0, 1)})
        append(path, rec)
        print(key, rec["seconds"], "s", flush=True)


def run_strip():
    path = os.path.join(RES, "strip.jsonl")
    have = done_keys(path)
    for tname, tr in TEMPS.items():
        K = K_C / tr
        key = "colmi_%s" % tname
        if key not in have:
            Ws = list(range(2, 13))
            append(path, {"key": key, "T_over_Tc": tr, "W": Ws,
                          "I_bits": [column_mi(W, K) for W in Ws]})
            print(key, flush=True)
        for W in (4, 6, 8, 10):
            key = "row_%s_W%d" % (tname, W)
            if key in have:
                continue
            Tmax = 8 if W <= 8 else 6
            I = row_ipred(W, K, Tmax)
            append(path, {"key": key, "T_over_Tc": tr, "W": W,
                          "T": list(range(1, Tmax + 1)), "I_bits": I.tolist()})
            print(key, flush=True)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("strip", "all"):
        run_strip()
    if what in ("mc", "all"):
        run_mc()
    if what in ("burn", "all"):
        run_burn_check()
