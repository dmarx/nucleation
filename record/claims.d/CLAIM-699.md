---
number: 699
status: Proposed
formerly:
- CLAIM-tmpwxs2x
title: 'Where the reward used in RL post-training is also available as a verifier at test time, the RL model''s single-sample gain is a cheaper route to what base sampling filtered by that verifier reaches at matched compute, and should not exceed it at large budgets; RL''s distinctive value lies where recognition at test time is unavailable or costly, so the substitutability of training and search is fixed by the cost of recognition'
version: 2
history:
- version: 2
  date: '2026-11-18'
  note: >-
    "Admission" added at the synthesis review of 2026-11-18
    (learned-structure): the claim rests on two claims, so it was tested
    under ADR-075 step 5. It passes by a separating case and a
    discriminating prediction. The claim is unchanged.
role: thesis
warrant: empirical
defeated_if: >-
  An RL-trained model whose large-budget accuracy, with no verifier at
  test time, exceeds what its own base reaches by best-of-N under the same
  verifier the training used, at matched total compute, on the training
  task family; or evidence that recognition cost does not moderate the
  substitution of training for search; or a reading under which this
  restates THEORY-331 or THEORY-342, the record's training–inference
  substitution readings, without the recognition condition.
tags:
- learning-theory
- operations-research
- anthology-candidate
date: '2026-11-15'
line:
- realizability
- learned-structure
rests_on:
- CLAIM-697
- CLAIM-695
bears_on:
- QUESTION-392
summary: >-
  The assistant's hypothesis, offered at the end of the filing of
  2026-11-15 and filed at the owner's request. It joins two of the owner's
  claims. [CLAIM-697](CLAIM-697.md) says generation, recognition and selection are
  separate capacities. [CLAIM-695](CLAIM-695.md) says RL can amortize search. Put
  together, what RL amortizes is search filtered by the reward's verifier,
  so where that verifier can be run at test time, RL buys economy, not
  reach. Yue et al.'s large-k crossings fit the claim; ProRL's new
  strategies are the case that would defeat it if they hold against
  verifier-filtered base sampling at matched compute, which ProRL did not
  test. Untested. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1908 CLAIM-697 CLAIM-695 THEORY-331 — Proposed or new; the claims this rests on and the readings it is set against -->

# CLAIM-699: Where the reward used in RL post-training is also available as a verifier at test time, the RL model's single-sample gain is a cheaper route to what base sampling filtered by that verifier reaches at matched compute, and should not exceed it at large budgets; RL's distinctive value lies where recognition at test time is unavailable or costly, so the substitutability of training and search is fixed by the cost of recognition

## The argument

1. RLVR trains on a reward that is a verifier: it recognizes success.
2. At test time, the base model plus that verifier can draw N samples and
   return a verified one. Its delivered accuracy is its coverage, which
   grows as 1 − (1 − p)^N for each problem ([CLAIM-697](CLAIM-697.md)).
3. The RL policy reaches comparable accuracy in fewer samples, because
   training moved probability toward what the verifier accepts
   ([CLAIM-695](CLAIM-695.md)). Under the ideal tilt it can only reweight what the
   base already reaches.
4. So with the verifier available at test time, RL is a way to spend
   training compute instead of inference compute on the same reach. That
   is the training–search trade of [THEORY-342](../theory.d/THEORY-342.md), here with the condition
   that a recognizer is cheap.
5. Without the verifier at test time (open-ended tasks, unit tests
   unavailable, a reward model too costly to run per sample), base
   sampling cannot be filtered. Then RL's gain is real reach for the
   deployed system, because the system lacks the selector.

## Admission

Added at the synthesis review of 2026-11-18 ([ADR-075](../decisions.d/ADR-075.md), step 5), because
the claim rests on two claims.

- **What it adds.** With the training verifier available at test time,
  the RL model's large-budget accuracy does not exceed its base's
  best-of-N under that verifier at matched total compute. Neither premise
  says so. [CLAIM-697](CLAIM-697.md) says nothing about RL, and [CLAIM-695](CLAIM-695.md) leaves
  sharpening against expansion to each run.
- **A separating case.** A run in which RL expands what the base reaches,
  which [CLAIM-695](CLAIM-695.md) allows "per run", with [CLAIM-697](CLAIM-697.md)'s envelope intact.
  Both premises hold and the sentence fails. The case is realistic:
  ProRL ([THEORY-1908](../theory.d/THEORY-1908.md)) reports new strategies under prolonged RL. So it may
  also defeat this claim, under its own `defeated_if`. It does not yet,
  because ProRL compared against base sampling at k up to about 128, not
  against base sampling filtered by the training verifier at matched
  compute.
- **A discriminating prediction.** The premises leave open how the RL
  curve and the verifier-filtered base curve compare at large budgets.
  This claim predicts the second meets or exceeds the first on the
  training task family, and that the substitution weakens as recognition
  grows costly.

## What would test it

Compare an RL model at one or few samples with no verifier against its
base under best-of-N with the training verifier, at matched total compute
(training amortized across the test set plus inference), across k. The
claim predicts the base-plus-verifier curve meets or exceeds the RL curve
at large budgets on the training task family. A dated note on [QUESTION-392](../questions.d/QUESTION-392.md)
places the test.

## What it does not say

- **That RL is pointless where a verifier exists.** It is cheaper at
  deployment. That is the claim's "economy".
- **That every RL gain is reweighting.** ProRL-style expansion would defeat
  the claim's large-budget clause if it held against verifier-filtered
  base sampling.
