---
number: 167
status: Proposed
formerly:
- TERM-tmpz28l1
title: 'reorganization viability kernel'
statement: >-
  viability kernel of reorganization readiness, of an organization for a
  declared family of contingencies, budget and deadline: the states from
  which it can keep operating within its core requirements while preserving,
  at every moment, an affordable route that stays within transition
  safeguards to some viable alternative organization after any declared
  contingency
version: 3
history:
- version: 2
  date: '2026-11-26'
  note: >-
    Dated note of 2026-11-26 from the exchange "Alignment consequences
    brainstorm" (ChatGPT, 2026-11-26): A2 §6 and A4 §1 read for AI control
    at the owner's U2; A4's fourth achievement mapped to held entries. The
    definition is unchanged.
- version: 3
  date: '2026-11-26'
  note: >-
    Dated note of 2026-11-26 from the exchange "Alignment
    consequences brainstorm" (ChatGPT, 2026-11-26), U8–A15: A15's
    authority-sensitive kernel, which indexes this term by an
    authorized coalition, corrected by the assistant: a pointwise
    readiness constraint is not a kernel, and thresholds the
    governed state can lower make every state viable. The definition
    is unchanged.
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

# TERM-167: reorganization viability kernel

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

## Note of 2026-11-26: the exchange "Alignment consequences brainstorm" (ChatGPT, U1–A4)

<!-- inactive-ok-file: CLAIM-667 CLAIM-tmp887rf — Proposed; the study and the entries of 2026-11-26 that use this kernel -->

A2 §6 proposed the governance of possibility as "a formal framework for AI
control", a reachable set ℛ_T(x, B; 𝒢) of corrective states for a
human–AI organization, and the owner answered at U2: "let's double click
on this. the luria line of work should probably have stuff in this
neighborhood". A4 §1 then read this term's three achievements, current
adequacy, reorganization readiness and adaptive viability, for an AI
research organization, accurately and with the inclusions the
manuscript's §8.4 states ("Current adequacy does not imply readiness, and
readiness does not imply its own continued viability").

A4 adds "A fourth achievement, not fully captured by the current
construction ... the maintained ability to revise the governance
organization itself, including its criteria for what constitutes an
appropriate response". That is held: the manuscript's §8.4 says the
construction formalizes [CLAIM-025](../claims.d/CLAIM-025.md)'s third tier, "the capacity to
transform that organization", "only as far as 𝔇 reaches", and leaves
open what would make that capacity the organization's own ([QUESTION-388](../questions.d/QUESTION-388.md)).

A4 §5 proposes indexing the kernel by actor, V_human, V_AI, V_joint; that
is [LEAD-254](../leads.d/LEAD-254.md)'s, and its note of today states what the indexing must fix.
A4 §15 proposes a study connecting this kernel to [CLAIM-667](../claims.d/CLAIM-667.md)'s experiment
([LEAD-tmp9snzi](../leads.d/LEAD-tmp9snzi.md)), and A5 §2 calls a strike fund "part of the material
infrastructure of reorganization readiness" ([CLAIM-tmp887rf](../claims.d/CLAIM-tmp887rf.md)). Each is an
application, not a revision; the term is unchanged.

## Note of 2026-11-26: the exchange "Alignment consequences brainstorm" (ChatGPT, U8–A15)

<!-- inactive-ok-file: CLAIM-tmpygs06 CLAIM-tmpv3frk — new or Proposed; the claims of 2026-11-26 the note corrects and uses, and the held readiness term -->

A correction, the assistant's, to a use of this term.

**What A15 proposes.** For its platform (CLAIM-tmpygs06), A15 §VII takes
the institutional state z_t = (K_t, C_t, D_t, A_t, G_t), epistemic,
capability, dependency, effective-authority and governing components, and
for an authorized constituent or coalition i the set R_i(z_t, B, T) of
states it can reach with resources B by deadline T. For each designated
contingency ω it requires Pr_i(adequate response to ω within B_ω, T_ω) ≥
q_ω, "where the relevant actors, adequacy criteria, budgets, deadlines,
and readiness thresholds are themselves subject to legitimate
governance", and calls this "part of an **authority-sensitive viability
kernel**". The new element is the index i: this term's routes C_ω become
the routes open to a particular coalition, and readiness becomes [TERM-115](TERM-115.md)'s
probability.

**Two corrections.**

1. *A constraint is not a kernel.* The inequality, imposed for each ω,
   defines a constraint set M_i, the states from which coalition i is
   ready now. The kernel is Viab(M_i), the states from which ordinary
   operation can keep it ready, as this term's V_reorg = Viab_F0(M) says.
   A15's "part of" passes over that step, which is the term's whole point.
2. *Thresholds inside the state.* If the governing apparatus G_t sets
   q_ω, B_ω and T_ω, and G_t is a component of the state the dynamics
   move, then a policy that lowers the threshold as readiness decays stays
   in M_i for ever. Every state is then viable, and the kernel says
   nothing. This is this term's limit, that K_ω "must be fixed
   independently of the current arrangement, or every arrangement is
   viable by its own standards", met through the governance component, and
   it is the constitutional capture of CLAIM-tmpv3frk in formal dress. The
   remedy consistent with A15's own R12: compute the kernel with the
   thresholds frozen at the time of judgement, and judge their revision
   separately, as a constitutional change under authority the governed
   process does not hold.

**A check (python3 -I).** States (r, q), readiness r and threshold q in
0..5, constraint r ≥ q; readiness decays by one each step unless
maintained. A coalition that can maintain has kernel equal to the whole
constraint set (21 states). One that can only neglect has kernel {q = 0}
(6 states). One that can neglect or lower q by one each step has kernel
equal to the whole constraint set again: from (3, 3) it runs (2, 2),
(1, 1), (0, 0), meeting r ≥ q at every step while failing the frozen
threshold 3 from the first. Restricting a coalition's actions can only
shrink its kernel (the neglect-only kernel lies inside the others), which
is the sense in which the kernel is authority-sensitive; letting it set
its own thresholds can make it as large as it likes. The script, a
backward fixed-point computation over the 36 states, was run in this
session's scratchpad and is not committed. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
