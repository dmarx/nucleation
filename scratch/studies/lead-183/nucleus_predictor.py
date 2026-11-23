"""LEAD-183: a non-monotone, architecture-only predictor of productive seed sets,
tested out of sample on a kinetic constraint-growth model.

See PREREGISTRATION.md for the predictor, the system and the criterion, fixed
before any test run. Run: python3 -I nucleus_predictor.py [--quick]
"""
from __future__ import annotations

import itertools
import json
import random
import sys
from collections import deque

import numpy as np

# ---------------------------------------------------------------- architecture


class Architecture:
    """Graph, q states per component, a relation per edge, a target x*."""

    def __init__(self, n, edges, q, rel, target):
        self.n = n
        self.q = q
        self.edges = edges
        self.rel = rel  # (u, v) -> set of allowed (a, b); stored both ways
        self.target = target
        self.strength = {e: 1 for e in rel}  # bond strength; rigid edges 2 in lattices
        self.nbrs = [[] for _ in range(n)]
        for u, v in edges:
            self.nbrs[u].append(v)
            self.nbrs[v].append(u)

    def allowed(self, u, v):
        return self.rel[(u, v)]


def lattice_architecture(L, q, p_rigid, m, rng):
    n = L * L
    edges = []
    for i in range(L):
        for j in range(L):
            v = i * L + j
            if j + 1 < L:
                edges.append((v, v + 1))
            if i + 1 < L:
                edges.append((v, v + L))
    target = [rng.randrange(q) for _ in range(n)]
    rel = {}
    strength = {}
    others = [(a, b) for a in range(q) for b in range(q)]
    for u, v in edges:
        strength[(u, v)] = strength[(v, u)] = 1
        tu, tv = target[u], target[v]
        if rng.random() < p_rigid:
            perm = list(range(q))
            rng.shuffle(perm)
            # make perm map tu -> tv
            k = perm.index(tv)
            perm[k], perm[tu] = perm[tu], perm[k]
            allowed = {(a, perm[a]) for a in range(q)}
            strength[(u, v)] = strength[(v, u)] = 2
        elif AMBIGUITY == "random":
            pool = [p for p in others if p != (tu, tv)]
            allowed = {(tu, tv)} | set(rng.sample(pool, m))
        else:  # "two-sided": ambiguous from the target state in both directions
            b = rng.choice([x for x in range(q) if x != tv])
            a = rng.choice([x for x in range(q) if x != tu])
            allowed = {(tu, tv), (tu, b), (a, tv)}
        rel[(u, v)] = allowed
        rel[(v, u)] = {(b, a) for a, b in allowed}
    arch = Architecture(n, edges, q, rel, target)
    arch.strength = strength
    return arch


# ---------------------------------------------------------------- predictors


def arc_consistency(arch, seeds):
    """AC-3 with seeds clamped at target. Returns list of domains (sets)."""
    dom = [set(range(arch.q)) for _ in range(arch.n)]
    for s in seeds:
        dom[s] = {arch.target[s]}
    queue = deque((u, v) for u in range(arch.n) for v in arch.nbrs[u])
    inq = set(queue)
    while queue:
        u, v = queue.popleft()
        inq.discard((u, v))
        r = arch.allowed(u, v)
        new = {a for a in dom[u] if any((a, b) in r for b in dom[v])}
        if new != dom[u]:
            dom[u] = new
            for w in arch.nbrs[u]:
                if w != v and (w, u) not in inq:
                    queue.append((w, u))
                    inq.add((w, u))
    return dom


def island_ac(arch, seeds):
    """Pre-registered v1 island: static arc consistency. Degenerate on the
    pre-registered system (every single seed's island is the whole lattice)."""
    dom = arc_consistency(arch, seeds)
    return {v for v in range(arch.n) if dom[v] == {arch.target[v]}}


def compatible(arch, v, state):
    return [a for a in range(arch.q)
            if all(state[w] < 0 or (a, state[w]) in arch.allowed(v, w) for w in arch.nbrs[v])]


def island_forward(arch, seeds):
    """Amended island: forward forcing closure. Starting from the seeds at
    target, repeatedly set any unset component adjacent to the set ones whose
    states compatible with its set neighbours are exactly {x*_v}. What the seed
    forces by propagation through what is already formed, as the cut-out
    definition of a folding island asks."""
    state = [-1] * arch.n
    for s in seeds:
        state[s] = arch.target[s]
    frontier = deque(w for s in seeds for w in arch.nbrs[s])
    while frontier:
        v = frontier.popleft()
        if state[v] >= 0:
            continue
        if compatible(arch, v, state) == [arch.target[v]]:
            state[v] = arch.target[v]
            frontier.extend(w for w in arch.nbrs[v] if state[w] < 0)
    return {v for v in range(arch.n) if state[v] >= 0}


ISLAND = "forward"
AMBIGUITY = "two-sided"


def island(arch, seeds):
    return island_forward(arch, seeds) if ISLAND == "forward" else island_ac(arch, seeds)


def hop_distances(arch, src):
    d = [-1] * arch.n
    d[src] = 0
    dq = deque([src])
    while dq:
        u = dq.popleft()
        for w in arch.nbrs[u]:
            if d[w] < 0:
                d[w] = d[u] + 1
                dq.append(w)
    return d


class Predictors:
    def __init__(self, arch):
        self.arch = arch
        self._isl1 = {}
        self._dist = {}

    def isl1(self, s):
        if s not in self._isl1:
            self._isl1[s] = island(self.arch, [s])
        return self._isl1[s]

    def dist(self, s):
        if s not in self._dist:
            self._dist[s] = hop_distances(self.arch, s)
        return self._dist[s]

    def vic(self, S):
        """P1: Voronoi-island coverage."""
        if not S:
            return 0.0
        total = 0.0
        for v in range(self.arch.n):
            ds = [self.dist(s)[v] for s in S]
            dmin = min(ds)
            near = [s for s, d in zip(S, ds) if d == dmin]
            total += sum(v in self.isl1(s) for s in near) / len(near)
        return total / self.arch.n

    def icn(self, S):
        """P2: joint island coverage divided by the number of seeded island components."""
        if not S:
            return 0.0
        I = island(self.arch, list(S))
        seen, k = set(), 0
        for s in S:
            if s in seen:
                continue
            k += 1
            dq = deque([s])
            seen.add(s)
            while dq:
                u = dq.popleft()
                for w in self.arch.nbrs[u]:
                    if w in I and w not in seen:
                        seen.add(w)
                        dq.append(w)
        return (len(I) / self.arch.n) / k

    def count(self, S):
        return float(len(S))

    def ufi(self, S):
        U = set()
        for s in S:
            U |= self.isl1(s)
        return len(U) / self.arch.n

    def joint(self, S):
        return len(island(self.arch, list(S))) / self.arch.n if S else 0.0


PREDICTORS = ["vic", "icn", "count", "ufi", "joint"]
MONOTONE = ["count", "ufi", "joint"]

# ---------------------------------------------------------------- dynamics


KAPPA = 100.0  # cooperativity: net attachment rate kappa**(s - TAU), s = bond strength
TAU = 2      # threshold-2 regime of the kinetic tile assembly model


def simulate(arch, seeds, eps, rng, kappa=None):
    """One zero-temperature growth run. Returns True on exact target."""
    n, q = arch.n, arch.q
    state = [-1] * n
    for s in seeds:
        state[s] = arch.target[s]
    nset = [0] * n  # total bond strength from set neighbours, per unset component
    for s in seeds:
        for w in arch.nbrs[s]:
            nset[w] += arch.strength[(s, w)]
    kap = KAPPA if kappa is None else kappa
    unset = [v for v in range(n) if state[v] < 0]
    while unset:
        rates = [kap ** (nset[v] - TAU) if nset[v] > 0 else eps for v in unset]
        tot = sum(rates)
        x = rng.random() * tot
        acc = 0.0
        idx = len(unset) - 1
        for i, r in enumerate(rates):
            acc += r
            if x < acc:
                idx = i
                break
        v = unset[idx]
        if nset[v] == 0:
            a = rng.randrange(q)
        else:
            cand = []
            for a in range(q):
                ok = True
                for w in arch.nbrs[v]:
                    if state[w] >= 0 and (a, state[w]) not in arch.allowed(v, w):
                        ok = False
                        break
                if ok:
                    cand.append(a)
            if not cand:
                return False  # jam
            a = rng.choice(cand)
        if a != arch.target[v]:
            return False  # any wrong state is final at zero temperature
        state[v] = a
        unset[idx] = unset[-1]
        unset.pop()
        for w in arch.nbrs[v]:
            if state[w] < 0:
                nset[w] += arch.strength[(v, w)]
    return True


def estimate_V(arch, seeds, eps, runs, rng, kappa=None):
    wins = sum(simulate(arch, seeds, eps, rng, kappa) for _ in range(runs))
    return wins / runs


# ---------------------------------------------------------------- metrics


def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)

    def rank(a):
        order = a.argsort(kind="mergesort")
        r = np.empty(len(a))
        r[order] = np.arange(len(a))
        # average ties
        for val in np.unique(a):
            m = a == val
            r[m] = r[m].mean()
        return r

    rx, ry = rank(x), rank(y)
    if rx.std() == 0 or ry.std() == 0:
        return float("nan")
    return float(np.corrcoef(rx, ry)[0, 1])


def auc(scores_pos, scores_neg):
    """P(score_pos > score_neg) + 0.5 P(tie)."""
    if not scores_pos or not scores_neg:
        return float("nan")
    p = np.asarray(scores_pos)[:, None]
    q = np.asarray(scores_neg)[None, :]
    return float(((p > q).sum() + 0.5 * (p == q).sum()) / (p.size * q.size))


def addition_pairs(records, runs):
    """Pairs (S, S+c) among evaluated sets with significance labels."""
    by = {tuple(sorted(r["S"])): r for r in records}
    out = []
    keys = list(by)
    for key in keys:
        for c_key in keys:
            if len(c_key) == len(key) + 1 and set(key) <= set(c_key):
                a, b = by[key], by[c_key]
                va, vb = a["V"], b["V"]
                se = np.sqrt(va * (1 - va) / runs + vb * (1 - vb) / runs)
                d = vb - va
                lab = 0
                if d < -2 * se and d <= -0.05:
                    lab = -1
                elif d > 2 * se and d >= 0.05:
                    lab = 1
                out.append({"S": key, "Sc": c_key, "dV": d, "label": lab,
                            **{"d_" + p: b[p] - a[p] for p in PREDICTORS}})
    return out


def m2(pairs, p):
    dec = [-x["d_" + p] for x in pairs if x["label"] == -1]
    inc = [-x["d_" + p] for x in pairs if x["label"] == 1]
    flagged = [x for x in pairs if x["d_" + p] < -1e-12]
    recall = (sum(1 for x in pairs if x["label"] == -1 and x["d_" + p] < -1e-12) / len(dec)
              if dec else float("nan"))
    precision = (sum(1 for x in flagged if x["label"] == -1) / len(flagged)
                 if flagged else float("nan"))
    return {"auc": auc(dec, inc), "recall": recall, "precision": precision,
            "n_dec": len(dec), "n_inc": len(inc), "n_flagged": len(flagged)}


# ---------------------------------------------------------------- driver


def run_architecture(arch_seed, L=8, q=4, p_rigid=0.5, m=2, eps=1e-4, runs=300,
                     pool_size=10, n_triples=40, out=None):
    rng = random.Random(arch_seed)
    arch = lattice_architecture(L, q, p_rigid, m, rng)
    pred = Predictors(arch)
    pool = rng.sample(range(arch.n), pool_size)
    sets = [()] + [(s,) for s in pool] + list(itertools.combinations(pool, 2))
    triples = list(itertools.combinations(pool, 3))
    rng.shuffle(triples)
    sets += triples[:n_triples]
    sim_rng = random.Random(10_000 + arch_seed)
    records = []
    for S in sets:
        rec = {"arch": arch_seed, "p_rigid": p_rigid, "S": list(S),
               "V": estimate_V(arch, list(S), eps, runs, sim_rng)}
        for p in PREDICTORS:
            rec[p] = getattr(pred, p)(list(S))
        records.append(rec)
        if out is not None:
            out.write(json.dumps(rec) + "\n")
            out.flush()
    return records


def summarize(records, runs):
    nonempty = [r for r in records if r["S"]]
    m1 = {p: spearman([r[p] for r in nonempty], [r["V"] for r in nonempty]) for p in PREDICTORS}
    pairs = addition_pairs(records, runs)
    return m1, pairs


def main(quick=False):
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    runs = 60 if quick else 300
    cfgs = [(s, 0.5) for s in range(5)] + [(100, 0.4), (101, 0.6)]
    if quick:
        cfgs = cfgs[:1]
    path = os.path.join(here, "results_quick.jsonl" if quick else "results.jsonl")
    done = set()
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                r = json.loads(line)
                done.add((r["arch"], r["p_rigid"]))
    allrec = {}
    with open(path, "a") as out:
        for s, pr in cfgs:
            if (s, pr) in done:
                continue
            run_architecture(s, p_rigid=pr, runs=runs, n_triples=10 if quick else 40, out=out)
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            allrec.setdefault((r["arch"], r["p_rigid"]), []).append(r)
    summary = {"runs": runs, "per_arch": {}, "primary": {}, "sensitivity": {}}
    prim_pairs, sens_pairs, m1s = [], [], {p: [] for p in PREDICTORS}
    for (s, pr), recs in sorted(allrec.items()):
        m1, pairs = summarize(recs, runs)
        summary["per_arch"][f"{s}@{pr}"] = {
            "m1": m1, "V_empty": [r["V"] for r in recs if not r["S"]][0],
            "V_max": max(r["V"] for r in recs),
            "m2": {p: m2(pairs, p) for p in PREDICTORS}}
        if pr == 0.5:
            prim_pairs += pairs
            for p in PREDICTORS:
                m1s[p].append(m1[p])
        else:
            sens_pairs += pairs
    summary["primary"]["m1_mean"] = {p: float(np.nanmean(m1s[p])) for p in PREDICTORS}
    summary["primary"]["m2"] = {p: m2(prim_pairs, p) for p in PREDICTORS}
    if sens_pairs:
        summary["sensitivity"]["m2"] = {p: m2(sens_pairs, p) for p in PREDICTORS}
    best_mono = max(summary["primary"]["m1_mean"][p] for p in MONOTONE)
    verdict = {}
    for p in ["vic", "icn"]:
        mm = summary["primary"]["m2"][p]
        verdict[p] = bool(mm["auc"] >= 0.7 and mm["recall"] >= 0.5
                          and summary["primary"]["m1_mean"][p] >= best_mono - 0.05)
    summary["primary"]["transfer"] = verdict
    summary["primary"]["best_monotone_m1"] = best_mono
    if not prim_pairs or not any(x["label"] == -1 for x in prim_pairs):
        summary["primary"]["void"] = True
    out_path = os.path.join(here, "summary_quick.json" if quick else "summary.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=1)
    print(json.dumps(summary["primary"], indent=1))
    return summary


if __name__ == "__main__":
    main(quick="--quick" in sys.argv)
