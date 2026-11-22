---
status: Proposed
title: 'Probing two compatibility-equivalent constraint systems at rising move budgets, the distinguish-or-not verdict stabilizes at a finite budget below which they are indistinguishable, and a construction realizes any chosen finite stabilization budget, so the budget at which a reachability distinction first appears is a measurable threshold and not fixed'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the runs or the constructions: a budget at which a reported
  readout is miscomputed, a pair whose recorded stabilization budget differs
  from a correct recomputation, or a member of the tunable family whose two
  mechanisms do not share a compatibility complex. Not defeated by the
  distinctions being descriptive only (TERM-088), by the mechanisms'
  smallness, or by the probe family being one among others.
tags:
- complex-systems
- mathematics
- individuation
date: '2026-11-22'
line:
- realizability
- formal-apparatus
bears_on:
- QUESTION-382
corroborates:
- CLAIM-583
- CLAIM-574
grounds:
- CASE-tmpxkvpz
uses:
- TERM-114
---
<!-- inactive-ok-file: CASE-tmpxkvpz CASE-202 — CASE-tmpxkvpz is the executed study this claim is grounded in, filed in this batch; CASE-202 is the Proposed design it runs -->

# CLAIM-tmpco6u9: Probing two compatibility-equivalent constraint systems at rising move budgets, the distinguish-or-not verdict stabilizes at a finite budget below which they are indistinguishable, and a construction realizes any chosen finite stabilization budget, so the budget at which a reachability distinction first appears is a measurable threshold and not fixed

## The claim

Run the individuation-by-probing procedure of [CASE-202](../cases.d/CASE-202.md) on a pair of
resource-bounded constraint systems ([TERM-114](../terms.d/TERM-114.md)) that share a compatibility
complex, a single-flip move rule and costs: probe each at budgets b = 0, 1,
2, …, where the budget is the number of admissible moves a probe may attempt,
and read off at each budget whether the reachability-between-demands readout
tells the two apart. Two findings, from the executed study [CASE-tmpxkvpz](../cases.d/CASE-tmpxkvpz.md):

1. **The verdict stabilizes at a finite budget.** For [CLAIM-583](CLAIM-583.md)'s seed pair,
   the readouts agree at budget 0 (the static family) and part at budget 1,
   where B's D₁-configuration reaches a D₂-configuration in one move and A's
   does not; the verdict is "distinguishable" from budget 1 on and never
   reverts, as it cannot along nested families ([CLAIM-574](CLAIM-574.md)). A finite
   stabilization budget is what [LEAD-135](../leads.d/LEAD-135.md) counts as support for [CLAIM-583](CLAIM-583.md).
2. **The stabilization budget is a measured quantity, not fixed.** A
   construction realizes any finite distinguishing budget L: B admits a
   Hamming path of length L between the two demand targets and A admits only
   the endpoints, so the complexes, moves and costs agree and the readouts
   agree at every budget below L, and the pair parts exactly at L. Run for
   L = 2…5, the stabilization budget equals L. So the budget at which a
   reachability distinction first appears between compatibility-equivalent
   systems is set by the systems, read off as a threshold, and not pinned to
   any particular value.

Together these corroborate [CLAIM-583](CLAIM-583.md) by a route independent of its hand
enumeration — an operationalized, tested procedure — and locate its
separation of the configuration layer from the process layer at a definite,
tunable budget. For [QUESTION-382](../questions.d/QUESTION-382.md) the seed pair is an interface equivalence
(agreement under the static family) that fails once the reachability of the
process layer is counted, with the failure budget measured.

## What it does not say

- **That the distinction is of individuals.** Separating two mechanisms by a
  readout is descriptive individuation in [TERM-088](../terms.d/TERM-088.md)'s sense only; the
  dynamical, constitutive and autonomy senses are not reached here.
- **That the probe found a difference it did not make.** That the procedure
  discovers rather than creates the difference holds here because the prober
  is non-destructive ([CASE-tmpxkvpz](../cases.d/CASE-tmpxkvpz.md)'s control); it is not a general claim
  about probes, which a destructive probe would test.
- **That a costly distinguishing budget is realized by a natural substrate.**
  The tunable family is abstract; whether a mechanism whose parting budget is
  large arises for origami or any physical substrate is left open, as [CASE-202](../cases.d/CASE-202.md)
  frames the broader study.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
