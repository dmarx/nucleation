---
number: 382
status: Active
formerly:
- CLAIM-tmpt2jwl
title: "In an autoencoder initialised with i.i.d. Gaussian weights and zero biases and trained by SGD or momentum SGD on a loss of its output, the law of each hidden layer's learned representation is invariant under every orthogonal map of that layer that commutes with its activation, so under a radial activation no basis is privileged in law, while elementwise tanh or Leaky-ReLU yields invariance only under the signed permutations or the permutations, which leaves the standard axes free to be privileged"
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-288 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-288.yaml, batch 013, ADR-047).
    THEORY-288's body gave this symmetry argument as the record's own, from
    the setup, and a result the record proves is a CLAIM (ADR-032). The
    proof is written out below, with the optimiser condition the argument
    needs. THEORY-288 keeps its empirical title, Proposed, and cites this
    claim for the symmetry in law.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: an orthogonal reparametrisation that
  commutes with the activation but does not leave the loss invariant, an
  SGD or momentum step that does not commute with it, or an i.i.d.
  Gaussian matrix whose law changes under multiplication by orthogonal
  matrices.
tags:
- representation-learning
- mathematics
date: '2026-10-19'
line:
- learned-structure
summary: >-
  [THEORY-288](../theory.d/THEORY-288.md)'s symmetry argument, stated as the record's own and proved.
  Transform the parameters by orthogonal maps Q_l of the hidden spaces
  that commute with the activation. The network then computes Q_l h_l and
  the same output, so the loss is invariant. Gradient steps commute with
  the transformation, and an i.i.d. Gaussian initialisation is invariant
  under it, so the law of the trained representations is too. For radial
  activations this is all of O(n), and no basis is privileged in law. For
  elementwise ones it is a finite group, so the axes may be privileged.
  Whether they are, and how strongly, is [THEORY-288](../theory.d/THEORY-288.md)'s empirical content.
  The argument needs an orthogonally equivariant optimiser, and fails for
  Adam.
---
<!-- inactive-ok-file: THEORY-288 — Proposed; the account this argument was split from and that cites it, cited as open -->

# CLAIM-382: In an autoencoder initialised with i.i.d. Gaussian weights and zero biases and trained by SGD or momentum SGD on a loss of its output, the law of each hidden layer's learned representation is invariant under every orthogonal map of that layer that commutes with its activation, so under a radial activation no basis is privileged in law, while elementwise tanh or Leaky-ReLU yields invariance only under the signed permutations or the permutations, which leaves the standard axes free to be privileged

## The claim

Take an autoencoder with:
- an affine encoder W_enc, b_0 into hidden space 0;
- hidden blocks, each an activation σ on space l − 1 followed by an affine
  map W_l, b_l into space l;
- a final activation and an affine decoder W_dec, b_dec.

Weights are initialised with i.i.d. Gaussian entries (Xavier-normal is one
case), biases at zero, and training is SGD or momentum SGD on a loss that
depends only on the output. For each hidden space l, let G_l be a group of
orthogonal maps Q with σ(Qh) = Qσ(h). Then, at every step of training and
for any sequence of minibatches, the joint law of the representations
{h_l(x)}, over the initialisation, is invariant under h ↦ Qh for Q ∈ G_l.

- For a radial activation, σ(h) = s(‖h‖)h/‖h‖, G_l is all of O(n). Every
  statistic of how the representations align with the standard basis has
  the same law as for any rotated basis.
- For elementwise tanh, G_l contains the signed permutations B_n. For
  elementwise Leaky-ReLU it contains the permutations S_n. Invariance is
  then only under a finite group, so the standard axes (B_n) or the ±1
  diagonal (S_n) are not excluded from being privileged.

## Proof

1. Choose Q_l ∈ G_l for each hidden space l, and act on the parameters by
   W_enc ↦ Q_0 W_enc, b_0 ↦ Q_0 b_0, W_l ↦ Q_l W_l Q_{l−1}ᵀ, b_l ↦ Q_l b_l,
   and W_dec ↦ W_dec Q_Lᵀ, with b_dec unchanged. Call this map T.
2. By induction over the layers, the transformed network has hidden state
   Q_l h_l wherever the original has h_l. This uses σ(Q_l h) = Q_l σ(h).
   The decoder then receives Q_L σ(h_L) and multiplies it by W_dec Q_Lᵀ, so
   the output is unchanged. So the loss satisfies ℓ(Tθ) = ℓ(θ) on every
   minibatch.
3. T is an orthogonal linear map of parameter space. Differentiating
   ℓ(Tθ) = ℓ(θ) gives Tᵀ∇ℓ(Tθ) = ∇ℓ(θ), so ∇ℓ(Tθ) = T∇ℓ(θ). An SGD step
   θ ↦ θ − η∇ℓ(θ) commutes with T, and so does a momentum step, which is
   linear in past gradients, given the same minibatch sequence.
4. A matrix W with i.i.d. N(0, s²) entries has the same law as QWQ′ᵀ for
   orthogonal Q and Q′. Zero biases are fixed by T. So the initialisation
   θ₀ and Tθ₀ have the same law.
5. By 3 and 4, θ_t and Tθ_t have the same law at every step t. By 2,
   h_l(x; Tθ_t) = Q_l h_l(x; θ_t) for every input x, which is the claim.

## What it does not say

- **That radial networks stay spread.** A law invariant under O(n) is
  consistent with every run concentrating in some random direction. That
  the radial networks of [LIT-976](../literature.d/LIT-976.md) do not, and that the elementwise ones form
  strong, narrow beams on the group's directions, is [THEORY-288](../theory.d/THEORY-288.md)'s empirical
  content, Proposed.
- **That elementwise activations privilege the axes.** The symmetry permits
  it and does not force it.
- **Anything for Adam or other coordinate-wise optimisers.** Their updates
  commute with signed permutations, not with general rotations, so step 3
  fails. With Adam even a radial network's law is invariant only under B_n.
- **Anything for nonzero or non-Gaussian initial biases, or for weight
  initialisations that are not orthogonally invariant.**
