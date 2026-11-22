"""LEAD-016 study: arms of CASE-117 on the operator population of opmodel.py.

Usage: python3 -I study.py RULE [SEEDS]   (results/runs_<RULE>.jsonl, resumable)

For each rule, K in {4, 6} and seed: differentiate for T0 steps, then run each
arm from that snapshot. Every arm is one JSON line, keyed by
(rule, K, seed, arm); finished keys are skipped on restart. The snapshot is
itself a line ("diff"), and arms are rebuilt from it, so a restart does not
redo differentiation.
"""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # python3 -I drops it
from opmodel import (Config, init_state, make_env, shares, logit_for_share, step,
                     own_risk, collective_risk, marginal_contribution,
                     mutual_information, usage, entropy, gram_spectrum, State)

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
T0 = 40000        # differentiation
TREC = 20000      # recovery / refill window
TS = 20000        # suppression window
EVERY = 250       # checkpoint interval
R = 3             # the rare context (p = 0.02)
WD = 1e-4
RULE_KW = {"moe": {}, "moe_aux": {"aux": 0.01}, "moe_bias": {}, "rep": {}, "uniform": {}}


def cfg_for(rule, K, wd=0.0):
    return Config(rule=rule, K=K, wd=wd, **RULE_KW[rule])


def done_keys(path):
    keys, diffs = set(), {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue  # a torn last line from a killed run
                keys.add((r["rule"], r["K"], r["seed"], r["arm"]))
                if r["arm"] == "diff":
                    diffs[(r["K"], r["seed"])] = r
    return keys, diffs


def append(path, rec):
    with open(path, "a") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())


def snapshot_metrics(cfg, st, beta):
    P = shares(cfg, st)
    r = own_risk(cfg, st, beta)
    return {
        "P": np.round(P, 6).tolist(),
        "own_risk": np.round(r, 6).tolist(),
        "coll_risk": np.round(collective_risk(cfg, st, beta), 6).tolist(),
        "marg": np.round(marginal_contribution(cfg, st, beta), 6).tolist(),
        "MI": mutual_information(cfg, P),
        "usage": np.round(usage(cfg, P), 6).tolist(),
        "H_usage": entropy(usage(cfg, P)),
        "gram": np.round(gram_spectrum(st), 6).tolist(),
    }


def restore(cfg, d, rng_seed):
    rng = np.random.default_rng(rng_seed)
    beta = make_env(cfg, rng)
    st = init_state(cfg, rng)
    st.theta = np.array(d["theta"])
    st.Z = np.array(d["Z"])
    st.b = np.array(d["b"])
    return beta, st


def track(cfg, st, beta, i, T, rng, ctx_p=None):
    """Run T steps, recording i's share and risk in R, and who holds R."""
    traj = []
    for k in range(T):
        step(cfg, st, beta, rng, ctx_p)
        if (k + 1) % EVERY == 0:
            P = shares(cfg, st)
            traj.append([
                int(st.n_ctx[R]),
                float(P[R, i]) if st.alive[i] else 0.0,
                float(own_risk(cfg, st, beta)[i, R]),
                float(collective_risk(cfg, st, beta, P)[R]),
                int(P[R].argmax()),
                float(collective_risk(cfg, st, beta, P)[:R].mean()),
            ])
    return traj


def thin(traj):
    """Keep checkpoints at roughly log-spaced indices, to keep files small."""
    idx = sorted(set(np.unique(np.geomspace(1, len(traj), 16).astype(int) - 1).tolist()))
    return [[round(v, 5) if isinstance(v, float) else v for v in traj[k]] for k in idx]


def growth(traj, eps, n0=0.0):
    """Initial recovery exponent per R-sample, time to share 0.5, final share.
    R-sample counts are taken from n0, the count when the window opened."""
    n = np.array([t[0] for t in traj], float) - n0
    s = np.array([t[1] for t in traj], float)
    x = np.concatenate([[0.0], n])
    ly = np.log(np.concatenate([[eps], np.maximum(s, 1e-300)]))
    # slope over the window before the share reaches 0.1, at most 300 R samples
    m = (x <= 300) & (np.exp(ly) < 0.1)
    m[0] = True
    lam = float(np.polyfit(x[m], ly[m], 1)[0]) if m.sum() >= 3 else (
        float((ly[1] - ly[0]) / x[1]) if x[1] > 0 else float("nan"))
    hit = np.nonzero(s >= 0.5)[0]
    return {"lam_cond": lam, "nR_to_half": float(n[hit[0]]) if len(hit) else None,
            "final_share": float(s[-1])}


def arm_rare(cfg, d, seed, i, eps, freeze, sham=False):
    beta, st = restore(cfg, d, seed)
    rng = np.random.default_rng(10_000 + seed)
    if sham:
        # an operator as incompetent in R as the residents: a copy of the
        # specialist of context 0
        j = int(np.argmax(shares(cfg, st)[0]))
        st.theta[i] = st.theta[j].copy()
    st.Z[R, i] = logit_for_share(st.Z[R], st.b, st.alive, i, eps)
    st.frozen[i] = freeze
    u0 = float(usage(cfg, shares(cfg, st))[i])
    traj = track(cfg, st, beta, i, TREC, rng)
    out = growth(traj, eps)
    out.update({"usage0": u0, "usage_final": float(usage(cfg, shares(cfg, st))[i]),
                "traj": thin(traj)})
    return out


def arm_remove(cfg, d, seed, i):
    beta, st = restore(cfg, d, seed)
    rng = np.random.default_rng(20_000 + seed)
    st.alive[i] = False
    r0 = collective_risk(cfg, st, beta).tolist()
    traj = track(cfg, st, beta, i, TREC, rng)
    P = shares(cfg, st)
    holder = int(P[R].argmax())
    return {"risk_after_removal": r0, "traj": thin(traj), "holder": holder,
            "holder_share": float(P[R, holder]),
            "holder_own_risk_R": float(own_risk(cfg, st, beta)[holder, R]),
            "final": snapshot_metrics(cfg, st, beta)}


def arm_suppress(cfg, d, seed, i, coupled, eps=1e-3, freeze_release=False):
    """Clamp i's share in R at eps for TS steps, then release with no further
    intervention. Decoupled: i's exposure in R stays at its pre-suppression
    value throughout suppression (QUESTION-134's control)."""
    beta, st = restore(cfg, d, seed)
    rng = np.random.default_rng(30_000 + seed)
    risk_before = float(own_risk(cfg, st, beta)[i, R])
    P0 = shares(cfg, st)
    if not coupled:
        st.dec[R, i] = float(P0[R, i])  # its typical exposure before
    st.clamp[R, i] = eps
    e0 = st.exposure_acc[R, i]
    n0 = st.n_ctx[R]
    traj_s = track(cfg, st, beta, i, TS, rng)
    access = float((st.exposure_acc[R, i] - e0) / max(st.n_ctx[R] - n0, 1))
    risk_mid = float(own_risk(cfg, st, beta)[i, R])
    holder_mid = int(np.argmax(np.where(np.arange(cfg.K) == i, -1, shares(cfg, st)[R])))
    holder_mid_risk = float(own_risk(cfg, st, beta)[holder_mid, R])
    # release
    st.clamp[R, i] = np.nan
    st.dec[R, i] = np.nan
    st.Z[R, i] = logit_for_share(st.Z[R], st.b, st.alive, i, eps)
    st.frozen[i] = freeze_release
    n_rel = float(st.n_ctx[R])
    traj_r = track(cfg, st, beta, i, TREC, rng)
    g = growth(traj_r, eps, n_rel)
    g.update({"own_risk_R_before": risk_before, "own_risk_R_at_release": risk_mid,
              "own_risk_R_final": float(own_risk(cfg, st, beta)[i, R]),
              "access_during": access, "holder_at_release": holder_mid,
              "holder_risk_at_release": holder_mid_risk,
              "coll_risk_R_final": float(collective_risk(cfg, st, beta)[R]),
              "traj_suppress": thin(traj_s), "traj_release": thin(traj_r)})
    return g


ARMS = [
    ("rare_frozen_e2", lambda c, d, s, i: arm_rare(c, d, s, i, 1e-2, True)),
    ("rare_frozen_e3", lambda c, d, s, i: arm_rare(c, d, s, i, 1e-3, True)),
    ("rare_frozen_e5", lambda c, d, s, i: arm_rare(c, d, s, i, 1e-5, True)),
    ("rare_train_e3", lambda c, d, s, i: arm_rare(c, d, s, i, 1e-3, False)),
    ("sham_frozen_e3", lambda c, d, s, i: arm_rare(c, d, s, i, 1e-3, True, sham=True)),
    ("remove", lambda c, d, s, i: arm_remove(c, d, s, i)),
    ("suppress_coupled_wd0", lambda c, d, s, i: arm_suppress(c, d, s, i, True)),
    ("suppress_decoupled_wd0", lambda c, d, s, i: arm_suppress(c, d, s, i, False)),
    ("suppress_coupled_wd", lambda c, d, s, i: arm_suppress(c, d, s, i, True), WD),
    ("suppress_decoupled_wd", lambda c, d, s, i: arm_suppress(c, d, s, i, False), WD),
    ("suppress_coupled_wd_frozen",
     lambda c, d, s, i: arm_suppress(c, d, s, i, True, freeze_release=True), WD),
]


def main():
    rule = sys.argv[1]
    seeds = range(int(sys.argv[2]) if len(sys.argv) > 2 else 12)
    os.makedirs(RES, exist_ok=True)
    path = os.path.join(RES, f"runs_{rule}.jsonl")
    keys, diffs = done_keys(path)
    for seed in seeds:
        for K in (4, 6):
            cfg = cfg_for(rule, K)
            if (rule, K, seed, "diff") not in keys:
                t = time.time()
                rng = np.random.default_rng(seed)
                beta = make_env(cfg, rng)
                st = init_state(cfg, rng)
                for _ in range(T0):
                    step(cfg, st, beta, rng)
                rec = {"rule": rule, "K": K, "seed": seed, "arm": "diff",
                       "theta": st.theta.tolist(), "Z": st.Z.tolist(), "b": st.b.tolist(),
                       "n_R": int(st.n_ctx[R]),
                       "secs": time.time() - t}
                rec.update(snapshot_metrics(cfg, st, beta))
                append(path, rec)
                diffs[(K, seed)] = rec
                keys.add((rule, K, seed, "diff"))
            if rule == "uniform":
                continue
            d = diffs[(K, seed)]
            i = int(np.argmax(np.array(d["P"])[R]))
            for arm in ARMS:
                name, fn = arm[0], arm[1]
                wd = arm[2] if len(arm) > 2 else 0.0
                if (rule, K, seed, name) in keys:
                    continue
                t = time.time()
                out = fn(cfg_for(rule, K, wd), d, seed, i)
                rec = {"rule": rule, "K": K, "seed": seed, "arm": name, "spec": i,
                       "secs": time.time() - t}
                rec.update(out)
                append(path, rec)
                keys.add((rule, K, seed, name))
            print(rule, K, seed, "done", flush=True)


if __name__ == "__main__":
    main()
