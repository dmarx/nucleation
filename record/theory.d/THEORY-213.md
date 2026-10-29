---
number: 213
status: Active
formerly:
- THEORY-tmppei8o
title: 'Every mirror symmetry of a network''s per-sample loss makes its symmetric subspace invariant under gradient descent and SGD, and when the loss''s Hessian is bounded below by −c, weight decay γ‖θ‖² with γ > c/2 puts every minimum in that subspace; rescaling symmetries that hold at λ = −1, rotation symmetries and permutation symmetries contain such mirrors, whose subspaces are zeroed weights, reduced rank and identical neurons'
version: 3
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-213 (batch 049, ADR-047 v2). The dated note below re-derives
    Theorem 1's invariance and weight-decay parts and the three corollaries.
    Dropped: the SGD-noise clause, which rests on a diagonal approximation,
    and "rescaling symmetry" without the λ = −1 condition, since ReLU's
    positive rescaling contains no mirror. The promote_when moves to
    QUESTION-206.
- version: 3
  date: '2026-10-20'
  note: >-
    The wider claim this account dropped when it was narrowed, that strong
    SGD noise makes a mirror's subspace attracting even at a saddle,
    giving sparsity, low rank and identical neurons in SGD-trained
    networks, as the paper argues, is filed as the Proposed
    THEORY-781, which extends this one (ADR-047 v4, narrowing-loss sweep,
    batch 068). Status and title are unchanged.
tags:
- learning-theory
- loss-landscapes
- anthology-candidate
date: '2026-10-13'
source:
- LIT-1014
summary: >-
  Ziyin (2024), [LIT-1014](../literature.d/LIT-1014.md), read in [NOTE-716](../notes.d/NOTE-716.md). If a per-sample loss
  is invariant under the reflection I − 2OOᵀ, then Oᵀθ = 0 is a stationary
  condition for GD and SGD. The Hessian is block diagonal there. Above a
  critical weight decay all minima satisfy the constraint. Under SGD with
  strong noise the subspace is attractive even at a strict saddle, by a
  Lyapunov-exponent argument. Rescaling, rotation and permutation
  symmetries imply mirrors, so they yield sparsity, low rank and merged
  neurons, with collapse and loss of plasticity as consequences. The SGD
  half is approximate and the network evidence is limited; the title holds
  only the exact half.
  Promoted on 2026-10-20 on the exact half, re-derived. The SGD half is
  QUESTION-206.
extended_by:
- THEORY-781
bears_on:
- QUESTION-058
---
<!-- inactive-ok-file: THEORY-781 — Proposed; the wider claim this account dropped, filed separately and cited as open -->

# THEORY-213: Every mirror symmetry of a network's per-sample loss makes its symmetric subspace invariant under gradient descent and SGD, and when the loss's Hessian is bounded below by −c, weight decay γ‖θ‖² with γ > c/2 puts every minimum in that subspace; rescaling symmetries that hold at λ = −1, rotation symmetries and permutation symmetries contain such mirrors, whose subspaces are zeroed weights, reduced rank and identical neurons

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

## Note of 2026-10-20: the exact half, re-derived

Re-derived for the promotion audit (batch 049, [ADR-047](../decisions.d/ADR-047.md) v2). Appendix C's
proofs were not checked, so this stands on its own.

**Setting.** O has orthonormal columns, R = I − 2OOᵀ (symmetric and
orthogonal), and every per-sample loss satisfies ℓ₀(θ) = ℓ₀(Rθ).

**Invariance.** Differentiating gives ∇ℓ₀(θ) = R∇ℓ₀(Rθ). Where Oᵀθ = 0,
Rθ = θ, so the gradient g satisfies g = Rg, and Oᵀg = Oᵀg − 2Oᵀg, hence
Oᵀg = 0. The weight-decay gradient 2γθ has no O-component there either.
Every per-sample step, and so every GD or SGD step, keeps Oᵀθ = 0.

**Weight decay.** Write θ = θ⊥ + Oz with z = Oᵀθ and f(z) = ℓ₀(θ⊥ + Oz).
R(θ⊥ + Oz) = θ⊥ − Oz, so f is even and its gradient at 0 vanishes. If the
Hessian of ℓ₀ is bounded below by −cI (the paper's Assumption 1), then
f(z) − f(0) ≥ −(c/2)‖z‖² along the segment from 0. With
L = ℓ₀ + γ‖θ‖² and ‖θ‖² = ‖θ⊥‖² + ‖z‖²,
L(θ) − L(θ⊥) ≥ (γ − c/2)‖z‖². So for γ > c/2 every minimum has z = 0.

**Which symmetries contain a mirror.** A rescaling symmetry
ℓ₀(u, w) = ℓ₀(λu, w/λ) that holds at λ = −1 contains (u, w) ↦ (−u, −w),
whose subspace is u = w = 0. For a ReLU network the rescaling holds only
for λ > 0, which gives no mirror. A rotation symmetry contains every
reflection I − 2ooᵀ, whose subspace oᵀW = 0 lowers the rank. Swapping two
neurons is a reflection across θ_a − θ_b, whose subspace is θ_a = θ_b.

## Note of 2026-10-20: the wider claim, filed separately

When this account was narrowed, its wider form went nowhere a later result
could confirm or reject it. Under [ADR-047](../decisions.d/ADR-047.md) v4 it is now the Proposed
[THEORY-781](THEORY-781.md): that strong SGD noise makes a mirror's subspace
attracting even at a saddle, giving sparsity, low rank and identical
neurons in SGD-trained networks, as the paper argues. This account is that
one's evidence, and nothing here changes.
