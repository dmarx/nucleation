---
number: 230
status: Active
formerly:
- THEORY-tmpbbojk
title: 'The Fisher–Rao geometry of a language model''s next-token laws over a set of contexts is a function of those laws alone, so models with identical laws share it, while activation geometry changes under invertible reparameterizations of the hidden layer that leave outputs unchanged; in Picozzi''s ten transformer, state-space and recurrent models it agreed at a mean rank correlation of 0.88 against 0.62 for activation geometry, and about 9% of the top eigenvector overlap exceeded a null matched to the shared laws'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-230 (batch 049). The identification is re-derived in the dated
    note below (ADR-047 v2). The measurement is one study read in full,
    with every number in the text or a Supplementary Note (ADR-047 v3).
    "Ten architectures" becomes ten models of three kinds, "far more"
    becomes the numbers, and "what the shared laws imply" becomes the
    displacement-matched null. The promote_when moves to QUESTION-216.
tags:
- information-geometry
- representation-learning
date: '2026-10-14'
source:
- LIT-936
summary: >-
  Picozzi (2026), [LIT-936](../literature.d/LIT-936.md), read in [NOTE-755](../notes.d/NOTE-755.md), a single-author v1
  preprint with code on request. The matrix of Fisher–Rao distances between
  a model's next-token laws on a context battery is invariant to every
  output-preserving reparameterization, while activation geometry has a
  GL(d) gauge (Prop. 1); two models with identical outputs can have hidden
  geometries that rank-correlate at −4/17 (Prop. 3). Over ten transformer,
  state-space and recurrent models the mean rank agreement is 0.88 against
  0.62 for mid-layer activations. Convergence is proved only as a
  consequence of each model's excess risk to a common law, and that bound
  is vacuous on real models. Against a law-matched null, about 9% of the
  top-six eigenvector overlap is shared beyond the laws.
  Promoted on 2026-10-20. Replication and a test that varies the law are
  QUESTION-216.
---
<!-- inactive-ok-file: QUESTION-027 QUESTION-052 CLAIM-142 CLAIM-193 CLAIM-209 THEORY-002 — Open or Proposed; cited for context, nothing here rests on them -->

# THEORY-230: The Fisher–Rao geometry of a language model's next-token laws over a set of contexts is a function of those laws alone, so models with identical laws share it, while activation geometry changes under invertible reparameterizations of the hidden layer that leave outputs unchanged; in Picozzi's ten transformer, state-space and recurrent models it agreed at a mean rank correlation of 0.88 against 0.62 for activation geometry, and about 9% of the top eigenvector overlap exceeded a null matched to the shared laws

## Source

Picozzi (2026), [LIT-936](../literature.d/LIT-936.md), read in [NOTE-755](../notes.d/NOTE-755.md): Part I (Eq. 1, Theorem 2,
Lemma 2, Propositions 1 and 3), Part II (agreement measurements,
Theorems 6 and 8, Remark 2, SN18, SN19) and the synthetic language
assignment (SN3.1).

## What was actually shown

**Identification, by construction.** For a battery of contexts, the
relational geometry is the matrix d_ij = 2 arccos Σ_a √(p_i(a) p_j(a)) of
Fisher–Rao distances between next-token laws. It is a function of the
laws, so it is unchanged by any reparameterization that leaves outputs
unchanged (Lemma 2(a), "immediate"). Activation geometry is not: for every
A ∈ GL(d), (g ∘ A⁻¹) ∘ (A h) has the same outputs and a different Gram
matrix (Prop. 1). Two models with identical outputs can have hidden
relational geometries whose rank agreement is −4/17 (Prop. 3), so output
agreement puts no floor under activation agreement. Random anisotropic
reparameterizations leave output agreement constant to machine precision
while activation CKA, mutual k-NN and cosine RSA degrade.

**Sharing, proved only through the laws.** On a shared outcome space,
E{d_A − d_B}² ≤ 4(ε_A + ε_B) for root-probability distances, where ε is
each model's excess risk to a common law (Thm 6), and rank agreement tends
to 1 as the risks vanish (Thm 8). On real models the worst-case form is
"vacuous" (Remark 2). The measured stability is explained instead by low
coherence: the directions in which models disagree are nearly orthogonal
to the relational structure (median coherence 0.024–0.034).

**Measured agreement.** Over ten models from 70M to 7B parameters, seven
training pipelines and four tokenizers, the mean Spearman agreement of
output distance matrices is 0.88 on natural text, against 0.62 for
mid-layer and 0.61 for last-layer activation geometry, with a bootstrap
interval on the gap excluding zero. At the first byte, cross-tokenizer
agreement is 0.91.

**What exceeds the laws (SN18).** The top-six cross-family eigenvector
overlap is 0.698. A null matched in displacement magnitude, which follows
from the shared output laws alone, gives 0.636. The residual, +0.063
(+0.056 to +0.070), is "about 9% of the raw overlap".

**The law decides, in synthetic languages (SN3.1).** Three architectures at
two capacities trained on eight pairs of synthetic languages: the assigned
law recovers 0.998 of the imposed separation, and changing architecture
within a law leaves the geometry nearly unchanged.

What could have failed: architectures fitted to one corpus could have
disagreed in output geometry as much as they do in activations. They did
not.

## What this does not say

- **Not a signature identified beyond the probes.** The geometry is
  identified because it is a function of the observed laws, the in-probe
  case [QUESTION-027](../questions.d/QUESTION-027.md) calls automatic. The two results that reach past the
  battery, a 40-anchor probe transferred between models (0.659 against
  0.724 within model, chance 0.125) and a risk-to-human-alignment relation
  applied to unseen families (r = 0.758), are empirical and narrow.
- **Not that the models share something beyond their behaviour.** Only
  about 9% of the eigenvector overlap does, and it is graded by training
  lineage. The paper does not separate law from corpus on natural text.
- **Not that the bounds explain the agreement.** Theorems 6 and 8 are
  vacuous on real models. The explanation offered, low coherence, is a
  measurement, and the paper says a pair disagreeing along relational
  directions "could agree far less at the same per-context excess risk".
- **Not that the shared geometry is semantic.** Its alignment with a
  Sentence-BERT geometry is 0.044 on natural text.
- **Not across tokenizers in the native vocabulary.** Convergence is
  proved on a shared outcome space; native cross-tokenizer agreement is
  measured only.
- **Not the steering, editing and fine-tuning results.** Most of the paper
  uses the pullback Fisher metric for interventions. That is
  machine-learning practice and belongs in the anthology.

## Connections

- **[THEORY-002](THEORY-002.md).** A measured form of the Platonic hypothesis recast in
  output geometry, where convergence follows from predictive fit. It fits
  [THEORY-002](THEORY-002.md)'s reading that what converges is fixed only up to the
  symmetry of what is observed: here what is observed is the law, and the
  geometry is a function of it.
- **[CLAIM-148](../claims.d/CLAIM-148.md).** Propositions 1 and 3 restate its point for networks: the
  GL(d) gauge of a hidden layer is not a symmetry of anything observable.
- **[CLAIM-142](../claims.d/CLAIM-142.md) and [CLAIM-193](../claims.d/CLAIM-193.md).** Agreement on the battery holds because
  disagreement falls in directions the battery's relational structure does
  not see, a measured instance of agreement relative to probes.
- **[THEORY-175](THEORY-175.md).** Distances to matched anchors transfer between models with
  loss, here with Fisher–Rao distances on outputs instead of cosines on
  activations. Transfer goes through the consensus; the model-specific
  residual transfers at 0.091, below chance.
- **[QUESTION-052](../questions.d/QUESTION-052.md).** The output Fisher's leading eigenspace is where
  cross-model sharing concentrates. It is the eigenspace of a per-context
  covariance operator, not of the pair operator the question defines.
- **[QUESTION-027](../questions.d/QUESTION-027.md) and [CLAIM-209](../claims.d/CLAIM-209.md).** Evidence for the unrestricted form only.

## Note of 2026-10-20: the identification, re-derived

For the promotion audit (batch 049). The relational geometry is
d_ij = 2 arccos Σ_a √(p_i(a) p_j(a)) over the battery, a function of the
next-token laws p_i alone. Any reparameterization that leaves every
output unchanged leaves every p_i, and so d, unchanged; two models with
identical laws on the battery have the same matrix. For the hidden layer,
take an invertible A and replace the hidden state h by Ah and the
readout g by g ∘ A⁻¹. Every output is unchanged, and the Gram matrix
becomes hᵢᵀAᵀAhⱼ, which differs from hᵢᵀhⱼ unless A is orthogonal
(Prop. 1). The measured numbers are as [NOTE-755](../notes.d/NOTE-755.md) reports them from the
text and SN18. The residual +0.063 is 0.063 / 0.698 ≈ 9% of the raw
overlap.
