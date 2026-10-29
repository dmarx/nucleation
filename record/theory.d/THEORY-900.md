---
number: 900
status: Active
formerly:
- THEORY-tmp4ahqw
title: "A systematic review of 116 studies of avoidance learning in healthy humans finds the evidence contradicting two-factor and other associative theories and favouring expectancy and inference-based accounts, but also finding residual avoidance after the outcome is visibly removed, which a purely inferential account does not predict"
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Promoted by the thirteenth status review (ADR-057; ADR-047's
    evidence ruling, read in full in NOTE-1134). The title claims no
    more than the source showed and is unchanged. The promote_when moves
    unchanged to QUESTION-328, as THEORY-285's did to QUESTION-303.
    CLAIM-446 now lists this reading under corroborated_by, not grounds
    (ADR-058): the claim's argument does not rest on it.
tags:
- learning-and-conditioning
- cognition
date: '2026-10-24'
source:
- LIT-1477
bears_on:
- QUESTION-328
summary: >-
  Mancinelli & Bach (preprint 2025; NBR 2026), [LIT-1477](../literature.d/LIT-1477.md), read in full
  in [NOTE-1134](../notes.d/NOTE-1134.md). A PRISMA review without meta-analysis, searched to
  December 2024, of studies with shock or noise in healthy volunteers. The
  verdict is the authors' scoring of five theories against phenomena they
  rate for robustness; no model was fitted. They argue current paradigms
  are too simple to expose where inference gives way to Pavlovian
  control.
corroborates:
- CLAIM-446
---
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim and reading this bears on, named -->

# THEORY-900: A systematic review of 116 studies of avoidance learning in healthy humans finds the evidence contradicting two-factor and other associative theories and favouring expectancy and inference-based accounts, but also finding residual avoidance after the outcome is visibly removed, which a purely inferential account does not predict

## Source

Mancinelli & Bach, [LIT-1477](../literature.d/LIT-1477.md), read in full in [NOTE-1134](../notes.d/NOTE-1134.md) from the
PsyArXiv preprint: pp. 2, 9–28, and Figs 1 and 4 (pp. 50, 53).

## What was actually shown

Against two-factor theory and safety-signal theory:

- Avoidance is learned when the response cancels the US without ending the
  CS, in eight studies with no counterevidence (p. 12).
- An avoidance response is selected for a new CS that predicts the same US,
  without training (US-based transfer, p. 14), and spreads through learned
  stimulus equivalence (latent transfer, p. 14).
- Avoidance appears after Pavlovian conditioning alone, without any
  avoidance training (p. 16): "the anticipation of a US is sufficient to
  elicit an AR" (p. 17).
- Fear responses are not necessary for avoidance to be maintained, and
  intentions to avoid modulate them (pp. 11, 25).

Against a purely inferential account:

- "AR are consistently emitted despite signalled US omission, suggesting
  that avoidance is not fully goal-directed" (p. 22), with no evidence of
  habits forming through overtraining. Hence avoidance "can not be fully
  inferential in the first place, directly challenging expectancy theory"
  (p. 23).

The authors' summary: "a substantial body of evidence supports expectancy
theory and aligns with an inference-based algorithmic framework. However,
this perspective is tempered by findings of Pavlovian influences in certain
experiments" (p. 28).

What could have come out otherwise: avoidance could have required CS
termination, as Mowrer predicted, or could have stopped once the outcome
was visibly gone, as expectancy theory predicts.

## What this does not say

- **That inference explains clinical avoidance.** No patients, and the
  authors say "all our theoretical deductions are specific to the
  paradigms" in the literature (p. 28), which are signalled, instructed and
  simple.
- **That a computational inferential model has been tested.** None
  exists for avoidance: "there is no computational counterpart of
  expectancy theory" (p. 6).
- **That residual avoidance is habit.** No study found the overtraining
  interaction that would show it; a small subset of participants carries
  the effect.

## Connections

- **[CLAIM-446](../claims.d/CLAIM-446.md).** The claim's account is inferential at its core (the
  likelihood ratio under avoidance), and this verdict is favourable to
  that framing. The residual avoidance after signalled omission is the
  laboratory case of defence outlasting a corrected expectation, which the
  claim needs, though its explanation here is Pavlovian rather than
  governance.
- **[THEORY-910](THEORY-910.md).** Brown et al. recast expectancy theory in
  temporal-difference terms; this review says the existing
  temporal-difference models are model-free and fail the inferential
  phenomena.
