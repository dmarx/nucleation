---
status: Active
title: A state sufficient for a family of decisions under a model makes the rest
  of an inquiry's history worthless for those decisions, and it can stop being sufficient
  when a source is discredited, the model is revised or the decisions change
version: 1
role: thesis
defeated_if: >-
  An error in either construction: a sufficient statistic under a fixed model whose
  history improves the Bayes risk of a decision in the same family, or two samples
  with equal means whose remaining reading after dropping the first coincides.
tags:
- mathematical-statistics
- epistemology
date: '2026-10-15'
line:
- formal-apparatus
- nucleating-argument
answers:
- QUESTION-tmpzf5on
grounds:
- CASE-tmp390tl
- CASE-tmph4ds5
complements:
- CLAIM-152
summary: >-
  A10's answer to the owner's U10, with A8's fourth case and A10's normal constructions
  ([CASE-tmp390tl](../cases.d/CASE-tmp390tl.md), [CASE-tmph4ds5](../cases.d/CASE-tmph4ds5.md)). Under a fixed, correctly specified model a sufficient
  posterior makes the history redundant for those decisions. The same sample mean
  that sufficed cannot say which reading remains when one instrument is discredited,
  or test a mixture. Sufficiency was always relative to the model and the family.
  [CLAIM-152](CLAIM-152.md) says the same of individuation by target; this says it of a retained
  state over time.
supports:
- CLAIM-tmp7t44x
---
<!-- inactive-ok-file: CLAIM-tmp7t44x — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# CLAIM-tmpp7a8x: A state sufficient for a family of decisions under a model makes the rest of an inquiry's history worthless for those decisions, and it can stop being sufficient when a source is discredited, the model is revised or the decisions change

## The claim

**Redundancy.** A10: "If a current epistemic state is genuinely
sufficient for the entire family of future decisions under consideration,
then preserving its history cannot improve ideal decision performance.
That's not an empirical conjecture. It follows from what sufficiency
means." [CASE-tmp390tl](../cases.d/CASE-tmp390tl.md): under a correctly specified model with observations
conditionally independent given Θ, p(Θ | E₁:t) is all a Bayesian updater
needs.

**Relativity.** [CASE-tmph4ds5](../cases.d/CASE-tmph4ds5.md), from A10 §2. Two readings of μ, X₁, X₂ ~ N(μ, σ²)
independent with σ known. History A has (0, 10), history B (4, 6). Both
have mean 5, and since σ is known both likelihoods for μ are proportional
to exp(−(μ − 5)²/σ²). The mean is sufficient and the histories are
indistinguishable for inference about μ. Now instrument 1 is found
miscalibrated and X₁ must be dropped. History A leaves 10 and history B
leaves 6, and the mean cannot say which. Introduce a two-component
mixture and the mean cannot test it either, since the histories differ
in spread. A18: "The earlier statistic has not somehow become
mathematically incorrect. Its sufficiency was conditional on a
specification that has changed."

## Why it is Active

Both halves follow from the definition of sufficiency and the stated
constructions, which were checked for this entry. They hold whatever any
line concludes ([ADR-040](../decisions.d/ADR-040.md)).

## What it bears on

- [CLAIM-152](CLAIM-152.md) makes sufficiency relative to its target. This adds the
  model and the decision family, and change over time.
- [CLAIM-tmp2rwpl](CLAIM-tmp2rwpl.md) is not a special case. A marginal is not sufficient even under
  the original model; here the state is sufficient and stops being so.
- A10 drew the consequence for history: "justificatory history is not
  extra information beyond a sufficient state." [CLAIM-tmp7t44x](CLAIM-tmp7t44x.md) takes it up.
- A10 §2 noted what [CASE-tmph4ds5](../cases.d/CASE-tmph4ds5.md) needs is "a source-indexed data record", not
  the researcher's argument. That is an objection to reading this as a
  case for keeping justifications.
