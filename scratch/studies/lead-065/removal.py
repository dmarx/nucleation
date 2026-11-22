"""LEAD-065: remove core units from Ito and Kaneko's network and see whether
the periphery refills the core.

Protocol (per seed):
  1. Grow the paper's system (N = 100, a = 3.97, c = 0.12, delta = 0.1) from
     its initial condition for T0 steps. Classify units by the time-averaged
     weight matrix over the last WIN steps (the paper's W^{ij}); also classify
     at T0 - 10^6 to check that membership has settled.
  2. From the same state, run five arms for T1 steps:
       control          no intervention
       remove_core      delete every core unit (rows and columns), renormalize
       remove_periph    delete as many randomly chosen periphery units
                        (controls for the smaller network)
       remove_half_core delete a random half (rounded up) of the core
       suppress_core    keep the core units but multiply every weight given
                        to them by EPS and renormalize: the core made rare in
                        influence, the recovery-from-rarity test
  3. At checkpoints, classify again from a WIN-step average and record who
     is in the core: original core units, or original periphery units.

Core criterion. Primary: unit j is core if its time-averaged total outgoing
weight W_out^j exceeds 1, the mean (each row of w sums to 1, so the mean of
W_out over units is 1 by construction). The paper's own criterion, a snapshot
out-degree #{i : w^{ij} > 1/(M-1)} above 20 (scaled to 20 (M-1)/99 for a
network of M units), is recorded alongside with the paper's Table I counts.

Usage:  python3 -I removal.py [--seeds 12] [--t0 3000000] [--t1 1000000]
        [--procs 4] [--out results]
"""

import argparse
import json
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ikmodel as m  # noqa: E402

A, C, DELTA, N = 3.97, 0.12, 0.1, 100
WIN = 50_000
EPS = 1e-3


def classify(w_avg):
    """Primary core: time-averaged W_out^j > 1, the mean (one run)."""
    return m.w_out(w_avg) > 1.0


def classify_snapshot(w):
    """The paper's core, from a snapshot: out-degree > 20 (M-1)/99 (one run)."""
    M = w.shape[-1]
    return m.out_degree(w) > 20.0 * (M - 1) / 99.0


def advance(x, w, n_steps):
    """Run n_steps, the last WIN of them averaged. Returns x, w, w_avg."""
    return m.run(x, w, A, C, DELTA, n_steps, avg_from=max(0, n_steps - WIN))


def grow(seed_batch, t0):
    # Each seed gets its own generator, so a run does not depend on batching.
    parts = [m.init_state(N, 1, np.random.default_rng(seed)) for seed in seed_batch]
    x = np.concatenate([p[0] for p in parts])
    w = np.concatenate([p[1] for p in parts])
    late = min(1_000_000, t0 // 2)
    x, w, wa_early = advance(x, w, t0 - late)
    x, w, wa = advance(x, w, late)
    return x, w, wa_early, wa


def summarize(w, w_avg, orig_ids, orig_core_ids):
    """Classify one run; w is the snapshot at the checkpoint, w_avg the
    WIN-step average ending there; orig_ids[k] is the original index of
    current unit k; orig_core_ids the core at the end of growth."""
    core = classify(w_avg)
    snap = classify_snapshot(w)
    M = w_avg.shape[-1]
    ids = np.asarray(orig_ids)
    oc = np.isin(ids, orig_core_ids)
    wo = m.w_out(w_avg)
    return {
        "M": int(M),
        "core_size": int(core.sum()),
        "core_from_orig_core": int((core & oc).sum()),
        "core_from_orig_periph": int((core & ~oc).sum()),
        "orig_core_present": int(oc.sum()),
        "snap_core_size": int(snap.sum()),
        "snap_core_from_orig_periph": int((snap & ~oc).sum()),
        "snap_blocks": m.block_counts(w, snap),
        "wout_sorted": [round(float(v), 3) for v in np.sort(wo)[::-1]],
        "core_ids": [int(i) for i in ids[core]],
    }


def run_arm(x, w, ids, orig_core_ids, checkpoints):
    """x (S, M), w (S, M, M); ids list of per-run original-id arrays."""
    out = [[] for _ in range(x.shape[0])]
    done = 0
    for cp in checkpoints:
        x, w, wa = advance(x, w, cp - done)
        done = cp
        for s in range(x.shape[0]):
            rec = summarize(w[s], wa[s], ids[s], orig_core_ids)
            rec["t"] = cp
            out[s].append(rec)
    return out


def worker(args):
    seed_batch, t0, t1 = args
    t_start = time.time()
    x, w, wa_early, wa = grow(seed_batch, t0)
    checkpoints = [60_000, 200_000, 500_000, t1] if t1 > 500_000 else [t1]
    results = []
    for s, seed in enumerate(seed_batch):
        rng = np.random.default_rng([seed, 7])
        all_ids = np.arange(N)
        core = classify(wa[s])
        core_early = classify(wa_early[s])
        core_ids = all_ids[core]
        periph_ids = all_ids[~core]
        k = len(core_ids)
        base = summarize(w[s], wa[s], all_ids, core_ids)
        base["t"] = 0
        rec = {
            "seed": int(seed),
            "t0": t0,
            "grown": base,
            "core_early_size": int(core_early.sum()),
            "core_overlap_early_late": int((core & core_early).sum()),
            "snap_core_agrees": int((core == classify_snapshot(w[s])).sum()),
            "arms": {},
        }
        xs, ws = x[s:s + 1], w[s:s + 1]

        # control and suppress_core: same size, batched
        w_sup = m.suppress_sources(ws, core, EPS)
        xb = np.concatenate([xs, xs])
        wb = np.concatenate([ws, w_sup])
        o = run_arm(xb, wb, [all_ids, all_ids], core_ids, checkpoints)
        rec["arms"]["control"] = o[0]
        rec["arms"]["suppress_core"] = o[1]

        # remove_core and remove_periph: both leave N - k units, batched
        keep_rc = ~core
        drop_p = rng.choice(periph_ids, size=k, replace=False)
        keep_rp = ~np.isin(all_ids, drop_p)
        x1, w1 = m.remove_units(xs, ws, keep_rc)
        x2, w2 = m.remove_units(xs, ws, keep_rp)
        o = run_arm(np.concatenate([x1, x2]), np.concatenate([w1, w2]),
                    [all_ids[keep_rc], all_ids[keep_rp]], core_ids, checkpoints)
        rec["arms"]["remove_core"] = o[0]
        rec["arms"]["remove_periph"] = o[1]

        # remove_half_core
        drop_h = rng.choice(core_ids, size=(k + 1) // 2, replace=False)
        keep_h = ~np.isin(all_ids, drop_h)
        x3, w3 = m.remove_units(xs, ws, keep_h)
        o = run_arm(x3, w3, [all_ids[keep_h]], core_ids, checkpoints)
        rec["arms"]["remove_half_core"] = o[0]
        rec["removed_half"] = [int(i) for i in drop_h]
        results.append(rec)
    print(f"batch {seed_batch} done in {time.time() - t_start:.0f}s", flush=True)
    return results


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--seeds", type=int, default=12)
    p.add_argument("--t0", type=int, default=3_000_000)
    p.add_argument("--t1", type=int, default=1_000_000)
    p.add_argument("--procs", type=int, default=4)
    p.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "results"))
    a = p.parse_args()
    seeds = list(range(1, a.seeds + 1))
    batches = [seeds[i::a.procs] for i in range(a.procs) if seeds[i::a.procs]]
    with Pool(len(batches)) as pool:
        parts = pool.map(worker, [(b, a.t0, a.t1) for b in batches])
    res = sorted([r for part in parts for r in part], key=lambda r: r["seed"])
    os.makedirs(a.out, exist_ok=True)
    meta = {"a": A, "c": C, "delta": DELTA, "N": N, "win": WIN, "eps": EPS,
            "t0": a.t0, "t1": a.t1, "seeds": seeds}
    with open(os.path.join(a.out, "runs.json"), "w") as f:
        json.dump({"meta": meta, "runs": res}, f, indent=1)
    print("wrote", os.path.join(a.out, "runs.json"))


if __name__ == "__main__":
    main()
