---
status: Proposed
promote_when: >-
  A causal-inference model of ownership with its likelihoods, prior and
  threshold fixed before the data, fitted to graded manipulations (for
  example visuotactile delay, hand offset and rotation) in one sample, that
  predicts held-out conditions, including the review's untested
  predictions on stimulation complexity and visuomotor onset, better than
  a model that sums congruence cues without a latent common cause, on a
  measure that survives an expectancy-matched control. More qualitative
  agreement with published results cannot settle it, since the model as
  stated accommodates both persistence and abolition of the illusion.
title: "A body ownership illusion arises when seen and felt or seen and performed events agree in time and place on a plausibly shaped and posed body, or when a realistic body is seen where one's own is; on the review's proposal this is Bayesian causal inference that one body part rather than two caused the visual, proprioceptive, tactile and semantic evidence, but the model is qualitative, unfitted, and flexible enough in its prior and threshold that few results could count against it"
version: 1
tags:
- self
- probabilistic-modeling
- neuroscience
date: '2026-10-18'
source:
- LIT-tmpt4bij
summary: >-
  Kilteni, Maselli, Kording & Slater (2015), [LIT-tmpt4bij](../literature.d/LIT-tmpt4bij.md), read in full in
  [NOTE-tmpy8fky](../notes.d/NOTE-tmpy8fky.md). The empirical half is a narrative review graded mainly by
  questionnaire; the reviewed studies were not checked, apart from Petkova
  and Ehrsson ([THEORY-tmpvh682](THEORY-tmpvh682.md)). The model half is two equations and a
  qualitative mapping, with a prior that includes suggestibility and an
  iterative extension that absorbs after-effects. Its own predictions are
  listed as untested.
---

# THEORY-tmp5h02h: A body ownership illusion arises when seen and felt or seen and performed events agree in time and place on a plausibly shaped and posed body, or when a realistic body is seen where one's own is; on the review's proposal this is Bayesian causal inference that one body part rather than two caused the visual, proprioceptive, tactile and semantic evidence, but the model is qualitative, unfitted, and flexible enough in its prior and threshold that few results could count against it

## Source

Kilteni, Maselli, Kording & Slater (2015), "Over my fake body", *Frontiers
in Human Neuroscience* 9:141, [LIT-tmpt4bij](../literature.d/LIT-tmpt4bij.md), read in full in
[NOTE-tmpy8fky](../notes.d/NOTE-tmpy8fky.md).

## What was actually shown

**The regularities (reviewed, not shown here).** Agreement in time (touch
within about 300 ms; movement under about 500 ms) and place (homologous
parts) induces ownership of a rubber hand or a full body. Offsets toward
the midline are tolerated, outward and large vertical ones attenuate.
Non-body shapes, a hand rotated 180° and a third-person view of a full
body at 40–100 cm inhibit or abolish it; size, length and texture
modulate it. A realistic body seen in the real body's place is owned even
under asynchronous touch, or by sight alone.

**The proposal.** p(C = 1 | m_V, x_V, x_P, s_V, s_T) ∝ p(m_V | C = 1)
p(x_V, x_P | C = 1) p(s_V, s_T | C = 1) p(C = 1), with the illusion felt
above a threshold. Each regularity is mapped onto a likelihood or the
prior. An iterative version, in which having the illusion raises the
prior and widens the likelihoods, is offered for persistence under later
conflict.

Nothing in the review could have come out otherwise: it reports no data
and fits no model. What would have counted against the proposal is a
graded manipulation whose effect on reports is not monotone in any
likelihood, and no such test is reported.

## What this does not say

- **That the brain computes this posterior.** The mapping is qualitative,
  and the authors call it a "first step".
- **That questionnaire differences are perceptual.** The review grades by
  questionnaire and does not discuss demand characteristics; the model
  places suggestibility in the prior, which accommodates expectancy
  effects without distinguishing them from perception.
- **That causal inference beats predictive coding.** The review calls
  them "conceptually analogous" in the iterative form and prefers causal
  inference for simplicity, not on a test.
- **That self-location is ownership.** Out-of-body illusions of
  self-location are classed separately.
- **Anything about the self beyond the body.** The review's "own-body
  perception" is ownership of parts and bodies; self-awareness, agency and
  the first-person perspective as a subject are not its topic.

## Connections

- [THEORY-tmpvh682](THEORY-tmpvh682.md) (Petkova and Ehrsson) is one of the regularities this
  account must explain; the review supplies the third-person comparisons
  that paper did not run.
- Bears on [NOTE-372](../notes.d/NOTE-372.md)'s C6 by classifying Lenggenhager et al.'s full-body
  illusion as self-location rather than ownership.
- A sibling of the free-energy accounts ([LIT-1181](../literature.d/LIT-1181.md)) without action: the
  conflict is resolved by inference, not by acting.
