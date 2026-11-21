---
status: Proposed
title: "Evidence that a system has learned a distinction certifies it only when scored against what the same measure shows with no learning, a null; a measure read without its null cannot certify"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A measure of learned structure whose reading, with no null computed,
  reliably separates systems that learned the distinction from systems
  that did not, across the cases this claim cites (concentration in high
  dimension, cone occupancy, power-law distributions); or a showing that
  in each of those cases the null is already built into the measure, so
  that the claim adds nothing to CLAIM-402.
tags:
- learning-theory
- representation-learning
- epistemology
line:
- learning-and-inquiry
- learned-structure
rests_on:
- CLAIM-402
- CLAIM-tmp41gfr
- CLAIM-tmp6mjfc
summary: >-
  Filed at the owner's go-ahead under the dialectic regime, from the
  manuscript's update of 2026-11-21 (§2.4), where it was marked as the
  draft's own addition: "evidence must be scored against what the measure
  would show with no learning at all." Four cases from the exchange "Rich
  Get Richer Power Laws" show a measure that moves with no learning: a
  thin shell and near-orthogonal directions in high dimension
  ([CLAIM-tmp41gfr](CLAIM-tmp41gfr.md)), cone occupancy that rises when boundaries move or
  under collapse ([CLAIM-tmp6mjfc](CLAIM-tmp6mjfc.md)), coupled embeddings that relax rather
  than act ([CLAIM-tmpet76z](CLAIM-tmpet76z.md)), and a power law that many routes produce
  ([CLAIM-tmpsr8r4](CLAIM-tmpsr8r4.md), [CLAIM-tmp8h6nt](CLAIM-tmp8h6nt.md)). Whether null scoring is a fourth
  route to certification or a case of an existing one is filed as two
  alternatives, [CLAIM-tmpz5c3x](CLAIM-tmpz5c3x.md) and [CLAIM-tmpnf9by](CLAIM-tmpnf9by.md). The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
date: '2026-11-21'
---
<!-- inactive-ok-file: CLAIM-tmp41gfr CLAIM-tmp6mjfc CLAIM-tmpet76z CLAIM-tmpsr8r4 CLAIM-tmp8h6nt CLAIM-tmpz5c3x CLAIM-tmpnf9by — Proposed or new; filed 2026-11-21 -->

# CLAIM-tmpfls41: Evidence that a system has learned a distinction certifies it only when scored against what the same measure shows with no learning, a null; a measure read without its null cannot certify

**The claim.** A reading of a measure is evidence that a system has learned a distinction only relative to the reading the same measure gives, in the same system class, with no learning: a random initialization, a shuffled target, an untrained network of the same width, a generative process with no feedback. Where the null is not computed, the reading cannot certify, however striking it is.

**Why it is not already held.** [CLAIM-402](CLAIM-402.md) (Active; P3 of the manuscript) says a category's predictive success warrants it only when the evidence does not pass through the category's own use, or when that use is modelled. That concerns evidence produced *by the categories*. The cases here are different: the measure moves for reasons that have nothing to do with the system's categories, because of geometry ([CLAIM-tmp41gfr](CLAIM-tmp41gfr.md)), the measure's own construction ([CLAIM-tmp6mjfc](CLAIM-tmp6mjfc.md)), the dynamics of optimization ([CLAIM-tmpet76z](CLAIM-tmpet76z.md)), or many generating routes ([CLAIM-tmpsr8r4](CLAIM-tmpsr8r4.md)). So the limit is on the measure, not on the categories.

**Cases.**
- In high dimension a thin radial shell, near-orthogonality and equal distances "arise with no interaction at all" ([CLAIM-tmp41gfr](CLAIM-tmp41gfr.md)).
- Cone occupancy "rises when cone boundaries move as well as when representations flow", and nesting makes the coarse cone entered first by construction ([CLAIM-tmp6mjfc](CLAIM-tmp6mjfc.md)).
- A power-law distribution is produced by many routes, so it does not show the route at work ([CLAIM-tmp8h6nt](CLAIM-tmp8h6nt.md), [CLAIM-tmpsr8r4](CLAIM-tmpsr8r4.md)).

**Scope.** A null is relative to a declared ensemble, and different ensembles give different nulls ([CLAIM-tmp41gfr](CLAIM-tmp41gfr.md)'s ensemble dependence). The claim does not say which null; it says a reading needs one, and states it.

**Admission ([ADR-075](../decisions.d/ADR-075.md)).** The claim's premises are claims, so it passes only if it adds something. It passes by a *separating case*. Take a measure whose every premise holds, for example a high-dimensional representation whose measured distances are nearly equal. Read without a null, that is taken as evidence of learned uniformity. With the null, it is what any random embedding of that width shows. [CLAIM-402](CLAIM-402.md) holds and is silent: the evidence did not pass through the system's categories. [CLAIM-tmp41gfr](CLAIM-tmp41gfr.md) holds and is silent on certification. The claim says the reading certifies nothing, which neither premise says.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
