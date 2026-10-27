---
number: 1022
status: Proposed
formerly:
- THEORY-tmpb0s0r
promote_when: >-
  Evidence that accounts for the weak firings, not more strong ones: for
  the mixed3b curve units, a sample of dataset positions drawn across the
  whole activation distribution (not activation-binned for strong cases)
  in which the units' activation is predicted from curve properties alone,
  for instance by a hand-written curve detector or the article's own
  promised reimplementation, with most of the variance, or most of the
  contribution to expected value now unexplained, accounted for; and an
  intervention showing that downstream units use the curve units' output as
  curve evidence. Refuted if a coherent secondary stimulus class accounts
  for a substantial share of the weak firings, or if the reimplementation
  matches the strong responses but not the weak ones. Further feature
  visualizations, top-activating examples or synthetic curves cannot settle
  it: they are the evidence it already rests on.
title: 'The curve units of InceptionV1''s mixed3b detect curves as such: curves, not correlated stimuli, cause their firing, they respond to curves in general whatever their colour, fill or texture, and they have no meaningful secondary function, their weak responses to edges and angles being part of the same curve-detecting algorithm, as Cammarata, Goh, Carter, Schubert, Petrov and Olah claim'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1198, as the claim the measured
    THEORY-1028 leaves out (ADR-047 v4). The authors grade their
    purity evidence themselves: any secondary function "would need to be
    rare", and the mechanistic support is promised for the next article.
tags:
- representation-learning
date: '2026-10-27'
source:
- LIT-1575
extends:
- THEORY-1028
summary: >-
  Cammarata et al. (2020), [LIT-1575](../literature.d/LIT-1575.md), read in [NOTE-1198](../notes.d/NOTE-1198.md). The
  article's four claims (causality, generality, purity, family) taken
  together, as the authors state them. Generality and the family are
  measured ([THEORY-1028](THEORY-1028.md)). Causality rests on feature visualization and
  attribution. Purity rests on feature visualization with a diversity term
  and activation-binned labels, while most of the unit's firings, and 45%
  of its contribution to expected value, are not shown to be curves.
---
<!-- inactive-ok-file: THEORY-1013 — Proposed; the general account this case would serve, cited as open -->
# THEORY-1022: The curve units of InceptionV1's mixed3b detect curves as such: curves, not correlated stimuli, cause their firing, they respond to curves in general whatever their colour, fill or texture, and they have no meaningful secondary function, their weak responses to edges and angles being part of the same curve-detecting algorithm, as Cammarata, Goh, Carter, Schubert, Petrov and Olah claim

## Source

Cammarata et al. (2020), *Curve Detectors*, [LIT-1575](../literature.d/LIT-1575.md), read in full in
[NOTE-1198](../notes.d/NOTE-1198.md): the section "What exactly are we claiming", and the
evidence each claim is assigned.

## What is asserted

The article's four claims, in its words. **Causality**: "Curve detectors
genuinely detect a curve feature, rather than another stimulus correlated
with curves." **Generality**: they "respond to a wide variety of curve
stimuli", tolerant of radius and "largely invariant to cosmetic attributes
like color, brightness, and texture". **Purity**: they "are not
polysemantic and they have no meaningful secondary function"; weak
responses to edges or angles "are a natural extension of the algorithm".
**Family**: they "collectively span all orientations of curves".

## What the record holds toward it

- **Generality and family, measured** ([THEORY-1028](THEORY-1028.md)): synthetic curves,
  invariance to fill and colour, rotation tuning across the ten units.
- **Causality, argued**: an optimized input is always a curve, and
  attribution of activating images through the previous layer shows the
  curves in them. An optimized input shows that curves can drive the unit.
  That curves are what drive it on natural images rests on the attribution
  and labelling, for strongly firing cases.
- **Purity, argued for the strong cases**: diversity-regularized
  visualizations are all curves, and blind labels sort by activation. For
  the weak cases, where most firing happens, the authors attribute curve
  labels' presence "at least partly" to labelling error and give no
  precision–recall analysis.
- **The mechanism, promised**: "We'll see in the next article that the
  algorithm used is straightforward and understandable, and we've since
  reimplemented it by hand." That article is not held.

## Why it stays Proposed

Purity is the claim that matters for whether a unit is a feature in
[THEORY-1013](THEORY-1013.md)'s sense, and the article itself says only that a secondary
function "would need to be rare". The 45% of 3b:379's contribution to
expected value that is not curves or imperfect curves is not explained.

## What would confirm or reject it

The promote_when above.
