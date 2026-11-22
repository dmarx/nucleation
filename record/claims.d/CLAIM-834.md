---
number: 834
status: Proposed
formerly:
- CLAIM-tmpp83vc
title: 'Singularity theory''s account of phase transitions in learning as resolutions of singularities might be useful for the account of progressive, coarse-to-fine learning the exchange had built'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that singular learning theory adds nothing to the account of
  progressive learning under either reading of the suggestion: that no
  transition in learning is the network carrying out a resolution
  (reading a, CLAIM-802), and that representational stages, with
  local learning coefficients measured across them, coincide with no
  change in the dominant singular region and are fully accounted for by
  concentration, spectral detectability and cone geometry without
  singular geometry (reading b, CLAIM-823). A transition the theory
  cannot compute for a large network does not defeat it; the claim is that
  the account might be useful, not that it is tractable everywhere.
tags:
- learning-theory
- loss-landscapes
- model-comparison
date: '2026-11-21'
line:
- learned-structure
grounds:
- THEORY-087
- THEORY-1275
- THEORY-975
- THEORY-2160
- LIT-2960
- LIT-3000
bears_on:
- QUESTION-363
- QUESTION-217
- QUESTION-514
summary: >-
  The owner's U23 in the exchange "Rich Get Richer Power Laws"
  (2026-11-21), after the exchange had described progressive learning
  through concentration of measure, spectral detectability and entailment
  cones: "singularity theory has an account for phase transitions in
  learning as resolutions of singularities that might be useful here".
  The thesis and its wording are the owner's, at U23. "As resolutions of
  singularities" admits two readings that would be filed differently, and
  both are filed as alternatives for the owner to choose: (a) training
  carries out a resolution ([CLAIM-802](CLAIM-802.md)), and (b) a transition is a
  change of the dominant singularity, with resolution as the tool that
  computes its learning coefficients ([CLAIM-823](CLAIM-823.md), A37's reframing).
---

<!-- inactive-ok-file: THEORY-2160 — Proposed or new; the reading of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-811 CLAIM-807 CLAIM-802 CLAIM-823 ARG-132 — claims filed with this one -->
<!-- inactive-ok-file: THEORY-2163 THEORY-2164 — Proposed readings, filed 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-812 THEORY-2157 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# CLAIM-834: Singularity theory's account of phase transitions in learning as resolutions of singularities might be useful for the account of progressive, coarse-to-fine learning the exchange had built

## The claim

U23, verbatim: "singularity theory has an account for phase transitions
in learning as resolutions of singularities that might be useful here".
"Here" is the exchange's account of progressive, coarse-to-fine learning,
which so far rested on concentration of measure, spectral detectability
(BBP) and entailment cones.

## Two readings, filed as alternatives

"As resolutions of singularities" can be read two ways, and they would be
filed differently, so each is filed as an alternative. The owner chooses.

- **Reading (a), training performs a resolution** ([CLAIM-802](CLAIM-802.md)): a
  phase transition is the network carrying out, or passing through, a
  blow-up of a singular point. The statement is the assistant's.
- **Reading (b), a change of the dominant singularity** ([CLAIM-823](CLAIM-823.md)):
  regions with different fits and learning coefficients compete in the
  free energy, the dominant one can switch as n grows, and resolution is
  how each coefficient is found. The wording is A's, at A37 §3 and §5.

The assistant's view, that the record's [CLAIM-305](CLAIM-305.md) tells against reading (a)
and leaves (b), is argued in [ARG-132](../arguments.d/ARG-132.md); it is a verdict on the
readings, not a choice between them for the owner.

## How the exchange developed it

- **Dynamics are separate.** "The fact that a singularity exists does not
  tell us when or whether gradient descent will move away from it" (A37
  §4). Plateaus near singularities are Amari's and Wei's work
  ([LIT-2960](../literature.d/LIT-2960.md), [LIT-3000](../literature.d/LIT-3000.md), read on 2026-11-21; the dated note
  below). How slowly a flow leaves or
  reaches a singular point is not fixed by its learning coefficient
  ([CLAIM-811](CLAIM-811.md)).
- **Three transitions** (A37 §5): Bayesian (the dominant posterior region
  changes), dynamical (the optimizer's trajectory reorganizes) and
  semantic (a new distinction becomes stable and decodable). "These may
  be related, but they're not equivalent." The record holds the first two
  apart in [QUESTION-363](../questions.d/QUESTION-363.md). The third, and A43's split of the semantic event
  into encoded, stable and expressed, is added there as a dated note of
  this date.
- **A worked mechanism** in which a feature switches on at a threshold
  where the local coefficient dips from 1 to 3/4 is [CLAIM-807](CLAIM-807.md).

## A correction to A37's chart

A37 §5 illustrates the crossover with a chart captioned F_A = 0.02n +
0.3 ln n and F_B = 0.012n + 0.8 ln n. Its F_A series matches the caption.
Its F_B series does not: the chart gives F_B = 4.224, 5.708 and 18.908 at
n = 100, 200 and 1000, where the caption's formula gives 4.884, 6.639 and
17.526. Under the caption's formulas the crossover is at n ≈ 370 (solving
0.008n = 0.5 ln n), not between 200 and 300 as plotted. The assistant
checked both with `python3 -I` (`t5/check2.py`). The qualitative point
survives: the simpler region wins at small n and the richer one later.

## What it does not say

It does not say that every stage of learning is a singular transition,
nor that the Bayesian order in n is the training order in t. That bridge
is [QUESTION-363](../questions.d/QUESTION-363.md), open.

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

## Note of 2026-11-21: Amari, Park & Ozeki (2006), Wei et al. (2008) and Hoogland et al., read

Three readings bear on U23; none of them decides between its readings.

- **Amari, Park and Ozeki: background, and A37's "dynamics are separate"
  borne out** ([NOTE-2255](../notes.d/NOTE-2255.md), [THEORY-2163](../theory.d/THEORY-2163.md)). Their account of learning
  near singularities uses the Fisher metric and fast and slow manifolds,
  never resolution: algebraic geometry is "Another general framework …
  which we do not summarize here" (p. 1024). A smooth prior favours
  singular points "with an infinitely large factor" (p. 1029), which is
  consonant with reading (b), the Bayesian competition between regions,
  but gives no account of a transition.
- **Wei and colleagues: the same point, sharper** ([NOTE-2254](../notes.d/NOTE-2254.md),
  [THEORY-2164](../theory.d/THEORY-2164.md)). One singular set is reached, crossed or left according
  to the signature of a residual matrix and a conserved quantity of the
  flow (Theorem 1, Eq. 3.15); its existence does not fix the dynamics. No
  learning coefficient appears, and no transition is read as a
  resolution. Background for reading (b) at most.
- **Hoogland and colleagues, read by the other filer in this batch**
  ([LIT-2966](../literature.d/LIT-2966.md), [NOTE-2248](../notes.d/NOTE-2248.md), [THEORY-2160](../theory.d/THEORY-2160.md)), are the measured stages
  reading (b) would have to meet. The paper calls its link to singular
  learning an analogy: "an analogy to the singular learning process
  informs our methodology for stage division"; it never calls a stage a
  singularity; and, by that reading, three of its stages show decreases of the estimated
  local learning coefficient that it does not explain (of one, "This may
  be related to interaction between heads"). Neither reading of U23
  accounts for those decreases: reading (a) has no stage at which training
  carries out a resolution, and reading (b), as filed, has the dominant
  region move to a richer one as n grows, with a higher coefficient,
  where the paper's coefficient falls. Whether a fall can be a change of
  dominant region at fixed n over training time is the bridge of
  [QUESTION-363](../questions.d/QUESTION-363.md), still open.

## Note of 2026-11-21: grounds

Hoogland et al. ([LIT-2966](../literature.d/LIT-2966.md)) is now read ([NOTE-2248](../notes.d/NOTE-2248.md)), so its place in this claim's grounds passes to the reading's account, [THEORY-2160](../theory.d/THEORY-2160.md). As the reading found, that paper calls its link to singular learning "an analogy" and never calls a stage a singularity, so it grounds only that stages leave a mark in the learning coefficient. The note is the assistant's (Claude, in this session).

## Note of 2026-11-21: the step to the new ground

The step that puts [THEORY-2160](../theory.d/THEORY-2160.md) in this claim's grounds is the one [ARG-156](../arguments.d/ARG-156.md) argues for reading (b), [CLAIM-823](CLAIM-823.md): Hoogland et al. ground only that stages leave a mark in the learning coefficient. That is all this claim takes from it. The note is the assistant's (Claude, in this session).
