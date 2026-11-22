---
number: 515
status: Open
formerly:
- QUESTION-tmpvu6cb
title: 'What follows if the representational manifold a deep network learns, a high-dimensional system, is modelled as an active-matter system?'
version: 1
tags:
- representation-learning
- complex-systems
- learning-theory
date: '2026-11-21'
line:
- learned-structure
summary: >-
  The owner's, at U18 of the exchange "Rich Get Richer Power Laws"
  (2026-11-21): "how about if high dimensional systems? consider a
  representational manifold learned by a DNN modeled as an active matter
  system". The other assistant's answer (A29 §11) grades the idea into
  three hypotheses of increasing strength, which the body sets out as A's,
  and the owner's next turn (U19) adds concentration of measure as the
  baseline any such model has to beat ([CLAIM-822](../claims.d/CLAIM-822.md)).
---
<!-- inactive-ok-file: NOTE-tmpcjw5n LIT-tmpu2kk5 — Skimmed, Deferred or new; readings of 2026-11-22 and Cassi, registered -->
<!-- inactive-ok-file: CLAIM-799 THEORY-tmpcij35 THEORY-tmphbp5a — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: CLAIM-822 CLAIM-798 CLAIM-818 CLAIM-842 TERM-136 CLAIM-797 CLAIM-838 THEORY-1095 THEORY-2051 THEORY-209 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Proposed entries the record already held, cited for context -->
<!-- inactive-ok-file: THEORY-tmpvwv5n — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# QUESTION-515: What follows if the representational manifold a deep network learns, a high-dimensional system, is modelled as an active-matter system?

## Why it is a question

The owner, at U18: "how about if high dimensional systems? consider a
representational manifold learned by a DNN modeled as an active matter
system".

The record holds Toner and Tu's theory of flocks ([THEORY-1085](../theory.d/THEORY-1085.md), [THEORY-1095](../theory.d/THEORY-1095.md)),
a reading on symmetry breaking and Goldstone modes in deep networks
([THEORY-2051](../theory.d/THEORY-2051.md)), and readings on the probability currents of SGD ([THEORY-209](../theory.d/THEORY-209.md),
[THEORY-779](../theory.d/THEORY-779.md)). It has nothing on what would make a population of learned
representations an active-matter system, or on which dimension would govern
its collective behaviour.

The grading below is A's, not the owner's. A29 §11 separates three
things the question could mean, "of increasing strength", and warns that "these hypotheses shouldn't be collapsed into a
single assertion":

1. **Collective representation dynamics**: embeddings "behave like coupled
   particles whose movements are mediated by shared parameters". A29: "This
   follows naturally from the gradient-flow formulation" ([CLAIM-798](../claims.d/CLAIM-798.md)).
2. **Nonequilibrium self-organization**: a "driven, noisy process with
   measurable irreversible dynamics", which "needs to be demonstrated rather
   than assumed".
3. **Critical or scale-free active representation dynamics**: collective
   rearrangements, relaxation times or correlations obeying universal
   scaling laws, which "requires dynamical and finite-size evidence beyond a
   power-law covariance spectrum".

## What would count as an answer

- For the second sense: a source of broken detailed balance in training,
  identified and measured, such as nonzero probability currents or
  time-reversal asymmetry in the trajectories of a fixed probe set's
  representations. Gradient flow alone cannot supply one ([CLAIM-818](../claims.d/CLAIM-818.md)); [THEORY-209](../theory.d/THEORY-209.md)
  and [THEORY-779](../theory.d/THEORY-779.md) say where SGD's currents come from in the parameters.
- For the third: velocity correlations, slow modes and finite-size collapse
  that neither the high-dimensional concentration null ([CLAIM-797](../claims.d/CLAIM-797.md), [CLAIM-838](../claims.d/CLAIM-838.md)) nor
  the correlations the representation kernel predicts already explain
  ([LEAD-210](../leads.d/LEAD-210.md)).
- Or a dissolution: an argument that representations lack the
  self-propulsion or orientational degrees of freedom any active-matter
  theory needs, so that only the first sense survives and "active" adds
  nothing to "coupled".

Which dimension governs the collective behaviour is part of the question:
A29 argues it is the spectral dimension of the interaction geometry, not
layer width ([CLAIM-842](../claims.d/CLAIM-842.md); the senses are [TERM-136](../terms.d/TERM-136.md)).

## Note of 2026-11-22: Park and colleagues, read

Park and colleagues ([LIT-2990](../literature.d/LIT-2990.md), [NOTE-tmpzethm](../notes.d/NOTE-tmpzethm.md), [THEORY-tmphbp5a](../theory.d/THEORY-tmphbp5a.md)): **leaves
the question open.** The paper establishes a BBP outlier transition in a
solvable training model and speaks of "the notion of criticality arising
during optimisation itself", but says nothing of active matter and leaves
"the precise universality class of the transition in practical deep
learning systems" unclear.

## Note of 2026-11-22: Dandi and colleagues, read

Dandi and colleagues ([LIT-2983](../literature.d/LIT-2983.md), [NOTE-tmpdac0o](../notes.d/NOTE-tmpdac0o.md), [THEORY-tmpcij35](../theory.d/THEORY-tmpcij35.md)): **leaves
the question open.** One gradient step and no dynamics; the spiked picture
of learned features is a theorem there, which supports only the claim that
the spectral perspective is not merely an analogy ([CLAIM-799](../claims.d/CLAIM-799.md)).

## Note of 2026-11-22: Cai and colleagues, read

Cai, Zhang, Liu and Shi (LIT-2975, NOTE-tmpll97d, THEORY-tmpvwv5n): **background;
leaves it open.** It gives the "forces" half of A29 §2's particle picture
an explicit population form for contrastive objectives: an alignment field
and a partition field that is a mean field through the representation's
own density. It says nothing on activity or criticality, and places the
source of any irreversibility outside the objective, which is a joint
energy even for two modalities (CLAIM-798's note). No relation.

## Note of 2026-11-22: Toner and Tu (1998), and the Mermin–Wagner neighbours, read

**Background, no edge.** Toner and Tu's long paper (LIT-2970,
NOTE-tmpcjw5n) names what an active-matter model of a representation
would have to carry over before its results transfer: self-propulsion
through a medium that singles out a frame (no Galilean invariance, no
momentum conservation), rotation invariance, a conserved density, and
convective transport that changes who interacts with whom; it is these,
out of equilibrium, that remove the 2D logarithm and give true order. It
says nothing of representations. And the criterion of CLAIM-842, which
"What would count as an answer" cites, is now held in the literature as a
theorem for spin models in equilibrium (Cassi, LIT-tmpu2kk5, through
Gelfert and Nolting, LIT-tmpbgf6y), with conditions (a local continuous
symmetry, equilibrium, finite second moments) an active-matter reading
would break: the flock is the worked case where breaking equilibrium
reverses the conclusion (CLAIM-842's section of 2026-11-22). No status
change.
