---
number: 480
status: Read
formerly:
- NOTE-tmpmuzzu
paper: 'LIT-621'
title: 'Shampoo: Preconditioned Stochastic Tensor Optimization'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (21 pages, text layer). Sections 1–6 and Appendix A
    (diagonal Shampoo, Theorem 13) read, with the proofs of Lemmas 8–9 and
    Theorem 7 followed. Appendix B (proofs of Lemmas 11–12 for tensors) and
    Appendix C (proofs of Lemmas 2 and 4) skimmed. Figures 2–4 are read
    from their captions; the extracted text does not carry the curves.
date: '2026-10-03'
summary: >-
  Matrix case: L = εI + Σ GGᵀ, R = εI + Σ GᵀG, W ← W − ηL^{-1/4}GR^{-1/4}.
  Lemma 8: εI + (1/r)Σ ggᵀ ⪯ L^{1/2} ⊗ R^{1/2} for rank-r gradients, so the
  Kronecker preconditioner dominates full AdaGrad. Regret
  √(2r) D Tr(L^{1/4}) Tr(R^{1/4}) = O(√T) (Theorem 7); order-k tensors use
  power −1/2k per dimension (Theorem 10). Steps per second within a few
  percent of SGD/Adam/AdaGrad (Table 1); on LM1B 3.509 against 4.87–4.92.
---

# NOTE-480: Shampoo: Preconditioned Stochastic Tensor Optimization

## Contribution

A full-matrix-style adaptive preconditioner that respects the tensor shape of
parameters: one moderately sized preconditioner per dimension instead of one
enormous one for the flattened tensor, with a regret guarantee in online
convex optimization and an implementation that drops into TensorFlow without
knowing the model.

## Key insight

Full-matrix AdaGrad preconditions by (Σ ggᵀ)^{-1/2}, which is impossible to
store for a weight matrix. For a gradient matrix of rank at most r, that full
matrix is dominated, up to the factor r, by the Kronecker product of the
square roots of its row and column second moments. Using the Kronecker
product of fourth roots on each side therefore preconditions at least as
strongly in every direction as full AdaGrad would, at the cost of two small
matrices.

## Assumptions

- **Online convex optimization**: convex losses fₜ chosen possibly
  adversarially; stochastic convex optimization follows by online-to-batch
  conversion (Section 2.1).
- **Bounded rank** of each gradient's matricizations, rank(matᵢ(Gₜ)) ≤ rᵢ,
  with r = (Π rᵢ)^{1/k} (Theorem 10).
- **D = maxₜ ‖Wₜ − W*‖_F** appears in the bound and is not controlled
  without a projection step that the implementation omits (Section 3).
- **Lipschitz losses** in the spectral norm, ‖Gₜ‖₂ ≤ 1, for the O(√T)
  instantiation.
- **Implementation**: each tensor separately, so no cross-tensor
  correlations; diagonal factors for dimensions above about 1200.

## Key results

- **Algorithm 1** (matrix) and **Algorithm 2** (tensor, step
  G̃ ← G̃ ×ᵢ (Hⁱₜ)^{-1/2k}).
- **Lemma 9.** For G of rank ≤ r, (1/r)ggᵀ ⪯ Iₘ ⊗ (GᵀG) and
  (1/r)ggᵀ ⪯ (GGᵀ) ⊗ Iₙ.
- **Lemma 8.** εIₘₙ + (1/r)Σ gₜgₜᵀ ⪯ (εIₘ + Σ GₜGₜᵀ)^{1/2} ⊗ (εIₙ + Σ GₜᵀGₜ)^{1/2},
  by the operator-monotone geometric mean of commuting PSD matrices
  (Lemma 5, Ando et al.).
- **Theorem 7.** Regret ≤ √(2r) D Tr(L_T^{1/4}) Tr(R_T^{1/4}); with
  ‖Gₜ‖₂ ≤ 1 and ε = 0 the traces are at most mT^{1/4} and nT^{1/4}, so
  regret is O(√T).
- **Theorem 10.** Tensor version: regret ≤ √(2r) D Πᵢ Tr((Hⁱ_T)^{1/2k}),
  again O(√T).
- **Theorem 13.** The diagonal variant has an analogous bound with D∞.
- **Table 1.** Steps per second at batch 128 on a Tesla K40: ResNet-32
  CIFAR-10 2.151 vs 2.184 (SGD); Inception CIFAR-10 3.506 vs 3.638;
  ResNet-55 CIFAR-100 1.249 vs 1.210 (Shampoo faster); LM1B Attention
  3.509 vs 4.919.
- **Figures 2–4.** Lower training loss than Adagrad, Adam and momentum on
  ResNet-32 and Inception (CIFAR-10) and ResNet-55 without batch norm
  (CIFAR-100), and lower test log-perplexity on LM1B with an attention
  model, Shampoo at its default η = 1.0.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The Kronecker product of row and column gradient statistics dominates the full AdaGrad preconditioner up to the gradient rank | strong (proof) | Lemmas 8–9 |
| C2 | Shampoo has O(√T) regret for convex Lipschitz losses | strong (proof), with D uncontrolled absent projection | Theorems 7, 10 |
| C3 | Shampoo trains deep networks faster than SGD, Adam and AdaGrad | weak to moderate: four curves, no repeated seeds reported; 10 learning rates swept per method on CIFAR, while on LM1B Shampoo ran at its default and only the baselines were swept | Figures 2–4 |
| C4 | Its per-step runtime is comparable to first-order methods | moderate: one GPU, with roots recomputed every 20–100 steps | Table 1, Section 6 |

## Method

Accumulate, per tensor dimension, the gradient contracted with itself over
the other dimensions; every 20–100 steps take each accumulator to the power
−1/2k by SVD; precondition the momentum-averaged gradient along each
dimension in turn; take a step.

## Concepts

- **matricization matᵢ(A)**: the nᵢ × n₋ᵢ matrix whose rows are the
  vectorized slices along dimension i.
- **contraction A⁽ⁱ⁾**: matᵢ(A)matᵢ(A)ᵀ, the dimension-i second moment.
- **regret**: cumulative loss minus that of the best fixed parameter in
  hindsight.

## Connections

- **AdaGrad (Duchi, Hazan & Singer 2011)** is the direct ancestor;
  Shampoo approximates its full-matrix form.
- **K-FAC ([LIT-622](../literature.d/LIT-622.md))** is discussed in Section 1.2 as the other
  factored preconditioner and contrasted, not compared experimentally.
- **Gupta, Koren & Singer (2017)**, the authors' unified adaptive
  regularization framework, supplies Lemma 2.

## Bearing on the record

- It shows that Kronecker structure is a computational convenience that can
  be justified without any statistical model of the network: Lemma 8 is pure
  matrix analysis. That sharpens the owner's question. When Papyan finds
  class-indexed structure in the Fisher, it is structure in a model-defined
  matrix; Shampoo's matrices are a different object.
- Carries an instruction for practice; `anthology-candidate`.

## Limitations

- No non-convex theory, and the deep-learning evidence is training loss and
  one test perplexity curve, without repeated seeds or error bars.
- The bound's D can grow with T without the omitted projection.
- Block-diagonal over tensors by construction; cross-layer curvature is
  ignored.
- The −1/4 exponent comes from the analysis; the paper offers it as giving
  an O(1/√t) step-size decay, not as optimal for training.

## Open questions

- How much of Shampoo's empirical gain is the Kronecker structure and how
  much the exponent and momentum? The anthology's SOAP reading
  ([ANTH-LIT-157](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-157.md)) is one later answer.
- What does the spectrum of L ⊗ R look like next to the Fisher of the same
  network?

## Corrections

- none (there was no seed)
