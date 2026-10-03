---
status: Proposed
promote_when: >-
  For the empirical half: the volume-against-diversity comparison
  repeated with model selection on a validation split disjoint from the
  unseen combinations, so that a model never chosen by its score on the
  test pairs still fails to generalize under more data of the same
  combinations and succeeds as coverage rises. A second architecture
  trained from scratch, or more than two concepts, would widen it. For
  the theoretical half: a line-by-line check of Proposition B.7's proof,
  or a second derivation such as Trager et al.'s. The account is refuted
  if, at fixed combinatorial coverage, enough added data of the seen
  combinations closes the gap on unseen ones, or if networks reach high
  accuracy on unseen pairs at low coverage without linearly factored
  features. Further runs with oracle selection on the test pairs cannot
  settle it, since they measure the best case by construction.
title: 'Compositional generalization comes from diversity of combinations, not data volume: in vision models trained from scratch on two-concept grids, unseen pairs are reached as the share of combinations seen grows and not as data of the same combinations grows, and with linearly factored features two seen combinations per value, suitably arranged, determine every unseen one'
version: 1
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-03'
source:
- LIT-tmpid11v
summary: >-
  Uselis, Dittadi & Oh (2025), [LIT-tmpid11v](../literature.d/LIT-tmpid11v.md). In an n × n grid of two
  concepts with k combinations seen per value, ResNet-50s trained from
  scratch fit seen pairs and fail on unseen ones; four times the data of
  the same combinations leaves 60–80% drops, while more values and more
  combinations help. Features pass from spurious, to decodable but
  entangled, to linearly factored as coverage grows. Proposition 4.1: under
  exact linear factorization with a (2n − 1)-dimensional span, k = 2
  suffices for a linear classifier to be right on all unseen pairs. Model
  selection was on the test set, by design, so the results bound what is
  possible. Synthetic data, two concepts, one from-scratch architecture.
---
<!-- inactive-ok-file: THEORY-004 — Proposed; named in Connections for representations fixed by their kernels, nothing here rests on it -->

# THEORY-tmpxlzlq: Compositional generalization comes from diversity of combinations, not data volume: in vision models trained from scratch on two-concept grids, unseen pairs are reached as the share of combinations seen grows and not as data of the same combinations grows, and with linearly factored features two seen combinations per value, suitably arranged, determine every unseen one

## Source

- Uselis, Dittadi & Oh (2025), [LIT-tmpid11v](../literature.d/LIT-tmpid11v.md), read in [NOTE-tmpbvbxb](../notes.d/NOTE-tmpbvbxb.md):
  Sections 3–5 (Figures 3–8, Proposition 4.1), Appendix B (Proposition B.7)
  and C.5.

## The claim, in two halves

**Empirically: coverage, not volume.** Uselis, Dittadi and Oh
([LIT-tmpid11v](../literature.d/LIT-tmpid11v.md)) set two labelled concepts, each with n values, on an
n × n grid. Training shows k combinations per value and the test uses the
(n − k)·n others. On dSprites, 3DShapes, PUG, colored MNIST and their own
FSprites, ResNet-50s trained from scratch reach near 100% on seen pairs
and lose a great deal on unseen ones (Figure 3a). With n = 3 and k = 1,
growing the training set from 7,500 to 30,000 images, and to 120,000 on
two datasets, leaves "accuracy drops of 60-80% on unseen combinations"
(Figure 4). What helps is coverage: raising n with k = n − 1, or raising k
at fixed n (Figures 3b–c). As coverage grows the features pass through
three stages (Figure 5). Below about 10% of combinations they are
spurious and not even decodable. At moderate coverage a linear probe on
balanced data decodes them perfectly, but they are not linearly
structured. Only at high coverage, 75–100% of combinations, do they become
linearly factored, a pair's embedding the sum of one vector per concept
value (R² > 0.8), with near-orthogonal concept subspaces, and accuracy on
unseen pairs above 90% on most datasets.

**Theoretically: why factorization makes two enough.** Proposition 4.1
(proved as B.7) says that if the embeddings are exactly linearly factored
and the 2n concept vectors jointly span 2n − 1 dimensions, then "k = 2
combinations per concept value suffice to learn a linear classifier that
perfectly generalizes to all (n − k)·n unseen combinations". The proof
uses a particular arrangement of the seen pairs, the diagonal (i, i), the
shifted diagonal (i, i + 1) and the closing pair (n, 1): a single cycle
through every value of both concepts. From it the factors are
identifiable, the linear system of 2n equations in 2n unknowns has full
rank, and classifiers by orthogonal projection are correct on every unseen
pair. The proposition states k = 2 without naming the arrangement. A
choice of two pairs per value that split the grid into disconnected
blocks would leave the offset between blocks unfixed, so "suitably
arranged" in the title is this account's reading of what the proof needs,
not a condition the paper states.

The two halves meet in the representation. Data of the same few
combinations can be fitted by recognizing those combinations whole;
coverage makes the additive solution the one training finds; and an
additive representation turns a new pairing into a new sum that a linear
readout already handles.

## Model selection was on the test set, by design

The authors' principle was "to grant models maximally favorable
conditions for demonstrating compositional abilities", and they "perform
oracle model selection by directly evaluating models on the test set to
select the best performing checkpoint", on the average accuracy across
concepts at each epoch (Section 3). The test set is the unseen
combinations. So every from-scratch number is the best checkpoint as
scored on the pairs the claim is about. That makes the failures strong
evidence, since even the best checkpoint by the test score fails under
more volume, and makes the successes an upper bound, not what a
practitioner without access to the unseen pairs would select.

## What this does not say

- **It does not say pretrained models are compositional.** Frozen DINO,
  DINOv2 and CLIP features are partly factored: factors recovered from
  k = 2 give above 90% on some concepts (CLIP on colour, DINOv2 on shape,
  scale and orientation), no model is perfect, and probes on all of them
  still improve as k grows (Figures 6, 8).
- **It does not say volume never helps.** The volume test is n = 3, k = 1,
  up to four times the data (sixteen on two datasets), one architecture.
- **It does not reach real scenes or more concepts.** Two concepts, single
  objects, synthetic or rendered data. The authors expect more concepts to
  be harder.
- **The thresholds are approximate.** The paper states the moderate stage
  as 25–75% in one place and 10–75% in another, and orthogonality as
  cosine below 0.1 in the text and below 0.2 in a takeaway
  ([NOTE-tmpbvbxb](../notes.d/NOTE-tmpbvbxb.md)).
- **The proposition assumes exact factorization,** which no trained model
  in the paper reaches, and a joint span of 2n − 1, which the authors note
  can fail as n grows. How it degrades under approximate factorization is
  open.
- **Architecture is not ruled out.** A ViT sweep did no better than the
  ResNet-50 at equal in-distribution accuracy (C.5), which is one
  comparison.

## Connections

- **The probe protocol** is Uselis and Oh's ([LIT-tmpt61ew](../literature.d/LIT-tmpt61ew.md)), cited for the
  decodability measure; no relation follows from sharing it.
- **Kernels.** Linear factorization and orthogonality of concept subspaces
  are invariant under the orthogonal freedom that the record says a
  representation keeps once its kernel is fixed ([THEORY-004](THEORY-004.md)). So the
  property is visible at the level of kernels. That is the reading in the
  LIT's standing, not the paper's.
- **Anthology.** Its closest holding makes the same move in language
  models: for a transformer to reason over facts it holds, the ratio of
  derived to atomic facts, not the size of the training set, decides when
  it generalizes ([ANTH-SOTA-402](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-402.md), from Wang et al., [ANTH-LIT-667](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-667.md)). There as
  here, what matters is which combinations the data contain, not how much
  data there is.
