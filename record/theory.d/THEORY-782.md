---
number: 782
status: Proposed
formerly:
- THEORY-tmplgh5u
promote_when: >-
  What would settle it is the same toy (two learned embeddings summed and
  decoded, addition hard-coded) run at several group sizes p. For each
  training set, it would have to report the nullity of the linear system
  its same-answer pairs impose and whether the trained network
  generalises. The claim holds if, at every p, full generalisation occurs
  with high probability exactly on training sets of nullity 2, and the
  empirical critical fraction follows the fraction at which nullity 2
  becomes likely. It is refuted by networks in that setting that
  generalise fully on training sets of nullity above 2, or by a critical
  fraction that departs from the nullity threshold as p grows. More
  single-size runs, or pictures of structured embeddings in larger models,
  are the wrong kind of evidence: they show structure, not that the
  training set's equations are what fix it.
title: 'In networks that learn addition from summed embeddings, the critical training fraction of grokking is the fraction at which the training set''s same-answer pairs come to fix the generalising representation up to translation and scale, at every group size, as Liu, Kitouni, Nolte, Michaud, Tegmark and Williams propose'
version: 1
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-20'
source:
- LIT-858
- LIT-341
summary: >-
  Liu, Kitouni, Nolte, Michaud, Tegmark and Williams (2022), [LIT-858](../literature.d/LIT-858.md), read
  in [NOTE-662](../notes.d/NOTE-662.md), with Power et al.'s critical fraction ([LIT-341](../literature.d/LIT-341.md)). The paper
  presents the critical training fraction as where the training set's
  equations fix the embedding. [THEORY-181](THEORY-181.md) holds the theorem for the ideal
  model and the match at the one size measured, p = 10 with 1D embeddings.
  Held to addition: for S₃ the networks generalise beyond this mechanism.
  The multi-size test is [QUESTION-199](../questions.d/QUESTION-199.md).
extends:
- THEORY-181
answers:
- QUESTION-199
---

# THEORY-782: In networks that learn addition from summed embeddings, the critical training fraction of grokking is the fraction at which the training set's same-answer pairs come to fix the generalising representation up to translation and scale, at every group size, as Liu, Kitouni, Nolte, Michaud, Tegmark and Williams propose

## Source

Liu, Kitouni, Nolte, Michaud, Tegmark and Williams (2022), [LIT-858](../literature.d/LIT-858.md), §3 and
Appendices C–F and H, as read in [NOTE-662](../notes.d/NOTE-662.md); Power et al. (2022), [LIT-341](../literature.d/LIT-341.md),
for the critical fraction in the original grokking setting.

## What is asserted

That grokking's critical training fraction is set by the training data's
algebra: a network that sums two learned embeddings generalises once the
same-answer pairs in its training set impose enough equations to leave
the embedding free only up to translation and scale, and the critical
fraction is where that first becomes likely. The paper offers this as the
explanation of the critical fraction, not only as a match at one size.

## What the Active account establishes toward it

[THEORY-181](THEORY-181.md) holds Propositions 1–2 for the ideal model (zero training loss,
injective decoder), re-derived, and the one measurement: for non-modular
addition with p = 10 and 1D embeddings, generalisation sets in near the
fraction, about 0.4, at which that becomes likely.

## Why it is held to addition

The pre-narrowing wording, and the sweep's first suggestion, spoke of the
model or of arithmetic in general. For S₃ the paper's predicted accuracy is
only a lower bound and the networks generalise by something beyond it
([NOTE-662](../notes.d/NOTE-662.md), App. H, Fig. 18e). So the source's own results do not support
the thesis beyond addition, and this entry does not claim it.

## What would confirm or reject it

The promote_when above, [QUESTION-199](../questions.d/QUESTION-199.md)'s test across group sizes.

## Provenance

Filed on 2026-10-20 by the narrowing-loss sweep ([ADR-047](../decisions.d/ADR-047.md) v4, batch 068),
from the critical-fraction clause [THEORY-181](THEORY-181.md)'s title carried before it was
narrowed on 2026-10-19.
