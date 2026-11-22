---
number: 823
status: Proposed
formerly:
- CLAIM-tmpgzb8v
title: "Alternative reading (b) of the owner's suggestion on singularities: a phase transition in learning is a change in which singular region of parameter space dominates, as the sample size grows, between regions that fit differently and have different learning coefficients, and resolution of singularities is the tool that computes those coefficients"
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    After the reading of Hoogland et al. (LIT-2966, NOTE-tmp2pgi8): the
    sentence calling the work unread updated, its ground changed from the
    work to the reading (THEORY-tmpr9w2r), and a dated note added
    (ARG-tmpfh555). Title and thesis unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A study of a network that passes through representational stages, with
  local learning coefficients measured across them, in which the stages
  coincide with no change in the dominant singular region or its
  coefficient and are fully accounted for by an account that uses no
  singular geometry, such as the order of the data's spectral modes
  alone; or a showing that the Bayesian order in sample size and the
  order of training's stages are unrelated in general. A transition the
  theory cannot compute for a large network does not defeat it; the claim
  is that the account is useful, not that it is tractable everywhere.
tags:
- learning-theory
- loss-landscapes
- model-comparison
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-305
grounds:
- THEORY-087
- THEORY-1275
- THEORY-975
- THEORY-tmpr9w2r
bears_on:
- QUESTION-tmphkb1w
- QUESTION-363
- QUESTION-217
- QUESTION-514
summary: >-
  One of two alternative readings of the owner's U23 in the exchange "Rich
  Get Richer Power Laws" ([CLAIM-834](CLAIM-834.md)): "singularity theory has an
  account for phase transitions in learning as resolutions of
  singularities that might be useful here". This is reading (b), the
  reframing A gave in reply: transitions are changes of the dominant
  singularity, and resolution is how their learning coefficients are
  found. The other is reading (a), [CLAIM-802](CLAIM-802.md), the owner's words taken
  literally. The owner chooses. The wording is A's (the other assistant in
  the exchange "Rich Get Richer Power Laws", A37); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-tmpu0f9k THEORY-tmpm3ux2 — Proposed; the readings of Yang and of Lee et al. filed 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-834 CLAIM-802 ARG-132 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21, or a Deferred work registered from it and not yet read -->
<!-- inactive-ok-file: CLAIM-812 THEORY-2157 THEORY-tmpr9w2r ARG-tmpfh555 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# CLAIM-823: Alternative reading (b) of the owner's suggestion on singularities: a phase transition in learning is a change in which singular region of parameter space dominates, as the sample size grows, between regions that fit differently and have different learning coefficients, and resolution of singularities is the tool that computes those coefficients

**This is reading (b) of [CLAIM-834](CLAIM-834.md), the owner's U23, one of two
alternatives.** The other, reading (a), is [CLAIM-802](CLAIM-802.md). The owner
chooses.

## The claim

A37 reframes the owner's "as resolutions of singularities". Resolution, at
A37 §3, "doesn't mean that training literally performs an algebraic
blow-up. Resolution is an analytical tool that reveals the structure hidden
inside a singular parameterization": it brings the loss to a normal form
from which the learning coefficient λ and its multiplicity m are read
([CLAIM-305](CLAIM-305.md): "what the resolution buys is a normal form for the divergence,
and so the learning coefficient").

The transition is then a competition. Regions of parameter space with
different fits and different learning coefficients contribute free
energies F ≈ nL + λ log n − (m − 1) log log n (A37 §5; [THEORY-087](../theory.d/THEORY-087.md)). A
simpler region with worse fit and smaller λ can dominate at small n and a
richer one later, with the crossover where "n(L_A − L_B) ≈ (λ_B − λ_A) log
n" (A37 §5). "At that point, the dominant contribution to the Bayesian
posterior can switch between different representational structures." The
record holds such Bayesian transitions in a toy model, and their partial
agreement with SGD's order ([THEORY-1275](../theory.d/THEORY-1275.md), [QUESTION-363](../questions.d/QUESTION-363.md)).

On this reading the owner's suggestion proposes that the stages of
representational development are such switches, or at least leave their
mark in local learning coefficients. The record holds one reading in
favour: weight-refined coefficients of attention heads diverge by function
over training ([THEORY-975](../theory.d/THEORY-975.md)). Hoogland and colleagues ([LIT-2966](../literature.d/LIT-2966.md),
read 2026-11-21: [THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)) report stagewise changes in the
coefficient in two small transformers; see the note below.

## What it does not say

- Not that the Bayesian order in n is the training order in t. A37 §5
  keeps three transitions apart, Bayesian, dynamical and semantic: "These
  may be related, but they're not equivalent." The bridge is
  [QUESTION-363](../questions.d/QUESTION-363.md), open.
- Not that every stage of learning is a singular transition.
- Not that it is the owner's meaning. It is A's reframing of the owner's
  words; reading (a) keeps them literal. [ARG-132](../arguments.d/ARG-132.md) gives the
  assistant's reason to prefer (b), which the owner may not share.

## Note of 2026-11-21: Lau et al., read

A caution from the estimator's source ([NOTE-2239](../notes.d/NOTE-2239.md), [THEORY-2157](../theory.d/THEORY-2157.md)) on
reading a change in local learning-coefficient estimates as a transition:
the estimate is made at one inverse temperature, β* = 1/log n, with a
localizer of precision γ, and both set which directions count (on a
quadratic loss, Σ ½·te_i/(te_i + γ), t = n/log n); consistency is a
conjecture; and an unsettled sampler underestimates ("If the step size is
too low, the sampler may not equilibriate, leading to underestimation",
App. H). A change in the estimate over training is evidence of a change of
stratum only with the sampler settings fixed across checkpoints, settling
checked, and β and γ varied ([LEAD-207](../leads.d/LEAD-207.md), [CLAIM-812](CLAIM-812.md)). The paper
itself has no dynamical content beyond its Outlook.

## Note of 2026-11-21: Hoogland, Wang, Farrugia-Roberts, Carroll, Wei & Murfet, read

Supports the claim's weak half, leaves its strong half untested, and
qualifies it ([ARG-tmpfh555](../arguments.d/ARG-tmpfh555.md); [NOTE-tmp2pgi8](../notes.d/NOTE-tmp2pgi8.md), [THEORY-tmpr9w2r](../theory.d/THEORY-tmpr9w2r.md)).

- **The weak half, supported in two small models.** Plateaus of the
  estimated coefficient divide training of a two-layer attention-only
  language model and a two-layer in-context regression model into stages
  that recur across five seeds, and "these changes in degeneracy coincide
  with significant changes in the internal computational structure and the
  input/output behavior of the transformers". That is "leave their mark in
  local learning coefficients".
- **The strong half, untested.** The authors use the singular learning
  process as an analogy ("an analogy to the singular learning process
  informs our methodology for stage division", §2); its link to training
  "remains to be understood" (§5); they never call a stage a change of
  dominant singular region.
- **The decreases qualify it.** Three stages lower the estimate (LM3,
  LR3, LR4). A crossover to a richer, higher-λ region, this claim's
  transition, produces increases; the authors call a full account "an open
  problem" (§8). The decreases are [QUESTION-tmphkb1w](../questions.d/QUESTION-tmphkb1w.md).
- **The estimator.** nβ is 21.7 and 66.7, not n/log n, with γ fixed, so a
  rise can be directions stiffening past the estimator's cut-off as much
  as a change of region ([CLAIM-812](CLAIM-812.md)).

The bearing on the owner's U23 itself ([CLAIM-834](CLAIM-834.md)) is noted there by the
filing of the other readings of this batch.

## Note of 2026-11-22: Lee, Smith, Adam and Hoogland, and Yang, read

- **Lee et al. (THEORY-tmpm3ux2): supports the weak half by the same
  analogy; leaves the strong half open.** The paper adopts this reading's
  picture, phases competing in a local free energy nL + λ log n with
  first-order transitions between them (A.2), and uses it to predict
  influence dynamics that are then observed. But it too models SGD by the
  Bayesian process and names the link as its "primary theoretical gap"
  (§5), and it never measures a change of dominant singular region. It
  adds that at equal loss a "Type-B" transition lowers the LLC (A.2),
  which is the qualification this claim's earlier note records. An
  analogy; no edge.
- **Yang (THEORY-tmpu0f9k): contrast.** No crossover in n; a training-time
  bifurcation in one parameter of a detached probe, on the dynamical side
  of the transitions this claim keeps apart.
