---
number: 270
status: Proposed
formerly:
- THEORY-tmpkpfpe
promote_when: >-
  A proof of the same kind of bound outside the uniform, lossless models:
  for non-uniform (for instance Zipfian) source languages, or for lossy
  translators, an error bound that still falls in the common ground and in
  the size of the source language, with a lower bound to match. Or an
  experiment on real corpora in which the error of prior-scored translation
  without parallel data falls with measured common ground at the predicted
  rate. It is refuted for natural settings by a non-uniform model in which
  richer source languages do not reduce the common ground needed. What
  cannot settle it: further synthetic runs in the same two models, which
  only confirm the proofs.
title: 'Translation without parallel data is learnable from a plausibility prior over the target language alone, with error falling in the common ground between prior and translations, in the size of the source language and in the number of samples'
version: 1
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
<!-- inactive-ok-file: THEORY-170 THEORY-161 CLAIM-054 — Proposed; theories and claim this account bears on, open -->

# THEORY-270: Translation without parallel data is learnable from a plausibility prior over the target language alone, with error falling in the common ground between prior and translations, in the size of the source language and in the number of samples

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
