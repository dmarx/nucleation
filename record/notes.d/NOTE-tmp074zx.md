---
status: Read
paper: LIT-tmp995ll
title: 'McDermott, Yap, Szolovits and Zitnik — Structure-inducing pre-training'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2103.10334v3
    (2022-08-04): main text, Methods, proofs, semi-synthetic and real-domain
    experiments, ablations; the review appendix skimmed. The journal version
    (Nature Machine Intelligence 5, 612-621, 2023) is open access under CC
    BY and was compared from its HTML and part of its Supplementary
    Information; it adds a stated limitation quoted below. Quotations
    rechecked by the filer by script against the downloaded texts.
date: '2026-11-19'
summary: >-
  A method paper, with a review and a theorem: pre-training helps a later
  per-sample task to the degree that the relational structure it induces
  among sample embeddings agrees with that task. A structure-inducing loss
  term, aligning embeddings to a chosen pre-training graph, bounds
  nearest-neighbour fine-tuning accuracy by the task's local consistency
  over the graph; it matched or beat language-model and supervised pre-
  training in real domains, and a graph misaligned with the task did worse
  than language-model pre-training. It measures final performance, not the
  cost of later learning, except in one convergence curve.
---
<!-- inactive-ok-file: CLAIM-756 CLAIM-758 — Proposed; entries this reading bears on -->

# NOTE-tmp074zx: McDermott, Yap, Szolovits and Zitnik — Structure-inducing pre-training

## Contribution

A taxonomy of pre-training objectives (explicit or implicit, deep or
shallow constraints on embeddings); structure-inducing pre-training, a
language-model loss plus a term pulling embeddings close exactly when
samples are linked in a chosen graph; a bound tying fine-tuning to the
graph's agreement with the task; modest real-domain gains with an
ablation separating the new term from extra training.

## Key results

1. **The question (p. 1).** "there remains considerable uncertainty on
   exactly why pre-training helps improve performance for fine-tuning
   tasks"; fine-tuning tasks "are not known at pretraining time" (p. 2).
2. **Theorem 1 (p. 7).** Nearest-neighbour fine-tuning accuracy
   "converges as dataset size increases to at least the local
   consistency" of the task over the pre-training graph. Corollary 1: a
   graph defined by class labels caps it, "once saturation is reached, it
   will not improve beyond this fixed upper bound relating to task
   correlation".
3. **Real domains (p. 8).** "SIPT improves over existing methods, and in
   no case does it do worse than either baseline", in 10 of 15
   comparisons, with significance "assessed via a t-test at significance
   level p < 0.1".
4. **Later-learning speed, once (p. 9).** "SIPT methods converge faster to
   better performance than both baselines", in one domain, with no
   threshold or budget; there the pre-training graph is built from 4,000
   GO annotations and fine-tuning targets "a smaller set of only 40 GO
   terms", on reused pre-training samples.
5. **Attribution (p. 9).** "performance gains shrink when considering
   these ablation studies", yet the authors state the gains are "uniquely
   attributable to the new, structure-inducing components".
6. **Mismatch hurts (semi-synthetic, p. 30; journal Supplementary p. 12).**
   "SIPT only under-performs LM PT on the" structural graph, where the
   task's local consistency is low; "inducing an inductive bias that is
   inversely related to a fine-tuning task can result in a degradation in
   performance relative to traditional pre-training", which the authors
   judge "not significant in practice".

## Assumptions

For the theorem: i.i.d. data, fine-tuning labels on the pre-training
samples, infinite data, nearest-neighbour classifiers rather than
fine-tuned networks. For the experiments: warm starts, one run per
configuration, small hand-tuned semi-synthetic models.

## Concepts

Explicit and implicit, deep and shallow constraints; per-sample and
per-token latent spaces; pre-training graph; structure-inducing loss;
local consistency (close to homophily).

## Bearing on the record

- **CLAIM-756 and the owner's point at U37.** It shows pre-training
  improving final downstream performance, and once a faster convergence,
  not a measured fall in the cost of later learning; at most a weak
  instance of the claim's premise, and nothing on valuation.
- **CLAIM-350 and CLAIM-152.** Corollary 1 is CLAIM-350 in pre-training
  form: a label-defined graph collapses each class, so a later task is
  served only as far as its labels are constant within the pre-training
  classes.
- **CLAIM-758.** A demonstrated form, as a bound, of the overcompression
  mechanism the claim lists: a constraint sufficient for the pre-training
  labels and insufficient for a task whose labels vary within them. It
  does not grow with training here.

## Limitations

One run per configuration; weak significance; small real gains that the
ablation shrinks; a likely flattering setup in the one domain with a
convergence curve; theory for nearest-neighbour probes in the
infinite-data limit; text and figure disagree on the noise threshold.
