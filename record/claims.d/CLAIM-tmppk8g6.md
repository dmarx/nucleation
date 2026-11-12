---
status: Proposed
title: 'Governance raises the value of a modifiable schema on tasks whose inherited categories are inadequate: with review, rationale and migration, letting a collective change its schema improves justified correction more than it does without them, while on routine tasks governance adds cost and no correction'
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  In a study that holds evidence, models, tools and budget fixed and
  crosses a fixed or modifiable schema with informal or explicit change
  governance, the interaction on tasks whose categories are inadequate is
  zero or negative: the gain from modifiability is no larger with
  governance than without, measured as justified correction completed
  without material regression; or a performance-gated arm, changes
  accepted on held-out tests alone, matches the governed arm at no greater
  cost. Also defeated if governance improves correction as much on routine
  tasks as on misfit tasks, which would make it a general benefit of
  review, not an interaction with modifiability. Not defeated by the
  governed arm scoring better on compliance or traceability alone: those
  are reported separately and are not the outcome.
tags:
- design-rationale
- databases
- epistemology
date: '2026-11-12'
line:
- record-as-apparatus
bears_on:
- QUESTION-tmps5iou
summary: >-
  What A45 §3 adds to its components, the synthesis of the exchange "luria
  experiment design" (2026-11-10) that the owner asked for at U19 ("reflect
  back on the full conversation and consider what different pieces might
  be worth synthesizing into our experimental program"). A: "Luria's schema
  flexibility and governance may be most valuable together", and "The
  scientifically interesting outcome is whether governance changes the
  value of schema modifiability." A48 §6, after the owner's U20, keeps it
  as the central test of its second study. The coupling it is about is the
  owner's U8. Filed under the synthesis audit by the discriminating-
  prediction route: no component predicts the interaction, and its sign
  can come out against. A states it as a hypothesis to test; filed
  Proposed with an empirical warrant that no result yet supplies. The
  wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmppm4do — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: ADR-075 — Proposed; the synthesis audit under which this claim was admitted -->
<!-- inactive-ok-file: LIT-2311 — Deferred; registered from the same exchange, not read -->

# CLAIM-tmppk8g6: Governance raises the value of a modifiable schema on tasks whose inherited categories are inadequate: with review, rationale and migration, letting a collective change its schema improves justified correction more than it does without them, while on routine tasks governance adds cost and no correction

## The claim

From A45 §3 of the exchange "luria experiment design"
(https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda): "A
flexible schema without governance may allow rapid but incoherent
adaptation. Governance without flexibility may reliably enforce inadequate
categories." Cross the two in a 2×2, with Y the probability of completing
a justified correction without material regressions within budget:

Δ = (Y_flexible,governed − Y_fixed,governed) − (Y_flexible,ungoverned − Y_fixed,ungoverned)

The claim is that Δ is positive on tasks where the inherited categories
cannot express a needed distinction, and that on routine tasks, where no
schema change is warranted, governance adds review cost without adding
correction. A45: "A positive interaction would indicate that flexibility
becomes more useful in the governed condition, within the tested tasks. It
would not automatically identify which governance mechanism caused the
difference." A48 §6: "The central test is the interaction, not merely
whether B11 scores highest."

The mechanism A proposes (A45 Study 2): governance helps "the handling of
changes whose meaning cannot be exhausted by immediate benchmark
performance". Its example: "a schema change may improve current retrieval
while making an old objection impossible to express correctly. A
performance gate that only tests the current query set may accept it; a
broader regression process may reveal the problem."

## Admission

Filed under the synthesis audit (ADR-075's step 5) by the route of a
**discriminating prediction**. The components A45 integrates, CLAIM-419
(the grammar is amended by decision when a misfit is noticed), CASE-178
(refinements came with an ADR nine times in ten), TERM-085 (correctability)
and CLAIM-470 (inquiry can revise what counts as an answer), say that the
record couples schema change to decision. None says the coupling changes
what modifiability is worth, and all of them hold whichever sign Δ takes.
The outcome against the claim is stated in `defeated_if`; the study that
would measure it is CASE-tmppm4do.

## What it does not say

- Not that the governed, modifiable arm scores highest. It could, with a
  zero interaction, if governance and modifiability each help on their
  own.
- Not that formal governance is better than performance gating. A48 makes
  performance-gated evolution, as in EvoOntology (LIT-2311), "a serious
  comparator"; the claim is defeated if it does as well.
- Not which governance mechanism does the work. The claim is about the
  combination of review, rationale and migration as one treatment; A48 §6
  varies who holds authority as a secondary design.
