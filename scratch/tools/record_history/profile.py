# scratch/tools/record_history/profile.py
"""Per-entry developmental profiles from the event table (A34, pilot 1).

An event is substantive when it is not mechanical, not a bot's, and not
part of a sweep (a commit touching at least `sweep_breadth` entries).
Every other touch is maintenance: the cost of keeping the entry.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

DAY = 86400
QUADRANTS = ("developing nucleus", "established anchor", "unresolved churn", "dormant structure")


@dataclass
class Params:
    now: int  # reference time, seconds
    sweep_breadth: int = 250
    reactivation_days: int = 14
    windows: tuple[int, int] = (7, 30)


def substantive(r: dict, p: Params) -> bool:
    return r["kind"] != "mechanical" and not r["bot"] and r.get("breadth", 1) < p.sweep_breadth


def quadrant(days_since_prose: float, new_dependents: int, stable_days: float, generative: int) -> str:
    stable = days_since_prose >= stable_days
    gen = new_dependents >= generative
    return {(False, True): "developing nucleus", (True, True): "established anchor",
            (False, False): "unresolved churn", (True, False): "dormant structure"}[(stable, gen)]


def profiles(rows: list[dict], p: Params) -> dict[str, dict]:
    rows = [r for r in rows if r["time"] <= p.now]
    w_short, w_long = p.windows
    info: dict[str, dict] = {}
    commits = defaultdict(lambda: defaultdict(bool))  # code -> commit -> any substantive
    edges: dict[str, set[tuple[str, str]]] = defaultdict(set)  # source -> live (field, target)
    first_edge: dict[tuple[str, str], int] = {}  # (source, target) -> first time
    activity = defaultdict(list)  # code -> times of own substantive events or incoming firsts
    subst_times = defaultdict(list)  # code -> (time, commit) of substantive touches

    for r in rows:
        code, t = r["code"], r["time"]
        e = info.setdefault(code, {"code": code, "scheme": r["scheme"], "status": "", "created": t,
                                   "prose_revisions": 0, "prose_churn": 0, "last_prose": t,
                                   "status_changes": 0})
        s = substantive(r, p)
        commits[code][r["commit"]] |= s
        k = r["kind"]
        if k == "created":
            e["created"], e["status"], e["last_prose"] = t, r.get("status", ""), t
        elif k == "status":
            e["status"] = r["new"]
            e["status_changes"] += s
        elif k == "prose" and s:
            e["prose_revisions"] += 1
            e["prose_churn"] += r["churn"]
            e["last_prose"] = t
        elif k in ("relation_add", "relation_remove"):
            tgt = r["target"]
            if tgt != code:
                (edges[code].add if k == "relation_add" else edges[code].discard)((r["field"], tgt))
                if k == "relation_add" and (code, tgt) not in first_edge:
                    first_edge[(code, tgt)] = t
                    activity[tgt].append(t)
        if s:
            activity[code].append(t)
            subst_times[code].append((t, r["commit"]))

    incoming = defaultdict(set)
    for src, es in edges.items():
        for _, tgt in es:
            incoming[tgt].add(src)
    firsts = defaultdict(list)
    for (src, tgt), t in first_edge.items():
        firsts[tgt].append(t)

    out = {}
    for code, e in info.items():
        neighbours = incoming[code] | {t for _, t in edges[code]}
        neighbours.discard(code)
        since = p.now - w_long * DAY
        neigh = sum(len({c for t, c in subst_times[n] if t > since}) for n in neighbours)
        acts = sorted(activity[code])
        gaps = sum(1 for a, b in zip(acts, acts[1:]) if b - a >= p.reactivation_days * DAY)
        ft = [t for t in firsts[code]]
        out[code] = {
            "code": code, "scheme": e["scheme"], "status": e["status"],
            "created_day": e["created"] // DAY, "age_days": (p.now - e["created"]) // DAY,
            "prose_revisions": e["prose_revisions"], "prose_churn": e["prose_churn"],
            "days_since_prose": (p.now - e["last_prose"]) // DAY,
            "status_changes": e["status_changes"],
            "maintenance_commits": sum(1 for v in commits[code].values() if not v),
            "substantive_commits": sum(1 for v in commits[code].values() if v),
            "in_degree": len(incoming[code]), "out_degree": len(edges[code]),
            f"new_dependents_{w_short}d": sum(1 for t in ft if t > p.now - w_short * DAY),
            f"new_dependents_{w_long}d": sum(1 for t in ft if t > since),
            "latency_days": (min(ft) - e["created"]) // DAY if ft else None,
            "reactivations": gaps,
            f"neighbourhood_{w_long}d": neigh,
        }
    return out
