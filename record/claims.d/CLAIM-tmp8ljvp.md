---
status: Proposed
title: 'Overconsolidation, a generalization of overfitting: relative to a declared family of future demands, continued stabilization of a learner''s organization can keep improving its present objective while raising the cost of acquiring, recovering or reaching other capabilities, so a learner can learn itself into a trap without overfitting its data; it is a failure only relative to that declared family and horizon'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Evidence that what is called overconsolidation is always one of the
  failures already named, overfitting to a data distribution or forgetting
  of held capabilities, so that no case shows present competence rising
  while the cost of a declared later acquisition rises and held
  capabilities are kept; or that the rise in acquisition cost is always
  undone by an alternative route the same learner already has, as when
  in-context adaptability rises while fine-tuning plasticity falls, so that
  nothing is lost but the place where learning happens.
tags:
- learning-theory
- representation-learning
- complex-systems
date: '2026-11-19'
line:
- learned-structure
- readiness
rests_on:
- CLAIM-675
- CLAIM-569
complements:
- CLAIM-695
- CLAIM-520
- CLAIM-605
- CLAIM-tmp1l2s7
bears_on:
- QUESTION-tmpwqepn
summary: >-
  The owner's generalization, in A's wording. A48 §8 named "the
  possibility of learning oneself into a trap"; the owner answered at U22
  of the exchange "Topological protection explained" (2026-11-19): "sounds
  like you've landed on a generalization of overfitting that I think
  captures the more recent notion of "over cooking" a learning process."
  A50 then separated overfitting, a failure across a distribution of
  examples, from what it named overconsolidation, which "can happen
  without conventional overfitting", and A71 §8 gave its signature: the
  operational frontier grows on familiar tasks while the developmental
  frontier does not contain its predecessor ([CLAIM-tmp1l2s7](CLAIM-tmp1l2s7.md)). The record
  held the trajectory form for support ([CLAIM-675](CLAIM-675.md)), plasticity loss as a
  reading ([THEORY-1353](../theory.d/THEORY-1353.md)) and the RL case in pass@k terms ([CLAIM-695](CLAIM-695.md)); it
  held no general claim for training.
---
<!-- inactive-ok-file: LIT-tmpco2kf LIT-tmpkfcwr LIT-tmpm4bnq LIT-tmpq5g0q — Deferred; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-695 CLAIM-tmp1l2s7 THEORY-1353 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-tmp8ljvp: Overconsolidation, a generalization of overfitting: relative to a declared family of future demands, continued stabilization of a learner's organization can keep improving its present objective while raising the cost of acquiring, recovering or reaching other capabilities, so a learner can learn itself into a trap without overfitting its data; it is a failure only relative to that declared family and horizon

## The claim

The owner, at U22 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf), on A48
§8's heading "The possibility of learning oneself into a trap":

> sounds like you've landed on a generalization of overfitting that I think captures the more recent notion of "over cooking" a learning process.

A50 §7 gave the general form: "the consolidation that makes acquired
capabilities inexpensive to use can also make alternative capabilities
expensive to acquire." Its toy model: value V(s) = P0(s) − λA(s) − C(s)
over training time s, with present performance P0 rising and the cost A
of a later acquisition rising too, so that "The optimal time to stop
learning one thing can precede the point at which one has stopped
improving at that thing." With P0 = 1 − e^(−s), A = a + αs and no training
cost, V′ = e^(−s) − λα, so for 0 < λα < 1 the optimum is s* = ln(1/(λα))
(A50 §1; checked).

## Its signature

In A71 §8's terms ([CLAIM-tmp1l2s7](CLAIM-tmp1l2s7.md)), the operational repertoire on a
declared set of familiar tasks contains its predecessor while the
developmental frontier, what can be learned within an acquisition budget,
does not. "The learner has improved its established competence but has
not preserved every previously affordable route to further competence."
[CLAIM-695](CLAIM-695.md) is the RL case: low-budget reliability gained, high-budget
coverage lost.

## What it is not

- **Not overfitting.** Overfitting fails across a distribution of
  examples; this can occur on a learner that generalizes on its training
  distribution.
- **Not forgetting.** Held capabilities may be kept; what rises is the
  cost of those not yet held.
- **Not one scalar.** Reusable structure, the capacity to acquire new
  structure and the capacity to retain old structure can move apart (A54
  §5, after Raghu et al.'s feature reuse, [LIT-tmpm4bnq](../literature.d/LIT-tmpm4bnq.md)), and in-context
  adaptability can rise while fine-tuning plasticity falls (A56 §3), which
  is defeated_if's second clause.
- **Not a failure in itself.** "That doesn't prove the learning was
  suboptimal; the lost adaptability might have little value in the
  relevant future" (A71 §8). A specialist in a stable environment is not
  overconsolidated. [CLAIM-520](CLAIM-520.md)'s conditional value of a corrective capacity
  is the same point for audits.
- **Not new as an objective.** Meta-learning's objective already targets
  future adaptability (A54 §3). What the claim adds is the name of the
  failure and its signature in resource terms.

## Candidate mechanisms (A50 §2–4; A's)

Overcompression: a learned equivalence stays sufficient for the present
target and becomes insufficient for the next ([CLAIM-152](CLAIM-152.md), [CLAIM-350](CLAIM-350.md)).
Plasticity loss, read as depletion of uncommitted capacity ([THEORY-1353](../theory.d/THEORY-1353.md),
whose relief by a query–key reset counts only if background skills
survive, per [CLAIM-347](CLAIM-347.md)'s note of 2026-11-04). Policy entrenchment. The
amortization trap, in which operating cost falls while reconfiguration
cost rises ([CLAIM-569](CLAIM-569.md)). Inquiry traps, in which the learner stops seeking
the evidence that would change it ([THEORY-285](../theory.d/THEORY-285.md), [CLAIM-466](CLAIM-466.md)).

## Rests on

- [CLAIM-675](CLAIM-675.md): the same capabilities now can leave different capabilities
  later, demonstrated for support; this claim says training can be such a
  process for the learner itself.
- [CLAIM-569](CLAIM-569.md): what it costs to acquire a form is not fixed by what it costs
  to keep it.

## Evidence wanted

Springer et al. ([LIT-tmpq5g0q](../literature.d/LIT-tmpq5g0q.md)), Han et al. ([LIT-tmpkfcwr](../literature.d/LIT-tmpkfcwr.md)) and Dohare et
al. ([LIT-tmpco2kf](../literature.d/LIT-tmpco2kf.md)), registered unread, are the empirical cases A cited.
[CASE-tmphsr99](../cases.d/CASE-tmphsr99.md) is the owner-requested test on Pythia checkpoints.
