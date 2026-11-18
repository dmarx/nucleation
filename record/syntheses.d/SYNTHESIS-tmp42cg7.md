---
status: Proposed
title: 'What a learned system retains is held relative to its readers, cues, interventions and budgets: the owner''s claim that a disposition is resource-conditional, with coverage under repeated sampling distinct from delivery; the owner''s claim that RL post-training can amortize search into the policy, sharpening or expanding per run; the assistant''s claim that where the training verifier runs at test time RL buys economy and not reach; a construction in which several queries separate readdressing, suppression and deletion and one cancellation no query reveals; and two proposed studies that would separate loss from readdressing, interference, suppression and higher cost'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  this part of the learned-structure line (latent capability, how it is
  elicited and at what cost, and how its loss is told from its
  inaccessibility) left out without a reason given; or a link this account
  states that no component states. Its standing is its components'.
tags:
- learning-theory
- representation-learning
- agency
date: '2026-11-18'
line:
- learned-structure
integrates:
- CLAIM-697
- CLAIM-695
- CLAIM-699
- CASE-271
- CASE-274
- CASE-275
summary: >-
  The account of the latent-capability part of the learned-structure line,
  filed at the synthesis review of 2026-11-18. All six components were
  filed on 2026-11-15 from the continuation of the exchange "Explain String
  Theory", and all are Proposed. The three claims' first line is
  realizability. It maps them and adds nothing.
---
<!-- inactive-ok-file: SYNTHESIS-034 SYNTHESIS-042 SYNTHESIS-tmpwrkqs CLAIM-698 CLAIM-697 CLAIM-695 CLAIM-699 CASE-271 CASE-274 CASE-275 CLAIM-576 CLAIM-182 TERM-118 THEORY-1880 THEORY-1908 ADR-075 ADR-083 ADR-084 — Proposed; the components, the entries they cite and the decisions this account follows -->

# SYNTHESIS-tmp42cg7: What a learned system retains is held relative to its readers, cues, interventions and budgets: the owner's claim that a disposition is resource-conditional, with coverage under repeated sampling distinct from delivery; the owner's claim that RL post-training can amortize search into the policy, sharpening or expanding per run; the assistant's claim that where the training verifier runs at test time RL buys economy and not reach; a construction in which several queries separate readdressing, suppression and deletion and one cancellation no query reveals; and two proposed studies that would separate loss from readdressing, interference, suppression and higher cost

## The account

- **Budgets.** CLAIM-697 (the owner's idea, A's formalization; Proposed,
  demonstrated) says a disposition's best success probability is "a
  nondecreasing function of the budget over nested procedure classes".
  Repeated sampling raises coverage to 1 − (1 − p)^N with no change of
  parameters. Coverage is not delivery: "generation, recognition and
  selection are separate capacities with separate costs". It reads
  TERM-118's "declared family of conditions" as largely the affordable
  compositions of declared operations, and it complements CLAIM-576 and
  CLAIM-567.
- **RL as amortized search.** CLAIM-695 (the owner's idea, A's wording;
  Proposed, empirical) rests on CLAIM-697. In its terms, RL can shift the
  resource–reliability curve left "without raising its plateau". Whether a
  run sharpened or expanded is "an empirical question per run". Yue et
  al. (THEORY-1880) fit sharpening; ProRL (THEORY-1908) is the
  counter-case, with its qualifiers.
- **Where recognition is cheap.** CLAIM-699 (the assistant's; Proposed,
  empirical) rests on CLAIM-697 and CLAIM-695 and states their join: what
  RL amortizes is search filtered by the reward's verifier, so where that
  verifier runs at test time "RL buys economy, not reach". It places its
  test on QUESTION-392 (note of 2026-11-15). Its admission is in its body
  (added at this review).
- **Retrieval relative to a query family.** CASE-271 (A's construction,
  rebuilt on filing; Proposed) illustrates CLAIM-182 and CLAIM-407 and
  bears on QUESTION-274. Readdressing, readout suppression and deletion
  all read zero at the original query, and further queries separate them.
  Two pathways that cancel at the output are indistinguishable from none
  "until one is silenced". One of A's values, 0.551, is not reproduced.
- **Telling loss from inaccessibility.** CASE-274 (A's proposed study;
  not run) separates readdressing, interference, downstream suppression,
  higher realization cost and loss. It takes its readdressing signature
  from CASE-271 and its budget axis from CLAIM-697, and tests CLAIM-698
  (SYNTHESIS-tmpwrkqs). CASE-275 (A's proposed study; not run) separates
  TERM-118's masking, finking and mimicking from removal for a suppressed
  transformation, "relative to the declared readers, contexts and
  budgets" of CLAIM-697.

## The components

- CLAIM-697, the owner's idea in A's formalization, Proposed.
- CLAIM-695, the owner's idea in A's wording, Proposed.
- CLAIM-699, the assistant's, filed at the owner's request, Proposed.
- CASE-271, A's construction, rebuilt from the text, Proposed.
- CASE-274 and CASE-275, A's proposed studies, Proposed.

## Links tested as claims

- **CLAIM-699's join of CLAIM-697 and CLAIM-695.** Tested at this review
  (ADR-075, step 5). It adds a sentence neither premise states: with the
  training verifier available at test time, the RL model's large-budget
  accuracy does not exceed its base's best-of-N under that verifier at
  matched compute. A run that expanded the base's reach, which CLAIM-695
  allows "per run", satisfies both premises and falsifies that sentence.
  It passes as a separating case and a discriminating prediction. The
  case is realistic (ProRL claims expansion), so it may also defeat the
  claim; ProRL did not compare against verifier-filtered base sampling, so
  it does not yet. Recorded in CLAIM-699's "Admission".

## Not stated on the record

- **The realizability line's account.** The three claims' first line is
  realizability, and its account, SYNTHESIS-042, integrates CLAIM-576 and
  CLAIM-567, which CLAIM-697 complements. It integrates none of the three.
  That is a coverage question for a review of that line.

## What it does not say

- That nonzero probability is a capability. CLAIM-697: "Nonzero
  generation probability is not sufficient evidence of meaningful task
  competence."
- That RL only sharpens. CLAIM-695 keeps ProRL as a counter-case.
- That trained transformers store facts as CASE-271's memory does. CASE-271
  "cannot show" it.
- That any of the studies has been run.
