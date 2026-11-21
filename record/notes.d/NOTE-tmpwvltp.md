---
status: Read
paper: LIT-2959
title: 'Acharya, Rimal & Dhakal — Concepts Whisper: spectral anti-concentration and the dual geometry of transformer representations'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    From the arXiv PDF of 2605.01609v2 (29 Aug 2026; v1 2 May 2026),
    25 pp., fetched 2026-11-21 from arxiv.org without obstacle. Read in
    full: §§1–9, Limitations, Ethics, Appendices A–M with Tables 1–15;
    figures through their captions; references skimmed. The ACL Anthology
    landing page (EMNLP 2026 main, 2026.emnlp-main.2362) was fetched and
    its title matches; its PDF was not fetched or compared with v2. Read
    beside it, for Theorem 3.2 and Eqs. 3.3 and 4.1 only: Park, Choe and
    Veitch, arXiv 2311.03658v2, already held (LIT-304, NOTE-302). Read by a
    reader subagent; filed by a second one, which rechecked every quote
    used here against a fresh pdftotext extraction of both PDFs. No email
    address sent.
date: '2026-11-21'
summary: >-
  Whitening by the causal inner product does not help cross-lingual
  Procrustes transport beyond its eigenvalues. In the eigenbasis of the
  unembedding's regularized uncentred second moment (WᵀW up to scale and
  ridge), word-level concept directions taken from activations put less of
  their energy in the top eigendirections than a uniform-in-variance
  baseline in all 17 models, and more in the tail than norm-matched random
  directions in 13 of 17; differences of the same concepts' unembedding
  rows lean the other way. The paper reads the flip as a rotation by the
  forward pass; Park, Choe and Veitch's map predicts it as a rescaling.
---
<!-- inactive-ok-file: THEORY-tmpklef6 CLAIM-tmpqy8mq ARG-tmp801ah CLAIM-835 ARG-139 TERM-138 LIT-tmpcvxug — Proposed or new; the account this reading files, the entries it bears on, and a work registered from it, Deferred -->

# NOTE-tmpwvltp: Acharya, Rimal & Dhakal — Concepts Whisper: spectral anti-concentration and the dual geometry of transformer representations

## Contribution

1. A negative result for the causal inner product in transport: with
   Haar-random eigenvectors and the true eigenvalues, results are the same
   (50.3% against 51.0% win rate, p = 0.95; §4), so "any observed benefit of
   WCA is attributable to spectral regularization".
2. A 17-model measurement of where concept vectors sit in the
   right-singular basis of the unembedding.
3. A sign flip between activation-side and vocabulary-side concept
   vectors, the "dual geometry".

## Key insight

Concept vectors read from activations put their energy where the
unembedding amplifies little; the same concepts read as differences of
unembedding rows put it where the unembedding amplifies much.

## Assumptions

- **The spectrum** (Eq. 1, p. 2) is "the regularized uncentered second
  moment of the unembedding rows", Σ_L = (1/|L|)Σ γ(w)γ(w)ᵀ + τI, τ = 0.1:
  "For brevity we refer to Σ_L as the unembedding covariance throughout".
  Its eigenvectors are the unembedding's right singular vectors, so up to
  scale and ridge it is the logit metric WᵀW. It is not an activation
  covariance: "activation-covariance spectra may reveal additional
  structure" (Limitations).
- **The statistic** (§3): energy fractions (vᵀu_i)²/‖v‖² accumulated
  against cumulative variance, Gini deviation the signed area against a
  uniform-in-variance baseline. A random direction already scores
  negative: "random unit vectors evaluated in these spectra are themselves
  negative (−0.16 to −0.28), so the raw statistic cannot separate the two"
  (§5).
- Concept directions: differences of means of final-layer pooled
  activations over counterfactual word pairs, SAE decoder columns, and
  probe weights; vocabulary side, means of γ(w⁺) − γ(w⁻). 27 word-level
  concepts plus 15 BATS categories. Whether the final norm's gain is
  folded into W_U is not stated.
- Euclidean norm on the residual stream; one basis from the LM head for
  every layer; base decoder-only models.

## Key results

- **Raw** (§5): "the mean Gini deviation is −0.282 and all 17 models are
  negative".
- **Against the matched null** (§5): concept directions are "more
  tail-aligned than their matched nulls in 13 of 17 models, with a mean
  true-minus-null Gini gap of −0.082"; Llama 3.2 (1B and 3B),
  Mistral-7B-v0.3 and OLMoE are the exceptions.
- **Three methods agree** (Table 4): SAE features −0.19 to −0.28; probes on
  two models; probes failed on a third.
- **Depth** (§5): "near-neutral at the embedding layer", −0.17 at layer 0,
  deepest near mid-depth. No training checkpoints anywhere.
- **Dual geometry** (§7): unembedding contrasts "concentrate in
  high-variance eigendirections (positive Gini), the opposite sign of
  activation-space directions"; "Random pairs mildly anti-concentrate
  (mean Gini ≈ −0.10); concept pairs concentrate (mean ≈ +0.07); p < 10⁻⁴"
  on four models. The paper's reading: the unembedding places contrasts
  "where they maximally influence logit differences", while activations
  "encode the same concepts in the spectral tail"; the depth profile
  "supports the interpretation that the forward pass rotates concept
  information from the vocabulary geometry into the low-variance
  activation subspace" (App. E), and the flip is "incompatible with a pure
  anisotropy account" (§5).
- **Steering** (§8, Table 5): injecting the top-10% component raises
  perplexity more than the bottom-10% in 4 of 5 models, in a window that
  "is post-hoc"; "whether it preserves concept-manipulation strength is
  untested" (§9).
- **POS probing** (Table 6): top-k beats bottom-k in 6 of 8 models by 1.6
  to 5.2 points; both Qwen 2.5 models reverse.
- **No dynamics**: "Our layer-wise analysis is descriptive"
  (Limitations).

## Concepts

- **Spectral anti-concentration**: this energy-against-variance
  statistic, not the probabilistic term of art (small-ball estimates).
- **Gini deviation**, **SCM** (the cumulative variance at half the
  energy).
- **Dual geometry**: activation-side against vocabulary-side concept
  vectors.
- **Causally separable concepts** (p. 1), Park et al.'s sense.

## Connections

The basis is Xu's, up to scale (NOTE-tmp454fw). The causal inner product
is Park, Choe and Veitch's (LIT-304, THEORY-018). The paper cites Staats et
al. (THEORY-420) and LASER (Sharma et al.; LIT-tmpcvxug, registered from
this reading).

## Bearing on the record

Filed as THEORY-tmpklef6. Dated notes of 2026-11-21 on each entry below.

- **CLAIM-835**: weak support at most. The paper works in one metric, the
  logit metric, and asks where concept vectors point in it; its own effect
  measures, perplexity under steering and POS probing, run with that
  metric, not against it. It shows no reversal of the claim's kind. It
  does show a direction's place depending on which vector of a concept is
  measured (ARG-139).
- **ARG-139**: corrects a premise. The spectrum is the unembedding's
  second moment, not representation variance, and the measure is
  Euclidean energy, not a separation. The four findings are three spectra.
- **CLAIM-tmpqy8mq**, **ARG-tmp801ah**: the dual geometry's sign is what
  Park, Choe and Veitch's map λ̄ ∝ Cov(γ)⁻¹γ̄ predicts, a rescaling in a
  fixed eigenbasis; the reader's idea, checked by the lead (filed in the
  assistant's voice).
- **QUESTION-511**: leaves open; the only trajectory is through depth.
  The statistic is not invariant under h ↦ Ah, W ↦ WA⁻¹, which leaves the
  logits unchanged (THEORY-018, THEORY-234).
- **TERM-138**: "causally separable" is a sense the term does not list.
- **THEORY-018**: the WCA null fits its thesis that no eigenbasis of the
  causal inner product is intrinsic.

Nothing here is filed as an instruction for machine-learning practice.

## Limitations

- Word-level single-token concepts; base models; one unembedding-derived
  basis applied at every layer.
- The raw statistic is confounded with anisotropy, as the paper says; the
  matched-null effect is modest and absent in 4 of 17 models.
- Steering window post-hoc, uncorrected across 30 configurations; POS gaps
  of a few points, reversed in two models.
- A gap in the argument: the dual geometry is read as a rotation without
  comparing the activation vectors with Park et al.'s Σ⁻¹γ̄, the embedding
  representation the paper's own source predicts (CLAIM-tmpqy8mq).
