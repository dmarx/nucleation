---
number: 818
status: Proposed
formerly:
- CLAIM-tmpet76z
title: 'Shared-kernel coupling does not make flow active'
statement: >-
  Under gradient flow, embeddings coupled through a shared-parameter kernel
  relax: the loss falls at the rate of a positive-semidefinite quadratic
  form in the embedding gradients however the kernel changes during
  training, so neither the coupling nor its co-evolution with the
  representation makes the dynamics active, and nonequilibrium behaviour has
  to come from the optimizer, from noise not matched to the kernel, or from
  a changing objective
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: a network trained by deterministic
  gradient flow on a loss that depends on its parameters only through the
  embeddings, with a fixed objective, along which the loss rises over some
  interval. Not met by momentum, adaptive or stochastic optimizers, weight
  decay outside the embedding loss, or a changing objective, which the
  claim names as the sources it leaves open.
tags:
- representation-learning
- learning-theory
- thermodynamics
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
bears_on:
- QUESTION-515
complements:
- CLAIM-798
grounds:
- THEORY-209
- THEORY-779
summary: >-
  Fills a gap the filing found in A29 of the exchange "Rich Get Richer
  Power Laws" (answering U18): A29 treats data embeddings as particles
  coupled by a kernel that co-evolves with them, but gives no mechanism by
  which that system is active. Under gradient flow the loss is a Lyapunov
  function for any shared-parameter coupling, evolving or not, so the
  activity has to come from elsewhere. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-798 THEORY-209 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Proposed entries the record already held, cited for context -->
<!-- inactive-ok-file: THEORY-2188 — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CLAIM-818: Shared-kernel coupling does not make flow active

## The claim

Let z_i = h_θ(x_i) be the embeddings of N inputs and let the loss depend on
θ only through them, L(θ) = L(z_1(θ), …, z_N(θ)). Write g_i = ∇_(z_i) L and
J_i = ∂z_i/∂θ. Under gradient flow θ̇ = −∇_θ L = −Σ_j J_jᵀ g_j, so

ż_i = −Σ_j K_ij g_j, with K_ij = J_i J_jᵀ,

which is A29 §2's equation. Then

dL/dt = Σ_i g_iᵀ ż_i = −Σ_ij g_iᵀ J_i J_jᵀ g_j = −‖Σ_j J_jᵀ g_j‖² ≤ 0.

The block matrix K = [K_ij] is JJᵀ with J the stacked Jacobian, so it is
symmetric and positive semidefinite at every θ. The identity uses only the
value of K at the current instant, so it holds however K changes during
feature learning. The loss is therefore a Lyapunov function of the
embedding dynamics: they relax, they carry no sustained current, and
"particles move because the network learns, but the manner in which they can
move also changes" (A29 §2) is true without making the system active.

So where the strong active-matter reading of [CLAIM-798](CLAIM-798.md) needs broken detailed
balance or persistent driving, it has to come from outside the coupling:

- the optimizer: momentum makes the dynamics second order ([THEORY-779](../theory.d/THEORY-779.md)'s
  damped oscillators), and an adaptive preconditioner P_t replaces K by
  J P_t Jᵀ, still positive semidefinite while P_t is, so it too keeps the
  descent and adds activity only through its own memory and time
  dependence;
- noise whose covariance is not matched to the mobility, which is how
  SGD's probability currents arise in the quadratic approximation
  ([THEORY-209](../theory.d/THEORY-209.md));
- a changing objective or data stream, which makes L time dependent and
  the Lyapunov argument inapplicable.

A29's own reasoning, not shown on the share page, reached the same point
in words: "shared-kernel interactions may remain reciprocal and
gradient-based, while nonreciprocity or active currents require explicit
asymmetric dynamics, adaptive protocols, or anisotropic stochasticity".
This entry supplies the step.

**Checked.** The identity is two lines of algebra. It was also checked
numerically in this session (python3 -I): for a random two-layer tanh
network (20 inputs of dimension 6, 10 hidden units, embeddings of width 5,
squared loss), the finite-difference rate of change of L along the flow
matched −‖Σ_j J_jᵀ g_j‖² to 5 parts in 10¹¹, and the smallest eigenvalue of
the 100 × 100 matrix K was positive (6.7 × 10⁻⁵).

## What it does not say

- Not that training is an equilibrium process. Stochastic training has
  currents ([THEORY-209](../theory.d/THEORY-209.md)); the claim locates their source.
- Not that the representation's geometry is static. It moves and its
  coupling changes; it moves downhill.
- Not that a time-dependent objective, such as contrastive learning with
  fresh negatives each step, is active. That needs its own showing.

## Note of 2026-11-22: Cai and colleagues, read

Cai, Zhang, Liu and Shi ([LIT-2975](../literature.d/LIT-2975.md), [NOTE-2277](../notes.d/NOTE-2277.md), [THEORY-2188](../theory.d/THEORY-2188.md)): **consistent, a
parallel at the population level.** One energy functional with an
equilibrium for one modality, one joint energy for two: so nonequilibrium
behaviour would have to come from the optimizer or the noise, as this
claim says. The paper studies the objective, not the flow, so it is a
parallel and not evidence for the claim's identity. No relation.
