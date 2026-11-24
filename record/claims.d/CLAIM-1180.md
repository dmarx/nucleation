---
number: 1180
status: Proposed
formerly:
- CLAIM-tmpv0azx
title: "With one capacity that can be brought to bear at every configuration, a reserve held at budget B keeps every transition whose threshold is at most B, while a redesign lowers only the thresholds whose least-peak path can use the redesigned route, so a redesign that lets the reserve fall from θ − h to θ′ − h keeps the redesigned transition and loses every other transition whose threshold lies above θ′ and whose least-peak path does not use the redesign"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation or the check. Or, in an architecture with one
  capacity applicable at every configuration: a transition whose threshold
  exceeds the budget that is kept, or a threshold that a redesign lowers
  although no least-peak path to it uses the redesigned route. Not defeated
  by architectures in which a reserve has a location (CLAIM-579) or which
  have several resources (CLAIM-585). The claim does not cover them.
tags:
- operations-research
- mathematics
- society-and-governance
date: '2026-11-23'
line:
- readiness
- realizability
rests_on:
- CLAIM-571
- CLAIM-577
- CLAIM-1099
summary: >-
  The manuscript governance-of-possibility's join JC5 (§9.4, §9.8): "a
  redesign is specific to one transition and a reserve is not". Filed at the
  owner's ruling of 2026-11-23. It is stated here for one capacity usable
  anywhere, the condition under which "a reserve serves any" holds. Checked
  with python3 -I. Integrated by the account [SYNTHESIS-124](../syntheses.d/SYNTHESIS-124.md). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---

<!-- inactive-ok-file: CLAIM-1099 CLAIM-1093 CLAIM-878 SYNTHESIS-124 — Proposed; the premise, the claim it qualifies, the drill, and the account filed with this claim -->

# CLAIM-1180: With one capacity that can be brought to bear at every configuration, a reserve held at budget B keeps every transition whose threshold is at most B, while a redesign lowers only the thresholds whose least-peak path can use the redesigned route, so a redesign that lets the reserve fall from θ − h to θ′ − h keeps the redesigned transition and loses every other transition whose threshold lies above θ′ and whose least-peak path does not use the redesign

## The derivation

For a fixed architecture and one capacity, the threshold of a transition
from A to X is the least, over admissible paths, of the peak requirement
along the path ([CLAIM-571](CLAIM-571.md)). It is affordable at budget B exactly when its
threshold is at most B. Under [CLAIM-577](CLAIM-577.md)'s rule the budget falls to the
holding cost h after one period spent holding, unless something keeps it
up.

1. **A reserve.** A budget held at B, by a floor, a committed reserve or a
   drill each period ([CLAIM-878](CLAIM-878.md)), keeps every X whose threshold from A is
   at most B, whatever X is. This holds if the capacity can be used at
   every configuration on the path.
2. **A redesign.** Adding configurations or connections adds paths. The
   least peak over a larger set of paths can only fall. It falls for X
   only if some new least-peak path to X uses an added element. Every
   other threshold stays as it was.
3. **The trade.** A redesign that lowers A → B from θ to θ′ lets the
   reserve fall from θ − h to θ′ − h for A → B ([CLAIM-1099](CLAIM-1099.md)). Take an X
   whose threshold lies in (θ′, θ] and whose least-peak path does not use
   the redesign. The reserve θ − h keeps it, and the reserve θ′ − h loses
   it. Under [CLAIM-577](CLAIM-577.md)'s rule only outside money of at least the
   difference restores it.

## The check

With python3 -I, on the configurations of the manuscript's §9:

- A, B and C are held at 1, and M at 3, on A → M → B. The redesign is a
  staged path A → S1 → S2 → B, with S1 and S2 at 2. C is reached over
  A → N → C, with N at 2.5.
- Least peaks before the redesign: A → B 3, A → C 2.5. After: A → B 2,
  A → C 2.5.
- A budget of 3 keeps B and C. A budget of 2 keeps B and loses C.
- A target C2, reachable over N or from S2, has its threshold lowered
  from 2.5 to 2 by the redesign. A redesign serves every transition whose
  least-peak path can use it.
- Under the peak rule, budgets with no reserve fall to 1 at once. A drill
  at 2 or a floor at 2 holds 2, and C is lost. A floor at 3 holds 3, and C
  is kept.

## Admission ([ADR-075](../decisions.d/ADR-075.md), step 5)

**Route: a derivation, with a discriminating prediction.**

- **The derivation.** [CLAIM-1099](CLAIM-1099.md) is about the redesigned transition
  alone: redesign "lowers the reserve a transition needs by the fall in
  its threshold". [CLAIM-1093](CLAIM-1093.md) says reserve and redesign are distinct
  routes. Neither says what trading reserve for redesign does to the
  transitions that were not redesigned. Steps 2 and 3 say it.
- **The discriminating prediction.** Take two regimes that both keep the
  redesigned transition: one with the full reserve, one with the redesign
  and the smaller reserve. They differ on a demand nobody named when the
  redesign was chosen, whose route has a threshold in (θ′, θ] and does
  not use the redesign. The full reserve meets it. The other regime meets
  it only with outside money. The manuscript's model, which the record does
  not yet hold (gap GC1), reports this. Regime II's reserve covers C's
  threshold of 2.5, and the harm lasts about 6.1 periods. Regimes III-b and
  IV last about 15.3 periods with outside money, and all 120 without it.
- **The free parameter, closed.** "A reserve serves any" holds only for
  one capacity that can be used at every configuration. Where a reserve
  has a location, "an organization can hold ample slack and still be
  pinned" ([CLAIM-579](CLAIM-579.md)). With several resources, the sufficient budgets form
  an upward-closed set that can be non-convex ([CLAIM-585](CLAIM-585.md)). In either case
  a reserve also serves only some transitions, and this claim says
  nothing about them.

## What it does not say

- Not which to choose. That needs the contingencies' probabilities and
  losses weighed against the reserve's cost ([QUESTION-395](../questions.d/QUESTION-395.md)).
- Not that redesign is the worse route. It keeps the redesigned
  transition at a smaller reserve. [LEAD-230](../leads.d/LEAD-230.md) would test how the
  ranking changes with several resources and contingencies.

## The join

The manuscript governance-of-possibility, §9.4 and §9.8, join JC5. Filed
at the owner's ruling of 2026-11-23. The account [SYNTHESIS-124](../syntheses.d/SYNTHESIS-124.md)
integrates it.

## Note of 2026-11-24: the exchange 'Memes, Contracts, and Systemic Normativity', A53

A53: "The claim's derivation concerns previously affordable transitions whose thresholds lie between the reduced and original reserve limits. The title should explicitly preserve that restriction rather than imply that reducing a reserve newly eliminates transitions that were never affordable in the first place." Checked against the title: a reserve falling from θ − h to θ′ − h "loses every other transition whose threshold lies above θ′", which takes in thresholds above θ, never kept at the old reserve either. The narrowing is to thresholds above θ′ and at most θ. It is a correction of wording, not of the derivation, and is due before a ruling. The note is the assistant's (Claude, in this session), reporting A's (ChatGPT's) text; adopting either is the owner's call. No status change.
