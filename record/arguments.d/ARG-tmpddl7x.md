---
status: Proposed
title: "Gutenkunst and colleagues' survey of seventeen systems-biology models, with its one comparison of a collective fit against direct measurement, as evidence, supports the claim that parameter and behavioural complexity come apart in such models, across the collection for loose parameters and in one model for tight predictions"
version: 1
form: evidence
grounds:
- THEORY-tmpks8pd
concludes:
- CLAIM-820
uses:
- TERM-140
tags:
- model-comparison
- information-geometry
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
summary: >-
  CLAIM-820 grounded LIT-2999 unread. Read (NOTE-tmp1feoo), the survey
  shows sloppy spectra and loose parameters across seventeen models and
  tight predictions from loose parameters in one, the PC12 model; it
  supports the claim's relativity to the observables fitted, and its
  rescaled model tells against the spread being an artefact of scales.
  The reading replaces the LIT in the claim's grounds. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-820 TERM-140 THEORY-tmpks8pd — Proposed; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" or from this reading -->

# ARG-tmpddl7x: Gutenkunst and colleagues' survey of seventeen systems-biology models, with its one comparison of a collective fit against direct measurement, as evidence, supports the claim that parameter and behavioural complexity come apart in such models, across the collection for loose parameters and in one model for tight predictions

## The inference

CLAIM-820: when predictions depend on a few stiff combinations, a model
can be hard to fit and still predictive. THEORY-tmpks8pd: in all
seventeen models the spectra "span many decades" with "no well-defined
cutoff"; an idealized fit "leaves many parameters with greater than 100%
uncertainty" in most of them; and in the PC12 model, after a fit in which
"Not a single parameter was constrained to better than a factor of 50",
the ERK prediction is tight, while matching it by measurement needs "all
24 involved parameters" to ±25%.

## Critical questions

- **Is the evidence what the claim needs?** For the first half (hard to
  fit), across the collection: yes. For the second (still predictive), in
  one model and one prediction (Fig. 4; others in an unread supplement).
  The paper's abstract generalizes it ("suggests that modelers should
  focus on predictions rather than on parameters"); the evidence does not
  test it in the other sixteen.
- **Is it relative to what is observed, as the claim says?** Yes, in the
  paper's own words: "exhaustive experiments designed to decouple the
  system and separately measure each parameter will naturally not yield
  sloppy parameter sensitivities."
- **Does it meet the claim's defeater?** The second clause of
  defeated_if asks whether the spread is an artefact of parametrization.
  The paper answers with the bare parametrization being "fundamental to
  the system, not an artifact" and with a rescaled model (every rate and
  concentration set to 1) that "remains sloppy". That tells against an
  artefact of scales; it does not show invariance under every
  reparametrization, which no eigenvalue spread has (TERM-140).
- **Would the evidence be expected if the claim were false?** Loose
  parameters alone would be: an unidentifiable model has them too. What
  is specific is a tight prediction from them, which rests on one model.

## Verdict

Supports the claim for systems-biology models of this kind: the
coming-apart of parameter and behavioural complexity is shown for
parameters across the collection and for one prediction in one model.
Proposed.
