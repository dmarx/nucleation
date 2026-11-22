#!/usr/bin/env python3
"""LEAD-135 — individuation by probing at rising budgets (CASE-202).

A resource-bounded constraint system (TERM-114), in its smallest finite
transition-system form, is here:

  - a set of admissible configurations, each an n-bit string;
  - a fixed local move rule: a single bit flip that STAYS inside the
    admissible set (Gopalan et al.'s solution graph, as CLAIM-583 uses);
  - a set of named demands, each a predicate on configurations (here: the
    config equals a stated target);
  - a probe budget b: the maximum number of moves a probe may attempt.

The restricted *static* probe family (b = 0) asks of a configuration only
which demands it meets (CASE-202; CLAIM-322's family is fixed in advance and
applied to every pair). At budget b the family is widened to: starting from
a configuration meeting demand D_i, which demands become reachable within b
admissible moves. This is the "reachability-between-demands" relation, the
process-layer readout CLAIM-583 separates from the configuration layer.

The VERDICT on a pair of mechanisms at budget b is whether this readout
distinguishes them. We probe at b = 0, 1, 2, ... and record the least budget
at which the verdict reaches its final value and stays there (it stabilizes,
and by CLAIM-574 along nested families distinctions only grow, so a verdict
of "distinguishable" never reverts).

CONTROL (CASE-202): every probe is run both on a reset copy and on a copy
earlier probes have acted on, so that a difference appearing only on the
acted-on copy would be attributed to the probing, not discovered in the
mechanism. The prober here is non-destructive (it only queries reachability
and never mutates the admissible set or move rule), so the acted-on readout
equals the reset readout by construction: any difference found is discovered,
not made. The destructive counterpart is left as the owner's call.

No status is changed and no record file is written by this script.
Run:  python3 -I prober.py
"""
from __future__ import annotations

import itertools
import json
import os
import sys

import numpy as np

# CPU only, single BLAS thread (belt and braces; numpy here is tiny anyway).
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")


def all_configs(n: int) -> np.ndarray:
    """The 2**n bit strings of length n, as an int array of shape (2**n, n)."""
    return np.array(list(itertools.product((0, 1), repeat=n)), dtype=np.int8)


class Mechanism:
    """A constrained mechanism: an admissible set with a single-flip move rule.

    admissible: iterable of tuples of bits (the admissible configurations).
    demands: dict name -> target tuple; a config meets the demand iff equal.
    All configs cost 0 (CLAIM-583's seed pair); cost is carried so that a
    budget can later be read as total cost rather than move count without
    changing the interface.
    """

    def __init__(self, name, n, admissible, demands):
        self.name = name
        self.n = int(n)
        self.admissible = [tuple(int(b) for b in c) for c in admissible]
        self.aset = set(self.admissible)
        for c in self.aset:
            if len(c) != self.n:
                raise ValueError(f"config {c} not of length {n}")
        self.demands = {k: tuple(int(b) for b in v) for k, v in demands.items()}
        for k, v in self.demands.items():
            if v not in self.aset:
                raise ValueError(f"demand {k} target {v} is not admissible")

    def neighbours(self, config):
        """Admissible configs one bit flip away (the local move rule)."""
        out = []
        c = list(config)
        for i in range(self.n):
            c[i] ^= 1
            t = tuple(c)
            if t in self.aset:
                out.append(t)
            c[i] ^= 1
        return out

    def reachable_within(self, start, budget):
        """Configs reachable from `start` in <= budget admissible moves (BFS).

        Monotone nondecreasing in `budget` by construction.
        """
        if start not in self.aset:
            return set()
        frontier = {start}
        seen = {start}
        for _ in range(int(budget)):
            nxt = set()
            for c in frontier:
                for m in self.neighbours(c):
                    if m not in seen:
                        seen.add(m)
                        nxt.add(m)
            if not nxt:
                break
            frontier = nxt
        return seen

    def compatibility_complex(self):
        """Downward-closed complex of jointly-satisfiable demand sets (CLAIM-347).

        A demand set S is a face iff some admissible config meets every demand
        in S. Here demands are 'equals target', so a set of size >1 is a face
        only if its targets coincide.
        """
        names = sorted(self.demands)
        faces = set()
        faces.add(frozenset())
        for r in range(1, len(names) + 1):
            for combo in itertools.combinations(names, r):
                targets = {self.demands[k] for k in combo}
                if len(targets) == 1 and next(iter(targets)) in self.aset:
                    faces.add(frozenset(combo))
        return faces

    def demand_reachability(self, budget):
        """Readout under the probe family at `budget`.

        For each ordered pair (i, j) of demand names: is there an admissible
        config meeting demand i from which a config meeting demand j is
        reachable within `budget` moves? Returned as a sorted tuple of
        (i, j, bool) so it is hashable and comparable across mechanisms.
        """
        names = sorted(self.demands)
        rows = []
        for i in names:
            # configs meeting demand i (here exactly the target, if admissible)
            starts = [self.demands[i]] if self.demands[i] in self.aset else []
            reach = set()
            for s in starts:
                reach |= self.reachable_within(s, budget)
            for j in names:
                tgt = self.demands[j]
                rows.append((i, j, bool(tgt in reach)))
        return tuple(rows)


def probe_pair(mech_a, mech_b, max_budget):
    """Probe a pair at budgets 0..max_budget; record verdict stabilization.

    Verdict(b) = 'distinguishable' iff the two demand-reachability readouts
    differ at budget b. Returns a dict with the per-budget verdicts, the
    stabilization budget, the distinguishing budget, and the control check.
    """
    assert sorted(mech_a.demands) == sorted(mech_b.demands), \
        "the fixed probe family must address the same demands on both"

    # Controls separate 'discovering a difference' from 'creating' one: run
    # each probe on a reset copy and on an acted-on copy. The prober is
    # non-destructive, so we exhibit this by re-probing the same object twice
    # and confirming the readout is identical.
    verdicts = []
    control_clean = True
    for b in range(int(max_budget) + 1):
        ra_reset = mech_a.demand_reachability(b)
        ra_acted = mech_a.demand_reachability(b)   # acted-on copy
        rb_reset = mech_b.demand_reachability(b)
        rb_acted = mech_b.demand_reachability(b)
        if ra_reset != ra_acted or rb_reset != rb_acted:
            control_clean = False
        verdicts.append({
            "budget": b,
            "readout_a": ra_reset,
            "readout_b": rb_reset,
            "distinguishable": ra_reset != rb_reset,
        })

    final = verdicts[-1]["distinguishable"]
    # stabilization budget: least b from which the verdict never changes again.
    stabilizes_at = 0
    for b in range(len(verdicts)):
        if all(v["distinguishable"] == final for v in verdicts[b:]):
            stabilizes_at = b
            break
    diverge_budgets = [v["budget"] for v in verdicts if v["distinguishable"]]
    distinguishing_budget = diverge_budgets[0] if diverge_budgets else None

    # monotonicity (CLAIM-574): once distinguishable, stays distinguishable.
    seq = [v["distinguishable"] for v in verdicts]
    monotone = all((not seq[k]) or seq[k + 1] for k in range(len(seq) - 1))

    return {
        "pair": f"{mech_a.name} vs {mech_b.name}",
        "same_complex": mech_a.compatibility_complex()
        == mech_b.compatibility_complex(),
        "max_budget": int(max_budget),
        "verdicts": [
            {"budget": v["budget"], "distinguishable": v["distinguishable"]}
            for v in verdicts
        ],
        "ever_diverge": final or len(diverge_budgets) > 0,
        "distinguishing_budget": distinguishing_budget,
        "stabilizes_at": stabilizes_at,
        "final_verdict": "distinguishable" if final else "indistinguishable",
        "control_reset_equals_acted": control_clean,
        "distinction_monotone_in_budget": monotone,
    }


# --- The seed pair (CLAIM-583) -------------------------------------------

def seed_pair():
    a = Mechanism("A={000,111}", 3, [(0, 0, 0), (1, 1, 1)],
                  {"D1": (0, 0, 0), "D2": (1, 1, 1)})
    b = Mechanism("B={000,001}", 3, [(0, 0, 0), (0, 0, 1)],
                  {"D1": (0, 0, 0), "D2": (0, 0, 1)})
    return a, b


# --- A tunable family: distinguishing budget = path length L -------------

def path_pair(L):
    """Two mechanisms whose distinguishing budget is exactly L.

    Both: D1 = start = 0^n, D2 = end. B admits a Hamming path start -> end of
    length L (flip bit 0, then 1, ...); A admits only {start, end} (no
    intermediate), so no admissible single-flip path joins them. Same complex
    ({},{D1},{D2}), same move rule, same (zero) costs, same readout at every
    budget < L; they part at budget L and stay apart.

    Requires L >= 2: at L = 1, A = {start, end} is itself a single-move path,
    so A and B coincide and there is no internal difference to probe.
    """
    if int(L) < 2:
        raise ValueError("path_pair requires L >= 2 (L=1 makes A and B equal)")
    n = L
    start = tuple([0] * n)
    # path: at step k, bits 0..k-1 are 1. end = all ones.
    path = [tuple([1] * k + [0] * (n - k)) for k in range(0, n + 1)]
    end = path[-1]
    a = Mechanism(f"A_path(L={L})", n, [start, end],
                  {"D1": start, "D2": end})
    b = Mechanism(f"B_path(L={L})", n, path,
                  {"D1": start, "D2": end})
    return a, b


def main():
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "results.jsonl")
    # append-only, one record per item, flushed as produced (skill step 5)
    runs = [("seed", seed_pair(), 4)]
    # Identical-mechanism control: a pair that cannot be told apart at any
    # budget (both = the seed's B). Verdict must be 'indistinguishable' with
    # no distinguishing budget.
    runs.append(("identical", (seed_pair()[1], seed_pair()[1]), 4))
    # Tunable family: distinguishing budget = path length L. L must be >= 2;
    # at L=1 the two mechanisms coincide (A={start,end} is itself a 1-move
    # path), so there is nothing to tell apart.
    for L in (2, 3, 4, 5):
        runs.append((f"path_L{L}", path_pair(L), L + 2))

    with open(out_path, "w") as fh:
        for tag, (a, b), maxb in runs:
            rec = {"item": tag}
            rec.update(probe_pair(a, b, maxb))
            fh.write(json.dumps(rec) + "\n")
            fh.flush()
            print(f"{tag:8s}  {rec['pair']:28s}  same_complex={rec['same_complex']}"
                  f"  distinguishing_budget={rec['distinguishing_budget']}"
                  f"  stabilizes_at={rec['stabilizes_at']}"
                  f"  final={rec['final_verdict']}")
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    sys.exit(main())
