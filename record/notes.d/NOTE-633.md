---
number: 633
status: Read
formerly:
- NOTE-tmpoc0i1
paper: LIT-797
title: 'Implicit Bayesian inference account of in-context learning'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the arXiv v6 PDF (21 Jul 2022, 31 pp.). Sections 1–6 read
    in full, with the heuristic derivation of §3.2 followed step by step;
    Appendix A (prompt distribution), F.1 (GINC construction) and F.5 (the
    GPT-3 LAMBADA experiment) read. The proofs in Appendices B–E
    (propositions for Theorem 1, convergence of the predictor, proofs of
    Theorems 2 and 3) were not followed, and the other experimental
    appendices were only looked over.
date: '2026-10-09'
summary: >-
  Proves that if pretraining text is a mixture of HMMs and a model fits it
  exactly, conditioning on a prompt of concatenated examples recovers the
  prompt's latent concept by posterior concentration, and the in-context
  predictor is asymptotically Bayes-optimal, whenever each example's KL
  signal about the concept beats the error from the improbable transitions
  between examples. The account is of the data distribution, not of any
  network's computation.
---

# NOTE-633: Implicit Bayesian inference account of in-context learning

## Contribution

A setting in which in-context learning provably happens without any
learning at test time: pretraining data with document-level latent
structure, and a model that matches the pretraining distribution. In it,
the paper shows that the prompt identifies its latent concept despite being
out of distribution as a whole, and gives conditions (distinguishability)
under which the in-context predictor is asymptotically optimal and a rate
(about 1/k in example length) when they fail. It adds a synthetic dataset,
GINC, on which trained Transformers and LSTMs do exhibit in-context
learning, and on which several phenomena seen in large models recur.

## Key insight

If the model is a Bayesian mixture, a prompt does not teach it anything; it
moves the posterior over which mixture component is generating the text.
p(y | prompt) = ∫ p(y | θ, prompt) p(θ | prompt) dθ, and if
p(θ | prompt) concentrates on θ*, the model "selects" the task by
marginalisation. The mismatch between prompts and documents costs a bounded
amount per example, while the evidence for θ* grows with every token of
every example, so evidence wins as the prompt grows.

## Assumptions

- Pretraining distribution: p(o₁…o_T) = ∫ p(o₁…o_T | θ) p(θ) dθ, with
  p(· | θ) an HMM whose hidden-state transition matrix is set by θ.
- The LM fits p exactly ("with enough data and expressivity"); the
  analysis is of p, not of a network.
- Prompt: n independent examples O_i = [x_i, y_i] of fixed length k, each
  started from a prompt start distribution and then generated under θ*,
  separated by a delimiter token.
- **Assumption 1**: a set D of delimiter hidden states emits the delimiter
  with probability 1, and no other state emits it.
- **Assumption 2**: transitions into delimiter states are bounded above by
  c₂ under θ ≠ θ* and below by c₁ > 0 under θ*; start probabilities of
  delimiter states lie in [c₃, c₄].
- **Assumption 3**: the prompt start distribution is within TV distance Δ/4
  of every θ*-transition from a delimiter state, Δ the margin between the
  most and second most likely label.
- **Assumption 4**: well-specification, θ* ∈ Θ.
- **Assumption 5**: regularity — all θ*-transitions ≥ c₅ > 0, all start
  states ≥ c₈, every token emittable, prior with full support and bounded.
- Theorem 2 adds a second-order Taylor expansion of each token's KL around
  θ* (Fisher information I_{j,θ*}); Theorems 2–3 assume the minimisers of
  0-1 and multiclass logistic risk coincide.

## Key results

- **Theorem 1.** Under Assumptions 1–5 and Condition 1,
  Σ_{j=1}^{k} KL_j(θ* ‖ θ) > ε_start + ε_delim for all θ ≠ θ*, with
  ε_delim = 2(log c₂ − log c₁) + log c₄ − log c₃ and ε_start = log(1/c₈):
  as n → ∞, argmax_y p(y | S_n, x_test) → argmax_y p_prompt(y | x_test),
  so lim L₀₋₁(f_n) = inf_f L₀₋₁(f). *Holds when:* the prompt concept is
  distinguishable, e.g. Θ discrete.
- **Theorem 2.** If B is the set of θ violating Condition 1 and the KL has
  a Taylor expansion with condition number γ_θ* = max_j λ_max(I_j) /
  min_j λ_min(I_j), then for k ≥ 2,
  lim L₀₋₁(f_n) ≤ inf_f L₀₋₁(f) + g⁻¹(O(γ_θ* sup_B(ε_start + ε_delim) /
  (k − 1))), g the calibration function of the multiclass logistic loss.
  Roughly O(1/k) for small error.
- **Theorem 3.** The same bound without the condition number and without
  continuity, when the test input's length is uniform on 2…k.
- **GINC** (uniform mixture of 5 concepts, ~10M tokens, vocabularies of
  50/100/150): accuracy grows with n and k for Transformers and LSTMs;
  ablating the mixture (one concept) or the structure (random transitions)
  removes in-context learning; unseen concepts fail; 12- and 16-layer
  Transformers with the same validation loss (1.33) reach 81.2% and 84.7%;
  LSTMs reach 95.8% at vocabulary 50; permutations of a fixed set of four
  examples differ by 10–40 points; at transition temperature 0.01 few-shot
  is first worse than zero-shot.
- **GPT-3 on LAMBADA (Appendix F.5).** Five longer examples (500–600
  characters) beat five short ones (70.7% vs 69.8%) on short test items;
  duplicating the short examples does not help (69.6%); ten independent
  short ones give 71.4%.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under the mixture-of-HMMs model and exact fit, posterior concentration on the prompt concept makes the in-context predictor asymptotically optimal despite prompt–pretraining mismatch | strong (proof, under stated assumptions) | Theorem 1; proof in Appendices B–C, not followed here |
| C2 | Without distinguishability, excess risk falls roughly as 1/k in example length | moderate | Theorems 2–3; proofs not followed |
| C3 | Information in example inputs, not only correct input-output pairs, contributes to in-context learning | moderate | Condition 1's per-token KL sum; GINC k-curves; the small LAMBADA gain |
| C4 | Latent-concept structure in pretraining is necessary for in-context learning in GINC | moderate | Figure 4 ablations, one synthetic family |
| C5 | Model size improves in-context accuracy beyond pretraining loss | weak | GINC, Table in Figure 6, three sizes |
| C6 | This is how in-context learning works in large LMs | not supported | the paper offers it as "a first step" and tests it at small scale |

## Concepts

- **concept θ**: the latent variable of the pretraining mixture; here the
  HMM's hidden-state transition matrix (in GINC, the property transition
  matrix).
- **prompt concept θ\***: the concept from which every prompt example is
  generated.
- **in-context predictor f_n**: argmax_y p(y | S_n, x_test) under the
  pretraining distribution.
- **distinguishability**: Condition 1, KL signal per example exceeding the
  per-example mismatch error.
- **GINC**: Generative IN-Context learning dataset; a factorial HMM of
  entities and properties emitting tokens through a fixed memory matrix.

## Connections

The analysis is a Bernstein–von Mises-style posterior concentration result
for dependent, misspecified observations (the paper cites Gunst and
Shcherbakova 2008 and Kleijn and van der Vaart 2012). The latent-document
structure is the topic model's (LDA), with the difference that no explicit
inference algorithm is run. Contrasted with meta-learning, where a model is
trained to learn from examples; here the ability is a by-product of
modelling the data. Min et al. ([LIT-814](../literature.d/LIT-814.md)) cite it as the theoretical
account their measurements bear on, and von Oswald et al. ([LIT-792](../literature.d/LIT-792.md))
offer the rival, mechanistic account.

## Bearing on the record

- No THEORY in the record holds a Bayesian account of conditioning in
  language models. I do not file one: the result is conditional on exact
  fit to a specific generative model, and the record would be stating the
  model's consequence, not a fact about LMs.
- What it supplies is a precise sense in which a context can act as a
  parameter of the prediction: the prompt sets p(θ | prompt), and the
  output is the predictive under that posterior. The model of the
  interpreter is fixed; only the evidence changes.
- Its order-sensitivity and zero-shot-beats-few-shot results arise inside
  the model from distribution mismatch, so they are not evidence against a
  Bayesian reading. Lu et al. ([LIT-833](../literature.d/LIT-833.md)) measure the same order effect
  in GPT-2 and GPT-3.
- No instruction for machine-learning practice is drawn here. The work's
  subject is held by an anthology topic (`anthology-candidate`).

## Limitations

- Exact fit to the pretraining distribution is assumed; the gap between
  this and a trained network is not studied.
- Results are asymptotic in n, with constants (c₁…c₈) that are not
  estimated for any real model.
- Fixed example length; a single output token per example; well-specified
  prompt concept (θ* ∈ Θ). The authors leave misspecification and
  extrapolation to unseen concepts open, and GINC shows the latter fails.
- GINC was built to satisfy the assumptions, so its confirmations are
  checks of consistency, not tests against an independent world.
- The GPT-3 experiment is a single comparison, with a gain under one
  point and no reported interval.

## Open questions

- Does the account survive misspecification (θ* ∉ Θ), as the authors
  propose via Kleijn and van der Vaart?
- Can a trained network be shown to compute the posterior predictive, or
  only to approximate its outputs? The paper is silent on mechanism.
- How does the latent-concept posterior relate to the mechanism claims of
  [LIT-792](../literature.d/LIT-792.md), where the same prompt structure is processed as a gradient
  step on an implicit regression?
