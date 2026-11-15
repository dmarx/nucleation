---
status: Proposed
title: 'Where the reward used in RL post-training is also available as a verifier at test time, the RL model''s single-sample gain is a cheaper route to what base sampling filtered by that verifier reaches at matched compute, and should not exceed it at large budgets; RL''s distinctive value lies where recognition at test time is unavailable or costly, so the substitutability of training and search is fixed by the cost of recognition'
version: 1
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
- CLAIM-tmps7g72
- CLAIM-tmp36o5i
bears_on:
- QUESTION-392
summary: >-
  The assistant's hypothesis, offered at the end of the filing of
  2026-11-15 and filed at the owner's request. It joins two of the owner's
  claims. [CLAIM-tmps7g72](CLAIM-tmps7g72.md) says generation, recognition and selection are
  separate capacities. [CLAIM-tmp36o5i](CLAIM-tmp36o5i.md) says RL can amortize search. Put
  together, what RL amortizes is search filtered by the reward's verifier,
  so where that verifier can be run at test time, RL buys economy, not
  reach. Yue et al.'s large-k crossings fit the claim; ProRL's new
  strategies are the case that would defeat it if they hold against
  verifier-filtered base sampling at matched compute, which ProRL did not
  test. Untested. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmps7g72 CLAIM-tmp36o5i THEORY-331 — Proposed or new; the claims this rests on and the readings it is set against -->

# CLAIM-tmpwxs2x: Where the reward is available as a verifier at test time, RL buys economy, not reach

## The argument

1. RLVR trains on a reward that is a verifier: it recognizes success.
2. At test time, the base model plus that verifier can draw N samples and
   return a verified one. Its delivered accuracy is its coverage, which
   grows as 1 − (1 − p)^N for each problem ([CLAIM-tmps7g72](CLAIM-tmps7g72.md)).
3. The RL policy reaches comparable accuracy in fewer samples, because
   training moved probability toward what the verifier accepts
   ([CLAIM-tmp36o5i](CLAIM-tmp36o5i.md)). Under the ideal tilt it can only reweight what the
   base already reaches.
4. So with the verifier available at test time, RL is a way to spend
   training compute instead of inference compute on the same reach. That
   is the training–search trade of [THEORY-342](../theory.d/THEORY-342.md), here with the condition
   that a recognizer is cheap.
5. Without the verifier at test time (open-ended tasks, unit tests
   unavailable, a reward model too costly to run per sample), base
   sampling cannot be filtered. Then RL's gain is real reach for the
   deployed system, because the system lacks the selector.

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
