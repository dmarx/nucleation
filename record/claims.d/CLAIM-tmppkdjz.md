---
status: Proposed
title: 'Whether a direction in a learned model is small depends on the metric it is measured in, and the metrics can rank directions in opposite orders: a label can sit wholly in the least-variance component, and the predictive Fisher pulled back to a hidden state, Wᵀ(diag p − ppᵀ)W, can rank a weight matrix''s smallest singular direction above its largest'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in either construction: the classifier on z = (X, ε(Y + η))
  not reaching accuracy Φ(1/σ) for every ε > 0 when it reads the second
  coordinate exactly, or the stated unembedding not giving the stated
  orders under WᵀW and the pulled-back Fisher. Findings that in trained
  networks the metrics mostly agree do not defeat it; the claim is that
  they can disagree, and says how much more it would take to show they
  do in practice.
tags:
- information-geometry
- representation-learning
- learning-theory
date: '2026-11-21'
line:
- learned-structure
complements:
- CLAIM-450
grounds:
- THEORY-420
- THEORY-084
- LIT-tmp0gbj6
- LIT-tmp83hha
- LIT-tmp4det7
bears_on:
- QUESTION-tmp82zpm
uses:
- TERM-tmpnxjq4
summary: >-
  A41 §§2–4 and §8 of the exchange "Rich Get Richer Power Laws"
  (2026-11-21), answering the owner's U25 on recent work about informative
  small-eigenvalue subspaces: "A direction can be thin under one metric and
  consequential under another", and "a hyperribbon tells us which parameter
  combinations are distinguishable under a particular observation metric".
  The assistant checked both constructions, built the unembedding example
  A asserted without one, and corrected the scope of the variance toy.
  The wording is A's (the other assistant in the exchange "Rich Get Richer
  Power Laws", A41); adopting it is the owner's call.
---

<!-- inactive-ok-file: TERM-tmpnxjq4 ARG-tmpjx3ww LIT-tmp0gbj6 LIT-tmp83hha LIT-tmp4det7 — Proposed or new, or Deferred works registered from the exchange and not yet read -->

# CLAIM-tmppkdjz: Whether a direction in a learned model is small depends on the metric it is measured in, and the metrics can rank directions in opposite orders: a label can sit wholly in the least-variance component, and the predictive Fisher pulled back to a hidden state, Wᵀ(diag p − ppᵀ)W, can rank a weight matrix's smallest singular direction above its largest

## The claim

A41 lists four spectra, each with its own meaning for "small": a
representation's covariance, a weight matrix's WᵀW, the loss Hessian and
the Fisher matrix ([TERM-tmpnxjq4](../terms.d/TERM-tmpnxjq4.md) sorts the senses). "A direction can be
small in one of these geometries and extremely important in another."
Two constructions show the orders can be reversed, not just
uncorrelated.

**Variance against label (A41 §3).** z = (X, ε(Y + η)), with X ∼ N(0, 1),
Y = ±1 and η ∼ N(0, σ²). The label's coordinate has variance
ε²(1 + σ²), the smallest of the two for small ε, and it carries all the
label: reading its sign gives accuracy Φ(1/σ) for every ε > 0
(Φ(5) = 0.9999997 at σ = 0.2). What matters is Mahalanobis separation,
not variance.

**Logit distance against prediction (A41 §2).** With logits ℓ = Wh + b and
p = softmax(ℓ), KL(p_h ‖ p_{h+δh}) ≈ ½ δhᵀ G_pred δh, where
G_pred = Wᵀ(diag p − ppᵀ)W is the categorical Fisher pulled back to h, and
G_logit = WᵀW measures raw logit change. A credits the distinction to Xu
([LIT-tmp4det7](../literature.d/LIT-tmp4det7.md), unread).

## The assistant's additions

**An example of the reversal**, which A asserts without one (the ledger's
gap at L19). Six tokens and two hidden dimensions. Tokens 1 and 2 are
near-tied candidates (biases 10.001 and 10) that differ only along e₂,
with weights ±0.05. Tokens 3–6 are implausible (bias 0) with weights ±3
and ±2 along e₁. The singular values of W are 5.10 (e₁) and 0.071 (e₂).

| direction | vᵀG_logit v | vᵀG_pred v | step of 0.05: logit change | KL | top token |
|---|---|---|---|---|---|
| e₁ (largest) | 26.0 | 0.00059 | 0.255 | 7.4 × 10⁻⁷ | unchanged |
| e₂ (smallest) | 0.0050 | 0.0025 | 0.0035 | 3.1 × 10⁻⁶ | flips 1 → 2 |

The logit metric ranks e₁ above e₂ by 5,200 to 1. The predictive metric
ranks e₂ above e₁ by 4 to 1. The reversal is not generic: for random
500 × 20 Gaussian unembeddings at a random hidden state, the Spearman
correlation between singular value and vᵀG_pred v averaged 0.85 over 200
draws (range 0.33 to 0.99). That trained unembeddings show the reversal
systematically is Xu's empirical claim, not checked here. Checked with
`python3 -I` (`t5/check5.py`, `check6.py`).

**A limit on the variance toy.** A's caption says it "assumes
arbitrarily precise measurements". With fixed additive readout noise τ
on the small coordinate, accuracy is Φ(ε/√(ε²σ² + τ²)), which falls to ½ as
ε → 0. At σ = 0.2 and τ = 0.01 it is 1.000, 1.000, 0.837 and 0.540 at
ε = 1, 0.1, 0.01, 0.001. A Monte Carlo of 10⁶ draws gives 0.8368 at
ε = 0.01 against 0.8366. So a low-variance direction carries its label
only down to the scale of the noise downstream of it. Finite precision,
weight decay on the readout and additive noise all set that scale.

## Task sensitivity relative to variance (A41 §4, §6)

Added 2026-11-21, from the same turn; the wording quoted is A's (the other
assistant in the exchange "Rich Get Richer Power Laws", A41), the check
the assistant's.

**A coordinate for the disagreement (A41 §4).** "One possible construction
is a generalized eigenvalue problem: G_task v = λ(C_repr + εI)v, where εI
provides regularization. The leading generalized eigenvectors identify
directions with high task sensitivity relative to their representation
variance." It sorts directions into large variance and little task
importance, small variance and little, and small variance but high
importance, and "The third class is the one the recent studies make
particularly interesting." A adds that it "is not a substitute for mutual
information, and the specific matrices must be chosen carefully."

With G_task the outer product of the difference of class means, the
problem is Fisher's linear discriminant, and the leading eigenvalue is a
squared Mahalanobis separation. On this claim's variance toy (writing δ
for A's regularizer, since ε is the toy's scale), the means differ by 2ε
along the second coordinate, whose variance is ε²(1 + σ²), so the leading
generalized eigenvalue is 4ε²/(ε²(1 + σ²) + δ), along that coordinate. At
δ = 0 it is 4/(1 + σ²) = 3.85 at σ = 0.2 for every ε: the smallest-variance
direction ranks first, as the claim says it should. At δ = 10⁻⁴ it is 3.81,
1.96 and 0.040 at ε = 0.1, 0.01 and 0.001. The regularizer acts as the
readout-noise floor τ² of the section above: below it, a low-variance
direction loses its rank. So δ is not a numerical convenience; it states
the precision at which "quiet" directions are read. Checked with
`python3 -I` (scipy's generalized symmetric eigensolver).

**Reallocating importance without reallocating variance (A41 §6).**
"Progressive learning could involve the network reallocating *functional
importance* across the spectrum without necessarily reallocating much
variance." A names three mechanisms it calls different: a downstream layer
learning to read a feature whose "raw variance changes very little"; a new
direction learned "in the spectral tail"; and "a change in the mapping
between representations and outputs". On this claim's terms, the first and
third move a direction's rank under G_task, or under the pulled-back
Fisher, while its rank under C_repr stays put; only the second changes the
variance spectrum. Which one occurs is [QUESTION-tmp82zpm](../questions.d/QUESTION-tmp82zpm.md)'s to settle.

## What the small-eigenvalue findings add, and do not

A41 cites four findings: small singular values of transformer weights
matter (Staats et al.; the record holds this reading, [THEORY-420](../theory.d/THEORY-420.md), which
includes the fine-tuning order); concept directions sit in the
low-variance tail of the unembedding covariance (Acharya et al.,
[LIT-tmp0gbj6](../literature.d/LIT-tmp0gbj6.md)); SGD progresses in the Hessian's bulk, not its top
subspace (Song et al., [LIT-tmp83hha](../literature.d/LIT-tmp83hha.md)); and the unembedding's smallest
directions move next-token distributions most (Xu, [LIT-tmp4det7](../literature.d/LIT-tmp4det7.md)). The
last three are unread. They bear on this claim as instances of metrics
disagreeing. A41 §8 also presents them as a correction to the hyperribbon
account. [ARG-tmpjx3ww](../arguments.d/ARG-tmpjx3ww.md) weighs that, and finds they do not bear on it: a
hyperribbon is already defined in the metric of the predictions.

This claim complements [CLAIM-450](CLAIM-450.md). That claim has distinguishability,
usability and efficacy coming apart for a communicative distinction. This
one has several geometries of the same learned model coming apart in the
order they give.

## Note of 2026-11-21: Transtrum, Machta & Sethna (2011) and Transtrum et al. (2015), read

A parallel that supports the claim's metric-dependence. Both say the
Fisher spectrum depends on the parametrization: "one can always
reparametrize the manifold to make the metric at a point any symmetric,
positive definite matrix" (2011, p. 6; NOTE-tmpzxtnv); "the FIM can be
transformed into any positive definite matrix by a simple linear
transformation of parameters" (2015, §III; NOTE-tmphbpab). Their answer is
to measure in the metric of the predictions, the model manifold's widths,
which is one of the metrics this claim sets side by side. They do not
compare that metric with the others the claim names. No relation is
written: the readings bear on the claim as background, not as evidence
for its ordering result.
