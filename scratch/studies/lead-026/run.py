"""LEAD-026: run CASE-101's populations through QUESTION-115's search and
the lagged block criterion. Appends one JSON line per (arm, item) to
results.jsonl and skips items already written; summarise.py writes
summary.txt from it.

Items per arm (A, B, C, C0):
  stats        the matched aggregate statistics, and lagged ones not matched;
  block:<obs>:W the priced lagged block test on every one of the 255
               subsets (127 with e hidden) at window W; <obs> is "all"
               (e observed) or "hidden" (e dropped from the observed set);
  profile      for each symmetry class of candidate (k members, e in or
               out, z in or out): A*, A, nC at lags 1..64 (E the rest, with
               and without e), and transfer entropy into the candidate
               (history 1 and 16);
  ahat         Bourrat's Ahat(D) by intervention in the simulator.
"""
import copy
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import measures as M  # noqa: E402
from model import E_IDX, N, NAMES, NV, Z_IDX, Sim, aggregate_stats  # noqa: E402

OUT = os.path.join(HERE, "results.jsonl")
ARMS = ["A", "B", "C", "C0"]
SEEDS = dict(A=101, B=102, C=103, C0=104)
R_OBS, T_OBS, BURN = 100, 2500, 800
P_EMB = 16
WINDOWS = [1, 2, 4, 6, 7, 8, 10, 12, 16]
LAGS = [1, 2, 4, 8, 16, 32, 64]
R_INT, BURN_INT = 20000, 600


def done_items():
    seen = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            for line in f:
                d = json.loads(line)
                seen.add((d["arm"], d["item"]))
    return seen


def emit(rec):
    with open(OUT, "a") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())
    print(rec["arm"], rec["item"], "written", flush=True)


def classes():
    """Symmetry classes of candidate: (k members, e?, z?), nonempty."""
    out = []
    for k in range(N + 1):
        for e in (0, 1):
            for z in (0, 1):
                S = list(range(k)) + ([E_IDX] if e else []) + ([Z_IDX] if z else [])
                if S:
                    out.append(dict(label=f"{k}m{'+e' if e else ''}{'+z' if z else ''}", S=S))
    return out


def ahat_rows(base, cands, rng, lags, seed):
    """Ahat(D) = I(S_{t+D}; S^_t) for each candidate: do(S) on a copy of the
    burned-in simulator, with values drawn from S's population marginal
    (rng, a generator separate from the simulator's), then D steps."""
    Cpop = np.cov(base.x.T)
    rows = []
    for c in cands:
        S = c["S"]
        sim = copy.deepcopy(base)
        sim.rng = np.random.default_rng([seed, 3000, len(rows)])
        vals = rng.multivariate_normal(np.zeros(len(S)), Cpop[np.ix_(S, S)], size=base.R)
        sim.intervene(S, vals)
        ah = {}
        for D in range(1, max(lags) + 1):
            sim.step()
            if D in lags:
                ah[D] = M.gaussian_mi_samples(sim.x[:, S], vals)
        rows.append(dict(label=c["label"], S=S, ahat=ah))
    return rows


def name(S):
    return "{" + ",".join(NAMES[v] for v in S) + "}"


def main():
    with open(os.path.join(HERE, "calibration.json")) as f:
        cal = json.load(f)
    seen = done_items()
    for arm in ARMS:
        par = {k: cal[arm][k] for k in ("a", "gain", "s")}
        need_obs = any((arm, it) not in seen for it in
                       ["stats", "profile"] + [f"block:{o}:{W}" for o in ("all", "hidden") for W in WINDOWS])
        if need_obs:
            t0 = time.time()
            sim = Sim(arm, par, R_OBS, np.random.default_rng(SEEDS[arm]))
            traj = sim.run(T_OBS, BURN)
            Cemb, n = M.embed_cov(traj, P_EMB)
            print(arm, "simulated and embedded", round(time.time() - t0, 1), "s", flush=True)
        if (arm, "stats") not in seen:
            emit(dict(arm=arm, item="stats", params=par, n_rows=n, **aggregate_stats(traj)))
        for obs in ("all", "hidden"):
            V = list(range(NV)) if obs == "all" else [v for v in range(NV) if v != E_IDX]
            for W in WINDOWS:
                item = f"block:{obs}:{W}"
                if (arm, item) in seen:
                    continue
                rows = []
                for S in M.subsets(V):
                    sc = M.block_scores(Cemb, n, NV, W, S, V)
                    rows.append(dict(S=S, **sc))
                passing = [name(r["S"]) for r in rows if r["passes"]]
                key = {name(r["S"]): {k: r[k] for k in ("internal", "edge", "edge_in", "edge_out")}
                       for r in rows if r["S"] in (list(range(N)), list(range(N)) + [E_IDX],
                                                   list(range(N)) + [E_IDX, Z_IDX], [E_IDX], [0],
                                                   list(range(N)) + [Z_IDX])}
                emit(dict(arm=arm, item=item, W=W, observed=obs, n_rows=n,
                          occam_per_coef=float(np.log(n)), passing=passing, key=key))
        if (arm, "profile") not in seen:
            prof = []
            pairs = {D: M.lag_pair_cov(traj, D) for D in LAGS}
            for c in classes():
                S = c["S"]
                rest = [v for v in range(NV) if v not in S]
                rest_h = [v for v in rest if v != E_IDX]
                kr = {D: M.krakauer(pairs[D], S, rest) for D in LAGS}
                krh = {D: M.krakauer(pairs[D], S, rest_h) for D in LAGS}
                te = {p: M.transfer_into(Cemb, NV, S, rest, p) for p in (1, 16)}
                te_h = {p: M.transfer_into(Cemb, NV, S, rest_h, p) for p in (1, 16)}
                prof.append(dict(label=c["label"], S=S, krakauer=kr, krakauer_e_hidden=krh,
                                 te=te, te_e_hidden=te_h))
            emit(dict(arm=arm, item="profile", lags=LAGS, rows=prof))
        if (arm, "ahat") not in seen:
            t0 = time.time()
            # the simulator's noise and the intervention values come from
            # separate generators: a deep copy of the simulator copies its
            # generator, so drawing the values from that same stream would
            # correlate them with the next step's noise
            base = Sim(arm, par, R_INT, np.random.default_rng(SEEDS[arm] + 1000))
            rng = np.random.default_rng(SEEDS[arm] + 2000)
            for _ in range(BURN_INT):
                base.step()
            rows = ahat_rows(base, classes(), rng, LAGS, SEEDS[arm])
            emit(dict(arm=arm, item="ahat", R=R_INT, lags=LAGS, rows=rows,
                      seconds=round(time.time() - t0, 1)))


if __name__ == "__main__":
    main()
