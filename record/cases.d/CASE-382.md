---
number: 382
status: Proposed
formerly:
- CASE-tmprt0hl
title: 'Fitting the expected-value-of-control effort-cost model to 122 participants'' cognitive-effort-discounting choices: a softmax over net value r − c(n) recovers an increasing cost of control and beats a reward-only model, so for about three-quarters of agents the control intensity elected falls as its cost rises, while a need-for-cognition minority seek effort'
version: 1
standing: documented
kind: executed-study
tags:
- behavioral-integration
- motivation
- cognition
- self-governance
date: '2026-11-22'
line:
- will-organization
bears_on:
- QUESTION-054
illustrates:
- CLAIM-358
- CLAIM-162
---
<!-- inactive-ok-file: CLAIM-358 CLAIM-162 THEORY-070 — Proposed; the claims this study illustrates and the EVC account it fits, all open -->
<!-- inactive-ok-file: CLAIM-981 — new in this batch; the finding this study grounds -->

# CASE-382: Fitting the expected-value-of-control effort-cost model to 122 participants' cognitive-effort-discounting choices: a softmax over net value r − c(n) recovers an increasing cost of control and beats a reward-only model, so for about three-quarters of agents the control intensity elected falls as its cost rises, while a need-for-cognition minority seek effort

## Why this study

[LEAD-128](../leads.d/LEAD-128.md) asks for a fit of the expected-value-of-control model
([THEORY-070](../theory.d/THEORY-070.md), Shenhav, Botvinick & Cohen 2013, [LIT-585](../literature.d/LIT-585.md)) in which
control intensity falls with its cost. [THEORY-070](../theory.d/THEORY-070.md) is the ground of
[CLAIM-358](../claims.d/CLAIM-358.md) and [CLAIM-162](../claims.d/CLAIM-162.md) and is kept Proposed partly for want of
exactly this: its `promote_when` (1) asks for "a fit of the EVC computation
to behaviour in which control intensity ... rises with the payoff for
control at fixed difficulty and falls with its cost, better than a model
without the cost term." No such fit was in the record.

A search of open literature (Europe PMC, arXiv) found no published fit that
plainly demonstrates the *cost* direction as its model-compared result. The
closest open EVC accumulator fits demonstrate the complementary *payoff*
direction — Leng, Yee, Ritz & Shenhav (2021, *PLoS Comput Biol*, PMC8746743,
CC BY) fit incentive-driven adjustments of drift rate and threshold; Masís
Obando, Musslick & Cohen (2025, *PNAS*, PMC12595486) show more control when
a task is learnable. So the fit was made here, as the lead provides for.

## The data

The Cognitive Effort Discounting (COG-ED) choices of Scheffel and colleagues,
"Need for Cognition is associated with a preference for higher task load in
effort discounting" (2023, *Scientific Reports*, PMC10636210, CC BY), shared
on the Open Science Framework (project vnj8x, "Cognitive and Affective
Discounting", **CC-BY 4.0**, public). 122 participants, 4428 binary choice
trials. Each trial offers two options; each is a pair (n, r), where n is an
n-back level (1–4, the cognitive-control intensity on offer) and r its
monetary reward in euros. Within a pair one level is held at a fixed 2€ and
the other's reward is titrated over six bisection steps to the indifference
point. The downloads were fetched to the session scratchpad only and are not
committed; no email or personal data was sent to any service ([ADR-008](../decisions.d/ADR-008.md)).

## The model

One agent electing how much control to deploy. The net subjective value of an
option is V(n, r) = r − c(n), with c(1) := 0; c(n) is the intrinsic cost of
exerting control at intensity n, the term [THEORY-070](../theory.d/THEORY-070.md) adds to the payoff.
Choice is by softmax, P(choose A) = logistic(β·(V_A − V_B)). This is the EVC
computation applied to revealed choice: payoff traded against an
intensity-dependent cost, the optimal choice maximising net value. The full
model (β and c(2), c(3), c(4) free) is compared against a reward-only null
(all c(n) = 0). A per-participant variant uses a linear cost c(n) = k·(n−1),
so k is each agent's marginal cost of control in euros per n-back level.
Maximum likelihood, numpy/scipy, CPU, single BLAS thread; scripts, synthetic
parameter-recovery and model-comparison tests, and how to rerun are under
scratch/studies/lead-128/, with all numbers in fit_result.json.

## What it found

1. **Subjective value falls monotonically with control intensity.** Group
   mean subjective value (the paradigm's own: titrated level = 1, fixed level
   = final titrated reward / 2€) is 0.92, 0.89, 0.78, 0.60 for 1- to 4-back.
   The agent must be paid more to accept a higher intensity, so at a fixed
   reward it elects less control. This reproduces the source article's group
   result, model-free.
2. **A per-participant cost fit is positive for about three-quarters.**
   Median marginal cost of control k = 0.26 €/level (IQR [−0.00, 0.52]).
   Of 116 participants fit, 75% have k > 0 — control intensity falls as its
   cost rises — and 74.6% are effort-averse counting the six separable cases
   (four always avoided the higher-effort option, two always sought it).
3. **The cost term is required.** Over all 4428 trials the full model beats
   the reward-only null: likelihood-ratio χ²(3) = 10.5, p = 0.015; AIC
   5809.8 vs 5814.3 (Δ = 4.5). The pooled cost curve increases,
   c = {2: −0.02, 3: 0.03, 4: 0.28} €, concentrated at 4-back, and β = 0.59
   > 0 (an option is chosen more as its reward rises — the payoff side).

## What it can show

That the EVC effort-cost computation fits real choices, and that for the
modal agent, and in the group-mean subjective value, the control intensity
elected falls as the cost of that control rises while payoff is held fixed —
the direction [LEAD-128](../leads.d/LEAD-128.md) asked for and the term that, on [THEORY-070](../theory.d/THEORY-070.md),
gives escalation the price [CLAIM-358](../claims.d/CLAIM-358.md) says a learned accommodation
saves. The payoff side of `promote_when` (1) appears in the same fit (β > 0)
and, in the accumulator form, in the published incentive fits named above; so
both halves of the condition are now evidenced, the cost half here. The
finding is stated as [CLAIM-981](../claims.d/CLAIM-981.md), which this study grounds.

## What it cannot show

- **Not the accumulator-parameter or conflict-adaptation operationalisation.**
  [THEORY-070](../theory.d/THEORY-070.md)'s `promote_when` (1) measures intensity "by an accumulator
  parameter or by conflict adaptation." This study measures it by revealed
  choice of effort level — a third operationalisation. Whether it meets the
  condition closely enough to promote [THEORY-070](../theory.d/THEORY-070.md) is the owner's call; no
  status is changed here.
- **Not a universal law.** About a quarter of participants are effort-seeking
  (k < 0), which is the source article's own finding (it reports 34.5%
  preferring a load above 1-back). The single-population pooled fit is the
  weakest of the three views — BIC favours the null (5835.4 vs 5820.7),
  the one pooled cost curve being diluted by that minority. The per-participant
  fit is the headline; the law holds for the modal agent, not all.
- **Not the cost's form or source.** c(n) is estimated per level or as a
  linear slope; the study does not adjudicate the cost function's shape, nor
  whether it is intrinsic or an opportunity cost ([THEORY-070](../theory.d/THEORY-070.md) leaves this
  open), nor anything about dACC: no dissociation of specifying from
  implementing is touched, so `promote_when` (2) is untouched.
- **Not amortised supervisory cost.** [CLAIM-358](../claims.d/CLAIM-358.md)'s amortization is over
  recurring conflicts; this is single-shot effort pricing. It supplies the
  per-encounter cost that claim's accounting presupposes, not the recurrence.
