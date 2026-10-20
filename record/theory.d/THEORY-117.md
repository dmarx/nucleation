---
number: 117
status: Active
formerly:
- THEORY-tmpxlzlq
title: "In Uselis, Dittadi and Oh's two-concept grids, ResNet-50s trained from scratch, with checkpoints chosen on the unseen pairs, reach unseen combinations as the share of combinations seen grows and not as up to four times more data of the same combinations is added; and when embeddings are exactly linearly factored, seen pairs that connect every value of both concepts, as two per value arranged in one cycle do, determine the embedding of every unseen pair"
version: 3
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-117 (batch 047, ADR-047 v3 for the measured half, v2 for the
    theorem). One study read in full, whose text states the volume and
    coverage results; the title now names oracle checkpoint selection and
    drops the general causal opener. The determination clause is re-derived
    (dated note below), which makes "suitably arranged" exact: the seen
    pairs must connect every value. The promote_when moves to
    QUESTION-207.
- version: 3
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 066, ADR-047 v4) filed
    THEORY-794 as a Proposed THEORY that extends this one, to carry
    what the narrowing dropped: the general claim that diversity of
    combinations, not data volume, drives compositional generalization
    in vision models. This entry's status and title are unchanged.
tags:
- representation-learning
- compositionality
- learning-theory
- anthology-candidate
date: '2026-10-03'
source:
- LIT-667
summary: >-
  Uselis, Dittadi & Oh (2025), [LIT-667](../literature.d/LIT-667.md). In an n × n grid of two concepts
  with k combinations seen per value, ResNet-50s trained from scratch fit
  seen pairs and fail on unseen ones; four times the data of the same
  combinations leaves 60–80% drops, while more values and more
  combinations help. Features pass from spurious, to decodable but
  entangled, to linearly factored as coverage grows. Model selection was
  on the test set, by design, so the results bound what is possible. The
  record re-derived that exactly factored embeddings of every unseen pair
  are fixed by seen pairs connecting every value, as the paper's k = 2
  cycle does. Honest selection, other architectures and more concepts are
  [QUESTION-207](../questions.d/QUESTION-207.md).
answers:
- QUESTION-025
extended_by:
- THEORY-794
---
<!-- inactive-ok-file: THEORY-794 — Proposed; the wider claim this account was narrowed from, which extends it and is cited as open -->

# THEORY-117: In Uselis, Dittadi and Oh's two-concept grids, ResNet-50s trained from scratch, with checkpoints chosen on the unseen pairs, reach unseen combinations as the share of combinations seen grows and not as up to four times more data of the same combinations is added; and when embeddings are exactly linearly factored, seen pairs that connect every value of both concepts, as two per value arranged in one cycle do, determine the embedding of every unseen pair

## Source

- Uselis, Dittadi & Oh (2025), [LIT-667](../literature.d/LIT-667.md), read in [NOTE-525](../notes.d/NOTE-525.md):
  Sections 3–5 (Figures 3–8, Proposition 4.1), Appendix B (Proposition B.7)
  and C.5.

## The claim, in two halves

**Empirically: coverage, not volume.** Uselis, Dittadi and Oh
([LIT-667](../literature.d/LIT-667.md)) set two labelled concepts, each with n values, on an
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
  ([NOTE-525](../notes.d/NOTE-525.md)).
- **The proposition assumes exact factorization,** which no trained model
  in the paper reaches, and a joint span of 2n − 1, which the authors note
  can fail as n grows. How it degrades under approximate factorization is
  open.
- **Architecture is not ruled out.** A ViT sweep did no better than the
  ResNet-50 at equal in-distribution accuracy (C.5), which is one
  comparison.

## Connections

- **The probe protocol** is Uselis and Oh's ([LIT-678](../literature.d/LIT-678.md)), cited for the
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

## Derivation (2026-10-20, promotion audit batch 047)

Exact linear factorization: the embedding of pair (i, j) is z(i, j) = a_i + b_j. Let G be the bipartite graph whose nodes are the values a_1, …, a_n of the first concept and b_1, …, b_n of the second, with an edge for each seen pair.

**Claim.** If G is connected, every z(i, j), seen or not, is a fixed linear combination of the seen embeddings.

**Proof.** G is bipartite, so a path from a_i to b_j alternates sides: a_i = u_0, u_1, …, u_{2m+1} = b_j, with edges e_1, …, e_{2m+1}. Summing the edges' embeddings with alternating signs, z(e_1) − z(e_2) + z(e_3) − …, each interior node enters once with a plus and once with a minus, leaving a_i + b_j = z(i, j). ∎

The arrangement in the paper's proof of Proposition B.7, the pairs (i, i), (i, i + 1) and (n, 1), is a single cycle b_1, a_1, b_2, a_2, …, a_n, b_1 through every node, so two pairs per value so arranged connect G.

Connectivity is needed. If G has two components, adding a constant vector c to every a and subtracting it from every b in one component leaves every seen sum unchanged and changes every sum across the components. With k = 1 the seen pairs form a matching of n edges on 2n nodes, never connected for n ≥ 2.

The paper's span condition (2n − 1 dimensions) is what its classifier statement needs, a linear readout correct on every unseen pair. That statement is not re-derived here and not claimed; this account claims only that the unseen embeddings are determined.

## Note of 2026-10-20: the wider claim filed separately

When this THEORY was narrowed to what its source showed, the wider claim
it had stated was left with nowhere to go but this body and a QUESTION.
Under [ADR-047](../decisions.d/ADR-047.md) v4 it is now its own Proposed THEORY, [THEORY-794](THEORY-794.md), which extends
this one: the general claim that diversity of combinations, not data volume, drives compositional generalization in vision models. This entry is that THEORY's evidence and is not
changed by it.
