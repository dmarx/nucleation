"""LEAD-089 study: price the will-organization against control-only models.

For each world, training size and seed: draw a true table, sample training
episodes under the four training arrangements, fit every model, and score
(i) log evidence on the training data, (ii) log predictive per episode on
fresh episodes under the training arrangements, and (iii) the same under the
four unseen combined arrangements. One JSON line per item, appended; a rerun
skips items already written.

    python3 -I study.py            # all items, models WO and C0-C3
    python3 -I study.py c4         # the same data, gate C4 only (runs_c4.jsonl)
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results", "runs.jsonl")
WORLDS = ["governed", "idle", "idiosyncratic", "interacting"]
NS = [30, 100, 300, 1000]
SEEDS = range(20)
N_TEST = 2000
OUT_C4 = os.path.join(HERE, "results", "runs_c4.jsonl")
PHI = {k: M.features(k)[0] for k in ("C2", "C3", "C4")}


def done_keys(path=OUT):
    if not os.path.exists(path):
        return set()
    with open(path) as fh:
        return {(r["world"], r["n"], r["seed"]) for r in map(json.loads, fh)}


def run_item(world, n_per, seed):
    rng = np.random.default_rng([89, WORLDS.index(world), n_per, seed])
    P, meta = M.world_table(world, rng)
    n = M.sample_counts(P, M.TRAIN_A, n_per, rng)
    t_seen = M.sample_counts(P, M.TRAIN_A, N_TEST, rng)
    t_new = M.sample_counts(P, M.TEST_A, N_TEST, rng)
    out = {"world": world, "n": n_per, "seed": seed, **meta, "models": {}}
    fits = {"WO": M.wo_posterior(n), "C0": M.c0(n), "C1": M.c1(n)}
    for k in ("C2", "C3"):
        le, pred, _ = M.gate_fit(n, PHI[k], rng=np.random.default_rng(seed))
        fits[k] = (le, pred)
    # the truth, as a ceiling for predictive scores
    for name, (le, pred) in fits.items():
        out["models"][name] = {
            "log_evidence": le,
            "lp_seen": M.log_pred(t_seen, pred) / t_seen.sum(),
            "lp_new": M.log_pred(t_new, pred) / t_new.sum(),
        }
    out["truth"] = {"lp_seen": M.log_pred(t_seen, P) / t_seen.sum(),
                    "lp_new": M.log_pred(t_new, P) / t_new.sum()}
    return out


def run_item_c4(world, n_per, seed):
    """Regenerates run_item's data with the same draws and fits C4 alone."""
    rng = np.random.default_rng([89, WORLDS.index(world), n_per, seed])
    P, meta = M.world_table(world, rng)
    n = M.sample_counts(P, M.TRAIN_A, n_per, rng)
    t_seen = M.sample_counts(P, M.TRAIN_A, N_TEST, rng)
    t_new = M.sample_counts(P, M.TEST_A, N_TEST, rng)
    le, pred, _ = M.gate_fit(n, PHI["C4"], rng=np.random.default_rng(seed))
    return {"world": world, "n": n_per, "seed": seed, "models": {"C4": {
        "log_evidence": le,
        "lp_seen": M.log_pred(t_seen, pred) / t_seen.sum(),
        "lp_new": M.log_pred(t_new, pred) / t_new.sum()}},
        "truth": {"lp_seen": M.log_pred(t_seen, P) / t_seen.sum(),
                  "lp_new": M.log_pred(t_new, P) / t_new.sum()}}


def main():
    c4 = len(sys.argv) > 1 and sys.argv[1] == "c4"
    out, fn = (OUT_C4, run_item_c4) if c4 else (OUT, run_item)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    have = done_keys(out)
    for world in WORLDS:
        for n_per in NS:
            for seed in SEEDS:
                if (world, n_per, seed) in have:
                    continue
                t0 = time.time()
                rec = fn(world, n_per, seed)
                rec["seconds"] = round(time.time() - t0, 2)
                with open(out, "a") as fh:
                    fh.write(json.dumps(rec) + "\n")
                print(world, n_per, seed, rec["seconds"], flush=True)


if __name__ == "__main__":
    main()
