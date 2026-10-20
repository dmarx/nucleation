---
number: 213
status: Proposed
formerly:
- THEORY-tmppei8o
promote_when: >-
  The SGD half shown beyond the second-order, diagonal-Hessian argument,
  or measured in a trained network. What would promote: a network with a
  known permutation, rotation or rescaling symmetry, trained with SGD
  across learning rates, batch sizes and weight decays, with a measured
  distance to the symmetric subspace (neuron coincidence, rank,
  sparsity) that falls to zero beyond a threshold predicted from the
  noise and curvature. The same should not happen when the symmetry is
  removed by reparametrization. What would refute it: training that
  reaches the symmetric subspace and leaves it, which part 1 of the
  theorem forbids; or no dependence of the outcome on weight decay and
  noise where the threshold predicts one. More toy factorizations cannot
  settle it.
title: 'Every mirror symmetry of a network''s loss makes its symmetric subspace absorbing for gradient-based training, and weight decay above a threshold or strong gradient noise makes that subspace favoured, so rescaling symmetry yields sparsity, rotation symmetry low rank, and permutation symmetry merged, identical neurons'
version: 1
tags:
- learning-theory
- loss-landscapes
- anthology-candidate
date: '2026-10-13'
source:
- LIT-1014
answers:
- QUESTION-058
summary: >-
  Ziyin (2024), [LIT-1014](../literature.d/LIT-1014.md), read in [NOTE-716](../notes.d/NOTE-716.md). If a per-sample loss
  is invariant under the reflection I − 2OOᵀ, then Oᵀθ = 0 is a stationary
  condition for GD and SGD. The Hessian is block diagonal there. Above a
  critical weight decay all minima satisfy the constraint. Under SGD with
  strong noise the subspace is attractive even at a strict saddle, by a
  Lyapunov-exponent argument. Rescaling, rotation and permutation
  symmetries imply mirrors, so they yield sparsity, low rank and merged
  neurons, with collapse and loss of plasticity as consequences. Proposed:
  the SGD half is approximate and the network evidence is limited.
---
<!-- inactive-ok-file: THEORY-210 QUESTION-080 — Proposed or Open; the accounts and question this one bears on, open -->

# THEORY-213: Every mirror symmetry of a network's loss makes its symmetric subspace absorbing for gradient-based training, and weight decay above a threshold or strong gradient noise makes that subspace favoured, so rescaling symmetry yields sparsity, rotation symmetry low rank, and permutation symmetry merged, identical neurons

## Source

Ziyin (2024), [LIT-1014](../literature.d/LIT-1014.md), read in [NOTE-716](../notes.d/NOTE-716.md): §§1–5, with Appendix C's
proofs unchecked.

## The claim

**Absorbing.** If a per-sample loss satisfies ℓ₀(θ) = ℓ₀((I − 2OOᵀ)θ), then
on the subspace Oᵀθ = 0 the gradient has no component leaving it, for
every data point and any weight decay (Theorem 1, part 1). The subspace is
a stationary condition of GD and SGD: once reached, it is kept.

**Favoured.** Two forces push training into it.

- **Weight decay.** The projection onto the subspace has lower
  regularized loss above some γ₀, and above γ₁ every minimum lies in it
  (parts 3–4). Along the symmetry-breaking direction, weight decay acts
  like an L1 penalty, which is why it gives exact zeros at finite strength.
- **Gradient noise.** Near the subspace, SGD's off-mirror component
  evolves as a random matrix product. It collapses when the Lyapunov
  exponent is negative, which happens at large learning rate, small batch
  or noisy data, even where the subspace is a saddle that GD escapes
  (§2.4; the threshold is derived under a diagonal approximation).

**Structure as a consequence.** Rescaling symmetry implies a mirror whose
subspace is u = w = 0, giving sparsity. Rotation symmetry gives low rank.
Permutation symmetry gives identical neurons. Each structure disappears
when the symmetry is removed by reparametrization (Fig. 3).

## What it bears on

- **[QUESTION-058](../questions.d/QUESTION-058.md)** asks how much of a network's learned structure comes
  from the symmetry of the update. On this account, sparsity, low rank and
  neuron homogeneity are produced by the loss's symmetries together with
  weight decay and noise, not by the data.
- **[THEORY-184](THEORY-184.md)** proves that coincident neurons stay coincident, and that
  distinct ones cannot merge in finitely many small steps. It leaves open
  whether they merge in the limit. This account says that, with strong
  weight decay or noise, the merged subspace is attractive, so they do
  merge asymptotically.
- **[THEORY-211](THEORY-211.md)** is the continuous counterpart. Noise drives a rescaling
  coordinate to a balanced value, where here it drives the
  symmetry-breaking component to zero.
- **[THEORY-083](THEORY-083.md) and [QUESTION-080](../questions.d/QUESTION-080.md).** The paper attributes neural collapse to
  symmetry, and absorbing states would keep a collapsed geometry fixed
  while other parameters move. But it describes neural collapse only as a
  low-rank penultimate representation, not by Papyan et al.'s four
  conditions.

## What this does not say

- It does not say every structure in trained networks comes from
  symmetry.
- It does not give an exact SGD threshold. The Lyapunov argument is
  approximate.
- It does not derive neural collapse as Papyan et al. define it.
- It does not instruct. The paper's algorithm for enforcing constraints
  (DCS) is practice, and belongs to the anthology.
