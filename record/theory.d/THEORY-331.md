---
number: 331
status: Proposed
formerly:
- THEORY-tmp2qsfa
promote_when: >-
  A comparison in which the quality reached is measured, not taken from a
  fitted law, for models trained to equal quality at different splits of
  compute between training and per-use inference, across several expected
  inference volumes and more than one model family or task, with the total
  cost at each volume counted, including the difficulty estimate and any
  verifier or revision-model training. It promotes the direction if the
  split with the least total cost moves toward up-front compute as volume
  grows, and the condition on difficulty if test-time compute keeps losing
  on questions the small model almost never solves. Re-solving the same
  optimisation with other constants, or another single benchmark with one
  model family, cannot settle it: those restate the accounting or repeat
  one case.
title: "Counting the inference a model will serve as well as its training, the least-compute way to reach a fixed quality shifts toward up-front compute as expected inference volume grows: a smaller model trained on more data in Sardana et al., a larger pretrained model over test-time search in Snell et al.; test-time compute won only at low volume and on questions the small model already sometimes solved"
version: 1
tags:
- learning-theory
- anthology-candidate
date: '2026-10-15'
source:
- LIT-1070
- LIT-1063
answers:
- QUESTION-095
summary: >-
  Sardana et al. (2024; arXiv 2023), [LIT-1070](../literature.d/LIT-1070.md), read in [NOTE-881](../notes.d/NOTE-881.md), and Snell et
  al. (2024), [LIT-1063](../literature.d/LIT-1063.md), read in [NOTE-869](../notes.d/NOTE-869.md). Sardana et al. minimise training
  plus lifetime inference FLOPs at a fixed loss under a Chinchilla-fitted
  law: the optimum moves to smaller models trained longer as known demand
  grows (28% fewer FLOPs at 30B quality and 10^13 inference tokens), and 47
  runs show loss still falling at extreme ratios but more slowly than the
  law predicts. Snell et al. match FLOPs between a small model with
  test-time search or revision and a ~14× larger model on MATH: test-time
  compute wins at a low ratio of inference to pretraining tokens on easier
  questions and loses at a high ratio, and on the hardest at every ratio.
  Both take expected use as a known aggregate; neither has staleness or
  uncertainty about demand, and Snell's evidence is one model family on 500
  questions.
---
<!-- inactive-ok-file: CLAIM-303 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# THEORY-331: Counting the inference a model will serve as well as its training, the least-compute way to reach a fixed quality shifts toward up-front compute as expected inference volume grows: a smaller model trained on more data in Sardana et al., a larger pretrained model over test-time search in Snell et al.; test-time compute won only at low volume and on questions the small model already sometimes solved

## Source

Sardana, Portes, Doubov & Frankle (2024, ICML; arXiv 2401.00448), [LIT-1070](../literature.d/LIT-1070.md),
read in [NOTE-881](../notes.d/NOTE-881.md). Snell, Lee, Xu & Kumar (2024, arXiv 2408.03314; ICLR
2025), [LIT-1063](../literature.d/LIT-1063.md), read in [NOTE-869](../notes.d/NOTE-869.md), both versions.

## What was actually shown

**Sardana et al.: the optimum moves with demand.** Holding pre-training loss
fixed under the Chinchilla law, and counting 6N FLOPs per training token
and 2N per inference token over a known lifetime demand D_inf, the
minimising (N, D_tr) has no closed form and is found numerically. "When
inference usage is significantly less than the number of pre-training
tokens, Chinchilla models are essentially compute-optimal." As demand
grows the optimum is smaller and trained longer: at 30B-Chinchilla quality
and 10^13 inference tokens, "reduce their total FLOPs by 28% by training a
13.6B model on 2.84× the data". The extra training "pays off after enough
inference requests". Priced in dollars, with generated tokens at 1%
hardware utilisation, the savings run from 17% to 58% in the paper's
examples, and a design 1.3% off in FLOPs is 36% off in dollars.

**Sardana et al.: the law it rests on, checked.** 47 runs (150M to 6B
parameters, 10 to 10,000 tokens per parameter) find "loss does not plateau
as we scale to 10,000 tokens per parameter for our 150M model", but
refitting on their own runs shows models "continue to learn at extreme
training durations, they do so more slowly than scaling laws predict". The
optimisation is not rerun with the refitted law, so how far the headline
shifts shrink is not stated.

**Snell et al.: the FLOPs-matched comparison.** A ~14× larger model costs
more to pretrain and more per inference token. Matching total FLOPs, the
small model may spend a multiple of its greedy inference that falls as R,
the ratio of inference tokens to pretraining tokens, grows (v1 multiplier
M + 3(M − 1)/R, the record's rearrangement). Relative accuracy against the
larger model, for revisions on easy questions, is +21.6% at R << 1 and
+5.4% at R >> 1; on hard questions +11.8% and −37.2%; for PRM search on
hard questions 0.0% and −52.9%. "Test-time and pretraining compute are not
1-to-1 “exchangeable”." The abstract limits its claim to "problems where a
smaller base model attains somewhat non-trivial success rates".

**What could have come out the other way.** Long training could have
plateaued (it slowed); test-time compute could have beaten the larger
model at every R and difficulty (it lost at high R and on the hardest).

## What this does not say

- **That this is an instruction for training or serving models.** These are
  findings under stated accountings. How to allocate compute in practice is
  a practice, and belongs in the Anthology of the SOTA.
- **That any crossover point is known.** Sardana's numbers come from a
  fitted law its own runs show overstates the gain from long training.
  Snell's R values halved between versions when verifier calls were
  charged, and its evidence is PaLM 2-S* on 500 MATH test questions.
- **That all the compute is counted.** Snell's difficulty estimate (2048
  samples per question) and the finetuning of its verifier and revision
  model are not charged. Sardana counts no post-training, storage or
  serving overhead.
- **That expected use is a count of recurring queries.** Both take an
  aggregate: D_inf in total tokens, R as a token ratio. Neither says which
  queries recur. Reuse here is of a capacity across a query distribution,
  not of a stored answer.
- **That demand is uncertain, shifts or ends.** Sardana assumes demand is
  known before training and independent of model size at fixed quality,
  and concedes in a footnote that smaller models may draw more demand.
  Neither paper has discounting, obsolescence, replacement or distribution
  shift.
- **That the two papers trade the same things.** Sardana trades model size
  against training data at fixed quality; Snell trades model size against
  test-time search or revision. The direction is shared, not the dial.

## Connections

- [QUESTION-095](../questions.d/QUESTION-095.md)'s note of 2026-10-15 reads these as pricing two of its
  terms, expected reuse and per-use (retrieval) cost, with no staleness,
  uncertainty about demand or erosion. The larger model's higher cost per
  token is a retrieval cost that the amortized-inference readings lack.
- [CLAIM-303](../claims.d/CLAIM-303.md)'s break-even is Sardana's trade with upkeep set to zero
  ([NOTE-881](../notes.d/NOTE-881.md)), and the paper turns the file-or-not choice into a continuous
  dial tied by a production function.
- Snell's condition on difficulty runs opposite to the cockpit's ([LIT-1066](../literature.d/LIT-1066.md)):
  per-query compute helped where what was precomputed was nearly enough,
  and not where the query lay outside it.
- [THEORY-342](THEORY-342.md) is the complement: Jones measures the exchange rate between
  training and search at fixed strength, with no volume term; these two
  add volume, with no iso-performance curve beyond Snell's one comparison.
