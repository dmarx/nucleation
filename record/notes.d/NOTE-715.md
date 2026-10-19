---
number: 715
status: Read
formerly:
- NOTE-tmpl050c
paper: LIT-943
title: 'From Lazy to Rich: Exact Learning Dynamics in Deep Linear Networks'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read from arXiv v2 (4 March 2025, ICLR 2025) through the PDF text
    layer: §§1–7 in full, and the statement of Appendix A.3. The proofs in
    Appendices B and C, the application appendices (D) and the
    implementation details were not checked. Figures were read from their
    captions.
date: '2026-10-13'
summary: >-
  Two-layer linear network ŷ = W₂W₁x, MSE, full-batch gradient flow.
  Assumptions: whitened inputs (A1), λ-balanced start W₂ᵀW₂ − W₁W₁ᵀ = λI
  (A2), no bottleneck (A3). Then QQᵀ, with Q = [W₁ᵀ; W₂], obeys a matrix
  Riccati equation (Lemma 4.1), solved exactly (Theorem 4.3). For aligned
  starts, each singular value moves by a λ-dependent transition function:
  sigmoidal as λ → 0, exponential 1 − e^{−|λ|t/τ} as |λ| → ∞ (Theorem 5.1).
---
<!-- inactive-ok-file: THEORY-186 THEORY-212 QUESTION-081 — Proposed or Open; readings, the account filed from this one and the question it raises, open -->

# NOTE-715: From Lazy to Rich: Exact Learning Dynamics in Deep Linear Networks

## Contribution

Exact solutions for the whole learning trajectory of a two-layer linear
network for any λ-balanced start, not only the zero-balanced one earlier
solutions needed. That covers the continuum from rich to lazy learning in
one solvable model. It includes the network function, both layers'
representational similarity and the finite-width NTK, and their
dependence on architecture.

## Key insight

With the absolute scale held fixed, how the weight is split between the
two layers decides how the network learns. If the layers are balanced,
both adapt together, and learning proceeds in stages through saddles,
building task-specific representations in both layers. If one layer is
much larger, it behaves like a fixed identity-like projection. The small
layer adapts quickly and exponentially, and the NTK barely moves.
Gradient flow conserves the split, so the initialization fixes the
regime.

## Assumptions

- **A1:** whitened inputs, Σ̃xx = I.
- **A2:** λ-balanced start, W₂ᵀW₂(0) − W₁W₁ᵀ(0) = λI. It persists
  throughout training under gradient flow.
- **A3:** hidden width N_h = min(N_i, N_o).
- **Full-batch gradient flow.** Learning rate enters only as the time
  constant τ = 1/η. No minibatch noise is modelled.

## Key results

- **Riccati solution (Theorem 4.3).** QQᵀ(t) = [Z₁A⁻¹Z₁ᵀ, Z₁A⁻¹Z₂ᵀ;
  Z₂A⁻¹Z₁ᵀ, Z₂A⁻¹Z₂ᵀ], built from the SVD of Σ̃yx and the initialization.
  Convergence to the global minimum is guaranteed when the initialization
  matrix B is non-singular.
- **Singular-value dynamics (Theorem 5.1).** For aligned starts,
  s_α(t) = s_α(0) + γ_α(t; λ)(s̃_α − s_α(0)). It is sigmoidal as λ → 0
  (rich) and exponential as |λ| → ∞ (lazy).
- **Parameters up to rotation (Theorem 5.2).** W₂ = U S₂ Rᵀ and
  W₁ = R S₁ Vᵀ, with S₁,₂ = ((S_λ ∓ λI/2))^{1/2} and
  S_λ = (S² + λ²/4 I)^{1/2}.
- **Representations at convergence (Theorem C.4).** λ = 0 gives
  task-specific representations in both layers, whatever the absolute
  scale. As λ → ±∞, one layer's similarity matrix tends to the identity
  while the other's is ∝ 1/|λ| but still structured. The paper calls this
  the "semi-structured lazy regime". The NTK becomes static
  (Theorem C.5).
- **Robustness.** Loss under input noise is independent of λ. Loss under
  parameter noise is smallest at λ = 0 (for equal input and output
  dimensions).
- **Architecture.** Funnel networks are lazy as λ → +∞, inverted funnels
  as λ → −∞. In the opposite limits there is a lazy phase and then a
  delayed rich phase (Theorem C.6).
- **Random initialization (App. A.3).** Common Gaussian initializations
  are λ-balanced in expectation, and in probability as width grows. This
  was stated but not checked here.
- **Applications (§6).**
  - Catastrophic forgetting occurs for every λ.
  - Reversal learning succeeds for λ ≠ 0, because it avoids the saddle.
  - Transfer improves with larger λ in the paper's semantic task.
  - Fine-tuning improves when the network is rebalanced to larger λ.

## Claims

- That relative scale, not only absolute scale, is "pivotal" in the
  transition between rich and lazy learning. Shown exactly within the
  model.
- That the semi-structured lazy regime "promotes transfer learning".
  Shown on one hierarchical semantic task.

## Concepts

- **λ-balanced:** W₂ᵀW₂ − W₁W₁ᵀ = λI. It is the matrix form of the
  rescale conservation law of Neural Mechanics ([LIT-1012](../literature.d/LIT-1012.md)).
- **Rich and lazy:** whether the NTK, and so the representation, changes
  during training.

## Connections

- **[THEORY-186](../theory.d/THEORY-186.md) and [THEORY-187](../theory.d/THEORY-187.md) (Saxe et al.)** are the λ = 0, aligned case
  of this solution.
- **[LIT-1012](../literature.d/LIT-1012.md) (Neural Mechanics)** derives the conservation of λ under
  gradient flow that Assumption A2 relies on.
- **[THEORY-211](../theory.d/THEORY-211.md) (law of balance)** says that under SGD the same quantity is
  not conserved. It is driven toward the point where the layers' gradient
  noise balances, at a rate set by η/S. The paper does not mention SGD or
  minibatch noise. [QUESTION-081](../questions.d/QUESTION-081.md) asks what that does to the regimes.

## Bearing on the record

It gives [QUESTION-039](../questions.d/QUESTION-039.md) a named determinant of how structure is acquired:
the relative scale of the layers, which decides between stage-like and
exponential learning. It is filed as [THEORY-212](../theory.d/THEORY-212.md). Its dependence on a
conserved quantity is what [QUESTION-081](../questions.d/QUESTION-081.md) puts in doubt under SGD.

## Limitations

- **Two layers, linear, whitened inputs, no bottleneck.** The paper
  defers deep networks and nonlinearities to Kunin et al. (2024), which
  is not held.
- **Gradient flow only.** The conservation that makes λ a fixed control
  parameter does not hold under SGD.
- **The applications** rest on small constructed tasks.

## Open questions

- Does the regime set by λ survive SGD? ([QUESTION-081](../questions.d/QUESTION-081.md))

## Corrections

The Deferred entry said the paper is about how "initialization scale"
moves networks between lazy and rich learning. Its contribution is the
relative scale, with the absolute scale held fixed.
