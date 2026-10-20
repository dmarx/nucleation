---
number: 270
status: Active
formerly:
- THEORY-tmpkpfpe
title: "In Goldwasser, Gruber, Kalai and Paradise's common-nonsense model, where the source language and the plausibility prior are uniform over sets from which shared random nonsense is removed and translators are one-to-one, maximum likelihood with the prior alone translates without parallel data with error O(log|Θ| / (α·min(m, |T|))) with high probability, falling in the shared nonsense α, in the size of the source language and in the number of samples"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted at the owner's direction, carrying out the
    promotion audit's decision for THEORY-270 (batch 044, ADR-047 v2).
    The upper bound of the common-nonsense model (Theorem 3.4, with
    Lemma C.1 and Proposition C.2) was re-derived from LIT-941's
    Appendix C.1, in the dated note below; Theorem A.2 had been re-derived
    in batch 038. The title is narrowed from "translation without parallel
    data is learnable" to that model and its bound. The knowledge-graph
    model and the lower bound stay in the body as the paper's statements.
    The former promote_when, a bound outside the uniform, lossless models,
    moves to QUESTION-195.
tags:
- translation
- learning-theory
- information-theory
date: '2026-10-14'
source:
- LIT-941
summary: >-
  Goldwasser, Gruber, Kalai and Paradise (NeurIPS 2023), [LIT-941](../literature.d/LIT-941.md), read in
  [NOTE-804](../notes.d/NOTE-804.md). Proved for maximum likelihood in stylised random models
  with uniform languages and one-to-one translators; in one model the bound
  O(log|Θ| / (α·min(m,|T|))) is tight up to a constant. Information-
  theoretic only. The prior substitutes for parallel data in learning the
  decoder, not for information in a message.
---
<!-- inactive-ok-file: THEORY-170 CLAIM-054 — Proposed; theories and claim this account bears on, open -->

# THEORY-270: In Goldwasser, Gruber, Kalai and Paradise's common-nonsense model, where the source language and the plausibility prior are uniform over sets from which shared random nonsense is removed and translators are one-to-one, maximum likelihood with the prior alone translates without parallel data with error O(log|Θ| / (α·min(m, |T|))) with high probability, falling in the shared nonsense α, in the size of the source language and in the number of samples

## Source

Goldwasser, Gruber, Kalai and Paradise (2022; NeurIPS 2023), [LIT-941](../literature.d/LIT-941.md), read
in full in [NOTE-804](../notes.d/NOTE-804.md): Definition 1.1, Theorems A.2, 3.2, 3.4, 3.5, B.1
and J.1, and Appendix E.

## What was actually shown

The learner sees m unlabelled source texts and can query a prior ρ that
scores how plausible a target text is. It picks the translator in a finite
family Θ that maximises Σ log ρ(f_θ(x_i)).

- **General bound (Theorem A.2).** If every translator with large loss
  makes more than a γ fraction of its translations impossible under ρ, then
  m ≥ (1/γ) ln(|Θ|/δ) samples suffice for MLE to have loss at most that
  of the worst translator that does not. This is the realisable Occam
  bound with "impossible under the prior" in place of "wrong label".
- **Common nonsense (Theorems 3.4, 3.5).** Prior and translations are
  uniform over sets from which a shared random α-fraction of texts is
  removed. Then err = O(log|Θ| / (α·min(m, |T|))) with probability 0.99,
  and some family of no greater size forces error ≥ log|Θ| / (c·α·min(m,
  |T|)) on any algorithm.
- **Knowledge graphs (Theorem 3.2).** Correlated random graphs with
  agreement α and edge density p over r source nodes:
  err = O(log n/(α²pr) + (1/α)√(r log n / m)). The first term is a floor
  that only richer per-node knowledge lowers.
- **Experiments.** Ten-node graphs: with α = 0.5, accuracy rises from 0.10
  at r = 4 to 1.00 at r = 10.

## What this does not say

- **Not that the receiver's knowledge replaces information in a message.**
  What the prior replaces is parallel data in learning the translator. The
  product α·min(m, |T|) is an exchange rate between common ground and
  source data for learning a code, not a rate–distortion trade-off for
  sending one message.
- **Not about natural languages.** The models are uniform and random by
  design and "not intended to accurately capture natural language".
- **Not about lossy translation.** Translators are one-to-one into a target
  that can say everything the source says. The lossy objective of
  Appendix I.1 is not analysed.
- **Not computational.** MLE over Θ may be intractable; no efficient
  algorithm is given.
- **Not that a good-looking translation is a right one.** The paper's own
  §4 notes that translations can match the prior and be wrong.

## Connections

No relations are declared: the account bears on [QUESTION-020](../questions.d/QUESTION-020.md) without
answering it, since the question asks about information in an utterance
and this is about data for learning a decoder.

- **[QUESTION-020](../questions.d/QUESTION-020.md).** The nearest formal result the record holds to its
  question: a receiver's prior lowers what must be observed, at a rate
  1/α. Its "explicit explanatory material" for an unfamiliar reader has a
  counterpart only in the paper's informal "background prompts" (App. H).
- **[THEORY-170](THEORY-170.md).** It says translation must add and drop information
  between grammars. This account holds only in the lossless case that
  [THEORY-170](THEORY-170.md) says is not the general one.
- **[CLAIM-054](../claims.d/CLAIM-054.md).** Plausibility to the receiver and correctness against the
  source come apart here too, as §4's "judging success" notes.
- **[THEORY-161](THEORY-161.md).** Both treat meaning against a known joint law; here the
  law is replaced by a prior over the target and a ground-truth map,
  unknown to the learner.

## Note of 2026-10-19: the common-nonsense upper bound, re-derived

The promotion audit (batch 044) worked through [LIT-941](../literature.d/LIT-941.md)'s Appendix C.1
(arXiv:2211.11081v2). Setting: T ⊆ P ⊆ Y finite; S ⊆ Y keeps each y
independently with probability β = 1 − α; τ = U(T ∩ S) and ρ = U(P ∩ S);
each translator f_θ is one-to-one, and π_θ = f_θ∘f⋆⁻¹ is extended to a
permutation of Y. ε_γ is the largest error among translators that make at
most a γ fraction of translations impossible under ρ.

- **Proposition C.2.** The points a permutation moves split into A1, A2,
  A3 with π(A_i) ∩ A_i = ∅: alternate each cycle between A1 and A2, and
  put the last element of an odd cycle in A3.
- **Lemma C.1.** For γ ≥ (8/(β|T|)) ln(4|Θ|/δ), with probability ≥ 1 − δ,
  ε_γ ≤ 6γ/α. Put a = 6γ/α. A Chernoff bound gives |T ∩ S| > β|T|/2
  except with probability below δ/4. Fix π and intersect each A_i with T
  (the source computes τ(A_i) as if A_i ⊆ T; intersecting keeps
  π(A_i) ∩ A_i = ∅). Error above a puts τ(A_i) > a/3 for some i. Given
  V = A_i ∩ T ∩ S of size at least βa|T|/6, making at most a γ fraction
  impossible forces fewer than an α/2 fraction of π(V) outside S. Those
  indicators are independent Bernoulli(α) even given A_i ∩ S, because π
  is one-to-one and maps A_i outside itself, so Chernoff bounds the event
  by e^{−α|V|/8} ≤ e^{−βγ|T|/8} ≤ δ/(4|Θ|). A union over the three parts
  and the |Θ| translators completes it.
- **Theorem 3.4.** With γ = max(1/m, 8/(β|T|)) ln(6|Θ|/δ), Lemma C.1 at
  confidence 2δ/3 and Theorem A.2 at δ/3 give, with probability ≥ 1 − δ,
  err(θ̂) ≤ (6/α) max(1/m, 8/(β|T|)) ln(6|Θ|/δ) ≤ (6/α) max(1/m, 16/|T|)
  ln(6|Θ|/δ) for α ≤ 1/2.

Not re-derived: the lower bound (Theorem 3.5, App. C.2) and the
knowledge-graph bound (Theorem 3.2, App. D). The title claims neither.
