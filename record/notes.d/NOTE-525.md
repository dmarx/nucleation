---
number: 525
status: Read
formerly:
- NOTE-tmpbvbxb
paper: 'LIT-667'
title: 'Does Data Scaling Lead to Visual Compositional Generalization?'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v1 (25 pages, text layer, ICML 2025 header). Sections
    1–6 read in full. Appendix B read through the notation, Definition B.1,
    Lemma B.2 and the three-step structure of Proposition B.7's proof (the
    combinations observed for k = 2), with the intermediate lemmas skimmed;
    B.1 (algorithmic recovery), C.1–C.5 and D skimmed, C.5 (ViT against
    ResNet-50) read. The linearity and orthogonality formulas did not
    survive text extraction and are described from the prose. Bar heights
    not stated in the text are not reported.
date: '2026-10-03'
summary: >-
  (n, k) framework: two concepts with n values, k seen combinations per
  value. From-scratch ResNet-50s: near-100% ID, large OOD drops; 4× ID data
  leaves 60–80% drops; more values or combinations help. Features go from
  spurious, to decodable but entangled, to linearly factored (R² > 0.8,
  cosine < 0.1–0.2). Proposition 4.1: with linearly factored embeddings
  spanning 2n − 1 dimensions, k = 2 suffices for a linear classifier to be
  correct on all (n − k)·n unseen pairs. DINO, DINOv2, CLIP: partly
  factored, above chance, not perfect.
---

<!-- inactive-ok-file: THEORY-002 — Proposed; named for the record's account of representational convergence, with no relation claimed -->
<!-- inactive-ok-file: THEORY-004 — Proposed; named for representations determined by their kernels, with no relation claimed -->
<!-- inactive-ok-file: THEORY-008 — Proposed; named for kernel similarity as averaged readout agreement, with no relation claimed -->

# NOTE-525: Does Data Scaling Lead to Visual Compositional Generalization?

## Contribution

A controlled separation of data volume from combinatorial coverage in
visual compositional generalization, with a link between coverage and a
specific representational geometry. Before it, failures of compositional
generalization in vision models were documented on benchmarks, and linear
compositional structure had been observed in pretrained vision-language
embeddings. After it, there is a clean experimental knob (k/n) under which
generalization to unseen attribute–object pairs rises with coverage and not
with volume, a measured three-stage progression of the features, and a
proof that exact additive structure makes two combinations per value enough.

## Key insight

Seeing more images of the same few combinations teaches a network to
recognize those combinations, not their parts. Only when the parts appear
in many different pairings does the cheapest solution become one that
represents each part separately and adds them. Once the representation is
additive, a new pairing is just a new sum, and a linear readout handles it
without ever having seen it.

## Assumptions

- **Concept space** (Definition 3.1): C = C1 × C2 with n values each; other
  factors (position, rotation, background) vary but are unlabelled.
- **Training set**: k combinations per value of the n × n grid, the same
  number of images per seen cell; test on the (n − k)·n unseen cells.
- **Favourable conditions by design** (Section 3): oracle model selection on
  the test set at each epoch, multiple classification heads on a shared
  backbone, clean train/test partitions. This deliberately overstates what a
  practitioner could select.
- **From-scratch model**: ResNet-50 with linear heads. A ViT sweep did not
  beat it on OOD generalization at equal ID accuracy (99.7%) (C.5).
- **Pretrained models**: ImageNet ResNet-50, DINO ResNet-50, DINOv2 ViT-L/14,
  CLIP ViT-L/14, frozen, with linear or one- or two-hidden-layer MLP probes.
- **Linear factorization** (Definition 3.2, after Trager et al. 2023): u_c =
  u_{c1} + u_{c2} for every combination c. Proposition 4.1 also needs the
  concept vectors' joint span to have dimension 2n − 1, which the authors
  note can fail as n grows.

## Key results

- **Basic setting (Figure 3a; n = 3, k = 2).** ID accuracy near 100%;
  large OOD drops, about 78% for MNIST digits; in every dataset at least one
  concept degrades only 3–17%.
- **Data volume (Figure 4; n = 3, k = 1).** Training sets of 7,500, 15,000
  and 30,000 (up to 120,000 for dSprites and FSprites) leave 60–80% OOD
  drops.
- **Diversity (Figures 3b–c).** Generalization improves with n at
  k = n − 1, and with k at fixed n.
- **Three phases (Figure 5).** (i) Below about 10% of combinations: spurious
  features, decoded accuracy under 80%, chance-level zero-shot. (ii)
  Moderate coverage: decodable features (100%) without linear structure.
  (iii) High coverage (75–100%): R² > 0.8, near-orthogonal concept
  subspaces, zero-shot above 90% on most datasets.
- **Proposition 4.1 / B.7.** For k = 2, the observed set {(i, i)} ∪
  {(i, i + 1)} ∪ {(n, 1)} identifies the factors; the linear system has
  full rank with 2n equations in 2n unknowns; classifiers by orthogonal
  projection then generalize to all unseen pairs.
- **Pretrained, factor recovery (Figure 6).** With factors estimated from
  k = 2, all models exceed 90% on PUG-Animal's world-name concept; CLIP is
  best on colour (CMNIST colour, 3DShapes object hue), DINOv2 on shape,
  scale and orientation; none is perfect.
- **Pretrained, probing (Figure 8).** All pretrained models beat the
  from-scratch ResNet-50, and all still improve as k grows.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | More in-distribution data does not close the compositional gap | moderate: up to 4× (16× for two datasets), n = 3, k = 1, one architecture | Figure 4 |
| C2 | Compositional generalization grows with combinatorial diversity | moderate to strong within the framework | Figures 3, 5 |
| C3 | Linearly factored features emerge only at high coverage, after decodability | moderate: measured on from-scratch models across datasets; thresholds approximate | Figure 5 |
| C4 | Exact linear factorization with a 2n − 1 dimensional span makes k = 2 sufficient | strong (proof), under its idealized assumptions | Proposition 4.1, B.7 |
| C5 | Large pretrained vision models are partly linearly factored | moderate: factor-recovery accuracy varies widely by concept | Figure 6 |
| C6 | Pretraining is not a substitute for data diversity | moderate | Figure 8 |

## Concepts

- **(n, k) framework**: n values per concept, k seen combinations per value.
- **decodability**: accuracy of linear probes trained on balanced data
  covering all combinations, following Kirichenko et al. and Uselis and Oh.
- **linearity**: R² of reconstructing joint representations from
  per-concept mean representations.
- **orthogonality**: mean cosine similarity between the two concepts'
  representation vectors.
- **linearly factored embeddings**: a pair's vector is the sum of one
  vector per concept value (Trager et al.).

## Connections

- **Trager et al. (2023)**: the definition of linear factorization and the
  recovery by averaging.
- **Stein et al. (2024), Park et al. (2024, categorical and hierarchical
  concepts)**: observed linear and orthogonal structure in large models.
- **Uselis and Oh ([LIT-678](../literature.d/LIT-678.md))**: the decodability protocol.
- **Kirichenko et al. (2023)**: last-layer retraining, the probe baseline.
- **Sonthalia, Uselis and Oh (2025)**: concept factors may occupy
  low-dimensional subspaces, the case where Proposition 4.1's span
  assumption fails.

## Bearing on the record

- **[THEORY-004](../theory.d/THEORY-004.md) and [THEORY-008](../theory.d/THEORY-008.md).** Linear factorization and orthogonality are
  invariant under the orthogonal transformations that [THEORY-004](../theory.d/THEORY-004.md) says a
  kernel leaves free, and a readout's success is what [THEORY-008](../theory.d/THEORY-008.md) says
  kernel similarity measures average. So the paper's structural property is
  visible at the level of kernels, and two representations with the same
  kernel are equally compositional in its sense. This is my connection, not
  the paper's.
- **[LIT-302](../literature.d/LIT-302.md) and [THEORY-002](../theory.d/THEORY-002.md).** The paper's finding that pretrained models
  differ by concept type (CLIP on colour, DINOv2 on shape) is a measured
  divergence among large models, in a property the Platonic picture would
  predict they share.
- **THEORY candidate (not filed):** "When a representation is exactly
  linearly factored over two concepts with n values each, and the concept
  vectors span 2n − 1 dimensions, observing two combinations per value in a
  connected cycle determines every unseen combination, so compositional
  generalization reduces to a coverage condition on the training grid."
  Source this paper; promote when the proof is checked line by line, or a
  second derivation (Trager et al.) is read.
- **Anthology.** The practice instruction (diversify combinations rather
  than add volume) is anthology material.

## Limitations

- **Oracle model selection on the test set**, chosen to give models
  "maximally favorable conditions". The results bound what is possible, not
  what a practitioner would select.
- **Two concepts, single objects, synthetic data** (except PUG's rendered
  animals). The authors say more concepts would be harder still.
- **One from-scratch architecture.** ResNet-50, with a ViT sweep that did
  no better.
- **Phase thresholds are approximate and stated inconsistently.** The text
  gives the moderate phase as 25–75% and the takeaway as 10–75%;
  orthogonality as cosine < 0.1 in the text and < 0.2 in the takeaway; and
  the basic-setting drops as 27–95% in the list of questions against 60–80%
  in the takeaway, which refers to the volume experiment.
- **Proposition 4.1 assumes exact factorization**, which no trained model
  in the paper reaches.

## Open questions

- What training signal produces linear factorization without full
  coverage?
- Does the k = 2 result survive approximate factorization, with an error
  bound in terms of the reconstruction R²?
- Does the coverage threshold scale with n, and how does it interact with
  more than two concepts?

## Corrections

- none (there was no seed)
