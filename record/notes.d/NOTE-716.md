---
number: 716
status: Read
formerly:
- NOTE-tmpxnmvt
paper: LIT-1014
title: 'Symmetry Induces Structure and Constraint of Learning'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read from arXiv v2 (1 June 2024, ICML 2024) through the PDF text layer:
    §§1–5 in full, with figure captions. The proofs in Appendix C and the
    experimental details in Appendix B (including the ResNet18 and
    transformer experiments) were not checked.
date: '2026-10-13'
summary: >-
  ℓ_γ = ℓ₀(θ, x) + γ‖θ‖². O-mirror symmetry: ℓ₀(θ) = ℓ₀((I − 2OOᵀ)θ). Theorem
  1: (1) Oᵀθ = 0 implies Oᵀ∇ℓ_γ = 0; (2) at symmetric points the Hessian
  splits into ker(Oᵀ) and im(OOᵀ) blocks; (3) above some γ₀ the projection
  (I − OOᵀ)θ has lower loss; (4) above some γ₁ all minima satisfy Oᵀθ = 0.
  SGD near the symmetric set: Pθ_{t+1} = Pθ_t − λH(x)Pθ_t, attractive when
  the Lyapunov exponent E log|1 − λ(ξ + γ)| < 0. Corollaries: sparsity,
  low rank, homogeneous neurons (Theorems 2–4).
---
<!-- inactive-ok-file: THEORY-083 THEORY-211 THEORY-210 THEORY-213 QUESTION-080 QUESTION-058 — Proposed or Open; the accounts and questions this reading bears on, open -->

# NOTE-716: Symmetry Induces Structure and Constraint of Learning

## Contribution

One framework for the effect of the discrete symmetries common in
networks. Each symmetry implies a reflection. Each reflection makes a
linear subspace absorbing for gradient-based training, and that subspace
is favoured by weight decay and by gradient noise. Known structured
outcomes (sparsity, low rank, merged neurons) and some failure modes
(collapse, loss of plasticity) then appear as consequences of symmetry.

## Key insight

If the loss cannot tell a point from its mirror image, then on the mirror
the gradient has no component leaving it, for every data point. So the
mirror is a trap: training that reaches it stays. Its points are also
shorter than their off-mirror equivalents, so weight decay prefers them.
And when gradient noise is strong, the random kicks near the mirror
shrink the off-mirror component on average, so SGD falls into it even
where gradient descent would roll away.

## Assumptions

- **A per-sample loss with an exact mirror symmetry,** plus L2 weight
  decay γ.
- **Assumption 1:** the Hessian of ℓ₀ is bounded below (needed for
  part 4).
- **For the SGD result:** a second-order expansion near the symmetric set
  and a diagonal approximation of the sample Hessian. The paper calls the
  resulting critical learning rate "qualitatively correct", not exact.

## Key results

- **Theorem 1** as in the summary. Corollary 1: every mirror symmetry
  implies a linear stationary condition Oᵀθ = 0.
- **Hessian structure.** At symmetric points the Hessian is block
  diagonal along the mirror, for every sample. A two-layer tanh network
  near the origin has d 2×2 blocks, with eigenvectors (1, 1) and (1, −1).
- **SGD near the mirror (§2.4).** GD is attracted iff ξ* + γ > 0. SGD is
  attracted when the Lyapunov exponent is negative, roughly when
  λ > −2E[ξ + γ]/E[(ξ + γ)²]. That can hold at a strict saddle. Large
  learning rate, small batches or noisy data favour it.
- **L1 equivalence (§2.5).** Along a symmetry-breaking direction, weight
  decay on a mirror-symmetric loss is equivalent to an L1 penalty, which
  is why it gives exact sparsity at finite strength.
- **Rescaling gives sparsity (Theorem 2).** In linear regression
  reparametrized as v = u ⊙ w, SGD at large learning rates finds sparse
  solutions that plain regression never does (Fig. 3, left).
- **Rotation gives low rank (Theorem 3).** Matrix factorization with SGD
  prefers low rank at strong noise. A residual connection removes the
  symmetry and the effect (Fig. 3, middle).
- **Permutation gives homogeneity (Theorem 4).** Neurons tend to become
  identical copies. In a ResNet18 on CIFAR-10, penultimate-layer neurons
  form homogeneous correlation blocks with weight decay, and rarely
  without (Fig. 3, right).
- **Loss of plasticity (§3.4).** Symmetric solutions are absorbing, so
  later tasks cannot recover the capacity they remove. Removing the
  symmetry or injecting noise helps (Fig. 4).

## Claims

- That collapse phenomena, including neural collapse, posterior collapse
  and dimensional collapse, "are caused by symmetries in the loss
  function". Argued by mapping each to a symmetry. For neural collapse,
  the paper describes the phenomenon as the penultimate representation
  becoming low-rank, which is looser than Papyan et al.'s four conditions
  ([THEORY-083](../theory.d/THEORY-083.md)).
- That the result is "universal", relying only on the symmetry. True of
  Theorem 1. The SGD half rests on the approximations above.

## Concepts

- **Mirror symmetry:** invariance under I − 2OOᵀ. Continuous symmetries
  are one way to have one, but the constraints come from the reflections.
- **Stationary condition:** f(θ_t) = 0 implies f(θ_{t+1}) = 0 under
  (S)GD. It is an absorbing state of the training process.

## Connections

- **[THEORY-184](../theory.d/THEORY-184.md) (Yang, Poggio, Chuang & Ziyin)** proves coincident neurons
  stay coincident (the same stationary condition as Theorem 4, part 1),
  and that distinct ones cannot merge in finitely many steps below
  η = 1/K. It does not say they never merge in the limit. This paper
  says that with strong weight decay or noise the merged subspace is
  favoured and attractive, so merging happens asymptotically. The two fit.
- **[THEORY-211](../theory.d/THEORY-211.md) (law of balance)** is the continuous-symmetry counterpart,
  by the same author: noise drives a rescaling coordinate to a balanced
  value. This paper treats the reflections, where noise drives toward
  zero along the symmetry-breaking direction.
- **[THEORY-210](../theory.d/THEORY-210.md)** says the position along a symmetry orbit is set by
  initialization and optimizer. This paper adds the discrete case: which
  symmetric subspace training falls into is set by weight decay and noise
  level.
- **[THEORY-083](../theory.d/THEORY-083.md) and [QUESTION-080](../questions.d/QUESTION-080.md) (neural collapse).** A symmetry account of
  collapse in the last layers, with absorbing states that would keep the
  collapsed geometry fixed once reached.

## Bearing on the record

It is filed as [THEORY-213](../theory.d/THEORY-213.md), answering [QUESTION-058](../questions.d/QUESTION-058.md) in part on how much
learned structure comes from the update's symmetry. It completes
[THEORY-184](../theory.d/THEORY-184.md)'s asymptotic half and bears on [QUESTION-080](../questions.d/QUESTION-080.md).

## Limitations

- **The SGD half is approximate:** second-order expansion, diagonal
  Hessian, a "qualitatively correct" threshold.
- **Experiments.** Toy regressions and matrix factorization, plus one
  ResNet18 correlation analysis and a transformer experiment that were
  not checked here.
- **Neural collapse.** The account of neural collapse is a mapping, not a
  derivation of Papyan et al.'s conditions.

## Open questions

- Is the ResNet18 block structure neurons merging, or only correlating?
- Does the symmetry account of neural collapse predict NC1–NC4, or only
  low rank?

## Corrections

None.
