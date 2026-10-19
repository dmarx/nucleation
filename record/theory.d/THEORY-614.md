---
number: 614
status: Proposed
formerly:
- THEORY-tmpqkmcq
promote_when: >-
  A reading of LIT-797's Appendices B–C, or a re-derivation, of the one
  step the record has not checked in Theorem 1. The likelihood of the
  prompt is summed over the hidden delimiter states, because the HMM's
  state carries across delimiters. That sum must be bounded by the
  product of per-example factors, times the c₁–c₄ ratios of Assumption 2.
  With that step, the posterior-concentration argument in the note of
  2026-10-19 closes, at least for finitely many concepts. Evidence about
  trained networks cannot settle it, since the title disclaims that
  clause. That question is QUESTION-161.
title: "If pretraining text is a mixture of hidden Markov models indexed by a latent concept and a model fits that distribution exactly, then a prompt of concatenated examples moves the posterior onto the prompt's concept, and the in-context predictor becomes Bayes-optimal as examples accumulate, whenever each example's evidence for the concept outweighs the cost of the improbable transitions between examples; whether trained networks learn in context this way is not shown"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Corrected, status unchanged, carrying out the promotion audit's batch
    026 decision for THEORY-614. The promote_when asked for evidence about
    trained language models, the clause the title disclaims. It moves
    unchanged to QUESTION-161. The new promote_when asks for the one
    step of Theorem 1's proof that the record could not re-derive. The
    partial re-derivation is in the dated note below.
tags:
- probabilistic-modeling
- learning-theory
date: '2026-10-16'
source:
- LIT-797
summary: >-
  Xie, Raghunathan, Liang & Ma (2021), [LIT-797](../literature.d/LIT-797.md), read in [NOTE-633](../notes.d/NOTE-633.md).
  Theorem 1 is proved under Assumptions 1–5 and a distinguishability
  condition; Theorems 2–3 give roughly 1/k excess risk without it. The
  proofs were not followed in the reading. [NOTE-633](../notes.d/NOTE-633.md) declined a THEORY
  because the result is conditional on exact fit to a specific generative
  model, so it is a consequence of that model, not a fact about language
  models. It is filed Proposed under the owner's ruling, with the
  condition in the title.
---

<!-- inactive-ok-file: CLAIM-029 — Proposed; named for the reading it uses, not leaned on -->

# THEORY-614: If pretraining text is a mixture of hidden Markov models indexed by a latent concept and a model fits that distribution exactly, then a prompt of concatenated examples moves the posterior onto the prompt's concept, and the in-context predictor becomes Bayes-optimal as examples accumulate, whenever each example's evidence for the concept outweighs the cost of the improbable transitions between examples; whether trained networks learn in context this way is not shown

## Source

Xie, Raghunathan, Liang & Ma (2021), "An Explanation of In-context
Learning as Implicit Bayesian Inference", arXiv v6, [LIT-797](../literature.d/LIT-797.md), read in
[NOTE-633](../notes.d/NOTE-633.md). Sections 1–6 in full, with the heuristic derivation of §3.2
followed step by step. The proofs in Appendices B–E were not followed.

## What was actually shown

**The mechanism.** p(y | prompt) = ∫ p(y | θ, prompt) p(θ | prompt) dθ.
If p(θ | prompt) concentrates on the prompt concept θ*, the model
"selects" the task by marginalising. A prompt does not teach the model
anything; it moves the posterior over which mixture component is
generating the text.

**Theorem 1.** Under Assumptions 1–5 (delimiter states, bounded
transitions into them, a prompt start distribution close to θ*'s, θ* ∈
Θ, regularity) and Condition 1, Σ_j KL_j(θ* ‖ θ) > ε_start + ε_delim for
every θ ≠ θ*: as the number of examples n → ∞, argmax_y p(y | S_n,
x_test) → argmax_y p_prompt(y | x_test), so the 0-1 risk tends to the
optimum. The prompt is out of distribution as a whole, and the mismatch
costs a bounded amount per example while the evidence grows with every
token.

**Theorems 2–3.** Without distinguishability, the excess risk is bounded
by roughly O(1/k) in example length k.

**GINC.** On a synthetic mixture of five concepts (about 10M tokens),
Transformers and LSTMs learn in context, with accuracy rising in n and k.
Ablating the mixture or the structure removes the ability, and unseen
concepts fail.

What could have come out otherwise: on GINC the trained models could have
failed to learn in context, or ablating the mixture could have left the
ability intact. Neither happened. The theorems themselves are
consequences of the model.

## What this does not say

- **That language models do this.** The analysis is of the pretraining
  distribution under exact fit. The gap between that and a trained
  network is not studied, and the paper calls it "a first step" (C6,
  not supported).
- **What the network computes.** It is silent on mechanism. Von Oswald et
  al.'s account ([THEORY-169](THEORY-169.md)) says what attention computes; the two are
  at different levels and are not rivals as stated.
- **Anything about misspecification or new concepts.** θ* ∈ Θ is
  assumed; GINC shows unseen concepts fail.
- **That GINC is independent evidence.** It was built to satisfy the
  assumptions, so it checks consistency, not truth about the world.
- **That order effects or zero-shot beating few-shot refute a Bayesian
  reading.** Both arise inside the model from distribution mismatch
  ([NOTE-633](../notes.d/NOTE-633.md), Bearing).

## Connections

- [THEORY-169](THEORY-169.md) (in-context learning as an implicit gradient step in
  attention) is the mechanistic account; Min et al. ([LIT-814](../literature.d/LIT-814.md)) cite this
  paper as the account their measurements bear on.
- [CLAIM-029](../claims.d/CLAIM-029.md) uses this reading for the formal sense in which a context
  fixes a posterior over a latent concept.
- The latent-document structure is a topic model's (LDA), with no
  inference algorithm run.
- [QUESTION-161](../questions.d/QUESTION-161.md) carries the former promotion condition, about trained
  networks.

## Note of 2026-10-19: how far Theorem 1 re-derives

From the promotion audit (batch 026). Take finitely many concepts θ.
Write log p(θ | S_n) − log p(θ* | S_n) as the log prior ratio plus a sum
over the n prompt examples. Each example contributes its within-example
log-likelihood ratio and boundary terms at its delimiter and start.

- **The within-example term.** Under the prompt distribution, its
  expectation is −Σ_j KL_j(θ* ‖ θ).
- **The boundary terms.** Assumptions 2 and 5 bound them by
  ε_delim + ε_start. They also bound every log probability, so the
  summands are bounded and independent across examples.
- **Concentration.** By the strong law,
  n⁻¹ log[p(θ | S_n)/p(θ* | S_n)] has limit at most
  −(Σ_j KL_j − ε_start − ε_delim). Condition 1 makes that negative.
  So the posterior concentrates on θ*, and Assumption 3's Δ/4 margin
  preserves the argmax.

The step that does not close is the first: the decomposition into
per-example terms. The hidden state carries across delimiters, so the
likelihood is a sum over delimiter states, not a product. Bounding it by
the per-example factors and the c₁–c₄ ratios is [LIT-797](../literature.d/LIT-797.md)'s Appendix B,
which [NOTE-633](../notes.d/NOTE-633.md) did not follow. That step is the promote_when.
