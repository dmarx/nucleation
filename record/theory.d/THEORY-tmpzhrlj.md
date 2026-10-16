---
status: Active
title: "Thresholding linear attribute probes on a language model's embeddings yields a complete concept lattice for any incidence whatever, so the lattice is guaranteed by construction; what the Lattice Representation Hypothesis measured is per-attribute agreement with GPT-4o annotations at F1 70–83, and no lattice law"
version: 1
tags:
- representation-learning
- logic
- mathematics
date: '2026-10-16'
source:
- LIT-267
answers:
- QUESTION-025
summary: >-
  Xiong (2026), [LIT-267](../literature.d/LIT-267.md), read in [NOTE-240](../notes.d/NOTE-240.md). Theorem 1 is the basic theorem
  of formal concept analysis applied to the crisp relation got by
  thresholding Fisher-LDA probes, and it holds for every binary relation;
  the paper's own proof plan says so. The empirical content is that the
  thresholded probes on three 7–8B models agree with a GPT-4o-annotated
  incidence at macro F1 69.7–83.2 and predict WordNet subsumption at F1
  57.1–77.1. No closure, absorption or recovered-lattice comparison is
  tested, and the paper's join is not a lattice join as written. It is not
  evidence that language models encode a lattice beyond the incidence.
---
<!-- inactive-ok-file: LIT-267 — Proposed; the paper whose theorem and measurements this account states; the account is about what they do and do not show -->
<!-- inactive-ok-file: CLAIM-119 THEORY-008 THEORY-185 — Proposed; the lattice claim and neighbouring accounts, named in Connections, not leaned on -->

# THEORY-tmpzhrlj: Thresholding linear attribute probes on a language model's embeddings yields a complete concept lattice for any incidence whatever, so the lattice is guaranteed by construction; what the Lattice Representation Hypothesis measured is per-attribute agreement with GPT-4o annotations at F1 70–83, and no lattice law

## Source

Xiong (2026), [LIT-267](../literature.d/LIT-267.md) (ICLR 2026), read in full in [NOTE-240](../notes.d/NOTE-240.md) from the
arXiv v3 camera-ready, Appendices A–D included.

## What was actually shown

**The theorem.** Each attribute m gets a direction ℓ̄_m and a threshold
τ_m. A soft incidence σ(α(v_g·ℓ̄_m − τ_m)) is cut at confidence δ into a
crisp relation I_δ. For finite objects and attributes, the closed pairs
of the Galois connection under I_δ form a complete lattice (Theorem 1,
restated as Theorem 2 in App. B). The proof uses nothing geometric. The
paper says as much: "Once I_δ is fixed, the statement becomes a standard
FCA result" (App. B). Thresholding the soft incidence is a hard threshold
at τ_m + α⁻¹ logit δ, so the soft version does no work in the theorem.

**The measurements.** Five WordNet domains (Animal, Plant, Food, Event,
Cognition), 60–184 attributes each. The attribute schema and the full
object–attribute incidence were written by GPT-4o (§4.1), and only the
is_a hierarchy comes from WordNet. Fisher-LDA probes with a midpoint
threshold on LLaMA3.1-8B, Gemma-7B and Mistral-7B recover the annotated
incidence at macro F1 69.7–83.2 (Table 1), against 50.1–68.4 for a
mean-centroid baseline and 45.0–50.1 for random. A profile-based
inclusion score predicts WordNet subsumption at F1 57.1–77.1 (Table 2),
and loses to the mean baseline once (Mistral, Plant: 57.1 against 60.5).
Meet and join operators beat baselines in mean reciprocal rank (Fig. 4),
reported only as bars.

**What could have come out otherwise.** The probes could have failed to
separate the annotated attributes, or the inclusion score could have
missed the hierarchy. Both came out above baseline. The lattice could not
have failed to exist.

## What this does not say

- **That language models encode a concept lattice.** The lattice exists
  for any incidence, including a random one. The evidence reaches the
  incidence, at 70–83 F1, and pairwise subsumption. No recovered lattice
  is compared with the annotated one, and no closure or absorption law is
  tested ([NOTE-240](../notes.d/NOTE-240.md), Limitations).
- **That the ground truth is independent of language models.** The
  incidence the probes are scored against is another language model's
  annotation, unvalidated against people.
- **That the region-level operations are lattice operations.** Def. 7
  defines the join as the set union of two cones, which is not a region.
  The conic hull it is "approximated by" is dual to the meet. The least
  region containing both is R of the Galois closure of the shared intent
  ([NOTE-240](../notes.d/NOTE-240.md), Corrections, the reader's check). None of the three is used
  in the experiments, which use coordinatewise min and max of profiles.
  Under the paper's own inclusion score those operators sit in the
  reverse order, the "meet" above A and the "join" below it, in every
  draw of the reader's simulation.
- **That the lattice is Boolean, or that it is not.** The object-level
  lattice need not be distributive even with independent directions
  ([NOTE-240](../notes.d/NOTE-240.md)'s M₃ example). The region lattice with the correct join is
  Boolean when the directions are independent. The paper never mentions
  distributivity, so which lattice "the lattice" is decides the answer.
- **That the probes use the model's own geometry.** The Fisher direction
  and midpoint threshold are functions of the embedding kernel and the
  labels, so the incidence is invariant to orthogonal maps of the
  embedding ([THEORY-004](THEORY-004.md)) and, in the unregularised limit, to any
  invertible linear map ([NOTE-240](../notes.d/NOTE-240.md), the reader's inference). The causal
  inner product of §2.1 is not used in the experiments.

## Connections

- **[QUESTION-025](../questions.d/QUESTION-025.md)** asks whether correlated or hierarchical attributes keep
  linear directions, and with them a non-Boolean lattice. This account
  constrains it: a lattice follows from any thresholded incidence, so the
  question is entirely about the incidence and its implications, and this
  paper's evidence does not test attributes that imply one another.
  [THEORY-185](THEORY-185.md) derives the linear directions this paper assumes, for
  independent attributes only, whose lattice is Boolean.
- **[CLAIM-119](../claims.d/CLAIM-119.md)** holds that communicative categories form a concept
  lattice. That a lattice exists is guaranteed for any context; what
  [CLAIM-119](../claims.d/CLAIM-119.md) needs is that the lattice predicts something a flat feature
  list does not, which is its own defeat condition.
- **[THEORY-008](THEORY-008.md).** The Fisher direction is a regularised linear readout of
  the family that account treats, so the paper's empirical content is a
  statement about the embedding kernel. Consistent with it, not evidence
  for it.
- **Van Rijsbergen ([LIT-262](../literature.d/LIT-262.md), [NOTE-239](../notes.d/NOTE-239.md)).** The same construction as his
  chapter 2, the Galois connection between documents and index terms, with
  the incidence computed from an embedding instead of given by indexing.
- **The anthology** holds the paper as [ANTH-LIT-460](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-460.md) with its account
  [ANTH-THEORY-034](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-034.md). [NOTE-240](../notes.d/NOTE-240.md)'s corrections to that reading (the join, the
  GPT-4o ground truth) are reported there, not edited from here.
