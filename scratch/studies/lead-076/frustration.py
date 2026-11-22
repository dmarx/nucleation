"""Structural frustration against operative thwarting, in a finite model.

LEAD-076, part 1 (QUESTION-131). An organization has a finite set of
attainable arrangements R and members i, each with an acceptance set A[i]
(where its demand is met) and a quiet set Q[i] (where it does not act toward
its demand; CLAIM-549's T_i, CLAIM-631's quiet region). A resolution rule
picks the arrangement from the members that are active and, optionally,
their weights and preferences.

Definitions used here (the assistant's, stated in the CASE):

- S is structurally frustrated when no r in R lies in every A[i], i in S
  (CLAIM-347: S not in the requirement complex K).
- At arrangement r, member i is unmet and acting when r not in A[i] and
  r not in Q[i] (CLAIM-631).
- i is operatively thwarted by j at the organization's outcome when i is
  unmet and acting there, and silencing j (removing j's push from the
  resolution, a counterfactual intervention) yields an outcome at which i
  is met. j is then a but-for thwarter of i. The same with a set of
  members silenced together gives a but-for thwarting set.

Outcomes are computed by iterating r <- rule(active(r)) from a start
arrangement to a fixed point; the resolution reads the demands of members
that are met (they maintain them) or unmet and acting, and not those of
members unmet and quiet. All the constructions here reach a fixed point in
at most two steps; outcome() raises if a run cycles.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from itertools import combinations
from typing import Callable, Dict, FrozenSet, Hashable, Iterable, List, Optional, Sequence, Tuple

Arr = Hashable
Member = Hashable


@dataclass
class Org:
    R: Tuple[Arr, ...]
    A: Dict[Member, FrozenSet[Arr]]
    Q: Dict[Member, FrozenSet[Arr]]
    weight: Dict[Member, float] = field(default_factory=dict)
    # pref[i][r]: strength of i's preference for r beyond its acceptance set
    pref: Dict[Member, Dict[Arr, float]] = field(default_factory=dict)

    @property
    def members(self) -> Tuple[Member, ...]:
        return tuple(self.A)

    def w(self, i: Member) -> float:
        return self.weight.get(i, 1.0)


def in_K(org: Org, S: Iterable[Member]) -> bool:
    """S is in the requirement complex: some arrangement meets all of S."""
    S = tuple(S)
    return any(all(r in org.A[i] for i in S) for r in org.R)


def frustrated(org: Org, S: Iterable[Member]) -> bool:
    return not in_K(org, S)


def minimal_nonfaces(org: Org) -> List[FrozenSet[Member]]:
    out = []
    ms = org.members
    for k in range(1, len(ms) + 1):
        for S in combinations(ms, k):
            if frustrated(org, S) and all(in_K(org, T) for T in combinations(S, k - 1)):
                out.append(frozenset(S))
    return out


def active(org: Org, r: Arr, silenced: FrozenSet[Member] = frozenset()) -> FrozenSet[Member]:
    """The members whose demands the resolution reads at r: every member
    not silenced, except one that is unmet and quiet there. A met member
    keeps its demand in force (maintenance); an unmet, quiet one has
    dropped it for now."""
    return frozenset(i for i in org.members
                     if i not in silenced and (r in org.A[i] or r not in org.Q[i]))


def unmet_acting(org: Org, r: Arr) -> FrozenSet[Member]:
    return frozenset(i for i in org.members if r not in org.A[i] and r not in org.Q[i])


# ---- resolution rules ------------------------------------------------------

Rule = Callable[[Org, FrozenSet[Member]], Arr]


def rule_count_max(org: Org, P: FrozenSet[Member]) -> Arr:
    """Joint-satisfaction-seeking: the arrangement meeting the greatest
    weighted count of active demands; ties broken by order in R."""
    best, bestv = org.R[0], -1.0
    for r in org.R:
        v = sum(org.w(i) for i in P if r in org.A[i])
        if v > bestv + 1e-12:
            best, bestv = r, v
    return best


def rule_authority(org: Org, P: FrozenSet[Member]) -> Arr:
    """Each active member pushes for its most preferred arrangement inside
    its acceptance set, with its weight; the arrangement with the greatest
    weighted push wins (ties by order in R). Preference beyond acceptance
    counts here, so a weighty member can pick an arrangement that fails
    another although a jointly acceptable one exists."""
    score = {r: 0.0 for r in org.R}
    for i in P:
        acc = [r for r in org.R if r in org.A[i]]
        if not acc:
            continue
        pi = org.pref.get(i, {})
        top = max(acc, key=lambda r: (pi.get(r, 0.0), -org.R.index(r)))
        score[top] += org.w(i)
    best = max(org.R, key=lambda r: (score[r], -org.R.index(r)))
    return best


def rule_fixed(default: Arr) -> Rule:
    """A resolution that does not read the demands at all."""
    def rule(org: Org, P: FrozenSet[Member]) -> Arr:  # noqa: ARG001
        return default
    return rule


def outcome(org: Org, rule: Rule, start: Optional[Arr] = None,
            silenced: FrozenSet[Member] = frozenset(), max_iter: int = 50) -> Arr:
    """Iterate r <- rule(active(r)) to a fixed point (or first repeat).

    Silenced members do not push. Their demands still define who is met.
    """
    r = org.R[0] if start is None else start
    seen = [r]
    for _ in range(max_iter):
        nxt = rule(org, active(org, r, silenced))
        if nxt == r:
            return r
        if nxt in seen:
            raise RuntimeError(f"resolution cycles: {seen + [nxt]}")
        seen.append(nxt)
        r = nxt
    raise RuntimeError("no fixed point")


def but_for_thwarters(org: Org, rule: Rule, i: Member, start: Optional[Arr] = None,
                      max_size: int = 1) -> List[FrozenSet[Member]]:
    """Minimal sets of other members whose silencing gets i met, provided i
    is unmet and acting at the actual outcome. Empty list: i is not
    operatively thwarted by any process (up to max_size)."""
    r0 = outcome(org, rule, start)
    if i not in unmet_acting(org, r0):
        return []
    others = [j for j in org.members if j != i]
    found: List[FrozenSet[Member]] = []
    for k in range(1, max_size + 1):
        for J in combinations(others, k):
            J = frozenset(J)
            if any(F <= J for F in found):
                continue
            r1 = outcome(org, rule, start, silenced=J)
            if r1 in org.A[i]:
                found.append(J)
    return found


def thwarted(org: Org, rule: Rule, start: Optional[Arr] = None, max_size: int = 1) -> Dict[Member, List[FrozenSet[Member]]]:
    return {i: but_for_thwarters(org, rule, i, start, max_size) for i in org.members
            if but_for_thwarters(org, rule, i, start, max_size)}


# ---- the constructions -----------------------------------------------------

def fs(*xs):
    return frozenset(xs)


def c1_frustration_quiet() -> Tuple[Org, Rule]:
    """Frustration without thwarting, the quiet member (CLAIM-631 item 3,
    reproduced): R={x,y}, A1={x}, A2={y}, Q1={y}, Q2={x}."""
    org = Org(R=("x", "y"), A={1: fs("x"), 2: fs("y")}, Q={1: fs("y"), 2: fs("x")})
    return org, rule_count_max


def c2_frustration_idle() -> Tuple[Org, Rule]:
    """Frustration with an unmet, acting member and no but-for process: the
    resolution never reads the demands (it always yields y). Member 1 is
    unmet and acting; silencing member 2, or deleting member 2's demand,
    leaves 1 unmet. The frustration is real and causally idle."""
    org = Org(R=("x", "y"), A={1: fs("x"), 2: fs("y")}, Q={1: fs("x"), 2: fs("y")})
    return org, rule_fixed("y")


def c3_minimal_conflict(n: int = 3) -> Tuple[Org, Rule]:
    """Frustration that shows up as thwarting: a minimal conflict of n
    members (each pair-free: every n-1 of them is jointly satisfiable, all n
    are not). Arrangements r_k meet everyone but k. Every member acts
    whenever unmet. Under the count-maximizing rule exactly one member is
    unmet, and each other member is separately a but-for thwarter."""
    R = tuple(f"r{k}" for k in range(n))
    A = {i: frozenset(f"r{k}" for k in range(n) if k != i) for i in range(n)}
    Q = {i: A[i] for i in range(n)}
    return Org(R=R, A=A, Q=Q), rule_count_max


def c4_pair_inside_larger() -> Tuple[Org, Rule]:
    """A minimal conflicting pair {i, j} whose pairwise attribution fails:
    i wants x; j, k and l want y. {i, j} is a minimal non-face, but
    silencing j alone leaves y the winner, so j is not a but-for thwarter
    of i; the minimal but-for sets are the pairs of {j, k, l} (silencing
    two leaves a tie, which the rule breaks toward x)."""
    org = Org(R=("x", "y"),
              A={"i": fs("x"), "j": fs("y"), "k": fs("y"), "l": fs("y")},
              Q={"i": fs("x"), "j": fs("y"), "k": fs("y"), "l": fs("y")})
    return org, rule_count_max


def c5_thwarting_without_frustration() -> Tuple[Org, Rule]:
    """Thwarting without frustration, governance-induced: R={x,y,z},
    A1={x,z}, A2={y,z}, so z meets both and {1,2} is in K. Member 2 has
    weight 2 and prefers y within its acceptance set. Under the authority
    rule y wins; member 1 is unmet and acting; silencing 2 gets 1 met.
    Under the count-maximizing rule the same organization reaches z and no
    one is thwarted."""
    org = Org(R=("x", "y", "z"), A={1: fs("x", "z"), 2: fs("y", "z")},
              Q={1: fs("x", "z"), 2: fs("y", "z")}, weight={1: 1.0, 2: 2.0},
              pref={1: {"x": 1.0}, 2: {"y": 1.0}})
    return org, rule_authority


def c6_sentry_static() -> Tuple[Org, Rule]:
    """The sentry of CASE-153 as a static organization (first version,
    inspection physically safe). Arrangements: (posture, evidence) pairs
    shelter-blind, protect-inspect, engage-inspect, engage-blind. The
    sentry's demand: no exposure to harm while danger is possible, met by
    shelter-blind and protect-inspect (inspection is safe). The
    investigator's demand: diagnostic evidence, met by protect-inspect and
    engage-inspect. protect-inspect meets both, so the pair is not
    frustrated. The sentry is vigilant (never quiet). With authority and a
    preference for shelter-blind the
    sentry thwarts the investigator; silencing the sentry's push (a
    protected investigator) gets it met."""
    R = ("shelter-blind", "protect-inspect", "engage-inspect", "engage-blind")
    org = Org(R=R,
              A={"sentry": fs("shelter-blind", "protect-inspect"),
                 "investigator": fs("protect-inspect", "engage-inspect")},
              Q={"sentry": fs(),  # vigilant: pushes whatever the arrangement
                 "investigator": fs("protect-inspect", "engage-inspect")},
              weight={"sentry": 2.0, "investigator": 1.0},
              pref={"sentry": {"shelter-blind": 1.0}, "investigator": {"engage-inspect": 1.0}})
    return org, rule_authority


CONSTRUCTIONS = {
    "C1 frustration, quiet member (CLAIM-631 item 3)": c1_frustration_quiet,
    "C2 frustration, unmet acting member, idle": c2_frustration_idle,
    "C3 minimal conflict of 3, responsive rule": lambda: c3_minimal_conflict(3),
    "C3' minimal conflict of 5, responsive rule": lambda: c3_minimal_conflict(5),
    "C4 minimal pair inside a larger organization": c4_pair_inside_larger,
    "C5 thwarting without frustration (authority)": c5_thwarting_without_frustration,
    "C5' same organization, count-max rule": lambda: (c5_thwarting_without_frustration()[0], rule_count_max),
    "C6 sentry, static (authority)": c6_sentry_static,
    "C6' sentry, static, count-max rule": lambda: (c6_sentry_static()[0], rule_count_max),
}


def report() -> str:
    lines = []
    for name, make in CONSTRUCTIONS.items():
        org, rule = make()
        S = org.members
        r0 = outcome(org, rule)
        th = thwarted(org, rule, max_size=len(S) - 1)
        lines.append(f"## {name}")
        lines.append(f"- whole set frustrated: {frustrated(org, S)}; minimal non-faces: "
                     f"{sorted(sorted(map(str, m)) for m in minimal_nonfaces(org))}")
        lines.append(f"- outcome: {r0}; unmet and acting there: {sorted(map(str, unmet_acting(org, r0)))}")
        if th:
            for i, Js in th.items():
                lines.append(f"- {i} thwarted; minimal but-for sets: {sorted(sorted(map(str, J)) for J in Js)}")
        else:
            lines.append("- no member operatively thwarted (no but-for set)")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    print(report())
