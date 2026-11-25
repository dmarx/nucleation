---
number: 821
status: Proposed
formerly:
- CLAIM-tmpfls41
title: 'No certification without a null'
statement: >-
  Evidence that a system has learned a distinction certifies it only when
  scored against what the same measure shows with no learning, a null; a
  measure read without its null cannot certify
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
- CLAIM-797
- CLAIM-800
summary: >-
  Filed at the owner's go-ahead under the dialectic regime, from the
  manuscript's update of 2026-11-21 (§2.4), where it was marked as the
  draft's own addition: "evidence must be scored against what the measure
  would show with no learning at all." Four cases from the exchange "Rich
  Get Richer Power Laws" show a measure that moves with no learning: a
  thin shell and near-orthogonal directions in high dimension
  ([CLAIM-797](CLAIM-797.md)), cone occupancy that rises when boundaries move or
  under collapse ([CLAIM-800](CLAIM-800.md)), coupled embeddings that relax rather
  than act ([CLAIM-818](CLAIM-818.md)), and a power law that many routes produce
  ([CLAIM-841](CLAIM-841.md), [CLAIM-803](CLAIM-803.md)). Whether null scoring is a fourth
  route to certification or a case of an existing one is filed as two
  alternatives, [CLAIM-851](CLAIM-851.md) and [CLAIM-831](CLAIM-831.md). The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
date: '2026-11-21'
---
<!-- inactive-ok-file: THEORY-2173 — Proposed; the readings of 2026-11-22 cited in the notes -->
<!-- inactive-ok-file: CLAIM-797 CLAIM-800 CLAIM-818 CLAIM-841 CLAIM-803 CLAIM-851 CLAIM-831 — Proposed or new; filed 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2188 — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CLAIM-821: No certification without a null

**The claim.** A reading of a measure is evidence that a system has learned a distinction only relative to the reading the same measure gives, in the same system class, with no learning: a random initialization, a shuffled target, an untrained network of the same width, a generative process with no feedback. Where the null is not computed, the reading cannot certify, however striking it is.

**Why it is not already held.** [CLAIM-402](CLAIM-402.md) (Active; P3 of the manuscript) says a category's predictive success warrants it only when the evidence does not pass through the category's own use, or when that use is modelled. That concerns evidence produced *by the categories*. The cases here are different: the measure moves for reasons that have nothing to do with the system's categories, because of geometry ([CLAIM-797](CLAIM-797.md)), the measure's own construction ([CLAIM-800](CLAIM-800.md)), the dynamics of optimization ([CLAIM-818](CLAIM-818.md)), or many generating routes ([CLAIM-841](CLAIM-841.md)). So the limit is on the measure, not on the categories.

**Cases.**
- In high dimension a thin radial shell, near-orthogonality and equal distances "arise with no interaction at all" ([CLAIM-797](CLAIM-797.md)).
- Cone occupancy "rises when cone boundaries move as well as when representations flow", and nesting makes the coarse cone entered first by construction ([CLAIM-800](CLAIM-800.md)).
- A power-law distribution is produced by many routes, so it does not show the route at work ([CLAIM-803](CLAIM-803.md), [CLAIM-841](CLAIM-841.md)).

**Scope.** A null is relative to a declared ensemble, and different ensembles give different nulls ([CLAIM-797](CLAIM-797.md)'s ensemble dependence). The claim does not say which null; it says a reading needs one, and states it.

**Admission ([ADR-075](../decisions.d/ADR-075.md)).** The claim's premises are claims, so it passes only if it adds something. It passes by a *separating case*. Take a measure whose every premise holds, for example a high-dimensional representation whose measured distances are nearly equal. Read without a null, that is taken as evidence of learned uniformity. With the null, it is what any random embedding of that width shows. [CLAIM-402](CLAIM-402.md) holds and is silent: the evidence did not pass through the system's categories. [CLAIM-797](CLAIM-797.md) holds and is silent on certification. The claim says the reading certifies nothing, which neither premise says.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.

## Note of 2026-11-22: Clauset, Shalizi and Newman, read

Clauset, Shalizi and Newman ([LIT-2987](../literature.d/LIT-2987.md), read in [NOTE-2262](../notes.d/NOTE-2262.md); the reading is [THEORY-2173](../theory.d/THEORY-2173.md)): **a parallel**. Their bootstrap p-value scores the data against a
null fitted to the same data, refitting each synthetic set by "the same
calculation that we performed for the real data set" (§4.1, p. 17), and
they warn that "a large p-value does not necessarily mean the power law
is the correct distribution for the data". A measure read against its
null, and a null that cannot certify by itself. No edge. Status
unchanged.

## Note of 2026-11-22: Cai and colleagues, read

Cai, Zhang, Liu and Shi ([LIT-2975](../literature.d/LIT-2975.md), [NOTE-2277](../notes.d/NOTE-2277.md), [THEORY-2188](../theory.d/THEORY-2188.md)): **a parallel.** Their
"uniformity" is a property of the objective's optimum, a Gibbs density;
a measurement of uniformity in a trained network would still need this
claim's null, since near-equal distances arise in high dimension with no
learning. A note, no relation.
