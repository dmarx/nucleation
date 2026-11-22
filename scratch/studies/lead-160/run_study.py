"""LEAD-160: run CASE-187's comparison on small gridworld mazes.

Writes one JSON line per (seed, item) to results.jsonl and skips items
already written, so a stopped run resumes. Usage:

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run_study.py [n_seeds]
"""
from __future__ import annotations

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import gridagents as ga  # noqa: E402

H, W, EXTRA = 8, 8, 8
N_STREAM = 60_000
LEVELS = (0.5, 0.8, 1.0)
K = 5
CHECKPOINTS = (0, 30, 100, 300, 1000, 3000, 10000)
DAMAGE = (0.1, 0.3)
DAMAGE_DRAWS = 2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.jsonl")


def done_items():
    have = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            for line in f:
                r = json.loads(line)
                have.add((r["seed"], r["item"]))
    return have


def emit(rec):
    with open(OUT, "a") as f:
        f.write(json.dumps(rec) + "\n")


def trained(S, trans):
    out = {}
    for cls in ga.AGENTS:
        ag = cls(S)
        ag.train(trans)
        out[cls.name] = ag
    return out


def clone(ag):
    new = type(ag)(ag.S)
    for k, v in vars(ag).items():
        setattr(new, k, v.copy() if isinstance(v, np.ndarray) else v)
    return new


def dist_from_Q(Q):
    V = Q.max(axis=1)
    with np.errstate(divide="ignore"):
        d = 1 + np.round(np.log(V) / np.log(ga.GAMMA_P))
    d[V <= 0] = np.inf
    np.fill_diagonal(d, 0)
    return d


def blocked(Th, s, d, t):
    Th = Th.copy()
    Th[s, d] = s
    Th[t, ga.OPP[d]] = t
    return Th


def occ_ok(est, true):
    return np.abs(est - true) <= 1e-6 * np.abs(true) + 1e-15


def costs(S):
    G = S
    extract_P = S * ga.A * G
    extract_D = S * ga.A * S * S
    bfs = S * ga.A
    solve = S ** 3
    return {
        "Q1_next": {"M": 1, "P": G, "D": S * S},
        "Q2_dist": {"M": bfs, "P": ga.A, "D": extract_D + bfs},
        "Q3_occ": {"M": solve, "P": extract_P + solve, "D": ga.A},
        "Q4_dist_do": {"M": 2 + bfs, "P": extract_P + 2 + bfs, "D": extract_D + 2 + bfs},
        "Q4_occ_do": {"M": 2 + solve, "P": extract_P + 2 + solve, "D": 5 * ga.A},
        "budget_own": {"M": bfs, "P": ga.A, "D": ga.A},
        "budget_common": bfs,
    }


def queries(m, agents, dist, occ_true, block_set):
    S = m.S
    off = ~np.eye(S, dtype=bool)
    fin = off & np.isfinite(dist)
    res = {}
    models = {n: ag.model() for n, ag in agents.items()}
    res["Q1_next"] = {n: float((models[n] == m.T).mean()) for n in agents}
    q2 = {"M": ga.all_pairs_dist(models["M"]),
          "P": dist_from_Q(agents["P"].Q),
          "D": ga.all_pairs_dist(models["D"])}
    res["Q2_dist"] = {n: float((q2[n][fin] == dist[fin]).mean()) for n in agents}
    q3 = {"M": ga.occupancy(models["M"]), "P": ga.occupancy(models["P"]),
          "D": agents["D"].occupancy()}
    res["Q3_occ"] = {n: float(occ_ok(q3[n], occ_true).mean()) for n in agents}
    d4 = {n: [] for n in ("M", "P", "P_own", "D")}
    o4 = {n: [] for n in agents}
    for (s, d, t) in block_set:
        m2 = m.copy()
        m2.block(s, d)
        dist2 = ga.all_pairs_dist(m2.T)
        occ2 = ga.occupancy(m2.T)
        f2 = off & np.isfinite(dist2)
        for n in agents:
            Th2 = blocked(models[n], s, d, t)
            d4[n].append(float((ga.all_pairs_dist(Th2)[f2] == dist2[f2]).mean()))
            if n == "D":
                est = agents["D"].occupancy_after_block(s, d, t)
            else:
                est = ga.occupancy(Th2)
            o4[n].append(float(occ_ok(est, occ2).mean()))
        d4["P_own"].append(float((q2["P"][f2] == dist2[f2]).mean()))
        changed = f2 & (dist2 != dist)
        d4.setdefault("changed_frac", []).append(float(changed.sum() / f2.sum()))
    res["Q4_dist_do"] = {n: float(np.mean(v)) for n, v in d4.items()}
    res["Q4_occ_do"] = {n: float(np.mean(v)) for n, v in o4.items()}
    return res


def pick_blocks(m, dist):
    """K open passages on the most shortest paths whose removal keeps the maze connected."""
    S = m.S
    cands = []
    for s, d in m.passages():
        t = m.T[s, d]
        m2 = m.copy()
        m2.block(s, d)
        if not np.isfinite(ga.all_pairs_dist(m2.T)).all():
            continue
        use = ((dist[:, s][:, None] + 1 + dist[t][None, :] == dist) |
               (dist[:, t][:, None] + 1 + dist[s][None, :] == dist)).sum()
        cands.append((int(use), s, d, int(t)))
    cands.sort(reverse=True)
    return [(s, d, t) for _, s, d, t in cands[:K]]


def pick_shortcuts(m, dist):
    out = []
    for s, d in m.walls():
        t = m.neighbour(s, d)
        new = np.minimum(dist, np.minimum(dist[:, s][:, None] + 1 + dist[t][None, :],
                                          dist[:, t][:, None] + 1 + dist[s][None, :]))
        out.append((float((dist - new).sum()), s, d, int(t)))
    out.sort(reverse=True)
    return [(s, d, t) for _, s, d, t in out[:K]]


def recovery(m2, agents, rng, extra=None):
    """Online learning from a fresh random walk in m2; competence at checkpoints."""
    dist2 = ga.all_pairs_dist(m2.T)
    stream = ga.random_walk(m2.T, CHECKPOINTS[-1], rng)
    out = {n: [] for n in agents}
    first_seen = {}
    flags = {n: {} for n in agents}
    i = 0
    for cp in CHECKPOINTS:
        while i < cp:
            s, a, s2 = (int(v) for v in stream[i])
            first = (s, a) not in first_seen
            if first:
                first_seen[(s, a)] = i
            for n, ag in agents.items():
                if first:
                    flags[n][(s, a)] = ag.error(s, a, s2)
                ag.learn(s, a, s2)
            i += 1
        for n, ag in agents.items():
            succ, exc, _ = ga.competence(m2.T, ag.values(), dist2)
            out[n].append([cp, succ, exc])
    return out, flags


def run_seed(seed, have):
    rng = np.random.default_rng(1000 + seed)
    m = ga.make_maze(H, W, EXTRA, rng)
    S = m.S
    dist = ga.all_pairs_dist(m.T)
    occ_true = ga.occupancy(m.T)
    stream = ga.random_walk(m.T, N_STREAM, rng)
    seen = np.zeros((S, ga.A), bool)
    cover = None
    for i, (s, a, _) in enumerate(stream):
        seen[s, a] = True
        if cover is None and seen.all():
            cover = i + 1
            break
    assert cover is not None, "stream did not cover every unit"
    blocks = pick_blocks(m, dist)
    shortcuts = pick_shortcuts(m, dist)

    def success_M(n):
        pl = ga.Planner(S)
        pl.train(stream[:n])
        return ga.competence(m.T, pl.values(), dist)[0]

    # ---- matched levels: smallest prefix at which the planner reaches the target success
    levels = {}
    for tgt in LEVELS:
        lo, hi = 1, cover
        while lo < hi:
            mid = (lo + hi) // 2
            if success_M(mid) >= tgt:
                hi = mid
            else:
                lo = mid + 1
        levels[f"succ>={tgt}"] = lo
    levels["full_coverage"] = cover

    for name, n in levels.items():
        item = f"level:{name}"
        if (seed, item) in have:
            continue
        t0 = time.time()
        agents = trained(S, stream[:n])
        comp = {}
        for k, ag in agents.items():
            succ, exc, _ = ga.competence(m.T, ag.values(), dist)
            comp[k] = {"success": succ, "excess": exc, "train_updates": ag.updates,
                       "memory": ag.memory()}
        pis = {k: ga.greedy(ag.values()) for k, ag in agents.items()}
        off = ~np.eye(S, dtype=bool)
        agree = {"M_P": float((pis["M"] == pis["P"])[off].mean()),
                 "M_D": float((pis["M"] == pis["D"])[off].mean())}
        q = queries(m, agents, dist, occ_true, blocks)
        emit({"seed": seed, "item": item, "n_transitions": int(n), "competence": comp,
              "agreement": agree, "queries": q, "costs": costs(S),
              "secs": round(time.time() - t0, 2)})

    full = trained(S, stream[:cover])

    # ---- test 3: targeted intervention on the unit that carries a passage
    item = "edit"
    if (seed, item) not in have:
        rows = []
        for (s, d, t) in blocks:
            m2 = m.copy()
            m2.block(s, d)
            dist2 = ga.all_pairs_dist(m2.T)
            rec = {"passage": [s, d, t]}
            for k, ag in full.items():
                pre_succ, pre_exc, pre_done = ga.competence(m2.T, ag.values(), dist2)
                ed = clone(ag)
                ed.local_edit_block(s, d)
                ed.local_edit_block(t, ga.OPP[d])
                succ, exc, done = ga.competence(m2.T, ed.values(), dist2)
                affected = ~pre_done & ~np.eye(S, dtype=bool)
                rec[k] = {"pre_success": pre_succ, "post_success": succ, "pre_excess": pre_exc,
                          "post_excess": exc, "n_affected": int(affected.sum()),
                          "repaired": float(done[affected].mean()) if affected.any() else None,
                          "units_written": {"M": 2, "P": 2 * S, "D": 2 * S}[k]}
            # variant: the same block propagated through every demon (Woodbury), no table
            pre_succ, pre_exc, pre_done = ga.competence(m2.T, full["D"].values(), dist2)
            ed = clone(full["D"])
            ed.global_edit_block(s, d, t)
            succ, exc, done = ga.competence(m2.T, ed.values(), dist2)
            affected = ~pre_done & ~np.eye(S, dtype=bool)
            rec["D_global"] = {"pre_success": pre_succ, "post_success": succ, "pre_excess": pre_exc,
                               "post_excess": exc, "n_affected": int(affected.sum()),
                               "repaired": float(done[affected].mean()) if affected.any() else None,
                               "units_written": S * ga.A * S}
            rows.append(rec)
        emit({"seed": seed, "item": item, "rows": rows})

    # ---- test 4a: environmental change, recovery by ordinary online learning
    for kind, sites in (("block", blocks), ("shortcut", shortcuts)):
        for j, (s, d, t) in enumerate(sites):
            item = f"change:{kind}:{j}"
            if (seed, item) in have:
                continue
            m2 = m.copy()
            (m2.block if kind == "block" else m2.open)(s, d)
            agents = {k: clone(ag) for k, ag in full.items()}
            curves, _ = recovery(m2, agents, np.random.default_rng(seed * 100 + j + (50 if kind == "shortcut" else 0)))
            emit({"seed": seed, "item": item, "site": [s, d, t], "curves": curves})

    # ---- test 4b: damage to the predictive store, recovery and detection
    for f in DAMAGE:
        for r in range(DAMAGE_DRAWS):
            item = f"damage:{f}:{r}"
            if (seed, item) in have:
                continue
            drng = np.random.default_rng(seed * 1000 + int(f * 100) + r)
            units = np.array([(s, a) for s in range(S) for a in range(ga.A)])
            n_dmg = int(round(f * len(units)))
            pick = drng.choice(len(units), size=n_dmg, replace=False)
            dst = units[pick]
            src = units[drng.choice(len(units), size=n_dmg, replace=True)]
            agents = {k: clone(ag) for k, ag in full.items()}
            effective = {}
            for k, ag in agents.items():
                before = {"M": ag.__dict__.get("Th"), "P": ag.__dict__.get("Q"),
                          "D": ag.__dict__.get("Msr")}[k].copy()
                ag.overwrite(dst, src)
                after = {"M": ag.__dict__.get("Th"), "P": ag.__dict__.get("Q"),
                         "D": ag.__dict__.get("Msr")}[k]
                diff = (before != after)
                if diff.ndim == 3:
                    diff = diff.any(axis=2)
                effective[k] = {(int(s), int(a)) for s, a in np.argwhere(diff)}
            curves, flags = recovery(m, agents, drng)
            det = {}
            for k in agents:
                hits = [v for u, v in flags[k].items() if u in effective[k]]
                fas = [v for u, v in flags[k].items() if u not in effective[k]]
                det[k] = {"n_effective": len(effective[k]),
                          "hit_rate": float(np.mean(hits)) if hits else None,
                          "false_alarm_rate": float(np.mean(fas)) if fas else None,
                          "n_first_visits": len(flags[k])}
            emit({"seed": seed, "item": item, "fraction": f, "curves": curves, "detection": det})


def main():
    n_seeds = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    have = done_items()
    for seed in range(n_seeds):
        t0 = time.time()
        run_seed(seed, have)
        print(f"seed {seed} done in {time.time() - t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
