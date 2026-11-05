---
number: 560
status: Proposed
formerly:
- CLAIM-tmp4rtpa
title: 'The resource-indexed compatibility filtration and the resource-indexed reachability filtration of one architecture both grow with the budget and neither determines the other: a budget can make a transition between configurations already feasible affordable while adding no jointly satisfiable set of demands, and a configuration can be feasible at a budget at which it is unreachable from the start'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a budget increase, with the architecture, the
  demands and the resource requirement fixed, that removes a face of the
  budgeted complex or a pair from the reachability relation; or, in the
  three-state construction, a face entering the complex at budget 3 for the
  declared demands, a path from s₁ to s₃ below 3, or s₃ reachable from s₁
  at a budget in [1, 3). Not defeated by a demand that only the
  intermediate state meets, which makes the complex gain a vertex at 3:
  the claim says a budget can add a transition without a face, not that it
  always does.
tags:
- mathematics
- complex-systems
- operations-research
date: '2026-11-05'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-586
- CLAIM-571
complements:
- CLAIM-567
- CLAIM-591
uses:
- TERM-114
summary: >-
  A's proposal, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 3 §3: beside the
  compatibility filtration K_z(b) of CLAIM-586 there is a reachability
  filtration, and "A system can acquire new reachable transitions without
  adding any new feasible endpoint configurations. Conversely, a new
  configuration may become feasible while remaining unreachable from the
  initial state." Demonstrated on A's own three-state example, endpoints
  needing capacity 1 and the intermediate 3, with one demand on each
  endpoint, checked by the filer: on [1, 3) both endpoints are feasible and
  neither reaches the other; at 3 they become mutually reachable and the
  complex does not change. The second half is already in CLAIM-571;
  what is new is the pairing. The wording is A's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-563 CLAIM-571 CLAIM-583 CLAIM-585 CLAIM-586 CLAIM-591 THEORY-1420 — Proposed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-560: The resource-indexed compatibility filtration and the resource-indexed reachability filtration of one architecture both grow with the budget and neither determines the other: a budget can make a transition between configurations already feasible affordable while adding no jointly satisfiable set of demands, and a configuration can be feasible at a budget at which it is unreachable from the start

## The claim

A (Response 3 §3): "Your PR already gives a resource-indexed compatibility
filtration: K_z(b_1)⊆K_z(b_2) when b_1⪯b_2. But we can construct a second
filtration: resource-bounded reachability." A's table:

| structure | what appears as the budget increases |
|---|---|
| compatibility filtration K_z(b) | "New combinations of demands become jointly satisfiable" |
| reachability filtration | "New transitions between existing feasible states become affordable" |

"They answer different questions. A system can acquire new reachable
transitions without adding any new feasible endpoint configurations.
Conversely, a new configuration may become feasible while remaining
unreachable from the initial state."

**The two filtrations.** Fix an architecture with configurations Q,
moves between them, a capacity requirement r and demands D_i. Let
Q(b) = {q : r(q) ≤ b}.

- **Compatibility**: K(b), the sets of demands some q ∈ Q(b) meets
  together. It grows with b ([CLAIM-586](CLAIM-586.md)).
- **Reachability**: R(b), the pairs (q, q′) joined by a sequence of moves
  through Q(b). It grows with b, since a path within Q(b) lies within Q(b′)
  for b ≤ b′; (q, q′) enters at [CLAIM-571](CLAIM-571.md)'s threshold B*(q, q′).

K(b) depends on Q(b) and the demands only; R(b) on how Q(b) is joined by
moves. Neither fixes the other.

**A's example, with demands (the demands are the filer's).** Three states
in a row, s₁ — s₂ — s₃, with moves between neighbours both ways; r(s₁) =
r(s₃) = 1 and r(s₂) = 3, A's "both endpoint configurations require
capacity 1, but moving between them requires passing through a state
demanding capacity 3." Demands D₁ = {s₁} and D₃ = {s₃}.

| budget | Q(b) | K(b) | R(b) |
|---|---|---|---|
| b < 1 | ∅ | no faces | ∅ |
| 1 ≤ b < 3 | {s₁, s₃} | {∅, {1}, {3}} | ∅ |
| b ≥ 3 | {s₁, s₂, s₃} | {∅, {1}, {3}} | every ordered pair |

Checked by the filer by enumeration.

- **A transition without a face.** At b = 3, s₁ and s₃ become mutually
  reachable, and K(b) is unchanged.
- **Feasible and unreachable.** On [1, 3), s₃ is feasible ({3} is a face)
  and unreachable from s₁. This half is [CLAIM-571](CLAIM-571.md)'s, whose example has
  both endpoints feasible at 1.0 and the threshold at 1.3.

**Where persistence sees it.** With moves reversible at equal cost, R(b)
is the partition of Q(b) into the components the moves join, so the
reachability filtration is the zero-dimensional part of the sublevel-set
persistence of r: A's "two disconnected regions merge when the budget
reaches 3", and the merge-level reading of Mirth et al. ([THEORY-1420](../theory.d/THEORY-1420.md))
held in [CLAIM-571](CLAIM-571.md). With one-way moves it is not ([CLAIM-591](CLAIM-591.md)).

## What it does not say

- **That a transition never comes with a face.** A demand met only by s₂
  would enter K(b) at 3 with the transition; which demands are declared
  decides that.
- **That either filtration is the finer.** Each can change where the other
  does not; [CLAIM-583](CLAIM-583.md) shows reachability can differ where the complex
  agrees at every budget.
- **Anything for several resources or other resource types.** Both
  filtrations are over one capacity; with several, the index is a partial
  order ([CLAIM-585](CLAIM-585.md)), and with cumulative costs reachability within a
  budget is not even closed under composition ([CLAIM-563](CLAIM-563.md)).
- **A's appraisal.** A calls the pairing "one of the most promising
  mathematical features of the entire proposal". The claim is only the
  separation.
