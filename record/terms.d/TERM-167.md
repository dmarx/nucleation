---
number: 167
status: Proposed
formerly:
- TERM-tmpz28l1
title: 'viability kernel of reorganization readiness, of an organization for
  a declared family of contingencies, budget and deadline: the states from
  which it can keep operating within its core requirements while preserving,
  at every moment, an affordable route that stays within transition safeguards
  to some viable alternative organization after any declared contingency'
version: 1
tags:
- society-and-governance
- control-theory
- mathematics
date: '2026-11-22'
line: realizability
complements:
- TERM-115
summary: A36 of the exchange "Explain First Contact RL" (ChatGPT, second share
  of 2026-11-22), answering the owner's U19, which asked A to make formal
  A34's sentence "The deepest achievement of ecological governance is not
  maintaining a particular equilibrium. It is maintaining the capacity for
  viable reorganization when the equilibrium becomes inadequate." The wording
  is A's (ChatGPT, in the exchange of 2026-11-22); adopting it is the owner's
  call.
---

<!-- inactive-ok-file: CLAIM-916 — Proposed; cited in this filing of 2026-11-22 (second share) -->

# TERM-167: viability kernel of reorganization readiness, of an organization for a declared family of contingencies, budget and deadline: the states from which it can keep operating within its core requirements while preserving, at every moment, an affordable route that stays within transition safeguards to some viable alternative organization after any declared contingency

## Definition (A36)

State y = (x, g, c): the ecosystem, its operative governance, and its
reorganizational capacities, each with its own dynamics. For a
contingency ω, V_ω is the union over post-contingency governance regimes
j of the viability kernels Viab_{F_ω^j}(K_ω^j). C_ω(B, τ) is the states
from which some admissible policy reaches V_ω by time τ, at cost within
B, staying in K_safe on the way. Then

  M(B, τ, Ω) = K_core ∩ ⋂_{ω ∈ Ω} T_ω⁻¹(C_ω(B, τ)),

  V_reorg = Viab_{F_0}(M(B, τ, Ω)).

A state is in V_reorg when ordinary operation can keep the organization
in M indefinitely.

## Against the record

- Viability kernel: [THEORY-134](../theory.d/THEORY-134.md). Stability is not viability: [CLAIM-079](../claims.d/CLAIM-079.md).
- Keeping an effective regime and keeping the capacity to govern among
  regimes are different achievements: [CLAIM-099](../claims.d/CLAIM-099.md), and [CLAIM-025](../claims.d/CLAIM-025.md).
- A transition's threshold can exceed both endpoints' costs: [CLAIM-571](../claims.d/CLAIM-571.md)
  and [CLAIM-569](../claims.d/CLAIM-569.md). Feasibility at a budget is not reachability at it:
  [CLAIM-560](../claims.d/CLAIM-560.md).
- A36 §5's example, A held at cost 1, B at cost 1, the route through M at
  cost 3, with each period's budget set to the last period's peak spend,
  is [CLAIM-577](../claims.d/CLAIM-577.md) exactly: efficient holding destroys the route.
- Permitted, actuated, affordable, reliable and sustainable motions:
  [CLAIM-589](../claims.d/CLAIM-589.md).
- Readiness as the probability of an effective response by a deadline:
  [TERM-115](TERM-115.md). This term is its set-valued, worst-case-over-Ω counterpart,
  made a viability requirement.
- What K_core must hold, fixed by what realizes the capacity: [CLAIM-916](../claims.d/CLAIM-916.md).
- Correctability by others, which A36 §8 adds as a constraint on
  admissible policies: [CLAIM-462](../claims.d/CLAIM-462.md) and [TERM-085](TERM-085.md).

## Limits

- A36 says that its conditional proposition (a state in V_reorg keeps,
  along a maintained trajectory, a route after each contingency) is "an
  immediate consequence of the construction, not a new empirical
  theorem". It is, so no claim is filed for it.
- The ∀ω ∃π order assumes the contingency is observed in time. Under
  partial observation the policies must agree on contingencies that
  cannot yet be told apart (A36 says so). A contingency that recurs during
  recovery needs a robust kernel.
- K_ω must be fixed independently of the current arrangement, or every
  arrangement is viable by its own standards (A36 says so). This is
  [THEORY-134](../theory.d/THEORY-134.md)'s requirement that the constraint set be fixed independently
  of the dynamics.

<!-- inactive-ok-file: CLAIM-1135 CLAIM-1070 — Proposed; filed in this filing of 2026-11-23 (third share) -->

## Note of 2026-11-23: a second-order version

A44 §5 of the third share extends this term from contingencies to
changes of the demand specification itself. The state is (x, θ, c),
with c the capacities that make revising θ feasible. M_D is the states
whose actual policies meet the current demands D with declared
reliability. T_{D→D′}^{B,H} is the states with an affordable, safe route
to M_{D′} within H. Then M_adaptive = M_D ∩ ⋂_{D′∈𝔇} T_{D→D′}^{B,H}, and
V_adaptive = Viab_{F_aug}(M_adaptive): "the viability kernel of the
capacity to remain ready for current demands while retaining affordable
routes to readiness under alternative demands." A42 §6 states the design
problem that uses it: minimize operating, maintenance and
reconfiguration costs subject to [TERM-115](TERM-115.md) readiness and this kernel.
[CLAIM-1135](../claims.d/CLAIM-1135.md) and [CLAIM-1070](../claims.d/CLAIM-1070.md) cite both.

## Note of 2026-11-23: the manuscript governance-of-possibility

<!-- inactive-ok-block: ADR-144 — Proposed; the work this note names -->
Restatement. A48 §8 of the owner's manuscript ([ADR-144](../decisions.d/ADR-144.md)) restates this
term's second-order kernel of the note above, S = (x, θ, c), M_adaptive and
V_adaptive, and names three achievements, M_D ⊇ M_adaptive ⊇ V_adaptive. It
secures one retuning: nothing in the construction requires readiness again
after a switch to a new demand unless the family of demands is closed under
retuning, which the manuscript leaves unstated.

## Note of 2026-11-23: a gap of the manuscript governance-of-possibility

Qualification, the assistant's. A gap of the manuscript governance-of-possibility, §8.5 (GA2). The second-order kernel of the note "a second-order version" above can be read with two sets of evolutions. Its M_D is taken under "actual policies", while Viab_{F_aug} asks whether some evolution stays in M_adaptive ([THEORY-134](../theory.d/THEORY-134.md)). Write V_π for the kernel of the closed loop under the policy the regime follows, and V_adm for the kernel when F_aug admits every evolution an admissible revision of policy produces. A viability kernel can only grow when more evolutions are admitted, so V_π ⊆ V_adm ⊆ M_adaptive.

The manuscript's separating case holds for V_π only. Under the peak budget rule, (A, budget 3) leaves M_adaptive after one period of holding ([CLAIM-577](../claims.d/CLAIM-577.md)), so it is outside V_π. If F_aug admits a drill each period at the transition's threshold, the budget stays at 3 ([CLAIM-878](../claims.d/CLAIM-878.md): "A drill each period holds the budget"); if it admits a revision of the budget rule to a floor at 3, the budget stays at 3 as well. Either way (A, 3) is in V_adm, provided the drill leaves D met while it runs. If revising the budget rule is admissible from (A, budget 1) and takes effect within H, that state is in T_{D→D′} on the same reading, and the manuscript's state separating M_D from M_adaptive fails too; a drill at 3 is not affordable from it ([CLAIM-577](../claims.d/CLAIM-577.md)).

So V_adm \ V_π is the set of states the arrangement loses by keeping its policy and could keep by changing it: what a change of governance can save. The term should say which kernel it means, or carry both. This qualifies the audit in record/curation.d/2026/11/23/031842.md, which found that the manuscript's §8 "passes by a separating case (a Regime I state is in M_adaptive and not in V_adaptive)": it passes for the kernel under the policy followed, and for the kernel under admissible revisions only if the drill and the floor are left out of F_aug. The note is the assistant's (Claude, in this session); adopting it is the owner's call.
